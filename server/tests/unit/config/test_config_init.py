"""
Unit tests for config module initialization.
"""

from server.config import get_config, reset_config


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
