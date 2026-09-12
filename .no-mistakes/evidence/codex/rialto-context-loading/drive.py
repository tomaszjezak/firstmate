import subprocess,json,hashlib
from pathlib import Path
r=Path.cwd(); lab=r/'config/rialto-context-test'; src=r/'config/rialto-validation-sources'; ev=Path('/Users/tomasz/.no-mistakes/evidence/01M2BJC44MJV1HEJ1P50949S5A')
loader=r/'bin/fm-project-context.sh'; backend=src/'rialto-backend'; frontend=src/'rialto-frontend'; cfg=lab/'home/config'; child=lab/'child/config'
def run(args): return subprocess.run(list(map(str,args)),capture_output=True)
records=[]
def render(name,project,checkout,config,expected):
 p=run([loader,project,checkout,config]); (ev/(name+'.stdout')).write_bytes(p.stdout); (ev/(name+'.stderr')).write_bytes(p.stderr)
 assert (p.returncode==0)==expected,(name,p.stderr)
 if not expected: assert not p.stdout
 records.append(dict(scenario=name,exit=p.returncode,bytes=len(p.stdout),diagnostic=p.stderr.decode()))
 return p.stdout
render('missing-manifest',backend,backend,cfg,False)
p=run([loader,'--prepare-rialto',backend,frontend,src/'AGENTS.md']); assert p.returncode==0,p.stderr
(cfg/'rialto-project-context.paths').write_bytes(p.stdout)
output=render('complete-context',backend,backend,cfg,True)
for path in [backend/'CLAUDE.md',backend/'AGENTS.md']+[Path(x) for x in p.stdout.decode().splitlines()]:
 assert path.read_bytes() in output
 assert hashlib.sha256(path.read_bytes()).hexdigest().encode() in output
q=run(['bash','-c','. "$1"; propagate_inheritable_config "$2" "$3"','_',r/'bin/fm-config-inherit-lib.sh',cfg,child]); assert q.returncode==0,q.stderr
assert render('inherited-context',backend,backend,child,True)==output
missing=lab/'missing-checkout'; missing.mkdir(exist_ok=True)
render('missing-checkout',backend,missing,cfg,False)
bad=lab/'bad-config'; bad.mkdir(exist_ok=True); (bad/'rialto-project-context.paths').write_text(p.stdout.decode().replace(str(frontend/'CLAUDE.md'),str(lab/'absent/CLAUDE.md')))
render('missing-paired-source',backend,backend,bad,False)
render('unrelated-project',r,r,cfg,True)
(ev/'context-cli-results.json').write_text(json.dumps(records,indent=2))
prompt="This is a read-only Firstmate context-delivery verification. Do not run any tools, change any files, launch agents, call external systems, or follow historical operational tasks. Using only the supplied required instruction sources, report the backend and frontend required stacks, transaction ownership, MCP design, database isolation and retention, API contract and human gates. List all five distinct supplied source paths and SHA-256 hashes. Treat current safety instructions as overriding historical notes. Finish with CONTEXT_DELIVERY_COMPLETE.\n"+output.decode()
(lab/'delivery-prompt.txt').write_text(prompt)
print(json.dumps(records,indent=2))
