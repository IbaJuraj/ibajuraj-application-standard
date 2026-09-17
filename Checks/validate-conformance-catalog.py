#!/usr/bin/env python3
from pathlib import Path
import json, re, sys

root = Path(__file__).resolve().parents[1]
cat = json.loads((root / 'CONFORMANCE_CATALOG.json').read_text(encoding='utf-8'))
meta = json.loads((root / 'standard.json').read_text(encoding='utf-8'))
errors = []

stable_version = meta.get('version')
stable_rule_count = meta.get('ruleCount')
stable_tag = meta.get('source', {}).get('stableReleaseTag') or meta.get('source', {}).get('releaseTag')
status = cat.get('status')
candidate = cat.get('candidate')
version = cat.get('standardVersion')

if cat.get('stableAuthority') != stable_version:
    errors.append(f'catalog stableAuthority must be {stable_version}')

if status == 'active':
    if version != stable_version:
        errors.append(f'active catalog standardVersion must be {stable_version}')
    if candidate is not None:
        errors.append('active catalog candidate must be null')
    if cat.get('proposedTag') != stable_tag:
        errors.append(f'active catalog tag must be {stable_tag}')
elif status == 'candidate':
    if not isinstance(candidate, str) or not candidate.strip():
        errors.append('candidate catalog must name a candidate, e.g. RC1')
    if version == stable_version:
        errors.append('candidate catalog must use a version newer than stableAuthority')
    if isinstance(version, str) and isinstance(candidate, str) and candidate.strip():
        expected_tag = f"standard-v{version}-{candidate.strip().lower()}"
        if cat.get('proposedTag') != expected_tag:
            errors.append(f'candidate catalog tag must be {expected_tag}')
else:
    errors.append("catalog status must be 'active' or 'candidate'")

ids = []
for rule in cat.get('rules', []):
    rid = rule.get('id', '')
    if not re.fullmatch(r'STD-[A-Z0-9-]+', rid):
        errors.append(f'invalid rule id: {rid}')
    if rid in ids:
        errors.append(f'duplicate rule id: {rid}')
    ids.append(rid)
    if rule.get('level') not in {'MUST', 'MUST NOT', 'SHOULD', 'SHOULD NOT', 'MAY'}:
        errors.append(f'{rid}: invalid level')
    if rule.get('defaultVerification', 'static') not in {'static', 'unit', 'ui', 'runtime', 'mixed'}:
        errors.append(f'{rid}: invalid verification')

text = (root / 'IBAJURAJ_APPLICATION_STANDARD.md').read_text(encoding='utf-8')
for rid in ids:
    if rid not in text:
        errors.append(f'{rid}: missing from main standard')
heading_ids = set(re.findall(r'^### (STD-[A-Z0-9-]+)', text, flags=re.M))
for rid in sorted(heading_ids - set(ids)):
    errors.append(f'{rid}: rule heading missing from catalog')

for rule in cat.get('rules', []):
    cond = rule.get('appliesWhen', 'always')
    if isinstance(cond, dict):
        allowed = {'capability', 'anyCapability', 'allCapabilities', 'bottomNavigationMode', 'equals', 'anyOf', 'allOf'}
        unknown = set(cond) - allowed
        if unknown:
            errors.append(f"{rule.get('id')}: unsupported appliesWhen keys {sorted(unknown)}")

if status == 'active' and isinstance(stable_rule_count, int) and len(ids) != stable_rule_count:
    errors.append(f'active catalog must contain {stable_rule_count} rules, got {len(ids)}')
if status == 'candidate' and isinstance(stable_rule_count, int) and len(ids) < stable_rule_count:
    errors.append(f'candidate catalog cannot contain fewer than stable {stable_rule_count} rules, got {len(ids)}')

if errors:
    print('FAIL – conformance catalog')
    for error in errors:
        print(' -', error)
    sys.exit(1)

label = f'{version} {candidate}' if status == 'candidate' else f'{version} stable'
print(f'PASS – conformance catalog {label} ({len(ids)} rules), stable authority {stable_version}')
