# Test Matrix – IbaJuraj Application Standard 1.8.0

## Package gates

- `bash Checks/validate-standard.sh`
- `python3 Checks/validate-conformance-catalog.py`
- `python3 -m unittest Checks/test_validate_app_conformance.py`

All must pass for the exact release commit.

## Cross-app runtime gates

For each adopting app, verify applicable rule families on the exact candidate build:
- settings/navigation/header/chrome,
- localization and locale-aware formatting,
- persisted-data continuity and upgrade path,
- Production backend read/write/sync/share where applicable,
- async/derived-state integrity,
- deterministic-engine regression tests where applicable,
- permissions and feature-flag parity,
- representative-data performance,
- compact-surface destination integrity.

## Security runtime gate (`STD-SECURITY-001`)

When the app has a local app lock:
1. enable Face ID/Touch ID/Optic ID without requiring an app PIN,
2. confirm successful biometric unlock,
3. force biometric failure/unavailability/lockout,
4. confirm system device passcode/password fallback appears and unlocks correctly,
5. confirm normal internal navigation does not retrigger authentication,
6. confirm repeated biometric prompts cannot overlap,
7. if optional app PIN exists, confirm it is securely stored and is not required merely to enable biometrics.

Runtime evidence must identify app version/build, device/OS and result.
