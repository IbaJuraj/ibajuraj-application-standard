# IbaJuraj Application Standard 1.8.0

**Released:** 15 September 2026  
**Stable tag:** `standard-v1.8.0`

## Summary

Version 1.8.0 promotes the validated RC2 rule set to stable authority with **119 machine-readable rules**.

It includes:
- localization-first architecture and locale-safe persisted identity,
- Xcode ↔ TestFlight/App Store ↔ Xcode continuity,
- Production backend readiness and real Production smoke requirements,
- async/derived-state integrity,
- cloud mutation truth and durable reconciliation,
- persisted-data recovery and upgrade-path gates,
- deterministic regression coverage,
- feature/permission parity,
- build-scoped runtime evidence,
- compact-surface destination integrity.

## Final security clarification

The final release clarifies existing rule `STD-SECURITY-001` without creating a new rule ID:

- biometrics are the primary app-lock mechanism when enabled,
- unavailable/failed/locked-out biometrics MUST fall back to system device authentication using the device passcode/password,
- a separate app PIN MUST NOT be required simply to enable biometrics,
- an app PIN MAY remain optional when justified by product requirements,
- internal navigation MUST NOT repeatedly trigger authentication.

Applications already aligned to RC2 should re-audit only this clarified security behavior plus normal stable-release metadata adoption.
