# IbaJuraj Application Standard

Autoritatívny spoločný štandard pre aplikácie IbaJuraj.

Aktuálna verzia: **1.3.0**  
Stav: **active**

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

## Verzie a tagy

Používa sa sémantické verzionovanie:

- PATCH – oprava bez zmeny významu,
- MINOR – nové spätne kompatibilné pravidlo,
- MAJOR – zmena vyžadujúca migráciu alebo meniaca záväzné správanie.

Každá vydaná verzia má tag vo formáte:

```text
standard-v1.3.0
```

Aktuálny release: **IbaJuraj Application Standard 1.3.0**.

## Návrhy zmien

Zmena začína návrhom podľa `Proposals/TEMPLATE.md`. Automatický nástroj môže vytvoriť návrh alebo report, ale nesmie bez schválenia zaviesť nové MUST pravidlo.
