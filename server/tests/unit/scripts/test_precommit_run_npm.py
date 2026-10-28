"""Unit tests for scripts/precommit_run_npm.py.

The wrapper runs the client npm scripts CI also runs (lint, format, knip) from pre-commit, so a CI-only
failure such as an unused export (knip, #1069) is caught before the push.
"""

from __future__ import annotations

import importlib.util
import subprocess
import sys
from pathlib import Path
from typing import Protocol, cast

import pytest

PROJECT_ROOT = Path(__file__).resolve().parents[4]
SCRIPT_PATH = PROJECT_ROOT / "scripts" / "precommit_run_npm.py"
PRE_COMMIT_CONFIG = PROJECT_ROOT / ".pre-commit-config.yaml"


class _PrecommitRunNpmModule(Protocol):
    """Typed surface of the loaded script, for the parts these tests exercise."""

    CLIENT: Path
    SCRIPTS: tuple[str, ...]

    def main(self) -> int: ...


def _load_script() -> _PrecommitRunNpmModule:
    spec = importlib.util.spec_from_file_location("precommit_run_npm_for_tests", SCRIPT_PATH)
    assert spec is not None
    assert spec.loader is not None
    mod = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = mod
    spec.loader.exec_module(mod)
    return cast(_PrecommitRunNpmModule, cast(object, mod))


def _record_calls(monkeypatch: pytest.MonkeyPatch, exit_code: int = 0) -> list[tuple[list[str], str]]:
    """Replace subprocess.call with a recorder returning `exit_code`."""
    calls: list[tuple[list[str], str]] = []

    def fake_call(args: list[str], cwd: str) -> int:
        calls.append((args, cwd))
        return exit_code

    monkeypatch.setattr(subprocess, "call", fake_call)
    return calls


@pytest.mark.parametrize("script", ["lint", "format", "knip"])
def test_runs_the_named_npm_script_in_client_and_returns_its_exit_code(
    script: str, monkeypatch: pytest.MonkeyPatch
) -> None:
    module = _load_script()
    calls = _record_calls(monkeypatch, exit_code=3)
    monkeypatch.setattr(module, "_resolved_npm", lambda: "/usr/bin/npm", raising=False)
    monkeypatch.setattr(sys, "argv", ["precommit_run_npm.py", script])

    assert module.main() == 3
    assert calls == [(["/usr/bin/npm", "run", script], str(module.CLIENT))]


@pytest.mark.parametrize("argv", [["precommit_run_npm.py"], ["precommit_run_npm.py", "build"]])
def test_rejects_a_missing_or_unknown_script_without_running_npm(
    argv: list[str], monkeypatch: pytest.MonkeyPatch
) -> None:
    module = _load_script()
    calls = _record_calls(monkeypatch)
    monkeypatch.setattr(sys, "argv", argv)

    assert module.main() == 2
    assert calls == []


def test_reports_a_missing_npm_instead_of_failing_silently(monkeypatch: pytest.MonkeyPatch) -> None:
    module = _load_script()
    calls = _record_calls(monkeypatch)
    monkeypatch.setattr(module, "_resolved_npm", lambda: None, raising=False)
    monkeypatch.setattr(sys, "argv", ["precommit_run_npm.py", "knip"])

    assert module.main() == 127
    assert calls == []


def test_knip_is_a_supported_script() -> None:
    assert "knip" in _load_script().SCRIPTS


def test_pre_commit_config_runs_knip_on_every_commit() -> None:
    """Dropping the hook would silently let CI's 'Dead code check (knip)' be the first place this fails."""
    config = PRE_COMMIT_CONFIG.read_text(encoding="utf-8")
    hook = config.split("id: npm-knip", maxsplit=1)
    assert len(hook) == 2, "the npm-knip hook is missing from .pre-commit-config.yaml"
    block = hook[1].split("\n      - id:", maxsplit=1)[0]
    assert "scripts/precommit_run_npm.py knip" in block
    assert "always_run: true" in block
