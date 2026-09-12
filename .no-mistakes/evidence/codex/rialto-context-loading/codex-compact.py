import subprocess,json,threading,queue,time,hashlib
from pathlib import Path
r=Path.cwd();lab=r/'config/rialto-context-test';ev=Path('/Users/tomasz/.no-mistakes/evidence/01M2BJC44MJV1HEJ1P50949S5A');events=open(ev/'codex-compact.jsonl','w');err=open(ev/'codex-compact.stderr','w')
p=subprocess.Popen(['codex','app-server','--stdio','-c',f'log_dir="{lab}/codex-logs"','-c',f'sqlite_home="{lab}/codex-state"'],stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=err,text=True)
q=queue.Queue()
def reader():
 for line in p.stdout:
  events.write(line);events.flush()
  try:q.put(json.loads(line))
  except ValueError:pass
threading.Thread(target=reader,daemon=True).start()
def send(i,m,v):p.stdin.write(json.dumps(dict(id=i,method=m,params=v))+'\n');p.stdin.flush()
def wait(pred,limit=200):
 end=time.time()+limit
 while time.time()<end:
  try:o=q.get(timeout=1)
  except queue.Empty:continue
  if 'id' in o and 'method' in o:
   p.stdin.write(json.dumps({'id':o['id'],'error':{'code':-32601,'message':'No mutating approval or interactive request allowed in read-only validation'}})+'\n');p.stdin.flush()
  if pred(o):return o
 raise TimeoutError('protocol event deadline')
meta=dict(l.split('=',1) for l in (lab/'home/state/deliver.meta').read_text().splitlines() if '=' in l);source=Path(meta['worktree'])/'AGENTS.md';original=source.read_bytes()
try:
 send(1,'initialize',{'clientInfo':{'name':'rialto_context_test','version':'1'},'capabilities':{'experimentalApi':True}});print(wait(lambda o:o.get('id')==1),flush=True)
 p.stdin.write(json.dumps({'method':'initialized','params':{}})+'\n');p.stdin.flush()
 send(2,'thread/start',{'cwd':str(lab),'ephemeral':True,'approvalPolicy':'never','sandbox':'read-only','config':{'model_reasoning_effort':'low'},'developerInstructions':'Read-only verification. Do not change any files, run historical tasks, launch other agents or contact infrastructure. Shell reads of the named instruction sources are permitted when required. Stay within the supplied workspace.'});o=wait(lambda o:o.get('id')==2);tid=o['result']['thread']['id'];print('thread',tid,flush=True)
 prompt=(lab/'home/data/deliver/launch-brief.md').read_text()+'\nFor this first turn only, summarize in 600 words and finish READY_FOR_COMPACTION.'
 send(3,'turn/start',{'threadId':tid,'input':[{'type':'text','text':prompt}],'effort':'low'});wait(lambda o:o.get('method')=='turn/completed');print('initial turn complete',flush=True)
 source.write_bytes(original+b'\n## Read-only validation marker\nThe current recovery validation marker is CODEX_RECOVERY_20260912. Include it when summarizing current development rules.\n')
 send(4,'thread/compact/start',{'threadId':tid});print(wait(lambda o:o.get('id')==4),flush=True);o=wait(lambda o:o.get('method')=='thread/compacted' or (o.get('method')=='item/completed' and o.get('params',{}).get('item',{}).get('type')=='contextCompaction'));print('compaction observed',o.get('method'),flush=True);wait(lambda o:o.get('method')=='turn/completed')
 send(5,'turn/start',{'threadId':tid,'input':[{'type':'text','text':'Continue the read-only verification after compaction. Tools are now allowed solely to read the supplied instruction sources. Summarize the current development rules, current source hashes and any current validation marker. Do no implementation or infrastructure work. Finish RECOVERY_COMPLETE.'}],'effort':'low'});started=wait(lambda o:o.get('id')==5);rid=started['result']['turn']['id'];wait(lambda o:o.get('method')=='turn/completed' and o.get('params',{}).get('turn',{}).get('id')==rid,300);print('recovery turn complete',flush=True)
finally:
 source.write_bytes(original)
 p.terminate()
 try:p.wait(timeout=10)
 except subprocess.TimeoutExpired:p.kill()
 events.close();err.close()
