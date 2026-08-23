# IbaJuraj Application Standard 1.6.2

**Dátum vydania:** 20. august 2026
**Typ:** PATCH
**Kompatibilita:** spätne kompatibilná; bez migrácie doménových používateľských dát

## Prečo táto verzia vznikla

Runtime audit ukázal opakujúci sa problém: dve obrazovky môžu používať rovnaký vizuálny header, ale nadpis alebo pravá Settings akcia sú vertikálne posunuté, pretože každá obrazovka používa vlastný top padding alebo safe-area kompenzáciu. Verzia 1.6.2 tento rozdiel explicitne zakazuje pre jednu header family.

## Hlavné zmeny

- Header Family Alignment Contract pre root aj vnorené obrazovky,
- spoločný top anchor, title baseline a trailing-action baseline,
- stabilný leading slot pre Back akciu bez posunu ostatných prvkov,
- zákaz lokálnych hardcoded top offsetov ako primárneho mechanizmu zarovnania zdieľaného headeru,
- nové `appPage.headerFamily.*` semantic tokeny,
- runtime parity gate v Light/Dark a pri podporovanom Dynamic Type.

## Adopcia

Prechod z 1.6.1 na 1.6.2 nevyžaduje migráciu používateľských dát. Aplikácia má skontrolovať obrazovky, ktoré používajú rovnaký produktový header pattern, a zjednotiť ich geometriu cez spoločný komponent alebo tokeny.
