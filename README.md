# IbaJuraj Application Standard

Autoritatívny spoločný štandard pre aplikácie IbaJuraj.

Aktuálna verzia: **1.0.0**  
Stav: **active**

## Účel repozitára

Tento repozitár je jediným zdrojom pravdy pre spoločné pravidlá kvality, UX, architektúry, lokalizácie, prístupnosti, dát, bezpečnosti, testovania a vydávania aplikácií IbaJuraj.

Produktové pravidlá zostávajú v repozitároch jednotlivých aplikácií. Lex Drive, Strážca Termínov a ďalšie aplikácie si uchovávajú lokálnu kópiu konkrétnej prijatej verzie a záznam `APP_STANDARD_ADOPTION.md`.

## Hlavné súbory

- `IBAJURAJ_APPLICATION_STANDARD.md` – záväzné spoločné pravidlá,
- `STANDARD_VERSION` – jednoduchá strojovo čitateľná verzia,
- `standard.json` – metadata pre automatické kontroly,
- `GOVERNANCE.md` – verzionovanie a proces zmien,
- `CHANGELOG.md` – história vydaných verzií,
- `SUPPORT_AND_LINKS.md` – autoritatívny register verejných odkazov,
- `Proposals/` – návrhy zmien štandardu,
- `Templates/` – šablóny adopcie a výnimiek,
- `Checks/` – automatické validačné skripty.

## Ako aplikácia prijme štandard

1. Skontroluje najnovšiu verziu v `standard.json`.
2. Prečíta `CHANGELOG.md` a posúdi dopad.
3. Upraví kód, testy a dokumentáciu.
4. Skopíruje dokumenty z konkrétneho tagu, nie z pohyblivého `main`.
5. Aktualizuje svoj `APP_STANDARD_ADOPTION.md`.
6. Vykoná automatický a manuálny release audit.

Aplikácia nesmie automaticky prijať novú verziu iba preto, že bola publikovaná.

## Verzie a tagy

Používa sa sémantické verzionovanie:

- PATCH – oprava bez zmeny významu,
- MINOR – nové spätne kompatibilné pravidlo,
- MAJOR – zmena vyžadujúca migráciu alebo meniaca záväzné správanie.

Každá vydaná verzia má tag vo formáte:

```text
standard-v1.0.0
```

## Prvé publikovanie tohto repozitára

1. Vytvorte verejný repozitár `IbaJuraj/ibajuraj-application-standard`.
2. Nahrajte celý obsah tohto balíka do koreňa repozitára.
3. Spustite GitHub Action **Validate standard**.
4. Vytvorte tag `standard-v1.0.0`.
5. Vytvorte GitHub Release **IbaJuraj Application Standard 1.0.0**.
6. Až potom zmeňte odkazy v aplikáciách a na webe IbaJuraj Apps.

## Návrhy zmien

Zmena začína návrhom podľa `Proposals/TEMPLATE.md`. Automatický nástroj môže vytvoriť návrh alebo report, ale nesmie bez schválenia zaviesť nové MUST pravidlo.
