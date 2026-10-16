# IJAS-0039 — Shared Recipient Content Parity
**Status:** accepted for candidate 1.9.0 RC4; **Rule:** `STD-SHARE-001`.

**Problem:** Successful CloudKit invite/membership does not imply recipient sees owner records; missing snapshot and destructive initial push can corrupt owner state.

**Contract:** Separate invite/role/content evidence, download-first or equivalent safe first sync, owner-preserving conflict/retry and later edit/revoke acceptance. One-off card share is not shared-wallet success.

**Applies to:** `hasCloudSharingOrAccessControl`. **Evidence:** Production-relevant two-account recipient-record parity and revoke.
