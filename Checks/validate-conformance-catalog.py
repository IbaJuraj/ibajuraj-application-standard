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
    if not isinstance(rule.get('title'),str) or not rule['title'].strip():
        errors.append(f'{rid}: missing human-readable title')
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

template=json.loads((root/'STANDARD_CONFORMANCE_TEMPLATE.json').read_text(encoding='utf-8'))
cap_keys=set(template.get('capabilities',{}))
allowed_phases={'development','release-candidate','post-release'}
def validate_condition(condition, rid):
    if condition == 'always': return
    if not isinstance(condition,dict):
        errors.append(f'{rid}: invalid applicability condition')
        return
    allowed={'capability','anyCapability','allCapabilities','bottomNavigationMode','equals','anyOf','allOf','phase'}
    unknown=set(condition)-allowed
    if unknown: errors.append(f'{rid}: unsupported appliesWhen keys {sorted(unknown)}')
    keys=set(condition)&{'capability','anyCapability','allCapabilities','bottomNavigationMode','anyOf','allOf','phase'}
    if len(keys)!=1:
        errors.append(f'{rid}: condition must have exactly one operator; combine using anyOf/allOf')
        return
    if 'phase' in condition:
        if condition['phase'] not in allowed_phases: errors.append(f'{rid}: invalid phase')
    if 'capability' in condition:
        if condition['capability'] not in cap_keys: errors.append(f'{rid}: capability missing from conformance template: {condition["capability"]}')
        if type(condition.get('equals')) is not bool: errors.append(f'{rid}: capability condition requires Boolean equals')
    for key in ('anyCapability','allCapabilities'):
        if key in condition:
            names=condition[key]
            if not isinstance(names,list) or not names or any(not isinstance(n,str) or n not in cap_keys for n in names):
                errors.append(f'{rid}: unsupported/empty {key} capabilities')
    if 'bottomNavigationMode' in condition and condition['bottomNavigationMode'] not in {'none','native','custom'}:
        errors.append(f'{rid}: invalid bottomNavigationMode')
    for key in ('anyOf','allOf'):
        if key in condition:
            parts=condition[key]
            if not isinstance(parts,list) or not parts:
                errors.append(f'{rid}: empty/invalid {key}')
            else:
                for part in parts: validate_condition(part,rid)

for rule in cat.get('rules', []):
    validate_condition(rule.get('appliesWhen','always'),rule.get('id','<unknown>'))
    if rule.get('releaseBlocking') is False and rule.get('level') in ('MUST','MUST NOT'):
        condition=rule.get('appliesWhen','always')
        # Normative obligation can be nonblocking *before* release only for a post-release gate.
        if rule.get('id')!='STD-POSTRELEASE-001' or 'post-release' not in json.dumps(condition):
            errors.append(f"{rule.get('id')}: MUST cannot be non-blocking outside post-release")

declared_rule_count = cat.get('ruleCount')
if declared_rule_count is not None and declared_rule_count != len(ids):
    errors.append(f'catalog ruleCount must equal actual rules: declared {declared_rule_count}, got {len(ids)}')

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
