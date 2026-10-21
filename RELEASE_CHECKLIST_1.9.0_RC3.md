# IbaJuraj Application Standard 1.9.0 RC3 — Candidate Checklist

## Package
- [x] RC2 131-rule candidate preserved
- [x] IJAS-0036 accepted
- [x] AI family consolidated to seven contracts
- [x] candidate catalog expanded to 134 rules
- [x] AI risk-profile/execution metadata added
- [x] main Standard updated to RC3
- [x] RC3 migration, release notes, test matrix and checklist added
- [ ] final SHA256 manifest refreshed before tag/publication

## AI conformance
- [ ] every AI feature has stable feature ID
- [ ] every AI feature has valid risk profile
- [ ] every AI feature has on-device/cloud/hybrid execution metadata
- [ ] grounded/authoritative source boundary reviewed
- [ ] generated vs authoritative UI semantics reviewed
- [ ] AI is read-only by default
- [ ] secrets/credentials absent from model inputs
- [ ] credentials stored securely with least privilege
- [ ] provider/model unavailable/offline/quota/billing failure tested
- [ ] imported/external prompt-like content treated as data
- [ ] structured outputs validated before deterministic use
- [ ] model/provider/prompt/tool-policy regression suite PASS
- [ ] rollback path verified
- [ ] adaptive learning provenance/reset/reversibility verified where applicable

## Pilot Release Candidate
- [ ] TradeBook pilot nominated
- [ ] Product → Build PASS
- [ ] Product → Test PASS
- [ ] In-App Full App Check PASS
- [ ] Release Inspector deterministic findings reviewed
- [ ] local AI path tested where supported
- [ ] cloud fallback tested if enabled
- [ ] no unresolved BLOCKER/ERROR without exception
- [ ] Evidence Bundle exported

## Promotion
- [ ] cross-app AI applicability reviewed
- [ ] non-AI apps verified unaffected
- [ ] validation workflow green on final candidate commit
- [ ] checksum manifest refreshed
- [ ] RC3 tag/release only after candidate gate
