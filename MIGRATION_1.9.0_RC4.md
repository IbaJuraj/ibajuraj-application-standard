# Migration to IbaJuraj Application Standard 1.9.0 RC4

**Candidate only.** Public stable authority and stable metadata remain `1.8.0`. No automatic migration of application databases or user data.

1. Preserve all 134 RC3 rule objects and add only the four RC4 scoped contracts; pin `standardVersion: 1.9.0` and `standardCandidate: RC4` in the app's candidate conformance manifest.
2. Declare Boolean capabilities `hasPortableBackup`, `hasUserRestore` and `hasAppUpdateNotice`. The existing `hasCloudSharingOrAccessControl` selects shared-content parity. Declare true **only for features the app actually exposes**; missing/false = N/A.
3. Export-only does not imply restore; restoring an externally supplied backup does not imply the app can also export. No capability is imposed solely because an optional shared Swift Package exists.
4. For portable backup, audit versioned format/manifest, off-database data, authenticated encryption according to sensitivity, independent recovery-key handling and intentional secret exclusions.
5. For restore, require read-only preflight and user consent, migration compatibility, staged commit/checkpoint, safe rollback and isolated-device content comparison before saying full recovery PASS.
6. For cloud sharing, test invitation and membership separately from delivered recipient records; verify no destructive empty initial sync, subsequent edits/conflicts and revoke on two real accounts.
7. For update notices, test App Store/TestFlight/private provider correctness, last attempt vs last successful check, shorter bounded retry, per-version snooze and correct localized URL. Non-App-Store private apps are N/A without a real provider.
8. Existing native iPad support belongs to `STD-ADAPT-*` / `STD-SCREEN-*` adoption and iPad matrix, not a new RC4 rule ID.
9. Adopt shared security utilities only after application-specific secret/storage/CloudKit review; domains retain distinct credentials, keys, identities and merge policies.
10. Re-run the candidate validators and record exact-app-version/build/device/OS evidence. Full release-quality check is for release candidates, not each small development revision.

**Initial pilots:** TradeBook 269 R8 cross-device backup/restore on iPad (still runtime pending); Strážca 134 recipient content parity after accepted invite (still pending); Peňaženka 92 shared-wallet two-account lifecycle (still pending); store apps update service checks before later release builds.

No RC4 rule or proposal is already a production feature merely because it is documented here.
