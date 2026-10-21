# Test Matrix – IbaJuraj Application Standard 1.9.0 RC1

## Package gates

Run on the exact candidate commit:

- `bash Checks/validate-standard.sh`
- `python3 Checks/validate-conformance-catalog.py`
- `python3 -m unittest Checks/test_validate_app_conformance.py`

All must pass.

## Stable inheritance gate

Confirm that all 119 rules inherited from 1.8.0 retain their IDs and semantics, that the candidate catalog contains exactly 121 unique rules, and that stable authority remains 1.8.0 until promotion.

## Async responsiveness gate (`STD-ASYNC-002`)

For every adopting app with `hasRemoteInviteShareAccessFlow = true`, verify the exact candidate build where supported:

1. opening invite/access UI remains responsive while remote preparation is pending,
2. invite create/publish does not freeze navigation, sheet presentation or primary interaction,
3. cancel/revoke remains responsive while the remote mutation is pending,
4. retry/reconciliation work does not monopolize MainActor/UI interaction,
5. long operations expose visible progress,
6. remote destructive/access success is shown only after confirmed remote truth,
7. transient failures preserve retry/reconciliation,
8. representative slow-network/backend latency is included in runtime evidence.

## Authoritative-source gate (`STD-AUTH-SOURCE-001`)

For every adopting app with `hasAuthoritativeFunctionalSources = true`, verify the exact candidate build:

1. the user-facing result identifies the authoritative source used,
2. the exact source version/effective date is available where the source changes over time,
3. legal or equivalently normative results expose exact citation or verbatim provision,
4. the source basis remains accessible with network unavailable,
5. verified content exposes or preserves a verification/provenance trace,
6. an official external source may be opened when online but is not the only access path,
7. user-friendly labels/descriptions do not replace the authoritative citation,
8. regression coverage proves the result still maps to the intended authoritative source after updates.

For Lex Drive, include representative offence/administrative-delict legal chains and at least one offline opening of the exact cited provision.

## Root-title family clarification gate

For representative peer root screens on compact and regular widths:

1. use one shared title family/token strategy,
2. derive final sizing from available container/viewport width,
3. avoid device-name-specific sizing branches where a container rule is sufficient,
4. prefer a complete readable title over isolated `…` truncation,
5. keep nested/system navigation headers as a separate family.

## Reference-app gates

- Strážca Termínov Build 120 Phase 14A R12 or its superseding exact candidate build: capture build-scoped runtime evidence for supported invite/cancel/revoke/reconcile paths before RC tagging.
- Lex Drive Build 232 or its superseding exact candidate build: capture build-scoped evidence for offline legal citation, version/effective-date metadata and authoritative legal-chain traceability before RC tagging.

## Regression gates

Re-run applicable 1.8.0 gates for each adopting app, especially:

- security/app lock,
- persisted-data continuity,
- Production backend read/write/sync/share,
- async derived-state integrity,
- permission/privacy parity,
- representative-data performance,
- screen-family runtime audit.
