"""Tests for scripts/audit_suppressions.py (#784 changes).

Two defects were fixed: the audit had no basedpyright-suppression pattern at all, so those
suppressions were invisible to it; and `has_explanation()` accepted any ten characters of trailing
text, which passed almost everything and made the "explained" percentage meaningless.

Note: the suppression marker is assembled at runtime rather than written literally, because
scripts/lint_pyright_suppressions.py scans every file under server/** including this one.
"""

from __future__ import annotations

import importlib.util
import re
import sys
from collections.abc import Callable
from dataclasses import dataclass
from pathlib import Path
from typing import Protocol, cast

import pytest

PROJECT_ROOT = Path(__file__).resolve().parents[4]
SCRIPT_PATH = PROJECT_ROOT / "scripts" / "audit_suppressions.py"

# Assembled, not literal -- see the module docstring.
IGNORE = "# pyright:" + " ignore"
BECAUSE = "# Appropriate because:"


class _AuditModule(Protocol):
    """Public surface of scripts/audit_suppressions.py used by these tests."""

    has_explanation: Callable[[str, int], bool]
    PYTHON_PATTERNS: list[tuple[str, str]]
    MIN_EXPLANATION_CHARS: int


@dataclass(frozen=True, slots=True)
class AuditTestApi:
    """Typed facade over the dynamically imported script."""

    has_explanation: Callable[[str, int], bool]
    python_patterns: list[tuple[str, str]]
    min_explanation_chars: int


def _load_script_module() -> AuditTestApi:
    module_name = "audit_suppressions_script"
    spec = importlib.util.spec_from_file_location(module_name, SCRIPT_PATH)
    assert spec is not None and spec.loader is not None
    mod = importlib.util.module_from_spec(spec)
    sys.modules[module_name] = mod
    spec.loader.exec_module(mod)
    loaded = cast(_AuditModule, cast(object, mod))
    return AuditTestApi(
        has_explanation=loaded.has_explanation,
        python_patterns=list(loaded.PYTHON_PATTERNS),
        min_explanation_chars=loaded.MIN_EXPLANATION_CHARS,
    )


@pytest.fixture(scope="module", name="audit_api")
def audit_api_module_scope() -> AuditTestApi:
    return _load_script_module()


def test_pyright_ignore_is_now_detected(audit_api: AuditTestApi) -> None:
    """basedpyright suppressions were entirely invisible to the audit before #784."""
    line = f"value = call()  {IGNORE}[reportAny]"
    matched = [tool for pattern, tool in audit_api.python_patterns if re.search(pattern, line)]
    assert "pyright" in matched


def test_pyright_pattern_matches_the_bare_form_too(audit_api: AuditTestApi) -> None:
    line = f"value = call()  {IGNORE}"
    matched = [tool for pattern, tool in audit_api.python_patterns if re.search(pattern, line)]
    assert "pyright" in matched


def test_explicit_reason_marker_counts_as_explained(audit_api: AuditTestApi) -> None:
    line = "x = 1  # noqa: E501  # Reason: long URL in docstring"
    assert audit_api.has_explanation(line, line.index("# Reason:"))


def test_appropriate_because_counts_as_explained(audit_api: AuditTestApi) -> None:
    line = f"x = 1  {IGNORE}[reportAny]  {BECAUSE} boundary is validated below"
    assert audit_api.has_explanation(line, line.index(BECAUSE))


def test_short_trailing_text_no_longer_passes(audit_api: AuditTestApi) -> None:
    """`# noqa  legacy code` used to count as an explanation. It explains nothing."""
    line = "x = 1  # noqa  legacy code"
    assert not audit_api.has_explanation(line, line.index("# noqa") + len("# noqa"))


def test_bare_suppression_is_unexplained(audit_api: AuditTestApi) -> None:
    line = "x = 1  # noqa"
    assert not audit_api.has_explanation(line, len(line))


def test_substantial_prose_still_counts(audit_api: AuditTestApi) -> None:
    trailer = "x" * audit_api.min_explanation_chars
    line = f"value = 1  # noqa  {trailer}"
    assert audit_api.has_explanation(line, line.index("# noqa") + len("# noqa"))
