"""Tests for scripts/run_make_stages.py fail-fast helpers."""

from __future__ import annotations

import importlib.util
from pathlib import Path
from typing import Protocol, cast

PROJECT_ROOT = Path(__file__).resolve().parents[4]
SCRIPT = PROJECT_ROOT / "scripts" / "run_make_stages.py"


class _RunMakeStages(Protocol):
    """The functions these tests call on scripts/run_make_stages.py (loaded by path, so untyped)."""

    def stage_failed_from_output(self, output: str, returncode: int) -> str | None: ...

    def keep_going_requested(self, makeflags: str | None = None) -> bool: ...


def _load_module() -> _RunMakeStages:
    spec = importlib.util.spec_from_file_location("run_make_stages", SCRIPT)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return cast(_RunMakeStages, cast(object, module))


def test_stage_failed_from_output_nonzero() -> None:
    mod = _load_module()
    assert mod.stage_failed_from_output("ok", 1) == "non-zero exit (1)"


def test_stage_failed_from_output_traceback() -> None:
    mod = _load_module()
    out = 'Traceback (most recent call last):\n  File "x.py", line 1\n'
    assert mod.stage_failed_from_output(out, 0) == "traceback/callstack detected in output"


def test_stage_failed_from_output_node_fatal_crash_fails_despite_exit_zero() -> None:
    """A crashed vitest that still left exit 0 must fail the stage (#950); this is the real output."""
    mod = _load_module()
    out = (
        " RUN  v5.0.0 C:/projects/MythosMUD/client\n"
        "      Coverage enabled with v8\n"
        "FATAL ERROR: MarkCompactCollector: young object promotion failed "
        "Allocation failed - JavaScript heap out of memory\n"
        "----- Native stack trace -----\n"
        " 1: 00007FF6477A9891\n"
    )
    assert mod.stage_failed_from_output(out, 0) == "Node/V8 fatal crash detected in output"


def test_stage_failed_from_output_server_fatal_log_line_is_not_a_crash() -> None:
    """The server's own "FATAL ERROR: ..." log line must not be mistaken for a V8 crash."""
    mod = _load_module()
    out = "[error] FATAL ERROR: Terminating all connections for player player_id=abc\n11525 passed\n"
    assert mod.stage_failed_from_output(out, 0) is None


def test_stage_failed_from_output_ok() -> None:
    mod = _load_module()
    assert mod.stage_failed_from_output("WARNING: optional skip\n", 0) is None


def test_keep_going_requested() -> None:
    mod = _load_module()
    assert mod.keep_going_requested("kw") is True
    assert mod.keep_going_requested("--keep-going") is True
    assert mod.keep_going_requested("w") is False
    assert mod.keep_going_requested("") is False


def test_makefile_composites_use_fail_fast_runner() -> None:
    makefile = (PROJECT_ROOT / "Makefile").read_text(encoding="utf-8")
    assert "scripts/run_make_stages.py" in makefile
    for target in ("all:", "codacy-tools:", "test:", "test-coverage:"):
        assert target in makefile
