# IJAS-0010 – User-selected theme surface and accent contrast

**Status:** implemented  
**Target:** IbaJuraj Application Standard 1.5.2  
**Date:** 2026-08-14

## Problem

Standard 1.5.1 správne zjednotil neutrálne surfaces, ale príliš široké znenie neúmyselne deaktivovalo existujúcu používateľskú funkciu farebného root backgroundu v Kalkulačke 2v1. Zároveň sa ukázalo, že pevný biely foreground na svetlých accent farbách môže mať nedostatočný kontrast.

## Decision

- Predvolená téma zostáva family-neutral.
- Explicitne používateľom zvolená produktová farebná téma MAY zmeniť root/background surface.
- Vzhľad a Farebná téma MUST mať oddelený persistentný stav, ak existujú súčasne.
- Card/text semantic roly zostávajú spoločné, pokiaľ nejde o explicitnú product/brand surface.
- Foreground na plnom accent fille MUST adaptovať kontrast.

## Migration

Aplikácia s historicky spojeným appearance/theme enumom vykoná jednorazovú migráciu preference kľúčov. Doménové používateľské dáta sa nemenia.

## Verification

Runtime audit overí Predvolenú tému, minimálne jednu svetlú a jednu tmavú používateľskú tému, oddelenú persistence a kontrast plných accent prvkov.
