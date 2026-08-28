# IbaJuraj Application Standard 1.7.0 – Test Matrix

## Povinné vrstvy

| Vrstva | Čo dokazuje | Čo nedokazuje |
|---|---|---|
| Static conformance | prítomnosť contractov, evidence, localization parity, pin | živé UI správanie |
| Unit/XCTest | deterministická logika, metadata provider, layout math | reálne clipping/safe-area |
| UI test | navigácia, spoločné surface, selected state, live appearance | všetky zariadenia bez matice |
| Runtime acceptance | fyzický vzhľad, safe area, Dynamic Type, platform interaction | regresiu do budúcna bez automatizácie |

## Adaptive matrix

### iPhone – každá aplikácia
- [ ] Small container
- [ ] Regular container
- [ ] Large container
- [ ] Accessibility Dynamic Type
- [ ] Light
- [ ] Dark
- [ ] Longest supported localization
- [ ] Keyboard/form state, ak aplikovateľné

### iPad – ak podporované
- [ ] Portrait
- [ ] Landscape
- [ ] Supported window/multitasking sizes

### iPhone-only compatibility – ak systém umožní
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
- [ ] small/regular/large width
- [ ] Dynamic Type
- [ ] safe-area position
- [ ] last content fully scrolls above bar
- [ ] final extra clearance approximately 16–24 pt
- [ ] primary action does not inflate custom bar unnecessarily

## Accessibility
- [ ] 44 × 44 pt touch targets
- [ ] VoiceOver labels/traits
- [ ] no color-only meaning
- [ ] Increase Contrast
- [ ] Reduce Motion

## Release
- [ ] `validate-app-conformance.py` PASS
- [ ] app-native build PASS
- [ ] tests PASS
- [ ] runtime pending = 0 for release blockers
