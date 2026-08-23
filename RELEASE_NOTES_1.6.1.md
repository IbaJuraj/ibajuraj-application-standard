# IbaJuraj Application Standard 1.6.1

**Dátum vydania:** 19. august 2026
**Typ:** PATCH
**Kompatibilita:** spätne kompatibilná; bez migrácie doménových používateľských dát

## Prečo táto verzia vznikla

Verzia 1.6.1 kodifikuje opakované nálezy z whole-app runtime auditov. Cieľom je zabrániť situáciám, keď statické testy prejdú, ale používateľský flow zostane nekonzistentný: hardcoded build pri kompatibilite dát, swipe-back iba na niektorých routach, slepé výsledky vyhľadávania, odlišné neutrálne root pozadia, trvalé `NOVÉ` badge alebo právny/technický detail pred používateľskou odpoveďou.

## Hlavné zmeny

- jeden runtime source of truth pre verziu, build a kompatibilitné metadata,
- globálna navigačná politika Back + native edge swipe-back,
- outcome-first / practical-first detail hierarchy,
- pinned section headers a collapsing title pre dlhé katalógy,
- semantic root background bez lokálnych gray/opacity náhrad,
- semantic/relative Dynamic Type pre bežný text,
- explicitný lifecycle dočasných badge,
- časové vstupy obmedzené na reálne overené dátové pokrytie,
- navigačné mosty vo vyhľadávaní a answer flows,
- completeness audit všetkých publikovaných položiek,
- behaviorálne regresné testy pre kritické routy,
- zákaz interných technických/auditných poznámok v produkčnom UI.

## Adopcia

Aplikácia môže prejsť na 1.6.1 bez migrácie používateľských dát. Pri Level 3/4 má vykonať nový Whole-App Integrity Gate a uložiť runtime dôkazy pre navigáciu, metadata, katalógové completeness a relevantné dátové časovanie.
