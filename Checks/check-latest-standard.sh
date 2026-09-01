#!/bin/bash
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
VERSION="$(tr -d '[:space:]' < "$ROOT/STANDARD_VERSION")"
[ "$VERSION" = "1.7.0" ] || { echo "FAIL: expected 1.7.0"; exit 1; }
echo "PASS: local active Standard $VERSION"
echo "Final release tag: standard-v1.7.0"
