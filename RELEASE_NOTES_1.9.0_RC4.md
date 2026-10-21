# IbaJuraj Application Standard 1.9.0 RC4 — Candidate Release Notes

**Candidate date:** 16 October 2026  
**Stable authority:** `standard-v1.8.0`  
**Candidate branch:** `standard-1.9.0-rc4-data-continuity-updates`  
**Proposed tag:** `standard-v1.9.0-rc4` — NOT created

RC4 preserves the 134 RC3 candidate contracts and adds four machine-readable rules, for **138** total. It is a non-breaking candidate and does not modify stable metadata.

## New normative scope

- `STD-BACKUP-001`: portable backup manifest/scope/completeness, authenticated integrity/encryption when personal/financial data are involved, safe recovery-key lifecycle and secret exclusions.
- `STD-BACKUP-002`: compatible staged restore, destructive-operation preview, rollback, corruption tests and **independent second-device recovery evidence**.
- `STD-SHARE-001`: actual delivered content parity after invitation, protection against empty-owner overwrite, follow-up sync/edit/revoke.
- `STD-UPDATE-001`: distribution channel identity, meaningful version comparison, successful-check TTL vs bounded failure retry, version-scoped snooze and non-blocking localized UX.

## Not new requirements

Native iPad/adaptive layout was already specified; this candidate does not force all iPhone apps to support iPad. Existing RC3 AI provider/fallback/read-only and release audit cadence remain unchanged. Common Swift packages are optional.

## Promotion prerequisites

Candidate/static validation; independent app native/runtime proof; correct handling of financial/history/off-DB data, invite/content truth, and provider update failure/snooze. No stable tag, version or app build change is implied.

## RC4 consolidation — scope refinement only

All **138 rule IDs** remain stable; no arbitrary removals or new RC numbering. The refinements clarify seven ambiguous/overbroad areas: phase-specific Release Inspector, external-allowed developer diagnostics, optional own language selector, live-vs-normative authoritative sources, persistent content-vs-access sharing, non-blocking post-release feedback, and exact-build verified test evidence.

Legacy catalog titles are now machine-readable summaries, **not a rewrite of inherited normative clauses**. The template exposes missing applicability flags. Central CI PASS is distinct from runtime adoption PASS in TradeBook, Lex Drive, Strážca, Peňaženka and Kalkulačka.

Stable 1.8.0 and existing App Store binaries remain unchanged.

## Governance acceptance addendum — 22 October 2026 (CANDIDATE, NOT STABLE)

The owner approved [IJAS-0041](Proposals/IJAS-0041-central-standard-promotion-vs-app-release-adr.md), which distinguishes publication of the validated shared Standard from full App Store/production acceptance of individual apps. **All applicable MUST/MUST NOT requirements remain unchanged and enforced at the respective app release gate.** Pending cross-device restore (TradeBook), recipient content parity (Strážca), two-account wallet share (Peňaženka), exact app release checks and AI/provider applicability are not certified by publishing the central Standard.

On the documented prior head `d898962`, 138/138 catalog, 47/47 tests and 132-file manifest were green; the Calculator B64 R6 pilot proved failure/pending enforcement but not positive native execution evidence or full RC compliance. Positive execution evidence, cross-app capability register, new exact-head CI and separate merge/tag authorization remain required. Public stable 1.8.0 is unchanged.
