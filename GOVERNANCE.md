# Governance – IbaJuraj Application Standard

## Change classes
- PATCH: clarification/hardening without new contract family.
- MINOR: new compatible contract family, test system or shared UX behavior.
- MAJOR: incompatible product/release contract.

## Stable rule IDs
Once a `STD-*` ID is published in a tagged release candidate or stable release, its semantic meaning SHOULD NOT be silently repurposed. Breaking semantic change receives a new ID.

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

## RC publication
Publishing a tagged RC freezes that candidate's normative semantics. If real adoption discovers a normative ambiguity or required contract change, create a later RC rather than silently rewriting the published RC tag/release.

## Release-candidate iteration
A later RC supersedes an earlier RC for new adoption work without rewriting the historical RC tag/release. Semantic rule IDs already introduced SHOULD retain their meaning; newly discovered obligations receive new IDs. Promotion to active requires resolving all known RC ambiguities and completing the agreed cross-app adoption matrix.

## Active authority
Only a release with `standard.json.status = active` and a stable final tag is public authority. A `release-candidate` may be published as a GitHub prerelease and adopted for validation without replacing the current active Standard.
