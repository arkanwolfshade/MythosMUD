"""
Zone Configuration Module.

This module provides the ZoneConfiguration class for managing zone and sub-zone
configuration data, including spawn modifiers and access requirements.
"""

from typing import TypedDict


class ZoneSpecialRules(TypedDict, total=False):
    """NPC-related modifiers and access rules stored in zone special_rules JSON."""

    npc_spawn_modifier: float
    lucidity_drain_rate: float
    combat_modifier: float
    exploration_bonus: float
    access_requirements: list[str]


class ZoneConfigurationData(TypedDict, total=False):
    """Raw zone or sub-zone configuration payload from the database or tests."""

    zone_type: str
    environment: str
    description: str
    weather_patterns: list[str]
    special_rules: ZoneSpecialRules


class ZoneConfiguration:  # pylint: disable=too-many-instance-attributes  # Reason: Zone configuration requires many fields to capture complete zone configuration
    """Represents the configuration for a zone or sub-zone."""

    def __init__(self, config_data: ZoneConfigurationData) -> None:
        """
        Initialize zone configuration.

        Args:
            config_data: Dictionary containing zone configuration data
        """
        self.zone_type: str | None = config_data.get("zone_type")  # Only populated for zone-level configs
        self.environment: str = config_data.get("environment", "outdoors")
        self.description: str = config_data.get("description", "")
        self.weather_patterns: list[str] = config_data.get("weather_patterns", [])
        special_rules: ZoneSpecialRules = config_data.get("special_rules", {})
        self.special_rules: ZoneSpecialRules = special_rules

        # Extract NPC-related modifiers
        self.npc_spawn_modifier: float = special_rules.get("npc_spawn_modifier", 1.0)
        self.lucidity_drain_rate: float = special_rules.get("lucidity_drain_rate", 0.0)
        self.combat_modifier: float = special_rules.get("combat_modifier", 1.0)
        self.exploration_bonus: float = special_rules.get("exploration_bonus", 0.0)
        self.access_requirements: list[str] = special_rules.get("access_requirements", [])

    def get_effective_spawn_probability(self, base_probability: float) -> float:
        """
        Calculate effective spawn probability based on zone modifiers.

        Args:
            base_probability: Base spawn probability from NPC definition

        Returns:
            Effective spawn probability adjusted for zone modifiers
        """
        result: float = min(1.0, base_probability * self.npc_spawn_modifier)
        return result

    def can_access(self, player_requirements: list[str]) -> bool:
        """
        Check if a player can access this zone based on requirements.

        Args:
            player_requirements: List of player capabilities/items

        Returns:
            True if player can access the zone, False otherwise
        """
        if not self.access_requirements:
            return True

        return any(req in player_requirements for req in self.access_requirements)
