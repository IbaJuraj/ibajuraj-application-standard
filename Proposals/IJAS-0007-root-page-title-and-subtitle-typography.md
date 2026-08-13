# IJAS-0007 – Root page title and subtitle typography

**Stav:** Accepted  \n**Verzia:** 1.5.0  \n**Dotknuté aplikácie:** Strážca Termínov, Lex Drive, Peňaženka Kariet, Kalkulačka 2v1

## Problém

Rovnaká hierarchická rola hlavného názvu a priameho podnadpisu používala medzi aplikáciami rozdielne lokálne bodové veľkosti a váhy.

## Rozhodnutie

Spoločný root header používa `appPage.title` = `.largeTitle.weight(.bold)`, `appPage.subtitle` = `.subheadline` so sekundárnou farbou a 6 pt medzerou. Oba štýly používajú Dynamic Type.

## Dôsledok

Produktový text zostáva odlišný, typografická rola je však spoločná a merateľná side-by-side auditom.
