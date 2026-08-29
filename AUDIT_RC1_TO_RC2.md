# Audit – IbaJuraj Application Standard 1.7.0 RC1 → RC2

## Trigger
Cross-app comparison of Lex Drive and Peňaženka Kariet showed that RC1 correctly required safe-area-aware adaptivity but did not explicitly prevent two defects:
1. unnecessary extra root-header top padding despite available safe-area geometry,
2. custom bottom navigation being kept entirely above the bottom safe area, creating unused space, while scroll clearance and bar placement were coupled.

## RC2 resolution
RC2 adds stable rules for:
- top/root viewport anchoring,
- bottom-edge utilization and Home Indicator safety,
- separation of chrome position from content clearance,
- horizontal utilization and unexplained edge waste,
- peer-root anchor parity,
- screen-family inventory and runtime audit,
- keyboard/chrome coordination,
- state stability and layout performance.

## Conformance changes
- validator supports `allCapabilities`,
- `screenAudit.families` is required,
- capability-driven screen families are enforced,
- pending family status blocks Level 4,
- `pass` family requires evidence.

No product/domain data semantics are changed by RC2.
