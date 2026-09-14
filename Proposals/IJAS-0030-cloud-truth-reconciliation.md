# IJAS-0030 — Cloud Mutation Truth and Reconciliation

**Status:** accepted for 1.8.0 RC2.

Adds:
- `STD-CLOUD-001` — remote destructive/access success follows confirmed remote truth,
- `STD-CLOUD-002` — security/access mutations have durable retry or reconciliation.

The rule prevents local UI from claiming successful revoke/cancel/delete/share changes when the remote operation failed, and requires durable reconciliation for security-relevant cloud mutations across interruption or relaunch.
