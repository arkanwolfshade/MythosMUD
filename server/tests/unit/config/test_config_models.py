"""
Unit tests for configuration models.
"""

import os
from unittest.mock import patch

import pytest

from server.config.models import (
    DatabaseConfig,
    ServerConfig,
    _default_cors_origins,
    _parse_env_list,
)


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
        assert "http://example.com" in result


def test_server_config_default_host():
    """Test ServerConfig default host."""
    with patch.dict(os.environ, {"SERVER_PORT": "54731"}, clear=False):
        config = ServerConfig()
        assert config.host == "127.0.0.1"


def test_server_config_validate_port_valid():
    """Test ServerConfig port validation with valid port."""
    with patch.dict(os.environ, {"SERVER_PORT": "54731"}, clear=False):
        config = ServerConfig()
        assert config.port == 54731


def test_server_config_validate_port_invalid_low():
    """Test ServerConfig port validation with port too low."""
    with patch.dict(os.environ, {"SERVER_PORT": "1000"}, clear=False):
        with pytest.raises(ValueError, match="Port must be between 1024 and 65535"):
            ServerConfig()


def test_server_config_validate_port_invalid_high():
    """Test ServerConfig port validation with port too high."""
    with patch.dict(os.environ, {"SERVER_PORT": "70000"}, clear=False):
        with pytest.raises(ValueError, match="Port must be between 1024 and 65535"):
            ServerConfig()


def test_database_config_validate_url_postgresql():
    """Test DatabaseConfig URL validation with PostgreSQL URL."""
    with patch.dict(
        os.environ,
        {
            "DATABASE_URL": "postgresql+asyncpg://user:pass@localhost/db",
            "DATABASE_NPC_URL": "postgresql+asyncpg://user:pass@localhost/db",
        },
        clear=False,
    ):
        config = DatabaseConfig()
        assert config.url.startswith("postgresql")


def test_database_config_validate_url_empty():
    """Test DatabaseConfig URL validation with empty URL."""
    with patch.dict(os.environ, {"DATABASE_URL": "", "DATABASE_NPC_URL": ""}, clear=False):
        with pytest.raises(ValueError, match="Database URL cannot be empty"):
            DatabaseConfig()


def test_database_config_validate_pool_config_positive():
    """Test DatabaseConfig pool config validation with positive values."""
    with patch.dict(
        os.environ,
        {
            "DATABASE_URL": "postgresql+asyncpg://user:pass@localhost/db",
            "DATABASE_NPC_URL": "postgresql+asyncpg://user:pass@localhost/db",
            "DATABASE_POOL_SIZE": "5",
        },
        clear=False,
    ):
        config = DatabaseConfig()
        assert config.pool_size == 5


def test_database_config_validate_pool_config_invalid():
    """Test DatabaseConfig pool config validation with invalid value."""
    with patch.dict(
        os.environ,
        {
            "DATABASE_URL": "postgresql+asyncpg://user:pass@localhost/db",
            "DATABASE_NPC_URL": "postgresql+asyncpg://user:pass@localhost/db",
            "DATABASE_POOL_SIZE": "0",
        },
        clear=False,
    ):
        with pytest.raises(ValueError, match="Pool configuration values must be at least 1"):
            DatabaseConfig()
