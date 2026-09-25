# Changelog

## 1.9.0 RC3 – 2026-09-25

### Added
- `STD-AI-005` — provider/runtime, on-device/cloud transparency and graceful fallback.
- `STD-AI-006` — untrusted input/output boundary, structured-output validation, AI eval/regression and rollback.
- `STD-AI-007` — controlled adaptation/self-learning, separate learning memory, provenance, reversibility and human reset.
- Machine-readable `ai.features[]` metadata with stable feature ID, risk profile and execution mode.
- AI capability flags for on-device, cloud, tools, adaptive behavior and personalization.
- Candidate catalog expanded from 131 to **134 unique rules**.

### Consolidated
- `STD-AI-001` and `STD-AI-002` retain their stable identities and are explicitly defined as grounded/verified assistance and user transparency/fallback/feedback contracts.
- `STD-AI-003` is generalized from Release-Inspector-only wording to advisory, explainable and read-only-by-default AI.
- `STD-AI-004` is generalized to privacy, data minimization, sanitization and secure secret handling for all AI use.
- AI release review remains subordinate to deterministic Release Inspector PASS/FAIL.

### Reference implementation
- Apple Foundation Models / Core AI are documented as reference on-device implementations, not mandatory technologies.
- TradeBook is the first intended RC3 pilot for local/cloud AI review and controlled adaptation contracts.

## 1.9.0 RC2 – 2026-09-25

### Added
- RC-only full quality gate rather than a full audit after every small development build.
- In-App Full App Check with structured severity findings.
- Release diff/risk audit, critical journeys/failure injection and UI/runtime matrix.
- Governed AI release review with explainability and privacy/data-minimization boundaries.
- Exact-build RC Evidence Bundle and optional post-release feedback loop.
- Candidate catalog expanded from 121 to **131 unique rules**.

### Preserved
- Stable authority remains 1.8.0.
- RC1 async responsiveness and authoritative-source contracts remain unchanged.
- Runtime evidence remains exact-build scoped.


## 1.9.0 RC1 – 2026-09-17

### Added
- `STD-ASYNC-002` for remote invite/share/access responsiveness; network/backend orchestration must not block interactive UI/MainActor responsiveness and long-running work must expose a visible in-progress state.
- `STD-AUTH-SOURCE-001` for authoritative functional sources; legal/regulatory/normative basis used by a user-facing result must be locally/offline available, version/effective-date identified, exactly citable and externally traceable.
- 1.9.0 RC1 machine-readable catalog expanded from the stable 1.8.0 baseline of 119 rules to **121 unique rules**.

### Clarified
- Root-title adaptive family: peer root screens use one shared title family driven by available viewport/container width; full titles should be preferred over truncation. This clarification does not add a new `STD-*` rule ID.
- `STD-AUTH-SOURCE-001` makes an official external website supplemental only; it must not be the sole access path to the authoritative basis.

### Preserved
- `STD-CLOUD-001` remains the authority for confirmed remote destructive/access success.
- `STD-CLOUD-002` remains the authority for durable retry/reconciliation.
- Stable public authority remains 1.8.0 until 1.9.0 is promoted.

### Reference adoption
- Strážca Termínov Build 120 Phase 14A R12 is the first implementation reference for `STD-ASYNC-002`.
- Lex Drive Build 232 is the first implementation/reference case for `STD-AUTH-SOURCE-001` and offline legal citation behavior.

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
- Localization-first architektúra a stable semantic localization keys.
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
