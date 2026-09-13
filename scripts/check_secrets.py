# Candidate: Manoher Singh | manoharmsp93@gmail.com | +91-9648548275
# HabotConnect Hiring Project — deterministic secret gate

#!/usr/bin/env python3
"""Small deterministic fail-closed secret-pattern scan for assignment evidence."""

from __future__ import annotations

import re
import sys
from pathlib import Path

EXCLUDED = {".git", ".terraform", "__pycache__", ".venv", "presentation"}
PATTERNS = [
    re.compile(r"AKIA[0-9A-Z]{16}"),
    re.compile(r"(?i)(api[_-]?key|secret[_-]?key|access[_-]?token)\s*[:=]\s*['\"][A-Za-z0-9_\-+/=]{12,}['\"]"),
    re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
]


def iter_files(root: Path):
    for path in root.rglob("*"):
        if not path.is_file():
            continue
        if any(part in EXCLUDED for part in path.parts):
            continue
        if path.suffix.lower() in {".png", ".jpg", ".jpeg", ".pptx", ".xlsx", ".pdf", ".zip"}:
            continue
        yield path


def main() -> int:
    findings = []
    root = Path(".")
    for path in iter_files(root):
        try:
            text = path.read_text(encoding="utf-8", errors="ignore")
        except OSError:
            continue
        for pattern in PATTERNS:
            if pattern.search(text):
                findings.append(str(path))
                break

    if findings:
        print("FAIL-CLOSED: possible hardcoded secret detected in:")
        for item in findings:
            print(f" - {item}")
        return 1

    print("PASS: no configured hardcoded-secret patterns detected.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
