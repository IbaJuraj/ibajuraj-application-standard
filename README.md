# IbaJuraj Application Standard

Autoritatívny spoločný štandard pre aplikácie IbaJuraj.

Aktuálna verzia: **1.6.4**

Najnovší patch 1.6.4 spresňuje spoločnú geometriu navigačných dlaždíc a ikonových kontajnerov, zabraňuje lokálnemu geometry driftu, chráni čitateľnosť segmented/mode controls pri lokalizácii a Dynamic Type a zavádza whole-app visual consistency a feature-maturity exposure gate.

Stav: **finálne vydanie**

## Účel repozitára

Tento repozitár je jediným zdrojom pravdy pre spoločné pravidlá kvality, UX, architektúry, lokalizácie, prístupnosti, dát, bezpečnosti, testovania a vydávania aplikácií IbaJuraj.

Produktové pravidlá zostávajú v repozitároch jednotlivých aplikácií. Aplikácie si uchovávajú lokálnu kópiu konkrétnej prijatej verzie a záznam `APP_STANDARD_ADOPTION.md`.

## Hlavné súbory

- `IBAJURAJ_APPLICATION_STANDARD.md` – záväzné spoločné pravidlá,
- `DESIGN_TOKENS.md` – spoločné rozmery, rozostupy a komponentové varianty,
- `STANDARD_VERSION` – jednoduchá strojovo čitateľná verzia,
- `standard.json` – metadata pre automatické kontroly,
- `GOVERNANCE.md` – verzionovanie a proces zmien,
- `CHANGELOG.md` – história vydaných verzií,
- `MIGRATION.md` – migračné pokyny medzi zdrojmi/verziami,
- `TEST_MATRIX.md` – minimálna manuálna a runtime testovacia matica,
- `RELEASE_CHECKLIST.md` – spoločné release brány,
- `REFERENCE_PATTERNS.md` – referenčná informačná hierarchia spoločných obrazoviek,
- `SUPPORT_AND_LINKS.md` – autoritatívny register verejných odkazov,
- `Proposals/` – návrhy zmien štandardu,
- `Templates/` – šablóny adopcie a výnimiek,
- `Checks/` – automatické validačné skripty.

## Ako aplikácia prijme štandard

1. Skontroluje najnovšiu verziu v `standard.json`.
2. Prečíta `CHANGELOG.md` a `MIGRATION.md` a posúdi dopad.
3. Upraví kód, testy a dokumentáciu.
4. Skopíruje dokumenty z konkrétneho tagu, nie z pohyblivého `main`.
5. Aktualizuje svoj `APP_STANDARD_ADOPTION.md`.
6. Určí pravdivú úroveň adopcie Level 0 až Level 4.
7. Vykoná automatický a manuálny release audit.

Pre Level 3 a Level 4 musí aplikácia uložiť vyplnenú testovaciu maticu, release checklist a odkazy na dôkazy. Samotný úspech textového validačného skriptu nestačí.

Aplikácia nesmie automaticky prijať novú verziu iba preto, že bola publikovaná.

### Nové v 1.6.4

Verzia 1.6.4 je spätne kompatibilný UX/consistency PATCH. Zavádza Component Family Geometry & Icon Contract, Shared Component First / No Local Geometry Drift, Text Fit & Mode-Control Readability, Feature Maturity Exposure a Whole-App Visual Consistency Gate. Rovnako pomenované komponentové roly už nemajú mať náhodne rozdielny shape, výšku, icon container alebo padding medzi obrazovkami.

### Nové v 1.6.3

Verzia 1.6.3 je spätne kompatibilný PATCH/hardening release. Dopĺňa Floating Tab Bar Content Clearance Contract, Pinned Header Eligibility, voliteľný Rotating Content Pattern, Verified AI & Generated Assistance Contract, Authoritative Data Separation & Traceability a povinné bezpečné správanie pri nízkej istote. Zároveň opravuje historické nekonzistencie testovacej matice a verzie 1.4.1 v release dokumentácii.

### Nové v 1.6.2

Verzia 1.6.2 dopĺňa Header Family Alignment Contract. Obrazovky používajúce rovnaký produktový header musia zachovať spoločný top anchor, title baseline a trailing-action baseline aj vtedy, keď jedna z nich obsahuje Back akciu. Zdieľaný header sa nemá dorovnávať lokálnymi hardcoded top offsetmi.

### Nové v 1.6.0

Verzia 1.6.0 zjednocuje používateľské metadata na obrazovke **O aplikácii** a zavádza spoločný kontrakt pre kompaktné súhrnné sekcie typu **Na prvý pohľad**. Používateľ vidí marketingovú verziu + build aplikácie a pri IbaJuraj Application Standard iba `Verzia X.Y.Z`; interné adoption/audit údaje zostávajú mimo bežného UI. Súhrnné metriky nesmú vytláčať hlavnú úlohu detailu z prvého viewportu.

## Verzie a tagy

standard-v1.6.4

Používa sa sémantické verzionovanie:

- PATCH – spätne kompatibilné spresnenie/oprava alebo conditional quality/safety hardening bez migrácie nedotknutých produktov,
- MINOR – nový spoločný capability/contract s širším adopčným dopadom,
- MAJOR – zmena vyžadujúca migráciu alebo meniaca záväzné správanie.

Každá vydaná verzia má tag vo formáte:

```text
standard-v1.6.4
```

Aktuálny release: **IbaJuraj Application Standard 1.6.4**.

## Návrhy zmien

Zmena začína návrhom podľa `Proposals/TEMPLATE.md`. Automatický nástroj môže vytvoriť návrh alebo report, ale nesmie bez schválenia zaviesť nové MUST pravidlo.

Verzia 1.6.4 zachováva pravidlá 1.6.3 a spresňuje spoločnú komponentovú geometriu, text-fit/localization, maturity exposure a whole-app visual consistency bez migrácie doménových používateľských dát.
