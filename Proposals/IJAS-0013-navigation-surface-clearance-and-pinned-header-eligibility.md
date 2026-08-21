# IJAS-0013 – Navigation Surface Clearance & Pinned Header Eligibility

**Status:** Implemented  
**Target:** 1.6.3  
**Date:** 2026-08-21

## Problem

Runtime audity ukázali dva opačné layoutové problémy: posledný obsah môže byť prekrytý floating tab barom alebo môže po doscrollovaní zostať neprimerane veľká medzera. Zároveň automatické pripínanie section headerov môže zakrývať prvý riadok alebo súperiť s navigation headerom.

## Decision

Floating navigation používa dynamický bottom clearance podľa reálnej geometrie a safe area s kompaktnou 16–24 pt vizuálnou rezervou. Pinned header je oprávnený iba vtedy, keď pri dlhom katalógu reálne zachováva orientáciu; featured/úvodné sekcie sa nepripínajú automaticky.

## Verification

Runtime porovnanie peer root tabov pri úplnom doscrollovaní a scroll test každej pinned skupiny vrátane prvého riadku, safe area a navigation title.
