# IbaJuraj Application Standard 1.5.2

**Dátum:** 14. august 2026
**Typ:** backward-compatible patch

## Prečo vzniká

Standard 1.5.1 zaviedol správny neutral surface kontrakt, ale jeho pôvodné znenie bolo príliš prísne pre aplikácie, ktoré už používateľovi vedome ponúkajú produktovú Farebnú tému. V Kalkulačke 2v1 to spôsobilo regresiu: výber farebnej témy prestal meniť root background.

## Zmeny

- Predvolená téma naďalej používa spoločný neutral `appBackground`.
- Výslovne používateľom zvolená Farebná téma môže meniť root/background surface.
- Vzhľad a Farebná téma musia mať oddelený persistentný stav.
- Používateľská téma musí zostať čitateľná v podporovanom Light/Dark režime.
- Plný accent fill musí voliť kontrastný foreground (čierny alebo biely podľa fillu).
- Runtime gate dopĺňa test Predvolenej, svetlej a tmavej používateľskej témy.

## Kompatibilita

- Bez migrácie doménových používateľských dát.
- Aplikácie bez používateľských farebných tém nemusia meniť implementáciu 1.5.1 neutral surfaces.
- Aplikácie so zlúčeným appearance/theme stavom vykonajú jednorazovú migráciu preferencií.
