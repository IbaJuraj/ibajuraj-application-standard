# IbaJuraj Application Standard 1.8.0 RC1 – Reference Patterns

## 1. Settings → O aplikácii
```text
O aplikácii                         1.11 (53)
Verzia, súkromie a štandard
```
Hodnota sa skladá z runtime `marketingVersion` a `build`.

## 2. About – Version card
```text
Verzia
Kalkulačka 2v1 v1.11 – Build 53.
```
Generický pattern: `<AppName> v<marketingVersion> – Build <build>.`

## 3. About – Standard card
Pre stabilný verejný app release sa používateľovi zobrazuje aktívna verejná verzia Standardu. RC tag/commit/adoption level sa bežne používateľovi nezobrazuje.

## 4. Live theme selection
```text
Tap theme option
  → update selected model
  → persist value
  → invalidate/render current screen
  → checkmark and background change immediately
```

## 5. Container-driven adaptive keypad
```text
availableWidth  → widthLimit
availableHeight → heightLimit
keySize = clamp(min(widthLimit, heightLimit), minKey, maxKey)
```

## 6. Bottom navigation variants
### Native
Použi systémový `TabView`, ak netreba vlastnú globálnu akciu alebo inú oprávnenú geometriu.

### Custom floating
Použi shared baseline z `DESIGN_TOKENS.md`; safe area a content clearance sa počítajú dynamicky. Primary action nesmie nafúknuť celý bar len kvôli svojmu priemeru.

## 7. Conformance evidence
Static:
```json
"STD-ABOUT-002": {
  "mode": "static",
  "status": "implemented",
  "evidence": {"files":["App/AboutView.swift"],"containsAll":["CFBundleShortVersionString","CFBundleVersion"]}
}
```

UI:
```json
"STD-LOC-005": {
  "mode": "ui",
  "status": "implemented",
  "test": "LanguageSelectorUITests/testAutomaticAndSupportedLanguages"
}
```

Runtime:
```json
"STD-BACKEND-002": {
  "mode": "runtime",
  "status": "implemented",
  "runtimeGate": "RUNTIME_ACCEPTANCE.md#STD-BACKEND-002"
}
```

## 8. Root top anchor
```text
topSafeArea.bottom
  + shared root-header extra inset (0–4 pt baseline)
  → root title/header
```

## 9. Custom bottom chrome – position vs clearance
```text
viewport bottom / safe-area geometry
  → lowest safe bar position

bar overlap + final visual reserve
  → scroll content bottom clearance
```

## 10. Screen-family inventory
```json
"screenAudit": {
  "families": {
    "SCREEN-ROOT": {
      "status": "pass",
      "screens": ["Home", "Cards"],
      "evidence": ["RUNTIME_ACCEPTANCE.md#SCREEN-ROOT"]
    }
  }
}
```
Family `pass` bez evidence je invalidný. `pending` blokuje Level 4.

## 11. Header ownership
Prefer either native `navigationTitle` **or** a custom page/sheet header for the authoritative page title. A section heading must narrow the content meaning.

## 12. Localization-first semantic identity
```text
semantic key / raw ID            localized display
----------------------------------------------------
card.category.grocery       →    Potraviny / Groceries / Lebensmittel
raw enum: grocery           →    remains "grocery"
UUID                        →    unchanged
CloudKit record ID          →    unchanged
```

Never persist the translated user-facing label as the only stable domain identity.

## 13. In-app language selector
```text
Jazyk
  Automaticky / Podľa systému
  Slovenčina
  Čeština
  English
  Deutsch
  Polski
  Magyar
```

Behavior:
```text
select locale
  → persist UI-language preference
  → update localization presentation (or deterministic relaunch)
  → DO NOT migrate domain data

select Automatic/System
  → clear explicit app override
  → resolve iOS/per-app preferred locale again
```

## 14. Environment-specific backend binding
```text
Stable local domain object
  id = wallet-123
  data = cards/name/etc.

Development binding
  remoteRecordID = dev-abc
  shareToken = dev-token

Production binding
  remoteRecordID = prod-xyz
  shareToken = prod-token
```
Development/Production bindings are not interchangeable. Missing `prod-xyz` must not delete `wallet-123`.

## 15. Single-device continuity runtime pattern
```text
Xcode / Development
  → verify local objects + IDs
  → install/open same build from TestFlight if practical
TestFlight / Production
  → same local objects + IDs
  → Production sync/share smoke
  → return to Xcode without deleting app
Xcode / Development
  → same local objects + IDs still present
```

## 16. Production backend readiness
For CloudKit-like systems:
```text
Development schema/config
  ↓ explicit deploy / parity audit
Production schema/config
  - record types/resources
  - indexes
  - security roles/permissions
  - zones/config/entitlements
  ↓
TestFlight real read/write/sync/share smoke
```
A server-side deployment that fixes the unchanged binary is evidence of a backend fix, not a reason by itself to increment the app build.

## 17. Representative-data performance
```text
realistic dataset
  → populated root/grid/list
  → scroll
  → search/filter/sort
  → root/tab switching
  → no visible avoidable hitching/layout thrash
```
The item count is product-specific; the dataset must represent real or realistic high-volume use.

## 18. Release-root hygiene
```text
<AppRoot>/
  current source/project
  current conformance/release docs
  Documentation/History/Builds/<old builds>/
```
Historical evidence is archived or consolidated, not silently deleted.
