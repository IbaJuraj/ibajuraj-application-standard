#!/bin/bash
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"
python3 - <<'PY_INNER'
from pathlib import Path
import json, sys
r=Path('.')
errors=[]
version=(r/'STANDARD_VERSION').read_text().strip()
meta=json.loads((r/'standard.json').read_text())
if version!='1.7.0': errors.append('STANDARD_VERSION != 1.7.0')
if meta.get('version')!='1.7.0': errors.append('standard.json version != 1.7.0')
if meta.get('status')!='active': errors.append('standard.json status != active')
if meta.get('releasedAt')!='2026-09-02': errors.append('standard.json releasedAt != 2026-09-02')
if meta.get('candidate') not in (None, ''): errors.append('standard.json candidate marker must be cleared')
if meta.get('source',{}).get('releaseTag')!='standard-v1.7.0': errors.append('standard.json releaseTag != standard-v1.7.0')
required=['IBAJURAJ_APPLICATION_STANDARD.md','DESIGN_TOKENS.md','REFERENCE_PATTERNS.md','TEST_MATRIX.md','RELEASE_CHECKLIST.md','MIGRATION.md','CONFORMANCE_CATALOG.json','STANDARD_CONFORMANCE_TEMPLATE.json','STANDARD_CONFORMANCE.schema.json','AUDIT_1.6.4_TO_1.7.0.md','AUDIT_RC2_TO_RC3.md','RELEASE_NOTES_1.7.0.md','ADOPTION_PLAN_RC3.md','RC3_STATIC_AUDIT.md','FINAL_RELEASE_AUDIT_1.7.0.md']
for f in required:
    if not (r/f).is_file(): errors.append(f'missing {f}')
for p in r.rglob('*'):
    if p.name=='.DS_Store' or 'xcuserdata' in p.parts or '__pycache__' in p.parts or p.suffix=='.pyc': errors.append(f'hygiene: {p}')
if errors:
    print('FAIL – standard package')
    [print(' -',e) for e in errors]
    sys.exit(1)
print('PASS – Standard 1.7.0 active metadata and required files')
PY_INNER
python3 Checks/validate-conformance-catalog.py
