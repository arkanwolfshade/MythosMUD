"""
Tests for zone configuration system.

This module tests the zone configuration loading and management,
including effective spawn probability calculation and access requirements.

As documented in the Cultes des Goules, proper zone configuration is essential
for maintaining the delicate balance between the mundane and the eldritch forces
that lurk in the shadows of our world.
"""

from server.npc.population_control import ZoneConfiguration


class TestZoneConfiguration:
    """Test zone configuration loading and management."""

    def test_zone_configuration_creation(self):
        """Test creating a zone configuration from data."""
        config_data = {
            "environment": "outdoors",
            "description": "A test zone",
            "weather_patterns": ["clear", "overcast"],
            "special_rules": {
                "npc_spawn_modifier": 1.5,
                "lucidity_drain_rate": 0.1,
                "combat_modifier": 1.2,
                "exploration_bonus": 0.5,
                "access_requirements": ["stealth", "local_knowledge"],
            },
        }

        config = ZoneConfiguration(config_data)

        assert config.environment == "outdoors"
        assert config.description == "A test zone"
        assert config.weather_patterns == ["clear", "overcast"]
        assert config.npc_spawn_modifier == 1.5
        assert config.lucidity_drain_rate == 0.1
        assert config.combat_modifier == 1.2
        assert config.exploration_bonus == 0.5
        assert config.access_requirements == ["stealth", "local_knowledge"]

    def test_zone_configuration_defaults(self):
        """Test zone configuration with default values."""
        config_data = {}
        config = ZoneConfiguration(config_data)

        assert config.environment == "outdoors"
        assert config.description == ""
        assert config.weather_patterns == []
        assert config.npc_spawn_modifier == 1.0
        assert config.lucidity_drain_rate == 0.0
        assert config.combat_modifier == 1.0
        assert config.exploration_bonus == 0.0
        assert config.access_requirements == []

    def test_effective_spawn_probability_calculation(self):
        """Test effective spawn probability calculation with zone modifiers."""
        config_data = {"special_rules": {"npc_spawn_modifier": 1.5}}
        config = ZoneConfiguration(config_data)

        # Test normal probability
        assert config.get_effective_spawn_probability(0.5) == 0.75

        # Test probability that would exceed 1.0
        assert config.get_effective_spawn_probability(0.8) == 1.0

        # Test with modifier less than 1.0
        config_data["special_rules"]["npc_spawn_modifier"] = 0.5
        config = ZoneConfiguration(config_data)
        assert config.get_effective_spawn_probability(0.8) == 0.4

    def test_zone_access_requirements(self):
        """Test zone access requirement checking."""
        config_data = {"special_rules": {"access_requirements": ["stealth", "local_knowledge"]}}
        config = ZoneConfiguration(config_data)

        # Test with all requirements
        assert config.can_access(["stealth", "local_knowledge", "other"]) is True

        # Test with partial requirements
        assert config.can_access(["stealth"]) is True

        # Test with no requirements
        assert config.can_access(["other"]) is False

        # Test with no access requirements
        config_data["special_rules"] = {}
        config = ZoneConfiguration(config_data)
        assert config.can_access([]) is True
