# IJAS-0016 – Runtime Regression & Debug Isolation

**Status:** Implemented  
**Target:** 1.6.3  
**Date:** 2026-08-21

## Problem

Runtime chyby odhalené reálnym vstupom sa môžu opakovať, ak po oprave nevznikne regresný test. Vývojárske mocky a diagnostické ovládanie sa tiež nesmú omylom dostať do používateľského Release UI.

## Decision

Potvrdená runtime chyba s realistickým rizikom opakovania má po oprave dostať behaviorálny regresný test alebo zdokumentovanú výnimku. Interné DEBUG/test fixtures a ovládacie prvky musia byť izolované od produkčného správania.

## Verification

Regresný test používa pôvodný používateľský scenár; Release audit kontroluje neprítomnosť developer UI a test fixture dát v produkčnej vetve.
