#!/usr/bin/env python3
"""Verify complete SHA256SUMS coverage and content for the candidate repository.

SHA256SUMS.txt intentionally excludes itself; Git metadata, Python caches and
machine-generated files are excluded from the file inventory.
"""
from pathlib import Path
import hashlib
import re
import sys

ROOT = Path(__file__).resolve().parent.parent
MANIFEST = ROOT / "SHA256SUMS.txt"

def tracked_candidates():
    for p in ROOT.rglob("*"):
        if not p.is_file():
            continue
        parts = p.relative_to(ROOT).parts
        if ".git" in parts or "__pycache__" in parts or "xcuserdata" in parts:
            continue
        if p.suffix == ".pyc" or p.name in {"SHA256SUMS.txt", ".DS_Store"}:
            continue
        yield p.relative_to(ROOT).as_posix()

def main():
    errors, entries = [], {}
    for number, line in enumerate(MANIFEST.read_text(encoding="utf-8").splitlines(), 1):
        match = re.fullmatch(r"([0-9a-f]{64})  (.+)", line)
        if not match:
            errors.append(f"invalid SHA256SUMS line {number}")
            continue
        digest, relative = match.groups()
        if relative in entries:
            errors.append(f"duplicate manifest entry: {relative}")
        entries[relative] = digest

    actual = set(tracked_candidates())
    wanted = set(entries)
    for relative in sorted(actual - wanted):
        errors.append(f"file missing from manifest: {relative}")
    for relative in sorted(wanted - actual):
        errors.append(f"manifest points to missing file: {relative}")
    for relative in sorted(actual & wanted):
        digest = hashlib.sha256((ROOT / relative).read_bytes()).hexdigest()
        if digest != entries[relative]:
            errors.append(f"SHA256 mismatch: {relative}")

    if errors:
        print("FAIL – SHA256 manifest")
        for error in errors:
            print(" -", error)
        return 1
    print(f"PASS – SHA256 manifest ({len(actual)} files, complete)")
    return 0

if __name__ == "__main__":
    sys.exit(main())
