# Audit RC2 → RC3

RC3 je malý hardening nad RC2, vyvolaný whole-app viewport auditom Peňaženky Kariet Build 54.

## Nové povinné kontrakty
- `STD-HEADER-001`: jeden autoritatívny header owner na obrazovku.
- `STD-HEADER-002`: navigation title sa nesmie duplikovať ekvivalentným page/section headingom.
- `STD-HEADER-003`: sheet má jednu koherentnú title/subtitle/dismissal hierarchiu.
- `STD-CHROME-001`: zákaz imitácie platform-owned system chrome.

## Praktické príklady
- `Kontakt` + `KONTAKT` → odstrániť duplicitný section label.
- `O aplikácii` + `O APLIKÁCII` → odstrániť duplicitný section label.
- toolbar len s `X` + druhý veľký `Pridať kartu` pod ním → zjednotiť do jedného sheet headeru.
- vlastná dekoratívna kapsula imitujúca Home Indicator → odstrániť.

RC3 nemení stabilnú verejnú autoritu 1.6.4 ani marketingovú verziu pripravovaného Standardu 1.7.0.
