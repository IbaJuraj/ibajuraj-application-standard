#!/bin/bash
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
VERSION="$(tr -d '[:space:]' < "$ROOT/STANDARD_VERSION")"
[ "$VERSION" = "1.7.0" ] || { echo "FAIL: expected 1.7.0"; exit 1; }
echo "PASS: local candidate Standard $VERSION"
echo "NOTE: RC2 is a pre-release candidate; public authority remains the latest active Standard until standard-v1.7.0 is published."
