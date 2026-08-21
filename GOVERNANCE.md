# Správa IbaJuraj Application Standard

## Zdroj pravdy

Autoritatívna verzia je verzia publikovaná v spoločnom GitHub repozitári IbaJuraj. Kópie vložené do aplikácií slúžia na audit konkrétneho buildu a musia uvádzať verziu štandardu.

## Verzionovanie

Používa sa sémantické verzionovanie:

- PATCH – spätne kompatibilné spresnenie, oprava alebo quality/safety hardening existujúceho spoločného kontraktu; MAY pridať podmienené pravidlo pre funkciu, ktorú nie všetky aplikácie používajú, ak nevyžaduje migráciu nedotknutých produktov,
- MINOR – nový spoločný capability/contract, ktorý rozširuje povinný rozsah adopcie relevantných aplikácií alebo vyžaduje plánovaný širší adopčný krok,
- MAJOR – zmena, ktorá vyžaduje migráciu aplikácií alebo mení záväzné správanie.

## Proces zmeny

1. návrh,
2. posúdenie dopadu na všetky aplikácie,
3. rozhodnutie MUST / MUST NOT / SHOULD / SHOULD NOT / MAY,
4. schválenie,
5. aktualizácia štandardu a changelogu,
6. audit a postupná adopcia aplikáciami.

Pri MINOR alebo MAJOR vydaní SHOULD byť pred finálnym tagom vytvorený release candidate. Kandidát sa overí najmenej na všetkých aktívnych aplikáciách, ktorých sa nové spoločné pravidlo týka. Finálny tag MUST byť vytvorený až po úspešnej validácii release obsahu a zaznamenaní známych výnimiek.

Nový numerický token v MINOR verzii MUST byť aditívny, `preferred`, `minimum` alebo spätne kompatibilný `range`. Nekompatibilná náhrada existujúceho povinného `exact` tokenu vyžaduje MAJOR verziu alebo zachovanie starého variantu počas migračného obdobia.

## Automatizácia

Audit môže automaticky vytvoriť návrh, upozornenie alebo report. Nemôže bez schválenia zaviesť nové MUST pravidlo, zrušiť výnimku ani zmeniť produktovú architektúru.
