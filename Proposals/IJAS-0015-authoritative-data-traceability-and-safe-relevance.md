# IJAS-0015 – Authoritative Data Traceability & Safe Relevance

**Status:** Implemented  
**Target:** 1.6.3  
**Date:** 2026-08-21

## Problem

Paralelné hardcoded kópie autoritatívnych údajov v UI a „najbližší“ výsledok bez dostatočnej relevancie môžu vytvoriť používateľsky presvedčivý, ale nesprávny stav. Časovo verziované údaje navyše potrebujú zachovať históriu.

## Decision

Autoritatívny údaj má jeden zdroj pravdy, presentation model je iba odvodený a výsledok je podľa rizika dohľadateľný k stabilnej identite, verzii/časovej platnosti a stavu overenia. Nízka relevance nesmie automaticky vybrať nesúvisiacu vetvu. Nová časová verzia neprepisuje historický význam.

## Verification

Source audit paralelných modelov, temporal regression test a test nízkej relevancie/konfliktných zdrojov.
