# IJAS-0014 – Verified AI, Generated Assistance & Feedback

**Status:** Implemented
**Target:** 1.6.3
**Date:** 2026-08-21

## Problem

Generatívny model môže formulovať presvedčivú odpoveď aj vtedy, keď aplikácia nemá dostatočný autoritatívny podklad. Nedostupnosť AI navyše nesmie rozbiť funkciu, ktorá už má deterministický základ.

## Decision

Autoritatívne fakty deklarované ako overené musia pochádzať z dôveryhodného zdroja aplikácie alebo explicitne overeného vstupu. AI smie vysvetľovať a interpretovať, ale nesmie potichu nahradiť existujúcu autoritatívnu logiku. Pri nízkej istote sa použije clarification/fallback. Feedback sa neodosiela automaticky a používateľ vidí prenášaný kontext. DEBUG/mock režimy nesmú byť v produkčnom UI.

## Verification

Grounded-answer test, low-confidence test, unavailable-model fallback, feedback preview a Release build bez developer ovládania.
