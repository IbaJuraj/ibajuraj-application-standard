# IJAS-0034 – Release Communication and Store Metadata

**Stav:** accepted  
**Navrhovateľ:** IbaJuraj  
**Dotknuté aplikácie:** všetky IbaJuraj Apps; pilot Strážca Termínov  
**Navrhovaná verzia štandardu:** 1.9.0 RC1

## Problém

Duplicitné ručné texty pre App Store, web a Telegram vedú k rozdielnym údajom a príliš dlhým novinkám na mobilných obrazovkách.

## Navrhované pravidlo — STD-RELEASE-COMMS-001

- Verejné produktové informácie MUSIA vychádzať zo zverejnených údajov App Store; web nesmie zamieňať plánované funkcie za vydané.
- Description opisuje hlavné funkcie aplikácie, What's New iba skutočné zmeny vydanej verzie. Texty sa pripravujú v skutočne podporovaných lokalizáciách; nevytvára sa fiktívna jazyková verzia.
- Odporúčané rozsahy (SHOULD): Promotional Text 80–150 znakov; Description 300–500 znakov; What's New 150–350 znakov, 3–6 stručných bodov, každý približne do 60 znakov. Pri odchýlke má prednosť presnosť a čitateľnosť. Limity Apple sú samostatná podmienka.
- Web používa Description, číslo verzie, What's New a dostupné údaje vydania; Promotional Text a Keywords zostávajú určené pre App Store.
- Ak je zapnuté Telegram publikovanie, správa MUSÍ obsahovať iba názov aplikácie, číslo vydanej verzie a pôvodný What's New; bez reklamného dodatku, AI prepisu, screenshotov či odkazov.
- Verejné publikovanie MUSÍ byť explicitne povolené pre konkrétnu aplikáciu, nesmie spätne publikovať existujúce vydania a MUSÍ chrániť pred opakovaným odoslaním.
- Nejasný stav doručenia MUSÍ zastaviť automatické opakovanie až do overenia; chyba Telegramu nesmie zrušiť úspešné publikovanie webu.
- Publikačný News bot MUSÍ byť oddelený od súkromného Reports bota; tokeny sa ukladajú mimo verejného kódu a bot má len potrebné oprávnenia.

## Odkazy a umiestnenie v aplikácii

- Obrazovka **Kontakt** zachová kontaktný formulár a existujúcu Telegram komunitu pre otázky, návrhy a diskusiu. Odkaz na komunitu sa nesmie zameniť za jednosmerný kanál noviniek.
- Obrazovka **O aplikácii** má pri adopcii kontraktu obsahovať samostatný externý odkaz **Novinky na Telegrame**, s doplnkovým textom „Nové verzie a aktualizácie aplikácií“. Odporúčané umiestnenie: medzi Web IbaJuraj Apps a Ochrana súkromia. Použiť existujúci komponent externého odkazu, vzhľad a prístupnosť aplikácie.
- Cieľ: `https://t.me/IbaJurajAppsNews`. Odkaz sa centralizuje v konfigurácii identity/odkazov aplikácie, nie v jednotlivých views. Otvorenie musí fungovať aj bez nainštalovaného Telegramu cez systémový HTTPS odkaz.
- Samotný odkaz nevyžaduje Telegram SDK, token, nové oprávnenia ani integráciu bota v klientovi. News automatizácia zostáva serverová (App Store → GitHub Actions → Telegram).
- Verejné novinky, komunitná diskusia, kontaktný formulár a súkromné Reports hlásenia zostávajú účelovo oddelené. Žiadne citlivé údaje v komunite alebo novinkách.
- Pilot UI: Strážca Termínov pri najbližšej vhodnej revízii pred vydaním, ak je ešte otvorená; inak pri ďalšom plánovanom vydaní. Nevytvárať samostatný build iba kvôli odkazu. Ostatné aplikácie až po samostatnom schválení.
- Overenie: správny cieľ odkazu, otvorenie s Telegramom aj bez neho, nezmenený kontakt a súkromie, čitateľnosť a prístupnosť v podporovaných režimoch. Verzia štandardu zobrazená v aplikácii zostáva skutočne adoptovaná stabilná verzia, nie plánovaná RC.

## Migrácia a overenie

Pilot: Strážca Termínov, slovenský text. Ďalšie aplikácie až po samostatnom schválení pri najbližšom plánovanom vydaní. Žiadne vynútené nové buildy iba kvôli textu.

Dôkazy: kontrola textov oproti vydaným funkciám, porovnanie webu so zverejnenou verziou, offline regresné testy výberu aplikácie/verzie a duplicít, súkromný test doručenia, následne potvrdenie prvého reálneho verejného vydania. Pilot súkromného doručenia a produkčný režim bez novej verzie prešli; verejné doručenie novej verzie ešte nie je potvrdené.

## Rozhodnutie

**Výsledok:** accepted pre pripravovanú 1.9.0 RC1; stabilná 1.8.0 a jej machine-readable katalóg sa nemenia. Ide o novú kompatibilnú contract family (MINOR).
