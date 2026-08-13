"""Tests for scripts/run_make_stages.py fail-fast helpers."""

from __future__ import annotations

import importlib.util
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[4]
SCRIPT = PROJECT_ROOT / "scripts" / "run_make_stages.py"


def _load_module():
    spec = importlib.util.spec_from_file_location("run_make_stages", SCRIPT)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_stage_failed_from_output_nonzero() -> None:
    mod = _load_module()
    assert mod.stage_failed_from_output("ok", 1) == "non-zero exit (1)"


def test_stage_failed_from_output_traceback() -> None:
    mod = _load_module()
    out = 'Traceback (most recent call last):\n  File "x.py", line 1\n'
    assert mod.stage_failed_from_output(out, 0) == "traceback/callstack detected in output"


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
