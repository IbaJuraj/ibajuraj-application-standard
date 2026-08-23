# Audit IbaJuraj Application Standard 1.6.2 → 1.6.3

**Dátum:** 2026-08-21
**Výsledok:** základ 1.6.2 je architektonicky zdravý; 1.6.3 je vhodný ako spätne kompatibilný quality/safety hardening.

## Silné stránky 1.6.2

- jasná hierarchia Standard → Product Standard → ADR → Build Scope,
- normatívny MUST/SHOULD/MAY jazyk a adoption levels,
- silné common UX kontrakty pre Settings, navigation, Dynamic Type, neutral surfaces a header family,
- dobré pravidlá single source of truth, migration, remote content, privacy a release evidence,
- source-hygiene review threshold a behaviorálne quality gates.

## Zistené medzery

1. Bottom navigation mala iba všeobecné „nesmie zakrývať obsah“, ale chýbal spoločný dynamický clearance a parity gate medzi peer rootmi.
2. Pinned header bol v 1.6.1 formulovaný príliš všeobecne a mohol viesť k automatickému pripínaniu sekcií, ktoré kontext nepotrebujú.
3. Chýbal spoločný kontrakt pre AI/generované odpovede: grounding, low confidence, fallback, feedback a debug isolation.
4. Single-source pravidlo bolo silné na úrovni princípu, ale chýbala explicitná separation/traceability formulácia pre presentation layer a časovo verziované autoritatívne dáta.
5. Search neobsahoval explicitné pravidlo, že „najbližší“ nesúvisiaci výsledok je horší než žiadny výsledok/clarification.
6. Potvrdená runtime chyba nemala explicitný lifecycle do behaviorálneho regresného testu.
7. Line-count source hygiene potreboval spresniť, že ide o review trigger, nie mechanický hard limit.

## Zistené dokumentačné nekonzistencie 1.6.2

- `TEST_MATRIX.md` bol stále označený ako 1.6.1.
- `CHANGELOG.md` obsahoval dve sekcie 1.5.0; typografická patch sekcia patrila k 1.4.1.
- `RELEASE_NOTES_1.4.1.md` mal chybný nadpis a text „1.5.0“.
- hlavný Standard obsahoval dvakrát identickú vetu o lokalizovaných App Store textoch.

## Rozhodnutie pre 1.6.3

- Nezavádza sa paralelná architektúra ani produktovo špecifický Lex Drive engine do globálneho Standardu.
- Do Standardu vstupujú iba všeobecné kontrakty použiteľné naprieč IbaJuraj aplikáciami.
- Konkrétne režimy `Auto / Classic / AI Test`, názvy Lex Drive engine súborov a právny corpus roadmap ostávajú produktovo špecifické.
- Existujúce pravidlá header family, neutral surfaces, Dynamic Type a runtime metadata sa neduplikujú; nové pravidlá ich iba dopĺňajú.
