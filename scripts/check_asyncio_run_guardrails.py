#!/usr/bin/env python3
"""
Guardrail: forbid asyncio.run() in server library code (AnyIO best practice).

Scans server/ for asyncio.run( in .py files. Exits 0 if none found, 1 otherwise.
Comments and string literals are excluded so only actual code is flagged.

Usage: python scripts/check_asyncio_run_guardrails.py
"""

import re
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
SERVER_DIR = PROJECT_ROOT / "server"

# Pattern: asyncio.run( as executable code (not inside string or comment)
# Simple approach: line contains asyncio.run( and is not a comment
COMMENT_PATTERN = re.compile(r"^\s*#")
ASYNCIO_RUN_PATTERN = re.compile(r"\basyncio\.run\s*\(")


def _strip_triple_quoted_blocks(text: str) -> str:
    """Remove triple-quoted string blocks from file content."""
    text = re.sub(r'"""[\s\S]*?"""', "", text)
    text = re.sub(r"'''[\s\S]*?'''", "", text)
    return text


def _strip_string_literals(line: str) -> str:
    """Remove string literals from line to avoid false positives inside docs/strings."""
    line = re.sub(r'"[^"]*"', '""', line)
    line = re.sub(r"'[^']*'", "''", line)
    return line


def check_file(path: Path) -> list[tuple[int, str]]:
    """Return list of (line_no, line) where asyncio.run( appears in code."""
    violations: list[tuple[int, str]] = []
    try:
        text = path.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return violations
    # Remove triple-quoted blocks so docstrings do not trigger
    text_no_docstrings = _strip_triple_quoted_blocks(text)
    for i, line in enumerate(text_no_docstrings.splitlines(), start=1):
        if COMMENT_PATTERN.match(line):
            continue
        stripped = _strip_string_literals(line)
        if ASYNCIO_RUN_PATTERN.search(stripped):
            violations.append((i, line.strip()))
    return violations


def main() -> int:
    """Return 0 if no asyncio.run( in server/, else 1."""
    violations: list[tuple[Path, int, str]] = []
    for py_path in sorted(SERVER_DIR.rglob("*.py")):
        for line_no, line in check_file(py_path):
            rel = py_path.relative_to(PROJECT_ROOT)
            violations.append((rel, line_no, line))
    if violations:
        print("check_asyncio_run_guardrails: asyncio.run() is not allowed in server library code.")
        print("Use anyio.run() at entry points instead. See .cursor/rules/anyio.mdc")
        for rel, line_no, line in violations:
            print(f"  {rel}:{line_no}: {line[:80]}")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
