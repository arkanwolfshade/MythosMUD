"""Regression tests for scripts/load_world_seed.py (URL parsing, allowlist, search_path)."""

# Script helpers are underscore-prefixed on the real module; we cast importlib output to this
# Protocol once, then expose a small public API dataclass for tests.
# pylint: disable=protected-access

from __future__ import annotations

import importlib.util
from collections.abc import Callable
from dataclasses import dataclass
from pathlib import Path
from typing import Protocol, cast

import pytest

PROJECT_ROOT = Path(__file__).resolve().parents[4]
SCRIPT_PATH = PROJECT_ROOT / "scripts" / "load_world_seed.py"


class _LoadWorldSeedScriptInternals(Protocol):
    """Attributes of scripts/load_world_seed.py we read after dynamic import (not on ModuleType stub)."""

    _database_url_for_cli: Callable[[str], str]
    _parse_pg_url_for_psql: Callable[[str], tuple[str, int, str, str, str]]
    _validate_environment_and_files: Callable[[], tuple[str, Path, Path]]
    _asyncpg_server_settings: Callable[[str], dict[str, str]]


@dataclass(frozen=True, slots=True)
class LoadWorldSeedTestApi:
    """Typed facade over scripts/load_world_seed.py helpers (dynamic import)."""

    database_url_for_cli: Callable[[str], str]
    parse_pg_url_for_psql: Callable[[str], tuple[str, int, str, str, str]]
    validate_environment_and_files: Callable[[], tuple[str, Path, Path]]
    asyncpg_server_settings: Callable[[str], dict[str, str]]


def _load_script_module() -> LoadWorldSeedTestApi:
    spec = importlib.util.spec_from_file_location("load_world_seed_script", SCRIPT_PATH)
    assert spec is not None and spec.loader is not None
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    loaded = cast(_LoadWorldSeedScriptInternals, cast(object, mod))
    return LoadWorldSeedTestApi(
        database_url_for_cli=loaded._database_url_for_cli,  # pyright: ignore[reportPrivateUsage] -- script module API
        parse_pg_url_for_psql=loaded._parse_pg_url_for_psql,  # pyright: ignore[reportPrivateUsage] -- script module API
        validate_environment_and_files=loaded._validate_environment_and_files,  # pyright: ignore[reportPrivateUsage]
        asyncpg_server_settings=loaded._asyncpg_server_settings,  # pyright: ignore[reportPrivateUsage]
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
