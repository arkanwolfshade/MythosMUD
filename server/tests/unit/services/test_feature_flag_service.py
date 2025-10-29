"""
Tests for feature flag service.

These tests verify that the feature flag service properly manages
combat feature flags, handles configuration changes, and provides
reliable access to feature states.
"""

from unittest.mock import MagicMock, patch

import pytest

from server.services.feature_flag_service import (
    FeatureFlagService,
    get_feature_flags,
    is_combat_enabled,
    is_combat_logging_enabled,
    is_combat_monitoring_enabled,
    refresh_feature_flags,
)


@pytest.fixture
def mock_config():
    """Mock configuration for testing."""
    mock_config = MagicMock()
    mock_config.game.combat_enabled = True
    mock_config.game.combat_logging_enabled = True
    mock_config.game.combat_monitoring_enabled = True
    mock_config.game.combat_tick_interval = 6
    mock_config.game.combat_timeout_seconds = 180
    mock_config.game.combat_xp_multiplier = 1.0
    mock_config.game.combat_alert_threshold = 5
    mock_config.game.combat_performance_threshold = 1000
    mock_config.game.combat_error_threshold = 3
    return mock_config


class TestFeatureFlagService:
    """Test FeatureFlagService functionality."""

    @patch("server.services.feature_flag_service.get_config")
    def test_feature_flag_service_initialization(self, mock_get_config, mock_config):
        """Test feature flag service initialization."""
        mock_get_config.return_value = mock_config

        service = FeatureFlagService()
        assert service._config == mock_config

    @patch("server.services.feature_flag_service.get_config")
    def test_is_combat_enabled_true(self, mock_get_config, mock_config):
        """Test combat enabled returns True when enabled."""
        mock_get_config.return_value = mock_config

        service = FeatureFlagService()
        assert service.is_combat_enabled() is True

    @patch("server.services.feature_flag_service.get_config")
    def test_is_combat_enabled_false(self, mock_get_config, mock_config):
        """Test combat enabled returns False when disabled."""
        mock_config.game.combat_enabled = False
        mock_get_config.return_value = mock_config

        service = FeatureFlagService()
        assert service.is_combat_enabled() is False

    @patch("server.services.feature_flag_service.get_config")
    def test_is_combat_logging_enabled_true(self, mock_get_config, mock_config):
        """Test combat logging enabled returns True when enabled."""
        mock_get_config.return_value = mock_config

        service = FeatureFlagService()
        assert service.is_combat_logging_enabled() is True

    @patch("server.services.feature_flag_service.get_config")
    def test_is_combat_logging_enabled_false(self, mock_get_config, mock_config):
        """Test combat logging enabled returns False when disabled."""
        mock_config.game.combat_logging_enabled = False
        mock_get_config.return_value = mock_config

        service = FeatureFlagService()
        assert service.is_combat_logging_enabled() is False

    @patch("server.services.feature_flag_service.get_config")
    def test_is_combat_monitoring_enabled_true(self, mock_get_config, mock_config):
        """Test combat monitoring enabled returns True when enabled."""
        mock_get_config.return_value = mock_config

        service = FeatureFlagService()
        assert service.is_combat_monitoring_enabled() is True

    @patch("server.services.feature_flag_service.get_config")
    def test_is_combat_monitoring_enabled_false(self, mock_get_config, mock_config):
        """Test combat monitoring enabled returns False when disabled."""
        mock_config.game.combat_monitoring_enabled = False
        mock_get_config.return_value = mock_config

        service = FeatureFlagService()
        assert service.is_combat_monitoring_enabled() is False

    @patch("server.services.feature_flag_service.get_config")
    def test_get_combat_configuration(self, mock_get_config, mock_config):
        """Test getting combat configuration."""
        mock_get_config.return_value = mock_config

        service = FeatureFlagService()
        config = service.get_combat_configuration()

        assert config["combat_enabled"] is True
        assert config["combat_tick_interval"] == 6
        assert config["combat_timeout_seconds"] == 180
        assert config["combat_xp_multiplier"] == 1.0
        assert config["combat_logging_enabled"] is True
        assert config["combat_monitoring_enabled"] is True
        assert config["combat_alert_threshold"] == 5
        assert config["combat_performance_threshold"] == 1000
        assert config["combat_error_threshold"] == 3

    @patch("server.services.feature_flag_service.get_config")
    def test_clear_cache(self, mock_get_config, mock_config):
        """Test clearing feature flag cache."""
        mock_get_config.return_value = mock_config

        service = FeatureFlagService()

        # Call methods to populate cache
        service.is_combat_enabled()
        service.is_combat_logging_enabled()
        service.is_combat_monitoring_enabled()

        # Clear cache
        service.clear_cache()

        # Verify cache is cleared by checking cached values
        assert service._cached_combat_enabled is None
        assert service._cached_combat_logging_enabled is None
        assert service._cached_combat_monitoring_enabled is None

    @patch("server.services.feature_flag_service.get_config")
    def test_validate_combat_requirements_enabled_valid(self, mock_get_config, mock_config):
        """Test combat requirements validation when enabled and valid."""
        mock_get_config.return_value = mock_config

        service = FeatureFlagService()
        assert service.validate_combat_requirements() is True

    @patch("server.services.feature_flag_service.get_config")
    def test_validate_combat_requirements_disabled(self, mock_get_config, mock_config):
        """Test combat requirements validation when disabled."""
        mock_config.game.combat_enabled = False
        mock_get_config.return_value = mock_config

        service = FeatureFlagService()
        assert service.validate_combat_requirements() is True

    @patch("server.services.feature_flag_service.get_config")
    def test_validate_combat_requirements_invalid_tick_interval(self, mock_get_config, mock_config):
        """Test combat requirements validation with invalid tick interval."""
        mock_config.game.combat_enabled = True
        mock_config.game.combat_tick_interval = 0
        mock_get_config.return_value = mock_config

        service = FeatureFlagService()
        assert service.validate_combat_requirements() is False

    @patch("server.services.feature_flag_service.get_config")
    def test_validate_combat_requirements_invalid_timeout(self, mock_get_config, mock_config):
        """Test combat requirements validation with invalid timeout."""
        mock_config.game.combat_enabled = True
        mock_config.game.combat_timeout_seconds = 30
        mock_get_config.return_value = mock_config

        service = FeatureFlagService()
        assert service.validate_combat_requirements() is False

    @patch("server.services.feature_flag_service.get_config")
    def test_validate_combat_requirements_invalid_xp_multiplier(self, mock_get_config, mock_config):
        """Test combat requirements validation with invalid XP multiplier."""
        mock_config.game.combat_enabled = True
        mock_config.game.combat_xp_multiplier = 0.5
        mock_get_config.return_value = mock_config

        service = FeatureFlagService()
        assert service.validate_combat_requirements() is False

    @patch("server.services.feature_flag_service.get_config")
    def test_get_feature_status(self, mock_get_config, mock_config):
        """Test getting feature status."""
        mock_get_config.return_value = mock_config

        service = FeatureFlagService()
        status = service.get_feature_status()

        assert "combat" in status
        assert status["combat"]["enabled"] is True
        assert status["combat"]["logging_enabled"] is True
        assert status["combat"]["monitoring_enabled"] is True
        assert "configuration" in status["combat"]

    @patch("server.services.feature_flag_service.get_config")
    def test_check_combat_availability_enabled(self, mock_get_config, mock_config):
        """Test combat availability when enabled."""
        mock_get_config.return_value = mock_config

        service = FeatureFlagService()
        assert service.check_combat_availability() is True
        assert service.check_combat_availability("player123") is True

    @patch("server.services.feature_flag_service.get_config")
    def test_check_combat_availability_disabled(self, mock_get_config, mock_config):
        """Test combat availability when disabled."""
        mock_config.game.combat_enabled = False
        mock_get_config.return_value = mock_config

        service = FeatureFlagService()
        assert service.check_combat_availability() is False
        assert service.check_combat_availability("player123") is False

    @patch("server.services.feature_flag_service.get_config")
    def test_check_combat_availability_invalid_requirements(self, mock_get_config, mock_config):
        """Test combat availability when requirements are invalid."""
        mock_config.game.combat_enabled = True
        mock_config.game.combat_tick_interval = 0  # Invalid
        mock_get_config.return_value = mock_config

        service = FeatureFlagService()
        assert service.check_combat_availability() is False
        assert service.check_combat_availability("player123") is False


class TestGlobalFeatureFlagFunctions:
    """Test global feature flag functions."""

    @patch("server.services.feature_flag_service.feature_flags")
    def test_get_feature_flags(self, mock_flags):
        """Test getting global feature flag service."""
        result = get_feature_flags()
        assert result == mock_flags

    @patch("server.services.feature_flag_service.feature_flags")
    def test_refresh_feature_flags(self, mock_flags):
        """Test refreshing feature flags."""
        refresh_feature_flags()
        mock_flags.clear_cache.assert_called_once()

    @patch("server.services.feature_flag_service.feature_flags")
    def test_is_combat_enabled_convenience(self, mock_flags):
        """Test convenience function for combat enabled."""
        mock_flags.is_combat_enabled.return_value = True

        result = is_combat_enabled()
        assert result is True
        mock_flags.is_combat_enabled.assert_called_once()

    @patch("server.services.feature_flag_service.feature_flags")
    def test_is_combat_logging_enabled_convenience(self, mock_flags):
        """Test convenience function for combat logging enabled."""
        mock_flags.is_combat_logging_enabled.return_value = True

        result = is_combat_logging_enabled()
        assert result is True
        mock_flags.is_combat_logging_enabled.assert_called_once()

    @patch("server.services.feature_flag_service.feature_flags")
    def test_is_combat_monitoring_enabled_convenience(self, mock_flags):
        """Test convenience function for combat monitoring enabled."""
        mock_flags.is_combat_monitoring_enabled.return_value = True

        result = is_combat_monitoring_enabled()
        assert result is True
        mock_flags.is_combat_monitoring_enabled.assert_called_once()


class TestFeatureFlagServiceIntegration:
    """Test feature flag service integration scenarios."""

    @patch("server.services.feature_flag_service.get_config")
    def test_feature_flag_caching(self, mock_get_config, mock_config):
        """Test that feature flags are properly cached."""
        mock_get_config.return_value = mock_config

        service = FeatureFlagService()

        # First call should populate cache
        service.is_combat_enabled()
        assert service._cached_combat_enabled is not None

        # Second call should use cache
        service.is_combat_enabled()
        assert service._cached_combat_enabled is not None

        # get_config should only be called once due to caching
        assert mock_get_config.call_count == 1

    @patch("server.services.feature_flag_service.get_config")
    def test_configuration_change_handling(self, mock_get_config, mock_config):
        """Test handling of configuration changes."""
        mock_get_config.return_value = mock_config

        service = FeatureFlagService()

        # Initial state
        assert service.is_combat_enabled() is True

        # Change configuration
        mock_config.game.combat_enabled = False

        # Cache should still return old value
        assert service.is_combat_enabled() is True

        # Clear cache to get new value
        service.clear_cache()
        assert service.is_combat_enabled() is False

    @patch("server.services.feature_flag_service.get_config")
    def test_combat_configuration_completeness(self, mock_get_config, mock_config):
        """Test that combat configuration is complete."""
        mock_get_config.return_value = mock_config

        service = FeatureFlagService()
        config = service.get_combat_configuration()

        # Verify all expected keys are present
        expected_keys = {
            "combat_enabled",
            "combat_tick_interval",
            "combat_timeout_seconds",
            "combat_xp_multiplier",
            "combat_logging_enabled",
            "combat_monitoring_enabled",
            "combat_alert_threshold",
            "combat_performance_threshold",
            "combat_error_threshold",
        }

        assert set(config.keys()) == expected_keys

    @patch("server.services.feature_flag_service.get_config")
    def test_feature_status_completeness(self, mock_get_config, mock_config):
        """Test that feature status is complete."""
        mock_get_config.return_value = mock_config

        service = FeatureFlagService()
        status = service.get_feature_status()

        # Verify combat section is present
        assert "combat" in status
        combat_status = status["combat"]

        # Verify all expected keys are present
        expected_keys = {
            "enabled",
            "logging_enabled",
            "monitoring_enabled",
            "configuration",
        }

        assert set(combat_status.keys()) == expected_keys


class TestFeatureFlagServiceErrorHandling:
    """Test feature flag service error handling."""

    @patch("server.services.feature_flag_service.get_config")
    def test_config_access_error(self, mock_get_config):
        """Test handling of configuration access errors."""
        mock_get_config.side_effect = Exception("Config access error")

        with pytest.raises(Exception) as exc_info:
            FeatureFlagService()
        assert "Config access error" in str(exc_info.value)

    @patch("server.services.feature_flag_service.get_config")
    def test_combat_configuration_access_error(self, mock_get_config, mock_config):
        """Test handling of combat configuration access errors."""
        mock_config.game.combat_enabled = True
        mock_config.game.combat_tick_interval = 6
        mock_config.game.combat_timeout_seconds = 180
        mock_config.game.combat_xp_multiplier = 1.0
        mock_get_config.return_value = mock_config

        service = FeatureFlagService()

        # Simulate error accessing configuration
        mock_config.game.combat_tick_interval = None

        # Should handle gracefully
        config = service.get_combat_configuration()
        assert config["combat_tick_interval"] is None

    @patch("server.services.feature_flag_service.get_config")
    def test_validation_error_handling(self, mock_get_config, mock_config):
        """Test error handling in validation."""
        mock_config.game.combat_enabled = True
        mock_config.game.combat_tick_interval = -1  # Invalid value
        mock_get_config.return_value = mock_config

        service = FeatureFlagService()

        # Should return False for invalid configuration
        assert service.validate_combat_requirements() is False
        assert service.check_combat_availability() is False
