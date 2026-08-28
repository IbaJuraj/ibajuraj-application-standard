#!/usr/bin/env python3
from pathlib import Path
import json, re, sys
root=Path(__file__).resolve().parents[1]
cat=json.loads((root/'CONFORMANCE_CATALOG.json').read_text(encoding='utf-8'))
errors=[]
if cat.get('standardVersion')!='1.7.0': errors.append('catalog standardVersion must be 1.7.0')
ids=[]
for r in cat.get('rules',[]):
    rid=r.get('id','')
    if not re.fullmatch(r'STD-[A-Z0-9-]+', rid): errors.append(f'invalid rule id: {rid}')
    if rid in ids: errors.append(f'duplicate rule id: {rid}')
    ids.append(rid)
    if r.get('level') not in {'MUST','MUST NOT','SHOULD','SHOULD NOT','MAY'}: errors.append(f'{rid}: invalid level')
    if r.get('defaultVerification') not in {'static','unit','ui','runtime','mixed'}: errors.append(f'{rid}: invalid verification')
text=(root/'IBAJURAJ_APPLICATION_STANDARD.md').read_text(encoding='utf-8')
for rid in ids:
    if rid not in text: errors.append(f'{rid}: missing from main standard')
if errors:
    print('FAIL – conformance catalog')
    for e in errors: print(' -',e)
    sys.exit(1)
print(f'PASS – conformance catalog ({len(ids)} rules)')
