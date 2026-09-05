#!/usr/bin/env python3
"""
ADR-001 import layer direction guard (import-linter).

Wraps ``lint-imports`` so ``make all`` fails fast and loudly when domain or
persistence layers import forbidden service modules. See ``.importlinter``.

Usage: python scripts/lint_imports.py
Exit: 0 when all contracts are kept; 1 on broken contracts or tool failure.
"""

from __future__ import annotations

import os
import re
import shutil
import sys
from pathlib import Path

from utils.safe_subprocess import safe_run_static

PROJECT_ROOT = Path(__file__).resolve().parents[1]
# import-linter's rich-based progress spinner renders emoji (e.g. the brick in "Building
# graph..."). On Windows, subprocess stdout defaults to the console's active code page (often
# cp1252), which can't encode those characters -- rich then crashes mid-render with
# UnicodeEncodeError before printing any real contract results, and that crash's non-zero exit
# code gets misreported here as "ADR-001 violated" even when every contract is actually kept.
# Forcing UTF-8 for the child process only (not the whole environment) sidesteps this regardless
# of the host console's code page.
_UTF8_ENV = {**os.environ, "PYTHONUTF8": "1", "PYTHONIOENCODING": "utf-8"}
BANNER = "=" * 72
_BROKEN_CONTRACT_LINE = re.compile(r"^\s*(?P<name>.+?)\s+BROKEN\s*$", re.MULTILINE)
_CONTRACTS_SUMMARY = re.compile(r"Contracts:\s*\d+\s+kept,\s*(?P<broken>\d+)\s+broken", re.IGNORECASE)
_INSTALL_HINT = "Install with: uv sync --extra dev  (import-linter is in dev dependencies)"


def _resolve_lint_imports_cmd() -> list[str]:
    if shutil.which("uv"):
        return ["uv", "run", "lint-imports"]
    lint_imports = shutil.which("lint-imports")
    if lint_imports:
        return [lint_imports]
    return ["lint-imports"]


def broken_contract_names(output: str) -> list[str]:
    """Return contract names marked BROKEN in import-linter output."""
    return [match.group("name").strip() for match in _BROKEN_CONTRACT_LINE.finditer(output)]


def broken_contract_count(output: str) -> int | None:
    """Parse ``Contracts: N kept, M broken`` summary; None if summary line missing."""
    match = _CONTRACTS_SUMMARY.search(output)
    if match is None:
        return None
    return int(match.group("broken"))


def lint_imports_failed(output: str, returncode: int) -> bool:
    """True when import-linter reported broken contracts or exited non-zero."""
    if returncode != 0:
        return True
    broken = broken_contract_count(output)
    if broken is not None and broken > 0:
        return True
    return bool(broken_contract_names(output))


def _print_failure(output: str, returncode: int) -> None:
    print(BANNER, file=sys.stderr)
    print("[ERROR] ADR-001 import layer direction violated (import-linter)", file=sys.stderr)
    print("Domain (models/, events/) and persistence must not import game/, services/, or npc/.", file=sys.stderr)
    names = broken_contract_names(output)
    if names:
        print("Broken contracts:", file=sys.stderr)
        for name in names:
            print(f"  - {name}", file=sys.stderr)
    broken = broken_contract_count(output)
    if broken is not None:
        print(f"Contracts summary: {broken} broken", file=sys.stderr)
    print(f"exit code: {returncode}", file=sys.stderr)
    print(
        "See .importlinter and docs/architecture/decisions/ADR-001-layered-architecture-event-driven.md",
        file=sys.stderr,
    )
    print(BANNER, file=sys.stderr)
    if output.strip():
        print(output, file=sys.stderr)


def _contracts_summary_message(output: str) -> str:
    """Human-readable contracts summary from import-linter output."""
    match = _CONTRACTS_SUMMARY.search(output)
    if match is None:
        return "all contracts kept"
    kept_match = re.search(r"Contracts:\s*(?P<kept>\d+)\s+kept", output, re.IGNORECASE)
    kept = kept_match.group("kept") if kept_match else "?"
    return f"{kept} kept, {match.group('broken')} broken"


def _print_success(output: str) -> None:
    print(f"[OK] ADR-001 import layer direction: {_contracts_summary_message(output)}")


def main() -> int:
    cmd = _resolve_lint_imports_cmd()
    probe = safe_run_static(
        *cmd,
        "--version",
        cwd=PROJECT_ROOT,
        capture_output=True,
        text=True,
        env=_UTF8_ENV,
        encoding="utf-8",
        errors="replace",
    )
    if probe.returncode != 0:
        print("[ERROR] lint-imports is not runnable; failing fast so Make does not continue.", file=sys.stderr)
        print(_INSTALL_HINT, file=sys.stderr)
        if probe.stdout:
            print(probe.stdout, file=sys.stderr)
        if probe.stderr:
            print(probe.stderr, file=sys.stderr)
        return 1

    result = safe_run_static(
        *cmd,
        cwd=PROJECT_ROOT,
        capture_output=True,
        text=True,
        env=_UTF8_ENV,
        encoding="utf-8",
        errors="replace",
    )
    output = f"{result.stdout or ''}{result.stderr or ''}"
    if lint_imports_failed(output, result.returncode):
        _print_failure(output, result.returncode)
        return result.returncode if result.returncode != 0 else 1

    _print_success(output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
