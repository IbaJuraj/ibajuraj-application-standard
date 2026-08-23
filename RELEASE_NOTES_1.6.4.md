# IbaJuraj Application Standard 1.6.4

**Dátum vydania:** 23. august 2026
**Typ:** PATCH / backward-compatible UX & consistency hardening
**Kompatibilita:** bez migrácie doménových používateľských dát

## Prečo táto verzia vznikla
Runtime audit Lex Drive ukázal rozdielnu geometriu vizuálne rovnocenných navigačných prvkov: rozdielne icon-container shapes, rozmery a alignment. Súčasne sa ukázala potreba presnejšieho pravidla pre text fit v segmented/mode controls a pre skrytie nedokončených interných režimov pred bežným používateľom.

## Hlavné zmeny
- Component Family Geometry & Icon Contract,
- explicitný Navigation Tile & Icon Family token set,
- Shared Component First a No Local Geometry Drift,
- Text Fit, Localization & Mode-Control Readability Contract,
- Feature Maturity & Development Controls Exposure Contract,
- Whole-App Visual Consistency Gate,
- localization + Dynamic Type stress gate pre spoločné controls.

## Adopcia
Aplikácia pri prechode z 1.6.3 na 1.6.4 vykoná whole-app audit iba relevantných komponentových rodín. Produktovo odlišné komponenty sa nemajú násilne zjednocovať; rovnaká rola však nesmie driftovať medzi obrazovkami bez sémantického dôvodu alebo zdokumentovanej výnimky.
