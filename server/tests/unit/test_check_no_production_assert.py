"""Tests for scripts/check_no_production_assert.py."""

from __future__ import annotations

import importlib.util
import re
import subprocess
import sys
from collections.abc import Callable
from pathlib import Path
from typing import Protocol, cast

_REPO_ROOT = Path(__file__).resolve().parents[3]


class _NoProductionAssertModule(Protocol):
    """Public surface of check_no_production_assert loaded via importlib."""

    is_production_server_py: Callable[[Path], bool]
    find_assert_line_numbers: Callable[[Path], list[int]]


def _load_checker() -> _NoProductionAssertModule:
    path = _REPO_ROOT / "scripts" / "check_no_production_assert.py"
    spec = importlib.util.spec_from_file_location("_check_no_production_assert", path)
    assert spec and spec.loader
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    # ModuleType does not overlap Protocol; cast via object for importlib-loaded modules.
    return cast(_NoProductionAssertModule, cast(object, mod))


_checker = _load_checker()


def test_is_production_server_py_true_for_commands(tmp_path: Path) -> None:
    f = tmp_path / "server" / "commands" / "x.py"
    f.parent.mkdir(parents=True)
    _ = f.write_text("x = 1\n", encoding="utf-8")
    assert _checker.is_production_server_py(f) is True


def test_is_production_server_py_false_for_tests(tmp_path: Path) -> None:
    f = tmp_path / "server" / "tests" / "unit" / "foo.py"
    f.parent.mkdir(parents=True)
    _ = f.write_text("x = 1\n", encoding="utf-8")
    assert _checker.is_production_server_py(f) is False


def test_is_production_server_py_false_for_test_named_module(tmp_path: Path) -> None:
    f = tmp_path / "server" / "foo" / "test_bar.py"
    f.parent.mkdir(parents=True)
    _ = f.write_text("x = 1\n", encoding="utf-8")
    assert _checker.is_production_server_py(f) is False


def test_find_assert_line_numbers_detects_assert(tmp_path: Path) -> None:
    f = tmp_path / "a.py"
    _ = f.write_text("def f():\n    assert False\n", encoding="utf-8")
    assert _checker.find_assert_line_numbers(f) == [2]


def test_find_assert_line_numbers_empty_when_no_assert(tmp_path: Path) -> None:
    f = tmp_path / "b.py"
    _ = f.write_text("x = 1\n", encoding="utf-8")
    assert _checker.find_assert_line_numbers(f) == []


def test_script_exits_1_on_production_file_with_assert(tmp_path: Path) -> None:
    prod = tmp_path / "server" / "z.py"
    prod.parent.mkdir(parents=True)
    _ = prod.write_text("assert 1\n", encoding="utf-8")
    script = _REPO_ROOT / "scripts" / "check_no_production_assert.py"
    r = subprocess.run(
        [sys.executable, str(script), str(prod)],
        cwd=str(tmp_path),
        capture_output=True,
        text=True,
        check=False,
    )
    assert r.returncode == 1
    assert "ASSERT IN PRODUCTION" in (r.stderr or "")


def test_script_exits_0_on_test_file_with_assert(tmp_path: Path) -> None:
    t = tmp_path / "server" / "tests" / "t.py"
    t.parent.mkdir(parents=True)
    _ = t.write_text("assert 1\n", encoding="utf-8")
    script = _REPO_ROOT / "scripts" / "check_no_production_assert.py"
    r = subprocess.run(
        [sys.executable, str(script), str(t)],
        cwd=str(tmp_path),
        capture_output=True,
        text=True,
        check=False,
    )
    assert r.returncode == 0


def test_pre_commit_no_production_assert_hook_patterns_match_expected_paths() -> None:
    """Verify no-production-assert hook targets server code and excludes tests."""
    pre_commit = _REPO_ROOT / ".pre-commit-config.yaml"
    text = pre_commit.read_text(encoding="utf-8")

    block_match = re.search(r"- id: no-production-assert(?P<body>.*?)(?:\n\s*-\sid:|\Z)", text, re.DOTALL)
    assert block_match is not None
    body = block_match.group("body")

    files_match = re.search(r"^\s*files:\s*(?P<files>.+)$", body, re.MULTILINE)
    exclude_match = re.search(r"^\s*exclude:\s*(?P<exclude>.+)$", body, re.MULTILINE)
    assert files_match is not None
    assert exclude_match is not None

    files_re = re.compile(files_match.group("files").strip())
    exclude_re = re.compile(exclude_match.group("exclude").strip())

    production_path = "server/commands/inventory_commands.py"
    test_path = "server/tests/unit/test_inventory_commands.py"
    non_server_path = "client/src/App.tsx"

    assert files_re.search(production_path)
    assert not exclude_re.search(production_path)
    assert files_re.search(test_path)
    assert exclude_re.search(test_path)
    assert not files_re.search(non_server_path)
