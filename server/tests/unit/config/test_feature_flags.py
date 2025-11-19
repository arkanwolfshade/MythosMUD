"""
Tests for feature flag system and configuration management.

These tests verify that the feature flag system properly enables/disables
combat features, handles configuration changes, and provides monitoring capabilities.
"""

import os

import pytest
from pydantic import ValidationError

from server.config import get_config, reset_config
from server.config.models import AppConfig, GameConfig


class TestFeatureFlagSystem:
    """Test feature flag system for combat enable/disable."""

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

    def test_combat_feature_flag_enabled_by_default(self):
        """Test that combat is enabled by default."""
        config = GameConfig(aliases_dir=os.getenv("GAME_ALIASES_DIR") or "data/aliases" or "data/aliases")
        assert config.combat_enabled is True

    def test_combat_feature_flag_can_be_disabled(self):
        """Test that combat can be disabled via configuration."""
        config = GameConfig(aliases_dir=os.getenv("GAME_ALIASES_DIR") or "data/aliases", combat_enabled=False)
        assert config.combat_enabled is False

    def test_combat_feature_flag_from_environment(self, monkeypatch):
        """Test that combat feature flag can be set via environment variable."""
        monkeypatch.setenv("GAME_COMBAT_ENABLED", "false")

        config = GameConfig(aliases_dir=os.getenv("GAME_ALIASES_DIR") or "data/aliases")
        assert config.combat_enabled is False

    def test_combat_feature_flag_environment_override(self, monkeypatch):
        """Test that environment variable overrides default value."""
        monkeypatch.setenv("GAME_COMBAT_ENABLED", "true")

        # When no explicit value is provided, environment variable should be used
        config = GameConfig(aliases_dir=os.getenv("GAME_ALIASES_DIR") or "data/aliases")
        assert config.combat_enabled is True

    def test_combat_configuration_settings(self):
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

    def test_combat_configuration_defaults(self):
        """Test combat configuration default values."""
        config = GameConfig(aliases_dir=os.getenv("GAME_ALIASES_DIR") or "data/aliases")

        assert config.combat_enabled is True
        assert config.combat_tick_interval == 6
        assert config.combat_timeout_seconds == 180
        assert config.combat_xp_multiplier == 1.0
        assert config.combat_logging_enabled is True

    def test_combat_configuration_validation(self):
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

    def test_combat_configuration_invalid_tick_interval(self):
        """Test invalid combat tick interval is rejected."""
        with pytest.raises(ValidationError) as exc_info:
            GameConfig(aliases_dir=os.getenv("GAME_ALIASES_DIR") or "data/aliases", combat_tick_interval=0)
        assert "Combat tick interval must be between 1 and 60 seconds" in str(exc_info.value)

    def test_combat_configuration_invalid_timeout(self):
        """Test invalid combat timeout is rejected."""
        with pytest.raises(ValidationError) as exc_info:
            GameConfig(aliases_dir=os.getenv("GAME_ALIASES_DIR") or "data/aliases", combat_timeout_seconds=30)
        assert "Combat timeout must be between 60 and 1800 seconds" in str(exc_info.value)

    def test_combat_configuration_invalid_xp_multiplier(self):
        """Test invalid XP multiplier is rejected."""
        with pytest.raises(ValidationError) as exc_info:
            GameConfig(aliases_dir=os.getenv("GAME_ALIASES_DIR") or "data/aliases", combat_xp_multiplier=0.5)
        assert "XP multiplier must be between 1.0 and 5.0" in str(exc_info.value)


class TestCombatConfigurationManagement:
    """Test combat configuration management and deployment."""

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

    def test_feature_flag_deployment_scenario(self, monkeypatch):
        """Test feature flag deployment scenario - gradual rollout."""
        # Start with combat disabled
        monkeypatch.setenv("GAME_COMBAT_ENABLED", "false")
        config1 = get_config()
        assert config1.game.combat_enabled is False

        # Enable combat via feature flag
        monkeypatch.setenv("GAME_COMBAT_ENABLED", "true")
        reset_config()  # Force config reload
        config2 = get_config()
        assert config2.game.combat_enabled is True

    def test_combat_configuration_hot_reload(self, monkeypatch):
        """Test that combat configuration can be hot-reloaded."""
        # Initial configuration
        monkeypatch.setenv("GAME_COMBAT_TICK_INTERVAL", "6")
        monkeypatch.setenv("GAME_COMBAT_TIMEOUT_SECONDS", "180")

        config1 = get_config()
        assert config1.game.combat_tick_interval == 6
        assert config1.game.combat_timeout_seconds == 180

        # Update configuration
        monkeypatch.setenv("GAME_COMBAT_TICK_INTERVAL", "10")
        monkeypatch.setenv("GAME_COMBAT_TIMEOUT_SECONDS", "300")

        reset_config()  # Force config reload
        config2 = get_config()
        assert config2.game.combat_tick_interval == 10
        assert config2.game.combat_timeout_seconds == 300

    def test_combat_configuration_rollback(self, monkeypatch):
        """Test combat configuration rollback scenario."""
        # Deploy new configuration
        monkeypatch.setenv("GAME_COMBAT_ENABLED", "true")
        monkeypatch.setenv("GAME_COMBAT_XP_MULTIPLIER", "2.0")

        config1 = get_config()
        assert config1.game.combat_enabled is True
        assert config1.game.combat_xp_multiplier == 2.0

        # Rollback to previous configuration
        monkeypatch.setenv("GAME_COMBAT_ENABLED", "false")
        monkeypatch.delenv("GAME_COMBAT_XP_MULTIPLIER", raising=False)

        reset_config()  # Force config reload
        config2 = get_config()
        assert config2.game.combat_enabled is False
        assert config2.game.combat_xp_multiplier == 1.0  # Default value

    def test_environment_specific_combat_configuration(self, monkeypatch):
        """Test environment-specific combat configuration."""
        # Production environment
        monkeypatch.setenv("LOGGING_ENVIRONMENT", "production")
        monkeypatch.setenv("GAME_COMBAT_ENABLED", "true")
        monkeypatch.setenv("GAME_COMBAT_LOGGING_ENABLED", "true")

        config = get_config()
        assert config.game.combat_enabled is True
        assert config.game.combat_logging_enabled is True

        # Test environment
        monkeypatch.setenv("LOGGING_ENVIRONMENT", "unit_test")
        monkeypatch.setenv("GAME_COMBAT_ENABLED", "false")
        monkeypatch.setenv("GAME_COMBAT_LOGGING_ENABLED", "false")

        reset_config()  # Force config reload
        config = get_config()
        assert config.game.combat_enabled is False
        assert config.game.combat_logging_enabled is False


class TestCombatMonitoringConfiguration:
    """Test combat monitoring and alerting configuration."""

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

    def test_combat_monitoring_configuration(self):
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

    def test_combat_monitoring_defaults(self):
        """Test combat monitoring default values."""
        config = GameConfig(aliases_dir=os.getenv("GAME_ALIASES_DIR") or "data/aliases")

        assert config.combat_monitoring_enabled is True
        assert config.combat_alert_threshold == 5
        assert config.combat_performance_threshold == 1000
        assert config.combat_error_threshold == 3

    def test_combat_monitoring_validation(self):
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

    def test_combat_monitoring_invalid_thresholds(self):
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

    def test_combat_config_in_app_config(self):
        """Test that combat configuration is properly integrated in AppConfig."""
        config = AppConfig()

        # Verify combat settings are accessible
        assert hasattr(config.game, "combat_enabled")
        assert hasattr(config.game, "combat_tick_interval")
        assert hasattr(config.game, "combat_timeout_seconds")
        assert hasattr(config.game, "combat_xp_multiplier")
        assert hasattr(config.game, "combat_logging_enabled")
        assert hasattr(config.game, "combat_monitoring_enabled")

    def test_combat_config_legacy_dict_conversion(self):
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

    def test_combat_config_environment_variable_integration(self, monkeypatch):
        """Test that combat configuration integrates with environment variables."""
        # Set combat-specific environment variables
        monkeypatch.setenv("GAME_COMBAT_ENABLED", "false")
        monkeypatch.setenv("GAME_COMBAT_TICK_INTERVAL", "8")
        monkeypatch.setenv("GAME_COMBAT_TIMEOUT_SECONDS", "240")
        monkeypatch.setenv("GAME_COMBAT_XP_MULTIPLIER", "1.5")
        monkeypatch.setenv("GAME_COMBAT_LOGGING_ENABLED", "false")
        monkeypatch.setenv("GAME_COMBAT_MONITORING_ENABLED", "false")

        config = get_config()

        # Verify environment variables are properly loaded
        assert config.game.combat_enabled is False
        assert config.game.combat_tick_interval == 8
        assert config.game.combat_timeout_seconds == 240
        assert config.game.combat_xp_multiplier == 1.5
        assert config.game.combat_logging_enabled is False
        assert config.game.combat_monitoring_enabled is False

    def test_combat_config_validation_integration(self):
        """Test that combat configuration validation integrates with existing validation."""
        # This should pass - all valid values
        config = AppConfig()
        assert config.game.combat_enabled is True
        assert config.game.combat_tick_interval == 6
        assert config.game.combat_timeout_seconds == 180
        assert config.game.combat_xp_multiplier == 1.0

        # This should fail - invalid values
        with pytest.raises(ValidationError):
            GameConfig(
                aliases_dir="data/aliases",
                combat_tick_interval=0,  # Invalid
                combat_timeout_seconds=30,  # Invalid
                combat_xp_multiplier=0.5,  # Invalid
            )

    def test_combat_config_feature_flag_integration(self, monkeypatch):
        """Test that combat feature flag integrates with existing feature system."""
        # Test with combat disabled
        monkeypatch.setenv("GAME_COMBAT_ENABLED", "false")
        config = get_config()

        # When combat is disabled, other combat settings should still be accessible
        assert config.game.combat_enabled is False
        assert config.game.combat_tick_interval == 6  # Still accessible
        assert config.game.combat_logging_enabled is True  # Still accessible

        # Test with combat enabled
        monkeypatch.setenv("GAME_COMBAT_ENABLED", "true")
        reset_config()
        config = get_config()

        assert config.game.combat_enabled is True
        assert config.game.combat_tick_interval == 6
        assert config.game.combat_logging_enabled is True


class TestCombatConfigurationEdgeCases:
    """Test edge cases and boundary conditions for combat configuration."""

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

    def test_boundary_combat_tick_interval(self):
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

    def test_boundary_combat_timeout(self):
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

    def test_boundary_xp_multiplier(self):
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

    def test_boolean_feature_flags(self):
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

    def test_configuration_precedence(self, monkeypatch):
        """Test configuration precedence (explicit > environment > default)."""
        # Set environment variable
        monkeypatch.setenv("GAME_COMBAT_TICK_INTERVAL", "8")

        # Explicit value should override environment variable
        game_config = GameConfig(aliases_dir="data/aliases", combat_tick_interval=10)
        assert game_config.combat_tick_interval == 10

        # Environment variable should override default
        reset_config()
        from server.config.models import AppConfig
        app_config: AppConfig = get_config()
        assert app_config.game.combat_tick_interval == 8

        # Default should be used when neither is set
        monkeypatch.delenv("GAME_COMBAT_TICK_INTERVAL", raising=False)
        reset_config()
        app_config = get_config()
        assert app_config.game.combat_tick_interval == 6  # Default value
