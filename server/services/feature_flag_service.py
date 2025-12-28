"""
Feature flag service for MythosMUD.

This service provides centralized feature flag management for enabling/disabling
game features without requiring code deployments. Combat system integration
allows for safe rollout and quick rollback of combat features.

As noted in the restricted archives: "The ancient ones grant us the power
to shape reality itself through the manipulation of cosmic forces."
"""

from typing import Any

from server.config import get_config
from server.structured_logging.enhanced_logging_config import get_logger

logger = get_logger(__name__)


class FeatureFlagService:
    """
    Centralized feature flag service for MythosMUD.

    Provides type-safe access to feature flags with caching and
    validation. Supports runtime configuration changes and
    environment-specific overrides.
    """

    def __init__(self):
        """Initialize the feature flag service."""
        self._config = get_config()
        self._cached_combat_enabled: bool | None = None
        self._cached_combat_logging_enabled: bool | None = None
        self._cached_combat_monitoring_enabled: bool | None = None
        logger.debug("Feature flag service initialized")

    def is_combat_enabled(self) -> bool:
        """
        Check if combat system is enabled.

        Returns:
            bool: True if combat is enabled, False otherwise

        Example:
            if feature_flags.is_combat_enabled():
                # Execute combat logic
                pass
        """
        if self._cached_combat_enabled is None:
            self._cached_combat_enabled = self._config.game.combat_enabled
            logger.debug("Combat feature flag cached", combat_enabled=self._cached_combat_enabled)
        return self._cached_combat_enabled

    def is_combat_logging_enabled(self) -> bool:
        """
        Check if combat logging is enabled.

        Returns:
            bool: True if combat logging is enabled, False otherwise
        """
        if self._cached_combat_logging_enabled is None:
            self._cached_combat_logging_enabled = self._config.game.combat_logging_enabled
            logger.debug(
                "Combat logging feature flag cached", combat_logging_enabled=self._cached_combat_logging_enabled
            )
        return self._cached_combat_logging_enabled

    def is_combat_monitoring_enabled(self) -> bool:
        """
        Check if combat monitoring is enabled.

        Returns:
            bool: True if combat monitoring is enabled, False otherwise
        """
        if self._cached_combat_monitoring_enabled is None:
            self._cached_combat_monitoring_enabled = self._config.game.combat_monitoring_enabled
            logger.debug(
                "Combat monitoring feature flag cached",
                combat_monitoring_enabled=self._cached_combat_monitoring_enabled,
            )
        return self._cached_combat_monitoring_enabled

    def get_combat_configuration(self) -> dict[str, Any]:
        """
        Get all combat-related configuration settings.

        Returns:
            Dict[str, Any]: Dictionary containing all combat configuration

        Example:
            combat_config = feature_flags.get_combat_configuration()
            tick_interval = combat_config['combat_tick_interval']
        """
        config = {
            "combat_enabled": self.is_combat_enabled(),
            "combat_tick_interval": self._config.game.combat_tick_interval,
            "combat_timeout_seconds": self._config.game.combat_timeout_seconds,
            "combat_xp_multiplier": self._config.game.combat_xp_multiplier,
            "combat_logging_enabled": self.is_combat_logging_enabled(),
            "combat_monitoring_enabled": self.is_combat_monitoring_enabled(),
            "combat_alert_threshold": self._config.game.combat_alert_threshold,
            "combat_performance_threshold": self._config.game.combat_performance_threshold,
            "combat_error_threshold": self._config.game.combat_error_threshold,
        }

        logger.debug("Combat configuration retrieved", config=config)
        return config

    def clear_cache(self) -> None:
        """
        Clear the feature flag cache.

        This should be called when configuration changes are made
        to ensure fresh values are retrieved.
        """
        self._cached_combat_enabled = None
        self._cached_combat_logging_enabled = None
        self._cached_combat_monitoring_enabled = None
        logger.debug("Feature flag cache cleared")

    def validate_combat_requirements(self) -> bool:
        """
        Validate that all combat requirements are met.

        Returns:
            bool: True if combat can be safely enabled, False otherwise

        Raises:
            RuntimeError: If combat is enabled but requirements are not met
        """
        if not self.is_combat_enabled():
            logger.debug("Combat disabled, skipping validation")
            return True

        # Check that required configuration is present
        config = self.get_combat_configuration()

        if config["combat_tick_interval"] < 1:
            logger.error("Combat tick interval must be at least 1 second")
            return False

        if config["combat_timeout_seconds"] < 60:
            logger.error("Combat timeout must be at least 60 seconds")
            return False

        if config["combat_xp_multiplier"] < 1.0:
            logger.error("Combat XP multiplier must be at least 1.0")
            return False

        logger.debug("Combat requirements validation passed")
        return True

    def get_feature_status(self) -> dict[str, dict[str, Any]]:
        """
        Get status of all feature flags.

        Returns:
            Dict[str, Dict[str, Any]]: Status of all features

        Example:
            status = feature_flags.get_feature_status()
            logger.info("Feature status check", combat_enabled=status['combat']['enabled'])
        """
        status = {
            "combat": {
                "enabled": self.is_combat_enabled(),
                "logging_enabled": self.is_combat_logging_enabled(),
                "monitoring_enabled": self.is_combat_monitoring_enabled(),
                "configuration": self.get_combat_configuration(),
            }
        }

        logger.debug("Feature status retrieved", status=status)
        return status

    def check_combat_availability(self, player_id: str | None = None) -> bool:
        """
        Check if combat is available for a specific player or globally.

        Args:
            player_id: Optional player ID to check specific availability

        Returns:
            bool: True if combat is available, False otherwise
        """
        if not self.is_combat_enabled():
            logger.debug("Combat not available: feature disabled")
            return False

        if not self.validate_combat_requirements():
            logger.warning("Combat not available: requirements not met")
            return False

        # Future: Could add player-specific checks here
        # e.g., player level requirements, subscription status, etc.
        if player_id:
            logger.debug("Combat available for player", player_id=player_id)
        else:
            logger.debug("Combat available globally")

        return True


# Global feature flag service instance
feature_flags = FeatureFlagService()


def get_feature_flags() -> FeatureFlagService:
    """
    Get the global feature flag service instance.

    Returns:
        FeatureFlagService: The global feature flag service

    Example:
        flags = get_feature_flags()
        if flags.is_combat_enabled():
            # Execute combat logic
            pass
    """
    return feature_flags


def refresh_feature_flags() -> None:
    """
    Refresh feature flags by clearing cache and reloading configuration.

    This should be called when configuration changes are made
    to ensure fresh values are retrieved.
    """
    global feature_flags
    feature_flags.clear_cache()
    logger.info("Feature flags refreshed")


def is_combat_enabled() -> bool:
    """
    Convenience function to check if combat is enabled.

    Returns:
        bool: True if combat is enabled, False otherwise

    Example:
        if is_combat_enabled():
            # Execute combat logic
            pass
    """
    return feature_flags.is_combat_enabled()


def is_combat_logging_enabled() -> bool:
    """
    Convenience function to check if combat logging is enabled.

    Returns:
        bool: True if combat logging is enabled, False otherwise
    """
    return feature_flags.is_combat_logging_enabled()


def is_combat_monitoring_enabled() -> bool:
    """
    Convenience function to check if combat monitoring is enabled.

    Returns:
        bool: True if combat monitoring is enabled, False otherwise
    """
    return feature_flags.is_combat_monitoring_enabled()
