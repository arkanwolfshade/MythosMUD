"""
Unit tests for combat configuration service.

Tests the CombatConfigurationService class for managing combat configuration settings.
"""

from unittest.mock import MagicMock, patch

import pytest

from server.services.combat_configuration_service import (
    CombatConfiguration,
    CombatConfigurationError,
    CombatConfigurationScope,
    CombatConfigurationService,
)


class TestCombatConfiguration:
    """Test suite for CombatConfiguration dataclass."""

    def test_init_defaults(self):
        """Test CombatConfiguration initialization with defaults."""
        config = CombatConfiguration()
        assert config.combat_enabled is True
        assert config.combat_tick_interval == 6
        assert config.combat_timeout_seconds == 180
        assert config.combat_xp_multiplier == 1.0

    def test_init_custom_values(self):
        """Test CombatConfiguration initialization with custom values."""
        config = CombatConfiguration(
            combat_enabled=False,
            combat_tick_interval=10,
            combat_timeout_seconds=300,
            combat_xp_multiplier=2.0,
        )
        assert config.combat_enabled is False
        assert config.combat_tick_interval == 10
        assert config.combat_timeout_seconds == 300
        assert config.combat_xp_multiplier == 2.0

    def test_to_dict(self):
        """Test to_dict converts configuration to dictionary."""
        config = CombatConfiguration(combat_enabled=False, combat_tick_interval=5)
        result = config.to_dict()
        assert isinstance(result, dict)
        assert result["combat_enabled"] is False
        assert result["combat_tick_interval"] == 5

    def test_from_dict(self):
        """Test from_dict creates configuration from dictionary."""
        data = {
            "combat_enabled": False,
            "combat_tick_interval": 8,
            "combat_timeout_seconds": 240,
            "combat_xp_multiplier": 1.5,
        }
        config = CombatConfiguration.from_dict(data)
        assert config.combat_enabled is False
        assert config.combat_tick_interval == 8
        assert config.combat_timeout_seconds == 240
        assert config.combat_xp_multiplier == 1.5

    def test_validate_valid(self):
        """Test validate returns empty list for valid configuration."""
        config = CombatConfiguration()
        errors = config.validate()
        assert len(errors) == 0

    def test_validate_invalid_tick_interval_too_low(self):
        """Test validate catches tick interval too low."""
        config = CombatConfiguration(combat_tick_interval=0)
        errors = config.validate()
        assert len(errors) > 0
        assert any("tick interval" in error.lower() for error in errors)

    def test_validate_invalid_tick_interval_too_high(self):
        """Test validate catches tick interval too high."""
        config = CombatConfiguration(combat_tick_interval=61)
        errors = config.validate()
        assert len(errors) > 0

    def test_validate_invalid_timeout_too_low(self):
        """Test validate catches timeout too low."""
        config = CombatConfiguration(combat_timeout_seconds=59)
        errors = config.validate()
        assert len(errors) > 0
        assert any("timeout" in error.lower() for error in errors)

    def test_validate_invalid_timeout_too_high(self):
        """Test validate catches timeout too high."""
        config = CombatConfiguration(combat_timeout_seconds=1801)
        errors = config.validate()
        assert len(errors) > 0

    def test_validate_invalid_xp_multiplier_too_low(self):
        """Test validate catches XP multiplier too low."""
        config = CombatConfiguration(combat_xp_multiplier=0.9)
        errors = config.validate()
        assert len(errors) > 0
        assert any("xp multiplier" in error.lower() for error in errors)

    def test_validate_invalid_xp_multiplier_too_high(self):
        """Test validate catches XP multiplier too high."""
        config = CombatConfiguration(combat_xp_multiplier=5.1)
        errors = config.validate()
        assert len(errors) > 0

    def test_validate_invalid_alert_threshold(self):
        """Test validate catches alert threshold out of range."""
        config = CombatConfiguration(combat_alert_threshold=0)
        errors = config.validate()
        assert len(errors) > 0

    def test_validate_invalid_max_participants(self):
        """Test validate catches max participants out of range."""
        config = CombatConfiguration(combat_max_participants=1)
        errors = config.validate()
        assert len(errors) > 0


class TestCombatConfigurationService:
    """Test suite for CombatConfigurationService class."""

    @pytest.fixture
    def mock_config(self):
        """Create a mock config object."""
        config = MagicMock()
        config.game.combat_enabled = True
        config.game.combat_tick_interval = 6
        config.game.combat_timeout_seconds = 180
        config.game.combat_xp_multiplier = 1.0
        config.game.combat_logging_enabled = True
        config.game.combat_monitoring_enabled = True
        config.game.combat_alert_threshold = 5
        config.game.combat_performance_threshold = 1000
        config.game.combat_error_threshold = 3
        return config

    @pytest.fixture
    def service(self, mock_config):
        """Create a CombatConfigurationService instance for testing."""
        with patch("server.services.combat_configuration_service.get_config", return_value=mock_config):
            with patch("server.services.combat_configuration_service.get_feature_flags"):
                return CombatConfigurationService()

    def test_init(self, service):
        """Test CombatConfigurationService initialization."""
        assert service._config is not None
        assert service._overrides == {}
        assert service._cached_config is None

    def test_get_combat_configuration(self, service):
        """Test get_combat_configuration returns configuration."""
        config = service.get_combat_configuration()
        assert isinstance(config, CombatConfiguration)
        assert config.combat_enabled is True
        assert config.combat_tick_interval == 6

    def test_get_combat_configuration_caching(self, service):
        """Test get_combat_configuration caches configuration."""
        config1 = service.get_combat_configuration()
        config2 = service.get_combat_configuration()
        assert config1 is config2  # Should be same cached instance

    def test_get_combat_configuration_for_scope_global(self, service):
        """Test get_combat_configuration_for_scope with global scope."""
        config = service.get_combat_configuration_for_scope(CombatConfigurationScope.GLOBAL)
        assert isinstance(config, CombatConfiguration)

    def test_get_combat_configuration_for_scope_room(self, service):
        """Test get_combat_configuration_for_scope with room scope."""
        config = service.get_combat_configuration_for_scope(CombatConfigurationScope.ROOM, "room_001")
        assert isinstance(config, CombatConfiguration)

    def test_get_combat_configuration_for_scope_player(self, service):
        """Test get_combat_configuration_for_scope with player scope."""
        config = service.get_combat_configuration_for_scope(CombatConfigurationScope.PLAYER, "player_001")
        assert isinstance(config, CombatConfiguration)

    def test_get_combat_configuration_for_scope_temporary(self, service):
        """Test get_combat_configuration_for_scope with temporary scope."""
        config = service.get_combat_configuration_for_scope(CombatConfigurationScope.TEMPORARY, "temp_001")
        assert isinstance(config, CombatConfiguration)

    def test_update_combat_configuration(self, service):
        """Test update_combat_configuration sets configuration override."""
        updates = {"combat_enabled": False, "combat_tick_interval": 10}
        result = service.update_combat_configuration(updates, CombatConfigurationScope.ROOM, "room_001")
        assert result.combat_enabled is False
        assert result.combat_tick_interval == 10
        assert "room:room_001" in service._overrides

    def test_update_combat_configuration_global_raises(self, service):
        """Test update_combat_configuration raises error for global scope."""
        updates = {"combat_enabled": False}
        with pytest.raises(CombatConfigurationError, match="Global configuration updates"):
            service.update_combat_configuration(updates, CombatConfigurationScope.GLOBAL)

    def test_update_combat_configuration_invalid_raises(self, service):
        """Test update_combat_configuration raises error for invalid config."""
        updates = {"combat_tick_interval": 0}  # Invalid
        with pytest.raises(CombatConfigurationError):
            service.update_combat_configuration(updates, CombatConfigurationScope.ROOM, "room_001")

    def test_clear_scope_override(self, service):
        """Test clear_scope_override removes configuration override."""
        updates = {"combat_enabled": False}
        service.update_combat_configuration(updates, CombatConfigurationScope.ROOM, "room_001")
        service.clear_scope_override(CombatConfigurationScope.ROOM, "room_001")
        assert "room:room_001" not in service._overrides

    def test_clear_scope_override_global_raises(self, service):
        """Test clear_scope_override raises error for global scope."""
        with pytest.raises(CombatConfigurationError, match="Cannot clear global"):
            service.clear_scope_override(CombatConfigurationScope.GLOBAL, None)

    def test_clear_all_overrides(self, service):
        """Test clear_all_overrides removes all overrides."""
        updates = {"combat_enabled": False}
        service.update_combat_configuration(updates, CombatConfigurationScope.ROOM, "room_001")
        service.update_combat_configuration(updates, CombatConfigurationScope.PLAYER, "player_001")
        service.clear_all_overrides()
        assert len(service._overrides) == 0

    def test_get_active_overrides(self, service):
        """Test get_active_overrides returns all active overrides."""
        updates = {"combat_enabled": False}
        service.update_combat_configuration(updates, CombatConfigurationScope.ROOM, "room_001")
        overrides = service.get_active_overrides()
        assert "room:room_001" in overrides
        assert overrides["room:room_001"]["combat_enabled"] is False

    def test_validate_configuration(self, service):
        """Test validate_configuration validates current configuration."""
        errors = service.validate_configuration()
        assert isinstance(errors, list)

    def test_validate_configuration_custom(self, service):
        """Test validate_configuration validates custom configuration."""
        custom_config = CombatConfiguration(combat_tick_interval=0)  # Invalid
        errors = service.validate_configuration(custom_config)
        assert len(errors) > 0

    def test_is_combat_available(self, service):
        """Test is_combat_available returns combat availability."""
        with patch.object(service._feature_flags, "is_combat_enabled", return_value=True):
            result = service.is_combat_available()
            assert isinstance(result, bool)

    def test_is_combat_available_with_override(self, service):
        """Test is_combat_available respects override."""
        with patch.object(service._feature_flags, "is_combat_enabled", return_value=True):
            updates = {"combat_enabled": False}
            service.update_combat_configuration(updates, CombatConfigurationScope.ROOM, "room_001")
            result = service.is_combat_available(room_id="room_001")
            assert result is False
