"""
Test that server library code does not use asyncio.run() (AnyIO best practice).

This test runs the check_asyncio_run_guardrails script and asserts it passes.
"""

import subprocess
import sys
from pathlib import Path

import pytest

# Project root: server/tests/unit/test_*.py -> unit -> tests -> server -> project root
PROJECT_ROOT = Path(__file__).resolve().parents[3]
CHECK_SCRIPT = PROJECT_ROOT / "scripts" / "check_asyncio_run_guardrails.py"


def test_no_asyncio_run_in_server_library_code():
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
