# IbaJuraj Design Tokens

**Verzia:** 1.2.0  
**Stav:** autoritatívny spoločný register  
**Platnosť od:** 9. augusta 2026

Tento register definuje spoločné počiatočné hodnoty. Aplikácia ich MUST používať prostredníctvom centrálneho theme alebo foundation rozhrania, nie opakovanými číslami v jednotlivých obrazovkách.

## Rozostupy

| Token | Hodnota |
|---|---:|
| `space.xs` | 4 pt |
| `space.sm` | 8 pt |
| `space.md` | 12 pt |
| `space.lg` | 16 pt |
| `space.xl` | 24 pt |
| `space.xxl` | 32 pt |
| `layout.pageInsetCompact` | 16 pt |
| `layout.pageInsetRegular` | 20 pt |
| `layout.gridGap` | 12 pt |
| `layout.maximumReadableWidth` | 720 pt |

## Zaoblenie a dotyk

| Token | Hodnota |
|---|---:|
| `radius.small` | 12 pt |
| `radius.medium` | 16 pt |
| `radius.large` | 22 pt |
| `radius.feature` | 28 pt |
| `touch.minimum` | 44 × 44 pt |
| `iconContainer.compact` | 36 × 36 pt |
| `iconContainer.standard` | 44 × 44 pt |
| `iconContainer.feature` | 52 × 52 pt |

## Komponentové varianty

| Variant | Referenčná minimálna šírka | Referenčná minimálna výška | Poznámka |
|---|---:|---:|---|
| `navigationTile.compact` | 150 pt | 124 pt | Dvojstĺpcová kategória alebo rýchla akcia |
| `entityCard.standard` | podľa kontajnera | 96 pt | Výška rastie podľa stavu a kontextu |
| `walletCard.compact` | 150 pt | podľa pomeru strán | Predvolene pomer približne 1,586 : 1 |
| `featureCard` | podľa kontajnera | 144 pt | Obsahová výška, nie pevné maximum |
| `listRow.standard` | podľa kontajnera | 64 pt | Výška rastie podľa obsahu a Dynamic Type |
| `searchField.standard` | podľa kontajnera | 52 pt | Zachová minimálnu dotykovú plochu |

Referenčná minimálna veľkosť MUST NOT byť použitá ako pevná maximálna veľkosť. Ak obsah potrebuje viac priestoru, komponent sa zväčší alebo sa mriežka zmení na menší počet stĺpcov.

## Nastavenia

### Vstupné tlačidlo

| Token | Hodnota |
|---|---:|
| `settings.entry.container` | 48 × 48 pt |
| `settings.entry.symbol` | 20 pt |
| `settings.entry.radius` | 24 pt |
| `settings.entry.trailingInset` | 16 pt compact / 20 pt regular |
| `settings.entry.pressedScale` | 0.97 |
| `settings.entry.pressedOpacity` | 0.82 |

- Symbol MUST byť `gearshape.fill`.
- Kontajner MUST byť kruhový a používať sémantický surface alebo jemne tónovaný accent surface s dostatočným kontrastom.
- Odsadenie sa počíta od aktuálnej safe area, nie od fyzického okraja zariadenia.
- Stlačený stav MUST byť viditeľný a SHOULD rešpektovať Reduce Motion.

### Grouped-card rozloženie

| Token | Hodnota |
|---|---:|
| `settings.group.radius` | 22 pt |
| `settings.group.horizontalPadding` | 16 pt |
| `settings.sectionSpacing` | 24 pt |
| `settings.row.minimumHeight` | 56 pt |
| `settings.row.horizontalPadding` | 16 pt |
| `settings.row.verticalPadding` | 10 pt |
| `settings.iconTile.size` | 36 × 36 pt |
| `settings.iconTile.radius` | 10 pt |
| `settings.chevron.symbol` | `chevron.right` |
| `settings.segmented.minimumHitHeight` | 44 pt |

- Section header SHOULD používať lokalizovaný uppercase štýl `.footnote` so semibold váhou a sekundárnou farbou.
- Názov riadku MUST používať Dynamic Type; predvolená rola je `.body` alebo `.headline` podľa hierarchie.
- Krátka stavová hodnota vpravo SHOULD používať `.subheadline` a sekundárnu farbu; MUST sa bezpečne presunúť pod názov, ak sa vedľa neho nezmestí.
- Ikonová dlaždica MAY používať produktový alebo sémantický tint, ale MUST zachovať spoločný rozmer, radius a kontrast.
- Systémový segmented control SHOULD byť použitý pre priamu voľbu **Automaticky / Svetlý / Tmavý**; MUST NOT byť zmenšený pod použiteľnú dotykovú plochu.

## Adaptívna mriežka

- Dva stĺpce sa MAY použiť iba vtedy, keď po odpočítaní okrajov a medzery zostáva každému prvku minimálne 150 bodov a obsah je čitateľný.
- Pri menšej dostupnej šírke alebo accessibility texte MUST mriežka prejsť na jeden stĺpec.
- Na veľkom displeji SHOULD dlaždica zachovať rozumnú maximálnu šírku a mriežka SHOULD pracovať s okrajmi alebo ďalším stĺpcom podľa produktového významu.
- Karty v jednom riadku MUST používať rovnakú výslednú výšku; ďalší riadok MAY mať inú obsahovú výšku.

## Typografia a farby

- Text MUST používať Dynamic Type štýly.
- Sémantické farby MUST rozlišovať minimálne `accent`, `success`, `warning`, `danger`, `information`, `background`, `surface` a `elevatedSurface`.
- Stav MUST mať aj textový, ikonový alebo iný nefarený nositeľ významu.
- Produktový akcent MAY byť odlišný, ak zostáva konzistentný a spĺňa kontrast.
