# IbaJuraj Application Standard 1.9.0 RC2

This branch contains the **candidate IbaJuraj Application Standard 1.9.0 RC2**.

Stable public authority remains **1.8.0** (`standard-v1.8.0`). RC2 preserves the 121-rule RC1 candidate and adds 10 Release Candidate Quality Gate / Intelligent Self-Audit rules for **131 candidate rules total**.

## RC2 principle
A complete whole-app audit is required when a build is nominated for App Store/store/production submission, not after every small development build.

Reference architecture: **IbaJuraj Release Inspector / Quality Engine**
- internal In-App Full App Check,
- deterministic and app-specific checks,
- release diff + risk-based coverage,
- critical user journeys + failure injection,
- visual/runtime matrix,
- optional governed AI review,
- exact-build Evidence Bundle,
- post-release feedback where supported.

AI is advisory and explainable; it is not the sole PASS/FAIL authority and uses minimized/sanitized inputs.

## Validate
```bash
bash Checks/validate-standard.sh
python3 Checks/validate-conformance-catalog.py
python3 -m unittest Checks/test_validate_app_conformance.py
```

## Candidate
Branch: `standard-1.9.0-rc2`  
Proposed tag: `standard-v1.9.0-rc2`

Do not promote to stable 1.9.0 until pilot and cross-app exact-build evidence are complete.
