"""Unit tests for scripts/analyze_idle_memory_samples.py.

Covers the `--warmup` CLI flag (`#`, idle asyncio task leak attribution) and the
`task_qualnames` delta report `analyze()` produces from `memory_monitor.py`'s per-sample
coroutine-qualname histogram -- the mechanism that names a leaking coroutine instead of only
measuring the overall `asyncio_tasks` slope.
"""

from __future__ import annotations

import importlib.util
import json
import sys
from pathlib import Path
from typing import Protocol, cast

PROJECT_ROOT = Path(__file__).resolve().parents[4]
SCRIPT_PATH = PROJECT_ROOT / "scripts" / "analyze_idle_memory_samples.py"


class _AnalyzeIdleMemorySamplesModule(Protocol):
    """Typed surface of the loaded script, for the parts these tests exercise."""

    WARMUP_SECONDS: int

    def analyze(self, path: Path, warmup_seconds: int = ...) -> str: ...


def _load_script() -> _AnalyzeIdleMemorySamplesModule:
    spec = importlib.util.spec_from_file_location("analyze_idle_memory_samples_for_tests", SCRIPT_PATH)
    assert spec is not None
    assert spec.loader is not None
    mod = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = mod
    spec.loader.exec_module(mod)
    return cast(_AnalyzeIdleMemorySamplesModule, cast(object, mod))


def _write_samples(path: Path, rows: list[dict[str, object]]) -> None:
    with path.open("w", encoding="utf-8") as handle:
        for row in rows:
            _ = handle.write(json.dumps(row) + "\n")


def _base_row(ts: float, task_qualnames: dict[str, int]) -> dict[str, object]:
    return {
        "ts": ts,
        "rss_bytes": 100,
        "heap_current_bytes": 10,
        "heap_peak_bytes": 10,
        "npc_pending_keys": 0,
        "event_bus_queue": 0,
        "perf_metrics": 0,
        "perf_operation_keys": 0,
        "perf_operation_metrics": 0,
        "log_hour_keys": 0,
        "asyncio_tasks": sum(task_qualnames.values()),
        "task_qualnames": task_qualnames,
    }


def test_script_exists() -> None:
    assert SCRIPT_PATH.is_file()


def test_warmup_defaults_to_module_constant(tmp_path: Path) -> None:
    """Passing no warmup_seconds keeps existing callers' behavior unchanged."""
    mod = _load_script()
    path = tmp_path / "samples.jsonl"
    _write_samples(path, [_base_row(0.0, {"a": 1}), _base_row(60.0, {"a": 1})])
    report = mod.analyze(path)
    assert f"warmup_seconds={mod.WARMUP_SECONDS}" in report


def test_warmup_zero_uses_all_samples_as_measurement(tmp_path: Path) -> None:
    mod = _load_script()
    path = tmp_path / "samples.jsonl"
    _write_samples(path, [_base_row(0.0, {"a": 1}), _base_row(60.0, {"a": 1})])
    report = mod.analyze(path, warmup_seconds=0)
    assert "measure_samples=2" in report
    assert "warmup_samples=0" in report


def test_qualname_delta_names_the_growing_coroutine(tmp_path: Path) -> None:
    """The leaking coroutine's qualname is named with its start/end/delta, sorted first."""
    mod = _load_script()
    path = tmp_path / "samples.jsonl"
    _write_samples(
        path,
        [
            _base_row(0.0, {"steady.task": 2, "leaking.task": 1}),
            _base_row(60.0, {"steady.task": 2, "leaking.task": 6}),
        ],
    )
    report = mod.analyze(path, warmup_seconds=0)
    assert "leaking.task: start=1 end=6 delta=+5" in report
    assert "steady.task" not in report  # unchanged names are not reported


def test_qualname_delta_reports_no_change_when_flat(tmp_path: Path) -> None:
    mod = _load_script()
    path = tmp_path / "samples.jsonl"
    _write_samples(path, [_base_row(0.0, {"a": 3}), _base_row(60.0, {"a": 3})])
    report = mod.analyze(path, warmup_seconds=0)
    assert "task_qualnames: no change" in report
