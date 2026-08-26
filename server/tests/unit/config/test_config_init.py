"""
Unit tests for config module initialization.
"""

# pyright: reportPrivateUsage=false
# Reason: several tests exercise AppConfig's private CORS-sanitization helpers directly.

import json
import os
from unittest.mock import patch

import pytest
from pydantic_settings import BaseSettings, SettingsError

from server.config import get_config, reset_config
from server.config.models.app import AppConfig


def test_get_config_returns_app_config():
    """Test that get_config() returns an AppConfig object."""
    config = get_config()

    assert config is not None
    assert hasattr(config, "game")
    assert hasattr(config, "server")
    assert hasattr(config, "database")


def test_get_config_fresh_instances_in_test_mode():
    """Test that get_config() returns fresh instances in test mode."""
    config1 = get_config()
    config2 = get_config()

    # In test mode, should return different instances
    assert config1 is not config2


def test_reset_config_in_test_mode():
    """Test that reset_config() works in test mode."""
    config1 = get_config()
    reset_config()
    config2 = get_config()

    # Should still return fresh instances
    assert config1 is not config2


def test_get_config_has_server_config():
    """Test that config has server configuration."""
    config = get_config()

    assert config.server is not None
    assert hasattr(config.server, "host")
    assert hasattr(config.server, "port")
    assert isinstance(config.server.port, int)


def test_get_config_has_database_config():
    """Test that config has database configuration."""
    config = get_config()

    assert config.database is not None
    assert hasattr(config.database, "url")
    assert hasattr(config.database, "npc_url")
    assert isinstance(config.database.url, str)


def test_get_config_has_game_config():
    """Test that config has game configuration."""
    config = get_config()

    assert config.game is not None
    assert hasattr(config.game, "aliases_dir")


@pytest.mark.parametrize("env_key", ["CORS_ALLOW_ORIGINS", "CORS_ORIGINS", "CORS_ALLOWED_ORIGINS", "ALLOWED_ORIGINS"])
def test_first_cors_origins_env_returns_first_match(monkeypatch: pytest.MonkeyPatch, env_key: str) -> None:
    """_first_cors_origins_env returns the value of whichever CORS env var is set."""
    for key in ("CORS_ALLOW_ORIGINS", "CORS_ORIGINS", "CORS_ALLOWED_ORIGINS", "ALLOWED_ORIGINS"):
        monkeypatch.delenv(key, raising=False)
    monkeypatch.setenv(env_key, "http://example.com")

    assert AppConfig._first_cors_origins_env() == "http://example.com"


def test_first_cors_origins_env_none_when_unset(monkeypatch: pytest.MonkeyPatch) -> None:
    """_first_cors_origins_env returns None when no CORS origin env var is set."""
    for key in ("CORS_ALLOW_ORIGINS", "CORS_ORIGINS", "CORS_ALLOWED_ORIGINS", "ALLOWED_ORIGINS"):
        monkeypatch.delenv(key, raising=False)

    assert AppConfig._first_cors_origins_env() is None


def test_sanitize_environment_for_nested_configs_converts_comma_separated(monkeypatch: pytest.MonkeyPatch) -> None:
    """A comma-separated CORS origins env var is rewritten as a JSON list across all its aliases."""
    # The method under test writes CORS_ORIGINS and CORS_ALLOWED_ORIGINS directly via os.environ, not
    # through monkeypatch. monkeypatch.delenv() on an unset var records no undo action at all, so use
    # setenv() (which always tracks, even for a previously-unset key) to guarantee teardown reverts them.
    monkeypatch.setenv("CORS_ORIGINS", "placeholder")
    monkeypatch.setenv("CORS_ALLOWED_ORIGINS", "placeholder")
    monkeypatch.setenv("CORS_ALLOW_ORIGINS", "http://a.example, http://b.example")

    AppConfig._sanitize_environment_for_nested_configs()

    expected = ["http://a.example", "http://b.example"]
    assert json.loads(os.environ["CORS_ALLOW_ORIGINS"]) == expected
    assert json.loads(os.environ["CORS_ORIGINS"]) == expected
    assert json.loads(os.environ["CORS_ALLOWED_ORIGINS"]) == expected


def test_sanitize_environment_for_nested_configs_noop_when_already_json(monkeypatch: pytest.MonkeyPatch) -> None:
    """A CORS origins env var that already looks like JSON is left untouched."""
    monkeypatch.setenv("CORS_ALLOW_ORIGINS", '["http://a.example"]')

    AppConfig._sanitize_environment_for_nested_configs()  # must not raise

    assert os.environ["CORS_ALLOW_ORIGINS"] == '["http://a.example"]'


def test_sanitize_environment_for_nested_configs_noop_when_only_commas(monkeypatch: pytest.MonkeyPatch) -> None:
    """A CORS origins env var of only commas/whitespace parses to nothing and is left alone."""
    monkeypatch.setenv("CORS_ALLOW_ORIGINS", " , , ")

    AppConfig._sanitize_environment_for_nested_configs()  # must not raise

    assert os.environ["CORS_ALLOW_ORIGINS"] == " , , "


def test_sanitize_environment_for_nested_configs_noop_when_unset(monkeypatch: pytest.MonkeyPatch) -> None:
    """_sanitize_environment_for_nested_configs is a no-op when no CORS origin env var is set."""
    for key in ("CORS_ALLOW_ORIGINS", "CORS_ORIGINS", "CORS_ALLOWED_ORIGINS", "ALLOWED_ORIGINS"):
        monkeypatch.delenv(key, raising=False)

    AppConfig._sanitize_environment_for_nested_configs()  # must not raise


def test_appconfig_init_retries_after_settings_error_naming_allow_origins() -> None:
    """AppConfig.__init__ sanitizes and retries once when construction fails on allow_origins."""
    call_count = 0
    real_init = BaseSettings.__init__

    def fake_init(self: BaseSettings, **kwargs: object) -> None:
        nonlocal call_count
        call_count += 1
        if call_count == 1:
            raise SettingsError('error parsing value for field "allow_origins" from source EnvSettingsSource')
        real_init(self, **kwargs)  # pyright: ignore[reportArgumentType]  # Reason: forwarding a generic kwargs dict through a mocked __init__ boundary

    with patch.object(BaseSettings, "__init__", fake_init):
        config = AppConfig()

    assert call_count >= 2
    assert config.cors is not None


def test_appconfig_init_reraises_settings_error_unrelated_to_allow_origins() -> None:
    """AppConfig.__init__ does not swallow a SettingsError unrelated to allow_origins."""
    call_count = 0

    def fake_init(_self: BaseSettings, **_kwargs: object) -> None:
        nonlocal call_count
        call_count += 1
        raise SettingsError('error parsing value for field "port" from source EnvSettingsSource')

    with patch.object(BaseSettings, "__init__", fake_init), pytest.raises(SettingsError):
        _ = AppConfig()

    assert call_count == 1
