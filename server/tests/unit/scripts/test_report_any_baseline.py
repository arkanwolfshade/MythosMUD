"""Tests for scripts/report_any_baseline.py (#784).

This script is the burn-down chart's reader. The counts it prints decide which subsystem gets
worked next, so the grouping and the four-rule total are the behaviour worth pinning.
"""

from __future__ import annotations

import importlib.util
import json
import sys
from collections.abc import Callable
from dataclasses import dataclass
from pathlib import Path
from typing import Protocol, cast

import pytest

PROJECT_ROOT = Path(__file__).resolve().parents[4]
SCRIPT_PATH = PROJECT_ROOT / "scripts" / "report_any_baseline.py"


class _ReportModule(Protocol):
    """Public surface of scripts/report_any_baseline.py used by these tests."""

    main: Callable[[], None]
    BURN_DOWN_RULES: tuple[str, ...]


@dataclass(frozen=True, slots=True)
class ReportTestApi:
    """Typed facade over the dynamically imported script."""

    main: Callable[[], None]
    burn_down_rules: tuple[str, ...]


def _load_script_module() -> ReportTestApi:
    module_name = "report_any_baseline_script"
    spec = importlib.util.spec_from_file_location(module_name, SCRIPT_PATH)
    assert spec is not None and spec.loader is not None
    mod = importlib.util.module_from_spec(spec)
    sys.modules[module_name] = mod
    spec.loader.exec_module(mod)
    loaded = cast(_ReportModule, cast(object, mod))
    return ReportTestApi(main=loaded.main, burn_down_rules=tuple(loaded.BURN_DOWN_RULES))


@pytest.fixture(scope="module", name="report_api")
def report_api_module_scope() -> ReportTestApi:
    return _load_script_module()


def _write_baseline(root: Path, files: dict[str, list[str]]) -> None:
    """Build a baseline.json whose entries carry the given rule codes."""
    payload = {
        "files": {
            path: [{"code": code, "range": {"startColumn": 1, "endColumn": 2, "lineCount": 1}} for code in codes]
            for path, codes in files.items()
        }
    }
    baseline_dir = root / ".basedpyright"
    baseline_dir.mkdir(parents=True, exist_ok=True)
    _ = (baseline_dir / "baseline.json").write_text(json.dumps(payload), encoding="utf-8")


def test_missing_baseline_exits_with_guidance(
    report_api: ReportTestApi, tmp_path: Path, monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]
) -> None:
    monkeypatch.chdir(tmp_path)
    with pytest.raises(SystemExit) as excinfo:
        report_api.main()
    assert excinfo.value.code == 1
    assert "--writebaseline" in capsys.readouterr().err


def test_counts_the_four_burn_down_rules(
    report_api: ReportTestApi, tmp_path: Path, monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]
) -> None:
    _write_baseline(
        tmp_path,
        {
            "./server/commands/a.py": ["reportAny", "reportExplicitAny", "reportPrivateUsage"],
            "./server/commands/b.py": ["reportMissingParameterType", "reportUnknownParameterType"],
        },
    )
    monkeypatch.chdir(tmp_path)
    report_api.main()
    out = capsys.readouterr().out
    assert "baselined diagnostics : 5" in out
    # reportPrivateUsage is baselined and gated, but is not part of the burn-down commitment.
    assert "burn-down four-rule   : 4" in out


def test_groups_by_directory_not_by_file(
    report_api: ReportTestApi, tmp_path: Path, monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]
) -> None:
    _write_baseline(
        tmp_path,
        {
            "./server/commands/a.py": ["reportAny"],
            "./server/commands/b.py": ["reportAny"],
            "./server/realtime/c.py": ["reportAny"],
        },
    )
    monkeypatch.chdir(tmp_path)
    report_api.main()
    out = capsys.readouterr().out
    assert "2  server/commands" in out
    assert "1  server/realtime" in out


def test_non_burn_down_rules_are_listed_but_excluded_from_the_total(
    report_api: ReportTestApi, tmp_path: Path, monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]
) -> None:
    _write_baseline(tmp_path, {"./server/models/p.py": ["reportUnannotatedClassAttribute"] * 3})
    monkeypatch.chdir(tmp_path)
    report_api.main()
    out = capsys.readouterr().out
    assert "burn-down four-rule   : 0" in out
    assert "3  reportUnannotatedClassAttribute" in out


def test_burn_down_rules_cover_implicit_any(report_api: ReportTestApi) -> None:
    """The two parameter rules close the laundering path; dropping them re-opens it."""
    assert set(report_api.burn_down_rules) == {
        "reportAny",
        "reportExplicitAny",
        "reportMissingParameterType",
        "reportUnknownParameterType",
    }
