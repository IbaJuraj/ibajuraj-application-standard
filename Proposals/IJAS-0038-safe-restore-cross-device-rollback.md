# IJAS-0038 — Safe Restore and Cross-Device Proof
**Status:** accepted for candidate 1.9.0 RC4; **Rule:** `STD-BACKUP-002`.

**Problem:** XCTest and export success do not prove full-state restore. Partial DB replacement may lose historical/other persisted state on a real device.

**Contract:** Read-only compatibility preview, consent, isolated staging, checkpoint, rollback through verified activation, schema/corruption tests and second-device parity. Financial merge must remain domain-specific.

**Applies to:** `hasUserRestore` independently from export. **Evidence:** fault injection and exact-build runtime restore including off-DB state.
