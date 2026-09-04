"""Unit tests for scripts/check_coverage_thresholds.py.

Covers `check_thresholds`' three threshold sources: a critical file's own (high) floor, the
blanket 70% normal floor, and the `KNOWN_COVERAGE_DEBT` allowlist added in #677 -- which lowers
either kind of floor to the coverage measured when the #668 pipefail fix unmasked this check's
long-silent failures. See #677 for the debt-paydown tracking issue this allowlist exists to serve.
"""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path
from typing import Protocol, cast

PROJECT_ROOT = Path(__file__).resolve().parents[4]
SCRIPT_PATH = PROJECT_ROOT / "scripts" / "check_coverage_thresholds.py"


class _CheckCoverageThresholdsModule(Protocol):
    """Typed surface of the loaded script, for the parts these tests exercise."""

    def check_thresholds(self, file_coverage: dict[str, float]) -> list[str]: ...

    CRITICAL_FILES: dict[str, int]
    KNOWN_COVERAGE_DEBT: dict[str, int]
    NORMAL_THRESHOLD: int


def _load_script() -> _CheckCoverageThresholdsModule:
    spec = importlib.util.spec_from_file_location("check_coverage_thresholds_for_tests", SCRIPT_PATH)
    assert spec is not None
    assert spec.loader is not None
    mod = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = mod
    spec.loader.exec_module(mod)
    return cast(_CheckCoverageThresholdsModule, cast(object, mod))


def _fully_covered(mod: _CheckCoverageThresholdsModule) -> dict[str, float]:
    """check_thresholds evaluates every CRITICAL_FILES entry regardless of what's passed in --
    files missing from the coverage dict report as 0% failures of their own. Start from a dict
    where every critical file is at 100% so a test can isolate just the one file it cares about."""
    return dict.fromkeys(mod.CRITICAL_FILES, 100.0)


def test_script_exists() -> None:
    assert SCRIPT_PATH.is_file()


def test_critical_file_below_its_own_threshold_fails() -> None:
    mod = _load_script()
    # server/database.py: a CRITICAL_FILES entry with no KNOWN_COVERAGE_DEBT override -- its
    # threshold must stay at the value declared in CRITICAL_FILES (90).
    failures = mod.check_thresholds({"server/database.py": 89.99})
    assert any("server/database.py has 89.99% coverage, requires 90%" in f for f in failures)


def test_critical_file_at_its_own_threshold_passes() -> None:
    mod = _load_script()
    failures = mod.check_thresholds({"server/database.py": 90.0})
    assert not any("server/database.py" in f for f in failures)


def test_normal_file_below_blanket_threshold_fails() -> None:
    mod = _load_script()
    failures = mod.check_thresholds({"server/services/some_uncovered_service.py": 69.99})
    assert any("requires 70%" in f for f in failures)


def test_normal_file_at_blanket_threshold_passes() -> None:
    mod = _load_script()
    coverage = _fully_covered(mod)
    coverage["server/services/some_service.py"] = 70.0
    failures = mod.check_thresholds(coverage)
    assert failures == []


def test_test_files_are_never_checked() -> None:
    mod = _load_script()
    coverage = _fully_covered(mod)
    coverage["server/tests/unit/test_something.py"] = 0.0
    failures = mod.check_thresholds(coverage)
    assert failures == []


def test_known_coverage_debt_is_empty() -> None:
    """#677 paid down every entry that was in KNOWN_COVERAGE_DEBT -- it should stay empty until a
    new regression is discovered and deliberately floored, not silently re-accumulate debt."""
    mod = _load_script()
    assert mod.KNOWN_COVERAGE_DEBT == {}


def test_known_coverage_debt_lowers_a_critical_files_floor() -> None:
    """A KNOWN_COVERAGE_DEBT entry lowers a CRITICAL_FILES floor, not just replaces it (#677)."""
    mod = _load_script()
    path = "server/database.py"  # a real CRITICAL_FILES entry (90%)
    debt_floor = mod.CRITICAL_FILES[path] - 10
    mod.KNOWN_COVERAGE_DEBT[path] = debt_floor

    # Just above the debt floor, below the original 90% -- must pass, not fail.
    coverage = _fully_covered(mod)
    coverage[path] = debt_floor + 0.5
    failures = mod.check_thresholds(coverage)
    assert failures == []

    # Just below the debt floor -- must still fail, at the debt floor's number, not 90.
    coverage[path] = debt_floor - 0.5
    failures = mod.check_thresholds(coverage)
    assert failures == [f"CRITICAL: {path} has {debt_floor - 0.5:.2f}% coverage, requires {debt_floor}%"]


def test_known_coverage_debt_lowers_a_normal_files_floor() -> None:
    """A KNOWN_COVERAGE_DEBT entry lowers the blanket 70% normal-file floor (#677)."""
    mod = _load_script()
    path = "server/services/some_debt_carrying_service.py"  # no CRITICAL_FILES entry -- blanket 70% applies
    debt_floor = mod.NORMAL_THRESHOLD - 10
    mod.KNOWN_COVERAGE_DEBT[path] = debt_floor

    coverage = _fully_covered(mod)
    coverage[path] = debt_floor + 0.5
    failures = mod.check_thresholds(coverage)
    assert failures == []

    coverage[path] = debt_floor - 0.5
    failures = mod.check_thresholds(coverage)
    assert failures == [f"NORMAL: {path} has {debt_floor - 0.5:.2f}% coverage, requires {debt_floor}%"]


def test_missing_file_is_treated_as_zero_coverage() -> None:
    """A file present in CRITICAL_FILES but absent from the coverage.xml data (e.g. excluded by
    coverage config) must be treated as 0% -- not silently skipped."""
    mod = _load_script()
    failures = mod.check_thresholds({})
    assert any("server/database.py has 0.00% coverage" in f for f in failures)
