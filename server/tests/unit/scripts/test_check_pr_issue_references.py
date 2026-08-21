"""
Tests for scripts/check_pr_issue_references.py.

Covers the closing-keyword detection and the exit-0 warn-only policy described in the module
docstring. See #620/#621/#622/#629 for the recurring failure this guard targets.
"""

from __future__ import annotations

import importlib.util
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[4]
SCRIPT_PATH = PROJECT_ROOT / "scripts" / "check_pr_issue_references.py"

_spec = importlib.util.spec_from_file_location("check_pr_issue_references", SCRIPT_PATH)
assert _spec is not None and _spec.loader is not None
mod = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(mod)


def test_bare_reference_is_not_linked() -> None:
    refs = mod.find_bare_references("Related to #620 somehow.")
    assert refs == {620}


def test_closes_keyword_links_the_issue() -> None:
    refs = mod.find_bare_references("Closes #620")
    assert refs == set()


def test_fixes_and_resolved_keywords_link_case_insensitively() -> None:
    assert mod.find_bare_references("fixes #621") == set()
    assert mod.find_bare_references("Resolved #622") == set()
    assert mod.find_bare_references("FIXED #629") == set()


def test_closes_links_multiple_comma_separated_issues() -> None:
    refs = mod.find_bare_references("Closes #620, #621 and #622")
    assert refs == set()


def test_keyword_linked_and_bare_reference_coexist() -> None:
    refs = mod.find_bare_references("Closes #620. Also touches #627 for context.")
    assert refs == {627}


def test_no_references_at_all() -> None:
    assert mod.find_bare_references("Just a routine dependency bump.") == set()


def test_get_open_issue_numbers_filters_to_open_only(monkeypatch) -> None:
    def fake_run_gh(args: list[str]) -> str | None:
        number = args[2]
        return "OPEN" if number in {"620", "627"} else "CLOSED"

    monkeypatch.setattr(mod, "_run_gh", fake_run_gh)
    assert mod.get_open_issue_numbers({620, 621, 627}) == {620, 627}


def test_get_open_issue_numbers_empty_candidates_short_circuits(monkeypatch) -> None:
    def fail(_args: list[str]) -> str | None:
        raise AssertionError("should not call gh when there are no candidates")

    monkeypatch.setattr(mod, "_run_gh", fail)
    assert mod.get_open_issue_numbers(set()) == set()


def test_get_open_issue_numbers_returns_none_on_lookup_failure(monkeypatch) -> None:
    monkeypatch.setattr(mod, "_run_gh", lambda _args: None)
    assert mod.get_open_issue_numbers({620}) is None


def test_main_warns_on_open_bare_reference(monkeypatch, capsys) -> None:
    monkeypatch.setenv("PR_TITLE", "chore: unrelated bump")
    monkeypatch.setenv("PR_BODY", "Touches #627 for context, does not close it.")
    monkeypatch.delenv("GITHUB_ACTIONS", raising=False)
    monkeypatch.setattr(mod, "get_open_issue_numbers", lambda _candidates: {627})

    exit_code = mod.main()

    out = capsys.readouterr().out
    assert exit_code == 0
    assert "#627" in out
    assert "without a closing keyword" in out


def test_main_silent_when_referenced_issue_already_closed(monkeypatch, capsys) -> None:
    monkeypatch.setenv("PR_TITLE", "chore: unrelated bump")
    monkeypatch.setenv("PR_BODY", "Touches #620 for context.")
    monkeypatch.setattr(mod, "get_open_issue_numbers", lambda _candidates: set())

    exit_code = mod.main()

    out = capsys.readouterr().out
    assert exit_code == 0
    assert "either closed or linked" in out


def test_main_degrades_gracefully_when_gh_lookup_fails(monkeypatch, capsys) -> None:
    monkeypatch.setenv("PR_TITLE", "chore: unrelated bump")
    monkeypatch.setenv("PR_BODY", "Touches #620 for context.")
    monkeypatch.setattr(mod, "get_open_issue_numbers", lambda _candidates: None)

    exit_code = mod.main()

    out = capsys.readouterr().out
    assert exit_code == 0
    assert "could not query issue state" in out


def test_main_emits_github_annotation_in_ci(monkeypatch, capsys) -> None:
    monkeypatch.setenv("PR_TITLE", "chore: unrelated bump")
    monkeypatch.setenv("PR_BODY", "Touches #627 for context.")
    monkeypatch.setenv("GITHUB_ACTIONS", "true")
    monkeypatch.setattr(mod, "get_open_issue_numbers", lambda _candidates: {627})

    exit_code = mod.main()

    out = capsys.readouterr().out
    assert exit_code == 0
    assert out.startswith("::warning::")


def test_main_clean_when_no_references(monkeypatch, capsys) -> None:
    monkeypatch.setenv("PR_TITLE", "chore: unrelated bump")
    monkeypatch.setenv("PR_BODY", "No issue references here.")

    exit_code = mod.main()

    out = capsys.readouterr().out
    assert exit_code == 0
    assert "No unlinked issue references found." in out
