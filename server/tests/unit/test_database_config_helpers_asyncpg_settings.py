"""Unit tests for get_asyncpg_server_settings_for_database_url."""

import pytest

from server.database_config_helpers import get_asyncpg_server_settings_for_database_url


@pytest.fixture
def clear_postgres_search_path(monkeypatch: pytest.MonkeyPatch) -> None:
    """Ensure POSTGRES_SEARCH_PATH does not leak between cases."""
    monkeypatch.delenv("POSTGRES_SEARCH_PATH", raising=False)


@pytest.mark.usefixtures("clear_postgres_search_path")
def test_mythos_unit_defaults_search_path_to_db_name() -> None:
    """Known env DBs must set search_path to the database name when env override is unset."""
    url = "postgresql://u:p@localhost:5432/mythos_unit"
    assert get_asyncpg_server_settings_for_database_url(url) == {"search_path": "mythos_unit"}


@pytest.mark.usefixtures("clear_postgres_search_path")
def test_mythos_e2e_defaults_search_path_to_db_name() -> None:
    url = "postgresql://u:p@h:5432/mythos_e2e?sslmode=require"
    assert get_asyncpg_server_settings_for_database_url(url) == {"search_path": "mythos_e2e"}


def test_respects_postgres_search_path_when_matches_db_name(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    """When POSTGRES_SEARCH_PATH matches the DB name, keep that search_path."""
    monkeypatch.setenv("POSTGRES_SEARCH_PATH", "mythos_dev")
    url = "postgresql://u:p@localhost:5432/mythos_dev"
    assert get_asyncpg_server_settings_for_database_url(url) == {"search_path": "mythos_dev"}


def test_unknown_database_uses_postgres_search_path_when_set(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    """Non-mythos_* URLs still honor POSTGRES_SEARCH_PATH."""
    monkeypatch.setenv("POSTGRES_SEARCH_PATH", "custom_schema")
    url = "postgresql://u:p@localhost:5432/otherdb"
    assert get_asyncpg_server_settings_for_database_url(url) == {"search_path": "custom_schema"}


@pytest.mark.usefixtures("clear_postgres_search_path")
def test_unknown_database_empty_when_no_env() -> None:
    """Other databases without POSTGRES_SEARCH_PATH get no server_settings."""
    url = "postgresql://u:p@localhost:5432/otherdb"
    assert get_asyncpg_server_settings_for_database_url(url) == {}
