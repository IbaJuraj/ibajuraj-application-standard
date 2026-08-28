# Changelog

## 1.7.0 RC1 – 2026-08-28

### Added
- Whole-App Adaptive Layout Contract.
- Bottom Navigation & Floating Tab Bar Contract.
- About cross-app version/display contract.
- Live appearance-selection contract.
- Stable `STD-*` conformance rule IDs.
- Machine-readable `CONFORMANCE_CATALOG.json`.
- `STANDARD_CONFORMANCE.json` template/schema.
- Cross-app `validate-app-conformance.py`.
- Shared UI/accessibility test identifiers.
- Adaptive runtime matrix for small/regular/large iPhone and iPad where applicable.

### Clarified
- design-token fixed values are allowed; device-specific layout frames are not a substitute for container geometry,
- adaptivity includes reasonable use of available space, not only avoiding clipping,
- custom floating navigation baseline is adaptive, not a rigid 60–66 pt frame,
- static PASS is not runtime proof.

### Inherited
All 1.6.4 requirements remain in force unless explicitly superseded.
