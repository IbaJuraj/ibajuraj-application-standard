# Migration to IbaJuraj Application Standard 1.8.0

1.8.0 is non-breaking relative to the integrated RC2 rule catalog.

## Required adoption steps

1. Update declared standard version to `1.8.0` and stable tag to `standard-v1.8.0`.
2. Re-run applicability and evidence validation for the 119-rule catalog.
3. Preserve existing 1.8 RC1/RC2 data, localization, backend, async, cloud and evidence contracts.
4. Re-audit `STD-SECURITY-001` in every app that has a local app lock:
   - biometric unlock is primary when enabled,
   - system device authentication (device passcode/password) is the fallback,
   - a separate app PIN is not a prerequisite for enabling biometrics,
   - an optional app PIN may remain only where product-specific value exists.
5. Record runtime evidence for the exact candidate build used for adoption.

## No automatic domain-data migration

Adopting Standard 1.8.0 alone must not rewrite user domain data, stable raw IDs or cloud identities.
