"""
Tests for combat configuration service.

These tests verify that the combat configuration service properly manages
combat settings, handles scope-specific overrides, and provides reliable
configuration management.
"""

from unittest.mock import MagicMock, patch

import pytest

from server.services.combat_configuration_service import (
    CombatConfiguration,
    CombatConfigurationError,
    CombatConfigurationScope,
    CombatConfigurationService,
    get_combat_config,
    get_combat_configuration,
    is_combat_available,
    refresh_combat_configuration,
)


@pytest.fixture
def mock_config():
    """Mock configuration for testing."""
    config_mock = MagicMock()
    config_mock.game.combat_enabled = True
    config_mock.game.combat_logging_enabled = True
    config_mock.game.combat_monitoring_enabled = True
    config_mock.game.combat_tick_interval = 6
    config_mock.game.combat_timeout_seconds = 180
    config_mock.game.combat_xp_multiplier = 1.0
    config_mock.game.combat_alert_threshold = 5
    config_mock.game.combat_performance_threshold = 1000
    config_mock.game.combat_error_threshold = 3
    return config_mock


@pytest.fixture
def mock_feature_flags():
    """Mock feature flags for testing."""
    mock_flags = MagicMock()
    mock_flags.is_combat_enabled.return_value = True
    mock_flags.is_combat_logging_enabled.return_value = True
    mock_flags.is_combat_monitoring_enabled.return_value = True
    mock_flags.clear_cache.return_value = None
    return mock_flags


class TestCombatConfiguration:
    """Test CombatConfiguration data class."""

    def test_combat_configuration_defaults(self) -> None:
        """Test default combat configuration values."""
        config = CombatConfiguration()

        assert config.combat_enabled is True
        assert config.combat_tick_interval == 6
        assert config.combat_timeout_seconds == 180
        assert config.combat_xp_multiplier == 1.0
        assert config.combat_logging_enabled is True
        assert config.combat_monitoring_enabled is True
        assert config.combat_alert_threshold == 5
        assert config.combat_performance_threshold == 1000
        assert config.combat_error_threshold == 3
        assert config.combat_max_participants == 10
        assert config.combat_auto_cleanup_interval == 300
        assert config.combat_event_retention_hours == 24

    def test_combat_configuration_custom_values(self) -> None:
        """Test custom combat configuration values."""
        config = CombatConfiguration(
            combat_enabled=False, combat_tick_interval=10, combat_timeout_seconds=300, combat_xp_multiplier=2.0
        )

        assert config.combat_enabled is False
        assert config.combat_tick_interval == 10
        assert config.combat_timeout_seconds == 300
        assert config.combat_xp_multiplier == 2.0

    def test_combat_configuration_to_dict(self) -> None:
        """Test converting configuration to dictionary."""
        config = CombatConfiguration(combat_enabled=False, combat_tick_interval=10)
        config_dict = config.to_dict()

        assert config_dict["combat_enabled"] is False
        assert config_dict["combat_tick_interval"] == 10
        assert "combat_timeout_seconds" in config_dict

    def test_combat_configuration_from_dict(self) -> None:
        """Test creating configuration from dictionary."""
        config_dict = {
            "combat_enabled": False,
            "combat_tick_interval": 10,
            "combat_timeout_seconds": 300,
            "combat_xp_multiplier": 2.0,
            "combat_logging_enabled": True,
            "combat_monitoring_enabled": True,
            "combat_alert_threshold": 5,
            "combat_performance_threshold": 1000,
            "combat_error_threshold": 3,
            "combat_max_participants": 10,
            "combat_auto_cleanup_interval": 300,
            "combat_event_retention_hours": 24,
        }

        config = CombatConfiguration.from_dict(config_dict)

        assert config.combat_enabled is False
        assert config.combat_tick_interval == 10
        assert config.combat_timeout_seconds == 300
        assert config.combat_xp_multiplier == 2.0

    def test_combat_configuration_validation_valid(self) -> None:
        """Test configuration validation with valid values."""
        config = CombatConfiguration()
        errors = config.validate()

        assert errors == []

    def test_combat_configuration_validation_invalid_tick_interval(self) -> None:
        """Test configuration validation with invalid tick interval."""
        config = CombatConfiguration(combat_tick_interval=0)
        errors = config.validate()

        assert len(errors) == 1
        assert "Combat tick interval must be between 1 and 60 seconds" in errors[0]

    def test_combat_configuration_validation_invalid_timeout(self) -> None:
        """Test configuration validation with invalid timeout."""
        config = CombatConfiguration(combat_timeout_seconds=30)
        errors = config.validate()

        assert len(errors) == 1
        assert "Combat timeout must be between 60 and 1800 seconds" in errors[0]

    def test_combat_configuration_validation_invalid_xp_multiplier(self) -> None:
        """Test configuration validation with invalid XP multiplier."""
        config = CombatConfiguration(combat_xp_multiplier=0.5)
        errors = config.validate()

        assert len(errors) == 1
        assert "XP multiplier must be between 1.0 and 5.0" in errors[0]

    def test_combat_configuration_validation_multiple_errors(self) -> None:
        """Test configuration validation with multiple errors."""
        config = CombatConfiguration(combat_tick_interval=0, combat_timeout_seconds=30, combat_xp_multiplier=0.5)
        errors = config.validate()

        assert len(errors) == 3
        assert any("tick interval" in error for error in errors)
        assert any("timeout" in error for error in errors)
        assert any("XP multiplier" in error for error in errors)


class TestCombatConfigurationService:
    """Test CombatConfigurationService functionality."""

    @patch("server.services.combat_configuration_service.get_config")
    @patch("server.services.combat_configuration_service.get_feature_flags")
    def test_service_initialization(self, mock_get_feature_flags, mock_get_config, config_mock, feature_flags_mock):
        """Test service initialization."""
        mock_get_config.return_value = config_mock
        mock_get_feature_flags.return_value = feature_flags_mock

        service = CombatConfigurationService()
        assert service._config == config_mock
        assert service._feature_flags == feature_flags_mock

    @patch("server.services.combat_configuration_service.get_config")
    @patch("server.services.combat_configuration_service.get_feature_flags")
    def test_get_combat_configuration(self, mock_get_feature_flags, mock_get_config, config_mock, feature_flags_mock):
        """Test getting combat configuration."""
        mock_get_config.return_value = config_mock
        mock_get_feature_flags.return_value = feature_flags_mock

        service = CombatConfigurationService()
        config = service.get_combat_configuration()

        assert isinstance(config, CombatConfiguration)
        assert config.combat_enabled is True
        assert config.combat_tick_interval == 6
        assert config.combat_timeout_seconds == 180

    @patch("server.services.combat_configuration_service.get_config")
    @patch("server.services.combat_configuration_service.get_feature_flags")
    def test_get_combat_configuration_for_scope_global(
        self, mock_get_feature_flags, mock_get_config, config_mock, feature_flags_mock
    ):
        """Test getting configuration for global scope."""
        mock_get_config.return_value = config_mock
        mock_get_feature_flags.return_value = feature_flags_mock

        service = CombatConfigurationService()
        config = service.get_combat_configuration_for_scope(CombatConfigurationScope.GLOBAL)

        assert isinstance(config, CombatConfiguration)
        assert config.combat_enabled is True

    @patch("server.services.combat_configuration_service.get_config")
    @patch("server.services.combat_configuration_service.get_feature_flags")
    def test_get_combat_configuration_for_scope_with_override(
        self, mock_get_feature_flags, mock_get_config, config_mock, feature_flags_mock
    ):
        """Test getting configuration for scope with override."""
        mock_get_config.return_value = config_mock
        mock_get_feature_flags.return_value = feature_flags_mock

        service = CombatConfigurationService()

        # Set up override
        override_config = CombatConfiguration(combat_enabled=False, combat_tick_interval=10)
        service._overrides["room:test_room"] = override_config

        # Get configuration for room
        config = service.get_combat_configuration_for_scope(CombatConfigurationScope.ROOM, "test_room")

        assert config.combat_enabled is False
        assert config.combat_tick_interval == 10

    @patch("server.services.combat_configuration_service.get_config")
    @patch("server.services.combat_configuration_service.get_feature_flags")
    def test_update_combat_configuration_room_scope(
        self, mock_get_feature_flags, mock_get_config, config_mock, feature_flags_mock
    ):
        """Test updating configuration for room scope."""
        mock_get_config.return_value = config_mock
        mock_get_feature_flags.return_value = feature_flags_mock

        service = CombatConfigurationService()

        updates = {"combat_enabled": False, "combat_tick_interval": 10}
        updated_config = service.update_combat_configuration(updates, CombatConfigurationScope.ROOM, "test_room")

        assert updated_config.combat_enabled is False
        assert updated_config.combat_tick_interval == 10

        # Verify override was stored
        assert "room:test_room" in service._overrides

    @patch("server.services.combat_configuration_service.get_config")
    @patch("server.services.combat_configuration_service.get_feature_flags")
    def test_update_combat_configuration_invalid(
        self, mock_get_feature_flags, mock_get_config, config_mock, feature_flags_mock
    ):
        """Test updating configuration with invalid values."""
        mock_get_config.return_value = config_mock
        mock_get_feature_flags.return_value = feature_flags_mock

        service = CombatConfigurationService()

        updates = {"combat_tick_interval": 0}  # Invalid

        with pytest.raises(CombatConfigurationError) as exc_info:
            service.update_combat_configuration(updates, CombatConfigurationScope.ROOM, "test_room")

        assert "Invalid configuration" in str(exc_info.value)

    @patch("server.services.combat_configuration_service.get_config")
    @patch("server.services.combat_configuration_service.get_feature_flags")
    def test_update_combat_configuration_global_scope(
        self, mock_get_feature_flags, mock_get_config, config_mock, feature_flags_mock
    ):
        """Test updating configuration for global scope."""
        mock_get_config.return_value = config_mock
        mock_get_feature_flags.return_value = feature_flags_mock

        service = CombatConfigurationService()

        updates = {"combat_enabled": False}

        with pytest.raises(CombatConfigurationError) as exc_info:
            service.update_combat_configuration(updates, CombatConfigurationScope.GLOBAL)

        assert "Global configuration updates require server restart" in str(exc_info.value)

    @patch("server.services.combat_configuration_service.get_config")
    @patch("server.services.combat_configuration_service.get_feature_flags")
    def test_clear_scope_override(self, mock_get_feature_flags, mock_get_config, config_mock, feature_flags_mock):
        """Test clearing scope override."""
        mock_get_config.return_value = config_mock
        mock_get_feature_flags.return_value = feature_flags_mock

        service = CombatConfigurationService()

        # Set up override
        override_config = CombatConfiguration(combat_enabled=False)
        service._overrides["room:test_room"] = override_config

        # Clear override
        service.clear_scope_override(CombatConfigurationScope.ROOM, "test_room")

        # Verify override was removed
        assert "room:test_room" not in service._overrides

    @patch("server.services.combat_configuration_service.get_config")
    @patch("server.services.combat_configuration_service.get_feature_flags")
    def test_clear_all_overrides(self, mock_get_feature_flags, mock_get_config, config_mock, feature_flags_mock):
        """Test clearing all overrides."""
        mock_get_config.return_value = config_mock
        mock_get_feature_flags.return_value = feature_flags_mock

        service = CombatConfigurationService()

        # Set up overrides
        service._overrides["room:test_room"] = CombatConfiguration(combat_enabled=False)
        service._overrides["player:test_player"] = CombatConfiguration(combat_tick_interval=10)

        # Clear all overrides
        service.clear_all_overrides()

        # Verify all overrides were removed
        assert len(service._overrides) == 0

    @patch("server.services.combat_configuration_service.get_config")
    @patch("server.services.combat_configuration_service.get_feature_flags")
    def test_get_active_overrides(self, mock_get_feature_flags, mock_get_config, config_mock, feature_flags_mock):
        """Test getting active overrides."""
        mock_get_config.return_value = config_mock
        mock_get_feature_flags.return_value = feature_flags_mock

        service = CombatConfigurationService()

        # Set up overrides
        service._overrides["room:test_room"] = CombatConfiguration(combat_enabled=False)
        service._overrides["player:test_player"] = CombatConfiguration(combat_tick_interval=10)

        overrides = service.get_active_overrides()

        assert "room:test_room" in overrides
        assert "player:test_player" in overrides
        assert overrides["room:test_room"]["combat_enabled"] is False
        assert overrides["player:test_player"]["combat_tick_interval"] == 10

    @patch("server.services.combat_configuration_service.get_config")
    @patch("server.services.combat_configuration_service.get_feature_flags")
    def test_validate_configuration(self, mock_get_feature_flags, mock_get_config, config_mock, feature_flags_mock):
        """Test configuration validation."""
        mock_get_config.return_value = config_mock
        mock_get_feature_flags.return_value = feature_flags_mock

        service = CombatConfigurationService()

        # Test with valid configuration
        errors = service.validate_configuration()
        assert errors == []

        # Test with invalid configuration
        invalid_config = CombatConfiguration(combat_tick_interval=0)
        errors = service.validate_configuration(invalid_config)
        assert len(errors) == 1
        assert "tick interval" in errors[0]

    @patch("server.services.combat_configuration_service.get_config")
    @patch("server.services.combat_configuration_service.get_feature_flags")
    def test_is_combat_available_enabled(
        self, mock_get_feature_flags, mock_get_config, config_mock, feature_flags_mock
    ):
        """Test combat availability when enabled."""
        mock_get_config.return_value = config_mock
        mock_get_feature_flags.return_value = feature_flags_mock

        service = CombatConfigurationService()

        assert service.is_combat_available() is True
        assert service.is_combat_available("player123") is True
        assert service.is_combat_available("player123", "room456") is True

    @patch("server.services.combat_configuration_service.get_config")
    @patch("server.services.combat_configuration_service.get_feature_flags")
    def test_is_combat_available_disabled_feature_flag(
        self, mock_get_feature_flags, mock_get_config, config_mock, feature_flags_mock
    ):
        """Test combat availability when feature flag is disabled."""
        mock_get_config.return_value = config_mock
        feature_flags_mock.is_combat_enabled.return_value = False
        mock_get_feature_flags.return_value = feature_flags_mock

        service = CombatConfigurationService()

        assert service.is_combat_available() is False

    @patch("server.services.combat_configuration_service.get_config")
    @patch("server.services.combat_configuration_service.get_feature_flags")
    def test_is_combat_available_disabled_scope_config(
        self, mock_get_feature_flags, mock_get_config, config_mock, feature_flags_mock
    ):
        """Test combat availability when scope configuration is disabled."""
        mock_get_config.return_value = config_mock
        mock_get_feature_flags.return_value = feature_flags_mock

        service = CombatConfigurationService()

        # Set up room override with combat disabled
        override_config = CombatConfiguration(combat_enabled=False)
        service._overrides["room:test_room"] = override_config

        assert service.is_combat_available(room_id="test_room") is False

    @patch("server.services.combat_configuration_service.get_config")
    @patch("server.services.combat_configuration_service.get_feature_flags")
    def test_get_combat_settings_summary(
        self, mock_get_feature_flags, mock_get_config, config_mock, feature_flags_mock
    ):
        """Test getting combat settings summary."""
        mock_get_config.return_value = config_mock
        mock_get_feature_flags.return_value = feature_flags_mock

        service = CombatConfigurationService()

        summary = service.get_combat_settings_summary()

        assert "base_configuration" in summary
        assert "active_overrides" in summary
        assert "feature_flags" in summary
        assert "validation_errors" in summary

        assert summary["base_configuration"]["combat_enabled"] is True
        assert summary["feature_flags"]["combat_enabled"] is True
        assert summary["validation_errors"] == []

    @patch("server.services.combat_configuration_service.get_config")
    @patch("server.services.combat_configuration_service.get_feature_flags")
    def test_refresh_configuration(self, mock_get_feature_flags, mock_get_config, config_mock, feature_flags_mock):
        """Test refreshing configuration."""
        mock_get_config.return_value = config_mock
        mock_get_feature_flags.return_value = feature_flags_mock

        service = CombatConfigurationService()

        # Call refresh
        service.refresh_configuration()

        # Verify cache was cleared
        assert service._cached_config is None

    @patch("server.services.combat_configuration_service.get_config")
    @patch("server.services.combat_configuration_service.get_feature_flags")
    def test_clear_cache(self, mock_get_feature_flags, mock_get_config, config_mock, feature_flags_mock):
        """Test clearing cache."""
        mock_get_config.return_value = config_mock
        mock_get_feature_flags.return_value = feature_flags_mock

        service = CombatConfigurationService()

        # Populate cache
        service.get_combat_configuration()

        # Clear cache
        service.clear_cache()

        # Verify cache was cleared
        assert service._cached_config is None


class TestGlobalCombatConfigurationFunctions:
    """Test global combat configuration functions."""

    @patch("server.services.combat_configuration_service.combat_config")
    def test_get_combat_config(self, config_mock):
        """Test getting global combat configuration service."""
        result = get_combat_config()
        assert result == config_mock

    @patch("server.services.combat_configuration_service.combat_config")
    def test_refresh_combat_configuration(self, config_mock):
        """Test refreshing combat configuration."""
        refresh_combat_configuration()
        config_mock.refresh_configuration.assert_called_once()

    @patch("server.services.combat_configuration_service.combat_config")
    def test_get_combat_configuration_convenience(self, config_mock):
        """Test convenience function for getting combat configuration."""
        config_mock.get_combat_configuration.return_value = CombatConfiguration()

        result = get_combat_configuration()
        assert isinstance(result, CombatConfiguration)
        config_mock.get_combat_configuration.assert_called_once()

    @patch("server.services.combat_configuration_service.combat_config")
    def test_is_combat_available_convenience(self, config_mock):
        """Test convenience function for checking combat availability."""
        config_mock.is_combat_available.return_value = True

        result = is_combat_available("player123", "room456")
        assert result is True
        config_mock.is_combat_available.assert_called_once_with("player123", "room456")


class TestCombatConfigurationServiceIntegration:
    """Test combat configuration service integration scenarios."""

    @patch("server.services.combat_configuration_service.get_config")
    @patch("server.services.combat_configuration_service.get_feature_flags")
    def test_configuration_caching(self, mock_get_feature_flags, mock_get_config, config_mock, feature_flags_mock):
        """Test that configuration is properly cached."""
        mock_get_config.return_value = config_mock
        mock_get_feature_flags.return_value = feature_flags_mock

        service = CombatConfigurationService()

        # First call should populate cache
        service.get_combat_configuration()
        assert service._cached_config is not None

        # Second call should use cache
        service.get_combat_configuration()
        assert service._cached_config is not None

        # get_config should only be called once due to caching
        assert mock_get_config.call_count == 1

    @patch("server.services.combat_configuration_service.get_config")
    @patch("server.services.combat_configuration_service.get_feature_flags")
    def test_scope_override_priority(self, mock_get_feature_flags, mock_get_config, config_mock, feature_flags_mock):
        """Test that scope overrides take priority over base configuration."""
        mock_get_config.return_value = config_mock
        mock_get_feature_flags.return_value = feature_flags_mock

        service = CombatConfigurationService()

        # Set up room override
        override_config = CombatConfiguration(combat_enabled=False, combat_tick_interval=10)
        service._overrides["room:test_room"] = override_config

        # Get base configuration
        base_config = service.get_combat_configuration()
        assert base_config.combat_enabled is True
        assert base_config.combat_tick_interval == 6

        # Get room configuration
        room_config = service.get_combat_configuration_for_scope(CombatConfigurationScope.ROOM, "test_room")
        assert room_config.combat_enabled is False
        assert room_config.combat_tick_interval == 10

    @patch("server.services.combat_configuration_service.get_config")
    @patch("server.services.combat_configuration_service.get_feature_flags")
    def test_configuration_update_flow(self, mock_get_feature_flags, mock_get_config, config_mock, feature_flags_mock):
        """Test complete configuration update flow."""
        mock_get_config.return_value = config_mock
        mock_get_feature_flags.return_value = feature_flags_mock

        service = CombatConfigurationService()

        # Initial configuration
        initial_config = service.get_combat_configuration_for_scope(CombatConfigurationScope.ROOM, "test_room")
        assert initial_config.combat_enabled is True

        # Update configuration
        updates = {"combat_enabled": False, "combat_tick_interval": 10}
        updated_config = service.update_combat_configuration(updates, CombatConfigurationScope.ROOM, "test_room")

        assert updated_config.combat_enabled is False
        assert updated_config.combat_tick_interval == 10

        # Verify update is reflected in subsequent calls
        retrieved_config = service.get_combat_configuration_for_scope(CombatConfigurationScope.ROOM, "test_room")
        assert retrieved_config.combat_enabled is False
        assert retrieved_config.combat_tick_interval == 10

        # Clear override
        service.clear_scope_override(CombatConfigurationScope.ROOM, "test_room")

        # Verify configuration returns to base
        final_config = service.get_combat_configuration_for_scope(CombatConfigurationScope.ROOM, "test_room")
        assert final_config.combat_enabled is True
        assert final_config.combat_tick_interval == 6


class TestCombatConfigurationServiceErrorHandling:
    """Test combat configuration service error handling."""

    @patch("server.services.combat_configuration_service.get_config")
    @patch("server.services.combat_configuration_service.get_feature_flags")
    def test_invalid_configuration_update(
        self, mock_get_feature_flags, mock_get_config, config_mock, feature_flags_mock
    ):
        """Test handling of invalid configuration updates."""
        mock_get_config.return_value = config_mock
        mock_get_feature_flags.return_value = feature_flags_mock

        service = CombatConfigurationService()

        # Try to update with invalid values
        invalid_updates = {"combat_tick_interval": 0, "combat_timeout_seconds": 30, "combat_xp_multiplier": 0.5}

        with pytest.raises(CombatConfigurationError) as exc_info:
            service.update_combat_configuration(invalid_updates, CombatConfigurationScope.ROOM, "test_room")

        error_message = str(exc_info.value)
        assert "Invalid configuration" in error_message
        assert "tick interval" in error_message

    @patch("server.services.combat_configuration_service.get_config")
    @patch("server.services.combat_configuration_service.get_feature_flags")
    def test_clear_global_scope_override(
        self, mock_get_feature_flags, mock_get_config, config_mock, feature_flags_mock
    ):
        """Test error when trying to clear global scope override."""
        mock_get_config.return_value = config_mock
        mock_get_feature_flags.return_value = feature_flags_mock

        service = CombatConfigurationService()

        with pytest.raises(CombatConfigurationError) as exc_info:
            service.clear_scope_override(CombatConfigurationScope.GLOBAL, "global")

        assert "Cannot clear global configuration" in str(exc_info.value)
