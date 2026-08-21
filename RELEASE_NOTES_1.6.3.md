# IbaJuraj Application Standard 1.6.3

**Dátum vydania:** 21. august 2026  
**Typ:** PATCH / backward-compatible quality & safety hardening  
**Kompatibilita:** bez migrácie doménových používateľských dát

## Prečo táto verzia vznikla

Runtime audity v aplikáciách ukázali opakované problémy, ktoré už nie sú iba produktovo špecifické: nesprávny clearance nad floating navigáciou, automaticky pripínané sekčné headre, rozdielna geometria rovnakých komponentov a riziko presvedčivej, ale nepodloženej odpovede pri AI/generovaných funkciách. Súčasne audit samotného Standardu 1.6.2 odhalil niekoľko historických dokumentačných nekonzistencií.

## Hlavné zmeny

- Floating Tab Bar Content Clearance Contract,
- Pinned Header Eligibility Contract,
- Rotating Content Pattern – MAY,
- Verified AI & Generated Assistance Contract,
- safe low-confidence fallback a zákaz nesúvisiaceho „najbližšieho“ výsledku,
- Missing Knowledge / feedback pattern s preview pred odoslaním,
- Authoritative Data Separation & Traceability Contract,
- temporal integrity a conflict-safety hardening,
- runtime regression → behaviorálny test pattern,
- explicitná produkčná izolácia DEBUG/mock/test controls,
- spresnenie source-hygiene review pravidiel.

## Upratanie Standardu

- `TEST_MATRIX.md` má správny aktuálny nadpis 1.6.3,
- historický changelog rozlišuje 1.4.1 a 1.5.0,
- opravená nesprávna identita `RELEASE_NOTES_1.4.1.md`,
- odstránená duplicitná lokalizačná veta v hlavnom štandarde.

## Adopcia

Aplikácia pri prechode z 1.6.2 na 1.6.3 vykoná iba tie gate, ktoré zodpovedajú jej funkciám. Produkty s floating bottom navigation overia clearance; produkty s pinned headrami eligibility a scroll runtime; produkty s AI/generovanou asistenciou vykonajú grounded-answer/fallback/debug-isolation audit; produkty s autoritatívnymi alebo časovo verziovanými dátami overia source traceability a temporal resolver.
