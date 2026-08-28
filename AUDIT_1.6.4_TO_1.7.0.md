# Audit 1.6.4 → 1.7.0 RC1

## Change class
**MINOR**, backward-compatible contract expansion.

## New contract families
1. Whole-App Adaptive Layout Contract (`STD-ADAPT-*`).
2. Bottom Navigation & Floating Tab Bar Contract (`STD-NAV-*`).
3. About Cross-App Contract (`STD-ABOUT-*`).
4. Live Appearance Contract (`STD-APPEARANCE-*`).
5. Machine-Verifiable Conformance (`STD-CONF-*`).

## Why MINOR
1.7.0 adds new mandatory common behavior and verification machinery but does not require product-domain data-model changes and does not remove supported 1.6.4 behavior.

## Primary evidence that motivated the release
- different bottom-navigation geometries across peer apps without an explicit common variant contract,
- container-driven adaptive implementations in some apps vs `UIScreen`/device-size heuristics in others,
- calculator keypad leaving useful free space despite safe ability to grow,
- theme-selection screen that persisted a new theme but did not update checkmark/background until navigation back,
- cross-app About version formatting drift,
- static build checks passing despite runtime UX defects.

## Release conclusion
The RC must be applied to real applications before promotion to active. The conformance system itself is part of the acceptance target.
