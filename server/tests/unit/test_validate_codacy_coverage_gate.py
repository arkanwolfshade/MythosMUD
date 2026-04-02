"""Tests for scripts/validate_codacy_coverage_gate.py (Codacy upload quality gate)."""

from __future__ import annotations

import importlib.util
from collections.abc import Callable
from pathlib import Path
from typing import Protocol, cast

import pytest

_REPO_ROOT = Path(__file__).resolve().parents[3]


class _CodacyGateModule(Protocol):
    """Public surface of validate_codacy_coverage_gate loaded via importlib."""

    cobertura_root_line_rate: Callable[[Path], float]
    validate_python_gate: Callable[[Path, float], None]
    lcov_aggregate_hits: Callable[[Path], tuple[int, int]]
    validate_lcov_gate: Callable[[Path, float], None]


def _load_gate_module() -> _CodacyGateModule:
    path = _REPO_ROOT / "scripts" / "validate_codacy_coverage_gate.py"
    spec = importlib.util.spec_from_file_location("_validate_codacy_coverage_gate", path)
    assert spec and spec.loader
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    # importlib yields ModuleType; narrow to our Protocol via object (basedpyright).
    return cast(_CodacyGateModule, cast(object, mod))


_gate = _load_gate_module()


def test_cobertura_root_line_rate_parses(tmp_path: Path) -> None:
    xml = tmp_path / "coverage.xml"
    _ = xml.write_text(
        '<?xml version="1.0" ?><coverage line-rate="0.82" version="1">'
        + "<packages><package><classes>"
        + '<class filename="server/app.py" line-rate="1.0" name="x">'
        + "<methods/><lines/></class>"
        + "</classes></package></packages></coverage>",
        encoding="utf-8",
    )
    assert abs(_gate.cobertura_root_line_rate(xml) - 0.82) < 1e-9


def test_validate_python_gate_passes(tmp_path: Path) -> None:
    xml = tmp_path / "coverage.xml"
    _ = xml.write_text(
        '<?xml version="1.0" ?><coverage line-rate="0.90" version="1">'
        + "<packages><package><classes>"
        + '<class filename="server/app.py" line-rate="1.0" name="x">'
        + "<methods/><lines/></class>"
        + "</classes></package></packages></coverage>",
        encoding="utf-8",
    )
    _gate.validate_python_gate(xml, 0.63)


def test_validate_python_gate_fails_low_aggregate(tmp_path: Path) -> None:
    xml = tmp_path / "coverage.xml"
    _ = xml.write_text(
        '<?xml version="1.0" ?><coverage line-rate="0.50" version="1">'
        + "<packages><package><classes>"
        + '<class filename="server/app.py" line-rate="1.0" name="x">'
        + "<methods/><lines/></class>"
        + "</classes></package></packages></coverage>",
        encoding="utf-8",
    )
    with pytest.raises(ValueError, match="below gate"):
        _gate.validate_python_gate(xml, 0.63)


def test_validate_python_gate_fails_no_server_paths(tmp_path: Path) -> None:
    xml = tmp_path / "coverage.xml"
    _ = xml.write_text(
        '<?xml version="1.0" ?><coverage line-rate="0.90" version="1">'
        + "<packages><package><classes>"
        + '<class filename="other/app.py" line-rate="1.0" name="x">'
        + "<methods/><lines/></class>"
        + "</classes></package></packages></coverage>",
        encoding="utf-8",
    )
    with pytest.raises(ValueError, match="No server/"):
        _gate.validate_python_gate(xml, 0.63)


def test_lcov_aggregate_and_gate(tmp_path: Path) -> None:
    lcov = tmp_path / "lcov.info"
    _ = lcov.write_text(
        "TN:\nSF:src/App.tsx\nLF:100\nLH:80\nend_of_record\n",
        encoding="utf-8",
    )
    lh, lf = _gate.lcov_aggregate_hits(lcov)
    assert lh == 80
    assert lf == 100
    _gate.validate_lcov_gate(lcov, 0.70)


def test_validate_lcov_gate_fails(tmp_path: Path) -> None:
    lcov = tmp_path / "lcov.info"
    _ = lcov.write_text(
        "TN:\nSF:src/App.tsx\nLF:100\nLH:50\nend_of_record\n",
        encoding="utf-8",
    )
    with pytest.raises(ValueError, match="below gate"):
        _gate.validate_lcov_gate(lcov, 0.70)
