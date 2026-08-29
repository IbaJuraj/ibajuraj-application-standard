# IbaJuraj Application Standard 1.7.0 – Reference Patterns

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

Generický pattern:

```text
<AppName> v<marketingVersion> – Build <build>.
```

## 3. About – Standard card

```text
IbaJuraj Application Standard
Verzia 1.7.0
```

Používateľské UI neukazuje tag, commit ani adoption level.

## 4. Live theme selection

```text
Tap theme option
  → update selected model
  → persist value
  → invalidate/render current screen
  → checkmark and background change immediately
```

Návrat späť nie je triggerom aplikácie témy.

## 5. Container-driven adaptive keypad

```text
availableWidth  → widthLimit
availableHeight → heightLimit
keySize = clamp(min(widthLimit, heightLimit), minKey, maxKey)
```

Horná hranica keypadu môže byť produktový anchor. Rast smerom nadol/bočne nesmie vytlačiť obsah nad anchorom.

## 6. Bottom navigation variants

### Native
Použi systémový `TabView`, ak netreba vlastnú globálnu akciu alebo inú oprávnenú geometriu.

### Custom floating
Použi shared baseline z `DESIGN_TOKENS.md`; safe area a content clearance sa počítajú dynamicky. Primary action nesmie nafúknuť celý bar len kvôli svojmu priemeru.

## 7. Conformance evidence

```json
"STD-ABOUT-002": {
  "mode": "static",
  "status": "implemented",
  "evidence": {
    "files": ["App/AboutView.swift"],
    "containsAll": ["CFBundleShortVersionString", "CFBundleVersion"]
  }
}
```

Behaviorálne pravidlo:

```json
"STD-APPEARANCE-001": {
  "mode": "ui",
  "status": "implemented",
  "test": "AppearanceLiveUpdateUITests/testThemeAppliesWithoutBackNavigation"
}
```

Manuálny runtime gate:

```json
"STD-ADAPT-010": {
  "mode": "runtime",
  "status": "implemented",
  "runtimeGate": "RUNTIME_ACCEPTANCE.md#STD-ADAPT-010"
}
```

## 8. Root top anchor

```text
topSafeArea.bottom
  + shared root-header extra inset (0–4 pt baseline)
  → root title/header
```

Nevkladaj per-screen `padding(.top, 14)` iba kvôli historickému vzhľadu. Peer root screens používajú spoločný token.

## 9. Custom bottom chrome – position vs clearance

```text
viewport bottom / safe-area geometry
  → lowest safe bar position

bar overlap + final visual reserve
  → scroll content bottom clearance
```

Tieto dve hodnoty sa počítajú oddelene. Zvýšenie scroll clearance nesmie posunúť bar vyššie.

## 10. Screen-family inventory

```json
"screenAudit": {
  "families": {
    "SCREEN-ROOT": {
      "status": "pass",
      "screens": ["Home", "Cards"],
      "evidence": ["RUNTIME_ACCEPTANCE.md#SCREEN-ROOT"]
    },
    "SCREEN-SETTINGS": {
      "status": "pending",
      "screens": ["Settings"]
    }
  }
}
```

Family `pass` bez evidence je invalidný. `pending` blokuje Level 4.

## RC3 header ownership pattern
Prefer either native `navigationTitle` **or** a custom page/sheet header for the authoritative page title. A section heading must narrow the content meaning. Do not reserve an empty navigation band only for close/back control above a second title.
