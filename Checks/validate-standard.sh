#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

fail() {
  printf '❌ %s\n' "$1" >&2
  exit 1
}

pass() {
  printf '✅ %s\n' "$1"
}

version="$(tr -d '[:space:]' < STANDARD_VERSION 2>/dev/null || true)"
[[ "$version" =~ ^[0-9]+\.[0-9]+\.[0-9]+$ ]] || fail "STANDARD_VERSION nemá formát SemVer"

required_files=(
  ".github/ISSUE_TEMPLATE/config.yml"
  ".github/ISSUE_TEMPLATE/standard-change.yml"
  ".github/PULL_REQUEST_TEMPLATE.md"
  ".github/workflows/validate-standard.yml"
  ".gitignore"
  "README.md"
  "STANDARD_VERSION"
  "standard.json"
  "standard.schema.json"
  "IBAJURAJ_APPLICATION_STANDARD.md"
  "DESIGN_TOKENS.md"
  "GOVERNANCE.md"
  "CHANGELOG.md"
  "MIGRATION.md"
  "TEST_MATRIX.md"
  "RELEASE_CHECKLIST.md"
  "REFERENCE_PATTERNS.md"
  "RELEASE_NOTES_${version}.md"
  "SHA256SUMS.txt"
  "SUPPORT_AND_LINKS.md"
  "Proposals/README.md"
  "Proposals/TEMPLATE.md"
  "Templates/APP_STANDARD_ADOPTION.md"
  "Templates/STANDARD_EXCEPTION.md"
)

for path in "${required_files[@]}"; do
  [[ -f "$path" ]] || fail "Chýba povinný súbor: $path"
done
pass "Povinné súbory existujú"

python3 - "$version" <<'PY'
import json
import re
import sys
from datetime import date
from pathlib import Path
from urllib.parse import urlparse

version = sys.argv[1]
data = json.loads(Path("standard.json").read_text(encoding="utf-8"))
schema = json.loads(Path("standard.schema.json").read_text(encoding="utf-8"))

def validate(value, rule, path="$"):
    expected_type = rule.get("type")
    type_map = {
        "object": dict,
        "string": str,
        "boolean": bool,
        "integer": int,
        "array": list,
    }
    if expected_type in type_map and not isinstance(value, type_map[expected_type]):
        raise SystemExit(f"{path}: očakáva sa typ {expected_type}")
    if expected_type == "integer" and isinstance(value, bool):
        raise SystemExit(f"{path}: očakáva sa celé číslo")
    if "const" in rule and value != rule["const"]:
        raise SystemExit(f"{path}: hodnota sa nezhoduje s const")
    if "enum" in rule and value not in rule["enum"]:
        raise SystemExit(f"{path}: hodnota nie je v povolenom enum")
    if isinstance(value, str):
        if "pattern" in rule and not re.fullmatch(rule["pattern"], value):
            raise SystemExit(f"{path}: hodnota nezodpovedá pattern")
        if rule.get("format") == "date":
            try:
                date.fromisoformat(value)
            except ValueError as exc:
                raise SystemExit(f"{path}: neplatný dátum") from exc
        if rule.get("format") == "uri":
            parsed = urlparse(value)
            if not parsed.scheme or not parsed.netloc:
                raise SystemExit(f"{path}: neplatná URI")
    if isinstance(value, dict):
        properties = rule.get("properties", {})
        missing = [key for key in rule.get("required", []) if key not in value]
        if missing:
            raise SystemExit(f"{path}: chýbajú povinné kľúče: {', '.join(missing)}")
        if rule.get("additionalProperties") is False:
            extra = sorted(set(value) - set(properties))
            if extra:
                raise SystemExit(f"{path}: nepovolené kľúče: {', '.join(extra)}")
        for key, child in properties.items():
            if key in value:
                validate(value[key], child, f"{path}.{key}")
    if isinstance(value, list):
        if len(value) < rule.get("minItems", 0):
            raise SystemExit(f"{path}: pole má menej položiek než minItems")
        if rule.get("uniqueItems"):
            encoded = [json.dumps(item, sort_keys=True, ensure_ascii=False) for item in value]
            if len(encoded) != len(set(encoded)):
                raise SystemExit(f"{path}: položky poľa nie sú jedinečné")
        item_rule = rule.get("items")
        if item_rule:
            for index, item in enumerate(value):
                validate(item, item_rule, f"{path}[{index}]")

validate(data, schema)

if data["version"] != version:
    raise SystemExit("standard.json version sa nezhoduje so STANDARD_VERSION")
if data["source"]["tag"] != f"standard-v{version}":
    raise SystemExit("Tag v standard.json sa nezhoduje s verziou")

expected_keywords = ["MUST", "MUST NOT", "SHOULD", "SHOULD NOT", "MAY"]
if data["normativeKeywords"] != expected_keywords:
    raise SystemExit("standard.json nemá presný zoznam normatívnych kľúčových slov")

expected_levels = [
    (0, "declared", "Level 0 – Declared"),
    (1, "identity", "Level 1 – Identity"),
    (2, "shared-ux", "Level 2 – Shared UX"),
    (3, "quality-gates", "Level 3 – Quality Gates"),
    (4, "full-adoption", "Level 4 – Full Adoption"),
]
actual_levels = [(item["level"], item["id"], item["name"]) for item in data["adoptionLevels"]]
if actual_levels != expected_levels:
    raise SystemExit("standard.json nemá presný a usporiadaný zoznam úrovní adopcie")

for label, filename in data["documents"].items():
    if not Path(filename).is_file():
        raise SystemExit(f"standard.json documents.{label} odkazuje na chýbajúci súbor {filename}")

checks = {
    "IBAJURAJ_APPLICATION_STANDARD.md": rf"\*\*Verzia:\*\*\s*{re.escape(version)}\b",
    "DESIGN_TOKENS.md": rf"\*\*Verzia:\*\*\s*{re.escape(version)}\b",
    "SUPPORT_AND_LINKS.md": rf"\*\*Verzia:\*\*\s*{re.escape(version)}\b",
    "README.md": rf"Aktuálna verzia:\s*\*\*{re.escape(version)}\*\*",
    "CHANGELOG.md": rf"^##\s+{re.escape(version)}\b",
    f"RELEASE_NOTES_{version}.md": rf"^#\s+IbaJuraj Application Standard {re.escape(version)}\b",
}
for filename, pattern in checks.items():
    text = Path(filename).read_text(encoding="utf-8")
    if not re.search(pattern, text, re.MULTILINE):
        raise SystemExit(f"{filename} neobsahuje aktuálnu verziu {version}")

adoption = Path("Templates/APP_STANDARD_ADOPTION.md").read_text(encoding="utf-8")
if f"**Adopted standard:** {version}" not in adoption:
    raise SystemExit("Adopčná šablóna nemá aktuálnu verziu")
if adoption.count(f"standard-v{version}") < 2:
    raise SystemExit("Adopčná šablóna nemá aktuálny tag na všetkých miestach")
if not re.search(r"\*\*Adoption level:\*\*\s*Level [0-4]\b", adoption):
    raise SystemExit("Adopčná šablóna nemá platnú úroveň adopcie")
if "Level 2 – Enforced" in adoption:
    raise SystemExit("Adopčná šablóna obsahuje neplatný vlastný názov úrovne")

for filename in ("IBAJURAJ_APPLICATION_STANDARD.md", "DESIGN_TOKENS.md", "SUPPORT_AND_LINKS.md"):
    normative_text = Path(filename).read_text(encoding="utf-8")
    legacy = re.findall(r"\b(?:MUSÍ|MUSIA|MÁ|NESMIE|NESMÚ)\b", normative_text)
    if legacy:
        raise SystemExit(f"{filename} obsahuje nejednotné normatívne kľúčové slová")

contract_patterns = {
    "IBAJURAJ_APPLICATION_STANDARD.md": [
        r"gearshape\.fill.*vpravo hore na hlavnej obrazovke",
        r"systémovú šípku späť",
        r"gesto potiahnutia z ľavého okraja späť",
        r"Automaticky / Svetlý / Tmavý",
        r"Obrazovka Kontakt MUST byť bežnou push obrazovkou",
        r"UIScreen\.main\.bounds",
        r"minimumScaleFactor",
        r"Privacy Manifest.*app.*widget.*extension target",
    ],
    "DESIGN_TOKENS.md": [
        r"header\.action\.visualDiameter",
        r"header\.action\.hitArea",
        r"header\.action\.maximumPerSide",
        r"settings\.group\.radius",
        r"contact\.maximumPrimaryActions",
    ],
    "SUPPORT_AND_LINKS.md": [
        r"\?app=<app-id>&type=<type>&subject=<subject>#support",
        r"Web MUST validovať `app` a `type`",
    ],
}
for filename, patterns in contract_patterns.items():
    contract_text = Path(filename).read_text(encoding="utf-8")
    for pattern in patterns:
        if not re.search(pattern, contract_text, re.IGNORECASE | re.MULTILINE):
            raise SystemExit(f"{filename} neobsahuje povinný kontrakt: {pattern}")
PY
pass "Verzie, JSON schéma, metadata a normatívny jazyk sú konzistentné"

actual_files="$({
  find . -type f \
    -not -path './.git/*' \
    -not -path './SHA256SUMS.txt' \
    -print | sed 's#^./##' | LC_ALL=C sort
})"
manifest_files="$(awk '{sub(/^[^ ]+  /, ""); print}' SHA256SUMS.txt | LC_ALL=C sort)"
[[ "$actual_files" == "$manifest_files" ]] || fail "SHA256SUMS.txt neobsahuje presne všetky súbory release"
sha256sum --check --strict SHA256SUMS.txt >/dev/null || fail "Kontrola SHA-256 súčtov zlyhala"
pass "SHA-256 integrita release je platná"

if find . -type f \( -name '.DS_Store' -o -name 'Thumbs.db' \) -print -quit | grep -q .; then
  fail "Repozitár obsahuje systémové odpadové súbory"
fi
if find . -type d -name '__MACOSX' -print -quit | grep -q .; then
  fail "Repozitár obsahuje priečinok __MACOSX"
fi
pass "Repozitár neobsahuje známe odpadové súbory"

if grep -RIlE '(BEGIN (RSA|OPENSSH|EC) PRIVATE KEY|ghp_[A-Za-z0-9]{20,}|github_pat_[A-Za-z0-9_]{20,})' . \
  --exclude-dir=.git --exclude='validate-standard.sh' | grep -q .; then
  fail "Možný tajný kľúč alebo token v repozitári"
fi
pass "Nenašiel sa zjavný tajný kľúč alebo token"

printf '\nIbaJuraj Application Standard %s: VALID\n' "$version"
