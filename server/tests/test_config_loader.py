import os

from server import config_loader

# Use unit test configuration for config loader tests
CONFIG_PATH = os.path.join(os.path.dirname(__file__), "../server_config.unit_test.yaml")


def test_load_main_config_and_validate():
    config = config_loader.get_config(CONFIG_PATH)
    assert config_loader.validate_config(config)
    # Spot check a few fields
    assert isinstance(config["database_url"], str)
    assert isinstance(config["default_player_stats"], dict)
    # Check new logging configuration structure
    assert "logging" in config
    assert config["logging"]["level"] in ("DEBUG", "INFO", "WARNING", "ERROR")


def test_load_test_config_and_validate():
    # Since we removed test-specific config logic, this test should use the main config
    config = config_loader.get_config(CONFIG_PATH)
    assert config_loader.validate_config(config)
    # Check new logging configuration structure
    assert "logging" in config
    assert config["logging"]["level"] in ("DEBUG", "INFO", "WARNING", "ERROR")
    assert isinstance(config["database_url"], str)
    # Check that log_base is configured
    assert isinstance(config["logging"]["log_base"], str)


def test_environment_based_config_selection():
    """Test that environment-based config selection requires explicit configuration."""
    import pytest

    # Reset config cache
    config_loader._config = None

    # Test 1: Should raise ValueError if MYTHOSMUD_CONFIG_PATH is not set
    import os

    original_path = os.environ.get("MYTHOSMUD_CONFIG_PATH")
    try:
        if "MYTHOSMUD_CONFIG_PATH" in os.environ:
            del os.environ["MYTHOSMUD_CONFIG_PATH"]

        with pytest.raises(ValueError, match="MYTHOSMUD_CONFIG_PATH environment variable is not set"):
            config_loader.get_config()
    finally:
        # Restore original environment
        if original_path:
            os.environ["MYTHOSMUD_CONFIG_PATH"] = original_path
        config_loader._config = None

    # Test 2: Should load config when MYTHOSMUD_CONFIG_PATH is properly set
    config = config_loader.get_config(CONFIG_PATH)
    assert isinstance(config["port"], int)
    assert isinstance(config["host"], str)
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


def test_aliases_dir_required(monkeypatch, tmp_path):
    """
    Regression test for ALIASES_DIR configuration requirement.

    This test ensures that the system properly validates the presence of ALIASES_DIR
    environment variable, preventing silent command processing failures.

    Context: Bug fix for issue where commands failed silently when ALIASES_DIR was not set.
    """
    import pytest

    from server.alias_storage import AliasStorage

    # Test 1: AliasStorage should raise ValueError when ALIASES_DIR is not set and no storage_dir provided
    monkeypatch.delenv("ALIASES_DIR", raising=False)
    with pytest.raises(ValueError, match="ALIASES_DIR environment variable must be set"):
        AliasStorage()

    # Test 2: AliasStorage should work when explicit storage_dir is provided
    test_dir = tmp_path / "aliases"
    storage = AliasStorage(storage_dir=str(test_dir))
    assert storage.storage_dir.exists()

    # Test 3: AliasStorage should work when ALIASES_DIR environment variable is set
    env_dir = tmp_path / "env_aliases"
    monkeypatch.setenv("ALIASES_DIR", str(env_dir))
    storage_from_env = AliasStorage()
    assert storage_from_env.storage_dir == env_dir
    assert storage_from_env.storage_dir.exists()
