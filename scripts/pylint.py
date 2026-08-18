#!/usr/bin/env python3
"""
Run Pylint on Python code.
Excludes test files and uses project-specific configuration.

This script runs comprehensive pylint checks to align with ruff linting.
Categories enabled:
- E: Error (syntax errors, etc.)
- W: Warning (style issues)
- F: Fatal (internal pylint errors)
- C: Convention (coding standard violations)
- R: Refactor (code quality suggestions)

Note: Complexity checking (C901) is handled by ruff, not pylint.

Tool-missing / unrunnable pylint must exit non-zero so Make stops (make all / codacy-tools).
"""

from __future__ import annotations

import importlib.util
import shutil
import sys
from pathlib import Path
from typing import Protocol

from utils.safe_subprocess import safe_run_static


class _CompletedProcessLike(Protocol):
    returncode: int

    @property
    def stdout(self) -> str | None: ...

    @property
    def stderr(self) -> str | None: ...


_INSTALL_HINT = "Install with: uv sync --extra dev  (or: uv sync --group dev / uv pip install 'pylint>=4.0.4')"


def _resolve_pylint_cmd() -> list[str]:
    """Prefer current interpreter -m pylint (works under uv run --no-sync)."""
    if importlib.util.find_spec("pylint") is not None:
        return [sys.executable, "-m", "pylint"]
    pylint_path = shutil.which("pylint")
    if pylint_path:
        return [pylint_path]
    result = safe_run_static("uv", "run", "pylint", "--version", cwd=".")
    if result.returncode == 0:
        return ["uv", "run", "pylint"]
    print("[ERROR] pylint not found. " + _INSTALL_HINT)
    sys.exit(1)


def _require_pylint_runnable(cmd: list[str]) -> None:
    """Fail fast before scanning if pylint cannot start (missing package, broken venv)."""
    probe = safe_run_static(*cmd, "--version", cwd=".", capture_output=True, text=True)
    if probe.returncode != 0:
        print("[ERROR] pylint is not runnable; failing fast so Make does not continue.")
        print(_INSTALL_HINT)
        if probe.stdout:
            print(probe.stdout)
        if probe.stderr:
            print(probe.stderr, file=sys.stderr)
        sys.exit(1)


def _combined_output(result: _CompletedProcessLike) -> str:
    return f"{result.stdout or ''}\n{result.stderr or ''}"


def is_pylint_startup_failure(result: _CompletedProcessLike) -> bool:
    """
    True when pylint never ran as a linter (missing module, usage/invocation error).

    Pylint bit 32 = usage error. Python ``-m pylint`` with a missing package typically
    exits 1 with ``No module named pylint`` and must not be treated as lint findings.
    """
    text = _combined_output(result)
    if "No module named pylint" in text or "No module named 'pylint'" in text:
        return True
    if "No module named" in text and "pylint" in text.lower():
        return True
    # pylint usage / invocation error bit (see pylint exit codes)
    if (result.returncode & 32) != 0:
        return True
    return False


def _write_pylint_output(result: _CompletedProcessLike, output_file: Path) -> None:
    with output_file.open("w", encoding="utf-8") as f:
        if result.stdout:
            _ = f.write(result.stdout)
        if result.stderr:
            if result.stdout:
                _ = f.write("\n--- STDERR ---\n")
            _ = f.write(result.stderr)


def _report_pylint_failure(result: _CompletedProcessLike, output_file: Path, *, startup: bool) -> int:
    if startup:
        print("[ERROR] pylint failed to start; failing fast so Make does not continue.")
        print(_INSTALL_HINT)
    else:
        print("[ERROR] Pylint found code quality issues:")
    if result.stdout:
        print(result.stdout)
    if result.stderr:
        print("Errors:", result.stderr)
    print(f"\nFull output saved to: {output_file}")
    return 1


def main() -> int:
    pylint_cmd = _resolve_pylint_cmd()
    _require_pylint_runnable(pylint_cmd)

    print("Running comprehensive Pylint on Python code...")
    print("Categories: E (Error), W (Warning), F (Fatal), C (Convention), R (Refactor)")
    print("This will check for code quality issues...")

    # Run pylint on server directory
    # Exclude test files, scripts, docs, and other non-production code (matching ruff's scope)
    # Note: Complexity checking is handled by ruff (C901), not pylint
    cmd = pylint_cmd + [
        "server",
        "--ignore=tests,scripts,docs,alembic,stubs,graphify-out,.venv",
        "--max-line-length=120",
        "--disable=all",
        "--enable=E,W,F,C,R",  # E=Error, W=Warning, F=Fatal, C=Convention, R=Refactor
        # Re-apply disables from .pylintrc after --enable so they are not re-enabled by --enable=E,W,F,C,R.
        # Complexity (R0911-R0915, R0902, R0903, R0904) is handled by ruff C901; see .pylintrc and
        # docs/LINTING_COMPLEXITY_ALIGNMENT.md.
        (
            "--disable=line-too-long,import-outside-toplevel,too-many-arguments,"
            + "too-many-positional-arguments,too-many-locals,too-many-statements,"
            + "too-many-return-statements,too-many-branches,too-many-instance-attributes,"
            + "too-many-public-methods,too-few-public-methods"
        ),
        "--output-format=text",
        "--rcfile=.pylintrc",  # Use project pylintrc
    ]

    try:
        result = safe_run_static(*cmd, cwd=".", capture_output=True, text=True)
    except Exception as e:  # pylint: disable=W0718
        # Any failure launching subprocess is a hard stop for Make.
        print(f"[ERROR] Error running pylint: {e}")
        return 1

    output_file = Path("pylint_output.txt")
    _write_pylint_output(result, output_file)

    if is_pylint_startup_failure(result):
        return _report_pylint_failure(result, output_file, startup=True)

    if result.returncode == 0:
        print("[OK] Pylint scan completed successfully!")
        print("No code quality issues found.")
        print(f"Output saved to: {output_file}")
        print("\n[SUCCESS] Pylint checks completed!")
        return 0

    # Any pylint finding (E/W/F/C/R) fails make pylint / make all.
    return _report_pylint_failure(result, output_file, startup=False)


if __name__ == "__main__":
    sys.exit(main())
