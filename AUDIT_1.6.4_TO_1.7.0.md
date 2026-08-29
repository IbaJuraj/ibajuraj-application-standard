# Audit 1.6.4 → 1.7.0 RC2

## Change class
**MINOR**, backward-compatible contract expansion.

## New contract families
1. Whole-App Adaptive Layout Contract (`STD-ADAPT-*`).
2. Viewport Edge Utilization & Screen-Family Contract (`STD-VIEWPORT-*`, `STD-SCREEN-*`).
3. Bottom Navigation & Floating Tab Bar Contract (`STD-NAV-*`).
4. About Cross-App Contract (`STD-ABOUT-*`).
5. Live Appearance Contract (`STD-APPEARANCE-*`).
6. Machine-Verifiable Conformance (`STD-CONF-*`).

## Why MINOR
1.7.0 adds new mandatory common behavior and verification machinery but does not require product-domain data-model changes and does not remove supported 1.6.4 behavior.

## Primary evidence that motivated the release
- different bottom-navigation geometries across peer apps without an explicit common variant contract,
- container-driven adaptive implementations in some apps vs `UIScreen`/device-size heuristics in others,
- calculator keypad leaving useful free space despite safe ability to grow,
- theme-selection screen that persisted a new theme but did not update checkmark/background until navigation back,
- cross-app About version formatting drift,
- root headers with different unexplained extra top insets,
- custom bottom chrome kept entirely above the bottom safe area, creating avoidable empty space,
- scroll content clearance coupled to physical bar position,
- static build checks passing despite runtime UX defects,
- whole-app conformance claims without an explicit inventory of screen families actually audited.

## RC evolution
RC1 established adaptive layout, bottom-navigation variants and machine-verifiable conformance. RC2 keeps those semantics and closes gaps found during real app comparison by adding viewport-edge utilization, screen-family audit, keyboard/chrome coordination, state stability and layout-performance gates.

## Release conclusion
RC2 must be applied to real applications before promotion to active. The conformance system itself, including screen-family completeness, is part of the acceptance target.
