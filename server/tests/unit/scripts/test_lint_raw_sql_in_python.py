"""Unit tests for scripts/lint_raw_sql_in_python.py.

Verifies the detection logic that matters most: real table CRUD is caught, legitimate ADR-015
procedure calls are not (the false-positive failure mode that got .semgrep.yml ignored), comments
and docstrings using SQL-like English words aren't mistaken for embedded SQL, and any site in
server/ fails the scan (no grandfathered allowlist).
"""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path
from typing import Protocol, cast

from _pytest.monkeypatch import MonkeyPatch

PROJECT_ROOT = Path(__file__).resolve().parents[4]
SCRIPT_PATH = PROJECT_ROOT / "scripts" / "lint_raw_sql_in_python.py"


class _LintRawSqlModule(Protocol):
    """Typed surface of the loaded script, for the parts these tests exercise."""

    def _find_raw_sql_lines(self, content: str) -> list[int]: ...
    def scan(self) -> list[str]: ...


def _load_script() -> _LintRawSqlModule:
    spec = importlib.util.spec_from_file_location("lint_raw_sql_in_python_for_tests", SCRIPT_PATH)
    assert spec is not None
    assert spec.loader is not None
    mod = importlib.util.module_from_spec(spec)
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


def test_raw_sql_site_is_reported(tmp_path: Path, monkeypatch: MonkeyPatch) -> None:
    mod = _load_script()
    server_dir = tmp_path / "server"
    target_file = server_dir / "sample_service.py"
    server_dir.mkdir()
    _ = target_file.write_text('QUERY = "SELECT id FROM widgets"\n', encoding="utf-8")

    monkeypatch.setattr(mod, "PROJECT_ROOT", tmp_path)

    violations = mod.scan()

    assert len(violations) == 1
    assert "sample_service.py" in violations[0]
    assert "1 raw SQL site(s)" in violations[0]


def test_current_codebase_has_no_raw_sql() -> None:
    """server/ must have zero raw-SQL sites -- the migration completed under #633."""
    mod = _load_script()
    assert mod.scan() == []
