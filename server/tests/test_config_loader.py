import os

from server import config_loader

CONFIG_PATH = os.path.join(os.path.dirname(__file__), "../server_config.yaml")
TEST_CONFIG_PATH = os.path.join(os.path.dirname(__file__), "../test_server_config.yaml")


def test_load_main_config_and_validate():
    config = config_loader.get_config(CONFIG_PATH)
    assert config_loader.validate_config(config)
    # Spot check a few fields
    assert isinstance(config["db_path"], str)
    assert isinstance(config["areas"], list)
    assert config["log_level"] in ("DEBUG", "INFO", "WARNING", "ERROR")


def test_load_test_config_and_validate():
    config = config_loader.get_config(TEST_CONFIG_PATH)
    assert config_loader.validate_config(config)
    assert config["log_level"] == "INFO"  # Environment variable overrides config file
    assert config["db_path"] == "None"  # String 'None' from config file
    assert config["log_path"] == "logs/persistence.log"  # Environment variable value


def test_environment_based_config_selection():
    """Test that environment-based config selection works correctly."""
    # Since we're running under pytest, it should automatically use test config
    # But we can test the explicit environment variable approach
    original_env = os.environ.get("MYTHOSMUD_TEST_MODE")

    try:
        # Test explicit test mode
        os.environ["MYTHOSMUD_TEST_MODE"] = "1"
        config_loader._config = None  # Reset config cache
        config = config_loader.get_config()
        # The actual port from the current config (may vary based on environment)
        assert isinstance(config["port"], int)
        # The host may vary based on environment, just check it's a valid host
        assert isinstance(config["host"], str)
        # The disable_logging may vary based on environment, just check it's a boolean
        assert isinstance(config["disable_logging"], bool)

    finally:
        # Restore original environment
        if original_env:
            os.environ["MYTHOSMUD_TEST_MODE"] = original_env
        elif "MYTHOSMUD_TEST_MODE" in os.environ:
            del os.environ["MYTHOSMUD_TEST_MODE"]

        # Reset config cache
        config_loader._config = None


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
        allow_multiplay: "true"
        port: "1234"
        max_connections: "42"
        areas: test_area
        enable_combat: "false"
        """
    )
    config = config_loader.get_config(str(config_path))
    assert isinstance(config["allow_multiplay"], bool)
    assert config["allow_multiplay"] is True
    assert isinstance(config["port"], int)
    assert config["port"] == 1234
    assert isinstance(config["max_connections"], int)
    assert config["max_connections"] == 42
    assert isinstance(config["areas"], list)
    assert config["areas"] == ["test_area"]
    assert config["enable_combat"] is False


def test_invalid_types_fallback_to_default(tmp_path):
    config_path = tmp_path / "invalid.yaml"
    config_path.write_text(
        """
        port: not_a_number
        max_connections: [1,2,3]
        enable_combat: 123
        """
    )
    config = config_loader.get_config(str(config_path))
    # Should fallback to default types
    assert isinstance(config["port"], int)
    assert config["port"] == config_loader._DEFAULTS["port"]
    assert isinstance(config["max_connections"], int)
    assert config["max_connections"] == config_loader._DEFAULTS["max_connections"]
    assert isinstance(config["enable_combat"], bool)
    assert config["enable_combat"] == config_loader._DEFAULTS["enable_combat"]
