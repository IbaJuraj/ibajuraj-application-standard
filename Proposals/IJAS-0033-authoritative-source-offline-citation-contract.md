# IJAS-0033 – Authoritative Source Offline Citation Contract

**Stav:** accepted  
**Navrhovateľ:** IbaJuraj  
**Dátum:** 2026-09-17  
**Dotknuté aplikácie:** Lex Drive; všetky budúce aplikácie, ktoré používajú právne, regulačné alebo iné autoritatívne zdroje ako súčasť používateľského výsledku  
**Navrhovaná verzia štandardu:** 1.9.0 RC1

## Problém

Ak aplikácia odvodzuje používateľský výsledok z právneho, regulačného alebo iného autoritatívneho zdroja, používateľ nesmie byť odkázaný iba na externý webový odkaz. Slabý alebo nulový internetový signál nesmie znemožniť zobrazenie zdroja, z ktorého aplikácia vychádza.

Pri právnom obsahu zároveň nestačí zobrazovať iba používateľský názov skutku alebo výsledku. Používateľ musí vedieť, ktoré konkrétne ustanovenie tvorí porušenú povinnosť, kvalifikáciu, prípadnú závažnostnú vrstvu alebo sankčný základ, a musí mať dostupné presné znenie použitej verzie.

## Dôkazy a príklady

Lex Drive Build 232 ukázal praktický problém pri priestupku „Nedodržanie bezpečnej vzdialenosti“. Aplikácia mala v dátach právny reťazec § 17 ods. 1 zákona č. 8/2009 Z. z. → § 22 ods. 1 písm. l) zákona č. 372/1990 Zb., ale používateľské zobrazenie neukazovalo porušenú povinnosť rovnako jasne ako pri starších skutkoch. Zároveň sa potvrdila požiadavka, aby doslovná citácia bola dostupná aj bez pripojenia na Slov-Lex.

## Navrhované pravidlo

### STD-AUTH-SOURCE-001 — Authoritative source is available offline and externally traceable

Ak aplikácia používa právny, regulačný, normatívny alebo iný autoritatívny zdroj ako súčasť funkčného používateľského výsledku:

- MUSÍ lokálne sprístupniť použitú reprezentáciu zdroja bez závislosti od internetového pripojenia,
- MUSÍ jasne identifikovať zdroj a konkrétnu použitú časovú/verznú identitu,
- MUSÍ pri právnom alebo obdobne normatívnom obsahu sprístupniť presnú citáciu alebo doslovné znenie ustanovenia, z ktorého výsledok vychádza,
- MUSÍ uviesť účinnosť alebo verziu použitú pri výsledku, ak sa zdroj v čase mení,
- MUSÍ uchovať alebo sprístupniť dátum/verifikačnú stopu overenia, ak aplikácia používa verifikovaný obsah,
- externý oficiálny zdroj MÔŽE byť dostupný ako doplnkový odkaz, ale NESMIE byť jediným spôsobom zobrazenia autoritatívneho podkladu,
- používateľský názov, skrátený opis alebo praktické vysvetlenie NESMIE nahradiť identifikáciu autoritatívneho podkladu.

**Záväznosť:** MUST / MUST NOT podľa jednotlivých bodov vyššie.

## Rozsah

Do spoločného štandardu patrí:
- offline dostupnosť autoritatívneho podkladu,
- identita a verzia/účinnosť zdroja,
- verifikačná stopa,
- zákaz modelu „iba externý odkaz“,
- jasné rozlíšenie používateľského vysvetlenia od autoritatívneho zdroja.

Produktové zostáva:
- konkrétna informačná hierarchia právneho reťazca,
- názvy rolí typu „Porušená povinnosť“, „Závažné porušenie“, „Priestupková kvalifikácia“ alebo „Sankčné ustanovenie“,
- vizuálny komponent, navigácia a spôsob rozbalenia citácie,
- konkrétny externý oficiálny portál (napr. Slov-Lex).

## Migrácia

Existujúca aplikácia musí pri najbližšom plánovanom release:
1. identifikovať výsledky založené na autoritatívnom zdroji,
2. overiť, že použitý zdroj je lokálne dostupný aj offline,
3. odstrániť závislosť na externom webe ako jedinom prístupe k zdroju,
4. doplniť verziu/účinnosť a podľa potreby dátum overenia,
5. pridať regresnú kontrolu, že používateľský výsledok zostáva spätne dohľadateľný na konkrétny autoritatívny podklad.

## Kompatibilita a riziká

Pravidlo je spätne kompatibilné a predstavuje novú spoločnú contract family, preto patrí do MINOR línie podľa Governance. Hlavné riziká sú veľkosť lokálneho balíka, stale verzia zdroja a licenčné obmedzenia pri niektorých ne-právnych zdrojoch. Produkt musí tieto riziká riešiť zdrojovou politikou a temporal/verifikačnými mechanizmami; nesmie ich riešiť tým, že používateľa odkáže iba na externý web.

## Automatická kontrola

Pravidlo je čiastočne strojovo kontrolovateľné. Conformance môže vyžadovať dôkaz pre:
- lokálny/offline source artifact alebo embedded source bundle,
- source/version/effective-date metadata,
- verification timestamp alebo provenance record,
- zákaz external-only source presentation,
- runtime test otvorenia zdroja pri nedostupnej sieti.

## Rozhodnutie

**Výsledok:** accepted  
**Odôvodnenie:** Lex Drive Build 232 preukázal opakovateľnú potrebu oddeliť autoritatívny právny podklad od používateľského vysvetlenia a odstrániť závislosť od internetového pripojenia. Pravidlo je použiteľné aj mimo Lex Drive pre ďalšie aplikácie pracujúce s autoritatívnymi zdrojmi.  
**Schválená verzia:** 1.9.0 RC1
