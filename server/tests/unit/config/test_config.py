"""
Unit tests for configuration system.
"""

from server.config import get_config, reset_config


def test_get_config_returns_app_config():
    """Test that get_config() returns an AppConfig object."""
    config = get_config()

    assert hasattr(config, "game")
    assert hasattr(config, "server")
    assert hasattr(config, "database")


def test_get_config_test_mode_returns_fresh_instances():
    """Test that get_config() returns fresh instances in test mode."""
    config1 = get_config()
    config2 = get_config()

    # In test mode, should return fresh instances (not singletons)
    assert config1 is not config2


def test_reset_config_clears_state():
    """Test that reset_config() clears global state."""
    config1 = get_config()
    reset_config()
    config2 = get_config()

    # Should be different instances after reset
    assert config1 is not config2


def test_get_config_has_server_config():
    """Test that config has server configuration."""
    config = get_config()

    assert hasattr(config.server, "host")
    assert hasattr(config.server, "port")
    assert isinstance(config.server.port, int)


def test_get_config_has_database_config():
    """Test that config has database configuration."""
    config = get_config()

    assert hasattr(config.database, "url")
    assert hasattr(config.database, "npc_url")
    assert config.database.url.startswith("postgresql")


def test_get_config_has_game_config():
    """Test that config has game configuration."""
    config = get_config()

    assert hasattr(config.game, "aliases_dir")
    assert isinstance(config.game.aliases_dir, str)
