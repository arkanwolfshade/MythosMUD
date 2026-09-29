"""Tests for scripts/test_runner.py CLI parsing (typed argparse namespace).

scripts/test_runner.py configures structlog globally at import time, so it is driven in a
subprocess (never imported into the pytest process). TestRunner is swapped for a recorder,
so no tests are actually launched.
"""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path
from typing import cast

import pytest

PROJECT_ROOT = Path(__file__).resolve().parents[4]
SCRIPTS_ROOT = PROJECT_ROOT / "scripts"

_DRIVER = """
import json, os, sys
# Mirror `python scripts/test_runner.py`: the script's dir is on sys.path, the cwd is not
# (with -c the cwd is, and server/utils would shadow scripts/utils).
sys.path[:] = [p for p in sys.path if p not in ("", os.getcwd())]
sys.path.insert(0, sys.argv[1])
import test_runner

calls = []

class Recorder:
    def __init__(self, project_root):
        calls.append(["init", str(project_root)])
    def run_unit_tests(self, extra):
        calls.append(["unit", extra]); return 0
    def run_integration_tests(self, extra):
        calls.append(["integration", extra]); return 0
    def run_e2e_tests(self, extra):
        calls.append(["e2e", extra]); return 0
    def run_coverage_report(self):
        calls.append(["coverage"]); return 0
    def run_tests(self, test_paths, extra_args, markers):
        calls.append(["paths", test_paths, extra_args, markers]); return 0
    def run_all_tests(self, extra):
        calls.append(["all", extra]); return 0

test_runner.TestRunner = Recorder
sys.argv = ["test_runner.py", *sys.argv[2:]]
try:
    test_runner.main()
except SystemExit as exc:
    calls.append(["exit", exc.code])
print("CALLS=" + json.dumps(calls))
"""


def _run(*cli_args: str, cwd: Path = PROJECT_ROOT) -> list[list[object]]:
    completed = subprocess.run(  # noqa: S603  # fixed interpreter + literal driver, test-controlled args
        [sys.executable, "-c", _DRIVER, str(SCRIPTS_ROOT), *cli_args],
        cwd=cwd,
        capture_output=True,
        text=True,
        timeout=60,
        check=False,
    )
    line = next((ln for ln in completed.stdout.splitlines() if ln.startswith("CALLS=")), None)
    assert line is not None, completed.stderr
    return cast(list[list[object]], json.loads(line.removeprefix("CALLS=")))


def test_project_root_override_is_passed_to_runner(tmp_path: Path) -> None:
    calls = _run("--unit", "--project-root", str(tmp_path))
    assert calls == [["init", str(tmp_path)], ["unit", None], ["exit", 0]]


def test_project_root_defaults_to_nearest_pyproject() -> None:
    calls = _run("--integration", cwd=PROJECT_ROOT / "server")
    assert calls[0] == ["init", str(PROJECT_ROOT)]
    assert calls[1] == ["integration", None]


def test_paths_markers_and_pytest_args_are_forwarded() -> None:
    calls = _run("--path", "tests/unit", "--path", "tests/x", "-m", "not slow", "--pytest-args", "-k", "alias")
    assert calls[1] == ["paths", ["tests/unit", "tests/x"], ["-k", "alias"], "not slow"]


@pytest.mark.parametrize(("flag", "expected"), [("--coverage", ["coverage"]), ("--e2e", ["e2e", None])])
def test_mode_flags_select_runner_method(flag: str, expected: list[object]) -> None:
    assert _run(flag)[1] == expected


def test_no_flags_runs_all_tests() -> None:
    assert _run()[1] == ["all", None]


def test_missing_pyproject_exits_nonzero(tmp_path: Path) -> None:
    calls = _run(cwd=tmp_path)
    assert calls == [["exit", 1]]
