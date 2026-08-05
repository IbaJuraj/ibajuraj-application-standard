#!/usr/bin/env bash
set -euo pipefail

REMOTE_METADATA="${1:-https://raw.githubusercontent.com/IbaJuraj/ibajuraj-application-standard/main/standard.json}"
LOCAL_VERSION_FILE="${2:-IbaJurajStandard/STANDARD_VERSION}"

if [[ ! -f "$LOCAL_VERSION_FILE" ]]; then
  printf '❌ Chýba lokálny súbor verzie: %s\n' "$LOCAL_VERSION_FILE" >&2
  exit 2
fi

local_version="$(tr -d '[:space:]' < "$LOCAL_VERSION_FILE")"
remote_json="$(curl --fail --silent --show-error --location --max-time 15 "$REMOTE_METADATA")"

remote_version="$(
  python3 -c 'import json,sys; print(json.load(sys.stdin)["version"])' <<<"$remote_json"
)"
minimum_version="$(
  python3 -c 'import json,sys; print(json.load(sys.stdin)["minimumSupportedVersion"])' <<<"$remote_json"
)"

python3 - "$local_version" "$remote_version" "$minimum_version" <<'PY'
import sys

def parse(value):
    try:
        return tuple(int(part) for part in value.split("."))
    except Exception:
        raise SystemExit(f"Neplatná verzia: {value}")

local, remote, minimum = sys.argv[1:4]
l, r, m = map(parse, (local, remote, minimum))

if l < m:
    print(f"❌ Lokálna verzia {local} je staršia než minimálne podporovaná {minimum}.")
    raise SystemExit(2)
if l < r:
    print(f"⚠️ Dostupný je IbaJuraj Application Standard {remote}; projekt používa {local}.")
    print("Prečítajte CHANGELOG a vykonajte adopčný audit.")
    raise SystemExit(1)
if l > r:
    print(f"⚠️ Lokálna verzia {local} je novšia než centrálna verzia {remote}.")
    raise SystemExit(1)

print(f"✅ Projekt používa aktuálny IbaJuraj Application Standard {local}.")
PY
