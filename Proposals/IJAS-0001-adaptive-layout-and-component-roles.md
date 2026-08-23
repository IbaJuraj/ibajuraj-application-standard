# IJAS-0001 – Adaptívne rozloženie a sémantické roly komponentov

**Stav:** implemented
**Navrhovateľ:** IbaJuraj
**Dátum:** 2026-08-09
**Dotknuté aplikácie:** Strážca Termínov, Lex Drive, Peňaženka Kariet, Kalkulačka 2v1
**Navrhovaná verzia štandardu:** 1.2.0

## Problém

Rovnaké alebo podobné dlaždice používajú rozdielne rozmery a pevné rozloženia. Malé displeje, dlhšie lokalizácie a Dynamic Type môžu spôsobiť orezanie, zatiaľ čo veľké displeje komponenty neprimerane rozťahujú.

## Dôkazy a príklady

Potreba sa potvrdila pri kategóriách Strážcu Termínov, rýchlom výbere Lex Drive a domovských kartách Peňaženky Kariet. Komponenty majú spoločné geometrické potreby, ale rozdielny produktový význam.

## Navrhované pravidlo

Rozloženie MUST reagovať na dostupný priestor a obsah. Komponenty s rovnakou sémantickou rolou SHOULD používať spoločný variant a tokeny; rozdielne roly MUST NOT byť nútené do identickej výšky alebo pomeru strán.

**Záväznosť:** MUST / SHOULD

## Rozsah

Spoločný štandard vlastní adaptívne správanie, minimálne rozmery, rozostupy, dotykové plochy a sémantické roly. Produkt vlastní obsah, farebnú identitu, produktový pomer strán a informačnú prioritu.

## Migrácia

Nové obrazovky používajú pravidlá okamžite. Existujúce mriežky sa auditujú v plánovanom builde bez migrácie používateľských dát.

## Kompatibilita a riziká

Zmena je spätne kompatibilná. Rizikom je mechanické zjednotenie rozdielnych produktových kariet; návrh ho obmedzuje sémantickými rolami.

## Automatická kontrola

Statická kontrola môže overovať používanie tokenov. Snapshot a runtime testy overujú kompaktný, štandardný a veľký displej, Dynamic Type a dlhšie lokalizácie.

## Rozhodnutie

**Výsledok:** implemented
**Odôvodnenie:** Rovnaká potreba bola potvrdená vo viacerých nezávislých produktoch.
**Schválená verzia:** 1.2.0
