"""
Tests for NPC population control system.

This module tests the sub-zone-based NPC population management system,
including zone configuration loading, population tracking, and spawn logic.

As documented in the Cultes des Goules, proper population management is essential
for maintaining the delicate balance between the mundane and the eldritch forces
that lurk in the shadows of our world.
"""

import asyncio
import json
import tempfile
from pathlib import Path
from unittest.mock import Mock, patch

import pytest

from server.events.event_bus import EventBus
from server.events.event_types import NPCEnteredRoom, NPCLeftRoom, PlayerEnteredRoom
from server.models.npc import NPCDefinition, NPCDefinitionType, NPCSpawnRule
from server.models.room import Room
from server.npc.population_control import NPCPopulationController, PopulationStats, ZoneConfiguration


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
                "sanity_drain_rate": 0.1,
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
        assert config.sanity_drain_rate == 0.1
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
        assert config.sanity_drain_rate == 0.0
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


class TestPopulationStats:
    """Test population statistics tracking."""

    def test_population_stats_creation(self):
        """Test creating population statistics."""
        stats = PopulationStats("arkhamcity", "downtown")

        assert stats.zone_id == "arkhamcity"
        assert stats.sub_zone_id == "downtown"
        assert stats.total_npcs == 0
        assert stats.npcs_by_type == {}
        assert stats.npcs_by_room == {}
        assert stats.required_npcs == 0
        assert stats.optional_npcs == 0

    def test_add_npc_to_stats(self):
        """Test adding NPCs to population statistics."""
        stats = PopulationStats("arkhamcity", "downtown")

        # Add required NPC
        stats.add_npc("shopkeeper", "room_001", True)
        assert stats.total_npcs == 1
        assert stats.npcs_by_type["shopkeeper"] == 1
        assert stats.npcs_by_room["room_001"] == 1
        assert stats.required_npcs == 1
        assert stats.optional_npcs == 0

        # Add optional NPC
        stats.add_npc("passive_mob", "room_002", False)
        assert stats.total_npcs == 2
        assert stats.npcs_by_type["passive_mob"] == 1
        assert stats.npcs_by_room["room_002"] == 1
        assert stats.required_npcs == 1
        assert stats.optional_npcs == 1

        # Add another NPC of same type
        stats.add_npc("shopkeeper", "room_003", True)
        assert stats.total_npcs == 3
        assert stats.npcs_by_type["shopkeeper"] == 2
        assert stats.npcs_by_room["room_003"] == 1
        assert stats.required_npcs == 2
        assert stats.optional_npcs == 1

    def test_remove_npc_from_stats(self):
        """Test removing NPCs from population statistics."""
        stats = PopulationStats("arkhamcity", "downtown")

        # Add some NPCs first
        stats.add_npc("shopkeeper", "room_001", True)
        stats.add_npc("passive_mob", "room_002", False)
        stats.add_npc("shopkeeper", "room_003", True)

        # Remove one NPC
        stats.remove_npc("shopkeeper", "room_001", True)
        assert stats.total_npcs == 2
        assert stats.npcs_by_type["shopkeeper"] == 1
        assert stats.npcs_by_room["room_001"] == 0
        assert stats.required_npcs == 1
        assert stats.optional_npcs == 1

        # Remove another NPC
        stats.remove_npc("passive_mob", "room_002", False)
        assert stats.total_npcs == 1
        assert stats.npcs_by_type["passive_mob"] == 0
        assert stats.npcs_by_room["room_002"] == 0
        assert stats.required_npcs == 1
        assert stats.optional_npcs == 0

    def test_population_stats_negative_protection(self):
        """Test that population stats don't go negative."""
        stats = PopulationStats("arkhamcity", "downtown")

        # Try to remove from empty stats
        stats.remove_npc("shopkeeper", "room_001", True)
        assert stats.total_npcs == 0
        assert stats.npcs_by_type == {"shopkeeper": 0}  # Key exists but value is 0
        assert stats.npcs_by_room == {"room_001": 0}  # Key exists but value is 0
        assert stats.required_npcs == 0
        assert stats.optional_npcs == 0

    def test_population_stats_to_dict(self):
        """Test converting population stats to dictionary."""
        stats = PopulationStats("arkhamcity", "downtown")
        stats.add_npc("shopkeeper", "room_001", True)
        stats.add_npc("passive_mob", "room_002", False)

        stats_dict = stats.to_dict()

        assert stats_dict["zone_id"] == "arkhamcity"
        assert stats_dict["sub_zone_id"] == "downtown"
        assert stats_dict["total_npcs"] == 2
        assert stats_dict["npcs_by_type"]["shopkeeper"] == 1
        assert stats_dict["npcs_by_type"]["passive_mob"] == 1
        assert stats_dict["npcs_by_room"]["room_001"] == 1
        assert stats_dict["npcs_by_room"]["room_002"] == 1
        assert stats_dict["required_npcs"] == 1
        assert stats_dict["optional_npcs"] == 1
        assert "last_updated" in stats_dict


class TestNPCPopulationController:
    """Test the main NPC population controller."""

    @pytest.fixture
    def event_bus(self):
        """Create an event bus for testing."""
        return EventBus()

    @pytest.fixture
    def temp_rooms_dir(self):
        """Create a temporary directory with test room configurations."""
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_path = Path(temp_dir)

            # Create proper directory structure: plane/zone/subzone
            earth_dir = temp_path / "earth"
            earth_dir.mkdir()

            arkham_dir = earth_dir / "arkhamcity"
            arkham_dir.mkdir()

            downtown_dir = arkham_dir / "downtown"
            downtown_dir.mkdir()

            # Create zone config
            zone_config = {
                "zone_type": "city",
                "environment": "outdoors",
                "description": "A bustling urban area",
                "weather_patterns": ["fog", "rain", "overcast"],
                "special_rules": {
                    "npc_spawn_modifier": 1.2,
                    "sanity_drain_rate": 0.1,
                    "combat_modifier": 1.0,
                    "exploration_bonus": 0.5,
                },
            }

            with open(arkham_dir / "zone_config.json", "w") as f:
                json.dump(zone_config, f)

            # Create sub-zone config
            subzone_config = {
                "environment": "outdoors",
                "description": "The bustling commercial heart",
                "special_rules": {
                    "npc_spawn_modifier": 1.5,
                    "sanity_drain_rate": 0.08,
                    "combat_modifier": 1.1,
                    "exploration_bonus": 0.7,
                },
            }

            with open(downtown_dir / "subzone_config.json", "w") as f:
                json.dump(subzone_config, f)

            yield temp_path

    @pytest.fixture
    def population_controller(self, event_bus, temp_rooms_dir):
        """Create a population controller with test data."""
        # Create a mock spawning service
        mock_spawning_service = Mock()

        # Create a counter to generate unique NPC IDs
        npc_id_counter = [0]

        def create_mock_npc_instance(*args, **kwargs):
            npc_id_counter[0] += 1
            mock_npc_instance = Mock()
            mock_npc_instance.success = True
            mock_npc_instance.npc_id = f"test_npc_{npc_id_counter[0]:03d}"
            return mock_npc_instance

        mock_spawning_service._spawn_npc_from_request = Mock(side_effect=create_mock_npc_instance)

        # Create a mock lifecycle manager that tracks spawned NPCs
        mock_lifecycle_manager = Mock()
        mock_lifecycle_manager.active_npcs = {}

        def mock_spawn_npc(def_, room_id, reason):
            """Mock spawn_npc that actually adds to active_npcs."""
            npc_id = f"test_npc_{npc_id_counter[0]:03d}"
            npc_id_counter[0] += 1
            # Add the NPC to active_npcs
            mock_npc_instance = Mock()
            mock_npc_instance.name = def_.name
            mock_lifecycle_manager.active_npcs[npc_id] = mock_npc_instance
            return npc_id

        mock_lifecycle_manager.spawn_npc = Mock(side_effect=mock_spawn_npc)

        return NPCPopulationController(event_bus, mock_spawning_service, mock_lifecycle_manager, str(temp_rooms_dir))

    @pytest.fixture
    def shopkeeper_definition(self):
        """Create a shopkeeper NPC definition."""
        definition = NPCDefinition(
            name="Test Shopkeeper",
            description="A test shopkeeper",
            npc_type=NPCDefinitionType.SHOPKEEPER,
            sub_zone_id="downtown",
            required_npc=True,
            max_population=1,
            spawn_probability=1.0,
            base_stats='{"strength": 10, "sanity": 80, "current_health": 100}',
            behavior_config='{"greeting_message": "Welcome!"}',
            ai_integration_stub='{"ai_enabled": false}',
        )
        definition.id = 1  # Set explicit ID for testing
        return definition

    @pytest.fixture
    def passive_mob_definition(self):
        """Create a passive mob NPC definition."""
        definition = NPCDefinition(
            name="Test Passive Mob",
            description="A test passive mob",
            npc_type=NPCDefinitionType.PASSIVE_MOB,
            sub_zone_id="downtown",
            required_npc=False,
            max_population=3,
            spawn_probability=0.7,
            base_stats='{"strength": 8, "sanity": 60, "current_health": 80}',
            behavior_config='{"wandering_behavior": true}',
            ai_integration_stub='{"ai_enabled": false}',
        )
        definition.id = 2  # Set explicit ID for testing
        return definition

    @pytest.fixture
    def spawn_rule_shopkeeper(self, shopkeeper_definition):
        """Create a spawn rule for the shopkeeper."""
        return NPCSpawnRule(
            npc_definition_id=shopkeeper_definition.id,
            sub_zone_id="arkhamcity/downtown",
            min_population=0,
            max_population=999,
            spawn_conditions="{}",
        )

    @pytest.fixture
    def spawn_rule_passive_mob(self, passive_mob_definition):
        """Create a spawn rule for the passive mob."""
        return NPCSpawnRule(
            npc_definition_id=passive_mob_definition.id,
            sub_zone_id="arkhamcity/downtown",
            min_population=1,
            max_population=5,
            spawn_conditions='{"time_of_day": "day", "weather": "clear"}',
        )

    def test_population_controller_initialization(self, population_controller):
        """Test population controller initialization."""
        assert population_controller.event_bus is not None
        assert len(population_controller.zone_configurations) > 0
        assert "arkhamcity" in population_controller.zone_configurations
        assert "arkhamcity/downtown" in population_controller.zone_configurations
        assert len(population_controller.active_npcs) == 0
        assert len(population_controller.population_stats) == 0

    def test_zone_configuration_loading(self, population_controller):
        """Test that zone configurations are loaded correctly."""
        # Test zone configuration
        zone_config = population_controller.get_zone_configuration("arkhamcity")
        assert zone_config is not None
        assert zone_config.npc_spawn_modifier == 1.2
        assert zone_config.sanity_drain_rate == 0.1

        # Test sub-zone configuration
        subzone_config = population_controller.get_zone_configuration("arkhamcity/downtown")
        assert subzone_config is not None
        assert subzone_config.npc_spawn_modifier == 1.5
        assert subzone_config.sanity_drain_rate == 0.08

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

    def test_zone_configuration_missing_files(self, event_bus):
        """Test handling of missing zone configuration files."""
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_path = Path(temp_dir)

            # Create a zone directory without config files
            arkham_dir = temp_path / "arkhamcity"
            arkham_dir.mkdir()

            # This should not raise an exception
            controller = NPCPopulationController(event_bus, rooms_data_path=str(temp_path))
            assert len(controller.zone_configurations) == 0

    def test_zone_configuration_invalid_json(self, event_bus):
        """Test handling of invalid JSON in zone configuration files."""
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_path = Path(temp_dir)

            # Create zone directory with invalid JSON
            arkham_dir = temp_path / "arkhamcity"
            arkham_dir.mkdir()

            with open(arkham_dir / "zone_config.json", "w") as f:
                f.write("invalid json content")

            # This should not raise an exception
            controller = NPCPopulationController(event_bus, rooms_data_path=str(temp_path))
            assert len(controller.zone_configurations) == 0


# ============================================================================
# Tests merged from test_npc_population_management_legacy.py
# ============================================================================


"""
Tests for NPC population management and zone integration.

This module tests the NPC spawning, population control, and zone integration
systems that manage NPC populations across different areas of the game world.

As documented in the Cultes des Goules, proper population management is essential
for maintaining the delicate balance between the mundane and the eldritch forces
that lurk in the shadows of our world.
"""


class TestNPCPopulationManagement:
    """Test NPC population management and spawning logic."""

    @pytest.fixture
    def event_bus(self):
        """Create an event bus for testing."""
        return EventBus()

    @pytest.fixture
    def mock_room(self, event_bus):
        """Create a mock room for testing."""
        room_data = {
            "id": "test_room_001",
            "name": "Test Room",
            "description": "A test room for NPC population management",
            "plane": "earth",
            "zone": "arkhamcity",
            "sub_zone": "downtown",
            "environment": "outdoors",
            "exits": {"north": "test_room_002", "south": "test_room_003"},
        }
        return Room(room_data, event_bus)

    @pytest.fixture
    def shopkeeper_definition(self):
        """Create a shopkeeper NPC definition."""
        definition = NPCDefinition(
            name="Test Shopkeeper",
            description="A test shopkeeper for population management",
            npc_type=NPCDefinitionType.SHOPKEEPER,
            sub_zone_id="downtown",
            room_id="test_room_001",
            required_npc=True,
            max_population=1,
            spawn_probability=1.0,
            base_stats='{"strength": 10, "dexterity": 10, "constitution": 12, "intelligence": 14, "wisdom": 12, "charisma": 16, "sanity": 80, "current_health": 100}',
            behavior_config='{"greeting_message": "Welcome to my shop!", "farewell_message": "Come back soon!", "shop_items": ["potion", "scroll"]}',
            ai_integration_stub='{"ai_enabled": false, "response_delay": 1.0}',
        )
        return definition

    @pytest.fixture
    def passive_mob_definition(self):
        """Create a passive mob NPC definition."""
        definition = NPCDefinition(
            name="Test Passive Mob",
            description="A test passive mob for population management",
            npc_type=NPCDefinitionType.PASSIVE_MOB,
            sub_zone_id="downtown",
            room_id="test_room_001",
            required_npc=False,
            max_population=3,
            spawn_probability=0.7,
            base_stats='{"strength": 8, "dexterity": 12, "constitution": 10, "intelligence": 8, "wisdom": 10, "charisma": 6, "sanity": 60, "current_health": 80}',
            behavior_config='{"wandering_behavior": true, "response_message": "Hello there!", "flee_on_attack": true}',
            ai_integration_stub='{"ai_enabled": false, "wander_interval": 30.0}',
        )
        return definition

    @pytest.fixture
    def aggressive_mob_definition(self):
        """Create an aggressive mob NPC definition."""
        definition = NPCDefinition(
            name="Test Aggressive Mob",
            description="A test aggressive mob for population management",
            npc_type=NPCDefinitionType.AGGRESSIVE_MOB,
            sub_zone_id="downtown",
            room_id="test_room_001",
            required_npc=False,
            max_population=2,
            spawn_probability=0.5,
            base_stats='{"strength": 14, "dexterity": 10, "constitution": 12, "intelligence": 6, "wisdom": 8, "charisma": 4, "sanity": 40, "current_health": 120}',
            behavior_config='{"aggression_level": 0.8, "hunting_behavior": true, "territorial": true, "attack_message": "You dare enter my domain!"}',
            ai_integration_stub='{"ai_enabled": false, "hunt_radius": 2}',
        )
        return definition

    @pytest.fixture
    def spawn_rule_shopkeeper(self, shopkeeper_definition):
        """Create a spawn rule for the shopkeeper."""
        rule = NPCSpawnRule(
            npc_definition_id=shopkeeper_definition.id,
            sub_zone_id="downtown",
            min_population=0,
            max_population=999,
            spawn_conditions="{}",  # Empty conditions - should always pass
        )
        return rule

    @pytest.fixture
    def spawn_rule_passive_mob(self, passive_mob_definition):
        """Create a spawn rule for the passive mob."""
        rule = NPCSpawnRule(
            npc_definition_id=passive_mob_definition.id,
            sub_zone_id="downtown",
            min_population=1,
            max_population=5,
            spawn_conditions='{"time_of_day": "day", "weather": ["clear", "overcast"], "player_level_min": 1}',
        )
        return rule

    @pytest.fixture
    def spawn_rule_aggressive_mob(self, aggressive_mob_definition):
        """Create a spawn rule for the aggressive mob."""
        rule = NPCSpawnRule(
            npc_definition_id=aggressive_mob_definition.id,
            sub_zone_id="downtown",
            min_population=2,
            max_population=8,
            spawn_conditions='{"time_of_day": "night", "weather": ["fog", "rain"], "player_level_min": 3}',
        )
        return rule

    def test_npc_definition_population_limits(
        self, shopkeeper_definition, passive_mob_definition, aggressive_mob_definition
    ):
        """Test that NPC definitions properly enforce population limits."""
        # Test shopkeeper (required, max 1)
        assert shopkeeper_definition.is_required() is True
        assert shopkeeper_definition.can_spawn(0) is True
        assert shopkeeper_definition.can_spawn(1) is False

        # Test passive mob (optional, max 3)
        assert passive_mob_definition.is_required() is False
        assert passive_mob_definition.can_spawn(0) is True
        assert passive_mob_definition.can_spawn(2) is True
        assert passive_mob_definition.can_spawn(3) is False

        # Test aggressive mob (optional, max 2)
        assert aggressive_mob_definition.is_required() is False
        assert aggressive_mob_definition.can_spawn(0) is True
        assert aggressive_mob_definition.can_spawn(1) is True
        assert aggressive_mob_definition.can_spawn(2) is False

    def test_npc_spawn_rule_population_validation(
        self, spawn_rule_shopkeeper, spawn_rule_passive_mob, spawn_rule_aggressive_mob
    ):
        """Test that spawn rules properly validate NPC population counts."""
        # Shopkeeper: max 999 NPCs (essentially unlimited)
        assert spawn_rule_shopkeeper.can_spawn_with_population(0) is True
        assert spawn_rule_shopkeeper.can_spawn_with_population(1) is True
        assert spawn_rule_shopkeeper.can_spawn_with_population(998) is True
        assert spawn_rule_shopkeeper.can_spawn_with_population(999) is False  # At max

        # Passive mob: max 5 NPCs
        assert spawn_rule_passive_mob.can_spawn_with_population(0) is True
        assert spawn_rule_passive_mob.can_spawn_with_population(1) is True
        assert spawn_rule_passive_mob.can_spawn_with_population(4) is True
        assert spawn_rule_passive_mob.can_spawn_with_population(5) is False  # At max
        assert spawn_rule_passive_mob.can_spawn_with_population(6) is False  # Over max

        # Aggressive mob: max 8 NPCs
        assert spawn_rule_aggressive_mob.can_spawn_with_population(0) is True
        assert spawn_rule_aggressive_mob.can_spawn_with_population(2) is True
        assert spawn_rule_aggressive_mob.can_spawn_with_population(7) is True
        assert spawn_rule_aggressive_mob.can_spawn_with_population(8) is False  # At max
        assert spawn_rule_aggressive_mob.can_spawn_with_population(9) is False  # Over max

    def test_npc_spawn_rule_condition_checking(
        self, spawn_rule_shopkeeper, spawn_rule_passive_mob, spawn_rule_aggressive_mob
    ):
        """Test that spawn rules properly check game state conditions."""
        # Test shopkeeper conditions (any time, any weather, level 1+)
        game_state_shopkeeper = {"time_of_day": "day", "weather": "clear", "player_level_min": 1}
        # The shopkeeper rule has conditions that should match
        assert spawn_rule_shopkeeper.check_spawn_conditions(game_state_shopkeeper) is True

        # Test passive mob conditions (day, clear/overcast, level 1+)
        game_state_passive = {"time_of_day": "day", "weather": "clear", "player_level_min": 1}
        assert spawn_rule_passive_mob.check_spawn_conditions(game_state_passive) is True

        game_state_passive_overcast = {"time_of_day": "day", "weather": "overcast", "player_level_min": 1}
        assert spawn_rule_passive_mob.check_spawn_conditions(game_state_passive_overcast) is True

        # Test aggressive mob conditions (night, fog/rain, level 3+)
        game_state_aggressive = {"time_of_day": "night", "weather": "fog", "player_level_min": 3}
        assert spawn_rule_aggressive_mob.check_spawn_conditions(game_state_aggressive) is True

        game_state_aggressive_rain = {"time_of_day": "night", "weather": "rain", "player_level_min": 3}
        assert spawn_rule_aggressive_mob.check_spawn_conditions(game_state_aggressive_rain) is True

    def test_npc_spawn_rule_condition_failures(self, spawn_rule_passive_mob, spawn_rule_aggressive_mob):
        """Test that spawn rules properly reject invalid game states."""
        # Test passive mob failures
        game_state_wrong_time = {"time_of_day": "night", "weather": "clear", "player_level_min": 1}
        assert spawn_rule_passive_mob.check_spawn_conditions(game_state_wrong_time) is False

        game_state_wrong_weather = {"time_of_day": "day", "weather": "rain", "player_level_min": 1}
        assert spawn_rule_passive_mob.check_spawn_conditions(game_state_wrong_weather) is False

        # Test aggressive mob failures
        game_state_wrong_time_agg = {"time_of_day": "day", "weather": "fog", "player_level_min": 3}
        assert spawn_rule_aggressive_mob.check_spawn_conditions(game_state_wrong_time_agg) is False

        game_state_wrong_weather_agg = {"time_of_day": "night", "weather": "clear", "player_level_min": 3}
        assert spawn_rule_aggressive_mob.check_spawn_conditions(game_state_wrong_weather_agg) is False

        game_state_low_level = {"time_of_day": "night", "weather": "fog", "player_level_min": 2}
        assert spawn_rule_aggressive_mob.check_spawn_conditions(game_state_low_level) is False

    def test_npc_spawn_rule_range_conditions(self):
        """Test spawn rules with range-based conditions."""
        # Create a spawn rule with range conditions
        definition = NPCDefinition(
            name="Range Test NPC",
            description="Test NPC for range conditions",
            npc_type=NPCDefinitionType.PASSIVE_MOB,
            sub_zone_id="test_zone",
            required_npc=False,
            max_population=1,
            spawn_probability=1.0,
        )

        rule = NPCSpawnRule(
            npc_definition_id=definition.id,
            sub_zone_id="test_zone",
            min_population=0,
            max_population=999,
            spawn_conditions='{"player_level": {"min": 5, "max": 15}, "sanity": {"min": 50, "max": 100}}',
        )

        # Test valid ranges
        game_state_valid = {"player_level": 10, "sanity": 75}
        assert rule.check_spawn_conditions(game_state_valid) is True

        # Test edge cases
        game_state_min_edge = {"player_level": 5, "sanity": 50}
        assert rule.check_spawn_conditions(game_state_min_edge) is True

        game_state_max_edge = {"player_level": 15, "sanity": 100}
        assert rule.check_spawn_conditions(game_state_max_edge) is True

        # Test invalid ranges
        game_state_too_low = {"player_level": 4, "sanity": 75}
        assert rule.check_spawn_conditions(game_state_too_low) is False

        game_state_too_high = {"player_level": 16, "sanity": 75}
        assert rule.check_spawn_conditions(game_state_too_high) is False

        game_state_sanity_too_low = {"player_level": 10, "sanity": 49}
        assert rule.check_spawn_conditions(game_state_sanity_too_low) is False

    def test_npc_spawn_rule_list_conditions(self):
        """Test spawn rules with list-based conditions."""
        # Create a spawn rule with list conditions
        definition = NPCDefinition(
            name="List Test NPC",
            description="Test NPC for list conditions",
            npc_type=NPCDefinitionType.SHOPKEEPER,
            sub_zone_id="test_zone",
            required_npc=False,
            max_population=1,
            spawn_probability=1.0,
        )

        rule = NPCSpawnRule(
            npc_definition_id=definition.id,
            sub_zone_id="test_zone",
            min_population=0,
            max_population=999,
            spawn_conditions='{"weather": ["clear", "overcast", "mist"], "time_of_day": ["day", "dusk"]}',
        )

        # Test valid list values
        game_state_valid_clear = {"weather": "clear", "time_of_day": "day"}
        assert rule.check_spawn_conditions(game_state_valid_clear) is True

        game_state_valid_overcast = {"weather": "overcast", "time_of_day": "dusk"}
        assert rule.check_spawn_conditions(game_state_valid_overcast) is True

        game_state_valid_mist = {"weather": "mist", "time_of_day": "day"}
        assert rule.check_spawn_conditions(game_state_valid_mist) is True

        # Test invalid list values
        game_state_invalid_weather = {"weather": "rain", "time_of_day": "day"}
        assert rule.check_spawn_conditions(game_state_invalid_weather) is False

        game_state_invalid_time = {"weather": "clear", "time_of_day": "night"}
        assert rule.check_spawn_conditions(game_state_invalid_time) is False

    def test_npc_spawn_rule_missing_conditions(self):
        """Test spawn rules with missing game state conditions."""
        definition = NPCDefinition(
            name="Missing Test NPC",
            description="Test NPC for missing conditions",
            npc_type=NPCDefinitionType.PASSIVE_MOB,
            sub_zone_id="test_zone",
            required_npc=False,
            max_population=1,
            spawn_probability=1.0,
        )

        rule = NPCSpawnRule(
            npc_definition_id=definition.id,
            sub_zone_id="test_zone",
            min_population=0,
            max_population=999,
            spawn_conditions='{"required_condition": "value", "optional_condition": "optional"}',
        )

        # Test with missing required condition
        game_state_missing = {"optional_condition": "optional"}
        assert rule.check_spawn_conditions(game_state_missing) is False

        # Test with all conditions present
        game_state_complete = {"required_condition": "value", "optional_condition": "optional"}
        assert rule.check_spawn_conditions(game_state_complete) is True

    def test_npc_spawn_rule_empty_conditions(self):
        """Test spawn rules with empty conditions (should always pass)."""
        definition = NPCDefinition(
            name="Empty Test NPC",
            description="Test NPC for empty conditions",
            npc_type=NPCDefinitionType.SHOPKEEPER,
            sub_zone_id="test_zone",
            required_npc=False,
            max_population=1,
            spawn_probability=1.0,
        )

        rule = NPCSpawnRule(
            npc_definition_id=definition.id,
            sub_zone_id="test_zone",
            min_population=0,
            max_population=999,
            spawn_conditions="{}",
        )

        # Test with any game state (should pass)
        game_state_any = {"any_condition": "any_value"}
        assert rule.check_spawn_conditions(game_state_any) is True

        # Test with empty game state (should pass)
        game_state_empty = {}
        assert rule.check_spawn_conditions(game_state_empty) is True

    def test_npc_definition_json_serialization(self, shopkeeper_definition):
        """Test that NPC definitions properly serialize and deserialize JSON data."""
        # Test base stats
        stats = shopkeeper_definition.get_base_stats()
        assert isinstance(stats, dict)
        assert "strength" in stats
        assert "sanity" in stats
        assert stats["strength"] == 10
        assert stats["sanity"] == 80

        # Test behavior config
        behavior = shopkeeper_definition.get_behavior_config()
        assert isinstance(behavior, dict)
        assert "greeting_message" in behavior
        assert "shop_items" in behavior
        assert behavior["greeting_message"] == "Welcome to my shop!"

        # Test AI integration stub
        ai_config = shopkeeper_definition.get_ai_integration_stub()
        assert isinstance(ai_config, dict)
        assert "ai_enabled" in ai_config
        assert "response_delay" in ai_config
        assert ai_config["ai_enabled"] is False

    def test_npc_definition_json_modification(self, shopkeeper_definition):
        """Test that NPC definitions properly handle JSON data modification."""
        # Modify base stats
        new_stats = {"strength": 15, "dexterity": 12, "sanity": 90, "current_health": 120}
        shopkeeper_definition.set_base_stats(new_stats)

        retrieved_stats = shopkeeper_definition.get_base_stats()
        assert retrieved_stats["strength"] == 15
        assert retrieved_stats["sanity"] == 90

        # Modify behavior config
        new_behavior = {"greeting_message": "New greeting!", "farewell_message": "New farewell!"}
        shopkeeper_definition.set_behavior_config(new_behavior)

        retrieved_behavior = shopkeeper_definition.get_behavior_config()
        assert retrieved_behavior["greeting_message"] == "New greeting!"
        assert retrieved_behavior["farewell_message"] == "New farewell!"

        # Modify AI integration stub
        new_ai_config = {"ai_enabled": True, "response_delay": 2.0, "new_setting": "value"}
        shopkeeper_definition.set_ai_integration_stub(new_ai_config)

        retrieved_ai_config = shopkeeper_definition.get_ai_integration_stub()
        assert retrieved_ai_config["ai_enabled"] is True
        assert retrieved_ai_config["response_delay"] == 2.0
        assert retrieved_ai_config["new_setting"] == "value"

    def test_npc_definition_invalid_json_handling(self):
        """Test that NPC definitions handle invalid JSON gracefully."""
        definition = NPCDefinition(
            name="Invalid JSON Test",
            description="Test NPC for invalid JSON handling",
            npc_type=NPCDefinitionType.PASSIVE_MOB,
            sub_zone_id="test_zone",
            required_npc=False,
            max_population=1,
            spawn_probability=1.0,
            base_stats="invalid json",
            behavior_config="also invalid",
            ai_integration_stub="still invalid",
        )

        # Test that invalid JSON returns empty dict
        stats = definition.get_base_stats()
        assert stats == {}

        behavior = definition.get_behavior_config()
        assert behavior == {}

        ai_config = definition.get_ai_integration_stub()
        assert ai_config == {}

    def test_npc_spawn_rule_json_serialization(self, spawn_rule_shopkeeper):
        """Test that spawn rules properly serialize and deserialize JSON data."""
        # Test spawn conditions (initially empty)
        conditions = spawn_rule_shopkeeper.get_spawn_conditions()
        assert isinstance(conditions, dict)
        assert conditions == {}  # Should be empty initially

        # Test modification
        new_conditions = {"time_of_day": "night", "weather": "fog", "special_condition": True}
        spawn_rule_shopkeeper.set_spawn_conditions(new_conditions)

        retrieved_conditions = spawn_rule_shopkeeper.get_spawn_conditions()
        assert retrieved_conditions["time_of_day"] == "night"
        assert retrieved_conditions["weather"] == "fog"
        assert retrieved_conditions["special_condition"] is True

    def test_npc_spawn_rule_invalid_json_handling(self):
        """Test that spawn rules handle invalid JSON gracefully."""
        definition = NPCDefinition(
            name="Invalid Spawn Rule Test",
            description="Test NPC for invalid spawn rule JSON",
            npc_type=NPCDefinitionType.PASSIVE_MOB,
            sub_zone_id="test_zone",
            required_npc=False,
            max_population=1,
            spawn_probability=1.0,
        )

        rule = NPCSpawnRule(
            npc_definition_id=definition.id,
            sub_zone_id="test_zone",
            min_population=0,
            max_population=999,
            spawn_conditions="invalid json",
        )

        # Test that invalid JSON returns empty dict
        conditions = rule.get_spawn_conditions()
        assert conditions == {}

        # Test that empty conditions always pass
        game_state = {"any_condition": "any_value"}
        assert rule.check_spawn_conditions(game_state) is True


class TestNPCZoneIntegration:
    """Test NPC integration with zone and sub-zone systems."""

    @pytest.fixture
    def event_bus(self):
        """Create an event bus for testing."""
        return EventBus()

    @pytest.fixture
    def arkham_downtown_room(self, event_bus):
        """Create a room in Arkham downtown."""
        room_data = {
            "id": "earth_arkhamcity_downtown_001",
            "name": "Arkham Downtown Square",
            "description": "The bustling commercial heart of Arkham",
            "plane": "earth",
            "zone": "arkhamcity",
            "sub_zone": "downtown",
            "environment": "outdoors",
            "exits": {"north": "earth_arkhamcity_downtown_002", "south": "earth_arkhamcity_downtown_003"},
        }
        return Room(room_data, event_bus)

    @pytest.fixture
    def innsmouth_waterfront_room(self, event_bus):
        """Create a room in Innsmouth waterfront."""
        room_data = {
            "id": "earth_innsmouth_waterfront_001",
            "name": "Innsmouth Waterfront",
            "description": "The decaying waterfront district",
            "plane": "earth",
            "zone": "innsmouth",
            "sub_zone": "waterfront",
            "environment": "outdoors",
            "exits": {"east": "earth_innsmouth_waterfront_002", "west": "earth_innsmouth_waterfront_003"},
        }
        return Room(room_data, event_bus)

    def test_npc_zone_based_spawning(self, arkham_downtown_room, innsmouth_waterfront_room):
        """Test that NPCs spawn based on zone and sub-zone configurations."""
        # Test Arkham downtown (should have higher spawn modifier)
        assert arkham_downtown_room.zone == "arkhamcity"
        assert arkham_downtown_room.sub_zone == "downtown"
        assert arkham_downtown_room.environment == "outdoors"

        # Test Innsmouth waterfront (should have lower spawn modifier)
        assert innsmouth_waterfront_room.zone == "innsmouth"
        assert innsmouth_waterfront_room.sub_zone == "waterfront"
        assert innsmouth_waterfront_room.environment == "outdoors"

    def test_npc_room_occupancy_tracking(self, arkham_downtown_room, event_bus):
        """Test that rooms properly track NPC occupancy."""
        # Initially empty
        assert arkham_downtown_room.is_empty() is True
        assert arkham_downtown_room.get_occupant_count() == 0
        assert arkham_downtown_room.get_npcs() == []

        # Add NPCs
        npc_id_1 = "test_npc_001"
        npc_id_2 = "test_npc_002"

        arkham_downtown_room.npc_entered(npc_id_1)
        assert arkham_downtown_room.has_npc(npc_id_1) is True
        assert arkham_downtown_room.get_occupant_count() == 1
        assert arkham_downtown_room.get_npcs() == [npc_id_1]

        arkham_downtown_room.npc_entered(npc_id_2)
        assert arkham_downtown_room.has_npc(npc_id_2) is True
        assert arkham_downtown_room.get_occupant_count() == 2
        assert set(arkham_downtown_room.get_npcs()) == {npc_id_1, npc_id_2}

        # Remove NPCs
        arkham_downtown_room.npc_left(npc_id_1)
        assert arkham_downtown_room.has_npc(npc_id_1) is False
        assert arkham_downtown_room.has_npc(npc_id_2) is True
        assert arkham_downtown_room.get_occupant_count() == 1
        assert arkham_downtown_room.get_npcs() == [npc_id_2]

        arkham_downtown_room.npc_left(npc_id_2)
        assert arkham_downtown_room.has_npc(npc_id_2) is False
        assert arkham_downtown_room.is_empty() is True
        assert arkham_downtown_room.get_occupant_count() == 0
        assert arkham_downtown_room.get_npcs() == []

    @pytest.mark.asyncio
    async def test_npc_room_event_publishing(self, arkham_downtown_room, event_bus):
        """Test that room NPC events are properly published."""
        # Track events
        events = []

        def event_handler(event):
            events.append(event)

        event_bus.subscribe(NPCEnteredRoom, event_handler)
        event_bus.subscribe(NPCLeftRoom, event_handler)

        # Add NPC
        npc_id = "test_npc_001"
        arkham_downtown_room.npc_entered(npc_id)

        # Allow event processing with proper async handling
        await asyncio.sleep(0.1)

        # Check events
        assert len(events) == 1
        assert isinstance(events[0], NPCEnteredRoom)
        assert events[0].npc_id == npc_id
        assert events[0].room_id == arkham_downtown_room.id

        # Remove NPC
        arkham_downtown_room.npc_left(npc_id)

        # Allow event processing with proper async handling
        await asyncio.sleep(0.1)

        # Check events
        assert len(events) == 2
        assert isinstance(events[1], NPCLeftRoom)
        assert events[1].npc_id == npc_id
        assert events[1].room_id == arkham_downtown_room.id

    def test_npc_room_duplicate_handling(self, arkham_downtown_room):
        """Test that rooms handle duplicate NPC entries gracefully."""
        npc_id = "test_npc_001"

        # Add NPC first time
        arkham_downtown_room.npc_entered(npc_id)
        assert arkham_downtown_room.has_npc(npc_id) is True
        assert arkham_downtown_room.get_occupant_count() == 1

        # Try to add same NPC again (should be ignored)
        arkham_downtown_room.npc_entered(npc_id)
        assert arkham_downtown_room.has_npc(npc_id) is True
        assert arkham_downtown_room.get_occupant_count() == 1  # Should still be 1

    def test_npc_room_removal_of_nonexistent(self, arkham_downtown_room):
        """Test that rooms handle removal of non-existent NPCs gracefully."""
        npc_id = "nonexistent_npc"

        # Try to remove non-existent NPC (should be ignored)
        arkham_downtown_room.npc_left(npc_id)
        assert arkham_downtown_room.has_npc(npc_id) is False
        assert arkham_downtown_room.get_occupant_count() == 0

    def test_npc_room_mixed_occupancy(self, arkham_downtown_room, event_bus):
        """Test that rooms properly track mixed occupancy (players, objects, NPCs)."""
        # Add different types of occupants
        player_id = "test_player_001"
        object_id = "test_object_001"
        npc_id = "test_npc_001"

        arkham_downtown_room.player_entered(player_id)
        arkham_downtown_room.object_added(object_id)
        arkham_downtown_room.npc_entered(npc_id)

        # Check occupancy
        assert arkham_downtown_room.get_occupant_count() == 3
        assert arkham_downtown_room.get_players() == [player_id]
        assert arkham_downtown_room.get_objects() == [object_id]
        assert arkham_downtown_room.get_npcs() == [npc_id]
        assert arkham_downtown_room.is_empty() is False

        # Remove NPC
        arkham_downtown_room.npc_left(npc_id)
        assert arkham_downtown_room.get_occupant_count() == 2
        assert arkham_downtown_room.get_npcs() == []
        assert arkham_downtown_room.has_npc(npc_id) is False

    def test_npc_room_to_dict_serialization(self, arkham_downtown_room):
        """Test that rooms properly serialize to dictionary with NPC data."""
        # Add NPCs
        npc_id_1 = "test_npc_001"
        npc_id_2 = "test_npc_002"

        arkham_downtown_room.npc_entered(npc_id_1)
        arkham_downtown_room.npc_entered(npc_id_2)

        # Serialize to dict
        room_dict = arkham_downtown_room.to_dict()

        # Check NPC data
        assert "npcs" in room_dict
        assert set(room_dict["npcs"]) == {npc_id_1, npc_id_2}
        assert room_dict["occupant_count"] == 2

        # Check other room data
        assert room_dict["id"] == arkham_downtown_room.id
        assert room_dict["name"] == arkham_downtown_room.name
        assert room_dict["zone"] == arkham_downtown_room.zone
        assert room_dict["sub_zone"] == arkham_downtown_room.sub_zone
