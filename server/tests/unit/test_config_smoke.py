"""
Smoke test for configuration system.
"""

from server.config import get_config


def test_get_config_returns_app_config():
    """Test that get_config() returns an AppConfig object with expected structure."""
    config = get_config()

    # Verify it has the expected attributes
    assert hasattr(config, "game")
    assert hasattr(config, "server")
    assert hasattr(config, "database")

    # Verify game config has some default fields
    assert config.game is not None
    assert hasattr(config.game, "aliases_dir")
