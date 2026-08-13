# IbaJuraj Design Tokens

**Verzia:** 1.5.1  
**Stav:** autoritatívny spoločný register  
**Platnosť od:** 13. augusta 2026

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
| `summaryShortcut.compact` | 150 pt | 112 pt | Krátky názov a počet alebo stav; adaptívna dvojica |
| `entityCard.standard` | podľa kontajnera | 96 pt | Výška rastie podľa stavu a kontextu |
| `walletCard.compact` | 150 pt | podľa pomeru strán | Predvolene pomer približne 1,586 : 1 |
| `featureCard` | podľa kontajnera | 144 pt | Obsahová výška, nie pevné maximum |
| `listRow.standard` | podľa kontajnera | 64 pt | Výška rastie podľa obsahu a Dynamic Type |
| `searchField.standard` | podľa kontajnera | 52 pt | Zachová minimálnu dotykovú plochu |
| `calculatorKey.standard` | podľa produktovej matice | 44 pt | Doménový variant; dotyková plocha nesmie byť menšia než minimum |

Referenčná minimálna veľkosť MUST NOT byť použitá ako pevná maximálna veľkosť. Ak obsah potrebuje viac priestoru, komponent sa zväčší alebo sa mriežka zmení na menší počet stĺpcov.

## Typografia koreňovej obrazovky

| Token | Hodnota | Typ |
|---|---|---|
| `appPage.title` | `.largeTitle.weight(.bold)` | `exact` |
| `appPage.subtitle` | `.subheadline` + sekundárna farba | `exact` |
| `appPage.titleSubtitleGap` | 6 pt | `exact` |
| `appPage.titleLineBehavior` | Dynamic Type; bez lokálneho bodového override a bez `minimumScaleFactor` | `semantic` |
| `appPage.subtitleLineBehavior` | prirodzené viacriadkové zalomenie | `semantic` |

- Tokeny `appPage.*` sa používajú na hlavnom pracovnom root headri aplikácie alebo hlavného produktového tabu.
- Rovnaká rola MUST vyzerať typograficky rovnako naprieč aplikáciami, aj keď sa text a dĺžka podnadpisu líšia.
- Vnorené navigačné titulky, produktové hero nadpisy a transakčné sheet headre používajú svoje sémantické systémové roly a nie sú `appPage.title`.

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
| `settings.appearance.headerHorizontalPadding` | 16 pt |
| `settings.appearance.headerTopPadding` | 10 pt |
| `settings.appearance.segmentHorizontalPadding` | 16 pt |
| `settings.appearance.segmentBottomPadding` | 10 pt |
| `settings.divider.leadingInset` | 64 pt |
| `information.group.radius` | 20 pt |
| `information.row.horizontalPadding` | 16 pt |
| `information.row.verticalPadding` | 16 pt |
| `information.row.dividerLeadingInset` | 64 pt |

- Section header SHOULD používať lokalizovaný uppercase štýl `.footnote` so semibold váhou a sekundárnou farbou.
- Názov riadku MUST používať Dynamic Type; predvolená rola je `.body` alebo `.headline` podľa hierarchie.
- Krátka stavová hodnota vpravo SHOULD používať `.subheadline` a sekundárnu farbu; MUST sa bezpečne presunúť pod názov, ak sa vedľa neho nezmestí.
- Názov ani trailing hodnota MUST NOT používať `minimumScaleFactor` ako náhradu responzívneho rozloženia.
- Ikonová dlaždica MAY používať produktový alebo sémantický tint, ale MUST zachovať spoločný rozmer, radius a kontrast.
- Systémový segmented control SHOULD byť použitý pre priamu voľbu **Automaticky / Svetlý / Tmavý**; MUST NOT byť zmenšený pod použiteľnú dotykovú plochu.
- Tri alebo viac neinteraktívnych vysvetľujúcich riadkov rovnakej roly SHOULD používať jeden `information.group` kontajner a vnútorné oddeľovače namiesto série samostatných vysokých kariet.

- Pre rovnaký settings row je poradie modifierov súčasťou geometrického kontraktu: obsah → `.padding(.horizontal, 16)` → `.padding(.vertical, 10)` → `.frame(minHeight: 56)`. `frame(minHeight:)` pred paddingom MUST NOT byť použitý, pretože vytvorí vyšší výsledný komponent.
- Karta **Vzhľad** používa header s `settings.iconTile.size`, horizontálnym paddingom 16 pt a horným paddingom 10 pt; segmented control používa minimálnu hit výšku 44 pt, horizontálny padding 16 pt a spodný padding 10 pt.
- Divider medzi settings riadkami SHOULD začínať na 64 pt od leading hrany spoločnej karty, ak produktový variant nemá zdokumentovaný dôvod na iný inset.

## Navigačný surface a odkazy

| Token | Hodnota | Typ |
|---|---|---|
| `navigation.surface` | sémantický `background` alebo `elevatedSurface` | `semantic` |
| `navigation.internalIndicator` | `chevron.right` | `exact` |
| `navigation.externalIndicator` | `arrow.up.right.square` | `exact` |

- `navigation.surface` MUST zachovať čitateľnosť inline titulku počas posúvania a MUST zabrániť presvitaniu konkurenčného textu pod titulkom.
- Interný push cieľ MUST používať `navigation.internalIndicator`; externá URL MUST používať `navigation.externalIndicator` alebo rovnocenný systémový symbol.

## Kontakt

| Token | Hodnota | Typ |
|---|---:|---|
| `contact.primaryAction.minimumHeight` | 64 pt | `minimum` |
| `contact.action.horizontalPadding` | 16 pt | `exact` |
| `contact.action.verticalPadding` | 16 pt | `exact` |
| `contact.action.iconSize` | 42 × 42 pt | `exact` |
| `contact.action.iconRadius` | 12 pt | `exact` |
| `contact.action.contentGap` | 13 pt | `exact` |
| `contact.action.radius` | 20 pt | `exact` |
| `contact.actionGap` | 12 pt | `exact` |
| `contact.screen.contentSpacing` | 18 pt | `exact` |
| `contact.screen.pageInset` | 16 pt | `exact` |
| `contact.maximumPrimaryActions` | 2 | `maximum` |

- Kontaktná obrazovka SHOULD používať krátky úvod, samostatnú akciu formulára, samostatnú akciu Telegramu a kompaktné upozornenie na citlivé údaje.
- Produktová sekcia **Čo môžete poslať** používa obsahovú výšku a MUST NOT byť uzamknutá na pevné maximum.
- Ak text hlavnej akcie zaberá rovnaký počet riadkov, výsledná geometria akčnej karty MUST byť rovnaká naprieč aplikáciami.

## O aplikácii

| Token | Hodnota | Typ |
|---|---:|---|
| `about.screen.contentSpacing` | 18 pt | `exact` |
| `about.screen.pageInset` | 20 pt | `exact` |
| `about.metadata.radius` | 18 pt | `exact` |
| `about.metadata.padding` | 16 pt | `exact` |
| `about.metadata.iconColumnWidth` | 24 pt | `exact` |
| `about.action.radius` | 18 pt | `exact` |
| `about.action.padding` | 16 pt | `exact` |
| `about.action.iconColumnWidth` | 24 pt | `exact` |
| `about.actionGap` | 12 pt | `exact` |

- Metadata **Verzia**, **IbaJuraj Application Standard** a **Vývojár** používajú rovnaký metadata variant; produktový text MAY zväčšiť výšku pri reálnom zalomení.
- Akčné riadky Web, súkromie, novinky, stav aplikácie, právne upozornenie, hodnotenie alebo zdieľanie používajú rovnaký `about.action` variant podľa sémantiky interného alebo externého odkazu.

## Adaptívna mriežka

- Dva stĺpce sa MAY použiť iba vtedy, keď po odpočítaní okrajov a medzery zostáva každému prvku minimálne 150 bodov a obsah je čitateľný.
- Pri menšej dostupnej šírke alebo accessibility texte MUST mriežka prejsť na jeden stĺpec.
- Na veľkom displeji SHOULD dlaždica zachovať rozumnú maximálnu šírku a mriežka SHOULD pracovať s okrajmi alebo ďalším stĺpcom podľa produktového významu.
- Karty v jednom riadku MUST používať rovnakú výslednú výšku; ďalší riadok MAY mať inú obsahovú výšku.
- Dvojica `summaryShortcut.compact` MAY zostať v dvoch stĺpcoch; pri šírke pod minimum alebo pri accessibility texte MUST použiť jeden stĺpec.

## Typografia a farby

- Text MUST používať Dynamic Type štýly.
- Sémantické farby MUST rozlišovať minimálne `accent`, `success`, `warning`, `danger`, `information`, `background`, `surface` a `elevatedSurface`.
- Stav MUST mať aj textový, ikonový alebo iný nefarený nositeľ významu.
- Produktový akcent MAY byť odlišný, ak zostáva konzistentný a spĺňa kontrast.


## 1.5.1 – Neutral Surface & Text Color Contract

| Token | Light | Dark | Preferovaná systémová mapa | Záväznosť |
|---|---|---|---|---|
| `color.appBackground` | približne `#F2F2F7` | `#000000` | `systemGroupedBackground` / `systemBackground` | `MUST` |
| `color.cardSurface` | `#FFFFFF` | približne `#1C1C1E` | `secondarySystemGroupedBackground` | `MUST` |
| `color.elevatedSurface` | systémová secondary/elevated surface | systémová secondary/elevated surface | platform semantic color | `MAY` podľa role |
| `color.textPrimary` | `#000000` | `#FFFFFF` | `label` / `primary` | `MUST` |
| `color.textSecondary` | približne `#8E8E93` | približne `#8E8E93` | `secondaryLabel` / `secondary` | `MUST` |
| `color.separator` | platform separator | platform separator | `separator` | `MUST` |
| `color.disabled` | platform semantic disabled | platform semantic disabled | semantic disabled/tertiary | `MUST` |

- Hex hodnoty sú referenčný vizuálny cieľ, nie dôvod obísť sémantické systémové farby.
- Bežný neutrál text SHOULD NOT používať lokálne `.gray`, `.white.opacity(...)` ani `.black.opacity(...)`, ak existuje zodpovedajúca sémantická rola.
- Brand surface MAY obísť `color.cardSurface`, ale MUST zachovať kontrast textu a indikátorov.
- Rovnaký token MUST mať rovnaký vizuálny výsledok v každej aplikácii rodiny IbaJuraj.

## 1.5.0 – spoločné interaction a content-density tokeny

### Search

| Token | Hodnota | Poznámka |
|---|---:|---|
| `search.field.minimumHeight` | 52 pt | minimum; väčší obsah MAY zväčšiť výšku |
| `search.field.radius` | 18–22 pt | range podľa surface variantu |
| `search.field.horizontalPadding` | 16 pt | preferred |
| `search.field.iconSize` | 20–22 pt | range |
| `search.filter.minimumHitArea` | 44 pt | minimum |
| `search.filter.spacing` | 8 pt | preferred |

### Primary CTA a empty state

| Token | Hodnota | Poznámka |
|---|---:|---|
| `button.primary.minimumHeight` | 52 pt | minimum |
| `button.primary.radius` | 18–26 pt | range podľa šírky/role |
| `button.primary.horizontalPadding` | 18 pt | preferred |
| `emptyState.contentSpacing` | 8–12 pt | range |
| `emptyState.maximumPrimaryActions` | 1 | exact |

### Badge / label

| Token | Hodnota | Poznámka |
|---|---:|---|
| `badge.minimumHeight` | 22 pt | minimum |
| `badge.horizontalPadding` | 8 pt | preferred |
| `badge.radius` | 11 pt alebo capsule | semantic variant |
| `badge.minimumContrastRatio` | 4.5:1 text | cieľ pre bežný text |
| `badge.iconMinimumContrastRatio` | 3:1 | cieľ pre významovú grafiku |

Badge na produktovej farbe MUST adaptovať foreground/background. Pevný „favorite yellow“ nie je spoločný token; obľúbenosť je sémantická rola a musí zostať čitateľná aj na žltom, zelenom alebo inom brand surface.

### User label / market badge

- `card.userLabel.fontRole`: `caption` alebo ekvivalent sekundárnej role.
- `card.userLabel.lineLimit`: 1 preferred; MAY prejsť na 2 pri širšom detaile.
- `card.marketBadge.maximumCharacters`: krátke systémové/trhové označenie, typicky 2–4 znaky.
- Prázdny `userLabel` MUST NOT rezervovať samostatný riadok.

### Responsive content

| Token | Hodnota | Poznámka |
|---|---:|---|
| `content.phone.horizontalMargin` | 16–20 pt | range |
| `content.pad.maximumReadableWidth` | 760–980 pt | range podľa typu obrazovky |
| `grid.minimumCardWidth` | 150 pt | minimum pre dvojstĺpcové produktové karty |
| `grid.spacing` | 12–16 pt | range |

### Motion

| Token | Hodnota | Poznámka |
|---|---:|---|
| `motion.micro.preferredDuration` | 0.18–0.25 s | range |
| `motion.state.preferredDuration` | 0.20–0.35 s | range |
| `motion.reduceMotionFallback` | no-essential-motion | exact semantic rule |

### Source hygiene quality thresholds

- `source.workflowFile.reviewThresholdLines`: **430** (SHOULD audit, nie hard compile limit).
- `source.rootView.role`: composition/navigation preferred.
- `source.unusedProductionFiles`: 0 preferred; každá výnimka má byť zdokumentovaná.
