# pyright: reportPrivateUsage=false
"""Regression tests for scripts/ci/quality_fragmentation_guard.py."""

from __future__ import annotations

import importlib.util
import sys
from collections.abc import Callable
from pathlib import Path
from typing import Protocol, cast

_REPO_ROOT = Path(__file__).resolve().parents[3]


class _ChangedFile(Protocol):
    status: str
    old_path: str | None
    path: str


class _QualityGuardModule(Protocol):
    REPO_ROOT: Path
    ChangedFile: object
    collect_repo_texts: object
    _scan_changed_files: object
    is_safe_git_ref: object
    _parse_lizard_output: object


class _QualityTrendsModule(Protocol):
    append_rule_b_failure: object


def _load_guard_module() -> _QualityGuardModule:
    path = _REPO_ROOT / "scripts" / "ci" / "quality_fragmentation_guard.py"
    spec = importlib.util.spec_from_file_location("_quality_fragmentation_guard", path)
    assert spec and spec.loader
    mod = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = mod
    spec.loader.exec_module(mod)
    return cast(_QualityGuardModule, cast(object, mod))


def _load_trends_module() -> _QualityTrendsModule:
    path = _REPO_ROOT / "scripts" / "ci" / "quality_fragmentation_trends.py"
    spec = importlib.util.spec_from_file_location("_quality_fragmentation_trends", path)
    assert spec and spec.loader
    mod = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = mod
    spec.loader.exec_module(mod)
    return cast(_QualityTrendsModule, cast(object, mod))


def test_scan_changed_files_skips_single_use_for_test_file(tmp_path: Path) -> None:
    guard = _load_guard_module()
    test_file = tmp_path / "server" / "tests" / "unit" / "test_example.py"
    test_file.parent.mkdir(parents=True, exist_ok=True)
    _ = test_file.write_text("def helper():\n    return 1\n", encoding="utf-8")
    guard.REPO_ROOT = tmp_path
    failures: list[str] = []
    changed_file_ctor = cast(Callable[[str, str | None, str], _ChangedFile], guard.ChangedFile)
    changed = [changed_file_ctor("A", None, "server/tests/unit/test_example.py")]
    scan_changed_files = cast(
        Callable[
            [list[_ChangedFile], list[tuple[str, str]], list[tuple[str, str]], list[str]],
            tuple[dict[str, int], list[float], int, int],
        ],
        guard._scan_changed_files,
    )

    _ = scan_changed_files(changed, [], [], failures)

    assert failures == []


def test_scan_changed_files_flags_single_use_for_non_test_file(tmp_path: Path) -> None:
    guard = _load_guard_module()
    code_file = tmp_path / "server" / "commands" / "new_helper.py"
    code_file.parent.mkdir(parents=True, exist_ok=True)
    _ = code_file.write_text("def helper():\n    return 1\n", encoding="utf-8")
    guard.REPO_ROOT = tmp_path
    failures: list[str] = []
    changed_file_ctor = cast(Callable[[str, str | None, str], _ChangedFile], guard.ChangedFile)
    changed = [changed_file_ctor("A", None, "server/commands/new_helper.py")]
    scan_changed_files = cast(
        Callable[
            [list[_ChangedFile], list[tuple[str, str]], list[tuple[str, str]], list[str]],
            tuple[dict[str, int], list[float], int, int],
        ],
        guard._scan_changed_files,
    )

    _ = scan_changed_files(changed, [], [], failures)

    assert any("single-use and small" in failure for failure in failures)


def test_scan_changed_files_skips_single_use_for_grouped_file(tmp_path: Path) -> None:
    guard = _load_guard_module()
    code_file = tmp_path / "server" / "commands" / "grouped_helper.py"
    code_file.parent.mkdir(parents=True, exist_ok=True)
    _ = code_file.write_text(
        '"""group: inventory_container_helpers"""\n\ndef helper():\n    return 1\n', encoding="utf-8"
    )
    guard.REPO_ROOT = tmp_path
    failures: list[str] = []
    changed_file_ctor = cast(Callable[[str, str | None, str], _ChangedFile], guard.ChangedFile)
    changed = [changed_file_ctor("A", None, "server/commands/grouped_helper.py")]
    scan_changed_files = cast(
        Callable[
            [list[_ChangedFile], list[tuple[str, str]], list[tuple[str, str]], list[str]],
            tuple[dict[str, int], list[float], int, int],
        ],
        guard._scan_changed_files,
    )

    _ = scan_changed_files(changed, [], [], failures)

    assert not any("single-use and small" in failure for failure in failures)


def test_scan_changed_files_flags_tiny_single_use_function(tmp_path: Path) -> None:
    guard = _load_guard_module()
    code_file = tmp_path / "server" / "commands" / "tiny_rule_a.py"
    code_file.parent.mkdir(parents=True, exist_ok=True)
    _ = code_file.write_text("def tiny():\n    return 1\n", encoding="utf-8")
    guard.REPO_ROOT = tmp_path
    failures: list[str] = []
    changed_file_ctor = cast(Callable[[str, str | None, str], _ChangedFile], guard.ChangedFile)
    changed = [changed_file_ctor("A", None, "server/commands/tiny_rule_a.py")]
    scan_changed_files = cast(
        Callable[
            [list[_ChangedFile], list[tuple[str, str]], list[tuple[str, str]], list[str]],
            tuple[dict[str, int], list[float], int, int],
        ],
        guard._scan_changed_files,
    )

    _ = scan_changed_files(changed, [], [], failures)

    assert any("tiny single-use function" in failure for failure in failures)


def test_append_rule_b_failure_for_fragmentation_limit() -> None:
    trends = _load_trends_module()
    append_rule_b_failure = cast(Callable[[list[str], int, float], None], trends.append_rule_b_failure)
    failures: list[str] = []

    append_rule_b_failure(failures, 11, 49.0)

    assert failures == ["Rule B violation: new_files=11, avg_new_file_length=49.00 (<50)."]


def test_is_safe_git_ref_accepts_sha_and_branch_like_ref() -> None:
    guard = _load_guard_module()
    is_safe_git_ref = cast(Callable[[str], bool], guard.is_safe_git_ref)

    assert is_safe_git_ref("4b923c4ea016bddb7da5f97d4236ed1b2241e982")
    assert is_safe_git_ref("chore/codacy")


def test_is_safe_git_ref_rejects_suspicious_values() -> None:
    guard = _load_guard_module()
    is_safe_git_ref = cast(Callable[[str], bool], guard.is_safe_git_ref)

    assert not is_safe_git_ref("main..HEAD")
    assert not is_safe_git_ref("$(whoami)")


def test_collect_repo_texts_reports_unreadable_files(tmp_path: Path) -> None:
    guard = _load_guard_module()
    good = tmp_path / "ok.py"
    _ = good.write_text("x = 1\n", encoding="utf-8")
    bad = tmp_path / "bad.py"
    _ = bad.write_bytes(b"\xff")
    guard.REPO_ROOT = tmp_path

    collect_repo_texts = cast(Callable[[str], tuple[list[tuple[str, str]], int]], guard.collect_repo_texts)
    texts, read_errors = collect_repo_texts(".py")

    assert any(path == "ok.py" for path, _text in texts)
    assert read_errors == 1


def test_parse_lizard_output_maps_function_nodes() -> None:
    guard = _load_guard_module()
    parse_lizard_output = cast(Callable[[str], list[dict[str, object]]], guard._parse_lizard_output)
    payload = (
        '[{"function_list":[{"name":"fn_a","nloc":12,"cyclomatic_complexity":3,"parameter_count":2,"start_line":9}]}]'
    )

    rows = parse_lizard_output(payload)

    assert rows == [{"name": "fn_a", "nloc": 12, "ccn": 3, "params": 2, "start_line": 9}]
