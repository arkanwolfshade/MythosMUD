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


def _load_guard_module() -> _QualityGuardModule:
    path = _REPO_ROOT / "scripts" / "ci" / "quality_fragmentation_guard.py"
    spec = importlib.util.spec_from_file_location("_quality_fragmentation_guard", path)
    assert spec and spec.loader
    mod = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = mod
    spec.loader.exec_module(mod)
    return cast(_QualityGuardModule, cast(object, mod))


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

    scan_changed_files(changed, [], [], failures)

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

    scan_changed_files(changed, [], [], failures)

    assert any("single-use and small" in failure for failure in failures)
