"""Unit tests for scripts/lint_raw_sql_in_python.py.

Verifies the detection logic that matters most: real table CRUD is caught, legitimate ADR-015
procedure calls are not (the false-positive failure mode that got .semgrep.yml ignored), comments
and docstrings using SQL-like English words aren't mistaken for embedded SQL, allowlisted files'
site counts are confirmed, past-deadline entries warn without failing the build (as a GitHub
Actions annotation under GITHUB_ACTIONS, plain text otherwise), and the count-keyed allowlist
catches both new sites and stale (higher-than-actual) entries.
"""

from __future__ import annotations

import importlib.util
import sys
from datetime import date, timedelta
from pathlib import Path
from typing import Protocol, cast

PROJECT_ROOT = Path(__file__).resolve().parents[4]
SCRIPT_PATH = PROJECT_ROOT / "scripts" / "lint_raw_sql_in_python.py"


class _LintRawSqlModule(Protocol):
    """Typed surface of the loaded script, for the parts these tests exercise."""

    def _find_raw_sql_lines(self, content: str) -> list[int]: ...
    def scan(self) -> tuple[list[str], list[str], int]: ...

    RAW_SQL_ALLOWLIST: tuple[object, ...]
    AllowlistEntry: type


def _load_script() -> _LintRawSqlModule:
    spec = importlib.util.spec_from_file_location("lint_raw_sql_in_python_for_tests", SCRIPT_PATH)
    assert spec is not None
    assert spec.loader is not None
    mod = importlib.util.module_from_spec(spec)
    # dataclass's forward-reference resolution looks the module up via sys.modules[__module__];
    # register before exec_module so @dataclass(frozen=True) on AllowlistEntry doesn't crash.
    sys.modules[spec.name] = mod
    spec.loader.exec_module(mod)
    return cast(_LintRawSqlModule, cast(object, mod))


def test_script_exists() -> None:
    assert SCRIPT_PATH.is_file()


def test_flags_raw_select_star() -> None:
    mod = _load_script()
    assert mod._find_raw_sql_lines('cursor.execute("SELECT * FROM rooms")') == [1]


def test_flags_raw_insert_into() -> None:
    mod = _load_script()
    content = 'text(\n    "INSERT INTO containers (id, name) VALUES (:id, :name)"\n)'
    assert mod._find_raw_sql_lines(content) == [2]


def test_flags_raw_update_set() -> None:
    mod = _load_script()
    assert mod._find_raw_sql_lines('"UPDATE players SET name = :name"') == [1]


def test_flags_raw_delete_from() -> None:
    mod = _load_script()
    assert mod._find_raw_sql_lines('"DELETE FROM containers WHERE id = :id"') == [1]


def test_flags_bare_table_select_from() -> None:
    mod = _load_script()
    assert mod._find_raw_sql_lines('text("SELECT stable_id FROM rooms WHERE id = :id")') == [1]


def test_flags_bare_table_select_from_split_across_lines() -> None:
    """Regression test for the gap #624 found: a naive per-line matcher can't see SELECT and FROM
    on separate lines, which is how emote_service.py's own queries -- and roughly a dozen other
    files' -- were written. The line reported is where SELECT starts."""
    mod = _load_script()
    content = 'query = """\n    SELECT\n        stable_id\n    FROM rooms\n    ORDER BY stable_id\n"""'
    assert mod._find_raw_sql_lines(content) == [2]


def test_does_not_flag_procedure_call_no_from() -> None:
    """ADR-015 procedure call: SELECT fn(:arg) -- no FROM at all."""
    mod = _load_script()
    assert mod._find_raw_sql_lines('text("SELECT update_player_xp(:player_id, :delta)")') == []


def test_does_not_flag_procedure_call_with_from() -> None:
    """ADR-015 procedure call: SELECT col FROM fn(:arg) -- FROM target is a function call."""
    mod = _load_script()
    assert mod._find_raw_sql_lines('text("SELECT col1, col2 FROM fn(:id)")') == []


def test_does_not_flag_comment_mentioning_select_star() -> None:
    """A comment describing what to avoid must not itself be flagged as embedded SQL."""
    mod = _load_script()
    line = "PLAYER_COLUMNS = (  # avoids SELECT * anti-pattern"
    assert mod._find_raw_sql_lines(line) == []


def test_does_not_flag_docstring_prose_with_select_from() -> None:
    """Ordinary English sentence-case prose ('Select ... from ...') must not match -- only
    UPPERCASE SQL-keyword convention, which is how every real embedded-SQL site in this codebase
    writes it."""
    mod = _load_script()
    line = '"""Select target player from matching players, handling instance numbers."""'
    assert mod._find_raw_sql_lines(line) == []


def test_allowlist_entries_are_suppressed_and_counted(tmp_path, monkeypatch) -> None:
    mod = _load_script()
    server_dir = tmp_path / "server"
    target_file = server_dir / "sample_service.py"
    server_dir.mkdir()
    target_file.write_text('QUERY = "SELECT id FROM widgets"\n', encoding="utf-8")

    entry = mod.AllowlistEntry("server/sample_service.py", 1, "#000", date.today() + timedelta(days=365))
    monkeypatch.setattr(mod, "PROJECT_ROOT", tmp_path)
    monkeypatch.setattr(mod, "RAW_SQL_ALLOWLIST", (entry,))
    monkeypatch.setattr(mod, "_ALLOWLIST_BY_FILE", {entry.file: entry})

    new_violations, overdue_warnings, allowlisted_count = mod.scan()

    assert new_violations == []
    assert overdue_warnings == []
    assert allowlisted_count == 1


def test_overdue_allowlist_entry_warns_but_does_not_fail(tmp_path, monkeypatch) -> None:
    mod = _load_script()
    server_dir = tmp_path / "server"
    target_file = server_dir / "sample_service.py"
    server_dir.mkdir()
    target_file.write_text('QUERY = "SELECT id FROM widgets"\n', encoding="utf-8")

    entry = mod.AllowlistEntry("server/sample_service.py", 1, "#000", date.today() - timedelta(days=1))
    monkeypatch.setattr(mod, "PROJECT_ROOT", tmp_path)
    monkeypatch.setattr(mod, "RAW_SQL_ALLOWLIST", (entry,))
    monkeypatch.setattr(mod, "_ALLOWLIST_BY_FILE", {entry.file: entry})
    monkeypatch.delenv("GITHUB_ACTIONS", raising=False)

    new_violations, overdue_warnings, allowlisted_count = mod.scan()

    assert new_violations == []
    assert allowlisted_count == 1
    assert len(overdue_warnings) == 1
    assert "OVERDUE" in overdue_warnings[0]
    assert "#000" in overdue_warnings[0]
    assert "::warning" not in overdue_warnings[0]


def test_overdue_allowlist_entry_emits_github_annotation_in_ci(tmp_path, monkeypatch) -> None:
    """Under GITHUB_ACTIONS, an overdue entry renders as a ::warning:: annotation so it surfaces
    on the PR's Files-changed tab instead of scrolling past in stdout (#618 hardening)."""
    mod = _load_script()
    server_dir = tmp_path / "server"
    target_file = server_dir / "sample_service.py"
    server_dir.mkdir()
    target_file.write_text('QUERY = "SELECT id FROM widgets"\n', encoding="utf-8")

    entry = mod.AllowlistEntry("server/sample_service.py", 1, "#000", date.today() - timedelta(days=1))
    monkeypatch.setattr(mod, "PROJECT_ROOT", tmp_path)
    monkeypatch.setattr(mod, "RAW_SQL_ALLOWLIST", (entry,))
    monkeypatch.setattr(mod, "_ALLOWLIST_BY_FILE", {entry.file: entry})
    monkeypatch.setenv("GITHUB_ACTIONS", "true")

    new_violations, overdue_warnings, _allowlisted_count = mod.scan()

    assert new_violations == []
    assert len(overdue_warnings) == 1
    assert overdue_warnings[0].startswith("::warning file=server/sample_service.py::")


def test_new_unallowlisted_site_is_reported(tmp_path, monkeypatch) -> None:
    mod = _load_script()
    server_dir = tmp_path / "server"
    target_file = server_dir / "sample_service.py"
    server_dir.mkdir()
    target_file.write_text('QUERY = "SELECT id FROM widgets"\n', encoding="utf-8")

    monkeypatch.setattr(mod, "PROJECT_ROOT", tmp_path)
    monkeypatch.setattr(mod, "RAW_SQL_ALLOWLIST", ())
    monkeypatch.setattr(mod, "_ALLOWLIST_BY_FILE", {})

    new_violations, overdue_warnings, allowlisted_count = mod.scan()

    assert len(new_violations) == 1
    assert "sample_service.py" in new_violations[0]
    assert overdue_warnings == []
    assert allowlisted_count == 0


def test_count_exceeding_allowlist_is_reported(tmp_path, monkeypatch) -> None:
    """A file with more raw-SQL sites than its allowlist entry expects fails -- a genuinely new
    site was added alongside grandfathered ones."""
    mod = _load_script()
    server_dir = tmp_path / "server"
    target_file = server_dir / "sample_service.py"
    server_dir.mkdir()
    target_file.write_text('QUERY_A = "SELECT id FROM widgets"\nQUERY_B = "SELECT id FROM gadgets"\n', encoding="utf-8")

    entry = mod.AllowlistEntry("server/sample_service.py", 1, "#000", date.today() + timedelta(days=365))
    monkeypatch.setattr(mod, "PROJECT_ROOT", tmp_path)
    monkeypatch.setattr(mod, "RAW_SQL_ALLOWLIST", (entry,))
    monkeypatch.setattr(mod, "_ALLOWLIST_BY_FILE", {entry.file: entry})

    new_violations, _overdue, allowlisted_count = mod.scan()

    assert len(new_violations) == 1
    assert "2 raw SQL site(s) found, 1 allowlisted" in new_violations[0]
    assert allowlisted_count == 0


def test_count_under_allowlist_is_reported(tmp_path, monkeypatch) -> None:
    """A file with fewer raw-SQL sites than its allowlist entry expects fails -- a site was
    migrated and the allowlist entry was never lowered (#618 hardening: this used to pass
    silently under the old (file, line) key, since only the deleted line's specific key vanished)."""
    mod = _load_script()
    server_dir = tmp_path / "server"
    target_file = server_dir / "sample_service.py"
    server_dir.mkdir()
    target_file.write_text('QUERY = "SELECT id FROM widgets"\n', encoding="utf-8")

    entry = mod.AllowlistEntry("server/sample_service.py", 2, "#000", date.today() + timedelta(days=365))
    monkeypatch.setattr(mod, "PROJECT_ROOT", tmp_path)
    monkeypatch.setattr(mod, "RAW_SQL_ALLOWLIST", (entry,))
    monkeypatch.setattr(mod, "_ALLOWLIST_BY_FILE", {entry.file: entry})

    new_violations, _overdue, allowlisted_count = mod.scan()

    assert len(new_violations) == 1
    assert "lower the allowlist count to 1" in new_violations[0]
    assert allowlisted_count == 0


def test_drift_immune_to_unrelated_line_shift(tmp_path, monkeypatch) -> None:
    """A blank line inserted above the allowlisted site must not trip a violation -- the whole
    point of keying on a per-file count instead of (file, line) (#618 hardening)."""
    mod = _load_script()
    server_dir = tmp_path / "server"
    target_file = server_dir / "sample_service.py"
    server_dir.mkdir()
    target_file.write_text('\n\n\nQUERY = "SELECT id FROM widgets"\n', encoding="utf-8")

    entry = mod.AllowlistEntry("server/sample_service.py", 1, "#000", date.today() + timedelta(days=365))
    monkeypatch.setattr(mod, "PROJECT_ROOT", tmp_path)
    monkeypatch.setattr(mod, "RAW_SQL_ALLOWLIST", (entry,))
    monkeypatch.setattr(mod, "_ALLOWLIST_BY_FILE", {entry.file: entry})

    new_violations, _overdue, allowlisted_count = mod.scan()

    assert new_violations == []
    assert allowlisted_count == 1


def test_baseline_allowlist_matches_current_codebase() -> None:
    """The shipped RAW_SQL_ALLOWLIST must exactly match what the scanner currently finds in
    server/ -- catches allowlist drift (a count that no longer matches reality) as a test failure
    rather than a silent pass/fail surprise in CI."""
    mod = _load_script()
    new_violations, _overdue, allowlisted_count = mod.scan()
    assert new_violations == []
    assert allowlisted_count == len(mod.RAW_SQL_ALLOWLIST)
