# Migrácia z `ibajuraj.github.io/standard`

## Cieľ

Presunúť jediný autoritatívny zdroj IbaJuraj Application Standardu z webového repozitára do:

```text
https://github.com/IbaJuraj/ibajuraj-application-standard
```

## Bezpečné poradie

1. Vytvoriť a naplniť nový repozitár.
2. Overiť GitHub Action.
3. Vytvoriť tag a Release `standard-v1.0.0`.
4. Až potom upraviť `ibajuraj.github.io`.
5. V starom priečinku `standard/` nenechať druhú nezávislú autoritatívnu kópiu.
6. Nahradiť ju krátkym oznámením a odkazom na nový repozitár, prípadne ju udržiavať iba ako automaticky generované zrkadlo.
7. Následne aktualizovať odkazy a adopčné súbory v aplikáciách.

## Dôležité pravidlo

Obsah štandardu sa po migrácii upravuje iba v novom repozitári. Web IbaJuraj Apps môže štandard prezentovať alebo naň odkazovať, ale nesmie sa stať druhým zdrojom pravdy.
