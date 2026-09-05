# IbaJuraj Application Standard 1.8.0 RC1 – Test Matrix

## Povinné vrstvy

| Vrstva | Čo dokazuje | Čo nedokazuje |
|---|---|---|
| Static conformance | contracty, pin, capability flags, screen inventory, localization parity, release-root hygiene | živé UI/backend správanie |
| Unit/XCTest | deterministická logika, metadata provider, layout math, local/cloud identity separation, locale-neutral persistence | reálne clipping/safe-area/Production backend |
| UI test | navigácia, shared surfaces, selected state, live appearance, language selector, stabilné identifiers | všetky zariadenia/prostredia bez matice |
| Runtime acceptance | fyzický viewport, safe area, Dynamic Type, keyboard, performance, platform interaction, reálny Production flow | regresiu do budúcna bez automatizácie |

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

## Localization 1.8.0 RC1
- [ ] localization resources cover every declared runtime locale
- [ ] fallback locale is deterministic
- [ ] dates/numbers/currency/percent use active or explicit domain locale
- [ ] pluralization is locale-aware
- [ ] persisted raw values/IDs/keys do not change when UI language changes
- [ ] if search exists: representative localized names/aliases work in every runtime locale
- [ ] App Store storefront availability is not inferred from runtime locales

### In-app language selector – ak existuje
- [ ] Automatic/System mode exists
- [ ] all runtime-supported languages are selectable
- [ ] selected language persists after navigation/relaunch
- [ ] Automatic/System re-adopts iOS/per-app language
- [ ] language change does not alter user data, raw IDs, CloudKit IDs or payloads
- [ ] whole-app presentation changes deterministically; relaunch is explicit if required

## Single-device continuity – ak environment-specific backend existuje
Preferovať rovnaký marketing version/build v Development a TestFlight, ak je to prakticky možné.
- [ ] real local dataset exists before environment switch
- [ ] Xcode/Development sees the dataset
- [ ] install/open TestFlight/App Store without deleting the app
- [ ] same local domain objects and stable IDs remain
- [ ] Production sync/share/read/write works according to capability
- [ ] missing Production binding does not delete/duplicate local objects
- [ ] environment-specific binding can be recreated/rebound
- [ ] return to Xcode/Development preserves local objects
- [ ] Development and Production binding IDs/tokens are documented as separate

## Production backend readiness
- [ ] Production schema/resources deployed
- [ ] required indexes exist
- [ ] permissions/security roles match the intended production contract
- [ ] environment configuration/entitlements point to the intended Production backend
- [ ] TestFlight/Production real read path PASS
- [ ] real write/sync path PASS when applicable
- [ ] real sharing/invitation path PASS when applicable
- [ ] backend failure preserves local data and exposes understandable state
- [ ] server-side fix vs binary fix is recorded in release evidence

## Representative-data performance
- [ ] runtime dataset is representative of real or realistic high-volume usage
- [ ] critical scroll flow smooth enough for release
- [ ] search/filter/sort smoke if applicable
- [ ] root/tab switching with populated data
- [ ] no avoidable repeated decoding/render work on every frame/row
- [ ] no visible layout thrash introduced by adaptive logic

## Release-package hygiene
- [ ] root contains only current authoritative build/release docs
- [ ] superseded `BUILD_*` / runtime acceptance docs are archived or consolidated
- [ ] historical regression/migration/release evidence was not silently deleted
- [ ] archive docs are not added to runtime app bundle unless needed

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

## Header/chrome matrix
- Native title + content: no equivalent duplicate heading.
- Custom header: native navigation reservation hidden/removed unless semantically required.
- Sheet: one title/subtitle/dismissal hierarchy at small/regular/Accessibility Dynamic Type.
- Fullscreen: no decorative fake Home Indicator or other platform-owned chrome imitation.

## Release
- [ ] `validate-app-conformance.py` PASS
- [ ] screen families PASS/ADR, pending = 0 for Level 4
- [ ] app-native build PASS
- [ ] tests PASS
- [ ] runtime pending = 0 for release blockers
- [ ] Production backend gate PASS if applicable
- [ ] single-device continuity PASS if applicable
- [ ] representative-data performance PASS if persisted data applies
