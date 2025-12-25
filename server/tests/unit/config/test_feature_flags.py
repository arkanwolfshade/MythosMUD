"""
Tests for feature flag system and configuration management.

These tests verify that the feature flag system properly enables/disables
combat features, handles configuration changes, and provides monitoring capabilities.
"""

import os
from typing import cast

import pytest
from pydantic import ValidationError

from server.config import get_config, reset_config
from server.config.models import AppConfig, GameConfig

# Apply serial markers to entire module to prevent worker crashes in full suite
# All test classes modify global config state via autouse fixtures
pytestmark = [pytest.mark.serial, pytest.mark.xdist_group("serial_config_tests")]


class TestFeatureFlagSystem:
    """Test feature flag system for combat enable/disable."""

    # Apply serial markers to entire class to prevent worker crashes in full suite
    pytestmark = [pytest.mark.serial, pytest.mark.xdist_group("serial_config_tests")]

    @pytest.fixture(autouse=True)
    def setup_test_env(self, monkeypatch):
        """Set up test environment variables."""
        # Set required environment variables
        monkeypatch.setenv("SERVER_PORT", "54731")
        monkeypatch.setenv("DATABASE_URL", "postgresql+asyncpg://postgres:Cthulhu1@localhost:5432/mythos_unit")
        monkeypatch.setenv("DATABASE_NPC_URL", "postgresql+asyncpg://postgres:Cthulhu1@localhost:5432/mythos_unit")
        monkeypatch.setenv("MYTHOSMUD_ADMIN_PASSWORD", "test_admin_pass")
        monkeypatch.setenv("LOGGING_ENVIRONMENT", "unit_test")
        monkeypatch.setenv("GAME_ALIASES_DIR", "data/unit_test/players/aliases")

        # Reset config cache before each test
        reset_config()

        yield

        # Clean up after test
        reset_config()

    @pytest.mark.serial  # Class uses autouse fixture that modifies global config state
    @pytest.mark.xdist_group(name="serial_config_tests")  # Force serial execution with pytest-xdist
    def test_combat_feature_flag_enabled_by_default(self) -> None:
        """Test that combat is enabled by default."""
        config = GameConfig(aliases_dir=os.getenv("GAME_ALIASES_DIR") or "data/aliases" or "data/aliases")
        assert config.combat_enabled is True

    @pytest.mark.serial  # Class uses autouse fixture that modifies global config state
    @pytest.mark.xdist_group(name="serial_config_tests")  # Force serial execution with pytest-xdist
    def test_combat_feature_flag_can_be_disabled(self) -> None:
        """Test that combat can be disabled via configuration."""
        config = GameConfig(aliases_dir=os.getenv("GAME_ALIASES_DIR") or "data/aliases", combat_enabled=False)
        assert config.combat_enabled is False

    @pytest.mark.serial  # Class uses autouse fixture that modifies global config state
    @pytest.mark.xdist_group(name="serial_config_tests")  # Force serial execution with pytest-xdist
    def test_combat_feature_flag_from_environment(self, monkeypatch):
        """Test that combat feature flag can be set via environment variable."""
        monkeypatch.setenv("GAME_COMBAT_ENABLED", "false")

        config = GameConfig(aliases_dir=os.getenv("GAME_ALIASES_DIR") or "data/aliases")
        assert config.combat_enabled is False

    @pytest.mark.serial  # Class uses autouse fixture that modifies global config state
    @pytest.mark.xdist_group(name="serial_config_tests")  # Force serial execution with pytest-xdist
    def test_combat_feature_flag_environment_override(self, monkeypatch):
        """Test that environment variable overrides default value."""
        monkeypatch.setenv("GAME_COMBAT_ENABLED", "true")

        # When no explicit value is provided, environment variable should be used
        config = GameConfig(aliases_dir=os.getenv("GAME_ALIASES_DIR") or "data/aliases")
        assert config.combat_enabled is True

    @pytest.mark.serial  # Class uses autouse fixture that modifies global config state
    @pytest.mark.xdist_group(name="serial_config_tests")  # Force serial execution with pytest-xdist
    def test_combat_configuration_settings(self) -> None:
        """Test combat-specific configuration settings."""
        config = GameConfig(
            aliases_dir=os.getenv("GAME_ALIASES_DIR") or "data/aliases",
            combat_enabled=True,
            combat_tick_interval=10,
            combat_timeout_seconds=300,
            combat_xp_multiplier=1.5,
            combat_logging_enabled=True,
        )

        assert config.combat_enabled is True
        assert config.combat_tick_interval == 10
        assert config.combat_timeout_seconds == 300
        assert config.combat_xp_multiplier == 1.5
        assert config.combat_logging_enabled is True

    @pytest.mark.serial  # Class uses autouse fixture that modifies global config state
    @pytest.mark.xdist_group(name="serial_config_tests")  # Force serial execution with pytest-xdist
    def test_combat_configuration_defaults(self) -> None:
        """Test combat configuration default values."""
        config = GameConfig(aliases_dir=os.getenv("GAME_ALIASES_DIR") or "data/aliases")

        assert config.combat_enabled is True
        assert config.combat_tick_interval == 6
        assert config.combat_timeout_seconds == 180
        assert config.combat_xp_multiplier == 1.0
        assert config.combat_logging_enabled is True

    @pytest.mark.serial  # Class uses autouse fixture that modifies global config state
    @pytest.mark.xdist_group(name="serial_config_tests")  # Force serial execution with pytest-xdist
    def test_combat_configuration_validation(self) -> None:
        """Test combat configuration validation."""
        # Valid values should pass
        config = GameConfig(
            aliases_dir=os.getenv("GAME_ALIASES_DIR") or "data/aliases",
            combat_tick_interval=5,
            combat_timeout_seconds=120,
            combat_xp_multiplier=2.0,
        )
        assert config.combat_tick_interval == 5
        assert config.combat_timeout_seconds == 120
        assert config.combat_xp_multiplier == 2.0

    @pytest.mark.serial  # Class uses autouse fixture that modifies global config state
    @pytest.mark.xdist_group(name="serial_config_tests")  # Force serial execution with pytest-xdist
    def test_combat_configuration_invalid_tick_interval(self) -> None:
        """Test invalid combat tick interval is rejected."""
        with pytest.raises(ValidationError) as exc_info:
            GameConfig(aliases_dir=os.getenv("GAME_ALIASES_DIR") or "data/aliases", combat_tick_interval=0)
        assert "Combat tick interval must be between 1 and 60 seconds" in str(exc_info.value)

    @pytest.mark.serial  # Class uses autouse fixture that modifies global config state
    @pytest.mark.xdist_group(name="serial_config_tests")  # Force serial execution with pytest-xdist
    def test_combat_configuration_invalid_timeout(self) -> None:
        """Test invalid combat timeout is rejected."""
        with pytest.raises(ValidationError) as exc_info:
            GameConfig(aliases_dir=os.getenv("GAME_ALIASES_DIR") or "data/aliases", combat_timeout_seconds=30)
        assert "Combat timeout must be between 60 and 1800 seconds" in str(exc_info.value)

    @pytest.mark.serial  # Class uses autouse fixture that modifies global config state
    @pytest.mark.xdist_group(name="serial_config_tests")  # Force serial execution with pytest-xdist
    def test_combat_configuration_invalid_xp_multiplier(self) -> None:
        """Test invalid XP multiplier is rejected."""
        with pytest.raises(ValidationError) as exc_info:
            GameConfig(aliases_dir=os.getenv("GAME_ALIASES_DIR") or "data/aliases", combat_xp_multiplier=0.5)
        assert "XP multiplier must be between 1.0 and 5.0" in str(exc_info.value)


class TestCombatConfigurationManagement:
    """Test combat configuration management and deployment."""

    # Apply serial markers to entire class to prevent worker crashes in full suite
    pytestmark = [pytest.mark.serial, pytest.mark.xdist_group("serial_config_tests")]

    @pytest.fixture(autouse=True)
    def setup_test_env(self, monkeypatch):
        """Set up test environment variables."""
        # Set required environment variables
        monkeypatch.setenv("SERVER_PORT", "54731")
        monkeypatch.setenv("DATABASE_URL", "postgresql+asyncpg://postgres:Cthulhu1@localhost:5432/mythos_unit")
        monkeypatch.setenv("DATABASE_NPC_URL", "postgresql+asyncpg://postgres:Cthulhu1@localhost:5432/mythos_unit")
        monkeypatch.setenv("MYTHOSMUD_ADMIN_PASSWORD", "test_admin_pass")
        monkeypatch.setenv("LOGGING_ENVIRONMENT", "unit_test")
        monkeypatch.setenv("GAME_ALIASES_DIR", "data/unit_test/players/aliases")

        # Reset config cache before each test
        reset_config()

        yield

        # Clean up after test
        reset_config()

    @pytest.mark.serial
    @pytest.mark.xdist_group(name="serial_config_tests")
    def test_feature_flag_deployment_scenario(self, monkeypatch):
        """Test feature flag deployment scenario - gradual rollout."""
        # Ensure clean state before starting
        reset_config()

        # Start with combat disabled
        monkeypatch.setenv("GAME_COMBAT_ENABLED", "false")
        reset_config()  # Force config reload after setting env var
        config1: AppConfig = get_config()
        game_config1: GameConfig = cast(GameConfig, config1.game)
        # Pylint limitation: doesn't recognize cast() for Pydantic nested models
        assert game_config1.combat_enabled is False  # pylint: disable=no-member

        # Enable combat via feature flag
        monkeypatch.setenv("GAME_COMBAT_ENABLED", "true")
        reset_config()  # Force config reload
        config2: AppConfig = get_config()
        game_config2: GameConfig = cast(GameConfig, config2.game)
        # Pylint limitation: doesn't recognize cast() for Pydantic nested models
        assert game_config2.combat_enabled is True  # pylint: disable=no-member

    @pytest.mark.serial
    @pytest.mark.xdist_group(name="serial_config_tests")
    def test_combat_configuration_hot_reload(self, monkeypatch):
        """Test that combat configuration can be hot-reloaded."""
        # Ensure clean state before starting
        reset_config()
        # Verify cache is cleared by getting a fresh config
        _ = get_config()  # Force cache population, then reset again
        reset_config()

        try:
            # Initial configuration
            monkeypatch.setenv("GAME_COMBAT_TICK_INTERVAL", "6")
            monkeypatch.setenv("GAME_COMBAT_TIMEOUT_SECONDS", "180")

            reset_config()  # Force config reload after setting env vars
            # Get config twice to ensure cache is working and reading new values
            config1: AppConfig = get_config()
            config1_verify: AppConfig = get_config()  # Should return cached instance
            assert config1 is config1_verify  # Verify cache is working
            game_config1: GameConfig = cast(GameConfig, config1.game)
            # Pylint limitation: doesn't recognize cast() for Pydantic nested models
            assert game_config1.combat_tick_interval == 6  # pylint: disable=no-member
            assert game_config1.combat_timeout_seconds == 180  # pylint: disable=no-member

            # Update configuration
            monkeypatch.setenv("GAME_COMBAT_TICK_INTERVAL", "10")
            monkeypatch.setenv("GAME_COMBAT_TIMEOUT_SECONDS", "300")

            reset_config()  # Force config reload
            config2: AppConfig = get_config()
            game_config2: GameConfig = cast(GameConfig, config2.game)
            # Pylint limitation: doesn't recognize cast() for Pydantic nested models
            assert game_config2.combat_tick_interval == 10  # pylint: disable=no-member
            assert game_config2.combat_timeout_seconds == 300  # pylint: disable=no-member
            # Verify we got a new instance (cache was cleared)
            assert config1 is not config2  # Should be different instances after reset
        finally:
            # Ensure cleanup
            monkeypatch.delenv("GAME_COMBAT_TICK_INTERVAL", raising=False)
            monkeypatch.delenv("GAME_COMBAT_TIMEOUT_SECONDS", raising=False)
            reset_config()

    @pytest.mark.serial
    @pytest.mark.xdist_group(name="serial_config_tests")
    def test_combat_configuration_rollback(self, monkeypatch):
        """Test combat configuration rollback scenario."""
        # Ensure clean state before starting
        reset_config()

        try:
            # Deploy new configuration
            monkeypatch.setenv("GAME_COMBAT_ENABLED", "true")
            monkeypatch.setenv("GAME_COMBAT_XP_MULTIPLIER", "2.0")

            reset_config()  # Force config reload after setting env vars
            config1: AppConfig = get_config()
            game_config1: GameConfig = cast(GameConfig, config1.game)
            # Pylint limitation: doesn't recognize cast() for Pydantic nested models
            assert game_config1.combat_enabled is True  # pylint: disable=no-member
            assert game_config1.combat_xp_multiplier == 2.0  # pylint: disable=no-member

            # Rollback to previous configuration
            monkeypatch.setenv("GAME_COMBAT_ENABLED", "false")
            monkeypatch.delenv("GAME_COMBAT_XP_MULTIPLIER", raising=False)

            reset_config()  # Force config reload
            config2: AppConfig = get_config()
            game_config2: GameConfig = cast(GameConfig, config2.game)
            # Pylint limitation: doesn't recognize cast() for Pydantic nested models
            assert game_config2.combat_enabled is False  # pylint: disable=no-member
            assert game_config2.combat_xp_multiplier == 1.0  # pylint: disable=no-member  # Default value
        finally:
            # Ensure cleanup
            monkeypatch.delenv("GAME_COMBAT_ENABLED", raising=False)
            monkeypatch.delenv("GAME_COMBAT_XP_MULTIPLIER", raising=False)
            reset_config()

    @pytest.mark.serial  # Flaky in parallel execution - likely due to shared config state
    @pytest.mark.xdist_group(name="serial_config_tests")  # Force serial execution with pytest-xdist
    def test_environment_specific_combat_configuration(self, monkeypatch):
        """Test environment-specific combat configuration."""
        # Ensure clean state before starting
        reset_config()

        try:
            # Production environment
            monkeypatch.setenv("LOGGING_ENVIRONMENT", "production")
            monkeypatch.setenv("GAME_COMBAT_ENABLED", "true")
            monkeypatch.setenv("GAME_COMBAT_LOGGING_ENABLED", "true")

            reset_config()  # Force config reload after setting env vars
            config: AppConfig = get_config()
            game_config: GameConfig = cast(GameConfig, config.game)
            # Pylint limitation: doesn't recognize cast() for Pydantic nested models
            assert game_config.combat_enabled is True  # pylint: disable=no-member
            assert game_config.combat_logging_enabled is True  # pylint: disable=no-member

            # Test environment
            monkeypatch.setenv("LOGGING_ENVIRONMENT", "unit_test")
            monkeypatch.setenv("GAME_COMBAT_ENABLED", "false")
            monkeypatch.setenv("GAME_COMBAT_LOGGING_ENABLED", "false")

            reset_config()  # Force config reload
            config = get_config()
            game_config = cast(GameConfig, config.game)
            # Pylint limitation: doesn't recognize cast() for Pydantic nested models
            assert game_config.combat_enabled is False  # pylint: disable=no-member
            assert game_config.combat_logging_enabled is False  # pylint: disable=no-member
        finally:
            # Ensure cleanup
            reset_config()


class TestCombatMonitoringConfiguration:
    """Test combat monitoring and alerting configuration."""

    # Apply serial markers to entire class to prevent worker crashes in full suite
    pytestmark = [pytest.mark.serial, pytest.mark.xdist_group("serial_config_tests")]

    @pytest.fixture(autouse=True)
    def setup_test_env(self, monkeypatch):
        """Set up test environment variables."""
        # Set required environment variables
        monkeypatch.setenv("SERVER_PORT", "54731")
        monkeypatch.setenv("DATABASE_URL", "postgresql+asyncpg://postgres:Cthulhu1@localhost:5432/mythos_unit")
        monkeypatch.setenv("DATABASE_NPC_URL", "postgresql+asyncpg://postgres:Cthulhu1@localhost:5432/mythos_unit")
        monkeypatch.setenv("MYTHOSMUD_ADMIN_PASSWORD", "test_admin_pass")
        monkeypatch.setenv("LOGGING_ENVIRONMENT", "unit_test")
        monkeypatch.setenv("GAME_ALIASES_DIR", "data/unit_test/players/aliases")

        # Reset config cache before each test
        reset_config()

        yield

        # Clean up after test
        reset_config()

    @pytest.mark.serial
    @pytest.mark.xdist_group(name="serial_config_tests")
    def test_combat_monitoring_configuration(self) -> None:
        """Test combat monitoring configuration settings."""
        config = GameConfig(
            aliases_dir=os.getenv("GAME_ALIASES_DIR") or "data/aliases",
            combat_monitoring_enabled=True,
            combat_alert_threshold=10,
            combat_performance_threshold=500,
            combat_error_threshold=5,
        )

        assert config.combat_monitoring_enabled is True
        assert config.combat_alert_threshold == 10
        assert config.combat_performance_threshold == 500
        assert config.combat_error_threshold == 5

    @pytest.mark.serial
    @pytest.mark.xdist_group(name="serial_config_tests")
    def test_combat_monitoring_defaults(self) -> None:
        """Test combat monitoring default values."""
        config = GameConfig(aliases_dir=os.getenv("GAME_ALIASES_DIR") or "data/aliases")

        assert config.combat_monitoring_enabled is True
        assert config.combat_alert_threshold == 5
        assert config.combat_performance_threshold == 1000
        assert config.combat_error_threshold == 3

    @pytest.mark.serial  # Class uses autouse fixture that modifies global config state
    @pytest.mark.xdist_group(name="serial_config_tests")  # Force serial execution with pytest-xdist
    def test_combat_monitoring_validation(self) -> None:
        """Test combat monitoring configuration validation."""
        # Valid values should pass
        config = GameConfig(
            aliases_dir=os.getenv("GAME_ALIASES_DIR") or "data/aliases",
            combat_alert_threshold=15,
            combat_performance_threshold=750,
            combat_error_threshold=8,
        )
        assert config.combat_alert_threshold == 15
        assert config.combat_performance_threshold == 750
        assert config.combat_error_threshold == 8

    @pytest.mark.serial  # Class uses autouse fixture that modifies global config state
    @pytest.mark.xdist_group(name="serial_config_tests")  # Force serial execution with pytest-xdist
    def test_combat_monitoring_invalid_thresholds(self) -> None:
        """Test invalid monitoring thresholds are rejected."""
        # Alert threshold too low
        with pytest.raises(ValidationError) as exc_info:
            GameConfig(aliases_dir=os.getenv("GAME_ALIASES_DIR") or "data/aliases", combat_alert_threshold=0)
        assert "Alert threshold must be between 1 and 100" in str(exc_info.value)

        # Performance threshold too high
        with pytest.raises(ValidationError) as exc_info:
            GameConfig(aliases_dir=os.getenv("GAME_ALIASES_DIR") or "data/aliases", combat_performance_threshold=10000)
        assert "Performance threshold must be between 100 and 5000 milliseconds" in str(exc_info.value)

        # Error threshold too high
        with pytest.raises(ValidationError) as exc_info:
            GameConfig(aliases_dir=os.getenv("GAME_ALIASES_DIR") or "data/aliases", combat_error_threshold=100)
        assert "Error threshold must be between 1 and 50" in str(exc_info.value)


class TestCombatConfigurationIntegration:
    """Test combat configuration integration with existing systems."""

    # Apply serial markers to entire class to prevent worker crashes in full suite
    pytestmark = [pytest.mark.serial, pytest.mark.xdist_group("serial_config_tests")]

    @pytest.fixture(autouse=True)
    def setup_test_env(self, monkeypatch):
        """Set up test environment variables."""
        # Set required environment variables
        monkeypatch.setenv("SERVER_PORT", "54731")
        monkeypatch.setenv("DATABASE_URL", "postgresql+asyncpg://postgres:Cthulhu1@localhost:5432/mythos_unit")
        monkeypatch.setenv("DATABASE_NPC_URL", "postgresql+asyncpg://postgres:Cthulhu1@localhost:5432/mythos_unit")
        monkeypatch.setenv("MYTHOSMUD_ADMIN_PASSWORD", "test_admin_pass")
        monkeypatch.setenv("LOGGING_ENVIRONMENT", "unit_test")
        monkeypatch.setenv("GAME_ALIASES_DIR", "data/unit_test/players/aliases")

        # Reset config cache before each test
        reset_config()

        yield

        # Clean up after test
        reset_config()

    @pytest.mark.serial  # Class uses autouse fixture that modifies global config state
    @pytest.mark.xdist_group(name="serial_config_tests")  # Force serial execution with pytest-xdist
    def test_combat_config_in_app_config(self) -> None:
        """Test that combat configuration is properly integrated in AppConfig."""
        # Ensure config cache is cleared before creating new instance
        reset_config()
        config = AppConfig()

        # Verify combat settings are accessible
        assert hasattr(config.game, "combat_enabled")
        assert hasattr(config.game, "combat_tick_interval")
        assert hasattr(config.game, "combat_timeout_seconds")
        assert hasattr(config.game, "combat_xp_multiplier")
        assert hasattr(config.game, "combat_logging_enabled")
        assert hasattr(config.game, "combat_monitoring_enabled")

    @pytest.mark.serial  # Flaky in parallel execution - likely due to shared config state
    @pytest.mark.xdist_group(name="serial_config_tests")  # Force serial execution with pytest-xdist
    def test_combat_config_legacy_dict_conversion(self) -> None:
        """Test that combat configuration is included in legacy dict conversion."""
        config = AppConfig()
        legacy = config.to_legacy_dict()

        # Verify combat settings are in legacy dict
        assert "combat_enabled" in legacy
        assert "combat_tick_interval" in legacy
        assert "combat_timeout_seconds" in legacy
        assert "combat_xp_multiplier" in legacy
        assert "combat_logging_enabled" in legacy
        assert "combat_monitoring_enabled" in legacy

    @pytest.mark.serial  # Flaky in parallel execution - likely due to shared config state
    @pytest.mark.xdist_group(name="serial_config_tests")  # Force serial execution with pytest-xdist
    def test_combat_config_environment_variable_integration(self, monkeypatch):
        """Test that combat configuration integrates with environment variables."""
        # Set combat-specific environment variables
        monkeypatch.setenv("GAME_COMBAT_ENABLED", "false")
        monkeypatch.setenv("GAME_COMBAT_TICK_INTERVAL", "8")
        monkeypatch.setenv("GAME_COMBAT_TIMEOUT_SECONDS", "240")
        monkeypatch.setenv("GAME_COMBAT_XP_MULTIPLIER", "1.5")
        monkeypatch.setenv("GAME_COMBAT_LOGGING_ENABLED", "false")
        monkeypatch.setenv("GAME_COMBAT_MONITORING_ENABLED", "false")

        config: AppConfig = get_config()
        game_config: GameConfig = cast(GameConfig, config.game)

        # Verify environment variables are properly loaded
        # Pylint limitation: doesn't recognize cast() for Pydantic nested models
        assert game_config.combat_enabled is False  # pylint: disable=no-member
        assert game_config.combat_tick_interval == 8  # pylint: disable=no-member
        assert game_config.combat_timeout_seconds == 240  # pylint: disable=no-member
        assert game_config.combat_xp_multiplier == 1.5  # pylint: disable=no-member
        assert game_config.combat_logging_enabled is False  # pylint: disable=no-member
        assert game_config.combat_monitoring_enabled is False  # pylint: disable=no-member

    @pytest.mark.serial  # Class uses autouse fixture that modifies global config state
    @pytest.mark.xdist_group(name="serial_config_tests")  # Force serial execution with pytest-xdist
    def test_combat_config_validation_integration(self) -> None:
        """Test that combat configuration validation integrates with existing validation."""
        # Ensure clean state before starting
        reset_config()

        # This should pass - all valid values
        config: AppConfig = AppConfig()
        # Remove redundant cast - mypy recognizes config.game as GameConfig
        game_config: GameConfig = config.game
        # Pylint limitation: doesn't recognize cast() for Pydantic nested models
        assert game_config.combat_enabled is True  # pylint: disable=no-member
        assert game_config.combat_tick_interval == 6  # pylint: disable=no-member
        assert game_config.combat_timeout_seconds == 180  # pylint: disable=no-member
        assert game_config.combat_xp_multiplier == 1.0  # pylint: disable=no-member

        # This should fail - invalid values
        with pytest.raises(ValidationError):
            GameConfig(
                aliases_dir="data/aliases",
                combat_tick_interval=0,  # Invalid
                combat_timeout_seconds=30,  # Invalid
                combat_xp_multiplier=0.5,  # Invalid
            )

    @pytest.mark.serial  # Class uses autouse fixture that modifies global config state
    @pytest.mark.xdist_group(name="serial_config_tests")  # Force serial execution with pytest-xdist
    def test_combat_config_feature_flag_integration(self, monkeypatch):
        """Test that combat feature flag integrates with existing feature system."""
        # Test with combat disabled
        monkeypatch.setenv("GAME_COMBAT_ENABLED", "false")
        config: AppConfig = get_config()
        game_config: GameConfig = cast(GameConfig, config.game)

        # When combat is disabled, other combat settings should still be accessible
        # Pylint limitation: doesn't recognize cast() for Pydantic nested models
        assert game_config.combat_enabled is False  # pylint: disable=no-member
        assert game_config.combat_tick_interval == 6  # pylint: disable=no-member  # Still accessible
        assert game_config.combat_logging_enabled is True  # pylint: disable=no-member  # Still accessible

        # Test with combat enabled
        monkeypatch.setenv("GAME_COMBAT_ENABLED", "true")
        reset_config()
        config = get_config()
        game_config = cast(GameConfig, config.game)

        # Pylint limitation: doesn't recognize cast() for Pydantic nested models
        assert game_config.combat_enabled is True  # pylint: disable=no-member
        assert game_config.combat_tick_interval == 6  # pylint: disable=no-member
        assert game_config.combat_logging_enabled is True  # pylint: disable=no-member


class TestCombatConfigurationEdgeCases:
    """Test edge cases and boundary conditions for combat configuration."""

    # Apply serial markers to entire class to prevent worker crashes in full suite
    pytestmark = [pytest.mark.serial, pytest.mark.xdist_group("serial_config_tests")]

    @pytest.fixture(autouse=True)
    def setup_test_env(self, monkeypatch):
        """Set up test environment variables."""
        # Set required environment variables
        monkeypatch.setenv("SERVER_PORT", "54731")
        monkeypatch.setenv("DATABASE_URL", "postgresql+asyncpg://postgres:Cthulhu1@localhost:5432/mythos_unit")
        monkeypatch.setenv("DATABASE_NPC_URL", "postgresql+asyncpg://postgres:Cthulhu1@localhost:5432/mythos_unit")
        monkeypatch.setenv("MYTHOSMUD_ADMIN_PASSWORD", "test_admin_pass")
        monkeypatch.setenv("LOGGING_ENVIRONMENT", "unit_test")
        monkeypatch.setenv("GAME_ALIASES_DIR", "data/test/aliases")

        # Reset config cache before each test
        reset_config()

        yield

        # Clean up after test
        reset_config()

    @pytest.mark.serial  # Class uses autouse fixture that modifies global config state
    @pytest.mark.xdist_group(name="serial_config_tests")  # Force serial execution with pytest-xdist
    def test_boundary_combat_tick_interval(self) -> None:
        """Test boundary values for combat tick interval."""
        # Minimum valid value
        config = GameConfig(aliases_dir="data/aliases", combat_tick_interval=1)
        assert config.combat_tick_interval == 1

        # Maximum valid value
        config = GameConfig(aliases_dir="data/aliases", combat_tick_interval=60)
        assert config.combat_tick_interval == 60

        # Below minimum
        with pytest.raises(ValidationError):
            GameConfig(aliases_dir="data/aliases", combat_tick_interval=0)

        # Above maximum
        with pytest.raises(ValidationError):
            GameConfig(aliases_dir="data/aliases", combat_tick_interval=61)

    @pytest.mark.serial
    @pytest.mark.xdist_group(name="serial_config_tests")
    def test_boundary_combat_timeout(self) -> None:
        """Test boundary values for combat timeout."""
        # Minimum valid value
        config = GameConfig(aliases_dir="data/aliases", combat_timeout_seconds=60)
        assert config.combat_timeout_seconds == 60

        # Maximum valid value
        config = GameConfig(aliases_dir="data/aliases", combat_timeout_seconds=1800)
        assert config.combat_timeout_seconds == 1800

        # Below minimum
        with pytest.raises(ValidationError):
            GameConfig(aliases_dir="data/aliases", combat_timeout_seconds=59)

        # Above maximum
        with pytest.raises(ValidationError):
            GameConfig(aliases_dir="data/aliases", combat_timeout_seconds=1801)

    @pytest.mark.serial  # Class uses autouse fixture that modifies global config state
    @pytest.mark.xdist_group(name="serial_config_tests")  # Force serial execution with pytest-xdist
    def test_boundary_xp_multiplier(self) -> None:
        """Test boundary values for XP multiplier."""
        # Minimum valid value
        config = GameConfig(aliases_dir="data/aliases", combat_xp_multiplier=1.0)
        assert config.combat_xp_multiplier == 1.0

        # Maximum valid value
        config = GameConfig(aliases_dir="data/aliases", combat_xp_multiplier=5.0)
        assert config.combat_xp_multiplier == 5.0

        # Below minimum
        with pytest.raises(ValidationError):
            GameConfig(aliases_dir="data/aliases", combat_xp_multiplier=0.9)

        # Above maximum
        with pytest.raises(ValidationError):
            GameConfig(aliases_dir="data/aliases", combat_xp_multiplier=5.1)

    @pytest.mark.serial  # Class uses autouse fixture that modifies global config state
    @pytest.mark.xdist_group(name="serial_config_tests")  # Force serial execution with pytest-xdist
    def test_boolean_feature_flags(self) -> None:
        """Test boolean feature flags handle various input types."""
        # Test with string "true" - Pydantic will coerce string to bool
        config = GameConfig(aliases_dir="data/aliases", combat_enabled="true")
        assert config.combat_enabled is True

        # Test with string "false" - Pydantic will coerce string to bool
        config = GameConfig(aliases_dir="data/aliases", combat_enabled="false")
        assert config.combat_enabled is False

        # Test with integer 1 - Pydantic will coerce int to bool
        config = GameConfig(aliases_dir="data/aliases", combat_enabled=1)
        assert config.combat_enabled is True

        # Test with integer 0 - Pydantic will coerce int to bool
        config = GameConfig(aliases_dir="data/aliases", combat_enabled=0)
        assert config.combat_enabled is False

    @pytest.mark.serial
    @pytest.mark.xdist_group(name="serial_config_tests")
    def test_configuration_precedence(self, monkeypatch):
        """Test configuration precedence (explicit > environment > default)."""
        # Ensure clean state before starting
        reset_config()

        try:
            # Set environment variable
            monkeypatch.setenv("GAME_COMBAT_TICK_INTERVAL", "8")

            # Explicit value should override environment variable
            game_config = GameConfig(aliases_dir="data/aliases", combat_tick_interval=10)
            assert game_config.combat_tick_interval == 10

            # Environment variable should override default
            reset_config()  # Force config reload after setting env var

            app_config: AppConfig = get_config()
            game_config: GameConfig = cast(GameConfig, app_config.game)
            # Pylint limitation: doesn't recognize cast() for Pydantic nested models
            assert game_config.combat_tick_interval == 8  # pylint: disable=no-member

            # Default should be used when neither is set
            monkeypatch.delenv("GAME_COMBAT_TICK_INTERVAL", raising=False)
            reset_config()  # Force config reload after deleting env var
            app_config = get_config()
            game_config = cast(GameConfig, app_config.game)
            # Pylint limitation: doesn't recognize cast() for Pydantic nested models
            assert game_config.combat_tick_interval == 6  # pylint: disable=no-member  # Default value
        finally:
            # Ensure cleanup
            monkeypatch.delenv("GAME_COMBAT_TICK_INTERVAL", raising=False)
            reset_config()
