# IJAS-0041 — Separate Central Standard Promotion from Per-Application Release

**Decision:** ACCEPTED (project owner approved in chat, 22 October 2026)  
**Scope:** IbaJuraj Application Standard 1.9.0 RC4 / PR #13  
**Nature:** governance of *when* to require evidence; does not remove or weaken any `STD-*` MUST/MUST NOT rule.  
**Release state:** Standard 1.9.0 remains NOT STABLE; no merge/tag authorized.

## Context

The governing `GOVERNANCE.md` requires validated package integrity, at least one real application adoption proving conformance machinery, resolution of RC ambiguities and a completed cross-app adoption matrix. The RC4 release checklist additionally mixed entire-app recovery, CloudKit sharing and app provider runtime acceptance into the **central** Standard promotion gate. This could block publication of a verified shared contract until every app is ready for its own release.

CI on prior commit `d898962f7ca9cb673df8e1a68e7eff92e1c413a1` passed (47 tests, 138-rule catalog, 132 tracked SHA256 checks). The real Calculator v1.15.0 Build64 R6 validator pilot demonstrated development exit 0 with pending results, release-candidate exit 2 with pending results, and 3/3 negative guard cases. That is proof of gate logic, **not** full app RC compliance or a positive genuine executed-evidence acceptance.

## Decision

Use two independent gates:

1. **Central Standard publication gate**: certify a stable, internally coherent normative package, validators, regression/integrity checks, proper phase handling, and at least one *real-app adoption of the conformance machinery*, including a positive verified native/unit and UI/runtime execution-evidence sample on an exact existing app build and negative rejection scenarios. This is a test of the machinery, **not** the complete RC conformance of that app.
2. **Application release gate**: each nominated App Store/production build MUST satisfy all applicable release-candidate rules and its own high-risk device/account/runtime acceptance, with exact app/version/build/sourceRevision, primary evidence, verified hash, runner/time/device context, and an explicit release decision. `PENDING`/`FAIL` cannot be marked `PASS`.

A central cross-app applicability/status register MUST identify all relevant apps, actual capability flags, accountable app-specific gates, exact known baselines, and factual `PASS/PENDING/N/A/EXCEPTION` without synthetic assertions. Completing the register **does not mean** falsely marking all app-specific gates PASS. N/A requires a source-grounded capability decision. Exceptions to applicable MUST/MUST NOT still require the existing full exception process.

## Central publication acceptance (C-01 to C-07)

- **C-01**: 138/138 rules reviewed; 119 stable inherited IDs retained; known ambiguities resolved. **PASS** (completed 21 October audit).
- **C-02**: source validator/schema/catalog regression and integrity PASS on reviewed commit. **PASS on `d898962` only**; repeat exact-new-head CI before merge.
- **C-03**: real app source used for deterministic missing/mismatched evidence guard tests. **PASS, limited** (Calculator B64 R6).
- **C-04**: positive acceptance of at least one **genuinely executed applicable MUST native test** and one **real UI/screen-family or runtime check** associated with the same existing app source/build. Primary `.xcresult`/trusted CI/native reports or verifiable human-reviewed runtime record must have timestamp, runner, actual output, hash, and device/OS when UI/runtime; validator must accept these real PASS while keeping the rest PENDING. **PENDING** — must not be replaced with fixtures or user-confirmed Build/Test without execution artifacts.
- **C-05**: completed cross-app applicability/register with reviewed source capability TRUE/FALSE/N/A and ownership of missing tests. **PENDING**.
- **C-06**: governance decision documented with corresponding checklist/adoption plan/PR-body alignment. **APPROVED PRINCIPLE**; documentation must pass exact-head CI.
- **C-07**: final exact-head CI, manifest, metadata and release risk sign-off + explicit separate owner approval for merge and stable tag. **PENDING**.

No central `C-04` exception is silently inferred. If the gate cannot be genuinely met, Standard 1.9.0 remains a candidate.

## Preserved app-specific release blockers

- **Calculator v1.15.0 Build64 R6**: actual RC conformance and seven applicable screen families remain PENDING; central pilot PASS does not upgrade it.
- **TradeBook v2.1.0 Build280**: exact-native tests and full-state second-device iPad recovery, history/DeFi/off-DB parity, safe rollback/new private recovery key remain PENDING.
- **Strážca Termínov v1.62.0 Build135 R2**: owner/recipient shared-content equality, follow-up edit/revoke, privacy placement and actual backup restore remain PENDING.
- **Peňaženka Kariet v1.6.0 Build94 R8**: complete two-account shared-wallet lifecycle and device recovery remain PENDING (one-off card transport is separate).
- **Lex Drive v1.23.0 Build325**: exact native/release/temporal legal-source validation and App Store controls remain PENDING.

The relevant `STD-BACKUP-*`, `STD-SHARE-001`, `STD-UPDATE-001`, `STD-AI-*`, `STD-RELEASE-*` and all inherited rules remain applicable whenever their real capability/phase is in scope. AI/Release Inspector controls are per-app mandatory at an applicable app RC; independent Standard package verification still tests their rule semantics.

## Risks and compensating controls

- **Incorrect implied app certification**: publish a conspicuous notice that a stable Standard is NOT proof any particular application conforms.
- **Misrepresentation of test readiness**: per-app register exposes PENDING; existing app release CI must invoke `--phase release-candidate` explicitly.
- **False capability N/A**: independent source review; no self-asserted false flag accepted as definitive evidence.
- **Runtime privacy/security**: required high-risk device/account tests continue to gate the exact app release; artifacts must exclude secrets/private keys/PII.
- **Unchecked scope drift**: future normative MUST exception requires rule ID, reason, scope, risk, compensating control, review/removal condition, and ADR.

## Implementation and change control

Apply only documentation on this PR; do not edit app sources, stable `main`, stable tag, or normative rule IDs. The prior cross-app promotion checklist is replaced by a central `C-01...C-07` gate and a separately tracked per-app release acceptance register. The PR remains Draft until minimum positive evidence and exact-head checks are complete. Explicit authorization for merge/tag is a later, independent act.

**Evidence sources:** `GOVERNANCE.md`, `EXECUTION_EVIDENCE_CONTRACT.md`, `RELEASE_CHECKLIST_1.9.0_RC4.md`, `ADOPTION_PLAN_RC4.md`, 21 October Master Handoff and Calculator pilot. Historical proofs stay scoped to their source build.
