# IbaJuraj Application Standard 1.6.0 – Final Amendment

**Status:** Final, normative  
**Date:** 2026-08-17

## 1. Authority and precedence

This file is a normative part of the final **IbaJuraj Application Standard 1.6.0** release. It incorporates all rules from `IBAJURAJ_APPLICATION_STANDARD.md` and only supersedes the clauses explicitly changed below. If this amendment conflicts with the base 1.6.0 text, **this amendment prevails**.

The purpose of the amendment is to capture the final RC2/RC3 runtime decisions validated before release without rewriting unrelated, already validated sections of the Standard.

## 2. Settings entry on every primary root

The following final rule supersedes the permissive wording in section **6.3.1 Spoločný vstup do Nastavení**:

- Nastavenia MUST byť dostupné cez tlačidlo so symbolom `gearshape.fill` vpravo hore na **každom primárnom roote produktu, ktorý má vlastnú root hlavičku**.
- Používateľ MUST NOT byť nútený prepnúť na iný primárny tab alebo root iba preto, aby otvoril systémové Nastavenia.
- Ak konkrétny primárny root objektívne nemôže bezpečne niesť header action bez porušenia čitateľnosti alebo hlavnej úlohy, produkt MAY použiť zdokumentovanú jednorazovú výnimku a ekvivalentný priamy vstup. Výnimka MUST NOT skryť Nastavenia do sekundárneho obsahu.
- Spodná navigácia MUST NOT obsahovať samostatný tab systémových Nastavení.
- Nastavenia zostávajú samostatnou push obrazovkou so systémovým návratom a swipe-back správaním.

## 3. Shared primary-root header contract

The following rules extend sections **6.3.2** and the shared root-page typography/layout contract:

- Primárne root obrazovky jednej aplikácie MUST používať spoločnú vertikálnu baseline hlavného root titulku a spoločný top inset voči safe area.
- Pri prepínaní medzi primárnymi rootmi MUST NOT vzniknúť viditeľné vertikálne „skákanie“ titulku alebo pravej systémovej header akcie.
- Akcia Nastavení MUST zostať pravou krajnou systémovou akciou hlavičky na každom primárnom roote, na ktorom sa zobrazuje.
- Root title, subtitle a trailing system action MUST používať spoločnú geometriu komponentu; produktový obsah MAY byť odlišný.
- Dynamic Type a dlhšia lokalizácia MUST NOT spôsobiť kolíziu titulku so systémovou header akciou.

Semantic design-token roles introduced for this contract:

- `appPage.rootTitleTopInset` – spoločný vertikálny inset root titulku od bezpečnej hornej oblasti,
- `appPage.rootHeaderBaseline` – spoločná baseline pre root title/header kompozíciu,
- existujúce `header.action.*` tokeny zostávajú autoritatívne pre trailing system action.

Implementácia MAY mapovať tieto semantic roles na platformové alebo produktové hodnoty, ale rovnaká aplikácia MUST použiť rovnakú výslednú geometriu na všetkých svojich primárnych rootoch.

## 4. Overlay and floating-action safety

- Floating, overlay alebo plávajúca primárna akcia MUST NOT prekrývať obsah, trailing chevron, posledný interaktívny riadok, tab bar ani povinnú safe area.
- Scrollovateľný obsah MUST mať dostatočný bottom/trailing inset, aby všetky riadky zostali plne čitateľné a dotykovo dostupné aj pri zobrazenom FAB/overlay prvku.
- Overlay MUST NOT zmenšovať efektívnu dotykovú plochu susedného interaktívneho prvku pod 44 × 44 bodov.

## 5. State terminology and human-readable values

- Rovnaký doménový stav MUST používať konzistentnú používateľskú terminológiu na roote, v zozname aj detaile.
- Technická reprezentácia hodnoty MUST NOT presakovať do používateľského textu, ak existuje prirodzenejšie stavové znenie. Napríklad technické `-7 dní` SHOULD byť prezentované ako `7 dní po termíne` alebo ekvivalentný prirodzený text podľa lokalizácie.
- Text stavu a CTA MUST NOT vytvárať protichodný význam, napríklad prázdna agenda nesmie ponúkať „doplniť dátum“ pre neexistujúcu položku; má ponúknuť vytvorenie relevantného objektu.

## 6. Critical cards and direct actions

- Ak kritická alebo prioritná karta jednoznačne reprezentuje jeden konkrétny objekt, primárne CTA SHOULD otvoriť priamo tento objekt alebo jeho bezprostredný riešiaci krok.
- Všeobecný zoznam MAY zostať sekundárnou navigáciou, ale SHOULD NOT nahradiť priamu akciu, ak je cieľ jednoznačný.
- Kritický alebo varovný surface MUST NOT obsahovať pozitívny greeting alebo iný text, ktorý tónom odporuje zobrazovanému problému.

## 7. Compact summary contract

The final 1.6.0 release confirms the compact-detail rule introduced during RC validation:

- Súhrnné bloky typu **Na prvý pohľad** MUST byť proporcionálne k informačnej hodnote a MUST NOT neprimerane vytláčať hlavnú úlohu detailu z prvého viewportu.
- Opakované metriky SHOULD používať kompaktnú shared summary geometriu namiesto samostatných vysokých kariet, ak tým neutrpí čitateľnosť alebo prístupnosť.
- Dynamic Type MUST zostať plne podporovaný; kompaktnosť MUST NOT byť dosiahnutá zmenšovaním textu pod podporovanú typografickú rolu.

## 8. About metadata contract

The final 1.6.0 release confirms:

- používateľská verzia aplikácie SHOULD zobrazovať marketingovú verziu + build,
- položka **IbaJuraj Application Standard** v bežnom UI MUST zobrazovať iba `Verzia X.Y.Z`,
- interný tag, adoption level, runtime gate a audit stav MUST zostať mimo bežného používateľského About UI.

## 9. Runtime evidence

Final RC3 alignment was runtime-verified on **Strážca Termínov v1.55 Build 78**, including the shared root-title/header baseline on the primary roots and direct Settings availability pattern.
