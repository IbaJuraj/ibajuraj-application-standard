#!/usr/bin/env python3
from pathlib import Path
import json, re, sys
root=Path(__file__).resolve().parents[1]
cat=json.loads((root/'CONFORMANCE_CATALOG.json').read_text(encoding='utf-8'))
errors=[]
if cat.get('standardVersion')!='1.7.0': errors.append('catalog standardVersion must be 1.7.0')
if cat.get('status')!='active': errors.append('catalog status must be active')
if cat.get('candidate') not in (None, ''): errors.append('catalog candidate marker must be cleared')
ids=[]
for r in cat.get('rules',[]):
    rid=r.get('id','')
    if not re.fullmatch(r'STD-[A-Z0-9-]+', rid): errors.append(f'invalid rule id: {rid}')
    if rid in ids: errors.append(f'duplicate rule id: {rid}')
    ids.append(rid)
    if r.get('level') not in {'MUST','MUST NOT','SHOULD','SHOULD NOT','MAY'}: errors.append(f'{rid}: invalid level')
    if r.get('defaultVerification','static') not in {'static','unit','ui','runtime','mixed'}: errors.append(f'{rid}: invalid verification')
text=(root/'IBAJURAJ_APPLICATION_STANDARD.md').read_text(encoding='utf-8')
for rid in ids:
    if rid not in text: errors.append(f'{rid}: missing from main standard')
heading_ids=set(re.findall(r'^### (STD-[A-Z0-9-]+)', text, flags=re.M))
for rid in sorted(heading_ids-set(ids)):
    errors.append(f'{rid}: rule heading missing from catalog')
for r in cat.get('rules',[]):
    cond=r.get('appliesWhen','always')
    if isinstance(cond,dict):
        allowed={'capability','anyCapability','allCapabilities','bottomNavigationMode','equals','anyOf','allOf'}
        unknown=set(cond)-allowed
        if unknown: errors.append(f"{r.get('id')}: unsupported appliesWhen keys {sorted(unknown)}")
if errors:
    print('FAIL – conformance catalog')
    for e in errors: print(' -',e)
    sys.exit(1)
print(f'PASS – conformance catalog 1.7.0 ({len(ids)} rules)')
