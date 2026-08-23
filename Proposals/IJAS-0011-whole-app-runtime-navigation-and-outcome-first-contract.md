# IJAS-0011 – Whole-App Runtime Integrity, Navigation & Outcome-First Contract

**Stav:** accepted in Standard 1.6.1
**Dátum:** 19. august 2026

## Dôvod

Whole-app audit Lex Drive odhalil opakované triedy problémov, ktoré sú všeobecné pre aplikácie IbaJuraj: hardcoded runtime metadata, route-špecifický swipe-back, slepé výsledky vyhľadávania, lokálne odtiene neutrálneho pozadia, trvalé `NOVÉ` badge a príliš skoré zobrazovanie technických alebo právnych detailov.

## Rozsah

Návrh zavádza alebo spresňuje:

- runtime single source of truth,
- navigation policy pre celé rodiny detailov,
- outcome-first/practical-first hierarchy,
- pinned section context a collapsing titles,
- temporary-badge lifecycle,
- temporal coverage constraints,
- search/navigation bridges,
- published-item completeness a behaviorálne regresné testy,
- technický text hygiene a semantic color meaning.

## Dopad na aplikácie

Bez migrácie doménových používateľských dát. Vyžaduje audit existujúcich komponentov a runtime dôkazy tam, kde aplikácia používa príslušné funkcie.

## Záväznosť

Kritické metadata, navigačné, dátové a completeness pravidlá sú MUST. Prezentačné vzory pinned/collapsing a outcome-first používajú MUST/SHOULD podľa konkrétnej úlohy a rizika.
