# IJAS-0037 — Portable Backup Scope and Integrity
**Status:** accepted for candidate 1.9.0 RC4; **Rule:** `STD-BACKUP-001`.

**Problem:** File export may be incomplete or misleading. Sensitive user data require confidentiality, authenticated integrity and safe key handling. Historical/off-DB state is easily omitted.

**Contract:** Inventory+schema, authenticated integrity/encryption according to sensitivity, independent secret recovery and explicit exclusions. Wrong-key/corrupt payload tests. No mandatory SQLite adapter across unrelated apps.

**Applies to:** `hasPortableBackup`; other apps N/A. **Evidence:** deterministic export/integrity tests plus build-scoped runtime file evidence. No restore claims.
