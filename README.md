# IbaJuraj Application Standard 1.8.0

This branch contains the **stable IbaJuraj Application Standard 1.8.0**.

1.8.0 promotes the fully integrated RC2 rule set to stable authority:
- 96 exact stable 1.7.0 rule objects,
- 12 formalized commitments from the published RC1 scope,
- 11 RC2 hardening rules,
- **119 rules total**.

Main areas: localization-first architecture, Xcode ↔ TestFlight/App Store data continuity, Production backend readiness, async/derived-state integrity, cloud mutation truth and reconciliation, persisted-state recovery, upgrade continuity, deterministic regression coverage, disabled-feature permission parity, build-scoped evidence and compact-surface integrity.

## Security clarification in final 1.8.0

`STD-SECURITY-001` is clarified without adding a new rule ID:
- biometrics are the primary app-lock mechanism,
- biometric failure/unavailability/lockout must fall back to system device authentication (device passcode/password),
- a separate app PIN must not be required to enable biometrics,
- an app PIN may remain as optional additional protection where product-specific value exists.

## Validate

```bash
bash Checks/validate-standard.sh
python3 Checks/validate-conformance-catalog.py
python3 -m unittest Checks/test_validate_app_conformance.py
```

## Stable authority

Stable release tag: `standard-v1.8.0`.

Applications should adopt 1.8.0 at their next planned release and record applicability/runtime evidence in their conformance files.
