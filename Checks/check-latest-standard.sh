#!/bin/bash
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
VERSION="$(tr -d '[:space:]' < "$ROOT/STANDARD_VERSION")"
[ "$VERSION" = "1.8.0" ] || { echo "FAIL: expected 1.8.0"; exit 1; }
echo "PASS: local Standard candidate $VERSION RC1"
echo "Candidate tag: standard-v1.8.0-rc1"
echo "Active public authority remains: standard-v1.7.0"
