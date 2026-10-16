# IbaJuraj Application Standard 1.9.0 RC4 — Candidate Checklist

## Candidate implementation
- [x] Fork exact RC3 head into isolated RC4 branch; do not mutate public stable `main` 1.8.0.
- [x] Preserve existing 134 rules; add only four capability-scoped IDs (138 candidate).
- [x] Update normative text, catalog, conformance schema/template, validator and regression tests.
- [x] Candidate migration, notes, test matrix, adoption plan and proposals present.
- [ ] Candidate shell validation and GitHub Actions green on exact commit.
- [ ] Final SHA256SUMS refreshed and validated.

## Cross-app runtime evidence before promotion
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
