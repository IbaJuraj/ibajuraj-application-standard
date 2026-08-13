# IbaJuraj – podpora a verejné odkazy

**Stav:** autoritatívny register  
**Verzia:** 1.5.1

## Verejné adresy

| Účel | Adresa |
|---|---|
| Web IbaJuraj | https://ibajuraj.github.io/ |
| Kontaktný formulár | https://ibajuraj.github.io/#support |
| Ochrana súkromia | https://ibajuraj.github.io/privacy.html |
| Telegram komunita | https://t.me/+mEtAJXPMUF9mZjI0 |

## Kontaktná URL zmluva

Aplikácia SHOULD otvoriť kontaktný formulár v tvare:

```text
https://ibajuraj.github.io/?app=<app-id>&type=<type>&subject=<subject>#support
```

Povolené parametre:

| Parameter | Povinnosť | Význam |
|---|---|---|
| `app` | SHOULD | stabilný verejný identifikátor aplikácie z povoleného zoznamu webu |
| `type` | MAY | kategória podnetu z povoleného zoznamu webu |
| `subject` | MAY | stručný používateľsky čitateľný predmet; musí byť URL-encoded |
| `#support` | SHOULD | presun na kontaktnú sekciu |

- Aplikácia MUST zostaviť adresu cez bezpečné URL komponenty, nie spájaním neovereného používateľského vstupu.
- Web MUST validovať `app` a `type` proti povoleným hodnotám, MUST ignorovať neznáme hodnoty a MUST zachovať bezpečné predvolené hodnoty.
- Web SHOULD predvyplniť aplikáciu a typ podnetu a SHOULD presunúť fokus na prvé pole, ktoré používateľ musí doplniť.
- Predvyplnenie MUST NOT automaticky odoslať formulár.
- Verzia, build a diagnostické údaje MAY byť pridané iba vtedy, keď sú používateľovi pred odoslaním viditeľné.

## Pravidlá použitia

- Aplikácia MUST ponúknuť položku **Kontakt**, ktorá otvorí kontaktnú obrazovku s formulárom.
- Aplikácia SHOULD ponúknuť samostatné tlačidlo **Telegram komunita**.
- Telegram MUST NOT byť jediným kanálom podpory a MUST NOT sa používať na osobné, zdravotné, právne, identifikačné alebo iné citlivé údaje.
- Bežný používateľ SHOULD NOT byť posielaný priamo do GitHub Issues.
- GitHub môže byť technickým základom webu a internou evidenciou potvrdených chýb.
- Technické údaje pridané ku kontaktnej správe MUST byť používateľovi zobrazené pred odoslaním.
- Odkazy SHOULD NOT byť duplikované v jednotlivých obrazovkách; cieľom je spoločný `IJSupportLinks` alebo ekvivalentný jeden zdroj pravdy.
- Ak formulár nemožno otvoriť, aplikácia MUST zobraziť zrozumiteľnú chybu a SHOULD ponúknuť Telegram alebo inú bezpečnú alternatívu.
