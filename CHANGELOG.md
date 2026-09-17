# Changelog

## 1.9.0 RC1 – accepted scope (unreleased) – 2026-09-17

### Accepted
- `STD-AUTH-SOURCE-001` via `IJAS-0033-authoritative-source-offline-citation-contract.md`.
- Applications that use legal, regulatory, normative or other authoritative sources as part of a user-facing functional result must provide the used source locally/offline, preserve source identity and effective/version metadata, and keep a verification trace where verified content is used.
- Legal or equivalently normative content must expose the exact citation or verbatim provision used by the result.
- An external official website may remain available as a supplemental link, but must not be the only way to access the authoritative basis.

### Compatibility
- Classified as a MINOR compatible contract family under Governance.
- Stable 1.8.0 authority and its 119-rule machine-readable catalog remain unchanged until 1.9.0 RC integration.

## 1.8.0 – 2026-09-15

### Released
- Promoted the validated 1.8.0 RC2 machine-readable rule set to stable authority.
- Stable catalog remains **119 rules**: 96 inherited from 1.7.0, 12 formalized RC1 commitments and 11 RC2 hardening rules.
- Finalized metadata, release documentation and stable tag target `standard-v1.8.0`.

### Clarified
- `STD-SECURITY-001`: biometrics are the primary local app-lock mechanism when enabled.
- Biometric unavailability, lockout or failure must support fallback to system device authentication using the device passcode/password.
- A separate app PIN must not be required merely to enable biometrics; it may remain optional where product-specific value exists.

### Adoption
- Existing 1.8.0 RC2 adopters do not gain a new rule ID; they must re-audit the clarified `STD-SECURITY-001` behavior.

## 1.8.0 RC2 – 2026-09-12

### Integrated
- First fully integrated machine-readable candidate in the 1.8 line.
- Preserves the exact 96-rule 1.7.0 baseline metadata.
- Formalizes 12 commitments published in the RC1 prerelease scope.
- Adds 11 new cross-app hardening rules.
- Expands the conformance catalog to **119 unique rules**.

### Added
- async stale-completion protection,
- deterministic derived-state rebuild ordering,
- cloud remote-truth and durable reconciliation,
- corrupt persisted-state recovery,
- relationship-aware deletion,
- production-to-candidate upgrade gate,
- deterministic-engine automated regression coverage,
- disabled-feature/permission parity,
- exact-build runtime evidence,
- compact-surface content priority and destination integrity.

### Corrected
- Documents the RC1 integration gap: RC1 release notes declared 108 rules while the tagged machine files remained on the 1.7.0/96-rule baseline.

## 1.8.0 RC1 – 2026-09-05

### Published scope
- Localization-first architecture and stable semantic localization keys.
- Locale-aware formatting and pluralization.
- Optional in-app language selector with Automatic/System mode.
- No data migration/raw-ID change solely from language switching.
- Localized search parity and storefront independence.
- Release-package root hygiene.
- Single-device Xcode ↔ TestFlight/App Store ↔ Xcode continuity.
- Production backend schema/config readiness and Production smoke.
- Server-side vs binary fix distinction.
- Representative real-volume performance testing.

## 1.7.0 – 2026-09-02

### Released
- Promoted RC3 to the active IbaJuraj Application Standard 1.7.0 after cross-app adoption and runtime review across Peňaženka Kariet, Strážca Termínov, Lex Drive and Kalkulačka 2v1.
- Preserved the validated RC3 normative rule set without adding a new RC4 or changing rule semantics during final promotion.
- Finalized active metadata, release documentation and validation expectations for tag `standard-v1.7.0`.

### Included
- Whole-App Adaptive Layout and Viewport Edge Utilization contracts.
- Native/Custom Bottom Navigation and Screen-Family Audit contracts.
- Shared About, Appearance and machine-verifiable conformance contracts.
- Single Header Ownership, No Duplicate Heading, Coherent Sheet Header and System Chrome Ownership contracts.
- Conformance catalog with 96 stable `STD-*` rules.

## 1.7.0 RC3 – 2026-08-29

### Added
- Single Header Ownership Contract.
- No Duplicate Heading Contract.
- Coherent Sheet Header Contract.
- System Chrome Ownership Contract.
- Conformance catalog expanded from 92 to 96 stable `STD-*` rules.

### Clarified
- navigation titles and section headings must have distinct semantic roles,
- a sheet must not reserve an empty system navigation band above a second custom title,
- platform-owned chrome such as the Home Indicator must not be visually imitated by the app.

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
