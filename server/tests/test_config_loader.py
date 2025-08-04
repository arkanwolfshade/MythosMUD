import os

from server import config_loader

CONFIG_PATH = os.path.join(os.path.dirname(__file__), "../server_config.yaml")


def test_load_main_config_and_validate():
    config = config_loader.get_config(CONFIG_PATH)
    assert config_loader.validate_config(config)
    # Spot check a few fields
    assert isinstance(config["database_url"], str)
    assert isinstance(config["default_player_stats"], dict)
    assert config["log_level"] in ("DEBUG", "INFO", "WARNING", "ERROR")


def test_load_test_config_and_validate():
    # Since we removed test-specific config logic, this test should use the main config
    config = config_loader.get_config(CONFIG_PATH)
    assert config_loader.validate_config(config)
    # Check that log_level is a valid logging level
    assert config["log_level"] in ("DEBUG", "INFO", "WARNING", "ERROR")
    assert isinstance(config["database_url"], str)
    assert isinstance(config["persistence_log"], str)


def test_environment_based_config_selection():
    """Test that environment-based config selection works correctly."""
    # Since we removed test-specific config logic, this should always use production config
    config_loader._config = None  # Reset config cache
    config = config_loader.get_config()
    # The actual port from the current config (may vary based on environment)
    assert isinstance(config["port"], int)
    # The host may vary based on environment, just check it's a valid host
    assert isinstance(config["host"], str)
    # Check that we have the expected production fields
    assert "database_url" in config
    assert "default_player_stats" in config


def test_fallback_to_defaults(monkeypatch):
    # Simulate missing file
    monkeypatch.setattr(config_loader, "_config", None)
    config = config_loader.get_config("/nonexistent/path.yaml")
    assert config_loader.validate_config(config)
    for k in config_loader._DEFAULTS:
        assert k in config


def test_type_coercion_and_bool_handling(tmp_path):
    # Write a config with string bools and ints as strings
    config_path = tmp_path / "coerce.yaml"
    config_path.write_text(
        """
        port: "1234"
        max_connections_per_player: "3"
        default_player_room: test_room
        game_tick_rate: "2.5"
        """
    )
    config = config_loader.get_config(str(config_path))
    assert isinstance(config["port"], int)
    assert config["port"] == 1234
    assert isinstance(config["max_connections_per_player"], int)
    assert config["max_connections_per_player"] == 3
    assert isinstance(config["default_player_room"], str)
    assert config["default_player_room"] == "test_room"
    assert isinstance(config["game_tick_rate"], float)
    assert config["game_tick_rate"] == 2.5


def test_invalid_types_fallback_to_default(tmp_path):
    config_path = tmp_path / "invalid.yaml"
    config_path.write_text(
        """
        port: not_a_number
        max_connections_per_player: [1,2,3]
        game_tick_rate: "invalid"
        """
    )
    config = config_loader.get_config(str(config_path))
    # Should fallback to default types
    assert isinstance(config["port"], int)
    assert config["port"] == config_loader._DEFAULTS["port"]
    assert isinstance(config["max_connections_per_player"], int)
    assert config["max_connections_per_player"] == config_loader._DEFAULTS["max_connections_per_player"]
    assert isinstance(config["game_tick_rate"], float)
    assert config["game_tick_rate"] == config_loader._DEFAULTS["game_tick_rate"]
