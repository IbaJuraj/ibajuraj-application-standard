# IbaJuraj Design Tokens

**Verzia:** 1.3.0  
**Stav:** autoritatívny spoločný register  
**Platnosť od:** 10. augusta 2026

Tento register definuje spoločné počiatočné hodnoty. Aplikácia ich MUST používať prostredníctvom centrálneho theme alebo foundation rozhrania, nie opakovanými číslami v jednotlivých obrazovkách.

## Typ záväznosti tokenu

| Typ | Význam |
|---|---|
| `exact` | spoločný komponent používa presnú hodnotu |
| `minimum` | hodnota je dolná hranica a komponent MAY rásť |
| `maximum` | hodnota je horná hranica |
| `preferred` | odporúčaná predvolená hodnota v povolenom rozsahu |
| `range` | povolený interval spätne kompatibilných hodnôt |
| `semantic` | pravidlo správania bez jednej numerickej hodnoty |

Ak tabuľka neuvádza inak, spacing a radius tokeny sú `exact`, minimálne rozmery sú `minimum` a obsahová výška je `semantic`. Produktový token MAY centrálny register rozšíriť, ale MUST NOT prepísať spoločný token pod rovnakým názvom.

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
| `calculatorKey.standard` | podľa produktovej matice | 44 pt | Doménový variant; dotyková plocha nesmie byť menšia než minimum |

Referenčná minimálna veľkosť MUST NOT byť použitá ako pevná maximálna veľkosť. Ak obsah potrebuje viac priestoru, komponent sa zväčší alebo sa mriežka zmení na menší počet stĺpcov.

## Hlavička a vstup do Nastavení

| Token | Hodnota | Typ |
|---|---:|---|
| `header.action.visualDiameter` | 42 pt | `preferred` |
| `header.action.visualDiameterRange` | 42–48 pt | `range` |
| `header.action.hitArea` | 44 × 44 pt | `minimum` |
| `header.action.settingsSymbol` | 18 pt | `preferred` |
| `header.action.secondarySymbol` | 17 pt | `preferred` |
| `header.action.clusterGap` | 6 pt | `exact` |
| `header.action.maximumPerSide` | 2 | `maximum` |
| `header.action.pressedScale` | 0.97 | `preferred` |
| `header.action.pressedOpacity` | 0.82 | `preferred` |

- Akcia Nastavení MUST používať `gearshape.fill`, kruhový vizuálny kontajner a accessibility label **Nastavenia**.
- Nastavenia MUST byť pravou krajnou akciou hlavnej obrazovky.
- Hit area MAY presahovať vizuálny kruh a MUST zostať minimálne 44 × 44 pt.
- Odsadenie sa počíta od aktuálnej safe area, nie od fyzického okraja zariadenia.
- Surface, pressed state a animácia MUST používať sémantické farby a rešpektovať Reduce Motion.

## Nastavenia

### Vstupné tlačidlo

Nasledujúce tokeny z 1.2.0 zostávajú platné ako spätne kompatibilný variant do odstránenia v budúcej major verzii. Nové implementácie SHOULD používať `header.action.*`.

| Token | Hodnota | Stav |
|---|---:|---|
| `settings.entry.container` | 48 × 48 pt | deprecated alias/variant |
| `settings.entry.symbol` | 20 pt | deprecated alias/variant |
| `settings.entry.radius` | 24 pt | deprecated alias/variant |
| `settings.entry.trailingInset` | 16 pt compact / 20 pt regular | active |
| `settings.entry.pressedScale` | 0.97 | alias `header.action.pressedScale` |
| `settings.entry.pressedOpacity` | 0.82 | alias `header.action.pressedOpacity` |

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
- Názov ani trailing hodnota MUST NOT používať `minimumScaleFactor` ako náhradu responzívneho rozloženia.
- Ikonová dlaždica MAY používať produktový alebo sémantický tint, ale MUST zachovať spoločný rozmer, radius a kontrast.
- Systémový segmented control SHOULD byť použitý pre priamu voľbu **Automaticky / Svetlý / Tmavý**; MUST NOT byť zmenšený pod použiteľnú dotykovú plochu.

## Kontakt

| Token | Hodnota | Typ |
|---|---:|---|
| `contact.primaryAction.minimumHeight` | 64 pt | `minimum` |
| `contact.actionGap` | 12 pt | `exact` |
| `contact.maximumPrimaryActions` | 2 | `maximum` |

- Kontaktná obrazovka SHOULD používať krátky úvod, samostatnú akciu formulára, samostatnú akciu Telegramu a kompaktné upozornenie na citlivé údaje.
- Produktová sekcia **Čo môžete poslať** používa obsahovú výšku a MUST NOT byť uzamknutá na pevné maximum.

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
