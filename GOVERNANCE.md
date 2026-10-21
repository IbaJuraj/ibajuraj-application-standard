# Governance – IbaJuraj Application Standard

## Change classes
- PATCH: clarification/hardening without new contract family.
- MINOR: new compatible contract family, test system or shared UX behavior.
- MAJOR: incompatible product/release contract.

## Stable rule IDs
Once a `STD-*` ID is published, its semantic meaning SHOULD NOT be silently repurposed. Breaking semantic change receives a new ID.

## Exceptions
A MUST/MUST NOT exception requires:
- reason,
- affected rule ID,
- scope,
- risk,
- compensating control,
- review/removal condition,
- ADR path.

## RC promotion
RC may be used for implementation work but is not public authority. Promotion to active requires package validation and at least one real application adoption proving the new conformance machinery.

## Release-candidate iteration
A later RC supersedes an earlier RC for new adoption work without rewriting the historical RC tag/release. Semantic rule IDs already introduced SHOULD retain their meaning; newly discovered obligations receive new IDs. Promotion to active requires resolving all known RC ambiguities and completing the agreed cross-app adoption matrix.

## Central Standard publication vs application release (IJAS-0041, accepted 22 October 2026)

See [IJAS-0041](Proposals/IJAS-0041-central-standard-promotion-vs-app-release-adr.md). Central stable Standard publication certifies the normative package, validation tooling, integrity and promotion evidence **only**. It does **not** certify every consuming application.

Central promotion MUST satisfy all of:
- complete normative/compatibility audit and closure of known RC ambiguities;
- current exact-head package CI and complete SHA256 integrity;
- a **real-application conformance adoption** showing negative/PENDING guards *and* genuine positive native and UI/runtime evidence accepted by the validator on an exact app source/build;
- a completed cross-app capability and status matrix with factual `PASS/PENDING/N/A/EXCEPTION` and unambiguous ownership of outstanding app-specific acceptance;
- documented governance/ADR sign-off; and
- a **separate explicit owner authorization** for stable merge/tag after final review.

Individual apps remain responsible for **all** applicable MUST/MUST NOT rules on the exact nominated release build, including full `--phase release-candidate` native/runtime/visual and high-risk cloud sharing, data restore/rollback, AI/release inspector and update-provider checks. Their application release gate blocks that app, even when the central Standard is stable. PENDING or FAIL is never PASS; N/A must be supported by source/capability review. The existing rule-level exception contract is unchanged.

An approved decision to separate scheduling does not waive a normative rule. Any unapproved central gate, including real positive adoption, **still blocks** Standard promotion.
