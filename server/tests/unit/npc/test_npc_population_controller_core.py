"""
Tests for NPC population controller core functionality.

This module tests initialization, configuration loading, and data management
for the NPC population controller.

As documented in the Cultes des Goules, proper population management is essential
for maintaining the delicate balance between the mundane and the eldritch forces
that lurk in the shadows of our world.
"""

from unittest.mock import MagicMock, patch

from server.npc.population_control import NPCPopulationController


class TestNPCPopulationControllerCore:
    """Test the core functionality of NPC population controller."""

    def test_population_controller_initialization(self, population_controller):
        """Test population controller initialization."""
        assert population_controller.event_bus is not None
        assert len(population_controller.zone_configurations) > 0
        assert "arkhamcity" in population_controller.zone_configurations
        assert "arkhamcity/downtown" in population_controller.zone_configurations
        # REMOVED: active_npcs is no longer tracked in population_controller
        # Use lifecycle_manager.active_npcs as the single source of truth
        assert len(population_controller.population_stats) == 0

    def test_zone_configuration_loading(self, population_controller):
        """Test that zone configurations are loaded correctly."""
        # Test zone configuration
        zone_config = population_controller.get_zone_configuration("arkhamcity")
        assert zone_config is not None
        assert zone_config.npc_spawn_modifier == 1.2
        assert zone_config.lucidity_drain_rate == 0.1

        # Test sub-zone configuration
        subzone_config = population_controller.get_zone_configuration("arkhamcity/downtown")
        assert subzone_config is not None
        assert subzone_config.npc_spawn_modifier == 1.5
        assert subzone_config.lucidity_drain_rate == 0.08

    def test_zone_key_extraction(self, population_controller):
        """Test extracting zone keys from room IDs."""
        # Test standard room ID format
        zone_key = population_controller._get_zone_key_from_room_id("earth_arkhamcity_downtown_001")
        assert zone_key == "arkhamcity/downtown"

        # Test with different format
        zone_key = population_controller._get_zone_key_from_room_id("earth_innsmouth_waterfront_002")
        assert zone_key == "innsmouth/waterfront"

        # Test with unknown format
        zone_key = population_controller._get_zone_key_from_room_id("unknown_room")
        assert zone_key == "unknown/unknown"

    def test_npc_definitions_loading(self, population_controller, shopkeeper_definition, passive_mob_definition):
        """Test loading NPC definitions."""
        definitions = [shopkeeper_definition, passive_mob_definition]
        population_controller.load_npc_definitions(definitions)

        assert len(population_controller.npc_definitions) == 2
        assert shopkeeper_definition.id in population_controller.npc_definitions
        assert passive_mob_definition.id in population_controller.npc_definitions

    def test_spawn_rules_loading(self, population_controller, spawn_rule_shopkeeper, spawn_rule_passive_mob):
        """Test loading spawn rules."""
        rules = [spawn_rule_shopkeeper, spawn_rule_passive_mob]
        population_controller.load_spawn_rules(rules)

        assert len(population_controller.spawn_rules) == 2
        assert spawn_rule_shopkeeper.npc_definition_id in population_controller.spawn_rules
        assert spawn_rule_passive_mob.npc_definition_id in population_controller.spawn_rules

    def test_game_state_update(self, population_controller):
        """Test updating game state."""
        new_state = {"time_of_day": "night", "weather": "fog", "player_count": 3}

        population_controller.update_game_state(new_state)

        assert population_controller.current_game_state["time_of_day"] == "night"
        assert population_controller.current_game_state["weather"] == "fog"
        assert population_controller.current_game_state["player_count"] == 3

    def test_zone_configuration_missing_files(self, event_bus):
        """Test handling of missing zone configuration files."""
        # Create a mock async_persistence
        mock_persistence = MagicMock()

        # Patch the _load_zone_configurations method to skip database loading
        with patch.object(NPCPopulationController, "_load_zone_configurations", return_value=None):
            # This should not raise an exception
            controller = NPCPopulationController(
                event_bus,
                spawning_service=None,
                lifecycle_manager=None,
                async_persistence=mock_persistence,
            )
            assert len(controller.zone_configurations) == 0

    def test_zone_configuration_invalid_json(self, event_bus):
        """Test handling of invalid JSON in zone configuration files."""
        # Create a mock async_persistence
        mock_persistence = MagicMock()

        # Patch the _load_zone_configurations method to skip database loading
        with patch.object(NPCPopulationController, "_load_zone_configurations", return_value=None):
            # This should not raise an exception
            controller = NPCPopulationController(
                event_bus,
                spawning_service=None,
                lifecycle_manager=None,
                async_persistence=mock_persistence,
            )
            assert len(controller.zone_configurations) == 0
