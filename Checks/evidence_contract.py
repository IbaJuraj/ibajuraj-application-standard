#!/usr/bin/env python3
"""Exact-build execution evidence checks for IbaJuraj Standard RC4.

This validates recorded results, scope, and primary artifact integrity; it does
not manufacture an execution or replace independent runtime acceptance.
"""
from datetime import datetime
from pathlib import Path
import hashlib
import json
import re

REVISION = re.compile(r"^(?:[0-9a-fA-F]{40}|[0-9a-fA-F]{64})$")
SHA256 = re.compile(r"^[0-9a-f]{64}$")

def inside(root, relative):
    if not isinstance(relative, str) or not relative or Path(relative).is_absolute():
        return None
    root = root.resolve()
    target = (root / relative).resolve()
    if target == root or root not in target.parents:
        return None
    return target

def load_execution_report(app, manifest, catalog, phase, errors):
    descriptor = manifest.get("executionEvidence") or {}
    if not isinstance(descriptor, dict):
        errors.append("STD-EVIDENCE-001 executionEvidence must be an object")
        return None
    relative = descriptor.get("file")
    if not relative:
        return None
    p = inside(app, relative)
    if p is None or not p.is_file():
        errors.append("STD-EVIDENCE-001 execution evidence file missing or unsafe path")
        return None
    try:
        report = json.loads(p.read_text(encoding="utf-8"))
    except (ValueError, UnicodeError, OSError):
        errors.append("STD-EVIDENCE-001 execution evidence JSON unreadable")
        return None
    if not isinstance(report, dict) or report.get("schemaVersion") != 1:
        errors.append("STD-EVIDENCE-001 invalid execution evidence schemaVersion")
        return None
    if report.get("standardVersion") != catalog.get("standardVersion") or report.get("standardCandidate") != catalog.get("candidate"):
        errors.append("STD-EVIDENCE-001 execution evidence Standard pin mismatch")
    if report.get("phase") != phase:
        errors.append("STD-EVIDENCE-001 execution evidence phase mismatch")
    app_id = manifest.get("app", {})
    identity = report.get("app", {})
    for key in ("name", "productId", "version", "build"):
        if not isinstance(app_id.get(key), str) or not app_id[key].strip():
            errors.append(f"STD-EVIDENCE-001 app.{key} missing from manifest")
        if not isinstance(identity, dict) or identity.get(key) != app_id.get(key):
            errors.append(f"STD-EVIDENCE-001 execution evidence app.{key} mismatch")
    revision = app_id.get("sourceRevision")
    if not isinstance(revision, str) or not REVISION.fullmatch(revision):
        errors.append("STD-EVIDENCE-001 manifest sourceRevision must be 40/64 hex digits")
    if report.get("sourceRevision") != revision:
        errors.append("STD-EVIDENCE-001 sourceRevision mismatch")
    if not isinstance(report.get("results"), dict):
        errors.append("STD-EVIDENCE-001 execution evidence results must be an object")
        return None
    return report

def check_execution_result(app, report, identifier, mode, check, errors, warnings):
    if report is None:
        warnings.append(f"{identifier} PENDING – execution evidence absent")
        return False
    result = report["results"].get(identifier)
    if result is None:
        warnings.append(f"{identifier} PENDING – no executed result")
        return False
    if not isinstance(result, dict):
        errors.append(f"{identifier} invalid execution evidence record")
        return False
    status = result.get("status")
    if status == "pending":
        warnings.append(f"{identifier} PENDING – execution not completed")
        return False
    if status != "pass":
        errors.append(f"{identifier} execution status is not PASS: {status}")
        return False
    valid = True
    if result.get("mode") != mode or result.get("check") != check:
        errors.append(f"{identifier} execution mode/check mismatch")
        valid = False
    timestamp = result.get("executedAt")
    try:
        dt = datetime.fromisoformat(timestamp.replace("Z", "+00:00"))
        if dt.tzinfo is None:
            raise ValueError("timezone missing")
    except (ValueError, AttributeError, TypeError):
        errors.append(f"{identifier} executedAt must be timezone-aware ISO8601")
        valid = False
    if not isinstance(result.get("runner"), str) or not result["runner"].strip():
        errors.append(f"{identifier} missing execution runner")
        valid = False
    if mode in ("ui", "runtime"):
        for key in ("device", "os"):
            if not isinstance(result.get(key), str) or not result[key].strip():
                errors.append(f"{identifier} missing {key} for {mode} evidence")
                valid = False
    path = inside(app, result.get("artifact"))
    hash_declared = result.get("artifactSha256")
    if path is None or not path.is_file():
        errors.append(f"{identifier} missing/unsafe primary execution artifact")
        valid = False
    elif not isinstance(hash_declared, str) or not SHA256.fullmatch(hash_declared):
        errors.append(f"{identifier} missing/invalid artifact SHA256")
        valid = False
    elif hashlib.sha256(path.read_bytes()).hexdigest() != hash_declared:
        errors.append(f"{identifier} execution artifact SHA256 mismatch")
        valid = False
    return valid
