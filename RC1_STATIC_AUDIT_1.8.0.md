# Standard 1.8.0 RC1 – Static Audit

**Date:** 2026-09-05  
**Scope:** candidate package structure and normative consistency before cross-app runtime adoption.

## Candidate identity
- Standard version: 1.8.0
- Status: release-candidate
- Candidate: RC1
- Candidate tag target: `standard-v1.8.0-rc1`
- Inherits: active `standard-v1.7.0`

## Normative catalog
- 96 inherited rule IDs retained.
- 12 new rule IDs added.
- Total: **108 rules**.
- New families: localization/language selection, release-root history hygiene, single-device data continuity, Production backend readiness, representative-data performance.

## Proposal mapping
- IJAS-0025 → STD-LOC-003…008
- IJAS-0026 → STD-RELEASE-005…006
- IJAS-0027 → STD-DATA-005
- IJAS-0028 → STD-BACKEND-001…002
- representative-data runtime finding → STD-PERF-001

## Static validation result
Candidate branch validation reached PASS on commit:
`28ca05cfed12f73ccfacbfdb9832f9b788928526`

GitHub Actions:
- workflow: `Validate IbaJuraj Standard`
- run: `33985440558`
- event: push
- conclusion: **SUCCESS**

The workflow executed:
- `bash Checks/validate-standard.sh`,
- `python3 -m unittest Checks/test_validate_app_conformance.py`.

The package validator itself also executes `Checks/validate-conformance-catalog.py`, including the expected 108-rule count and candidate metadata checks.

## Runtime claims deliberately excluded
This static audit does not claim:
- Peňaženka 1.8.0 RC1 adoption PASS,
- Strážca 1.8.0 RC1 adoption PASS,
- final 1.8.0 promotion readiness,
- production behavior of any app beyond already recorded app-specific evidence.

## Candidate decision
**Static candidate package: PASS.**  
RC1 is suitable for publication as a GitHub **prerelease/release candidate**.

## Promotion rule
RC1 publication freezes candidate semantics. If adoption discovers a normative change, use RC2. Final 1.8.0 is created only after the governance promotion gate.
