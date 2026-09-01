# Audit 1.6.4 → 1.7.0

## Change class
**MINOR**, backward-compatible contract expansion.

## New contract families
1. Whole-App Adaptive Layout Contract (`STD-ADAPT-*`).
2. Viewport Edge Utilization & Screen-Family Contract (`STD-VIEWPORT-*`, `STD-SCREEN-*`).
3. Bottom Navigation & Floating Tab Bar Contract (`STD-NAV-*`).
4. About Cross-App Contract (`STD-ABOUT-*`).
5. Live Appearance Contract (`STD-APPEARANCE-*`).
6. Machine-Verifiable Conformance (`STD-CONF-*`).
7. Header & System Chrome Ownership (`STD-HEADER-*`, `STD-CHROME-*`).

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
- whole-app conformance claims without an explicit inventory of screen families actually audited,
- duplicate navigation/page/section headings and parallel sheet-header ownership found during real-app review,
- app-drawn imitations of platform-owned system chrome.

## RC evolution
- **RC1** established adaptive layout, bottom-navigation variants and machine-verifiable conformance.
- **RC2** added viewport-edge utilization, screen-family audit, keyboard/chrome coordination, state stability and layout-performance gates.
- **RC3** added single-header ownership, duplicate-heading prevention, coherent sheet headers and platform system-chrome ownership. The conformance catalog reached 96 stable `STD-*` rules.

## Cross-app acceptance
RC3 was applied/reviewed across the four target applications: Peňaženka Kariet, Strážca Termínov, Lex Drive and Kalkulačka 2v1. On 2 September 2026 the product owner reported no observed Standard-related malfunction or regression in any of the four applications during the final cross-app review.

Application-level automated/Xcode/runtime evidence remains owned by each adopting app; static evidence is not treated as a substitute for runtime behavior.

## Release conclusion
RC3 is accepted as the final normative basis for IbaJuraj Application Standard 1.7.0. No RC4 is required. The Standard is promoted to `active`, the candidate marker is cleared and the final release tag is `standard-v1.7.0`.
