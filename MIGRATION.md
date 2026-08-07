# Migrácia IbaJuraj Application Standard

## 1.0.0 → 1.1.0

Verzia 1.1.0 je spätne kompatibilná minor aktualizácia. Samotné prijatie štandardu nevyžaduje migráciu používateľských dát.

Aplikácia pri adopcii 1.1.0 skontroluje:

1. pomenovanie a umiestnenie spoločných položiek Nastavení,
2. zbytočné medziobrazovky pri jednoduchých voľbách,
3. návrat späť a systémový swipe-back na bežných vnorených obrazovkách,
4. používanie modálnych akcií iba pri skutočných modálnych workflow,
5. spoločný spôsob schovania klávesnice,
6. priamy Kontakt a podporu,
7. pri lokálnom zámku biometriu, PIN, autolock a lifecycle správanie,
8. Dynamic Type a pravé stavové hodnoty v Nastaveniach,
9. lokálny `APP_STANDARD_ADOPTION.md` a verziu lokálnej kópie štandardu.

Každá aplikácia prijíma verziu 1.1.0 samostatným auditovaným buildom; publikovanie centrálneho štandardu samo osebe nemení používanú verziu v aplikácii.

---

## Historická migrácia autoritatívneho zdroja z `ibajuraj.github.io/standard`

### Cieľ

Jediný autoritatívny zdroj IbaJuraj Application Standardu je:

```text
https://github.com/IbaJuraj/ibajuraj-application-standard
```

### Bezpečné poradie

1. Vytvoriť a naplniť nový repozitár.
2. Overiť GitHub Action.
3. Vytvoriť tag a Release konkrétnej verzie.
4. Až potom upraviť `ibajuraj.github.io`.
5. V starom priečinku `standard/` nenechať druhú nezávislú autoritatívnu kópiu.
6. Nahradiť ju krátkym oznámením a odkazom na nový repozitár, prípadne ju udržiavať iba ako automaticky generované zrkadlo.
7. Následne aktualizovať odkazy a adopčné súbory v aplikáciách.

### Dôležité pravidlo

Obsah štandardu sa po migrácii upravuje iba v tomto repozitári. Web IbaJuraj Apps môže štandard prezentovať alebo naň odkazovať, ale nesmie sa stať druhým zdrojom pravdy.
