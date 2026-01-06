"""
Combat configuration management service for MythosMUD.

This service provides centralized management of combat configuration settings,
including runtime updates, validation, and integration with the feature flag system.

As noted in the restricted archives: "The configuration of cosmic forces
determines the very fabric of reality within our domain."
"""

from dataclasses import asdict, dataclass
from enum import Enum
from typing import Any

from server.config import get_config
from server.services.feature_flag_service import get_feature_flags
from server.structured_logging.enhanced_logging_config import get_logger

logger = get_logger(__name__)


class CombatConfigurationError(Exception):
    """Exception raised for combat configuration errors."""


class CombatConfigurationScope(Enum):
    """Scope for combat configuration changes."""

    GLOBAL = "global"
    ROOM = "room"
    PLAYER = "player"
    TEMPORARY = "temporary"


@dataclass
class CombatConfiguration:
    """Combat configuration data class."""

    # Core combat settings
    combat_enabled: bool = True
    combat_tick_interval: int = 6
    combat_timeout_seconds: int = 180
    combat_xp_multiplier: float = 1.0

    # Logging and monitoring
    combat_logging_enabled: bool = True
    combat_monitoring_enabled: bool = True
    combat_alert_threshold: int = 5
    combat_performance_threshold: int = 1000
    combat_error_threshold: int = 3

    # Advanced settings
    combat_max_participants: int = 10
    combat_auto_cleanup_interval: int = 300
    combat_event_retention_hours: int = 24

    def to_dict(self) -> dict[str, Any]:
        """Convert to dictionary."""
        return asdict(self)

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "CombatConfiguration":
        """Create from dictionary."""
        return cls(**data)

    def validate(self) -> list[str]:
        """Validate configuration and return list of errors."""
        errors = []

        if self.combat_tick_interval < 1 or self.combat_tick_interval > 60:
            errors.append("Combat tick interval must be between 1 and 60 seconds")

        if self.combat_timeout_seconds < 60 or self.combat_timeout_seconds > 1800:
            errors.append("Combat timeout must be between 60 and 1800 seconds")

        if self.combat_xp_multiplier < 1.0 or self.combat_xp_multiplier > 5.0:
            errors.append("XP multiplier must be between 1.0 and 5.0")

        if self.combat_alert_threshold < 1 or self.combat_alert_threshold > 100:
            errors.append("Alert threshold must be between 1 and 100")

        if self.combat_performance_threshold < 100 or self.combat_performance_threshold > 5000:
            errors.append("Performance threshold must be between 100 and 5000 milliseconds")

        if self.combat_error_threshold < 1 or self.combat_error_threshold > 50:
            errors.append("Error threshold must be between 1 and 50")

        if self.combat_max_participants < 2 or self.combat_max_participants > 50:
            errors.append("Max participants must be between 2 and 50")

        if self.combat_auto_cleanup_interval < 60 or self.combat_auto_cleanup_interval > 3600:
            errors.append("Auto cleanup interval must be between 60 and 3600 seconds")

        if self.combat_event_retention_hours < 1 or self.combat_event_retention_hours > 168:
            errors.append("Event retention must be between 1 and 168 hours")

        return errors


class CombatConfigurationService:
    """
    Centralized combat configuration management service.

    Provides type-safe access to combat configuration with caching,
    validation, and runtime update capabilities.
    """

    def __init__(self) -> None:
        """Initialize the combat configuration service."""
        self._config = get_config()
        self._feature_flags = get_feature_flags()
        self._overrides: dict[str, CombatConfiguration] = {}
        self._cached_config: CombatConfiguration | None = None
        logger.debug("Combat configuration service initialized")

    def get_combat_configuration(self) -> CombatConfiguration:
        """
        Get current combat configuration.

        Returns:
            CombatConfiguration: Current combat configuration

        Example:
            config = combat_config.get_combat_configuration()
            if config.combat_enabled:
                # Execute combat logic
                pass
        """
        if self._cached_config is None:
            self._cached_config = CombatConfiguration(
                combat_enabled=self._config.game.combat_enabled,
                combat_tick_interval=self._config.game.combat_tick_interval,
                # pylint: disable=no-member  # Pydantic FieldInfo dynamic attributes
                combat_timeout_seconds=self._config.game.combat_timeout_seconds,
                combat_xp_multiplier=self._config.game.combat_xp_multiplier,
                combat_logging_enabled=self._config.game.combat_logging_enabled,
                combat_monitoring_enabled=self._config.game.combat_monitoring_enabled,
                combat_alert_threshold=self._config.game.combat_alert_threshold,
                combat_performance_threshold=self._config.game.combat_performance_threshold,
                combat_error_threshold=self._config.game.combat_error_threshold,
            )
            logger.debug("Combat configuration cached", config=self._cached_config.to_dict())
        return self._cached_config

    def get_combat_configuration_for_scope(
        self, scope: CombatConfigurationScope, scope_id: str | None = None
    ) -> CombatConfiguration:
        """
        Get combat configuration for a specific scope.

        Args:
            scope: Configuration scope
            scope_id: Optional scope identifier

        Returns:
            CombatConfiguration: Configuration for the specified scope
        """
        base_config = self.get_combat_configuration()

        # Check for scope-specific overrides
        if scope == CombatConfigurationScope.ROOM and scope_id:
            override_key = f"room:{scope_id}"
            if override_key in self._overrides:
                return self._overrides[override_key]
        elif scope == CombatConfigurationScope.PLAYER and scope_id:
            override_key = f"player:{scope_id}"
            if override_key in self._overrides:
                return self._overrides[override_key]
        elif scope == CombatConfigurationScope.TEMPORARY and scope_id:
            override_key = f"temp:{scope_id}"
            if override_key in self._overrides:
                return self._overrides[override_key]

        return base_config

    def update_combat_configuration(
        self,
        updates: dict[str, Any],
        scope: CombatConfigurationScope = CombatConfigurationScope.GLOBAL,
        scope_id: str | None = None,
    ) -> CombatConfiguration:
        """
        Update combat configuration.

        Args:
            updates: Dictionary of configuration updates
            scope: Configuration scope
            scope_id: Optional scope identifier

        Returns:
            CombatConfiguration: Updated configuration

        Raises:
            CombatConfigurationError: If configuration is invalid
        """
        if scope == CombatConfigurationScope.GLOBAL:
            # For global updates, we need to update the actual configuration
            # This would typically require a configuration reload
            raise CombatConfigurationError("Global configuration updates require server restart")

        # Get current configuration for scope
        current_config = self.get_combat_configuration_for_scope(scope, scope_id)

        # Create updated configuration
        updated_dict = current_config.to_dict()
        updated_dict.update(updates)

        updated_config = CombatConfiguration.from_dict(updated_dict)

        # Validate updated configuration
        errors = updated_config.validate()
        if errors:
            raise CombatConfigurationError(f"Invalid configuration: {', '.join(errors)}")

        # Store override
        if scope == CombatConfigurationScope.ROOM and scope_id:
            override_key = f"room:{scope_id}"
            self._overrides[override_key] = updated_config
        elif scope == CombatConfigurationScope.PLAYER and scope_id:
            override_key = f"player:{scope_id}"
            self._overrides[override_key] = updated_config
        elif scope == CombatConfigurationScope.TEMPORARY and scope_id:
            override_key = f"temp:{scope_id}"
            self._overrides[override_key] = updated_config

        logger.info("Combat configuration updated", scope=scope.value, scope_id=scope_id, updates=updates)
        return updated_config

    def clear_scope_override(self, scope: CombatConfigurationScope, scope_id: str) -> None:
        """
        Clear configuration override for a specific scope.

        Args:
            scope: Configuration scope
            scope_id: Scope identifier
        """
        if scope == CombatConfigurationScope.ROOM:
            override_key = f"room:{scope_id}"
        elif scope == CombatConfigurationScope.PLAYER:
            override_key = f"player:{scope_id}"
        elif scope == CombatConfigurationScope.TEMPORARY:
            override_key = f"temp:{scope_id}"
        else:
            raise CombatConfigurationError("Cannot clear global configuration")

        if override_key in self._overrides:
            del self._overrides[override_key]
            logger.info("Configuration override cleared", scope=scope.value, scope_id=scope_id)

    def clear_all_overrides(self) -> None:
        """Clear all configuration overrides."""
        self._overrides.clear()
        logger.info("All configuration overrides cleared")

    def get_active_overrides(self) -> dict[str, dict[str, Any]]:
        """
        Get all active configuration overrides.

        Returns:
            Dict[str, Dict[str, Any]]: Active overrides
        """
        return {key: config.to_dict() for key, config in self._overrides.items()}

    def validate_configuration(self, config: CombatConfiguration | None = None) -> list[str]:
        """
        Validate combat configuration.

        Args:
            config: Optional configuration to validate (uses current if None)

        Returns:
            List[str]: List of validation errors
        """
        if config is None:
            config = self.get_combat_configuration()

        return config.validate()

    def is_combat_available(self, player_id: str | None = None, room_id: str | None = None) -> bool:
        """
        Check if combat is available for a specific player/room.

        Args:
            player_id: Optional player ID
            room_id: Optional room ID

        Returns:
            bool: True if combat is available, False otherwise
        """
        # Check feature flag first
        if not self._feature_flags.is_combat_enabled():
            return False

        # Get configuration for the specific scope
        if room_id:
            config = self.get_combat_configuration_for_scope(CombatConfigurationScope.ROOM, room_id)
        elif player_id:
            config = self.get_combat_configuration_for_scope(CombatConfigurationScope.PLAYER, player_id)
        else:
            config = self.get_combat_configuration()

        # Check if combat is enabled for this scope
        if not config.combat_enabled:
            return False

        # Validate configuration
        errors = self.validate_configuration(config)
        if errors:
            logger.warning("Combat not available due to configuration errors", errors=errors)
            return False

        return True

    def get_combat_settings_summary(self) -> dict[str, Any]:
        """
        Get summary of combat settings for monitoring.

        Returns:
            Dict[str, Any]: Combat settings summary
        """
        base_config = self.get_combat_configuration()

        summary = {
            "base_configuration": base_config.to_dict(),
            "active_overrides": self.get_active_overrides(),
            "feature_flags": {
                "combat_enabled": self._feature_flags.is_combat_enabled(),
                "combat_logging_enabled": self._feature_flags.is_combat_logging_enabled(),
                "combat_monitoring_enabled": self._feature_flags.is_combat_monitoring_enabled(),
            },
            "validation_errors": self.validate_configuration(),
        }

        return summary

    def refresh_configuration(self) -> None:
        """Refresh configuration from source."""
        self._config = get_config()
        self._feature_flags.clear_cache()
        self._cached_config = None
        logger.info("Combat configuration refreshed")

    def clear_cache(self) -> None:
        """Clear configuration cache."""
        self._cached_config = None
        logger.debug("Combat configuration cache cleared")


# Global combat configuration service instance
combat_config = CombatConfigurationService()


def get_combat_config() -> CombatConfigurationService:
    """
    Get the global combat configuration service instance.

    Returns:
        CombatConfigurationService: The global combat configuration service
    """
    return combat_config


def refresh_combat_configuration() -> None:
    """
    Refresh combat configuration by clearing cache and reloading.
    """
    combat_config.refresh_configuration()


def get_combat_configuration() -> CombatConfiguration:
    """
    Convenience function to get current combat configuration.

    Returns:
        CombatConfiguration: Current combat configuration
    """
    return combat_config.get_combat_configuration()


def is_combat_available(player_id: str | None = None, room_id: str | None = None) -> bool:
    """
    Convenience function to check if combat is available.

    Args:
        player_id: Optional player ID
        room_id: Optional room ID

    Returns:
        bool: True if combat is available, False otherwise
    """
    return combat_config.is_combat_available(player_id, room_id)
