"""Unit tests for the migration-directory rules in scripts/lint_sql_guardrails.py.

dbmate reads two directories as one ledger: DDL in ``db/migrations/`` and DML (world content, in the data repo) in
``data/db/migrations/``. The linter keeps each file in its own directory and each version number unique, and must not
mistake SQL-looking text inside comments, strings or dollar-quoted JSON for a statement.
"""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path
from typing import Protocol, cast

import pytest

PROJECT_ROOT = Path(__file__).resolve().parents[4]
SCRIPT_PATH = PROJECT_ROOT / "scripts" / "lint_sql_guardrails.py"


class _LintSqlGuardrails(Protocol):
    """Typed surface of the loaded script, for the parts these tests exercise."""

    PROJECT_ROOT: Path

    def check_migration_kind(self, path: Path, content: str) -> list[str]: ...
    def check_unique_migration_versions(self, files: list[Path]) -> list[str]: ...
    def _collect_sql_files(self) -> list[Path]: ...


def _load_script() -> _LintSqlGuardrails:
    spec = importlib.util.spec_from_file_location("lint_sql_guardrails_for_tests", SCRIPT_PATH)
    assert spec is not None
    assert spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return cast(_LintSqlGuardrails, cast(object, module))


@pytest.fixture(name="lint")
def _lint(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> _LintSqlGuardrails:
    """The script with PROJECT_ROOT pointed at an empty temporary tree."""
    script = _load_script()
    monkeypatch.setattr(script, "PROJECT_ROOT", tmp_path)
    return script


def _migration(root: Path, directory: str, name: str, up: str) -> Path:
    path = root / directory / name
    path.parent.mkdir(parents=True, exist_ok=True)
    _ = path.write_text(f"-- migrate:up\n{up}\n-- migrate:down\nSELECT 1;\n", encoding="utf-8")
    return path


def _check(lint: _LintSqlGuardrails, path: Path) -> list[str]:
    return lint.check_migration_kind(path, path.read_text(encoding="utf-8"))


def test_dml_in_the_ddl_directory_is_flagged_with_where_it_belongs(lint: _LintSqlGuardrails, tmp_path: Path) -> None:
    path = _migration(tmp_path, "db/migrations", "20260101000000_a.sql", "INSERT INTO rooms (id) VALUES (1);")

    [issue] = _check(lint, path)

    assert "DML" in issue
    assert "INSERT" in issue
    assert "data/db/migrations/" in issue


@pytest.mark.parametrize(
    "statement",
    [
        "UPDATE rooms SET name = 'x';",
        "DELETE FROM room_links;",
        "WITH base AS (SELECT 1 AS n)\nINSERT INTO rooms (id) SELECT n FROM base;",
        "WITH gone AS (SELECT 1 AS n)\nUPDATE rooms SET name = 'x' FROM gone;",
    ],
)
def test_every_dml_verb_is_recognised_even_behind_a_cte(
    lint: _LintSqlGuardrails, tmp_path: Path, statement: str
) -> None:
    path = _migration(tmp_path, "db/migrations", "20260101000000_a.sql", statement)

    assert len(_check(lint, path)) == 1


def test_ddl_in_the_data_directory_is_flagged_with_where_it_belongs(lint: _LintSqlGuardrails, tmp_path: Path) -> None:
    path = _migration(tmp_path, "data/db/migrations", "20260101000000_a.sql", "ALTER TABLE rooms ADD COLUMN x int;")

    [issue] = _check(lint, path)

    assert "DDL" in issue
    assert "ALTER" in issue
    assert "db/migrations/" in issue


def test_a_pure_ddl_file_and_a_pure_dml_file_each_pass_in_their_own_directory(
    lint: _LintSqlGuardrails, tmp_path: Path
) -> None:
    ddl = _migration(
        tmp_path,
        "db/migrations",
        "20260101000000_a.sql",
        "CREATE INDEX IF NOT EXISTS i ON t (c);\nALTER TABLE t DROP CONSTRAINT IF EXISTS c;\nCOMMENT ON TABLE t IS 'x';",
    )
    dml = _migration(
        tmp_path,
        "data/db/migrations",
        "20260101000001_b.sql",
        "INSERT INTO t (id) VALUES (1) ON CONFLICT (id) DO UPDATE SET id = excluded.id;\nUPDATE t SET id = 2;",
    )

    assert _check(lint, ddl) == []
    assert _check(lint, dml) == []


def test_sql_looking_text_in_comments_strings_and_dollar_quotes_is_not_a_statement(
    lint: _LintSqlGuardrails, tmp_path: Path
) -> None:
    """A quest's JSON may say "UPDATE rooms"; a comment may hold an apostrophe; neither is a DML statement."""
    path = _migration(
        tmp_path,
        "db/migrations",
        "20260101000000_a.sql",
        "\n".join(
            [
                "-- the clerk's INSERT INTO note",
                "/* DELETE FROM everything; */",
                "COMMENT ON TABLE t IS 'INSERT INTO it''s fine; UPDATE too';",
                'CREATE FUNCTION f() RETURNS text AS $body$ UPDATE rooms SET name = "x"; $body$ LANGUAGE sql;',
            ]
        ),
    )

    assert _check(lint, path) == []


def test_files_outside_the_two_migration_directories_are_not_judged(lint: _LintSqlGuardrails, tmp_path: Path) -> None:
    other = _migration(tmp_path, "server/scripts", "a.sql", "INSERT INTO t (id) VALUES (1);")

    assert _check(lint, other) == []


def test_a_version_used_in_both_directories_is_flagged(lint: _LintSqlGuardrails, tmp_path: Path) -> None:
    ddl = _migration(tmp_path, "db/migrations", "20260101000000_schema.sql", "CREATE TABLE t (id int);")
    dml = _migration(tmp_path, "data/db/migrations", "20260101000000_data.sql", "INSERT INTO t (id) VALUES (1);")
    other = _migration(tmp_path, "data/db/migrations", "20260101000001_more.sql", "INSERT INTO t (id) VALUES (2);")

    [issue] = lint.check_unique_migration_versions([ddl, dml, other])

    assert "20260101000000" in issue
    assert "20260101000000_schema.sql" in issue


def test_the_real_migration_directories_obey_the_rules() -> None:
    """The repository as it stands: every migration sits in the directory for its kind, versions are unique."""
    script = _load_script()
    migrations = [
        path
        for path in script._collect_sql_files()  # pyright: ignore[reportPrivateUsage]
        if path.parent.name == "migrations"
    ]
    assert migrations, "found no migrations: has the layout changed?"

    issues = [issue for path in migrations for issue in _check(script, path)]
    issues += script.check_unique_migration_versions(migrations)

    assert issues == []
