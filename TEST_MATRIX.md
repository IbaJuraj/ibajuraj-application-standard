# IbaJuraj Application Standard 1.7.0 RC2 – Test Matrix

## Povinné vrstvy

| Vrstva | Čo dokazuje | Čo nedokazuje |
|---|---|---|
| Static conformance | contracty, pin, capability flags, screen inventory, localization parity | živé UI správanie |
| Unit/XCTest | deterministická logika, metadata provider, layout math, oddelenie bar position/clearance | reálne clipping/safe-area |
| UI test | navigácia, shared surfaces, selected state, live appearance, stabilné identifiers | všetky zariadenia bez matice |
| Runtime acceptance | fyzický viewport, safe area, Dynamic Type, keyboard, platform interaction | regresiu do budúcna bez automatizácie |

## Adaptive + viewport matrix – každá iPhone aplikácia
- [ ] Small container
- [ ] Regular container
- [ ] Large container
- [ ] Accessibility Dynamic Type
- [ ] Light
- [ ] Dark
- [ ] Longest supported localization
- [ ] top root anchor po live safe area
- [ ] peer-root top-anchor parity
- [ ] bottom fixed/custom chrome čo najnižšie, ak existuje
- [ ] Home Indicator bez kolízie
- [ ] horizontal utilization / max-width
- [ ] scroll endpoint + 16–24 pt final content reserve
- [ ] empty/loading/populated/error geometry stability podľa relevantnosti
- [ ] system-overlay/live-safe-area response
- [ ] keyboard/form state, ak aplikovateľné
- [ ] bez viditeľného layout thrash/lag pri scrollovaní a prepínaní rootov

## Screen-family gate
Manifest musí obsahovať konkrétne obrazovky pre každú aplikovateľnú family:
- [ ] `SCREEN-ROOT`
- [ ] `SCREEN-SETTINGS` + `SCREEN-ABOUT`, ak Settings existujú
- [ ] `SCREEN-DETAIL`, ak detaily existujú
- [ ] `SCREEN-FORM`, ak formuláre existujú
- [ ] `SCREEN-SEARCH`, ak search existuje
- [ ] `SCREEN-SHEET`, ak sheets existujú
- [ ] `SCREEN-FULLSCREEN`, ak fullscreen flow existuje
- [ ] `SCREEN-ONBOARDING`, ak onboarding existuje
- [ ] `SCREEN-STATES`, ak appka má meaningful empty/loading/error surface
- [ ] `SCREEN-BOTTOM-NAV`, ak bottom navigation existuje
- [ ] každý `pass` má runtime evidence
- [ ] žiadny release-blocking `pending` pri Level 4

## iPad – ak podporované
- [ ] Portrait
- [ ] Landscape
- [ ] Supported window/multitasking sizes

## iPhone-only compatibility – ak systém umožní
- [ ] iPad compatibility presentation kritického workflow

## Shared Settings/About
- [ ] `STD-ABOUT-001` row title/subtitle/trailing format
- [ ] `STD-ABOUT-002` runtime version sentence
- [ ] `STD-ABOUT-003` public Standard version only
- [ ] `STD-ABOUT-004` developer identity
- [ ] `STD-ABOUT-005` web/privacy links
- [ ] shared test identifiers exist

## Appearance
- [ ] theme/mode tap updates selected state immediately
- [ ] background/surface updates before navigation back
- [ ] value persists after back/reopen
- [ ] Light/Dark semantic surface parity

## Bottom navigation
- [ ] declared mode matches implementation
- [ ] native variant delegates system geometry to iOS
- [ ] custom baseline geometry
- [ ] custom surface may safely use bottom safe-area region
- [ ] bar position and content clearance are independently calculated
- [ ] small/regular/large width
- [ ] Dynamic Type
- [ ] last content fully scrolls above bar
- [ ] final extra clearance approximately 16–24 pt
- [ ] primary action does not inflate custom bar unnecessarily

## Keyboard
- [ ] focused field remains reachable
- [ ] required primary action remains reachable
- [ ] no double bottom reserve with tab/FAB
- [ ] keyboard dismissal does not lose draft data

## Accessibility
- [ ] 44 × 44 pt touch targets
- [ ] VoiceOver labels/traits
- [ ] no color-only meaning
- [ ] Increase Contrast
- [ ] Reduce Motion
- [ ] Reduce Transparency fallback, if material/translucent surfaces exist

## Release
- [ ] `validate-app-conformance.py` PASS
- [ ] screen families PASS/ADR, pending = 0 for Level 4
- [ ] app-native build PASS
- [ ] tests PASS
- [ ] runtime pending = 0 for release blockers
