# IJAS-0007 – Root page title and subtitle typography

**Stav:** Accepted  
**Verzia:** 1.5.0, clarified for 1.9.0 RC1  
**Dotknuté aplikácie:** Strážca Termínov, Lex Drive, Peňaženka Kariet, Kalkulačka 2v1

## Problém

Rovnaká hierarchická rola hlavného názvu a priameho podnadpisu používala medzi aplikáciami rozdielne lokálne bodové veľkosti a váhy. Pevná bodová veľkosť navyše môže na užšom viewport-e viesť k truncation (`…`) alebo k nekonzistentnému zmenšeniu iba niektorých peer root obrazoviek.

## Rozhodnutie

Spoločný root header používa jednu typografickú rodinu pre všetky peer root obrazovky. `appPage.title` je bold hlavný titul a `appPage.subtitle` je sekundárny podnadpis; oba štýly podporujú Dynamic Type.

Veľkosť hlavného root titulku sa MUSÍ odvodzovať od reálne dostupnej šírky viewport-u alebo kontajnera, nie od názvu konkrétneho modelu zariadenia. Peer root obrazovky na tom istom viewport-e MUSIA používať rovnaký výsledný title token/veľkosť.

Adaptácia MÁ preferovať zachovanie celého názvu primeraným zmenšením, tighteningom alebo breakpoint tokenom pred truncation pomocou `…`. Produkt MÔŽE definovať vlastné min/max clamped hodnoty; konkrétne bodové veľkosti nie sú cross-app povinné, ak je zachovaná rovnaká hierarchická rola a konzistencia family.

Nested/system navigation headers (napr. obrazovka Nastavenia otvorená z root obrazovky) sú samostatná header family a nemusia používať root-title veľkosť.

## Referenčná adopcia

Strážca Termínov Build 120 Phase 14B R21 používa viewport-width-driven root title token pre Prehľad, Kategórie a Dokumenty: 28 / 30 / 32 pt podľa dostupnej šírky. Ide o referenčnú implementáciu, nie povinné cross-app čísla.

## Dôsledok

Produktový text zostáva odlišný, typografická rola je spoločná a merateľná side-by-side auditom. Menší iPhone nesmie spôsobiť, že iba jeden peer root title bude orezaný alebo zmenšený iným pravidlom než ostatné peer root obrazovky.