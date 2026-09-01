# IbaJuraj Application Standard 1.7.0 RC2 – Static Audit

**Date:** 2026-08-29  
**Candidate:** RC2  
**Inherited stable authority:** 1.6.4

## Scope
RC2 supersedes RC1 for further adoption and keeps the 1.7.0 semantic version. It adds explicit viewport-edge utilization, screen-family inventory/audit, keyboard/bottom-chrome coordination, adaptive density, state stability, Reduce Transparency fallback and layout-performance gates.

## Structural validation
- `STANDARD_VERSION` = `1.7.0`: PASS
- `standard.json.version` = `1.7.0`: PASS
- `standard.json.candidate` = `RC2`: PASS
- required RC2 documents present: PASS
- source hygiene (`.DS_Store`, `xcuserdata`, `__pycache__`, `.pyc`): PASS

## Conformance catalog
- rule headings in main Standard: **92**
- catalog rules: **92**
- unique rule IDs: **92**
- main-document ↔ catalog parity: PASS
- new RC2 rules vs RC1: **20**
- supported conditional forms include capability, any/all capability, bottom-navigation mode and logical `anyOf`/`allOf`: PASS

## Validator
- `validate-app-conformance.py` supports `screenAudit.families`: PASS
- capability-driven required screen families: PASS
- pending screen family blocks Level 4: PASS
- `pass` screen family requires evidence: PASS
- `exception` screen family requires an existing ADR: PASS
- custom bottom-navigation conditional rules: PASS
- combined keyboard + bottom-navigation condition: PASS
- localization parity behavior retained: PASS

## Automated tests
`python3 -m unittest Checks/test_validate_app_conformance.py`

**9/9 PASS**

Coverage includes:
- complete fixture,
- missing always-applicable rule,
- custom-navigation condition,
- fixed-bottom-controls logical `anyOf`,
- combined-capabilities condition,
- release-blocking pending rule,
- missing required screen family,
- pending screen family,
- localization parity.

## Schema / syntax
- `standard.json` against `standard.schema.json`: PASS
- `STANDARD_CONFORMANCE_TEMPLATE.json` against `STANDARD_CONFORMANCE.schema.json`: PASS
- Python syntax: PASS
- shell syntax: PASS

## Runtime boundary
This audit does **not** claim physical-device viewport correctness. Root top anchor, lowest-safe bottom chrome, Home Indicator clearance, Dynamic Type, localization stress, keyboard interaction, system-overlay response and layout performance remain app-level runtime/UI gates during RC2 adoption.

## Conclusion
**RC2 package is statically ready for real-app adoption.** It is not the public active Standard until the cross-app RC2 adoption completes and final `standard-v1.7.0` is published.
