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
