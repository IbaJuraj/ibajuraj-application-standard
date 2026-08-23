from pathlib import Path
import json, hashlib, subprocess, os

ROOT = Path('.')
VERSION='1.6.4'
DATE_ISO='2026-08-23'
DATE_SK='23. augusta 2026'


def must_replace(path, old, new, count=1):
    p=ROOT/path
    text=p.read_text(encoding='utf-8')
    if old not in text:
        raise SystemExit(f'Missing anchor in {path}: {old[:80]!r}')
    text=text.replace(old,new,count)
    p.write_text(text,encoding='utf-8')

# Core version metadata
(ROOT/'STANDARD_VERSION').write_text(VERSION+'\n',encoding='utf-8')

p=ROOT/'standard.json'
data=json.loads(p.read_text(encoding='utf-8'))
data['version']=VERSION
data['releasedAt']=DATE_ISO
data['source']['tag']=f'standard-v{VERSION}'
data['contracts']['componentFamilyGeometry']='shared-role-shared-geometry-explicit-semantic-exceptions'
data['contracts']['featureMaturity']='unfinished-experimental-capabilities-not-equal-user-facing-modes'
data['contracts']['visualConsistency']='whole-app-component-family-localization-dynamic-type-audit'
p.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')

# Main normative standard
must_replace('IBAJURAJ_APPLICATION_STANDARD.md','**Verzia:** 1.6.3  \n**Stav:** autoritatívny spoločný štandard  \n**Platnosť od:** 21. augusta 2026','**Verzia:** 1.6.4  \n**Stav:** autoritatívny spoločný štandard  \n**Platnosť od:** 23. augusta 2026')
anchor='- Bežný používateľský text MUST používať sémantické alebo relatívne Dynamic Type roly. Pevná bodová veľkosť SHOULD byť vyhradená pre zdokumentovanú špecifickú vizuálnu rolu a MUST mať overený accessibility variant.\n\n\n### 6.3 Spoločné systémové nastavenia'
insert='''- Bežný používateľský text MUST používať sémantické alebo relatívne Dynamic Type roly. Pevná bodová veľkosť SHOULD byť vyhradená pre zdokumentovanú špecifickú vizuálnu rolu a MUST mať overený accessibility variant.\n\n### 6.2.1 Component Family Geometry & Icon Contract\n\n- Komponenty s rovnakou sémantickou rolou MUST používať rovnakú komponentovú rodinu alebo spoločný geometry contract naprieč celou aplikáciou. Rozdielna obrazovka sama osebe MUST NOT byť dôvodom na inú výšku, radius, padding, icon container alebo trailing geometriu.\n- Porovnateľné navigačné dlaždice MUST používať rovnaký variant `navigationTile.*`: rovnakú referenčnú minimálnu výšku, radius, vnútorné odsadenie, title/subtitle typografiu, medzery a trailing správanie. Pri nedostatku priestoru sa komponent adaptuje podľa Dynamic Type a dostupnej šírky; MUST NOT sa lokálne zmenšovať text alebo meniť geometriu iba kvôli jednej obrazovke.\n- Ikonový kontajner rovnakej komponentovej rodiny MUST mať rovnakú veľkosť, shape, radius, alignment a optickú symbolovú veľkosť. Kruh, rounded square, kapsula alebo iný shape MAY byť použitý iba ako pomenovaná sémantická rola alebo zdokumentovaná produktová výnimka.\n- Rovnaká kategória alebo stav SHOULD používať rovnakú sémantickú farebnú logiku; farba MUST NOT byť náhodnou per-screen dekoráciou a MUST NOT byť jediným nositeľom významu.\n- Interaktívny riadok rovnakej rodiny MUST zachovať spoločnú leading icon baseline, title/subtitle alignment, trailing value/chevron alignment a minimálnu dotykovú plochu.\n- Shared Component First: pred vytvorením novej lokálnej implementácie MUST byť overené, či rovnaká komponentová rodina už existuje. Ak existuje, nová obrazovka ju SHOULD znovu použiť alebo rozšíriť cez pomenovaný variant.\n- No Local Geometry Drift: lokálne `frame`, `padding`, `cornerRadius`, symbol size alebo offset MUST NOT obchádzať autoritatívny token/shared component bez zdokumentovaného dôvodu.\n- Selected, pressed, disabled a focused state rovnakého komponentu MUST zostať konzistentný naprieč obrazovkami a rešpektovať Reduce Motion, Increase Contrast a prístupnosť.\n\n### 6.2.2 Text Fit, Localization & Mode-Control Readability Contract\n\n- Dôležitý používateľský názov ovládacieho prvku MUST zostať čitateľný vo všetkých podporovaných lokalizáciách a pri podporovanom Dynamic Type. `minimumScaleFactor` alebo orezanie významového textu MUST NOT byť náhradou za adaptívny layout.\n- Segmented/mode control MUST mať dostatočnú výšku, vnútorné odsadenie a baseline tak, aby text nebol vertikálne orezaný, prekrytý ani vizuálne posunutý.\n- Ak sa podporované názvy segmentov nezmestia pri väčšom texte alebo dlhšej lokalizácii, layout MUST adaptovať počet riadkov, šírku, variant alebo prezentáciu namiesto straty textu.\n- Release audit SHOULD obsahovať stresový test najdlhšej podporovanej lokalizácie minimálne na spoločných navigačných dlaždiciach, segmented controls, settings rows a hlavných akciách.\n\n### 6.2.3 Feature Maturity & Development Controls Exposure Contract\n\n- Nedokončená, experimentálna alebo interná capability MUST NOT byť prezentovaná bežnému používateľovi ako rovnocenný produkčný režim iba preto, že je technicky prítomná v kóde.\n- Prepínače typu `Auto`, `Classic`, `AI Test`, mock/stub routing, interné score, pipeline názvy a diagnostické režimy MUST NOT byť súčasťou bežného produkčného UI. Ak sú potrebné pre vývoj, MUST byť compile-time alebo explicitne diagnosticky izolované.\n- Produkt MAY používateľovi sprístupniť nový režim až po definovanom capability/release gate. Dovtedy MUST zostať používateľská cesta jednoduchá a založená na najzrelšej podporovanej capability.\n- Interná existencia budúcej capability MUST NOT meniť právnu, bezpečnostnú alebo dátovú autoritu existujúceho produkčného režimu.\n\n### 6.2.4 Whole-App Visual Consistency Gate\n\nPred release, ktorý mení spoločné vizuálne komponenty, MUST whole-app audit skontrolovať všetky relevantné obrazovky, nie iba nahlásený screenshot. Minimálne sa overí:\n\n- navigačná tile/card geometry a content density,\n- icon container size/shape/radius a symbol alignment,\n- interactive row alignment, trailing values a chevrony,\n- segmented controls a text fit,\n- semantic color roles a Light/Dark parity,\n- Dynamic Type a najdlhšie podporované lokalizácie,\n- selected/pressed/disabled/focus states,\n- explicitné a zdokumentované sémantické výnimky.\n\nNáhodná vizuálna odchýlka medzi peer komponentmi je release defect. Zámerná odchýlka MAY zostať iba vtedy, keď má odlišnú sémantickú rolu alebo schválenú výnimku.\n\n### 6.3 Spoločné systémové nastavenia'''
must_replace('IBAJURAJ_APPLICATION_STANDARD.md',anchor,insert)

# Design tokens
must_replace('DESIGN_TOKENS.md','**Verzia:** 1.6.3  \n**Stav:** autoritatívny spoločný register  \n**Platnosť od:** 21. augusta 2026','**Verzia:** 1.6.4  \n**Stav:** autoritatívny spoločný register  \n**Platnosť od:** 23. augusta 2026')
anchor='Referenčná minimálna veľkosť MUST NOT byť použitá ako pevná maximálna veľkosť. Ak obsah potrebuje viac priestoru, komponent sa zväčší alebo sa mriežka zmení na menší počet stĺpcov.\n\n## Typografia koreňovej obrazovky'
insert='''Referenčná minimálna veľkosť MUST NOT byť použitá ako pevná maximálna veľkosť. Ak obsah potrebuje viac priestoru, komponent sa zväčší alebo sa mriežka zmení na menší počet stĺpcov.\n\n### Navigation tile & icon family geometry\n\n| Token | Hodnota | Typ |\n|---|---:|---|\n| `navigationTile.compact.minimumHeight` | 124 pt | `minimum` |\n| `navigationTile.compact.radius` | 22 pt | `exact` |\n| `navigationTile.compact.contentPadding` | 16 pt | `exact` |\n| `navigationTile.compact.contentGap` | 10 pt | `exact` |\n| `navigationTile.compact.iconContainer` | 44 × 44 pt | `exact` |\n| `navigationTile.compact.iconContainerRadius` | 12 pt | `exact` |\n| `navigationTile.compact.symbolOpticalSize` | 20 pt | `preferred` |\n| `navigationTile.compact.trailingIndicator` | `chevron.right` ak ide o push cieľ | `semantic` |\n| `navigationRow.standard.iconContainer` | 36 × 36 pt | `exact` |\n| `navigationRow.standard.iconContainerRadius` | 10 pt | `exact` |\n| `navigationRow.standard.symbolOpticalSize` | 17 pt | `preferred` |\n| `componentFamily.semanticException` | odlišná geometria iba pri odlišnej sémantickej roli alebo zdokumentovanej výnimke | `semantic` |\n| `componentFamily.localGeometryDrift` | zakázaný lokálny override bez pomenovaného variantu/výnimky | `semantic` |\n| `modeControl.textFit` | bez významového clippingu; adaptívne pre Dynamic Type a lokalizáciu | `semantic` |\n\n- `navigationTile.compact` používa jeden spoločný shape contract naprieč peer obrazovkami. Produktový obsah alebo farba MAY byť odlišná; geometry variant zostáva spoločný.\n- Ikonový kontajner rovnakej komponentovej rodiny MUST zachovať rovnaký shape a radius. Kruh nie je zameniteľný s rounded square iba podľa obrazovky.\n- Symbolová veľkosť je optická; konkrétny SF Symbol MAY vyžadovať malú centrálne definovanú korekciu, ale lokálne per-screen `font`/`scaleEffect` override SHOULD NOT vznikať.\n- Ak Dynamic Type alebo lokalizácia vyžaduje väčšiu výšku, komponent rastie smerom nahor od minima a peer komponenty v rovnakom layout kontexte SHOULD zachovať vizuálnu paritu.\n\n## Typografia koreňovej obrazovky'''
must_replace('DESIGN_TOKENS.md',anchor,insert)

# README
p=ROOT/'README.md'; text=p.read_text(encoding='utf-8')
text=text.replace('Aktuálna verzia: **1.6.3**','Aktuálna verzia: **1.6.4**',1)
text=text.replace('Najnovší patch 1.6.3 zjednocuje safe clearance pri floating navigácii, eligibility pinned headerov, kontrolovanú rotáciu obsahu a pridáva spoločné bezpečnostné pravidlá pre AI/generované odpovede, autoritatívne dáta, low-confidence fallback a regresné testovanie.','Najnovší patch 1.6.4 spresňuje spoločnú geometriu navigačných dlaždíc a ikonových kontajnerov, zabraňuje lokálnemu geometry driftu, chráni čitateľnosť segmented/mode controls pri lokalizácii a Dynamic Type a zavádza whole-app visual consistency a feature-maturity exposure gate.',1)
text=text.replace('### Nové v 1.6.3','''### Nové v 1.6.4\n\nVerzia 1.6.4 je spätne kompatibilný UX/consistency PATCH. Zavádza Component Family Geometry & Icon Contract, Shared Component First / No Local Geometry Drift, Text Fit & Mode-Control Readability, Feature Maturity Exposure a Whole-App Visual Consistency Gate. Rovnako pomenované komponentové roly už nemajú mať náhodne rozdielny shape, výšku, icon container alebo padding medzi obrazovkami.\n\n### Nové v 1.6.3''',1)
text=text.replace('standard-v1.6.3\n\nPoužíva sa','standard-v1.6.4\n\nPoužíva sa',1)
text=text.replace('```text\nstandard-v1.6.3\n```','```text\nstandard-v1.6.4\n```',1)
text=text.replace('Aktuálny release: **IbaJuraj Application Standard 1.6.3**.','Aktuálny release: **IbaJuraj Application Standard 1.6.4**.',1)
text=text.replace('Verzia 1.6.3 zachováva pravidlá 1.6.2 a rozširuje ich o navigation-surface, AI safety, authoritative-data a regression hardening bez migrácie doménových používateľských dát.','Verzia 1.6.4 zachováva pravidlá 1.6.3 a spresňuje spoločnú komponentovú geometriu, text-fit/localization, maturity exposure a whole-app visual consistency bez migrácie doménových používateľských dát.',1)
p.write_text(text,encoding='utf-8')

# Changelog
p=ROOT/'CHANGELOG.md'; text=p.read_text(encoding='utf-8')
entry='''## 1.6.4 – 2026-08-23\n\n### Added\n- Component Family Geometry & Icon Contract pre porovnateľné navigačné dlaždice, riadky a ikonové kontajnery naprieč celou aplikáciou.\n- Shared Component First a No Local Geometry Drift pravidlá proti lokálnym per-screen odchýlkam rovnakého komponentu.\n- Text Fit, Localization & Mode-Control Readability Contract pre segmented controls a významové ovládacie texty.\n- Feature Maturity & Development Controls Exposure Contract: nedokončené/experimentálne capability a Auto/Classic/AI Test/debug routing sa nezobrazujú ako bežné používateľské režimy.\n- Whole-App Visual Consistency Gate vrátane Light/Dark, Dynamic Type, najdlhších lokalizácií, icon shape/size a interaction states.\n- explicitné navigation tile/icon family tokeny v `DESIGN_TOKENS.md`.\n\n### Changed\n- existujúca component-family zásada z 1.6.3 je teraz normatívne presná aj pre size, shape, radius, padding, alignment a symbol geometry.\n- vizuálna odchýlka medzi peer komponentmi musí mať sémantický dôvod alebo zdokumentovanú výnimku.\n\n### Compatibility\n- spätne kompatibilný PATCH bez migrácie doménových používateľských dát,\n- existujúce aplikácie auditujú iba spoločné vizuálne komponenty pri najbližšom plánovanom builde; produktovo odlišné komponenty nemusia byť násilne zjednotené.\n\n'''
text=text.replace('# Changelog – IbaJuraj Application Standard\n\n','# Changelog – IbaJuraj Application Standard\n\n'+entry,1)
p.write_text(text,encoding='utf-8')

# Migration
p=ROOT/'MIGRATION.md'; text=p.read_text(encoding='utf-8')
block='''## 1.6.3 → 1.6.4\n\nVerzia 1.6.4 je spätne kompatibilný UX/consistency PATCH bez migrácie doménových používateľských dát.\n\n1. Vykonajte whole-app audit všetkých porovnateľných navigačných dlaždíc, navigačných riadkov a ikonových kontajnerov.\n2. Zjednoťte peer komponenty na spoločný variant/token pre minimum height, radius, padding, icon container, symbol alignment a trailing geometriu.\n3. Odstráňte náhodné kruh/rounded-square rozdiely v rovnakej komponentovej rodine; zachovajte iba pomenované sémantické výnimky.\n4. Odstráňte lokálne geometry overrides, ak rovnakú rolu už pokrýva shared component/token.\n5. Stresovo otestujte segmented/mode controls a spoločné riadky v najdlhších podporovaných lokalizáciách a pri Dynamic Type.\n6. Nedokončené/experimentálne capability, debug routing a test prepínače odstráňte z bežného používateľského UI alebo ich explicitne diagnosticky izolujte.\n7. Porovnajte Light/Dark, selected/pressed/disabled/focus states a whole-app component-family konzistenciu.\n8. Nevyžaduje sa migrácia uložených používateľských dát iba kvôli adopcii 1.6.4.\n\n'''
text=text.replace('# Migrácia IbaJuraj Application Standard\n\n','# Migrácia IbaJuraj Application Standard\n\n'+block,1)
p.write_text(text,encoding='utf-8')

# Test matrix
must_replace('TEST_MATRIX.md','# IbaJuraj Standard 1.6.3 – testovacia matica','# IbaJuraj Standard 1.6.4 – testovacia matica')
p=ROOT/'TEST_MATRIX.md'; text=p.read_text(encoding='utf-8')
block='''## Component family geometry & maturity exposure – 1.6.4\n\n- [ ] Whole-app audit prešiel všetky peer navigačné dlaždice/riadky, nie iba nahlásenú obrazovku.\n- [ ] Rovnaký navigation tile variant používa rovnaké minimum height, radius, padding, title/subtitle spacing a trailing geometriu.\n- [ ] Rovnaký icon-container variant používa rovnakú size, shape, radius a symbol alignment; odlišný kruh/rounded square má explicitný sémantický dôvod.\n- [ ] Neexistuje nezdokumentovaný per-screen `frame`/`padding`/`cornerRadius`/symbol-size override, ktorý obchádza spoločný variant.\n- [ ] Segmented/mode controls neorezávajú text pri default, XXL ani accessibility XXXL.\n- [ ] Najdlhšia podporovaná lokalizácia nespôsobí významový clipping navigačných dlaždíc, settings rows ani hlavných mode controls.\n- [ ] Selected/pressed/disabled/focus state rovnakého komponentu je konzistentný v Light/Dark.\n- [ ] Nedokončený/experimentálny režim ani Auto/Classic/AI Test/debug routing nie je viditeľný v bežnom používateľskom UI.\n- [ ] Každá zámerná vizuálna výnimka je pomenovaná sémantickou rolou alebo zdokumentovaná.\n\n'''
text=text.replace('## Kontakt a O aplikácii',block+'## Kontakt a O aplikácii',1)
p.write_text(text,encoding='utf-8')

# Release checklist
must_replace('RELEASE_CHECKLIST.md','# IbaJuraj Standard 1.6.3 – release checklist','# IbaJuraj Standard 1.6.4 – release checklist')
p=ROOT/'RELEASE_CHECKLIST.md'; text=p.read_text(encoding='utf-8')
text=text.replace('Tag má tvar `standard-v1.6.3`','Tag má tvar `standard-v1.6.4`',1)
block='''## Standard 1.6.4 – component geometry & exposure gate\n\n- [ ] Whole-app component-family audit bol vykonaný na všetkých relevantných root/list/detail obrazovkách.\n- [ ] Navigation tiles a rows rovnakej rodiny používajú spoločné geometry tokeny/varianty.\n- [ ] Icon containers rovnakej rodiny používajú spoločný shape/size/radius; výnimky sú sémanticky zdôvodnené.\n- [ ] Segmented/mode controls a významové akčné texty prešli localization + Dynamic Type stress testom bez clippingu.\n- [ ] Nedokončené/experimentálne capability a development routing controls nie sú v bežnom používateľskom UI.\n- [ ] Light/Dark a selected/pressed/disabled/focus states peer komponentov sú konzistentné.\n\n'''
text=text.replace('## Metadata a zdroj pravdy','## Metadata a zdroj pravdy',1)
# append before final historical sections safely
text += '\n'+block
p.write_text(text,encoding='utf-8')

# Reference patterns
must_replace('REFERENCE_PATTERNS.md','# IbaJuraj Standard 1.6.3 – referenčné vzory','# IbaJuraj Standard 1.6.4 – referenčné vzory')
p=ROOT/'REFERENCE_PATTERNS.md'; text=p.read_text(encoding='utf-8')
text += '''\n\n## Component family geometry – 1.6.4\n\n```text\n[44×44 rounded-square icon]  Názov                  >\n                            Podnadpis\n\nrovnaká rola na inej obrazovke:\n[44×44 rounded-square icon]  Názov                  >\n                            Podnadpis\n```\n\n- Rovnaký component family variant zachováva icon container, radius, alignment, padding a content density.\n- Kruh namiesto rounded square je prípustný iba pre inú pomenovanú sémantickú rolu (napr. avatar/status) alebo zdokumentovanú výnimku.\n- Dlhší text alebo Dynamic Type môže komponent zväčšiť; nemá vytvoriť náhodný lokálny variant.\n\n## Mode control text fit – 1.6.4\n\n```text\n[ Praktické ] [ Právne ]\n````\n\n- Text je vertikálne centrovaný, neorezaný a čitateľný.\n- Pri dlhšej lokalizácii alebo Dynamic Type sa mení vhodný layout/variant, nie význam textu.\n\n## Feature maturity exposure – 1.6.4\n\n```text\nprodukčný používateľ: [jedna podporovaná cesta]\n\ndeveloper diagnostika: Auto | Classic | AI Test | score/routing\n                       ^ mimo bežného používateľského UI\n```\n'''
p.write_text(text,encoding='utf-8')

# Fix accidental 4-backtick fence if present for consistency
p=ROOT/'REFERENCE_PATTERNS.md'; t=p.read_text(encoding='utf-8').replace('````\n\n- Text je','```\n\n- Text je'); p.write_text(t,encoding='utf-8')

# Support/version and adoption template
for fname in ['SUPPORT_AND_LINKS.md']:
    p=ROOT/fname; t=p.read_text(encoding='utf-8'); t=t.replace('**Verzia:** 1.6.3','**Verzia:** 1.6.4',1); p.write_text(t,encoding='utf-8')
p=ROOT/'Templates/APP_STANDARD_ADOPTION.md'; t=p.read_text(encoding='utf-8').replace('1.6.3','1.6.4'); p.write_text(t,encoding='utf-8')

# New proposal, audit, release notes
(ROOT/'Proposals/IJAS-0017-component-family-geometry-and-maturity-exposure.md').write_text('''# IJAS-0017 – Component Family Geometry & Maturity Exposure\n\n**Status:** accepted  \n**Target:** Standard 1.6.4  \n**Date:** 2026-08-23\n\n## Problem\nRuntime audit Lex Drive ukázal, že vizuálne rovnocenné navigačné položky môžu driftovať medzi kruhovými a rounded-square icon containers, rozdielnou veľkosťou, paddingom a text alignmentom. Zároveň interné Auto/Classic/AI Test ovládanie môže byť technicky dostupné skôr, než je capability pripravená pre používateľa.\n\n## Decision\nRovnaká komponentová rola používa spoločný geometry contract. Výnimka musí mať odlišnú sémantickú rolu alebo byť zdokumentovaná. Dôležitý text musí prežiť localization/Dynamic Type bez clippingu. Nedokončené/experimentálne capability a development routing controls sa nezobrazujú ako bežné používateľské režimy.\n\n## Scope\nNavigation tiles, navigation/list rows, icon containers, segmented/mode controls, shared interaction states a whole-app visual consistency audit.\n\n## Compatibility\nPATCH; bez migrácie doménových používateľských dát.\n''',encoding='utf-8')

(ROOT/'AUDIT_1.6.3_TO_1.6.4.md').write_text('''# Audit IbaJuraj Application Standard 1.6.3 → 1.6.4\n\n**Dátum:** 2026-08-23  \n**Výsledok:** 1.6.3 zostáva architektonicky platný; 1.6.4 je vhodný ako spätne kompatibilné UX/consistency spresnenie.\n\n## Zistenia\n1. Standard už vyžadoval spoločnú geometriu rovnakých rolí, ale icon-container shape/size a whole-app enforcement neboli dostatočne explicitné.\n2. `DESIGN_TOKENS.md` už definoval `navigationTile.compact` a všeobecné icon-container rozmery, no chýbala priama väzba na jeden shape/radius/symbol contract pre peer navigačné komponenty.\n3. Dynamic Type a localization boli všeobecne povinné, ale segmented/mode control text-fit potreboval explicitný clipping gate.\n4. DEBUG/mock izolácia existovala pre AI, ale chýbalo všeobecné pravidlo, že nedokončená capability sa nemá používateľovi ukazovať ako rovnocenný produkčný režim.\n5. Runtime nález v jednej obrazovke musí viesť k whole-app component-family auditu, nie iba k lokálnej oprave screenshotu.\n\n## Rozhodnutie\nPublikovať 1.6.4 ako PATCH bez migrácie doménových dát. Zaviesť Component Family Geometry & Icon Contract, Text Fit/Mode-Control Readability, Feature Maturity Exposure a Whole-App Visual Consistency Gate.\n''',encoding='utf-8')

(ROOT/'RELEASE_NOTES_1.6.4.md').write_text('''# IbaJuraj Application Standard 1.6.4\n\n**Dátum vydania:** 23. august 2026  \n**Typ:** PATCH / backward-compatible UX & consistency hardening  \n**Kompatibilita:** bez migrácie doménových používateľských dát\n\n## Prečo táto verzia vznikla\nRuntime audit Lex Drive ukázal rozdielnu geometriu vizuálne rovnocenných navigačných prvkov: rozdielne icon-container shapes, rozmery a alignment. Súčasne sa ukázala potreba presnejšieho pravidla pre text fit v segmented/mode controls a pre skrytie nedokončených interných režimov pred bežným používateľom.\n\n## Hlavné zmeny\n- Component Family Geometry & Icon Contract,\n- explicitný Navigation Tile & Icon Family token set,\n- Shared Component First a No Local Geometry Drift,\n- Text Fit, Localization & Mode-Control Readability Contract,\n- Feature Maturity & Development Controls Exposure Contract,\n- Whole-App Visual Consistency Gate,\n- localization + Dynamic Type stress gate pre spoločné controls.\n\n## Adopcia\nAplikácia pri prechode z 1.6.3 na 1.6.4 vykoná whole-app audit iba relevantných komponentových rodín. Produktovo odlišné komponenty sa nemajú násilne zjednocovať; rovnaká rola však nesmie driftovať medzi obrazovkami bez sémantického dôvodu alebo zdokumentovanej výnimky.\n''',encoding='utf-8')

# Update validation script for 1.6.4 artifacts/contracts
p=ROOT/'Checks/validate-standard.sh'; t=p.read_text(encoding='utf-8')
t=t.replace('  "AUDIT_1.6.2_TO_1.6.3.md"\n)', '  "AUDIT_1.6.2_TO_1.6.3.md"\n  "AUDIT_1.6.3_TO_1.6.4.md"\n  "Proposals/IJAS-0017-component-family-geometry-and-maturity-exposure.md"\n)')
t=t.replace('        r"Authoritative Data Separation & Traceability Contract",\n        r"najbližší.*výsledok.*MUST NOT",', '        r"Authoritative Data Separation & Traceability Contract",\n        r"najbližší.*výsledok.*MUST NOT",\n        r"Component Family Geometry & Icon Contract",\n        r"Feature Maturity & Development Controls Exposure Contract",\n        r"Whole-App Visual Consistency Gate",')
t=t.replace('        r"sectionHeader\\.pinnedEligibility",\n    ],', '        r"sectionHeader\\.pinnedEligibility",\n        r"navigationTile\\.compact\\.iconContainer",\n        r"navigationRow\\.standard\\.iconContainer",\n        r"componentFamily\\.localGeometryDrift",\n        r"modeControl\\.textFit",\n    ],')
p.write_text(t,encoding='utf-8')

# Final workflow: restore normal read-only validator after this release staging run.
workflow='''name: Validate IbaJuraj Application Standard\n\non:\n  push:\n    branches:\n      - main\n  pull_request:\n  workflow_dispatch:\n\npermissions:\n  contents: read\n\njobs:\n  validate:\n    runs-on: ubuntu-latest\n    steps:\n      - name: Checkout repository\n        uses: actions/checkout@v4\n\n      - name: Validate standard\n        run: bash Checks/validate-standard.sh\n'''
(ROOT/'.github/workflows/validate-standard.yml').write_text(workflow,encoding='utf-8')

# Remove staging directory before checksums/commit.
stage=ROOT/'.release-1.6.4'
if stage.exists():
    for child in stage.iterdir():
        child.unlink()
    stage.rmdir()

# Regenerate SHA256 manifest for exact final release tree excluding itself and .git.
files=[]
for p in ROOT.rglob('*'):
    if not p.is_file(): continue
    rel=p.as_posix()
    if rel.startswith('.git/') or rel=='SHA256SUMS.txt': continue
    files.append(rel)
files.sort()
lines=[]
for rel in files:
    digest=hashlib.sha256((ROOT/rel).read_bytes()).hexdigest()
    lines.append(f'{digest}  {rel}')
(ROOT/'SHA256SUMS.txt').write_text('\n'.join(lines)+'\n',encoding='utf-8')

print('Prepared IbaJuraj Application Standard 1.6.4 release tree')
