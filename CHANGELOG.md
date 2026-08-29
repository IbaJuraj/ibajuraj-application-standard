# Changelog

## 1.7.0 RC2 – 2026-08-29

### Added
- Viewport Edge Utilization contract for top, bottom and horizontal bounds.
- Shared root-header top-anchor baseline of safe area + 0–4 pt.
- Explicit distinction between bottom chrome position and scroll content clearance.
- Safe custom bottom-bar use of bottom safe-area region with Home Indicator protection.
- Screen-family inventory and release-blocking family audit.
- Adaptive density, state-geometry stability and layout-performance requirements.
- Keyboard avoidance and bottom-chrome coordination requirements.
- Reduce Transparency fallback contract for translucent/material surfaces.
- `allCapabilities` condition support in the conformance engine.
- Validator enforcement of required screen families.

### Clarified
- empty space caused by little content is not a defect; unexplained fixed edge waste is,
- peer root screens align relative to safe area, not to screenshots or absolute device coordinates,
- native tab bars remain platform-owned; custom bars may use safe-area penetration when safe,
- whole-app audit applies to root, settings/about, detail, form, search, sheet, fullscreen and state families where applicable.


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
