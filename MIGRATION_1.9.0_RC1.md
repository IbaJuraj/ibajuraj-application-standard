# Migration to IbaJuraj Application Standard 1.9.0 RC1

**Stable authority remains:** 1.8.0 (`standard-v1.8.0`)  
**Candidate:** 1.9.0 RC1  
**Candidate rule count:** 121

## Scope

1.9.0 RC1 introduces two new compatible cross-app contracts:

- `STD-ASYNC-002` — remote invite/share/access operations must not block interactive UI/MainActor responsiveness.
- `STD-AUTH-SOURCE-001` — an authoritative legal/regulatory/normative source used by a functional result must be available locally/offline, version/effective-date identified, exactly citable and externally traceable.

The 119-rule stable 1.8.0 set remains semantically unchanged. RC1 also clarifies the existing root-title family so peer root titles adapt from available viewport/container width rather than device-name-specific sizing.

## Applicability audit

Apps with remote invite/share/access flows set:

`hasRemoteInviteShareAccessFlow = true`

and verify supported create/publish, cancel/revoke, retry/reconciliation and screen responsiveness paths.

Apps that use authoritative legal, regulatory, normative or equivalent sources as part of a user-facing functional result set:

`hasAuthoritativeFunctionalSources = true`

and verify that the exact source basis used by the result is available without network access, identifies the used version/effective date and remains traceable to verification provenance and an optional official external source.

## `STD-ASYNC-002` migration

Remote network/backend orchestration must execute outside the interactive UI executor when it can take noticeable time. UI should present the destination screen without waiting for remote preparation and expose visible progress for long work. A delayed backend response is acceptable; frozen-feeling UI is not.

This rule does not weaken remote-truth requirements. `STD-CLOUD-001` and `STD-CLOUD-002` continue to govern authoritative completion and retry/reconciliation.

## `STD-AUTH-SOURCE-001` migration

For every applicable result:

1. identify the authoritative source and the exact version/effective date used,
2. provide a local/offline representation of the source basis,
3. expose the exact citation or verbatim provision for legal or equivalently normative content,
4. preserve a verification/provenance trace where verified content is used,
5. keep the official external website as a supplemental path only, never the sole way to access the authoritative basis,
6. add an offline runtime test and a regression check linking the user-facing result back to the authoritative source.

For Lex Drive this means legal chains such as duty → qualification → sanction/seriousness layer remain inspectable offline even when Slov-Lex is unavailable.

## Root-title clarification

Peer root screens should share one title family and derive the final title token from available width. Existing per-device hardcoding or one-off truncation behavior should be removed during the next planned UI audit.

## Adoption order

1. Strážca Termínov — reference adoption for `STD-ASYNC-002` from Build 120 Phase 14A R12 or its superseding exact build.
2. Lex Drive — reference adoption for `STD-AUTH-SOURCE-001` from Build 232 or its superseding exact build.
3. Audit all other IbaJuraj apps for both capability flags.
4. Promote 1.9.0 only after candidate validation and cross-app applicability/runtime review.
