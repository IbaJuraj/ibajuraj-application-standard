# IJAS-0027 – Single-Device Development/Release Data Continuity

**Stav:** proposed
**Navrhovateľ:** IbaJuraj Apps
**Dátum:** 2026-09-04
**Dotknuté aplikácie:** Peňaženka Kariet, Strážca Termínov a všetky budúce IbaJuraj aplikácie, ktoré uchovávajú používateľské dáta alebo používajú cloudovú synchronizáciu/zdieľanie
**Navrhovaná verzia štandardu:** 1.7.1

## Problém

Vývoj a produkčné overovanie IbaJuraj aplikácií sa môže vykonávať na jednom fyzickom iPhone. Na tom istom zariadení sa preto opakovane strieda vývojový build nainštalovaný z Xcode a distribuovaný build z App Store alebo TestFlight.

Používateľské dáta musia zostať použiteľné aj po tomto prechode. CloudKit Development a Production sú však oddelené prostredia. Ak je lokálny dátový model alebo identita používateľských objektov príliš pevne naviazaná na environment-specific CloudKit recordy, share identifikátory alebo pozývacie tokeny, prechod Xcode → App Store → Xcode môže viesť k nefunkčnému zdieľaniu, falošnému chýbajúcemu objektu, prepísaniu dát alebo požiadavke znovu vytvoriť lokálny obsah.

## Dôkazy a príklady

- **Peňaženka Kariet v1.5.2 / Build 72:** lokálne uložené karty a existujúca peňaženka zostali na jednom iPhone dostupné po prechode medzi Xcode a App Store buildom, ale vytvorenie/obnovenie zdieľania v App Store produkčnom prostredí zlyhalo. To ukazuje potrebu oddeliť stabilnú lokálnu identitu peňaženky od cloudovej reprezentácie zdieľania konkrétneho prostredia.
- **Strážca Termínov:** person-first sharing a CloudKit membership model musí byť testovateľný rovnakým jedným zariadením bez straty osôb, vozidiel, dokumentov, termínov alebo iných lokálnych dát pri striedaní Xcode a distribuovaného buildu.
- Rovnaká potreba vznikne v každej budúcej IbaJuraj aplikácii, ktorá bude mať lokálny dátový model a zároveň Development/Production cloudové prostredie.

## Navrhované pravidlo

Aplikácia, ktorá uchováva používateľské dáta a môže sa počas vývoja striedavo inštalovať z Xcode a z App Store/TestFlight na tom istom zariadení, **MUST** zachovať lokálne používateľské dáta a ich stabilnú identitu nezávisle od aktuálneho cloudového prostredia, pokiaľ používateľ aplikáciu alebo dáta výslovne nevymaže.

Cloudové väzby, record IDs, share IDs, invitation tokens, environment markers a podobná transportná metadata **MUST** byť oddelené od stabilnej lokálnej identity doménových objektov.

Pri zmene medzi Development a Production cloudovým prostredím aplikácia:

1. **MUST NOT** vymazať, zneplatniť alebo znovu vytvoriť lokálny doménový objekt iba preto, že jeho cloudová reprezentácia v aktuálnom prostredí neexistuje.
2. **MUST** zachovať stabilné lokálne ID objektu a jeho obsah.
3. **MUST** vedieť vytvoriť alebo znovu naviazať cloudovú reprezentáciu pre aktuálne prostredie bez požiadavky znovu zadávať používateľské dáta.
4. **MUST NOT** považovať Development a Production cloudové identifikátory za navzájom zameniteľné.
5. **SHOULD** používateľovi zobraziť zrozumiteľný stav, ak lokálny objekt existuje, ale cloudová väzba pre aktuálne prostredie ešte nie je vytvorená alebo potrebuje obnovu.
6. **MAY** vyžadovať nový environment-specific pozývací kód alebo share token; zmena tokenu nesmie meniť alebo poškodiť samotný lokálny objekt.
7. **MUST** zachovať lokálne dáta pri bežnom in-place prechode Xcode → App Store/TestFlight → Xcode na rovnakom zariadení, pokiaľ operačný systém zachová aplikačný kontajner a používateľ aplikáciu výslovne neodstráni.

**Záväznosť:** MUST / MUST NOT / SHOULD / MAY podľa jednotlivých bodov vyššie.

## Rozsah

Do spoločného štandardu patrí:

- oddelenie stabilnej lokálnej doménovej identity od cloudovej/transportnej identity,
- bezpečné správanie pri zmene Development ↔ Production,
- zákaz deštruktívnej interpretácie „remote object missing“ pri environment mismatch,
- povinnosť jedným zariadením overiť zachovanie dát medzi vývojovým a distribuovaným buildom,
- dokumentovanie environment-specific share/invitation správania.

Produktové zostáva:

- konkrétny formát lokálnych ID,
- konkrétne CloudKit record types a zones,
- konkrétny UI wording obnovy cloudovej väzby,
- či aplikácia používa CloudKit, iný backend alebo iba lokálne dáta.

## Migrácia

### Peňaženka Kariet

- potvrdiť, že Card a SharedWallet používajú stabilné lokálne ID nezávislé od CloudKit Development/Production,
- oddeliť environment-specific sharing metadata od identity a obsahu peňaženky,
- pri existujúcej lokálnej peňaženke umožniť vytvoriť/obnoviť Production share bez znovuvytvorenia peňaženky alebo kariet,
- zabezpečiť, že návrat do Xcode prostredia nepoškodí Production väzbu ani lokálny obsah.

### Strážca Termínov

- aplikovať rovnaký kontrakt na osoby, vozidlá, súbory vozidiel, dokumenty, termíny, membership a sharing metadata,
- overiť, že zmena Development/Production nemôže zmazať alebo duplikovať doménové objekty,
- person-first priradenia musia zostať lokálne stabilné aj bez dostupnej cloudovej väzby aktuálneho prostredia.

### Budúce aplikácie

Tento kontrakt sa musí posúdiť už pri návrhu persistence/sync architektúry, nie až pred App Store release.

## Kompatibilita a riziká

Pravidlo je spätne kompatibilné pre aplikácie bez cloudového backendu; tie iba overia lokálnu kontinuitu dát.

Pri existujúcich aplikáciách môže byť potrebná migrácia, ak lokálne objekty používajú cloudové ID ako jedinú identitu. Migrácia musí uprednostniť zachovanie dát a nesmie vytvárať duplicity.

Pravidlo negarantuje zachovanie dát po výslovnom odstránení aplikácie používateľom ani pri resetovaní zariadenia. Rovnako neznamená, že Development invitation/share token musí fungovať v Production; požaduje iba, aby táto environment-specific zmena nepoškodila doménové dáta.

## Automatická kontrola

Čiastočne.

Možné automatické kontroly:

- unit test, že doménové ID sa nemení pri zmene environment bindingu,
- unit test, že odstránenie/absencia environment-specific CloudKit metadata neodstráni doménový objekt,
- migration test Development binding → Production binding → Development binding,
- schema/static test, že environment marker a remote IDs sú samostatné polia od stabilného local ID.

Povinný manuálny runtime gate pre aplikácie s persistentnými dátami:

1. na jednom fyzickom zariadení vytvoriť reálne používateľské dáta,
2. spustiť Xcode build a overiť dáta,
3. bez vymazania aplikácie prejsť na App Store/TestFlight build a overiť tie isté dáta,
4. overiť sync/sharing správanie v Production,
5. znovu prejsť na Xcode build a overiť zachovanie lokálnych dát,
6. zaznamenať, ktoré cloudové väzby sú environment-specific a ktoré boli úspešne obnovené/rebindnuté.

Ak test vyžaduje druhého používateľa, prijatie pozvánky druhým Apple účtom môže zostať samostatným multi-user gate; nemožnosť mať druhé fyzické zariadenie nesmie blokovať overenie základnej single-device data continuity.

## Rozhodnutie

Vyplní sa po posúdení.

**Výsledok:**
**Odôvodnenie:**
**Schválená verzia:**
