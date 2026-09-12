# RC1 Integration Gap Audit

## Confirmed published state
The published GitHub prerelease `standard-v1.8.0-rc1` states 108 rules, but the tagged core machine files remained at the 1.7.0 active baseline:
- `STANDARD_VERSION` = `1.7.0`,
- `CONFORMANCE_CATALOG.json.standardVersion` = `1.7.0`,
- catalog status = `active`,
- candidate = `null`,
- catalog contains 96 rules.

Therefore RC1 was a published prerelease direction/release-note scope rather than a fully integrated 108-rule machine-readable package.

## RC2 resolution
RC2:
1. preserves all 96 tagged 1.7.0 rule objects without simplifying their applicability/verification metadata,
2. formalizes the 12 RC1 release-note commitments as machine-readable rules,
3. adds 11 RC2 audit-driven rules,
4. results in 119 unique rules,
5. introduces candidate-aware Standard/version/schema/template metadata.

This audit is included so the integration history remains explicit and traceable.
