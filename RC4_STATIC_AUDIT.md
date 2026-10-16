# IbaJuraj Standard — RC4 Static Audit (16 Oct 2026)

**Parent:** RC3 head `36ef13e55ff838368cc8d5fd718c6d37fe9f73c3`.  
**Candidate:** `standard-1.9.0-rc4-data-continuity-updates`.  
**Stable public metadata:** remains 1.8.0, never promoted by this draft.

## Scope
TradeBook 269 R8, Strážca Termínov 134 and Peňaženka Kariet 92 source audit plus App Update service review motivate 4 additional rule IDs. The existing native iPad adaptive matrix and RC3 Release Inspector cadence are **already covered**; no duplicate rules created.

## Rule mapping
- Backup scope + secret exclusions supplement `STD-DATA-005/006/008`.
- Safe restore requires an independent runtime gate, not simply exported file existence.
- Shared-content parity extends `STD-CLOUD-001/002` and `STD-BACKEND-002` rather than redefining remote truth.
- Update-notice control supplements app About/release channels and is conditional on an actual provider.
- `IbaJuraj DataKit` and `App Update Kit` are optional, implementation-specific libraries.

## Validation/evidence distinction
- Catalog IDs and candidate schema need static/catalog/validator tests and GitHub Actions.
- Native Xcode builds, live cloud sharing and real recovery need app-owned runtime acceptance. These **are not** made PASS by this Standard PR.
- Known open scenarios: TradeBook second-device restore; Strážca recipient content; Peňaženka shared-wallet full two-account lifecycle.

## Versioning guardrail
Old RC3 PR #12 is a predecessor; the new draft is independent. Stable 1.8.0 must remain public authority until separate stable promotion.

## Pre-adoption consolidation decisions

- No removal of rule IDs: 138 remain. The 90 missing legacy `title` fields are non-normative descriptive metadata.
- `STD-DIAG-001` may use an isolated external/CI diagnostic equivalent; no forced production UI.
- `STD-LOC-005` is scoped to in-app picker, not every localized app.
- `STD-AUTH-SOURCE-001` separates offline norm/legal evidence from live API source/freshness.
- `STD-SHARE-001` tests persistent recipient content, not mere invite/access role or one-off card link.
- RC-only checks run in release-candidate phase; post-release production feedback remains a later MUST, not pre-release-blocking.
- Executed evidence requires exact version/build/source revision/phase, check identity, PASS result, runner/time, device/OS when UI or runtime, and SHA256-matching primary artifact. Missing becomes PENDING; wrong source/failed/tampered evidence becomes FAIL.
- Two missing legacy capability flags are now declared in candidate template. Catalog applicability validates nested operators and known flags.
- Static validator fixtures are synthetic; app-native and physical-device proof stays pending independently.
