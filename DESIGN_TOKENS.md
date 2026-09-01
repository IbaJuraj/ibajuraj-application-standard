# IbaJuraj Application Standard 1.7.0 – Design Tokens

Tento dokument definuje spoločné referenčné tokeny. Token je baseline, nie náhrada adaptívneho layoutu.

## Spacing

| Token | Hodnota | Poznámka |
|---|---:|---|
| `space.xs` | 4 pt | jemné interné medzery |
| `space.sm` | 8 pt | kompaktný spacing |
| `space.md` | 12 pt | štandardný interný spacing |
| `space.lg` | 16 pt | sekčný/obsahový spacing |
| `space.xl` | 20–24 pt | väčší oddych medzi blokmi |

## Touch

- `touch.minimum`: **44 × 44 pt**
- Hit-area MAY byť väčšia než vizuálny symbol.

## Shared navigation tile

Peer tiles musia používať rovnaký variant a adaptovať sa cez obsah/container, nie per-screen offsetmi.

## Custom floating bottom navigation

Referenčná baseline pre `bottomNav.custom`:

| Token | Referencia |
|---|---:|
| `bottomNav.tabContentMin.compact` | 48 pt |
| `bottomNav.tabContentMin.regular` | 52 pt |
| `bottomNav.outerPadding` | 4 pt |
| `bottomNav.surfaceHeight.reference` | 60–66 pt |
| `bottomNav.radius` | 28 pt |
| `bottomNav.selectedRadius` | ~22 pt |
| `bottomNav.iconLabelSpacing` | 3 pt |
| `bottomNav.primaryAction.reference` | ~50 pt |
| `bottomNav.contentClearanceExtra` | 16–24 pt |

`surfaceHeight.reference` nie je rigidný frame. Pri Dynamic Type alebo inom kontejnery MAY výška rásť.

## Calculator Key adaptive family

- minimum hit target: 44 pt,
- final key size sa SHOULD odvodzovať z dostupnej šírky aj výšky,
- key size SHOULD mať min/max clamp,
- growth na veľkom displeji SHOULD využiť voľný priestor,
- ochranný top anchor MUST zostať stabilný, ak oddeľuje keypad od výsledkového obsahu,
- spacing MAY mierne rásť po vyčerpaní vhodného key-size rastu.

## About / Settings shared identifiers

| Role | accessibility/test ID |
|---|---|
| Settings About row | `ij.settings.about.row` |
| About Version card | `ij.about.version.card` |
| About Standard card | `ij.about.standard.card` |
| About Developer card | `ij.about.developer.card` |
| About Web row | `ij.about.web.row` |
| About Privacy row | `ij.about.privacy.row` |
| Custom bottom nav | `ij.bottomnav.container` |
| Bottom nav primary action | `ij.bottomnav.primaryAction` |
| Appearance mode control | `ij.appearance.mode.control` |
| Theme selection container | `ij.appearance.theme.list` |

## Semantic surfaces

Shared semantic roles must preserve family parity in Light/Dark:
- `background`
- `surface`
- `elevatedSurface`
- `primaryText`
- `secondaryText`
- `separator`
- `disabled`
- `accent`
- `success`
- `warning`
- `danger`

Product-selected theme MAY tint background/accent, but must preserve contrast and semantic meaning.

## Viewport edge utilization

| Token | Referencia |
|---|---:|
| `rootHeader.extraTopInset.reference` | **0–4 pt** |
| `viewport.horizontalInset.compact` | **16–20 pt** podľa family |
| `viewport.horizontalInset.regular` | **18–24 pt** podľa family |
| `viewport.contentMaxWidth` | produktovo/family špecifický; MUST byť container-driven |
| `bottomChrome.finalContentClearance` | **16–24 pt** vizuálnej rezervy po doscrollovaní |

`rootHeader.extraTopInset.reference` sa aplikuje **po top safe area**, nie od fyzického okraja displeja. Väčší inset vyžaduje zdôvodnenie.

Custom bottom surface MAY vstúpiť do bottom safe area; jeho interaktívny obsah však nesmie kolidovať s Home Indicatorom. `bottomChrome.finalContentClearance` je rezerva **obsahu nad chrome**, nie medzera pod chrome.

## Shared viewport/test identifiers

| Role | accessibility/test ID |
|---|---|
| Primary root title | `ij.root.title` |
| Nested/system navigation header | `ij.navigation.header` |
