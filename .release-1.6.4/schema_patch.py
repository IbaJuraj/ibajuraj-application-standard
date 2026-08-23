from pathlib import Path
import json

p = Path('standard.schema.json')
data = json.loads(p.read_text(encoding='utf-8'))
contracts = data['properties']['contracts']
for key in ('componentFamilyGeometry', 'featureMaturity', 'visualConsistency'):
    if key not in contracts['required']:
        contracts['required'].append(key)
contracts['properties']['componentFamilyGeometry'] = {
    'const': 'shared-role-shared-geometry-explicit-semantic-exceptions'
}
contracts['properties']['featureMaturity'] = {
    'const': 'unfinished-experimental-capabilities-not-equal-user-facing-modes'
}
contracts['properties']['visualConsistency'] = {
    'const': 'whole-app-component-family-localization-dynamic-type-audit'
}
p.write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
print('Patched standard.schema.json for 1.6.4 contracts')
