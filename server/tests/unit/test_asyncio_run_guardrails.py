"""
Test that server library code does not use asyncio.run() (AnyIO best practice).

This test runs the check_asyncio_run_guardrails script and asserts it passes.
"""

from __future__ import annotations

import importlib.util
import subprocess
import sys
from collections.abc import Callable
from pathlib import Path
from typing import Protocol, cast

import pytest

# Project root: server/tests/unit/test_*.py -> unit -> tests -> server -> project root
PROJECT_ROOT = Path(__file__).resolve().parents[3]
CHECK_SCRIPT = PROJECT_ROOT / "scripts" / "check_asyncio_run_guardrails.py"


class _AsyncioGuardrailsModule(Protocol):
    """Public skip helper of check_asyncio_run_guardrails loaded via importlib."""

    is_skipped_scan_path: Callable[[Path], bool]


def _load_checker() -> _AsyncioGuardrailsModule:
    spec = importlib.util.spec_from_file_location("_check_asyncio_run_guardrails", CHECK_SCRIPT)
    assert spec and spec.loader
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    # ModuleType does not overlap Protocol; cast via object for importlib-loaded modules.
    return cast(_AsyncioGuardrailsModule, cast(object, mod))


def test_skips_nested_graphify_venv_paths() -> None:
    """Vendored graphify/.venv trees are not server library code."""
    checker = _load_checker()
    nested_venv = Path("server/graphify-out/.venv/Lib/site-packages/graphify/serve.py")
    assert checker.is_skipped_scan_path(nested_venv) is True
    assert checker.is_skipped_scan_path(Path("server/main.py")) is False


def test_no_asyncio_run_in_server_library_code() -> None:
    """Assert server/ has no asyncio.run() in library code (use anyio.run() at entry points)."""
    if not CHECK_SCRIPT.exists():
        pytest.skip("check_asyncio_run_guardrails.py not found")
    result = subprocess.run(
        [sys.executable, str(CHECK_SCRIPT)],
        cwd=str(PROJECT_ROOT),
        capture_output=True,
        text=True,
        timeout=30,
    )
    assert result.returncode == 0, (
        "asyncio.run() should not be used in server library code. "
        "Use anyio.run() at entry points. See .cursor/rules/anyio.mdc. "
        f"Stdout: {result.stdout} Stderr: {result.stderr}"
    )
