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
if version!='1.8.0': errors.append('STANDARD_VERSION != 1.8.0')
if meta.get('version')!='1.8.0': errors.append('standard.json version != 1.8.0')
if meta.get('status')!='release-candidate': errors.append('standard.json status != release-candidate')
if meta.get('rcDate')!='2026-09-05': errors.append('standard.json rcDate != 2026-09-05')
if meta.get('candidate')!='RC1': errors.append('standard.json candidate != RC1')
if meta.get('source',{}).get('releaseTag')!='standard-v1.8.0-rc1': errors.append('standard.json releaseTag != standard-v1.8.0-rc1')
required=[
 'IBAJURAJ_APPLICATION_STANDARD.md','DESIGN_TOKENS.md','REFERENCE_PATTERNS.md','TEST_MATRIX.md',
 'RELEASE_CHECKLIST.md','MIGRATION.md','CONFORMANCE_CATALOG.json','STANDARD_CONFORMANCE_TEMPLATE.json',
 'STANDARD_CONFORMANCE.schema.json','AUDIT_1.7.0_TO_1.8.0_RC1.md','RELEASE_NOTES_1.8.0_RC1.md',
 'ADOPTION_PLAN_1.8.0_RC1.md','RC1_STATIC_AUDIT_1.8.0.md',
 'Proposals/IJAS-0025-localization-first-architecture-and-territory-independence.md',
 'Proposals/IJAS-0026-release-package-root-hygiene-and-build-history-archive.md',
 'Proposals/IJAS-0027-single-device-development-release-data-continuity.md',
 'Proposals/IJAS-0028-production-backend-environment-readiness.md'
]
for f in required:
    if not (r/f).is_file(): errors.append(f'missing {f}')
for p in r.rglob('*'):
    if p.name=='.DS_Store' or 'xcuserdata' in p.parts or '__pycache__' in p.parts or p.suffix=='.pyc': errors.append(f'hygiene: {p}')
if errors:
    print('FAIL – standard package')
    [print(' -',e) for e in errors]
    sys.exit(1)
print('PASS – Standard 1.8.0 RC1 metadata and required files')
PY_INNER
python3 Checks/validate-conformance-catalog.py
