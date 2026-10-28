"""Tests for the Python-runtime guard in scripts/check_codacy_yaml.py (#748)."""

# pyright: reportPrivateUsage=false
# Reason: this module unit-tests the script's private validator (_content_is_valid).

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path
from typing import Protocol, cast

PROJECT_ROOT = Path(__file__).resolve().parents[4]
SCRIPT = PROJECT_ROOT / "scripts" / "check_codacy_yaml.py"
SCRIPTS_ROOT = PROJECT_ROOT / "scripts"
PINNED_PYTHON = (PROJECT_ROOT / ".python-version").read_text(encoding="utf-8").strip()

# Filler for the guard's existing required-tool list (not something this repo has to use),
# so a failure below can only be about the Python runtime.
_REQUIRED = "\n".join(["lizard@1.17.31", "semgrep", "eslint@8.57.0", "ruff", "bandit", "node@22.2.0"])


class _CheckCodacyYamlModule(Protocol):
    """Shape of scripts/check_codacy_yaml.py, loaded dynamically below (not a static import)."""

    def _content_is_valid(self, content: str) -> tuple[bool, list[str]]: ...


def _load_module() -> _CheckCodacyYamlModule:
    scripts_root_s = str(SCRIPTS_ROOT)
    added = scripts_root_s not in sys.path
    if added:
        sys.path.insert(0, scripts_root_s)
    try:
        spec = importlib.util.spec_from_file_location("check_codacy_yaml", SCRIPT)
        assert spec is not None and spec.loader is not None
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        return cast(_CheckCodacyYamlModule, cast(object, module))
    finally:
        if added:
            sys.path.remove(scripts_root_s)


def test_stale_311_runtime_is_flagged_with_the_pinned_version() -> None:
    valid, reasons = _load_module()._content_is_valid(f"{_REQUIRED}\npython@3.11.11\n")
    assert not valid
    assert reasons == [f"wrong Python version (3.11.11 instead of {PINNED_PYTHON})"]


def test_pinned_runtime_is_accepted() -> None:
    valid, reasons = _load_module()._content_is_valid(f"{_REQUIRED}\npython@{PINNED_PYTHON}\n")
    assert valid
    assert reasons == []
