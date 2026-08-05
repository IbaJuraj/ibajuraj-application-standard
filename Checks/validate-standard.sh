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

required_files=(
  "README.md"
  "STANDARD_VERSION"
  "standard.json"
  "standard.schema.json"
  "IBAJURAJ_APPLICATION_STANDARD.md"
  "GOVERNANCE.md"
  "CHANGELOG.md"
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

version="$(tr -d '[:space:]' < STANDARD_VERSION)"
[[ "$version" =~ ^[0-9]+\.[0-9]+\.[0-9]+$ ]] || fail "STANDARD_VERSION nemá formát SemVer"

python3 - "$version" <<'PY'
import json
import re
import sys
from pathlib import Path

version = sys.argv[1]
data = json.loads(Path("standard.json").read_text(encoding="utf-8"))

if data.get("version") != version:
    raise SystemExit("standard.json version sa nezhoduje so STANDARD_VERSION")

if data.get("source", {}).get("tag") != f"standard-v{version}":
    raise SystemExit("Tag v standard.json sa nezhoduje s verziou")

doc = Path("IBAJURAJ_APPLICATION_STANDARD.md").read_text(encoding="utf-8")
match = re.search(r"\*\*Verzia:\*\*\s*([0-9]+\.[0-9]+\.[0-9]+)", doc)
if not match:
    raise SystemExit("V hlavnom štandarde sa nenašla verzia")
if match.group(1) != version:
    raise SystemExit("Verzia hlavného štandardu sa nezhoduje")

support = Path("SUPPORT_AND_LINKS.md").read_text(encoding="utf-8")
match = re.search(r"\*\*Verzia:\*\*\s*([0-9]+\.[0-9]+\.[0-9]+)", support)
if not match:
    raise SystemExit("V SUPPORT_AND_LINKS.md sa nenašla verzia")
if match.group(1) != version:
    raise SystemExit("Verzia registra odkazov sa nezhoduje")

changelog = Path("CHANGELOG.md").read_text(encoding="utf-8")
if not re.search(rf"^##\s+{re.escape(version)}\b", changelog, re.MULTILINE):
    raise SystemExit("CHANGELOG neobsahuje aktuálnu verziu")
PY
pass "Verzie a metadata sú konzistentné"

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
