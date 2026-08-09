# IJAS-0002 – Systémové interakcie a životný cyklus údajov

**Stav:** implemented  
**Navrhovateľ:** IbaJuraj  
**Dátum:** 2026-08-09  
**Dotknuté aplikácie:** Strážca Termínov, Lex Drive, Peňaženka Kariet, Kalkulačka 2v1  
**Navrhovaná verzia štandardu:** 1.2.0

## Problém

Produkty opakovane riešia upozornenia, oprávnenia, synchronizáciu, zálohy, export, chyby, rozpracované formuláre a prechod do backgroundu. Bez spoločného pravidla hrozia rozdielne významy a strata dôvery používateľa.

## Dôkazy a príklady

Strážca Termínov potrebuje presné dátumy, upozornenia a obnovu. Peňaženka Kariet používa iCloud, export a lokálny zámok. Lex Drive pracuje s overeným vzdialeným obsahom a chybovými stavmi. Kalkulačka rieši fokus, oprávnenie mikrofónu a zachovanie vstupu.

## Navrhované pravidlo

Aplikácie MUST rozlišovať synchronizáciu, zálohu a export, chrániť rozpracované údaje, vysvetľovať výsledky a chyby a žiadať systémové oprávnenia až v kontexte potrebnej funkcie.

**Záväznosť:** MUST / SHOULD

## Rozsah

Spoločné sú významy systémových interakcií a bezpečnostné hranice. Doménové dátové modely, termínové enginy, právne balíky a kalkulačné workflow zostávajú produktové.

## Migrácia

Nevyžaduje dátovú migráciu. Existujúce toky sa auditujú pri najbližšom plánovanom builde.

## Kompatibilita a riziká

Zmena je spätne kompatibilná. Najväčším rizikom je nepresné uplatnenie na produkt, ktorý danú funkciu nepoužíva; pravidlá sú preto podmienené prítomnosťou funkcie.

## Automatická kontrola

Testy môžu overiť duplicitné notifikácie, prechod časového pásma, obnovu formulára, lokálne a cloud vymazanie, offline stav a opakované lifecycle udalosti.

## Rozhodnutie

**Výsledok:** implemented  
**Odôvodnenie:** Rovnaké systémové riziká sa potvrdili vo viacerých produktoch.  
**Schválená verzia:** 1.2.0

