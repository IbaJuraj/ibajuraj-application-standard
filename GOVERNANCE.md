# Governance – IbaJuraj Application Standard 1.7.0

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
