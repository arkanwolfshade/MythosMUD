"""Tests for scripts/lint_pyright_suppressions.py (#784).

The linter's scoping is the part worth pinning down: a bare suppression fails for *any* rule, but
the `Reason:` / `Appropriate because:` block is required only for reportAny and reportExplicitAny.
Suppressions for unrelated rules (reportPrivateUsage on a test reaching into a private helper,
reportUnannotatedClassAttribute on SQLAlchemy's __tablename__) must keep working untouched -- the
category vocabulary describes why a value is untyped and says nothing about them.

Note: the suppression marker is assembled at runtime rather than written literally. The linter
scans every file under server/**, this one included, so a literal marker in test data would make
this file fail the very check it is testing.
"""

from __future__ import annotations

import importlib.util
import sys
from collections.abc import Callable
from dataclasses import dataclass
from pathlib import Path
from typing import Protocol, cast

import pytest

PROJECT_ROOT = Path(__file__).resolve().parents[4]
SCRIPT_PATH = PROJECT_ROOT / "scripts" / "lint_pyright_suppressions.py"

# Assembled, not literal -- see the module docstring.
IGNORE = "# pyright:" + " ignore"
REASON = "# Reason:"
BECAUSE = "# Appropriate because:"
LONG_ENOUGH = "this justification is comfortably long enough to pass the length check"


class _Failure(Protocol):
    """The shape of a reported violation."""

    lineno: int
    problem: str


class _Suppression(Protocol):
    """The shape of a parsed suppression."""

    lineno: int
    rules: tuple[str, ...]
    category: str | None


class _LintModule(Protocol):
    """Public surface of scripts/lint_pyright_suppressions.py used by these tests."""

    scan_file: Callable[[Path], tuple[list[_Suppression], list[_Failure]]]
    MIN_JUSTIFICATION_CHARS: int


@dataclass(frozen=True, slots=True)
class LintTestApi:
    """Typed facade over the dynamically imported script."""

    scan_file: Callable[[Path], tuple[list[_Suppression], list[_Failure]]]
    min_justification_chars: int


def _load_script_module() -> LintTestApi:
    module_name = "lint_pyright_suppressions_script"
    spec = importlib.util.spec_from_file_location(module_name, SCRIPT_PATH)
    assert spec is not None and spec.loader is not None
    mod = importlib.util.module_from_spec(spec)
    # The script defines @dataclass types, and dataclasses resolves annotations through
    # sys.modules[cls.__module__] -- so the module must be registered before exec_module.
    sys.modules[module_name] = mod
    spec.loader.exec_module(mod)
    loaded = cast(_LintModule, cast(object, mod))
    return LintTestApi(scan_file=loaded.scan_file, min_justification_chars=loaded.MIN_JUSTIFICATION_CHARS)


@pytest.fixture(scope="module", name="lint_api")
def lint_api_module_scope() -> LintTestApi:
    return _load_script_module()


def _write(tmp_path: Path, body: str) -> Path:
    target = tmp_path / "sample.py"
    _ = target.write_text(body, encoding="utf-8")
    return target


def _problems(lint_api: LintTestApi, tmp_path: Path, body: str) -> list[str]:
    _, failures = lint_api.scan_file(_write(tmp_path, body))
    return [f.problem for f in failures]


# --- the bare-suppression ban applies to every rule ----------------------------------------


def test_bare_ignore_is_rejected(lint_api: LintTestApi, tmp_path: Path) -> None:
    problems = _problems(lint_api, tmp_path, f"value = 1  {IGNORE}\n")
    assert len(problems) == 1
    assert "bare" in problems[0]


def test_empty_bracket_ignore_is_rejected(lint_api: LintTestApi, tmp_path: Path) -> None:
    problems = _problems(lint_api, tmp_path, f"value = 1  {IGNORE}[]\n")
    assert len(problems) == 1
    assert "names no rule" in problems[0]


# --- the justification block is scoped to the Any family -----------------------------------


def test_non_any_rule_needs_no_justification(lint_api: LintTestApi, tmp_path: Path) -> None:
    """The 53 existing non-Any suppressions must not be forced through an Any-shaped taxonomy."""
    body = f"value = obj._private  {IGNORE}[reportPrivateUsage]\n"
    assert _problems(lint_api, tmp_path, body) == []


def test_sqlalchemy_style_suppression_still_passes(lint_api: LintTestApi, tmp_path: Path) -> None:
    body = f'__tablename__ = "players"  {IGNORE}[reportUnannotatedClassAttribute]\n'
    assert _problems(lint_api, tmp_path, body) == []


def test_any_rule_without_justification_is_rejected(lint_api: LintTestApi, tmp_path: Path) -> None:
    problems = _problems(lint_api, tmp_path, f"value = call()  {IGNORE}[reportAny]\n")
    assert any("Reason" in p for p in problems)
    assert any("Appropriate because" in p for p in problems)


def test_reason_without_appropriate_because_is_rejected(lint_api: LintTestApi, tmp_path: Path) -> None:
    body = f"{REASON} TEST_MOCK - a stated cause\nvalue = call()  {IGNORE}[reportAny]\n"
    problems = _problems(lint_api, tmp_path, body)
    assert problems
    assert all("Appropriate because" in p for p in problems)


def test_short_appropriate_because_is_rejected(lint_api: LintTestApi, tmp_path: Path) -> None:
    """A token sentence must not satisfy the field the whole standard exists for."""
    body = f"{REASON} TEST_MOCK - cause\n{BECAUSE} too short\nvalue = call()  {IGNORE}[reportAny]\n"
    problems = _problems(lint_api, tmp_path, body)
    assert any(str(lint_api.min_justification_chars) in p for p in problems)


# --- category vocabulary --------------------------------------------------------------------


def test_unknown_category_is_rejected(lint_api: LintTestApi, tmp_path: Path) -> None:
    body = f"{REASON} LEGACY_REASONS - it has always been like this\n{BECAUSE} {LONG_ENOUGH}\nvalue = call()  {IGNORE}[reportAny]\n"
    problems = _problems(lint_api, tmp_path, body)
    assert any("unknown category" in p for p in problems)


def test_prefix_category_requires_a_suffix(lint_api: LintTestApi, tmp_path: Path) -> None:
    body = f"{REASON} THIRD_PARTY_UNTYPED - which library, though?\n{BECAUSE} {LONG_ENOUGH}\nvalue = call()  {IGNORE}[reportAny]\n"
    problems = _problems(lint_api, tmp_path, body)
    assert any("requires a `:<detail>` suffix" in p for p in problems)


# --- accepted forms --------------------------------------------------------------------------


def test_justification_above_the_suppression_is_accepted(lint_api: LintTestApi, tmp_path: Path) -> None:
    body = (
        f"{REASON} THIRD_PARTY_UNTYPED:nats - Msg.data is annotated bytes | Any upstream.\n"
        f"{BECAUSE} the payload is validated by _decode_envelope() on the next line,\n"
        "# which returns a typed Envelope.\n"
        f"msg = await sub.next_msg()  {IGNORE}[reportAny]\n"
    )
    suppressions, failures = lint_api.scan_file(_write(tmp_path, body))
    assert failures == []
    assert suppressions[0].category == "THIRD_PARTY_UNTYPED:nats"


def test_justification_below_the_suppression_is_accepted(lint_api: LintTestApi, tmp_path: Path) -> None:
    """Placement below matters for multi-line expressions, where 'above' is the only other option."""
    body = (
        f"msg = await sub.next_msg()  {IGNORE}[reportAny]\n"
        f"{REASON} TEST_MOCK - the double is a bare MagicMock, so attribute reads are Any.\n"
        f"{BECAUSE} asserting on the call record is the point of this test, and Python\n"
        "# has no intersection type for 'the real service AND a MagicMock'.\n"
    )
    _, failures = lint_api.scan_file(_write(tmp_path, body))
    assert failures == []


def test_multi_rule_suppression_reports_every_rule(lint_api: LintTestApi, tmp_path: Path) -> None:
    body = (
        f"{REASON} THIRD_PARTY_UNTYPED:logging - typeshed declares a narrower return type.\n"
        f"{BECAUSE} the precise union violates Liskov against the parent signature,\n"
        "# so writing it trades one diagnostic for another without helping any caller.\n"
        f"def _open(self) -> Any:  {IGNORE}[reportExplicitAny, reportAny]\n"
    )
    suppressions, failures = lint_api.scan_file(_write(tmp_path, body))
    assert failures == []
    assert suppressions[0].rules == ("reportExplicitAny", "reportAny")


def test_clean_file_reports_nothing(lint_api: LintTestApi, tmp_path: Path) -> None:
    _, failures = lint_api.scan_file(_write(tmp_path, "value: int = 1\n"))
    assert failures == []
