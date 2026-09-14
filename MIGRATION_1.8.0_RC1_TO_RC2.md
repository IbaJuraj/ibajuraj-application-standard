# Migration — IbaJuraj Application Standard 1.8.0 RC1 → RC2

RC2 is not a blind 11-rule append because RC1's tagged machine catalog remained on the 96-rule stable baseline.

## Adoption steps
1. Move an app Standard declaration to `1.8.0-rc2` only after an applicability audit.
2. Evaluate the 12 formalized RC1 rules and 11 new RC2 rules.
3. Preserve prior valid 1.7 evidence only where the exact tested behavior/build remains applicable and the evidence type is still sufficient.
4. Do not carry runtime PASS automatically to a different app build.
5. Run production→candidate upgrade testing when persisted data exists.
6. Add automated regression coverage for material deterministic engines.
7. Verify disabled permissioned features have no active entry point and no permission prompt.
8. Update `APP_STANDARD_ADOPTION.md` and `STANDARD_CONFORMANCE.json`.
