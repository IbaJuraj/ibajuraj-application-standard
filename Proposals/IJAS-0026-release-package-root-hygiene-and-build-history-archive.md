# IJAS-0026 – Release Package Root Hygiene and Build History Archive

**Stav:** proposed
**Navrhovateľ:** IbaJuraj
**Dátum:** 2026-09-04
**Dotknuté aplikácie:** všetky IbaJuraj aplikácie a ich distribuované source/release ZIP balíky
**Navrhovaná verzia štandardu:** 1.7.1

## Problém

Pri dlhšie vyvíjanej aplikácii sa môže root zdrojového/release balíka postupne zaplniť historickými súbormi jednotlivých buildov. Typický príklad je akumulácia súborov ako `BUILD_96_*.md`, `BUILD_97_*.md`, …, `BUILD_105_*.md`, viacerých `RUNTIME_ACCEPTANCE_BUILD_*.md`, starších migration/scope poznámok a ďalších už neaktuálnych checkpointov priamo vedľa Xcode projektu a aktuálnych autoritatívnych súborov.

Takýto balík môže byť technicky zostaviteľný, ale root prestáva byť jednoznačný. Zvyšuje sa riziko, že človek alebo automatizácia použije starý build dokument ako aktuálny zdroj pravdy, release ZIP rastie bez dôvodu a pri audite nie je na prvý pohľad jasné, ktoré súbory patria k aktuálnemu buildu.

Tento problém je odlišný od `.DS_Store`, `xcuserdata` alebo iných zakázaných technických nečistôt. Ide o **dokumentačný a release-package hygiene debt**: historické súbory môžu byť legitímne, ale nemajú sa neobmedzene hromadiť v koreňovom priečinku aktuálneho buildu.

## Dôkaz a motivácia

Pri Strážcovi Termínov v1.57.0 / Build 106 sa v root priečinku aktuálneho balíka nachádzali vedľa aktuálnych súborov aj buildové dokumenty Build 96 až 105, viacero `RUNTIME_ACCEPTANCE_BUILD_*` dokumentov a staršie lokalizačné/release checkpointy. Funkčný obsah týchto dokumentov môže mať historickú hodnotu, ale ich umiestnenie v root aktuálneho buildu znižuje čitateľnosť a jednoznačnosť balíka.

## Navrhované pravidlo

1. Root aktuálneho source/release balíka MUST obsahovať iba aktuálne autoritatívne projektové súbory, zdrojové priečinky, build/release konfiguráciu a malú sadu dokumentov potrebných pre aktuálny build.
2. Historické build-specific dokumenty MUST NOT zostať neobmedzene v root priečinku po tom, ako ich build prestane byť aktuálnym autoritatívnym buildom.
3. Historické dokumenty, ktoré majú zostať zachované, MUST byť presunuté do jasne oddelenej archívnej štruktúry, napr. `Documentation/History/Builds/`, `Documentation/Archive/` alebo ekvivalentu.
4. `CHANGELOG.md` SHOULD byť hlavný súhrnný historický záznam medzi buildmi. Detailný build dokument MAY existovať pre aktuálny build, ale po supersedovaní sa má archivovať alebo jeho podstatný obsah konsolidovať do changelogu.
5. Aktuálny root MAY obsahovať napr. `README`, `README_SK`, `APP_STANDARD_ADOPTION.md`, `STANDARD_VERSION`, `STANDARD_CONFORMANCE.json`, aktuálny build/release dokument a aktuálny runtime acceptance checklist. Staršie ekvivalenty týchto build-specific dokumentov nemajú zostať na rovnakej úrovni.
6. Build generation/release tooling SHOULD pri vytváraní nového autoritatívneho buildu automaticky identifikovať a archivovať alebo odstrániť root-level dokumenty patriace supersedovaným buildom.
7. Release/source hygiene gate SHOULD vedieť označiť root-level historické build dokumenty, ktorých build number je nižší než aktuálny autoritatívny build, ak nie sú na explicitnom allowliste.
8. Archívna dokumentácia MUST NOT byť omylom pridaná do app targetu alebo distribuovaná v runtime bundle, ak ju aplikácia nepotrebuje.
9. Čistenie rootu MUST NOT mazať jediný existujúci dôkaz o významnej runtime regresii, migrácii alebo release rozhodnutí. Taký dôkaz sa má archivovať alebo konsolidovať, nie bez stopy odstrániť.

**Záväznosť:** MUST / MUST NOT pre jednoznačnosť aktuálneho balíka a oddelenie histórie; SHOULD pre automatizáciu a preferovanú konsolidáciu.

## Odporúčaná root štruktúra

Príklad pre aplikáciu:

```text
<AppRoot>/
  <AppSource>/
  <AppTests>/
  <App>.xcodeproj/
  Checks/
  Documentation/
    History/
      Builds/
        105/
        104/
        ...
  APP_STANDARD_ADOPTION.md
  STANDARD_CONFORMANCE.json
  STANDARD_VERSION
  CHANGELOG.md
  BUILD_106_....md
  RUNTIME_ACCEPTANCE_BUILD_106.md
  README.md
```

Nie je povinné použiť presne tieto názvy priečinkov. Povinný je princíp: **aktuálny build je v roote jednoznačný a historické buildové dokumenty sú oddelené od aktívneho release povrchu**.

## Migrácia

Pri najbližšom novom builde existujúcej aplikácie:
- identifikovať root-level dokumenty viazané na staršie build numbers,
- ponechať v roote iba aktuálny build/release dokument a aktuálne autoritatívne spoločné dokumenty,
- staršie buildové poznámky presunúť do archívu alebo ich konsolidovať do `CHANGELOG.md`,
- overiť, že žiadny skript, test alebo build phase neočakáva ich pôvodnú root cestu,
- doplniť hygiene check tak, aby sa problém pri ďalších buildoch nevracal.

## Kompatibilita a riziká

Pravidlo nemení runtime správanie aplikácie ani dátový model. Je spätne kompatibilné. Rizikom nesprávnej migrácie je strata historického release dôkazu alebo rozbitie skriptov používajúcich staré cesty; preto sa história má najprv archivovať a až následne môže byť root zjednodušený.

## Automatická kontrola

Áno, vo veľkej miere:
- release checker môže zistiť aktuálny build number z autoritatívnych metadata,
- môže vyhľadať root-level názvy `BUILD_<n>_*`, `RUNTIME_ACCEPTANCE_BUILD_<n>*` a ďalšie dohodnuté family,
- nižšie build numbers môže označiť ako `archive-required`,
- explicitný allowlist môže zachovať dokumenty, ktoré nie sú historickým buildovým odpadom,
- ZIP hygiene test môže kontrolovať, že aktuálny release root neobsahuje supersedované build-specific dokumenty.

## Vzťah k existujúcemu Standardu

Aktívny Standard 1.7.0 už obsahuje všeobecný `STD-RELEASE-001 — Source hygiene`. IJAS-0026 ho nenahrádza; navrhuje spresnenie pre **release-package/root documentation hygiene**, ktoré súčasný text explicitne nerieši.

Aktívny verejný Standard zostáva 1.7.0. Tento návrh je kandidátom na 1.7.1 a nestáva sa záväzným, kým nebude formálne schválený a vydaný v novej verzii Standardu.

## Rozhodnutie

Vyplní sa po posúdení.

**Výsledok:**
**Odôvodnenie:**
**Schválená verzia:**
