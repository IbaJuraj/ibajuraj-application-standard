# Release Checklist – IbaJuraj Application Standard 1.8.0

## Package
- [ ] `STANDARD_VERSION` is `1.8.0`.
- [ ] `standard.json` is `active`, stable authority `1.8.0`, tag `standard-v1.8.0`.
- [ ] `CONFORMANCE_CATALOG.json` is active and contains exactly 119 unique rules.
- [ ] Main standard contains every catalog rule ID.
- [ ] Final release notes, migration guide and test matrix exist.
- [ ] No `.DS_Store`, `xcuserdata`, `__pycache__` or `.pyc` files.

## Validation
- [ ] `Checks/validate-standard.sh` PASS.
- [ ] `Checks/validate-conformance-catalog.py` PASS.
- [ ] `Checks/test_validate_app_conformance.py` PASS.
- [ ] GitHub Actions PASS on the final release commit.

## Security clarification
- [ ] `STD-SECURITY-001` documents biometrics as primary app-lock method.
- [ ] System device passcode/password is documented and tested as fallback.
- [ ] App PIN is not required to enable biometrics.
- [ ] Optional app PIN, if retained, is securely persisted and product-justified.

## Publication
- [ ] Final changes are merged to `main`.
- [ ] Tag `standard-v1.8.0` points to the validated final commit.
- [ ] GitHub Release `IbaJuraj Application Standard 1.8.0` is published and marked stable/latest.
