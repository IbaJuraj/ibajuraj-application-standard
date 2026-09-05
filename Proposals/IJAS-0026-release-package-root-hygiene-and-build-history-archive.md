# IJAS-0026 – Release Package Root Hygiene and Build History Archive

**Stav:** accepted  
**Navrhovateľ:** IbaJuraj  
**Dátum:** 2026-09-04  
**Dotknuté aplikácie:** všetky IbaJuraj aplikácie a distribuované source/release ZIP balíky  
**Schválená candidate verzia štandardu:** 1.8.0 RC1

## Problém
Pri dlhšie vyvíjanej aplikácii sa root zdrojového/release balíka môže zaplniť historickými `BUILD_*`, `RUNTIME_ACCEPTANCE_*`, migration/scope checkpointmi a ďalšími dokumentmi supersedovaných buildov. Balík môže byť technicky zostaviteľný, ale prestáva byť jednoznačné, ktorý dokument je aktuálny zdroj pravdy.

Toto je odlišné od technického odpadu typu `.DS_Store` alebo `xcuserdata`: ide o documentation/release-package hygiene debt.

## Dôkaz
Strážca Termínov mal v aktívnom root priečinku vedľa aktuálneho buildu historické dokumenty Build 96–105 a viacero runtime checklistov. Obsah mal historickú hodnotu, ale aktívny release povrch bol neprehľadný.

## Schválený kontrakt
1. Root aktuálneho source/release balíka MUST obsahovať iba aktuálne autoritatívne projektové súbory, zdrojové priečinky, build/release konfiguráciu a malú sadu dokumentov potrebných pre aktuálny build.
2. Historické build-specific dokumenty MUST NOT zostať neobmedzene v root priečinku po supersedovaní buildu.
3. Historické dokumenty, ktoré majú zostať zachované, MUST byť presunuté do jasne oddelenej archívnej štruktúry, napr. `Documentation/History/Builds/` alebo ekvivalentu.
4. `CHANGELOG.md` SHOULD byť hlavný súhrnný historický záznam medzi buildmi.
5. Aktuálny root MAY obsahovať README, adoption/conformance metadata, changelog, aktuálny build dokument a aktuálny runtime acceptance checklist.
6. Build/release tooling SHOULD pri novom autoritatívnom builde identifikovať a archivovať supersedované root dokumenty.
7. Release/source hygiene gate SHOULD označiť root-level build dokumenty s nižším build numberom, ak nie sú explicitne povolené.
8. Archívna dokumentácia MUST NOT byť omylom pridaná do runtime app bundle, ak ju aplikácia nepotrebuje.
9. Čistenie rootu MUST NOT potichu zmazať jediný dôkaz významnej runtime regresie, migrácie alebo release rozhodnutia; dôkaz sa archivuje alebo konsoliduje.

## Odporúčaná štruktúra
```text
<AppRoot>/
  <AppSource>/
  <AppTests>/
  <App>.xcodeproj/
  Checks/
  Documentation/History/Builds/
  APP_STANDARD_ADOPTION.md
  STANDARD_CONFORMANCE.json
  STANDARD_VERSION
  CHANGELOG.md
  BUILD_<current>_....md
  RUNTIME_ACCEPTANCE_BUILD_<current>.md
  README.md
```

## Migrácia
Pri najbližšom novom builde identifikovať staršie root-level build dokumenty, archivovať alebo konsolidovať ich, overiť skripty odkazujúce na pôvodné cesty a pridať hygiene kontrolu, aby sa problém nevracal.

## Vzťah k 1.7.0
Návrh rozširuje `STD-RELEASE-001 — Source hygiene` o explicitný release-package/root-history kontrakt. Runtime produktové správanie nemení.

## Rozhodnutie
**Výsledok:** accepted pre 1.8.0 RC1  
**Odôvodnenie:** opakovaný cross-app problém s nejednoznačným release rootom a rizikom použitia starého build dokumentu ako zdroja pravdy.  
**Schválená verzia:** 1.8.0 RC1
