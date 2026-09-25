# IbaJuraj Application Standard 1.9.0 RC3

This branch contains the **candidate IbaJuraj Application Standard 1.9.0 RC3**.

Stable public authority remains **1.8.0** (`standard-v1.8.0`). RC3 preserves the 131-rule RC2 candidate, consolidates AI governance into seven coherent contracts and adds three new machine-readable AI rules for **134 candidate rules total**.

## RC3 principle
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

AI is grounded, advisory, explainable and read-only by default. RC3 adds provider/runtime fallback, on-device/cloud transparency, untrusted-input/output validation, regression/rollback and controlled adaptation/self-learning. Apple Foundation Models/Core AI are reference on-device implementations, not mandatory technologies.

## Validate
```bash
bash Checks/validate-standard.sh
python3 Checks/validate-conformance-catalog.py
python3 -m unittest Checks/test_validate_app_conformance.py
```

## Candidate
Branch: `standard-1.9.0-rc3`  
Proposed tag: `standard-v1.9.0-rc3`

Do not promote to stable 1.9.0 until Release Inspector and consolidated AI contracts are validated in pilot apps with cross-app exact-build evidence.
