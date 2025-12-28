"""
Unit tests for feature flag service.

Tests the FeatureFlagService class and global convenience functions
for managing feature flags with caching and validation.
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


class TestFeatureFlagService:
    """Test suite for FeatureFlagService class."""

    def test_init(self):
        """Test FeatureFlagService initialization."""
        with patch("server.services.feature_flag_service.get_config") as mock_get_config:
            mock_config = MagicMock()
            mock_config.game.combat_enabled = True
            mock_config.game.combat_logging_enabled = False
            mock_config.game.combat_monitoring_enabled = True
            mock_get_config.return_value = mock_config

            service = FeatureFlagService()
            assert service._config == mock_config
            assert service._cached_combat_enabled is None
            assert service._cached_combat_logging_enabled is None
            assert service._cached_combat_monitoring_enabled is None

    def test_is_combat_enabled_true(self):
        """Test is_combat_enabled returns True when enabled."""
        with patch("server.services.feature_flag_service.get_config") as mock_get_config:
            mock_config = MagicMock()
            mock_config.game.combat_enabled = True
            mock_get_config.return_value = mock_config

            service = FeatureFlagService()
            result = service.is_combat_enabled()
            assert result is True
            assert service._cached_combat_enabled is True

    def test_is_combat_enabled_false(self):
        """Test is_combat_enabled returns False when disabled."""
        with patch("server.services.feature_flag_service.get_config") as mock_get_config:
            mock_config = MagicMock()
            mock_config.game.combat_enabled = False
            mock_get_config.return_value = mock_config

            service = FeatureFlagService()
            result = service.is_combat_enabled()
            assert result is False
            assert service._cached_combat_enabled is False

    def test_is_combat_enabled_caching(self):
        """Test is_combat_enabled caches the result."""
        with patch("server.services.feature_flag_service.get_config") as mock_get_config:
            mock_config = MagicMock()
            mock_config.game.combat_enabled = True
            mock_get_config.return_value = mock_config

            service = FeatureFlagService()
            # First call should read from config
            result1 = service.is_combat_enabled()
            # Change config value
            mock_config.game.combat_enabled = False
            # Second call should use cached value
            result2 = service.is_combat_enabled()
            assert result1 is True
            assert result2 is True  # Should still be True due to caching
            # Verify config was only accessed once
            assert mock_config.game.combat_enabled == False  # Config changed but cache used

    def test_is_combat_logging_enabled_true(self):
        """Test is_combat_logging_enabled returns True when enabled."""
        with patch("server.services.feature_flag_service.get_config") as mock_get_config:
            mock_config = MagicMock()
            mock_config.game.combat_logging_enabled = True
            mock_get_config.return_value = mock_config

            service = FeatureFlagService()
            result = service.is_combat_logging_enabled()
            assert result is True
            assert service._cached_combat_logging_enabled is True

    def test_is_combat_logging_enabled_false(self):
        """Test is_combat_logging_enabled returns False when disabled."""
        with patch("server.services.feature_flag_service.get_config") as mock_get_config:
            mock_config = MagicMock()
            mock_config.game.combat_logging_enabled = False
            mock_get_config.return_value = mock_config

            service = FeatureFlagService()
            result = service.is_combat_logging_enabled()
            assert result is False
            assert service._cached_combat_logging_enabled is False

    def test_is_combat_monitoring_enabled_true(self):
        """Test is_combat_monitoring_enabled returns True when enabled."""
        with patch("server.services.feature_flag_service.get_config") as mock_get_config:
            mock_config = MagicMock()
            mock_config.game.combat_monitoring_enabled = True
            mock_get_config.return_value = mock_config

            service = FeatureFlagService()
            result = service.is_combat_monitoring_enabled()
            assert result is True
            assert service._cached_combat_monitoring_enabled is True

    def test_is_combat_monitoring_enabled_false(self):
        """Test is_combat_monitoring_enabled returns False when disabled."""
        with patch("server.services.feature_flag_service.get_config") as mock_get_config:
            mock_config = MagicMock()
            mock_config.game.combat_monitoring_enabled = False
            mock_get_config.return_value = mock_config

            service = FeatureFlagService()
            result = service.is_combat_monitoring_enabled()
            assert result is False
            assert service._cached_combat_monitoring_enabled is False

    def test_get_combat_configuration(self):
        """Test get_combat_configuration returns all combat settings."""
        with patch("server.services.feature_flag_service.get_config") as mock_get_config:
            mock_config = MagicMock()
            mock_config.game.combat_enabled = True
            mock_config.game.combat_tick_interval = 5
            mock_config.game.combat_timeout_seconds = 300
            mock_config.game.combat_xp_multiplier = 1.5
            mock_config.game.combat_logging_enabled = True
            mock_config.game.combat_monitoring_enabled = False
            mock_config.game.combat_alert_threshold = 10
            mock_config.game.combat_performance_threshold = 100
            mock_config.game.combat_error_threshold = 5
            mock_get_config.return_value = mock_config

            service = FeatureFlagService()
            config = service.get_combat_configuration()
            assert config["combat_enabled"] is True
            assert config["combat_tick_interval"] == 5
            assert config["combat_timeout_seconds"] == 300
            assert config["combat_xp_multiplier"] == 1.5
            assert config["combat_logging_enabled"] is True
            assert config["combat_monitoring_enabled"] is False
            assert config["combat_alert_threshold"] == 10
            assert config["combat_performance_threshold"] == 100
            assert config["combat_error_threshold"] == 5

    def test_clear_cache(self):
        """Test clear_cache resets all cached values."""
        with patch("server.services.feature_flag_service.get_config") as mock_get_config:
            mock_config = MagicMock()
            mock_config.game.combat_enabled = True
            mock_config.game.combat_logging_enabled = True
            mock_config.game.combat_monitoring_enabled = True
            mock_get_config.return_value = mock_config

            service = FeatureFlagService()
            # Populate cache
            service.is_combat_enabled()
            service.is_combat_logging_enabled()
            service.is_combat_monitoring_enabled()
            # Verify cache is populated
            assert service._cached_combat_enabled is True
            assert service._cached_combat_logging_enabled is True
            assert service._cached_combat_monitoring_enabled is True
            # Clear cache
            service.clear_cache()
            # Verify cache is cleared
            assert service._cached_combat_enabled is None
            assert service._cached_combat_logging_enabled is None
            assert service._cached_combat_monitoring_enabled is None

    def test_validate_combat_requirements_disabled(self):
        """Test validate_combat_requirements returns True when combat is disabled."""
        with patch("server.services.feature_flag_service.get_config") as mock_get_config:
            mock_config = MagicMock()
            mock_config.game.combat_enabled = False
            mock_get_config.return_value = mock_config

            service = FeatureFlagService()
            result = service.validate_combat_requirements()
            assert result is True

    def test_validate_combat_requirements_valid(self):
        """Test validate_combat_requirements returns True with valid configuration."""
        with patch("server.services.feature_flag_service.get_config") as mock_get_config:
            mock_config = MagicMock()
            mock_config.game.combat_enabled = True
            mock_config.game.combat_tick_interval = 5
            mock_config.game.combat_timeout_seconds = 300
            mock_config.game.combat_xp_multiplier = 1.5
            mock_config.game.combat_logging_enabled = True
            mock_config.game.combat_monitoring_enabled = False
            mock_config.game.combat_alert_threshold = 10
            mock_config.game.combat_performance_threshold = 100
            mock_config.game.combat_error_threshold = 5
            mock_get_config.return_value = mock_config

            service = FeatureFlagService()
            result = service.validate_combat_requirements()
            assert result is True

    def test_validate_combat_requirements_invalid_tick_interval(self):
        """Test validate_combat_requirements returns False with invalid tick interval."""
        with patch("server.services.feature_flag_service.get_config") as mock_get_config:
            mock_config = MagicMock()
            mock_config.game.combat_enabled = True
            mock_config.game.combat_tick_interval = 0  # Invalid: less than 1
            mock_config.game.combat_timeout_seconds = 300
            mock_config.game.combat_xp_multiplier = 1.5
            mock_config.game.combat_logging_enabled = True
            mock_config.game.combat_monitoring_enabled = False
            mock_config.game.combat_alert_threshold = 10
            mock_config.game.combat_performance_threshold = 100
            mock_config.game.combat_error_threshold = 5
            mock_get_config.return_value = mock_config

            service = FeatureFlagService()
            result = service.validate_combat_requirements()
            assert result is False

    def test_validate_combat_requirements_invalid_timeout(self):
        """Test validate_combat_requirements returns False with invalid timeout."""
        with patch("server.services.feature_flag_service.get_config") as mock_get_config:
            mock_config = MagicMock()
            mock_config.game.combat_enabled = True
            mock_config.game.combat_tick_interval = 5
            mock_config.game.combat_timeout_seconds = 30  # Invalid: less than 60
            mock_config.game.combat_xp_multiplier = 1.5
            mock_config.game.combat_logging_enabled = True
            mock_config.game.combat_monitoring_enabled = False
            mock_config.game.combat_alert_threshold = 10
            mock_config.game.combat_performance_threshold = 100
            mock_config.game.combat_error_threshold = 5
            mock_get_config.return_value = mock_config

            service = FeatureFlagService()
            result = service.validate_combat_requirements()
            assert result is False

    def test_validate_combat_requirements_invalid_xp_multiplier(self):
        """Test validate_combat_requirements returns False with invalid XP multiplier."""
        with patch("server.services.feature_flag_service.get_config") as mock_get_config:
            mock_config = MagicMock()
            mock_config.game.combat_enabled = True
            mock_config.game.combat_tick_interval = 5
            mock_config.game.combat_timeout_seconds = 300
            mock_config.game.combat_xp_multiplier = 0.5  # Invalid: less than 1.0
            mock_config.game.combat_logging_enabled = True
            mock_config.game.combat_monitoring_enabled = False
            mock_config.game.combat_alert_threshold = 10
            mock_config.game.combat_performance_threshold = 100
            mock_config.game.combat_error_threshold = 5
            mock_get_config.return_value = mock_config

            service = FeatureFlagService()
            result = service.validate_combat_requirements()
            assert result is False

    def test_get_feature_status(self):
        """Test get_feature_status returns complete feature status."""
        with patch("server.services.feature_flag_service.get_config") as mock_get_config:
            mock_config = MagicMock()
            mock_config.game.combat_enabled = True
            mock_config.game.combat_tick_interval = 5
            mock_config.game.combat_timeout_seconds = 300
            mock_config.game.combat_xp_multiplier = 1.5
            mock_config.game.combat_logging_enabled = True
            mock_config.game.combat_monitoring_enabled = False
            mock_config.game.combat_alert_threshold = 10
            mock_config.game.combat_performance_threshold = 100
            mock_config.game.combat_error_threshold = 5
            mock_get_config.return_value = mock_config

            service = FeatureFlagService()
            status = service.get_feature_status()
            assert "combat" in status
            assert status["combat"]["enabled"] is True
            assert status["combat"]["logging_enabled"] is True
            assert status["combat"]["monitoring_enabled"] is False
            assert "configuration" in status["combat"]

    def test_check_combat_availability_enabled(self):
        """Test check_combat_availability returns True when combat is enabled and valid."""
        with patch("server.services.feature_flag_service.get_config") as mock_get_config:
            mock_config = MagicMock()
            mock_config.game.combat_enabled = True
            mock_config.game.combat_tick_interval = 5
            mock_config.game.combat_timeout_seconds = 300
            mock_config.game.combat_xp_multiplier = 1.5
            mock_config.game.combat_logging_enabled = True
            mock_config.game.combat_monitoring_enabled = False
            mock_config.game.combat_alert_threshold = 10
            mock_config.game.combat_performance_threshold = 100
            mock_config.game.combat_error_threshold = 5
            mock_get_config.return_value = mock_config

            service = FeatureFlagService()
            result = service.check_combat_availability()
            assert result is True

    def test_check_combat_availability_disabled(self):
        """Test check_combat_availability returns False when combat is disabled."""
        with patch("server.services.feature_flag_service.get_config") as mock_get_config:
            mock_config = MagicMock()
            mock_config.game.combat_enabled = False
            mock_get_config.return_value = mock_config

            service = FeatureFlagService()
            result = service.check_combat_availability()
            assert result is False

    def test_check_combat_availability_invalid_requirements(self):
        """Test check_combat_availability returns False when requirements are invalid."""
        with patch("server.services.feature_flag_service.get_config") as mock_get_config:
            mock_config = MagicMock()
            mock_config.game.combat_enabled = True
            mock_config.game.combat_tick_interval = 0  # Invalid
            mock_config.game.combat_timeout_seconds = 300
            mock_config.game.combat_xp_multiplier = 1.5
            mock_config.game.combat_logging_enabled = True
            mock_config.game.combat_monitoring_enabled = False
            mock_config.game.combat_alert_threshold = 10
            mock_config.game.combat_performance_threshold = 100
            mock_config.game.combat_error_threshold = 5
            mock_get_config.return_value = mock_config

            service = FeatureFlagService()
            result = service.check_combat_availability()
            assert result is False

    def test_check_combat_availability_with_player_id(self):
        """Test check_combat_availability with player ID parameter."""
        with patch("server.services.feature_flag_service.get_config") as mock_get_config:
            mock_config = MagicMock()
            mock_config.game.combat_enabled = True
            mock_config.game.combat_tick_interval = 5
            mock_config.game.combat_timeout_seconds = 300
            mock_config.game.combat_xp_multiplier = 1.5
            mock_config.game.combat_logging_enabled = True
            mock_config.game.combat_monitoring_enabled = False
            mock_config.game.combat_alert_threshold = 10
            mock_config.game.combat_performance_threshold = 100
            mock_config.game.combat_error_threshold = 5
            mock_get_config.return_value = mock_config

            service = FeatureFlagService()
            result = service.check_combat_availability(player_id="test-player-123")
            assert result is True


class TestGlobalFunctions:
    """Test suite for global convenience functions."""

    def test_get_feature_flags(self):
        """Test get_feature_flags returns the global service instance."""
        from server.services.feature_flag_service import feature_flags

        result = get_feature_flags()
        assert result is feature_flags
        assert isinstance(result, FeatureFlagService)

    def test_is_combat_enabled_global(self):
        """Test global is_combat_enabled function."""
        with patch("server.services.feature_flag_service.feature_flags") as mock_flags:
            mock_flags.is_combat_enabled.return_value = True
            result = is_combat_enabled()
            assert result is True
            mock_flags.is_combat_enabled.assert_called_once()

    def test_is_combat_logging_enabled_global(self):
        """Test global is_combat_logging_enabled function."""
        with patch("server.services.feature_flag_service.feature_flags") as mock_flags:
            mock_flags.is_combat_logging_enabled.return_value = True
            result = is_combat_logging_enabled()
            assert result is True
            mock_flags.is_combat_logging_enabled.assert_called_once()

    def test_is_combat_monitoring_enabled_global(self):
        """Test global is_combat_monitoring_enabled function."""
        with patch("server.services.feature_flag_service.feature_flags") as mock_flags:
            mock_flags.is_combat_monitoring_enabled.return_value = True
            result = is_combat_monitoring_enabled()
            assert result is True
            mock_flags.is_combat_monitoring_enabled.assert_called_once()

    def test_refresh_feature_flags(self):
        """Test refresh_feature_flags clears cache."""
        with patch("server.services.feature_flag_service.feature_flags") as mock_flags:
            refresh_feature_flags()
            mock_flags.clear_cache.assert_called_once()
