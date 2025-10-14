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
import time
from pathlib import Path
from unittest.mock import Mock, patch

import pytest

from server.events.event_bus import EventBus
from server.events.event_types import PlayerEnteredRoom
from server.models.npc import NPCDefinition, NPCDefinitionType, NPCSpawnRule
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
        return NPCPopulationController(event_bus, mock_spawning_service, str(temp_rooms_dir))

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
            min_players=0,
            max_players=999,
            spawn_conditions="{}",
        )

    @pytest.fixture
    def spawn_rule_passive_mob(self, passive_mob_definition):
        """Create a spawn rule for the passive mob."""
        return NPCSpawnRule(
            npc_definition_id=passive_mob_definition.id,
            sub_zone_id="arkhamcity/downtown",
            min_players=1,
            max_players=5,
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
            stats.add_npc(passive_mob_definition.npc_type, f"room_{i:03d}", False)

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

        # Check that NPC was created
        assert npc_id in population_controller.active_npcs
        npc_data = population_controller.active_npcs[npc_id]
        assert npc_data["definition_id"] == shopkeeper_definition.id
        assert npc_data["npc_type"] == shopkeeper_definition.npc_type
        assert npc_data["name"] == shopkeeper_definition.name
        assert npc_data["room_id"] == "earth_arkhamcity_downtown_001"
        assert npc_data["is_required"] is True

        # Check that population stats were updated
        zone_key = "arkhamcity/downtown"
        assert zone_key in population_controller.population_stats
        stats = population_controller.population_stats[zone_key]
        assert stats.total_npcs == 1
        assert stats.npcs_by_type[shopkeeper_definition.npc_type] == 1
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

        # Check that NPC was removed
        assert npc_id not in population_controller.active_npcs

        # Check that population stats were updated
        zone_key = "arkhamcity/downtown"
        stats = population_controller.population_stats[zone_key]
        assert stats.total_npcs == 0
        assert stats.npcs_by_type[shopkeeper_definition.npc_type] == 0
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
        assert zone_summary["npcs_by_type"]["shopkeeper"] == 1
        assert zone_summary["npcs_by_type"]["passive_mob"] == 1
        assert zone_summary["required_npcs"] == 1
        assert zone_summary["optional_npcs"] == 1

    def test_cleanup_inactive_npcs(self, population_controller, passive_mob_definition, spawn_rule_passive_mob):
        """Test cleaning up inactive NPCs."""
        # Load definitions and rules
        population_controller.load_npc_definitions([passive_mob_definition])
        population_controller.load_spawn_rules([spawn_rule_passive_mob])

        # Spawn an optional NPC
        npc_id = population_controller._spawn_npc(passive_mob_definition, "earth_arkhamcity_downtown_001")

        # Manually set the spawn time to be old
        population_controller.active_npcs[npc_id]["spawned_at"] = time.time() - 4000  # 4000 seconds ago

        # Clean up inactive NPCs
        cleaned_count = population_controller.cleanup_inactive_npcs(max_age_seconds=3600)

        assert cleaned_count == 1
        assert npc_id not in population_controller.active_npcs

    def test_cleanup_does_not_remove_required_npcs(
        self, population_controller, shopkeeper_definition, spawn_rule_shopkeeper
    ):
        """Test that cleanup doesn't remove required NPCs."""
        # Load definitions and rules
        population_controller.load_npc_definitions([shopkeeper_definition])
        population_controller.load_spawn_rules([spawn_rule_shopkeeper])

        # Spawn a required NPC
        npc_id = population_controller._spawn_npc(shopkeeper_definition, "earth_arkhamcity_downtown_001")

        # Manually set the spawn time to be old
        population_controller.active_npcs[npc_id]["spawned_at"] = time.time() - 4000  # 4000 seconds ago

        # Clean up inactive NPCs
        cleaned_count = population_controller.cleanup_inactive_npcs(max_age_seconds=3600)

        assert cleaned_count == 0
        assert npc_id in population_controller.active_npcs

    @pytest.mark.asyncio
    async def test_event_handling(self, population_controller, shopkeeper_definition, spawn_rule_shopkeeper):
        """Test event handling for player and NPC movements."""
        # Load definitions and rules
        population_controller.load_npc_definitions([shopkeeper_definition])
        population_controller.load_spawn_rules([spawn_rule_shopkeeper])

        # Test player entering room (should trigger spawn check)
        player_event = PlayerEnteredRoom(
            timestamp=None, event_type="", player_id="test_player", room_id="earth_arkhamcity_downtown_001"
        )

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
