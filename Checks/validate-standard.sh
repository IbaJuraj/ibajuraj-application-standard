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
if meta.get('candidate')!='RC2': errors.append('standard.json candidate != RC2')
required=['IBAJURAJ_APPLICATION_STANDARD.md','DESIGN_TOKENS.md','REFERENCE_PATTERNS.md','TEST_MATRIX.md','RELEASE_CHECKLIST.md','MIGRATION.md','CONFORMANCE_CATALOG.json','STANDARD_CONFORMANCE_TEMPLATE.json','STANDARD_CONFORMANCE.schema.json','AUDIT_1.6.4_TO_1.7.0.md','AUDIT_RC1_TO_RC2.md','RELEASE_NOTES_1.7.0.md','ADOPTION_PLAN_RC2.md','RC2_STATIC_AUDIT.md']
for f in required:
    if not (r/f).is_file(): errors.append(f'missing {f}')
for p in r.rglob('*'):
    if p.name=='.DS_Store' or 'xcuserdata' in p.parts or '__pycache__' in p.parts or p.suffix=='.pyc': errors.append(f'hygiene: {p}')
if errors:
    print('FAIL – standard package')
    [print(' -',e) for e in errors]
    sys.exit(1)
print('PASS – standard package metadata and required files')
PY_INNER
python3 Checks/validate-conformance-catalog.py
