# IJAS-0009 – Neutral Surface & Text Color Contract

**Status:** accepted  
**Target:** Standard 1.5.1  
**Date:** 2026-08-13

## Problém

Runtime porovnanie aplikácií IbaJuraj ukázalo rozdielne neutrálne Light/Dark pozadia, card/tile surfaces a intenzitu textov. Takéto rozdiely oslabujú rodinnú identitu aj napriek zhodnej geometrii komponentov.

## Rozhodnutie

Zaviesť povinné semantic roly pre app background, card/tile surface, primary/secondary text, separator a disabled state. Rovnaká rola musí mať rovnaký vizuálny výsledok naprieč aplikáciami.

Preferované mapovanie používa systémové semantic colors. Produktové accent/status/brand surfaces sú povolené iba ako významová alebo brand vrstva, nie ako náhrada základnej neutrálnej hierarchie.

## Runtime dôkaz

Adopcia vyžaduje screenshot parity audit Light aj Dark Mode. Odchýlky musia byť odstránené alebo evidované ako Standard Exception.

## Kompatibilita

Patch zmena bez dátovej migrácie.
