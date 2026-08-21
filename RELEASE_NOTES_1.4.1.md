# IbaJuraj Application Standard 1.4.1

Patch 1.4.1 uzatvára rozdiely v typografii hlavných pracovných obrazoviek medzi aplikáciami IbaJuraj.

## Hlavná zmena

- `appPage.title`: `.largeTitle.weight(.bold)` s Dynamic Type.
- `appPage.subtitle`: `.subheadline` so sekundárnou sémantickou farbou.
- Medzera title/subtitle: 6 pt.
- Lokálne pevné bodové veľkosti a `minimumScaleFactor` sa pre túto spoločnú rolu nepoužívajú.

## Dopad

Bez migrácie používateľských dát. Aplikácie majú v najbližšom UI builde zosúladiť hlavné root headre a vykonať side-by-side runtime audit.
