# Migration to IbaJuraj Application Standard 1.9.0 RC2

**Stable authority remains:** 1.8.0  
**Candidate:** 1.9.0 RC2  
**Candidate rule count:** 131

## Development builds
Use Product → Build, Product → Test and targeted regression of changed/high-risk areas. Full whole-app audit is not required after each small build.

## Release Candidate
For a build nominated for App Store/store/production:
1. run In-App Full App Check,
2. compare against the last production/App Store baseline,
3. execute deterministic/app-specific checks,
4. run critical journeys and applicable failure scenarios,
5. run representative UI/runtime matrix,
6. run AI review if enabled,
7. review severities/exceptions,
8. export the exact-build Evidence Bundle.

Any material change creates a new RC and repeats the gate.

## AI
Set `hasAIReleaseReview = true` only when AI is part of the release audit. Sanitize inputs; AI findings are advisory until corroborated or human-confirmed.

## Post-release
Set `hasPostReleaseMonitoring = true` where privacy-respecting production crash/error/performance monitoring exists.
