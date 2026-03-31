"""Regression tests for scripts/dependency_analyzer.py and scripts/utils/dependency_risk.py."""

from __future__ import annotations

import importlib.util
import sys
from collections.abc import Callable, Iterator
from contextlib import contextmanager
from dataclasses import dataclass
from pathlib import Path
from types import ModuleType
from typing import Any, Protocol, cast

import pytest

PROJECT_ROOT = Path(__file__).resolve().parents[4]
SCRIPTS_ROOT = PROJECT_ROOT / "scripts"
RISK_SCRIPT_PATH = SCRIPTS_ROOT / "utils" / "dependency_risk.py"
ANALYZER_SCRIPT_PATH = SCRIPTS_ROOT / "dependency_analyzer.py"


@dataclass(frozen=True, slots=True)
class _FakeCompletedProcess:
    returncode: int
    stdout: str


class _DependencyRiskScriptInternals(Protocol):
    categorize_update: Callable[[str, str], str]
    assess_npm_risk: Callable[[str, str, str], str]
    assess_python_risk: Callable[[str, str, str], str]


class _DependencyAnalyzerScriptInternals(Protocol):
    _dep_info_from_npm_row: Callable[[str, dict[str, object]], dict[str, object]]
    _parse_npm_outdated_json: Callable[[str], dict[str, dict[str, object]]]
    DependencyAnalyzer: type[Any]


@dataclass(frozen=True, slots=True)
class DependencyRiskTestApi:
    categorize_update: Callable[[str, str], str]
    assess_npm_risk: Callable[[str, str, str], str]
    assess_python_risk: Callable[[str, str, str], str]


@dataclass(frozen=True, slots=True)
class DependencyAnalyzerTestApi:
    dep_info_from_npm_row: Callable[[str, dict[str, object]], dict[str, object]]
    parse_npm_outdated_json: Callable[[str], dict[str, dict[str, object]]]
    dependency_analyzer_cls: type[Any]
    module: ModuleType


@contextmanager
def _scripts_path_on_syspath() -> Iterator[None]:
    scripts_root_s = str(SCRIPTS_ROOT)
    added = scripts_root_s not in sys.path
    if added:
        sys.path.insert(0, scripts_root_s)
    try:
        yield
    finally:
        if added:
            sys.path.remove(scripts_root_s)


def _load_dependency_risk_script() -> DependencyRiskTestApi:
    spec = importlib.util.spec_from_file_location("dependency_risk_script_for_tests", RISK_SCRIPT_PATH)
    assert spec is not None and spec.loader is not None
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    loaded = cast(_DependencyRiskScriptInternals, cast(object, mod))
    return DependencyRiskTestApi(
        categorize_update=loaded.categorize_update,
        assess_npm_risk=loaded.assess_npm_risk,
        assess_python_risk=loaded.assess_python_risk,
    )


def _load_dependency_analyzer_script() -> DependencyAnalyzerTestApi:
    with _scripts_path_on_syspath():
        spec = importlib.util.spec_from_file_location("dependency_analyzer_script_for_tests", ANALYZER_SCRIPT_PATH)
        assert spec is not None and spec.loader is not None
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
    loaded = cast(_DependencyAnalyzerScriptInternals, cast(object, mod))
    return DependencyAnalyzerTestApi(
        dep_info_from_npm_row=loaded._dep_info_from_npm_row,  # pyright: ignore[reportPrivateUsage] -- script API
        parse_npm_outdated_json=loaded._parse_npm_outdated_json,  # pyright: ignore[reportPrivateUsage]
        dependency_analyzer_cls=loaded.DependencyAnalyzer,
        module=cast(ModuleType, mod),
    )


@pytest.fixture(scope="module", name="risk_api")
def risk_api_module_scope() -> DependencyRiskTestApi:
    """Load scripts/utils/dependency_risk.py and expose tested helpers."""
    return _load_dependency_risk_script()


@pytest.fixture(scope="module", name="analyzer_api")
def analyzer_api_module_scope() -> DependencyAnalyzerTestApi:
    """Load scripts/dependency_analyzer.py and expose tested helpers."""
    return _load_dependency_analyzer_script()


@pytest.mark.parametrize(
    ("current_version", "latest_version", "expected"),
    [
        ("1.2.3", "2.0.0", "major"),
        ("1.2.3", "1.3.0", "minor"),
        ("1.2.3", "1.2.4", "patch"),
        ("1.2.3", "1.2.3", "none"),
        ("not-a-version", "1.2.3", "unknown"),
    ],
)
def test_categorize_update_handles_semver_and_invalid_input(
    risk_api: DependencyRiskTestApi,
    current_version: str,
    latest_version: str,
    expected: str,
) -> None:
    """categorize_update should classify major/minor/patch/none/unknown consistently."""
    assert risk_api.categorize_update(current_version, latest_version) == expected


def test_assess_npm_risk_uses_update_type_and_package_tiers(risk_api: DependencyRiskTestApi) -> None:
    """NPM risk should follow major > high-risk minor > medium-risk minor > patch/default."""
    assert risk_api.assess_npm_risk("some-lib", "1.0.0", "2.0.0") == "HIGH"
    assert risk_api.assess_npm_risk("react", "18.2.0", "18.3.0") == "MEDIUM"
    assert risk_api.assess_npm_risk("prettier", "3.0.0", "3.1.0") == "LOW"
    assert risk_api.assess_npm_risk("typescript", "5.4.0", "5.4.1") == "LOW"
    assert risk_api.assess_npm_risk("unknown-lib", "bogus", "still-bogus") == "LOW"


def test_assess_python_risk_uses_update_type_and_package_tiers(risk_api: DependencyRiskTestApi) -> None:
    """Python risk should follow major > high-risk minor > medium-risk minor > patch/default."""
    assert risk_api.assess_python_risk("some-lib", "1.0.0", "2.0.0") == "HIGH"
    assert risk_api.assess_python_risk("fastapi", "0.109.0", "0.110.0") == "MEDIUM"
    assert risk_api.assess_python_risk("click", "8.1.0", "8.2.0") == "LOW"
    assert risk_api.assess_python_risk("pytest", "8.1.0", "8.1.1") == "LOW"
    assert risk_api.assess_python_risk("unknown-lib", "bogus", "still-bogus") == "LOW"


def test_dep_info_from_npm_row_coerces_types_and_applies_defaults(analyzer_api: DependencyAnalyzerTestApi) -> None:
    """_dep_info_from_npm_row should normalize row values and include computed fields."""
    dep = analyzer_api.dep_info_from_npm_row(
        "react",
        {
            "current": 1,
            "latest": "2.0.0",
        },
    )

    assert dep["current"] == "1"
    assert dep["wanted"] == "1"
    assert dep["latest"] == "2.0.0"
    assert dep["type"] == "dependencies"
    assert dep["ecosystem"] == "npm"
    assert dep["update_type"] == "major"
    assert dep["risk_level"] == "HIGH"


def test_parse_npm_outdated_json_handles_non_object_and_valid_payload(
    analyzer_api: DependencyAnalyzerTestApi,
) -> None:
    """_parse_npm_outdated_json should return empty for non-object JSON and parse valid dict rows."""
    assert analyzer_api.parse_npm_outdated_json("[]") == {}

    parsed = analyzer_api.parse_npm_outdated_json(
        """
        {
          "vite": {"current": "5.0.0", "wanted": "5.1.0", "latest": "6.0.0", "type": "devDependencies"},
          "prettier": {"current": "3.0.0", "latest": "3.1.0"}
        }
        """
    )
    assert parsed["vite"]["update_type"] == "major"
    assert parsed["vite"]["risk_level"] == "HIGH"
    assert parsed["prettier"]["wanted"] == "3.0.0"
    assert parsed["prettier"]["risk_level"] == "LOW"


def test_analyze_npm_dependencies_parses_stdout_from_expected_outdated_exit_code(
    analyzer_api: DependencyAnalyzerTestApi,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    """_analyze_npm_dependencies should parse npm outdated JSON when return code is non-zero with stdout."""

    def fake_safe_run_static(*args: object, **kwargs: object) -> _FakeCompletedProcess:
        assert args == ("npm", "outdated", "--json")
        assert kwargs["cwd"] == PROJECT_ROOT / "client"
        assert kwargs["capture_output"] is True
        assert kwargs["text"] is True
        assert kwargs["check"] is False
        return _FakeCompletedProcess(
            returncode=1,
            stdout='{"react":{"current":"18.2.0","wanted":"18.3.0","latest":"19.0.0","type":"dependencies"}}',
        )

    monkeypatch.setattr(analyzer_api.module, "safe_run_static", fake_safe_run_static)
    analyzer = analyzer_api.dependency_analyzer_cls(PROJECT_ROOT)
    result = analyzer._analyze_npm_dependencies()  # pyright: ignore[reportPrivateUsage] -- script API

    assert result["react"]["update_type"] == "major"
    assert result["react"]["risk_level"] == "HIGH"


def test_analyze_python_dependencies_parses_outdated_table_output(
    analyzer_api: DependencyAnalyzerTestApi,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    """_analyze_python_dependencies should parse uv table output and compute risk and update type."""

    def fake_safe_run_static(*args: object, **kwargs: object) -> _FakeCompletedProcess:
        assert args == ("uv", "pip", "list", "--outdated")
        assert kwargs["cwd"] == PROJECT_ROOT
        return _FakeCompletedProcess(
            returncode=0,
            stdout=(
                "Package Version Latest Type\n"
                "------- ------- ------ ----\n"
                "fastapi 0.109.0 0.110.0 wheel\n"
                "click 8.1.0 8.2.0 wheel\n"
                "broken-line-without-columns\n"
            ),
        )

    monkeypatch.setattr(analyzer_api.module, "safe_run_static", fake_safe_run_static)
    analyzer = analyzer_api.dependency_analyzer_cls(PROJECT_ROOT)
    result = analyzer._analyze_python_dependencies()  # pyright: ignore[reportPrivateUsage] -- script API

    assert set(result) == {"fastapi", "click"}
    assert result["fastapi"]["ecosystem"] == "pip"
    assert result["fastapi"]["update_type"] == "minor"
    assert result["fastapi"]["risk_level"] == "MEDIUM"
    assert result["click"]["risk_level"] == "LOW"


def test_determine_strategy_covers_incremental_batched_and_immediate_paths(
    analyzer_api: DependencyAnalyzerTestApi,
) -> None:
    """_determine_strategy should prioritize major updates, then minor volume, else immediate."""
    analyzer = analyzer_api.dependency_analyzer_cls(PROJECT_ROOT)

    incremental = analyzer._determine_strategy(  # pyright: ignore[reportPrivateUsage] -- script API
        {"react": {"current": "1", "latest": "2", "ecosystem": "npm", "update_type": "major", "risk_level": "HIGH"}},
        {},
    )
    assert incremental["strategy"] == "INCREMENTAL"
    assert incremental["priority"] == "HIGH"
    assert incremental["update_counts"]["major"] == 1
    assert incremental["risk_counts"]["HIGH"] == 1
    assert incremental["total_packages"] == 1

    batched = analyzer._determine_strategy(  # pyright: ignore[reportPrivateUsage] -- script API
        {
            "a": {"current": "1", "latest": "1.1", "ecosystem": "npm", "update_type": "minor", "risk_level": "LOW"},
            "b": {"current": "1", "latest": "1.1", "ecosystem": "npm", "update_type": "minor", "risk_level": "LOW"},
        },
        {
            "c": {"current": "1", "latest": "1.1", "ecosystem": "pip", "update_type": "minor", "risk_level": "LOW"},
            "d": {"current": "1", "latest": "1.1", "ecosystem": "pip", "update_type": "minor", "risk_level": "LOW"},
        },
    )
    assert batched["strategy"] == "BATCHED"
    assert batched["priority"] == "MEDIUM"
    assert batched["update_counts"]["minor"] == 4

    immediate = analyzer._determine_strategy(  # pyright: ignore[reportPrivateUsage] -- script API
        {"x": {"current": "1.0.0", "latest": "1.0.1", "ecosystem": "npm", "update_type": "patch", "risk_level": "LOW"}},
        {},
    )
    assert immediate["strategy"] == "IMMEDIATE"
    assert immediate["priority"] == "LOW"


def test_assess_risks_maps_breaking_change_counts_to_overall_risk(analyzer_api: DependencyAnalyzerTestApi) -> None:
    """_assess_risks should produce LOW/MEDIUM/HIGH based on number of major upgrades."""
    analyzer = analyzer_api.dependency_analyzer_cls(PROJECT_ROOT)

    low = analyzer._assess_risks(  # pyright: ignore[reportPrivateUsage] -- script API
        {
            "patch-lib": {
                "current": "1.0.0",
                "latest": "1.0.1",
                "ecosystem": "npm",
                "update_type": "patch",
                "risk_level": "LOW",
            }
        },
        {},
    )
    assert low["overall_risk"] == "LOW"
    assert low["breaking_changes"] == []

    medium = analyzer._assess_risks(  # pyright: ignore[reportPrivateUsage] -- script API
        {
            "major-lib": {
                "current": "1.0.0",
                "latest": "2.0.0",
                "ecosystem": "npm",
                "update_type": "major",
                "risk_level": "HIGH",
            }
        },
        {},
    )
    assert medium["overall_risk"] == "MEDIUM"
    assert len(medium["breaking_changes"]) == 1
    assert medium["breaking_changes"][0]["package"] == "major-lib"

    high = analyzer._assess_risks(  # pyright: ignore[reportPrivateUsage] -- script API
        {
            "m1": {"current": "1", "latest": "2", "ecosystem": "npm", "update_type": "major", "risk_level": "HIGH"},
            "m2": {"current": "1", "latest": "2", "ecosystem": "npm", "update_type": "major", "risk_level": "HIGH"},
        },
        {
            "m3": {"current": "1", "latest": "2", "ecosystem": "pip", "update_type": "major", "risk_level": "HIGH"},
        },
    )
    assert high["overall_risk"] == "HIGH"
    assert len(high["breaking_changes"]) == 3


def test_prioritize_updates_scores_and_sorts_descending(analyzer_api: DependencyAnalyzerTestApi) -> None:
    """_prioritize_updates should compute expected scores and return highest-priority items first."""
    analyzer = analyzer_api.dependency_analyzer_cls(PROJECT_ROOT)

    ranked = analyzer._prioritize_updates(  # pyright: ignore[reportPrivateUsage] -- script API
        {
            "major-high": {
                "current": "1.0.0",
                "latest": "2.0.0",
                "ecosystem": "npm",
                "update_type": "major",
                "risk_level": "HIGH",
            },
            "minor-medium": {
                "current": "1.0.0",
                "latest": "1.1.0",
                "ecosystem": "npm",
                "update_type": "minor",
                "risk_level": "MEDIUM",
            },
        },
        {
            "major-low": {
                "current": "1.0.0",
                "latest": "2.0.0",
                "ecosystem": "pip",
                "update_type": "major",
                "risk_level": "LOW",
            },
            "patch-high": {
                "current": "1.0.0",
                "latest": "1.0.1",
                "ecosystem": "pip",
                "update_type": "patch",
                "risk_level": "HIGH",
            },
        },
    )

    assert [item["package"] for item in ranked] == ["major-high", "major-low", "minor-medium", "patch-high"]
    assert ranked[0]["priority_score"] == 120
    assert ranked[1]["priority_score"] == 100
    assert ranked[2]["priority_score"] == 60
    assert ranked[3]["priority_score"] == 30
