"""Regression tests for scripts/load_world_seed.py (URL parsing, allowlist, search_path)."""

# Script helpers are underscore-prefixed on the real module; we cast importlib output to this
# Protocol once, then expose a small public API dataclass for tests.
# pylint: disable=protected-access
#
# Dynamic module + patch.object(module, "asyncpg"/"shutil"/"subprocess") mocking (see
# test_run_quality_fragmentation_guard.py for the same convention): ModuleType attribute access
# and Mock call-arg introspection are untyped by nature, not a real Any leak.
# pyright: reportAny=false

from __future__ import annotations

import importlib.util
from collections.abc import Awaitable, Callable
from dataclasses import dataclass
from pathlib import Path
from types import ModuleType
from typing import Protocol, cast
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

PROJECT_ROOT = Path(__file__).resolve().parents[4]
SCRIPT_PATH = PROJECT_ROOT / "scripts" / "load_world_seed.py"


class _LoadWorldSeedScriptInternals(Protocol):
    """Attributes of scripts/load_world_seed.py we read after dynamic import (not on ModuleType stub)."""

    _database_url_for_cli: Callable[[str], str]
    _parse_pg_url_for_psql: Callable[[str], tuple[str, int, str, str, str]]
    _validate_environment_and_files: Callable[[], tuple[str, Path, Path]]
    _asyncpg_server_settings: Callable[[str], dict[str, str]]
    _reset_migration_ledger: Callable[[str, str], Awaitable[None]]
    _replay_migrations: Callable[[str, str], None]


@dataclass(frozen=True, slots=True)
class LoadWorldSeedTestApi:
    """Typed facade over scripts/load_world_seed.py helpers (dynamic import)."""

    module: ModuleType
    database_url_for_cli: Callable[[str], str]
    parse_pg_url_for_psql: Callable[[str], tuple[str, int, str, str, str]]
    validate_environment_and_files: Callable[[], tuple[str, Path, Path]]
    asyncpg_server_settings: Callable[[str], dict[str, str]]
    reset_migration_ledger: Callable[[str, str], Awaitable[None]]
    replay_migrations: Callable[[str, str], None]


def _load_script_module() -> LoadWorldSeedTestApi:
    spec = importlib.util.spec_from_file_location("load_world_seed_script", SCRIPT_PATH)
    assert spec is not None and spec.loader is not None
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    loaded = cast(_LoadWorldSeedScriptInternals, cast(object, mod))
    return LoadWorldSeedTestApi(
        module=mod,
        database_url_for_cli=loaded._database_url_for_cli,  # pyright: ignore[reportPrivateUsage] -- script module API
        parse_pg_url_for_psql=loaded._parse_pg_url_for_psql,  # pyright: ignore[reportPrivateUsage] -- script module API
        validate_environment_and_files=loaded._validate_environment_and_files,  # pyright: ignore[reportPrivateUsage]
        asyncpg_server_settings=loaded._asyncpg_server_settings,  # pyright: ignore[reportPrivateUsage]
        reset_migration_ledger=loaded._reset_migration_ledger,  # pyright: ignore[reportPrivateUsage]
        replay_migrations=loaded._replay_migrations,  # pyright: ignore[reportPrivateUsage]
    )


@pytest.fixture(scope="module", name="world_seed_api")
def world_seed_api_module_scope() -> LoadWorldSeedTestApi:
    """Dynamically loaded scripts/load_world_seed.py for unit tests."""
    return _load_script_module()


def test_database_url_for_cli_replaces_asyncpg_prefix(world_seed_api: LoadWorldSeedTestApi) -> None:
    """database_url_for_cli strips the asyncpg driver prefix for CLI tools."""
    url = "postgresql+asyncpg://user:pass@localhost:5432/mythos_unit"
    assert world_seed_api.database_url_for_cli(url) == "postgresql://user:pass@localhost:5432/mythos_unit"


def test_parse_pg_url_for_psql_decodes_user_password(world_seed_api: LoadWorldSeedTestApi) -> None:
    """parse_pg_url_for_psql URL-decodes credentials and returns connection parts."""
    host, port, user, password, dbname = world_seed_api.parse_pg_url_for_psql(
        "postgresql://myuser:myp%40ss@db.example.com:5433/mythos_dev?ssl=true"
    )
    assert host == "db.example.com"
    assert port == 5433
    assert user == "myuser"
    assert password == "myp@ss"
    assert dbname == "mythos_dev"


def test_parse_pg_url_for_psql_rejects_missing_host(world_seed_api: LoadWorldSeedTestApi) -> None:
    """parse_pg_url_for_psql requires a host in the URL."""
    with pytest.raises(ValueError, match="host"):
        _ = world_seed_api.parse_pg_url_for_psql("postgresql:///mythos_dev")


@pytest.mark.regression
def test_validate_environment_rejects_non_allowlist_database_name(
    monkeypatch: pytest.MonkeyPatch,
    world_seed_api: LoadWorldSeedTestApi,
    capsys: pytest.CaptureFixture[str],
) -> None:
    """validate_environment_and_files exits when DATABASE_URL names a non-allowlisted DB."""
    monkeypatch.setenv("DATABASE_URL", "postgresql://u:p@localhost:5432/evil_db")
    monkeypatch.setenv("CONFIRM_LOAD_WORLD_SEED", "1")
    with pytest.raises(SystemExit) as exc_info:
        _ = world_seed_api.validate_environment_and_files()
    assert exc_info.value.code == 1
    out = capsys.readouterr().out
    assert "evil_db" in out or "must be one of" in out


@pytest.mark.regression
def test_asyncpg_server_settings_defaults_to_db_name(
    monkeypatch: pytest.MonkeyPatch, world_seed_api: LoadWorldSeedTestApi
) -> None:
    """When POSTGRES_SEARCH_PATH is unset, search_path defaults to the DB name from the URL."""
    monkeypatch.delenv("POSTGRES_SEARCH_PATH", raising=False)
    url = "postgresql://localhost/mythos_e2e"
    assert world_seed_api.asyncpg_server_settings(url) == {"search_path": "mythos_e2e"}


@pytest.mark.regression
def test_asyncpg_server_settings_respects_postgres_search_path(
    monkeypatch: pytest.MonkeyPatch, world_seed_api: LoadWorldSeedTestApi
) -> None:
    """POSTGRES_SEARCH_PATH overrides the default schema/search_path."""
    monkeypatch.setenv("POSTGRES_SEARCH_PATH", "custom_schema")
    url = "postgresql://localhost/mythos_unit"
    assert world_seed_api.asyncpg_server_settings(url) == {"search_path": "custom_schema"}


@pytest.mark.regression
@pytest.mark.parametrize("db_name", ["mythos_dev", "mythos_unit", "mythos_e2e"])
def test_validate_environment_resolves_to_the_single_schema_agnostic_baseline(
    monkeypatch: pytest.MonkeyPatch,
    world_seed_api: LoadWorldSeedTestApi,
    db_name: str,
) -> None:
    """Since #811, every allowlisted DB resolves to the SAME db/schema.sql and
    data/db/seed.sql -- there is no longer a per-environment file to pick.

    `_validate_environment_and_files` checks existence against the process cwd (it is a
    script, run from the repo root), so this test anchors cwd explicitly rather than trusting
    whatever an earlier test in the same pytest session left it as.
    """
    monkeypatch.chdir(PROJECT_ROOT)
    monkeypatch.setenv("DATABASE_URL", f"postgresql://u:p@localhost:5432/{db_name}")
    monkeypatch.setenv("CONFIRM_LOAD_WORLD_SEED", "1")
    database_url, schema_file, dml_file = world_seed_api.validate_environment_and_files()
    assert database_url.endswith(db_name)
    assert schema_file == Path("db/schema.sql")
    assert dml_file == Path("data/db/seed.sql")


@pytest.mark.regression
def test_validate_environment_errors_when_baseline_files_are_missing(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    world_seed_api: LoadWorldSeedTestApi,
    capsys: pytest.CaptureFixture[str],
) -> None:
    """A missing db/schema.sql or data/db/seed.sql must fail loudly, not silently skip DDL/DML."""
    monkeypatch.setenv("DATABASE_URL", "postgresql://u:p@localhost:5432/mythos_unit")
    monkeypatch.setenv("CONFIRM_LOAD_WORLD_SEED", "1")
    monkeypatch.chdir(tmp_path)  # a fresh empty dir: guaranteed no db/schema.sql beneath it
    with pytest.raises(SystemExit) as exc_info:
        _ = world_seed_api.validate_environment_and_files()
    assert exc_info.value.code == 1
    assert "not found" in capsys.readouterr().out


# -- _reset_migration_ledger / _replay_migrations (#663) -----------------------------------


@pytest.mark.asyncio
@pytest.mark.regression
async def test_reset_migration_ledger_truncates_the_ledger_table(world_seed_api: LoadWorldSeedTestApi) -> None:
    """_reset_migration_ledger truncates schema_migrations in the target search_path's schema."""
    mock_conn = AsyncMock()
    with patch.object(world_seed_api.module, "asyncpg") as mock_asyncpg:
        mock_asyncpg.connect = AsyncMock(return_value=mock_conn)
        await world_seed_api.reset_migration_ledger("postgresql+asyncpg://u:p@localhost/mythos_unit", "mythos_unit")

    mock_asyncpg.connect.assert_awaited_once_with(
        "postgresql://u:p@localhost/mythos_unit", server_settings={"search_path": "mythos_unit"}
    )
    mock_conn.execute.assert_awaited_once_with('TRUNCATE TABLE "mythos_unit".schema_migrations')
    mock_conn.close.assert_awaited_once()


@pytest.mark.asyncio
@pytest.mark.regression
async def test_reset_migration_ledger_swallows_undefined_table(world_seed_api: LoadWorldSeedTestApi) -> None:
    """dbmate having never run against this database (no schema_migrations table yet) is not
    an error -- there is nothing to reset."""
    mock_conn = AsyncMock()
    with patch.object(world_seed_api.module, "asyncpg") as mock_asyncpg:
        mock_asyncpg.UndefinedTableError = Exception
        mock_asyncpg.connect = AsyncMock(return_value=mock_conn)
        mock_conn.execute = AsyncMock(side_effect=mock_asyncpg.UndefinedTableError())
        await world_seed_api.reset_migration_ledger("postgresql+asyncpg://u:p@localhost/mythos_unit", "mythos_unit")

    mock_conn.close.assert_awaited_once()


@pytest.mark.regression
def test_replay_migrations_raises_when_npx_missing(world_seed_api: LoadWorldSeedTestApi) -> None:
    """Missing npx on PATH must fail loudly, not silently skip replaying migrations."""
    with patch.object(world_seed_api.module.shutil, "which", return_value=None):
        with pytest.raises(FileNotFoundError, match="npx"):
            world_seed_api.replay_migrations("postgresql://u:p@localhost/mythos_unit", "mythos_unit")


@pytest.mark.regression
def test_replay_migrations_raises_on_nonzero_exit(world_seed_api: LoadWorldSeedTestApi) -> None:
    """A failed `dbmate up` must surface as an exception, not a silently-ignored return code."""
    with (
        patch.object(world_seed_api.module.shutil, "which", return_value="C:/npx.cmd"),
        patch.object(world_seed_api.module.subprocess, "run", return_value=MagicMock(returncode=1)) as mock_run,
    ):
        with pytest.raises(RuntimeError, match="dbmate up failed"):
            world_seed_api.replay_migrations("postgresql://u:p@localhost/mythos_unit", "mythos_unit")
    mock_run.assert_called_once()


@pytest.mark.regression
def test_replay_migrations_passes_url_via_env_not_argv(world_seed_api: LoadWorldSeedTestApi) -> None:
    """DATABASE_URL travels via the subprocess env block, not a --url argv entry -- a bare '&'
    in the query string (sslmode=disable&search_path=...) would otherwise be reinterpreted by
    cmd.exe when Windows launches npx's .cmd wrapper, even with shell=False."""
    with (
        patch.object(world_seed_api.module.shutil, "which", return_value="C:/npx.cmd"),
        patch.object(world_seed_api.module.subprocess, "run", return_value=MagicMock(returncode=0)) as mock_run,
    ):
        world_seed_api.replay_migrations("postgresql+asyncpg://u:p@localhost/mythos_unit", "mythos_unit")

    _args, kwargs = mock_run.call_args
    passed_cmd = _args[0]
    assert not any("--url" in str(part) for part in passed_cmd)
    assert "&" not in " ".join(str(part) for part in passed_cmd)
    assert (
        kwargs["env"]["DATABASE_URL"]
        == "postgresql://u:p@localhost/mythos_unit?sslmode=disable&search_path=mythos_unit"
    )
