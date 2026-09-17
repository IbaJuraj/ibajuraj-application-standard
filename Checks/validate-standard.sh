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
cat=json.loads((r/'CONFORMANCE_CATALOG.json').read_text())

# standard.json / STANDARD_VERSION continue to describe the current stable
# public authority even while a newer RC candidate is being reviewed.
if version!='1.8.0': errors.append('STANDARD_VERSION != 1.8.0')
if meta.get('version')!='1.8.0': errors.append('standard.json version != 1.8.0')
if meta.get('status')!='active': errors.append('standard.json status != active')
if meta.get('candidate') is not None: errors.append('standard.json candidate must be null')
if meta.get('stableAuthority')!='1.8.0': errors.append('stableAuthority != 1.8.0')
if meta.get('ruleCount')!=119: errors.append('stable ruleCount != 119')
if meta.get('source',{}).get('releaseTag')!='standard-v1.8.0': errors.append('stable releaseTag != standard-v1.8.0')

required=['IBAJURAJ_APPLICATION_STANDARD.md','DESIGN_TOKENS.md','REFERENCE_PATTERNS.md','TEST_MATRIX_1.8.0.md','RELEASE_CHECKLIST_1.8.0.md','MIGRATION_1.8.0.md','CONFORMANCE_CATALOG.json','STANDARD_CONFORMANCE_TEMPLATE.json','STANDARD_CONFORMANCE.schema.json','RELEASE_NOTES_1.8.0.md','RC1_INTEGRATION_GAP_AUDIT.md','RC2_STATIC_AUDIT.md']
for f in required:
    if not (r/f).is_file(): errors.append(f'missing {f}')
for k in ['testMatrix','releaseChecklist','migration','releaseNotes','integrationGapAudit']:
    p=meta.get('documents',{}).get(k)
    if not p or not (r/p).is_file(): errors.append(f'document pointer {k} invalid: {p}')

# Candidate-specific companion documents are validated without replacing the
# stable metadata authority until promotion.
if cat.get('status')=='candidate':
    candidate=cat.get('candidate')
    candidate_version=cat.get('standardVersion')
    if not candidate or not candidate_version:
        errors.append('candidate catalog metadata incomplete')
    else:
        candidate_docs=[
            f'MIGRATION_{candidate_version}_{candidate}.md',
            f'RELEASE_NOTES_{candidate_version}_{candidate}.md',
            f'TEST_MATRIX_{candidate_version}_{candidate}.md',
            f'RELEASE_CHECKLIST_{candidate_version}_{candidate}.md',
        ]
        for f in candidate_docs:
            if not (r/f).is_file(): errors.append(f'missing {f}')
    if cat.get('stableAuthority') != meta.get('version'):
        errors.append('candidate stableAuthority must match standard.json stable version')

for p in r.rglob('*'):
    if p.name=='.DS_Store' or 'xcuserdata' in p.parts or '__pycache__' in p.parts or p.suffix=='.pyc': errors.append(f'hygiene: {p}')
if errors:
    print('FAIL – standard package')
    [print(' -',e) for e in errors]
    sys.exit(1)

if cat.get('status')=='candidate':
    print(f"PASS – Stable {meta.get('version')} authority + candidate {cat.get('standardVersion')} {cat.get('candidate')} package metadata")
else:
    print(f"PASS – Standard {meta.get('version')} stable metadata and required files")
PY_INNER
python3 Checks/validate-conformance-catalog.py
