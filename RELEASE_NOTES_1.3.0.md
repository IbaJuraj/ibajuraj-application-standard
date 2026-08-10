# IbaJuraj Application Standard 1.3.0

Spätne kompatibilná minor aktualizácia spoločného autoritatívneho štandardu aplikácií IbaJuraj.

## Hlavné zmeny

- jednotná hlavička s preferovaným 42 pt vizuálom akcie, minimálnou 44 pt hit area a Nastaveniami ako pravou krajnou akciou,
- potvrdený vstup do Nastavení vpravo hore na hlavnej úvodnej obrazovke bez povinnosti opakovať ho v každom tabe,
- priamy segmented Vzhľad **Automaticky / Svetlý / Tmavý** v root Nastavení,
- predvídateľné poradie spoločných sekcií a posledná sekcia **Pomoc a informácie**,
- kompaktný Kontakt s formulárom, Telegramom, produktovým vysvetlením a upozornením na citlivé údaje,
- kontaktná URL zmluva pre predvyplnenie aplikácie a typu podnetu na webe,
- pravdivá obrazovka O aplikácii s jedným runtime zdrojom verzie, buildu, tagu a adopcie,
- povinná push navigácia bežných obrazoviek so šípkou aj swipe-back gestom,
- responzívne trailing hodnoty bez zmenšovania textu a layout podľa skutočnej dostupnej šírky,
- zachované sémantické varianty dlaždíc vrátane produktových Wallet Card a Calculator Key,
- privacy manifest kontrola každého distribuovaného targetu,
- silnejšie adopčné dôkazy, testovacia matica a release checklist.

## Kompatibilita

Existujúci 48 pt settings entry variant z 1.2.0 zostáva platný. Nový preferovaný vizuálny priemer 42 pt je súčasťou povoleného rozsahu 42–48 pt, preto aplikácie môžu migrovať postupne bez nekompatibilnej zmeny.

Verzia 1.3.0 nemení používateľské dátové modely. Aplikácie musia vykonať UX, navigačný, metadata, privacy a runtime audit podľa `MIGRATION.md`.

## Adopcia

Aplikácie majú používať konkrétny tag `standard-v1.3.0`, aktualizovať `APP_STANDARD_ADOPTION.md` a deklarovať iba presný názov úrovne adopcie. Level 3 a Level 4 vyžadujú uložené automatické aj manuálne release dôkazy.
