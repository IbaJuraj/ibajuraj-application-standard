# IJAS-0012 – Header Family Alignment Contract

**Status:** Implemented  
**Target:** 1.6.2  
**Date:** 2026-08-20

## Problem

Rovnaký produktový header sa môže na rôznych obrazovkách vertikálne posúvať, najmä ak jedna obrazovka obsahuje Back akciu a iná nie. Lokálne `padding(.top)`, `offset(y:)` a individuálne safe-area kompenzácie vedú k viditeľnému skákaniu title a trailing Settings/system action.

## Decision

Obrazovky rovnakej header family používajú spoločný top anchor, title baseline a trailing-action baseline. Leading Back akcia obsadí stabilný slot a nesmie meniť geometriu ostatných prvkov. Zdieľaný komponent alebo tokeny sú preferovaným zdrojom pravdy.

## Verification

Runtime audit porovná referenčný root a peer/nested screen rovnakej rodiny v Light/Dark a pri podporovanom Dynamic Type. Source audit hľadá lokálne hardcoded top offsety na obrazovkách, ktoré majú zdieľať spoločný header pattern.
