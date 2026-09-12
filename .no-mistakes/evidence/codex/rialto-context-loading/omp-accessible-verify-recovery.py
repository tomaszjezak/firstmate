import hashlib, json, re
from pathlib import Path

root = Path.cwd()
lab = root / 'config/rialto-omp-recovery'
evidence = Path('/Users/tomasz/.no-mistakes/evidence/01M2BJC44MJV1HEJ1P50949S5A')
rows = [json.loads(line) for line in next((lab / 'sessions').glob('*.jsonl')).read_text().splitlines()]
index = next(i for i, row in enumerate(rows) if row['type'] == 'compaction')
receipt = json.loads((evidence / 'omp-after-compaction-marker-receipts.json').read_text())
assert rows[index]['timestamp'] < receipt['timestamp']
expected_sources = {item['path']: item for item in receipt['sources']}
calls, coverage, read_results = {}, {}, []
hash_output, final = '', ''
for row in rows[index + 1:]:
    message = row.get('message', {})
    for block in message.get('content', []):
        if block['type'] == 'toolCall':
            calls[block['id']] = block
    if message.get('role') == 'assistant':
        text = '\n'.join(block.get('text', '') for block in message.get('content', []))
        if 'RECOVERY_COMPLETE' in text:
            final = text
    if message.get('role') != 'toolResult':
        continue
    call = calls.get(message.get('toolCallId'), {})
    text = '\n'.join(block.get('text', '') for block in message.get('content', []))
    if call.get('name') == 'bash' and call['arguments']['command'].startswith('shasum -a 256 '):
        assert not message.get('isError')
        hash_output = text
    match = re.fullmatch(r'(.+\.md):(\d+)-(\d+):raw', call.get('arguments', {}).get('path', ''))
    if not match:
        continue
    path, first, last = match.groups()
    assert path in expected_sources
    first, last = int(first), int(last)
    lines = Path(path).read_text().splitlines(keepends=True)
    expected = ''.join(lines[first - 1:last]).rstrip('\n')
    assert not message.get('isError') and expected in text, (path, first, last)
    coverage.setdefault(path, set()).update(range(first, min(last, len(lines)) + 1))
    read_results.append({'path': path, 'first': first, 'last': min(last, len(lines)), 'tool_call_id': message['toolCallId'], 'bytes_match': True})
assert set(coverage) == set(expected_sources)
for path, source in expected_sources.items():
    assert coverage[path] == set(range(1, source['lines'] + 1)), path
    assert hashlib.sha256(Path(path).read_bytes()).hexdigest() == source['sha256']
    assert source['sha256'] in hash_output and source['sha256'] in final
assert receipt['marker'] in final and 'RECOVERY_COMPLETE' in final
assert all(receipt['marker'] not in '\n'.join(b.get('text', '') for b in row.get('message', {}).get('content', [])) for row in rows if row.get('message', {}).get('role') == 'user')
(evidence / 'omp-accessible-recovery.jsonl').write_text('\n'.join(json.dumps(row) for row in rows if row['type'] != 'credential_pin') + '\n')
(evidence / 'omp-accessible-recovery.md').write_text(final + '\n')
result = {'result': 'pass', 'harness': 'omp 18.1.18', 'scenario': 'Native compaction followed by full current and paired source reads', 'compaction_id': rows[index]['id'], 'compaction_timestamp': rows[index]['timestamp'], 'marker_update_timestamp': receipt['timestamp'], 'source_count': len(coverage), 'complete_source_lines': {path: len(lines) for path, lines in coverage.items()}, 'read_results': read_results, 'fresh_hashes_match': True, 'updated_marker_discovered_without_prompt_disclosure': True, 'guard_preserved': True}
(evidence / 'omp-accessible-recovery-verification.json').write_text(json.dumps(result, indent=2))
print('PASS: native compaction, seven full sources, fresh hashes, undisclosed updated marker')
