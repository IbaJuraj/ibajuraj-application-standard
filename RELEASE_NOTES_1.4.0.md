# IbaJuraj Application Standard 1.4.0

**Dátum:** 13. augusta 2026  
**Typ:** MINOR – spätne kompatibilné spoločné UX pravidlá

## Prečo vznikla verzia 1.4.0

Pri runtime porovnaní aplikácií IbaJuraj sa ukázalo, že rovnaké obrazovky používali podobný vizuálny jazyk, ale rozdielnu hustotu: jedna aplikácia mala vyššie settings riadky, väčší segmented Vzhľad alebo väčšie medzery v Kontakt/O aplikácii. 1.4.0 mení spoločný vizuálny systém z približnej podobnosti na merateľný geometrický kontrakt.

## Hlavné zmeny

- Settings row: 16 pt horizontálny a 10 pt vertikálny padding, 36 × 36 pt ikonová dlaždica, minimálna výsledná výška 56 pt.
- SwiftUI poradie: padding sa aplikuje pred `frame(minHeight:)`, aby sa výsledná výška umelo nezväčšovala.
- Vzhľad: rovnaký header a segmented control s minimálnou 44 pt dotykovou výškou, 16 pt horizontálnym a 10 pt horným/spodným paddingom.
- Grouped settings: radius 22 pt, section spacing 24 pt, divider inset 64 pt.
- Kontakt: 16 pt card padding, 42 × 42 pt ikonový box, radius 20 pt, gap 12 pt.
- O aplikácii: radius 18 pt, padding 16 pt, ikonový stĺpec 24 pt, gap 12 pt.
- Rovnaký komponent s rovnakým obsahom musí mať rovnakú základnú geometriu vo všetkých aplikáciách.

## Dopad na aplikácie

Nie je potrebná migrácia používateľských dát. Každá aplikácia má v najbližšom UI builde vykonať geometry audit a odstrániť lokálne rozmery, ktoré duplikujú spoločné tokeny. Odlišné produktové funkcie a počet položiek zostávajú povolené.

## Release dôkaz

Adopcia Level 2 a vyššia má obsahovať side-by-side screenshoty obrazoviek Nastavenia, Kontakt a O aplikácii, aby bolo možné overiť hustotu spoločných komponentov.
