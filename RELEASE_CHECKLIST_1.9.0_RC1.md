# Release Checklist – IbaJuraj Application Standard 1.9.0 RC1

## Candidate package
- [ ] `standard.json` and `STANDARD_VERSION` still describe stable 1.8.0 until promotion.
- [ ] `CONFORMANCE_CATALOG.json` declares 1.9.0 / RC1, stable authority 1.8.0, proposed tag `standard-v1.9.0-rc1`.
- [ ] Catalog contains exactly **121 unique rules**.
- [ ] Main standard contains every catalog rule ID.
- [ ] `STD-ASYNC-002` and `STD-AUTH-SOURCE-001` are both present in the catalog and normative standard.
- [ ] Async proposal uses unique ID `IJAS-0034`; historical `IJAS-0012` remains the Header Family Alignment Contract.
- [ ] `MIGRATION_1.9.0_RC1.md` exists.
- [ ] `RELEASE_NOTES_1.9.0_RC1.md` exists.
- [ ] `TEST_MATRIX_1.9.0_RC1.md` exists.
- [ ] This checklist exists.
- [ ] No release-root hygiene violations.

## Validation
- [ ] `bash Checks/validate-standard.sh` PASS.
- [ ] `python3 Checks/validate-conformance-catalog.py` PASS.
- [ ] `python3 -m unittest Checks/test_validate_app_conformance.py` PASS.
- [ ] GitHub Actions PASS on the exact final RC commit.

## `STD-ASYNC-002` evidence
- [ ] At least one exact-build reference adoption exists.
- [ ] Invite create/publish responsiveness is runtime verified where supported.
- [ ] Cancel/revoke responsiveness is runtime verified where supported.
- [ ] Retry/reconciliation responsiveness is runtime verified where supported.
- [ ] Visible in-progress UI is verified for long remote work.
- [ ] `STD-CLOUD-001` remote-truth behavior remains intact.
- [ ] `STD-CLOUD-002` retry/reconciliation behavior remains intact.

## `STD-AUTH-SOURCE-001` evidence
- [ ] At least one exact-build reference adoption exists.
- [ ] Applicable user-facing result identifies the authoritative source and used version/effective date.
- [ ] Exact citation or verbatim provision is available for legal/equivalently normative content.
- [ ] Source basis opens with network unavailable.
- [ ] Verification/provenance trace is preserved for verified content.
- [ ] Official external source is supplemental and not the only access path.
- [ ] Regression evidence links the user-facing result to the authoritative source basis.

## Root-title clarification
- [ ] Peer root screens use one shared title family.
- [ ] Final title sizing is container/viewport driven rather than device-name driven.
- [ ] Supported compact-width runtime checks prefer full title over isolated truncation.

## Cross-app applicability
- [ ] IbaJuraj apps are audited for `hasRemoteInviteShareAccessFlow`.
- [ ] IbaJuraj apps are audited for `hasAuthoritativeFunctionalSources`.
- [ ] Apps without a capability are explicitly non-applicable.
- [ ] Apps with a capability have an adoption plan or runtime evidence.

## Publication
- [ ] PR #9 is no longer draft only after all candidate gates above are satisfied.
- [ ] Candidate changes are merged to `main` only when promotion strategy is agreed.
- [ ] Tag `standard-v1.9.0-rc1` is created only from the exact validated commit.
- [ ] No 1.9 RC tag exists before the runtime evidence gate is complete.
