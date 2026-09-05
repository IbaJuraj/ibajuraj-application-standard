# APP_STANDARD_ADOPTION

- Standard: IbaJuraj Application Standard 1.8.0 RC1
- Standard candidate tag: `standard-v1.8.0-rc1`
- Public authority during RC adoption: `standard-v1.7.0`
- Adoption status: release-candidate
- Adoption level: Level 0–4
- Product: <app name>
- Build: runtime
- Conformance manifest: `STANDARD_CONFORMANCE.json`

## Exceptions
List ADR-backed exceptions by `STD-*` ID. Empty means none.

## 1.8.0 RC1 additions
- Localization-ready architecture and locale-aware formatting/pluralization are audited if localization applies.
- If `hasInAppLanguageSelector=true`, verify Automatic/System mode, all runtime-supported languages, persistence and data-neutral switching.
- If localization + persisted data apply, raw IDs/keys/transport metadata remain locale-neutral.
- If localization + search apply, verify localized search names/aliases.
- Release root contains only current authoritative build/release documentation; superseded evidence is archived/consolidated.
- If `hasEnvironmentSpecificBackend=true`, stable local domain identity is separated from Development/Production binding identity.
- Production schema/config/permissions and a real TestFlight/Production smoke are evidenced.
- Persistent-data apps run performance smoke with a representative real-volume dataset.

## Viewport/screen audit inherited from 1.7.0
- `STANDARD_CONFORMANCE.json` includes capability-accurate `screenAudit.families`.
- Primary root top anchors and fixed bottom chrome follow shared viewport contracts.
- Header ownership, sheet hierarchy and system-chrome ownership are audited where applicable.
- Level 4 requires zero pending release-blocking rules and zero pending screen families.

## RC rule
Adopting an RC does not make it the public active Standard. Until final promotion, user-facing About surfaces should continue to identify the active Standard according to the product's release policy unless the app is explicitly distributed as an RC adoption build.
