# APP_STANDARD_ADOPTION

- Standard: IbaJuraj Application Standard 1.7.0
- Standard tag: `standard-v1.7.0`
- Adoption status: active
- Adoption level: Level 0–4
- Product: <app name>
- Build: runtime
- Conformance manifest: `STANDARD_CONFORMANCE.json`

## Exceptions
List ADR-backed exceptions by `STD-*` ID. Empty means none.

## 1.7.0 viewport/screen audit
- `STANDARD_CONFORMANCE.json` includes capability-accurate `screenAudit.families`.
- Primary root top anchors and fixed bottom chrome follow shared viewport contracts.
- Header ownership, sheet hierarchy and system-chrome ownership are audited where applicable.
- Level 4 requires zero pending release-blocking rules and zero pending screen families.
