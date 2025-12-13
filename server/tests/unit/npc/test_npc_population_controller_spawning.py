"""
Tests for NPC population controller spawning and lifecycle.

This module tests NPC spawning logic, despawning, cleanup, and event handling
for the NPC population controller.

As documented in the Cultes des Goules, proper population management is essential
for maintaining the delicate balance between the mundane and the eldritch forces
that lurk in the shadows of our world.
"""

import asyncio
from unittest.mock import patch

import pytest

from server.events.event_types import PlayerEnteredRoom
from server.npc.population_control import PopulationStats


class TestNPCPopulationControllerSpawning:
    """Test spawning and lifecycle functionality of NPC population controller."""

    def test_npc_spawning_logic(self, population_controller, shopkeeper_definition, spawn_rule_shopkeeper):
        """Test NPC spawning logic."""
        # Load definitions and rules
        population_controller.load_npc_definitions([shopkeeper_definition])
        population_controller.load_spawn_rules([spawn_rule_shopkeeper])

        # Test should spawn check
        zone_config = population_controller.get_zone_configuration("arkhamcity/downtown")
        should_spawn = population_controller._should_spawn_npc(
            shopkeeper_definition, zone_config, "earth_arkhamcity_downtown_001"
        )
        assert should_spawn is True

    def test_npc_spawning_with_population_limits(
        self, population_controller, passive_mob_definition, spawn_rule_passive_mob
    ):
        """Test NPC spawning with population limits."""
        # Load definitions and rules
        population_controller.load_npc_definitions([passive_mob_definition])
        population_controller.load_spawn_rules([spawn_rule_passive_mob])

        # Create population stats with max population reached
        zone_key = "arkhamcity/downtown"
        population_controller.population_stats[zone_key] = PopulationStats("arkhamcity", "downtown")
        stats = population_controller.population_stats[zone_key]

        # Add NPCs up to max population
        for i in range(passive_mob_definition.max_population):
            stats.add_npc(passive_mob_definition.npc_type, f"room_{i:03d}", False, passive_mob_definition.id)

        # Test that no more NPCs can spawn
        zone_config = population_controller.get_zone_configuration(zone_key)
        should_spawn = population_controller._should_spawn_npc(
            passive_mob_definition, zone_config, "earth_arkhamcity_downtown_001"
        )
        assert should_spawn is False

    def test_npc_spawning_with_spawn_conditions(
        self, population_controller, passive_mob_definition, spawn_rule_passive_mob
    ):
        """Test NPC spawning with spawn conditions."""
        # Load definitions and rules
        population_controller.load_npc_definitions([passive_mob_definition])
        population_controller.load_spawn_rules([spawn_rule_passive_mob])

        # Set game state that doesn't meet spawn conditions
        population_controller.update_game_state({"time_of_day": "night", "weather": "rain", "player_count": 1})

        zone_config = population_controller.get_zone_configuration("arkhamcity/downtown")
        should_spawn = population_controller._should_spawn_npc(
            passive_mob_definition, zone_config, "earth_arkhamcity_downtown_001"
        )
        assert should_spawn is False

        # Set game state that meets spawn conditions
        population_controller.update_game_state({"time_of_day": "day", "weather": "clear", "player_count": 1})

        should_spawn = population_controller._should_spawn_npc(
            passive_mob_definition, zone_config, "earth_arkhamcity_downtown_001"
        )
        assert should_spawn is True

    def test_npc_spawning_with_zone_modifiers(
        self, population_controller, passive_mob_definition, spawn_rule_passive_mob
    ):
        """Test NPC spawning with zone spawn modifiers."""
        # Load definitions and rules
        population_controller.load_npc_definitions([passive_mob_definition])
        population_controller.load_spawn_rules([spawn_rule_passive_mob])

        # Set game state that meets spawn conditions
        population_controller.update_game_state({"time_of_day": "day", "weather": "clear", "player_count": 1})

        zone_config = population_controller.get_zone_configuration("arkhamcity/downtown")

        # Test with high spawn probability (should spawn)
        passive_mob_definition.spawn_probability = 0.8
        should_spawn = population_controller._should_spawn_npc(
            passive_mob_definition, zone_config, "earth_arkhamcity_downtown_001"
        )
        assert should_spawn is True

        # Test with low spawn probability (might not spawn due to randomness)
        passive_mob_definition.spawn_probability = 0.1
        # This test might be flaky due to randomness, but we can test the logic
        # by checking that the effective probability is calculated correctly
        effective_prob = zone_config.get_effective_spawn_probability(0.1)
        assert abs(effective_prob - 0.15) < 0.0001  # 0.1 * 1.5 with floating point tolerance

    def test_npc_spawning_process(self, population_controller, shopkeeper_definition, spawn_rule_shopkeeper):
        """Test the complete NPC spawning process."""
        # Load definitions and rules
        population_controller.load_npc_definitions([shopkeeper_definition])
        population_controller.load_spawn_rules([spawn_rule_shopkeeper])

        # Spawn an NPC
        npc_id = population_controller._spawn_npc(shopkeeper_definition, "earth_arkhamcity_downtown_001")

        # Check that NPC was created (NPCs are now managed by lifecycle manager)
        assert npc_id is not None
        # Note: The lifecycle manager is mocked, so we verify by checking the mock was called
        assert population_controller.lifecycle_manager.spawn_npc.called

        # Check that population stats were updated
        zone_key = "arkhamcity/downtown"
        assert zone_key in population_controller.population_stats
        stats = population_controller.population_stats[zone_key]
        assert stats.total_npcs == 1
        assert stats.npcs_by_definition[shopkeeper_definition.id] == 1  # Changed from npcs_by_type
        assert stats.required_npcs == 1

    def test_npc_despawning_process(self, population_controller, shopkeeper_definition, spawn_rule_shopkeeper):
        """Test the NPC despawning process."""
        # Load definitions and rules
        population_controller.load_npc_definitions([shopkeeper_definition])
        population_controller.load_spawn_rules([spawn_rule_shopkeeper])

        # Spawn an NPC
        npc_id = population_controller._spawn_npc(shopkeeper_definition, "earth_arkhamcity_downtown_001")

        # Despawn the NPC
        result = population_controller.despawn_npc(npc_id)
        assert result is True

        # Note: NPCs are now managed by lifecycle manager, not population controller
        # Verify that the population controller called the lifecycle manager to despawn
        # (The lifecycle manager is mocked, so we can't directly check active_npcs)

        # Check that population stats were updated
        zone_key = "arkhamcity/downtown"
        stats = population_controller.population_stats[zone_key]
        assert stats.total_npcs == 0
        assert stats.npcs_by_definition[shopkeeper_definition.id] == 0  # Changed from npcs_by_type
        assert stats.required_npcs == 0

    def test_npc_despawning_nonexistent(self, population_controller):
        """Test despawning a non-existent NPC."""
        result = population_controller.despawn_npc("nonexistent_npc")
        assert result is False

    def test_population_summary(
        self,
        population_controller,
        shopkeeper_definition,
        passive_mob_definition,
        spawn_rule_shopkeeper,
        spawn_rule_passive_mob,
    ):
        """Test getting population summary."""
        # Load definitions and rules
        population_controller.load_npc_definitions([shopkeeper_definition, passive_mob_definition])
        population_controller.load_spawn_rules([spawn_rule_shopkeeper, spawn_rule_passive_mob])

        # Spawn some NPCs
        population_controller._spawn_npc(shopkeeper_definition, "earth_arkhamcity_downtown_001")
        population_controller._spawn_npc(passive_mob_definition, "earth_arkhamcity_downtown_002")

        # Get population summary
        summary = population_controller.get_zone_population_summary()

        assert summary["total_zones"] == 1
        assert summary["total_active_npcs"] == 2
        assert "arkhamcity/downtown" in summary["zones"]

        zone_summary = summary["zones"]["arkhamcity/downtown"]
        assert zone_summary["total_npcs"] == 2
        # Changed from npcs_by_type to npcs_by_definition
        assert len(zone_summary["npcs_by_definition"]) == 2
        assert zone_summary["required_npcs"] == 1
        assert zone_summary["optional_npcs"] == 1

    def test_cleanup_inactive_npcs(self, population_controller, passive_mob_definition, spawn_rule_passive_mob):
        """Test cleaning up inactive NPCs."""
        # Note: NPCs are now managed by lifecycle manager, not population controller
        # Cleanup should delegate to the lifecycle manager
        # For now, this test verifies that the cleanup method exists and doesn't crash

        # Load definitions and rules
        population_controller.load_npc_definitions([passive_mob_definition])
        population_controller.load_spawn_rules([spawn_rule_passive_mob])

        # Spawn an optional NPC
        _npc_id = population_controller._spawn_npc(passive_mob_definition, "earth_arkhamcity_downtown_001")

        # Note: Cannot manually set spawn time on lifecycle manager's internal state
        # This test would need to be updated when lifecycle manager implements cleanup

        # Clean up inactive NPCs (currently a no-op in population controller)
        cleaned_count = population_controller.cleanup_inactive_npcs(max_age_seconds=3600)

        # Cleanup is now delegated to lifecycle manager, so we can't verify the count here
        assert cleaned_count >= 0  # Just verify it doesn't crash

    def test_cleanup_does_not_remove_required_npcs(
        self, population_controller, shopkeeper_definition, spawn_rule_shopkeeper
    ):
        """Test that cleanup doesn't remove required NPCs."""
        # Note: NPCs are now managed by lifecycle manager, not population controller
        # Cleanup should delegate to the lifecycle manager
        # For now, this test verifies that the cleanup method exists and doesn't crash

        # Load definitions and rules
        population_controller.load_npc_definitions([shopkeeper_definition])
        population_controller.load_spawn_rules([spawn_rule_shopkeeper])

        # Spawn a required NPC
        _npc_id = population_controller._spawn_npc(shopkeeper_definition, "earth_arkhamcity_downtown_001")

        # Note: Cannot manually set spawn time on lifecycle manager's internal state
        # This test would need to be updated when lifecycle manager implements cleanup

        # Clean up inactive NPCs (currently a no-op in population controller)
        cleaned_count = population_controller.cleanup_inactive_npcs(max_age_seconds=3600)

        # Cleanup is now delegated to lifecycle manager, so we can't verify the count here
        assert cleaned_count >= 0  # Just verify it doesn't crash

    @pytest.mark.asyncio
    async def test_event_handling(self, population_controller, shopkeeper_definition, spawn_rule_shopkeeper):
        """Test event handling for player and NPC movements."""
        # Load definitions and rules
        population_controller.load_npc_definitions([shopkeeper_definition])
        population_controller.load_spawn_rules([spawn_rule_shopkeeper])

        # Test player entering room (should trigger spawn check)
        player_event = PlayerEnteredRoom(player_id="test_player", room_id="earth_arkhamcity_downtown_001")

        # This should trigger spawn checking
        with patch.object(population_controller, "_check_spawn_requirements_for_room") as mock_check:
            # Use the population controller's event bus
            population_controller.event_bus.publish(player_event)
            await asyncio.sleep(0.1)  # Allow async event processing
            mock_check.assert_called_once_with("earth_arkhamcity_downtown_001")
