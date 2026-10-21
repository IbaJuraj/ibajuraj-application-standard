# IbaJuraj Application Standard 1.9.0 RC4 — Candidate Checklist

## Candidate implementation
- [x] Fork exact RC3 head into isolated RC4 branch; do not mutate public stable `main` 1.8.0.
- [x] Preserve existing 134 rules; add only four capability-scoped IDs (138 candidate).
- [x] Update normative text, catalog, conformance schema/template, validator and regression tests.
- [x] Candidate migration, notes, test matrix, adoption plan and proposals present.
- [ ] Candidate shell validation and GitHub Actions green on exact commit.
- [ ] Final SHA256SUMS refreshed and validated.

## Historical cross-app runtime register (now app-specific release blockers under IJAS-0041)
- [ ] TradeBook encrypted portable export and complete second-device restore/rollback (new secret private).
- [ ] Strážca Termínov 134 owner/recipient Octavia + six terms content parity and edit/revoke.
- [ ] Peňaženka Kariet 92 complete two-account wallet sharing lifecycle, separate from one-off card link.
- [ ] Update notice regression tests for Store app identity, network failure, snooze, localization and destination.
- [ ] iPad adaptive UI tested where support declared, with exact build/device evidence.

## Final stable promotion — NOT authorized by this PR
- [ ] RC3 AI and Release Inspector applicability and exact-build evidence complete.
- [ ] RC4 requirements evaluated in all relevant apps; no unresolved blockers without approved ADR.
- [ ] Full candidate CI and checksum integrity PASS, release quality gate signed.
- [ ] Explicit authorization before stable merge/tag. The existing `standard-v1.8.0` stays public authority until then.

## Consolidation checklist (candidate only)

- [x] Preserved 138 machine-readable rule IDs; 90 historical records have descriptive titles.
- [x] Phase-scoped RC gate, external diagnostic equivalence, scoped locale/share conditions, authority freshness and post-release semantics documented.
- [x] Execution evidence format validates actual PASS vs declared tests, with exact build/source/phase and SHA256 artifacts.
- [x] Catalog/template includes previously missing capability flags; regression coverage added.
- [ ] Final exact-commit GitHub workflow and manifest integrity PASS after all edits.
- [ ] Candidate cross-app applicability reviewed before proposed stable promotion.
- [ ] Native runtime recovery/share/AI release requirements proven where supported (not by synthetic fixtures).
All app projects remain unchanged during Standard consolidation.

## Consolidated corrective update — 21 Oct 2026
- [x] Preserved 138 catalog IDs; applied explicit release-candidate conditions to seven existing release/screen contracts.
- [x] Development-only pending evidence no longer claims false PASS or blocks ordinary builds.
- [x] Missing critical capability declarations fail a real RC; SHOULD reports remain advisory.
- [ ] Verify new exact-head CI / checksum manifest and regression tests after this commit.
- [ ] Validate against at least one app with real exact-build test execution evidence; synthetic fixtures alone are insufficient.

## Governing promotion checklist — IJAS-0041 (owner-approved 22 Oct 2026)

This section **supersedes earlier promotion placement** of the cross-app runtime bullets, not their application-level MUST obligations. See [approved ADR](Proposals/IJAS-0041-central-standard-promotion-vs-app-release-adr.md) and [governance](GOVERNANCE.md).

### Central Standard 1.9.0 stable publication
- [x] C-01: 138-rule content audit and inherited 119 ID integrity.
- [x] C-02 historical: PR head `d898962` CI 2/2; 47/47 tests; 138 catalog; 132 files checksum. **Re-run on next documentation head before promotion.**
- [x] C-03: Calculator 1.15.0/64 R6 negative/PENDING pilot (development exit0, RC exit2, three negative cases); **NOT full app compliance**.
- [ ] C-04: positive **genuine executed** native/unit rule and UI/screen-family or runtime evidence on the same exact app build with primary artifact SHA256 and runner/device provenance. Do not fabricate PASS.
- [ ] C-05: verify and close cross-app capability/N/A and baseline/evidence register without converting app PENDING to PASS.
- [x] C-06 governance principle approved by owner; ADR and PR text documented as a candidate. **Candidate doc CI pending.**
- [ ] C-07: latest-head CI + checksum + release metadata/risk review, then *separate explicit owner approval* for merge/tag.

### Per-app release acceptance register — remains mandatory for each app
- [ ] Calculator 1.15.0/64 R6: full release-candidate applicable rules + seven screen families + native/runtime evidence.
- [ ] TradeBook 2.1.0/280: exact-native Build/Test, second-device full-state restore/rollback, key privacy and actual iPad compatibility where declared.
- [ ] Strážca Termínov 1.62.0/135 R2: recipient **content** parity, follow-up edit/revoke, private records and actual backup restore.
- [ ] Peňaženka Kariet 1.6.0/94 R8: complete owner/recipient two-account shared-wallet edit/revoke, second-device data recovery and privacy/deep-link checks.
- [ ] Lex Drive 1.23.0/325: current legal temporal integrity and exact release evidence/Archive Validate.
- [ ] Each app: provider update notice, RC3 AI runtime controls and Release Inspector **when capability-applicable**; source-backed N/A otherwise.

**No app build generated, no main merge, no stable tag.** Central Standard may publish only after its own C-01…C-07 have actual PASS; existing per-app PENDING never becomes an implicit waiver.
