# Standard 1.8.0 RC1 – Static Audit

**Date:** 2026-09-05  
**Scope:** candidate package structure and normative consistency before cross-app runtime adoption.

## Candidate identity
- Standard version: 1.8.0
- Status: release-candidate
- Candidate: RC1
- Candidate tag: `standard-v1.8.0-rc1`
- Inherits: active `standard-v1.7.0`

## Normative catalog
- 96 inherited rule IDs retained.
- 12 new rule IDs added.
- Expected total: 108.
- New families: localization/language selection, release-root history hygiene, single-device data continuity, Production backend readiness, representative-data performance.

## Proposal mapping
- IJAS-0025 → STD-LOC-003…008
- IJAS-0026 → STD-RELEASE-005…006
- IJAS-0027 → STD-DATA-005
- IJAS-0028 → STD-BACKEND-001…002
- representative-data runtime finding → STD-PERF-001

## Static checks required before publishing RC1
- `bash Checks/validate-standard.sh`
- `python3 Checks/validate-conformance-catalog.py`
- `python3 -m unittest Checks/test_validate_app_conformance.py`
- GitHub Actions validation on the candidate branch/head

## Runtime claims deliberately excluded
This static audit does not claim:
- Peňaženka 1.8.0 RC1 adoption PASS,
- Strážca 1.8.0 RC1 adoption PASS,
- final 1.8.0 promotion readiness,
- production behavior of any app beyond already recorded app-specific evidence.

## Promotion rule
RC1 publication freezes candidate semantics. If adoption discovers a normative change, use RC2. Final 1.8.0 is created only after the governance promotion gate.
