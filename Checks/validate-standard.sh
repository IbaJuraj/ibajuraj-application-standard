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
if version!='1.8.0-rc2': errors.append('STANDARD_VERSION != 1.8.0-rc2')
if meta.get('version')!='1.8.0': errors.append('standard.json version != 1.8.0')
if meta.get('status')!='release-candidate': errors.append('standard.json status != release-candidate')
if meta.get('candidate')!='RC2': errors.append('standard.json candidate != RC2')
if meta.get('stableAuthority')!='1.7.0': errors.append('stableAuthority != 1.7.0')
if meta.get('ruleCount')!=119: errors.append('ruleCount != 119')
if meta.get('source',{}).get('releaseTag')!='standard-v1.8.0-rc2': errors.append('releaseTag != standard-v1.8.0-rc2')
required=['IBAJURAJ_APPLICATION_STANDARD.md','DESIGN_TOKENS.md','REFERENCE_PATTERNS.md','TEST_MATRIX_1.8.0_RC2.md','RELEASE_CHECKLIST_1.8.0_RC2.md','MIGRATION_1.8.0_RC1_TO_RC2.md','CONFORMANCE_CATALOG.json','STANDARD_CONFORMANCE_TEMPLATE.json','STANDARD_CONFORMANCE.schema.json','RELEASE_NOTES_1.8.0_RC2.md','ADOPTION_PLAN_RC2.md','RC1_INTEGRATION_GAP_AUDIT.md','RC2_STATIC_AUDIT.md']
for f in required:
    if not (r/f).is_file(): errors.append(f'missing {f}')
for k in ['testMatrix','releaseChecklist','migration','releaseNotes','integrationGapAudit']:
    p=meta.get('documents',{}).get(k)
    if not p or not (r/p).is_file(): errors.append(f'document pointer {k} invalid: {p}')
for p in r.rglob('*'):
    if p.name=='.DS_Store' or 'xcuserdata' in p.parts or '__pycache__' in p.parts or p.suffix=='.pyc': errors.append(f'hygiene: {p}')
if errors:
    print('FAIL – standard package')
    [print(' -',e) for e in errors]
    sys.exit(1)
print('PASS – Standard 1.8.0 RC2 candidate metadata and required files')
PY_INNER
python3 Checks/validate-conformance-catalog.py
