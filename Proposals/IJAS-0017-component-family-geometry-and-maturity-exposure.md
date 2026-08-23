# IJAS-0017 – Component Family Geometry & Maturity Exposure

**Status:** accepted
**Target:** Standard 1.6.4
**Date:** 2026-08-23

## Problem
Runtime audit Lex Drive ukázal, že vizuálne rovnocenné navigačné položky môžu driftovať medzi kruhovými a rounded-square icon containers, rozdielnou veľkosťou, paddingom a text alignmentom. Zároveň interné Auto/Classic/AI Test ovládanie môže byť technicky dostupné skôr, než je capability pripravená pre používateľa.

## Decision
Rovnaká komponentová rola používa spoločný geometry contract. Výnimka musí mať odlišnú sémantickú rolu alebo byť zdokumentovaná. Dôležitý text musí prežiť localization/Dynamic Type bez clippingu. Nedokončené/experimentálne capability a development routing controls sa nezobrazujú ako bežné používateľské režimy.

## Scope
Navigation tiles, navigation/list rows, icon containers, segmented/mode controls, shared interaction states a whole-app visual consistency audit.

## Compatibility
PATCH; bez migrácie doménových používateľských dát.
