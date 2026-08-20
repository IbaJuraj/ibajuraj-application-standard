#!/usr/bin/env python3
from pathlib import Path
import json, hashlib

OLD='1.6.1'; NEW='1.6.2'; DATE='2026-08-20'

def read(path): return Path(path).read_text(encoding='utf-8')
def write(path, text): Path(path).write_text(text, encoding='utf-8')

# Canonical metadata
write('STANDARD_VERSION', NEW+'\n')
d=json.loads(read('standard.json')); d['version']=NEW; d['releasedAt']=DATE; d['source']['tag']=f'standard-v{NEW}'; write('standard.json', json.dumps(d, ensure_ascii=False, indent=2)+'\n')

# Version-bearing documents only; do not rewrite historical section labels.
for path in ['IBAJURAJ_APPLICATION_STANDARD.md','DESIGN_TOKENS.md','SUPPORT_AND_LINKS.md']:
    s=read(path).replace(f'**Verzia:** {OLD}', f'**Verzia:** {NEW}')
    write(path,s)

# Standard validity date and Header Family Alignment Contract.
p='IBAJURAJ_APPLICATION_STANDARD.md'; s=read(p).replace('**Platnosť od:** 19. augusta 2026','**Platnosť od:** 20. augusta 2026')
needle='- Všetky primárne rooty v rámci jednej aplikácie MUST ukotviť hlavný root nadpis na rovnakej vertikálnej baseline voči safe-area/root content anchoru. Root title a pravá systémová header akcia MUST používať spoločný top inset a rovnakú header geometriu; prepnutie medzi tabmi nesmie spôsobovať viditeľné vertikálne „skákanie“ nadpisu alebo Settings akcie.\n'
addition='''- Obrazovky, ktoré používajú rovnaký produktový header pattern, MUST používať spoločnú **header family geometriu** aj vtedy, keď jedna obrazovka je root a druhá je vnorená alebo obsahuje Back akciu. Prítomnosť leading Back akcie MUST NOT svojvoľne posunúť title/subtitle pár ani pravú systémovú akciu oproti referenčnej obrazovke rovnakej rodiny.\n- Header family SHOULD byť implementovaná jedným zdieľaným komponentom alebo jednou sadou tokenov; lokálne hardcoded `padding(.top)`, `offset(y:)`, vlastné safe-area kompenzácie alebo per-screen konštanty MUST NOT byť primárnym mechanizmom zarovnania, ak existuje spoločný header pattern.\n- Ak produkt určí referenčný root header (typicky Home), ostatné obrazovky rovnakej header family MUST pri rovnakom size class, Dynamic Type a orientation zachovať rovnaký top anchor, title baseline a trailing-action baseline, pokiaľ zdokumentovaná výnimka nevyžaduje odlišnú geometriu.\n'''
if 'header family geometriu' not in s:
    assert needle in s
    s=s.replace(needle, needle+addition)
write(p,s)

# Design tokens
p='DESIGN_TOKENS.md'; s=read(p).replace('**Platnosť od:** 19. augusta 2026','**Platnosť od:** 20. augusta 2026')
needle='| `appPage.rootHeaderBaseline` | rovnaká vertikálna baseline na všetkých primárnych rootoch produktu | `semantic` |\n'
addition='''| `appPage.headerFamilyTopAnchor` | spoločný safe-area/root content anchor pre obrazovky rovnakej header family | `semantic` |\n| `appPage.headerFamilyTitleBaseline` | rovnaká title baseline v rámci header family pri rovnakom prostredí | `semantic` |\n| `appPage.headerFamilyTrailingBaseline` | rovnaká baseline/centerline trailing systémovej akcie v rámci header family | `semantic` |\n| `appPage.headerLeadingSlotMinimum` | 44 pt | `minimum` |\n'''
if 'appPage.headerFamilyTopAnchor' not in s:
    assert needle in s
    s=s.replace(needle, needle+addition)
write(p,s)

# README
p='README.md'; s=read(p).replace(f'Aktuálna verzia: **{OLD}**',f'Aktuálna verzia: **{NEW}**')
s=s.replace(f'standard-v{OLD}',f'standard-v{NEW}').replace(f'**IbaJuraj Application Standard {OLD}**',f'**IbaJuraj Application Standard {NEW}**')
anchor='Stav: **finálne vydanie**\n'
note='\nNajnovší patch 1.6.2 dopĺňa Header Family Alignment Contract: rovnaký produktový header musí zachovať top anchor, title baseline a trailing-action baseline naprieč root aj vnorenými obrazovkami bez lokálnych hardcoded offsetov.\n'
if 'Najnovší patch 1.6.2' not in s: s=s.replace(anchor, anchor+note)
if '### Nové v 1.6.2' not in s:
    insert='''\n### Nové v 1.6.2\n\nVerzia 1.6.2 dopĺňa Header Family Alignment Contract. Obrazovky používajúce rovnaký produktový header musia zachovať spoločný top anchor, title baseline a trailing-action baseline aj vtedy, keď jedna z nich obsahuje Back akciu. Zdieľaný header sa nemá dorovnávať lokálnymi hardcoded top offsetmi.\n'''
    s=s.replace('### Nové v 1.6.1', insert+'\n### Nové v 1.6.1') if '### Nové v 1.6.1' in s else s.replace('### Nové v 1.6.0', insert+'\n### Nové v 1.6.0')
write(p,s)

# Adoption template
p='Templates/APP_STANDARD_ADOPTION.md'; s=read(p).replace(f'**Adopted standard:** {OLD}',f'**Adopted standard:** {NEW}').replace(f'standard-v{OLD}',f'standard-v{NEW}'); write(p,s)

# Changelog
p='CHANGELOG.md'; s=read(p)
entry='''## 1.6.2 – 2026-08-20\n\n### Added\n- Header Family Alignment Contract pre obrazovky používajúce rovnaký produktový header pattern, vrátane root a vnorených obrazoviek.\n- semantic tokeny `appPage.headerFamilyTopAnchor`, `appPage.headerFamilyTitleBaseline`, `appPage.headerFamilyTrailingBaseline` a minimálny leading slot.\n- runtime parity gate, ktorý porovná referenčný header s ďalšou obrazovkou rovnakej rodiny.\n\n### Changed\n- prítomnosť Back akcie nesmie svojvoľne meniť vertikálnu polohu title/subtitle páru ani trailing Settings/system action,\n- lokálne hardcoded top padding/offset/safe-area kompenzácie nesmú nahrádzať spoločnú header geometriu, ak existuje zdieľaný pattern.\n\n### Compatibility\n- spätne kompatibilný PATCH release bez migrácie doménových používateľských dát,\n- aplikácie musia skontrolovať iba obrazovky, ktoré zdieľajú rovnaký header pattern, ale používajú rozdielne lokálne odsadenia.\n\n'''
if '## 1.6.2 –' not in s: s=s.replace('# Changelog – IbaJuraj Application Standard\n\n','# Changelog – IbaJuraj Application Standard\n\n'+entry)
write(p,s)

# Migration, tests, checklist, reference patterns
p='MIGRATION.md'; s=read(p)
if '## Migrácia 1.6.1 → 1.6.2' not in s:
    s += '''\n## Migrácia 1.6.1 → 1.6.2\n\nIde o prezentačný PATCH bez migrácie používateľských dát.\n\n1. Identifikujte obrazovky používajúce rovnaký produktový header pattern (napr. Home a vnorené search/assistant obrazovky).\n2. Odstráňte lokálne `padding(.top)`, `offset(y:)` a vlastné safe-area kompenzácie, ktoré menia baseline rovnakého headeru.\n3. Presuňte geometriu do zdieľaného header komponentu alebo tokenov `appPage.headerFamily.*`.\n4. Back akciu implementujte v stabilnom leading slote bez posunu title/trailing action.\n5. Runtime porovnajte referenčný root a aspoň jednu vnorenú obrazovku v Light/Dark a pri podporovanom Dynamic Type.\n'''
write(p,s)

p='TEST_MATRIX.md'; s=read(p)
if '## Header Family Alignment Gate (1.6.2)' not in s:
    s += '''\n## Header Family Alignment Gate (1.6.2)\n\n- [ ] Referenčný root a peer/nested screen rovnakej header family majú rovnaký top anchor a title baseline.\n- [ ] Trailing Settings/system action nemení vertikálnu polohu medzi peer obrazovkami.\n- [ ] Leading Back akcia neposúva title/subtitle ani trailing action.\n- [ ] Test prebehne aspoň v Light a Dark režime.\n- [ ] Pri podporovanom väčšom Dynamic Type nevznikne kolízia, prekrývanie ani improvizovaný per-screen offset.\n- [ ] Source audit neodhalí lokálne hardcoded top offsety na obrazovkách, ktoré majú zdieľať spoločný header pattern.\n'''
write(p,s)

p='RELEASE_CHECKLIST.md'; s=read(p).replace(f'# IbaJuraj Standard {OLD} – release checklist',f'# IbaJuraj Standard {NEW} – release checklist').replace(f'standard-v{OLD}',f'standard-v{NEW}')
if '### Header family alignment (1.6.2)' not in s:
    s += '''\n### Header family alignment (1.6.2)\n- [ ] Root a vnorené obrazovky rovnakej header family používajú spoločnú geometriu.\n- [ ] Nadpis a trailing systémová akcia vizuálne neskáču medzi peer obrazovkami.\n- [ ] Back akcia nemení top anchor title/subtitle páru.\n- [ ] Neexistuje per-screen hardcoded top offset tam, kde má byť použitý spoločný header component/token.\n'''
write(p,s)

p='REFERENCE_PATTERNS.md'; s=read(p).replace('# IbaJuraj Standard 1.6.1 – referenčné vzory','# IbaJuraj Standard 1.6.2 – referenčné vzory')
if '## Header family alignment' not in s:
    s += '''\n## Header family alignment\n\nPoužite jeden spoločný header pattern pre obrazovky, ktoré majú rovnakú vizuálnu identitu, aj keď niektoré obsahujú Back akciu.\n\n```text\n[leading slot / Back]   [title + subtitle anchor]   [trailing Settings/action]\n                         ↑ rovnaká baseline          ↑ rovnaká centerline\n```\n\n- Home alebo iný určený root môže byť referenčnou geometriou.\n- Back akcia obsadí leading slot; nesmie posúvať title ani trailing action smerom nadol.\n- Nepoužívajte per-screen `padding(.top)` alebo `offset(y:)` na vizuálne dorovnávanie rovnakej header family.\n- Runtime parity kontrola porovná referenčný root s aspoň jednou vnorenou obrazovkou rovnakej rodiny v Light/Dark a pri podporovanom Dynamic Type.\n'''
write(p,s)

# Release notes and proposal
write('RELEASE_NOTES_1.6.2.md','''# IbaJuraj Application Standard 1.6.2\n\n**Dátum vydania:** 20. august 2026  \n**Typ:** PATCH  \n**Kompatibilita:** spätne kompatibilná; bez migrácie doménových používateľských dát\n\n## Prečo táto verzia vznikla\n\nRuntime audit ukázal opakujúci sa problém: dve obrazovky môžu používať rovnaký vizuálny header, ale nadpis alebo pravá Settings akcia sú vertikálne posunuté, pretože každá obrazovka používa vlastný top padding alebo safe-area kompenzáciu. Verzia 1.6.2 tento rozdiel explicitne zakazuje pre jednu header family.\n\n## Hlavné zmeny\n\n- Header Family Alignment Contract pre root aj vnorené obrazovky,\n- spoločný top anchor, title baseline a trailing-action baseline,\n- stabilný leading slot pre Back akciu bez posunu ostatných prvkov,\n- zákaz lokálnych hardcoded top offsetov ako primárneho mechanizmu zarovnania zdieľaného headeru,\n- nové `appPage.headerFamily.*` semantic tokeny,\n- runtime parity gate v Light/Dark a pri podporovanom Dynamic Type.\n\n## Adopcia\n\nPrechod z 1.6.1 na 1.6.2 nevyžaduje migráciu používateľských dát. Aplikácia má skontrolovať obrazovky, ktoré používajú rovnaký produktový header pattern, a zjednotiť ich geometriu cez spoločný komponent alebo tokeny.\n''')
Path('Proposals/IJAS-0012-header-family-alignment-contract.md').write_text('''# IJAS-0012 – Header Family Alignment Contract\n\n**Status:** Implemented  \n**Target:** 1.6.2  \n**Date:** 2026-08-20\n\n## Problem\n\nRovnaký produktový header sa môže na rôznych obrazovkách vertikálne posúvať, najmä ak jedna obrazovka obsahuje Back akciu a iná nie. Lokálne `padding(.top)`, `offset(y:)` a individuálne safe-area kompenzácie vedú k viditeľnému skákaniu title a trailing Settings/system action.\n\n## Decision\n\nObrazovky rovnakej header family používajú spoločný top anchor, title baseline a trailing-action baseline. Leading Back akcia obsadí stabilný slot a nesmie meniť geometriu ostatných prvkov. Zdieľaný komponent alebo tokeny sú preferovaným zdrojom pravdy.\n\n## Verification\n\nRuntime audit porovná referenčný root a peer/nested screen rovnakej rodiny v Light/Dark a pri podporovanom Dynamic Type. Source audit hľadá lokálne hardcoded top offsety na obrazovkách, ktoré majú zdieľať spoločný header pattern.\n''',encoding='utf-8')
p='Proposals/README.md'; s=read(p)
if 'IJAS-0012-header-family-alignment-contract.md' not in s: s += '\n- `IJAS-0012-header-family-alignment-contract.md` – Header Family Alignment Contract (implemented in Standard 1.6.2)\n'
write(p,s)

# Validator requires release proposal and new contracts.
p='Checks/validate-standard.sh'; s=read(p)
if 'Proposals/IJAS-0012-header-family-alignment-contract.md' not in s:
    s=s.replace('  "Proposals/IJAS-0009-neutral-surface-and-text-color-contract.md"\n','  "Proposals/IJAS-0009-neutral-surface-and-text-color-contract.md"\n  "Proposals/IJAS-0012-header-family-alignment-contract.md"\n')
    s=s.replace('        r"secondarySystemGroupedBackground",\n','        r"secondarySystemGroupedBackground",\n        r"header family geometriu",\n        r"hardcoded `padding\\(\\.top\\)`",\n')
    s=s.replace('        r"color\\.textSecondary",\n','        r"color\\.textSecondary",\n        r"appPage\\.headerFamilyTopAnchor",\n        r"appPage\\.headerFamilyTitleBaseline",\n        r"appPage\\.headerFamilyTrailingBaseline",\n')
write(p,s)

# Delete temporary migration mechanism before computing final manifest.
Path('Checks/apply-1.6.2.py').unlink(missing_ok=True)
Path('.github/workflows/apply-1.6.2.yml').unlink(missing_ok=True)

# SHA manifest reflects the final repository state.
files=sorted([p for p in Path('.').rglob('*') if p.is_file() and p.as_posix()!='SHA256SUMS.txt' and '.git/' not in p.as_posix()])
write('SHA256SUMS.txt','\n'.join(f'{hashlib.sha256(p.read_bytes()).hexdigest()}  {p.as_posix()}' for p in files)+'\n')
