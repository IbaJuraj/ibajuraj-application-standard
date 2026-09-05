# IbaJuraj Application Standard 1.8.0 RC1 – Release Candidate Checklist

## Candidate package
- [x] `STANDARD_VERSION` = `1.8.0`
- [x] `standard.json.version` = `1.8.0`
- [x] `standard.json.status` = `release-candidate`
- [x] `candidate` = `RC1`
- [x] `rcDate` = `2026-09-05`
- [x] candidate tag target = `standard-v1.8.0-rc1`
- [x] active public authority remains `standard-v1.7.0`
- [x] `CONFORMANCE_CATALOG.json` contains 108 unique rules
- [x] 96 rules from 1.7.0 preserved
- [x] 12 new 1.8.0 RC1 rule IDs added
- [x] 1.8.0 conformance schema/template updated
- [x] RC1 migration/test/adoption/release documents added

## Accepted change families
- [x] IJAS-0025 Localization-First Architecture and Storefront Independence
- [x] in-app language selector behavior folded into IJAS-0025 normative adoption
- [x] IJAS-0026 Release Package Root Hygiene and Build History Archive
- [x] IJAS-0027 Single-Device Development/Release Data Continuity
- [x] IJAS-0028 Production Backend Environment Readiness
- [x] representative real-volume performance rule based on runtime evidence from Peňaženka Kariet

## Static candidate validation
- [ ] `bash Checks/validate-standard.sh` PASS on RC1 head
- [ ] `python3 Checks/validate-conformance-catalog.py` PASS
- [ ] `python3 -m unittest Checks/test_validate_app_conformance.py` PASS
- [ ] GitHub Actions `Validate IbaJuraj Standard` PASS
- [ ] no `.DS_Store`, `xcuserdata`, `__pycache__`, `.pyc` or release-package hygiene regressions

## Primary adoption gate – Peňaženka Kariet
- [ ] adopt 1.8.0 RC1 without losing existing 1.5.3 work
- [ ] six runtime localizations PASS
- [ ] in-app selector Automatic/System + SK/CS/EN/DE/PL/HU PASS if included
- [ ] language switching/relaunch preserves all 32 cards and their raw data
- [ ] localized search parity PASS
- [ ] Production iCloud sync PASS
- [ ] Production sharing/rebind PASS
- [ ] Xcode ↔ TestFlight same-device continuity PASS
- [ ] representative 32-card scroll/search performance PASS
- [ ] release-root hygiene PASS

## Secondary adoption gate – Strážca Termínov
- [ ] stable local Person/Vehicle/VehicleSet/Document/Deadline identity audit
- [ ] Development/Production membership/share/invitation separation
- [ ] Production CloudKit readiness smoke
- [ ] same-device continuity without data loss/duplication
- [ ] root-document history hygiene
- [ ] localization/runtime closure

## Cross-app applicability audit
- [ ] Lex Drive checked for newly applicable localization/release/performance rules
- [ ] Kalkulačka 2v1 checked for language-selector/localization/release rules
- [ ] no new cross-app ambiguity requiring RC2

## Promotion to final 1.8.0
Do **not** mark these complete at RC1 publication.
- [ ] all known RC1 ambiguities resolved
- [ ] at least one real app adoption proves new conformance machinery
- [ ] agreed cross-app adoption matrix complete
- [ ] `standard.json.status` changed to `active`
- [ ] candidate marker cleared
- [ ] final release date set
- [ ] final tag changed to `standard-v1.8.0`
- [ ] final release audit generated
- [ ] final GitHub Actions validation PASS
- [ ] stable GitHub Release published

1.8.0 RC1 may be published as a **prerelease/release candidate**, but it is not yet the active public Standard.
