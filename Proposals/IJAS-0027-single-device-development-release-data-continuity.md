# IJAS-0027 – Single-Device Development/Release Data Continuity

**Stav:** accepted  
**Navrhovateľ:** IbaJuraj Apps  
**Dátum:** 2026-09-04  
**Rozšírené:** 2026-09-05  
**Dotknuté aplikácie:** Peňaženka Kariet, Strážca Termínov a všetky budúce IbaJuraj aplikácie s persistentnými dátami a environment-specific backendom  
**Schválená candidate verzia štandardu:** 1.8.0 RC1

## Problém
Vývoj a produkčné overovanie IbaJuraj aplikácií sa môže vykonávať na jednom fyzickom iPhone. Na tom istom zariadení sa opakovane strieda Xcode Development build a distribuovaný TestFlight/App Store build. CloudKit Development a Production sú oddelené prostredia; podobný problém môže mať aj iný backend.

Ak je lokálny dátový model príliš pevne naviazaný na environment-specific record/share/token identity, prechod medzi prostrediami môže viesť k nefunkčnému zdieľaniu, falošnému chýbajúcemu objektu, duplikácii alebo prepísaniu dát.

## Dôkaz
Peňaženka Kariet v1.5.2 / Build 72 zachovala lokálne karty a peňaženku pri prechode Xcode ↔ distribuovaný build, ale Production sharing nevedel obnoviť cloudovú väzbu. Neskoršia vetva oddelila stabilnú lokálnu identitu od environment-specific cloud bindingu a single-device continuity prešla bez straty 32 kariet.

Strážca Termínov používa person-first sharing a potrebuje rovnaký kontrakt pre osoby, vozidlá, súbory vozidiel, dokumenty, termíny a membership/sharing metadata.

## Schválený kontrakt
Aplikácia s persistentnými dátami a environment-specific backendom MUST zachovať lokálne používateľské dáta a ich stabilnú identitu nezávisle od aktuálneho backend prostredia, pokiaľ používateľ aplikáciu alebo dáta výslovne nevymaže.

Cloudové/backend väzby, record IDs, share IDs, invitation tokens, environment markers a podobná transportná metadata MUST byť oddelené od stabilnej lokálnej identity doménových objektov.

Pri zmene Development ↔ Production aplikácia:
1. MUST NOT vymazať, zneplatniť alebo znovu vytvoriť lokálny doménový objekt iba preto, že remote reprezentácia v aktuálnom prostredí neexistuje.
2. MUST zachovať stabilné lokálne ID a obsah objektu.
3. MUST vedieť vytvoriť alebo znovu naviazať backend reprezentáciu pre aktuálne prostredie bez opätovného zadávania doménových dát.
4. MUST NOT považovať Development a Production identifikátory za navzájom zameniteľné.
5. SHOULD zobraziť zrozumiteľný stav, ak lokálny objekt existuje, ale backend väzba aktuálneho prostredia ešte nie je vytvorená alebo potrebuje obnovu.
6. MAY vyžadovať nový environment-specific invitation/share token; zmena tokenu nesmie meniť samotný lokálny objekt.
7. MUST zachovať lokálne dáta pri bežnom in-place prechode Xcode → TestFlight/App Store → Xcode, ak operačný systém zachová aplikačný kontajner.

## Runtime gate
Preferovaný test používa **ten istý marketing version/build** v Xcode a TestFlight, ak je to prakticky možné, aby sa environment switch neplietol s verziovou migráciou.

1. vytvoriť reálne používateľské dáta,
2. spustiť Xcode/Development a overiť dáta,
3. bez vymazania aplikácie prejsť na TestFlight/App Store,
4. overiť tie isté lokálne dáta a stabilné ID,
5. overiť Production sync/sharing podľa capability,
6. znovu prejsť na Xcode/Development,
7. potvrdiť zachovanie lokálnych dát a zdokumentovať oddelené environment bindings.

Ak je potrebný druhý používateľ, multi-user acceptance môže zostať samostatný gate; single-device data continuity sa musí dať overiť aj bez druhého zariadenia.

## Migrácia
### Peňaženka Kariet
- stabilné Card/Wallet IDs nezávislé od Development/Production bindings,
- environment-specific sharing metadata oddelené od obsahu,
- Production share recreatable bez znovuvytvorenia peňaženky alebo kariet.

### Strážca Termínov
- rovnaký kontrakt pre Person/Vehicle/VehicleSet/Document/Deadline,
- membership/share/invitation identity oddelená od lokálnej identity,
- environment mismatch nesmie mazať ani duplikovať doménové objekty.

## Rozhodnutie
**Výsledok:** accepted pre 1.8.0 RC1  
**Odôvodnenie:** potvrdený reálny cross-environment problém v Peňaženke a priamy dopad na Strážcu.  
**Schválená verzia:** 1.8.0 RC1
