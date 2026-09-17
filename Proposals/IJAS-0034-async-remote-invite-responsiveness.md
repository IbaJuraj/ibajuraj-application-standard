# IJAS-0034 — Async Remote Invite Responsiveness

**Status:** accepted  
**Target:** 1.9.0 RC1  
**Date:** 2026-09-16  
**Renumbered:** 2026-09-17 from an unpublished colliding draft ID `IJAS-0012`

## Problem

Runtime testing of CloudKit invitation flows showed that invite publish/cancel/reconcile work can take several seconds. When the complete remote workflow is isolated to `MainActor`, navigation, sheet presentation and other interactions can feel frozen even when the underlying CloudKit calls are asynchronous.

This is not limited to one application. Any IbaJuraj app with remote invite/share/access mutations can hit the same failure mode.

## Rule

### STD-ASYNC-002 — MUST

Remote invite/share/access operations that can wait on network or backend state MUST NOT block interactive UI/MainActor responsiveness.

When applicable:

- remote orchestration SHOULD execute on a dedicated actor, background executor or equivalent non-UI isolation,
- opening an invite/access screen MUST NOT wait for remote preparation,
- long operations MUST expose a visible in-progress state such as `Pripravujem…`, `Ruším…` or equivalent,
- the rest of the screen SHOULD remain interactive whenever product safety allows it,
- retry/reconciliation MUST run asynchronously,
- remote destructive/access success MUST still follow confirmed remote truth under `STD-CLOUD-001`,
- transient failures MUST preserve a retry/reconciliation path under `STD-CLOUD-002`,
- runtime verification MUST include create/publish, cancel/revoke and retry/reconcile paths where the app supports them.

## Applicability

Capability: `hasRemoteInviteShareAccessFlow = true`

Default verification: `runtime`

Release blocking: `true`

## Relationship to existing rules

- `STD-ASYNC-001` prevents stale async completion from overwriting newer state.
- `STD-CLOUD-001` requires confirmed remote truth for destructive/access success.
- `STD-CLOUD-002` requires durable retry or reconciliation.
- `STD-ASYNC-002` adds the missing responsiveness contract: those remote workflows must not monopolize interactive UI execution while they wait.

## Reference implementation pattern

On Swift/SwiftUI, a dedicated actor for CloudKit invitation transport is an acceptable implementation. UI state commits remain on MainActor, while network orchestration executes outside MainActor. This is an implementation example, not a platform-specific requirement.

## ID correction

`IJAS-0012` was already assigned to **Header Family Alignment Contract** and remains historically owned by that proposal. The async proposal therefore uses the next free proposal identity `IJAS-0034`; no published historical proposal ID is repurposed.
