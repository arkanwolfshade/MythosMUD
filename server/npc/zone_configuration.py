"""
Zone Configuration Module.

This module provides the ZoneConfiguration class for managing zone and sub-zone
configuration data, including spawn modifiers and access requirements.
"""

from typing import Any


class ZoneConfiguration:
    """Represents the configuration for a zone or sub-zone."""

    def __init__(self, config_data: dict[str, Any]):
        """
        Initialize zone configuration.

        Args:
            config_data: Dictionary containing zone configuration data
        """
        self.zone_type = config_data.get("zone_type")  # Only populated for zone-level configs
        self.environment = config_data.get("environment", "outdoors")
        self.description = config_data.get("description", "")
        self.weather_patterns = config_data.get("weather_patterns", [])
        self.special_rules = config_data.get("special_rules", {})

        # Extract NPC-related modifiers
        self.npc_spawn_modifier = self.special_rules.get("npc_spawn_modifier", 1.0)
        self.lucidity_drain_rate = self.special_rules.get("lucidity_drain_rate", 0.0)
        self.combat_modifier = self.special_rules.get("combat_modifier", 1.0)
        self.exploration_bonus = self.special_rules.get("exploration_bonus", 0.0)
        self.access_requirements = self.special_rules.get("access_requirements", [])

    def get_effective_spawn_probability(self, base_probability: float) -> float:
        """
        Calculate effective spawn probability based on zone modifiers.

        Args:
            base_probability: Base spawn probability from NPC definition

        Returns:
            Effective spawn probability adjusted for zone modifiers
        """
        return min(1.0, base_probability * self.npc_spawn_modifier)

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
