# IJAS-0028 – Production Backend Environment Readiness

**Stav:** accepted  
**Navrhovateľ:** IbaJuraj Apps  
**Dátum:** 2026-09-05  
**Dotknuté aplikácie:** všetky IbaJuraj aplikácie používajúce backend s oddeleným Development/Production alebo ekvivalentným prostredím  
**Schválená candidate verzia štandardu:** 1.8.0 RC1

## Problém
Aplikácia môže byť zdrojovo aj binárne správna, ale distribuovaný TestFlight/App Store build zlyhá, ak Production backend nemá rovnaké potrebné server-side prerequisites ako Development prostredie. Binárny compile/static PASS preto nedokazuje Production readiness.

## Dôkaz – Peňaženka Kariet
TestFlight Build 78 zlyhával pri osobnej iCloud synchronizácii aj aktivácii zdieľanej peňaženky. CloudKit Console ukázala, že Development schema mala zmeny označené `Modified`, ktoré ešte neboli nasadené do Production.

Do Production boli následne nasadené:
- Record Type `WalletPersonalSnapshot`,
- Record Type `WalletSharedEnvelope`,
- ich indexy,
- Security Roles `_world` → Read, `_icloud` → Create, `_creator` → Write.

Po `Deploy Schema Changes…` začal **ten istý TestFlight Build 78** okamžite fungovať pri personal sync aj sharing. Nebola potrebná zmena binárky. To dokazuje potrebu samostatného Production backend gate a zároveň potrebu rozlišovať server-side fix od app-build fixu.

## Schválený kontrakt
1. Aplikácia s environment-specific backendom MUST pred distribuovaným release overiť Production schema/resources/configuration potrebné pre všetky release-blocking backend capabilities.
2. Ak backend používa indexy, permissions, security roles, zones, tables, buckets, functions, environment variables alebo ekvivalentné server-side objekty, relevantná Production konfigurácia MUST byť explicitne overená.
3. Development úspech MUST NOT byť považovaný za dôkaz Production parity.
4. TestFlight/Production runtime smoke MUST overiť reálny read path a podľa capability aj write/sync/share/invitation path.
5. Backend failure MUST NOT poškodiť bezpečne uložené lokálne doménové dáta; aplikácia má rozlíšiť lokálny stav od cloud/backend chyby.
6. Release evidence MUST zaznamenať, či oprava bola server-side deployment/configuration alebo binárna zmena.
7. Nový app build MUST NOT byť vytváraný iba z formálneho dôvodu, ak server-side deployment bezpečne opraví rovnakú už distribuovanú binárku a žiadna binárna zmena nie je potrebná.
8. Backend Production deployment MUST byť vykonaný pred finálnym release gate, nie iba plánovaný po App Store publikovaní, ak ho distribuovaná funkcia potrebuje okamžite.
9. Ak má backend Development a Production odlišné identifikátory/tokenty, ich oddelenie od stabilnej lokálnej identity sa riadi IJAS-0027 / `STD-DATA-005`.

## Rozsah
Kontrakt je backend-agnostic. CloudKit je aktuálny dôkaz, ale rovnaké pravidlo platí pre budúci REST/backend, Firebase, Supabase, vlastný server alebo iné prostredie s oddelenou Production konfiguráciou.

Do spoločného Standardu patrí:
- Production resource/config readiness,
- environment parity audit,
- real distributed-build smoke,
- local-safe failure behavior,
- evidence server-side vs binary fix.

Produktové zostáva:
- konkrétny backend provider,
- konkrétne názvy record types/tables/indexov,
- konkrétny deployment mechanizmus.

## Automatická kontrola
Čiastočne:
- static capability flag `hasEnvironmentSpecificBackend`,
- deployment/config manifest comparison, ak backend poskytuje export,
- test/CI assertion na required resource names,
- runtime integration smoke v TestFlight/Production,
- release checklist s explicitným Production evidence.

## Rozhodnutie
**Výsledok:** accepted pre 1.8.0 RC1  
**Odôvodnenie:** reálny Production blocker Peňaženky nebol binárnou chybou a odhalil medzeru medzi Development úspechom a distribuovanou Production pripravenosťou.  
**Schválená verzia:** 1.8.0 RC1
