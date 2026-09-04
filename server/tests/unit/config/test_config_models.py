"""
Unit tests for configuration models.
"""

import os
from unittest.mock import patch

import pytest

from server.config.models import (
    DatabaseConfig,
    GameConfig,
    ServerConfig,
    _default_cors_origins,
    _parse_env_list,
)

_POSTGRESQL_DATABASE_URL = "postgresql+asyncpg://user:pass@localhost/db"

# pylint: disable=protected-access  # Reason: Test file - accessing protected members is standard practice for unit testing
# pylint: disable=redefined-outer-name  # Reason: Test file - pytest fixture parameter names must match fixture names, causing intentional redefinitions

# pyright: reportPrivateUsage=false
# Reason: unit tests patch and assert ScheduleService private state by design.


def test_parse_env_list_none():
    """Test parsing None as env list."""
    result = _parse_env_list(None)
    assert result == []


def test_parse_env_list_empty_string():
    """Test parsing empty string as env list."""
    result = _parse_env_list("")
    assert result == []


def test_parse_env_list_json():
    """Test parsing JSON list."""
    result = _parse_env_list('["a", "b", "c"]')
    assert result == ["a", "b", "c"]


def test_parse_env_list_csv():
    """Test parsing CSV list."""
    result = _parse_env_list("a, b, c")
    assert result == ["a", "b", "c"]


def test_default_cors_origins_no_env():
    """Test default CORS origins when no env vars set."""
    with patch.dict(os.environ, {}, clear=True):
        result = _default_cors_origins()
        assert "http://localhost:5173" in result
        assert "http://127.0.0.1:5173" in result


def test_default_cors_origins_with_env():
    """Test default CORS origins with env var set."""
    with patch.dict(os.environ, {"CORS_ALLOW_ORIGINS": '["http://example.com"]'}, clear=False):
        result = _default_cors_origins()
        # Use exact equality check instead of 'in' operator to avoid CodeQL alert
        # This ensures we're checking for exact list match, not substring matching
        assert isinstance(result, list)
        assert result == ["http://example.com"]


def test_server_config_default_host():
    """Test ServerConfig default host."""
    config = ServerConfig(port=54768)
    assert config.host == "127.0.0.1"


def test_server_config_validate_port_valid():
    """Test ServerConfig port validation with valid port."""
    config = ServerConfig(port=54768)
    assert config.port == 54768


def test_server_config_validate_port_invalid_low():
    """Test ServerConfig port validation with port too low."""
    with pytest.raises(ValueError, match="Port must be between 1024 and 65535"):
        _ = ServerConfig(port=1000)


def test_server_config_validate_port_invalid_high():
    """Test ServerConfig port validation with port too high."""
    with pytest.raises(ValueError, match="Port must be between 1024 and 65535"):
        _ = ServerConfig(port=70000)


_GAME_CONFIG_ALIASES_DIR = "data/aliases"


def test_game_config_default_tick_rate():
    """Test GameConfig server_tick_rate default value still constructs cleanly."""
    config = GameConfig(aliases_dir=_GAME_CONFIG_ALIASES_DIR)
    assert config.server_tick_rate == 0.1


def test_game_config_tick_rate_accepts_positive_override():
    """Test GameConfig server_tick_rate accepts a valid positive override."""
    config = GameConfig(aliases_dir=_GAME_CONFIG_ALIASES_DIR, server_tick_rate=0.5)
    assert config.server_tick_rate == 0.5


def test_game_config_tick_rate_rejects_zero():
    """Test GameConfig server_tick_rate rejects zero (#622: busy-spins the tick loop and raises
    ZeroDivisionError in login grace period handling)."""
    with pytest.raises(ValueError, match="greater than 0"):
        _ = GameConfig(aliases_dir=_GAME_CONFIG_ALIASES_DIR, server_tick_rate=0)


def test_game_config_tick_rate_rejects_negative():
    """Test GameConfig server_tick_rate rejects negative values (#622: crashes the tick loop via
    asyncio.sleep's non-negative requirement)."""
    with pytest.raises(ValueError, match="greater than 0"):
        _ = GameConfig(aliases_dir=_GAME_CONFIG_ALIASES_DIR, server_tick_rate=-0.1)


def _make_game_config(field: str, value: float) -> GameConfig:
    """Construct GameConfig with one grace/countdown field set to `value`, others default.

    Avoids `GameConfig(**{field: value})`: pyright cannot type-check a `**dict` unpacking
    against GameConfig's per-field __init__ signature, since `value`'s type would be checked
    against every possible keyword field -- including str-typed ones like default_player_room.
    """
    if field == "disconnect_grace_period_seconds":
        return GameConfig(aliases_dir=_GAME_CONFIG_ALIASES_DIR, disconnect_grace_period_seconds=value)
    if field == "login_grace_period_seconds":
        return GameConfig(aliases_dir=_GAME_CONFIG_ALIASES_DIR, login_grace_period_seconds=value)
    if field == "rest_countdown_seconds":
        return GameConfig(aliases_dir=_GAME_CONFIG_ALIASES_DIR, rest_countdown_seconds=value)
    raise ValueError(f"Unknown grace/countdown field: {field}")


def test_game_config_grace_period_defaults() -> None:
    """#297: the three grace/countdown durations default to their prior hardcoded values."""
    config = GameConfig(aliases_dir=_GAME_CONFIG_ALIASES_DIR)
    assert config.disconnect_grace_period_seconds == 30.0
    assert config.login_grace_period_seconds == 10.0
    assert config.rest_countdown_seconds == 10.0


@pytest.mark.parametrize(
    "field",
    ["disconnect_grace_period_seconds", "login_grace_period_seconds", "rest_countdown_seconds"],
)
def test_game_config_grace_period_accepts_override(field: str) -> None:
    """#297: each grace/countdown duration is independently retunable."""
    config = _make_game_config(field, 45.0)
    assert getattr(config, field) == 45.0


@pytest.mark.parametrize(
    "field",
    ["disconnect_grace_period_seconds", "login_grace_period_seconds", "rest_countdown_seconds"],
)
def test_game_config_grace_period_rejects_zero(field: str) -> None:
    """#297: a zero grace/countdown period would silently disable the corresponding feature."""
    with pytest.raises(ValueError, match="between 1 and 600"):
        _ = _make_game_config(field, 0.0)


@pytest.mark.parametrize(
    "field",
    ["disconnect_grace_period_seconds", "login_grace_period_seconds", "rest_countdown_seconds"],
)
def test_game_config_grace_period_rejects_over_max(field: str) -> None:
    """#297: an absurdly large grace/countdown period is rejected, matching the other Field
    validators' range-bounding convention in this model."""
    with pytest.raises(ValueError, match="between 1 and 600"):
        _ = _make_game_config(field, 601.0)


def test_database_config_validate_url_postgresql():
    """Test DatabaseConfig URL validation with PostgreSQL URL."""
    config = DatabaseConfig(url=_POSTGRESQL_DATABASE_URL, npc_url=_POSTGRESQL_DATABASE_URL)
    assert config.url.startswith("postgresql")


def test_database_config_validate_url_empty():
    """Test DatabaseConfig URL validation with empty URL."""
    with pytest.raises(ValueError, match="Database URL cannot be empty"):
        _ = DatabaseConfig(url="", npc_url="")


def test_database_config_validate_pool_config_positive():
    """Test DatabaseConfig pool config validation with positive values."""
    config = DatabaseConfig(url=_POSTGRESQL_DATABASE_URL, npc_url=_POSTGRESQL_DATABASE_URL, pool_size=5)
    assert config.pool_size == 5


def test_database_config_validate_pool_config_invalid():
    """Test DatabaseConfig pool config validation with invalid value."""
    with pytest.raises(ValueError, match="Pool configuration values must be at least 1"):
        _ = DatabaseConfig(url=_POSTGRESQL_DATABASE_URL, npc_url=_POSTGRESQL_DATABASE_URL, pool_size=0)
