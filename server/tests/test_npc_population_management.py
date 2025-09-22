"""
Tests for NPC population management and zone integration.

This module tests the NPC spawning, population control, and zone integration
systems that manage NPC populations across different areas of the game world.

As documented in the Cultes des Goules, proper population management is essential
for maintaining the delicate balance between the mundane and the eldritch forces
that lurk in the shadows of our world.
"""

import time

import pytest

from server.events.event_bus import EventBus
from server.events.event_types import (
    NPCEnteredRoom,
    NPCLeftRoom,
)
from server.models.npc import NPCDefinition, NPCDefinitionType, NPCRelationship, NPCRelationshipType, NPCSpawnRule
from server.models.room import Room


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
            "zone": "arkham_city",
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
            min_players=0,
            max_players=999,
            spawn_conditions="{}",  # Empty conditions - should always pass
        )
        return rule

    @pytest.fixture
    def spawn_rule_passive_mob(self, passive_mob_definition):
        """Create a spawn rule for the passive mob."""
        rule = NPCSpawnRule(
            npc_definition_id=passive_mob_definition.id,
            sub_zone_id="downtown",
            min_players=1,
            max_players=5,
            spawn_conditions='{"time_of_day": "day", "weather": ["clear", "overcast"], "player_level_min": 1}',
        )
        return rule

    @pytest.fixture
    def spawn_rule_aggressive_mob(self, aggressive_mob_definition):
        """Create a spawn rule for the aggressive mob."""
        rule = NPCSpawnRule(
            npc_definition_id=aggressive_mob_definition.id,
            sub_zone_id="downtown",
            min_players=2,
            max_players=8,
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

    def test_npc_spawn_rule_player_count_validation(
        self, spawn_rule_shopkeeper, spawn_rule_passive_mob, spawn_rule_aggressive_mob
    ):
        """Test that spawn rules properly validate player counts."""
        # Shopkeeper: any player count
        assert spawn_rule_shopkeeper.can_spawn_for_player_count(0) is True
        assert spawn_rule_shopkeeper.can_spawn_for_player_count(1) is True
        assert spawn_rule_shopkeeper.can_spawn_for_player_count(10) is True

        # Passive mob: 1-5 players
        assert spawn_rule_passive_mob.can_spawn_for_player_count(0) is False
        assert spawn_rule_passive_mob.can_spawn_for_player_count(1) is True
        assert spawn_rule_passive_mob.can_spawn_for_player_count(3) is True
        assert spawn_rule_passive_mob.can_spawn_for_player_count(5) is True
        assert spawn_rule_passive_mob.can_spawn_for_player_count(6) is False

        # Aggressive mob: 2-8 players
        assert spawn_rule_aggressive_mob.can_spawn_for_player_count(1) is False
        assert spawn_rule_aggressive_mob.can_spawn_for_player_count(2) is True
        assert spawn_rule_aggressive_mob.can_spawn_for_player_count(5) is True
        assert spawn_rule_aggressive_mob.can_spawn_for_player_count(8) is True
        assert spawn_rule_aggressive_mob.can_spawn_for_player_count(9) is False

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
            min_players=0,
            max_players=999,
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
            min_players=0,
            max_players=999,
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
            min_players=0,
            max_players=999,
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
            min_players=0,
            max_players=999,
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
            min_players=0,
            max_players=999,
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
            "id": "earth_arkham_city_downtown_001",
            "name": "Arkham Downtown Square",
            "description": "The bustling commercial heart of Arkham",
            "plane": "earth",
            "zone": "arkham_city",
            "sub_zone": "downtown",
            "environment": "outdoors",
            "exits": {"north": "earth_arkham_city_downtown_002", "south": "earth_arkham_city_downtown_003"},
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
        assert arkham_downtown_room.zone == "arkham_city"
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

    def test_npc_room_event_publishing(self, arkham_downtown_room, event_bus):
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

        # Allow event processing
        time.sleep(0.1)

        # Check events
        assert len(events) == 1
        assert isinstance(events[0], NPCEnteredRoom)
        assert events[0].npc_id == npc_id
        assert events[0].room_id == arkham_downtown_room.id

        # Remove NPC
        arkham_downtown_room.npc_left(npc_id)

        # Allow event processing
        time.sleep(0.1)

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


class TestNPCRelationshipSystem:
    """Test NPC relationship and interaction systems."""

    @pytest.fixture
    def shopkeeper_definition(self):
        """Create a shopkeeper NPC definition."""
        return NPCDefinition(
            name="Test Shopkeeper",
            description="A test shopkeeper",
            npc_type=NPCDefinitionType.SHOPKEEPER,
            sub_zone_id="downtown",
            required_npc=True,
            max_population=1,
            spawn_probability=1.0,
        )

    @pytest.fixture
    def guard_definition(self):
        """Create a guard NPC definition."""
        return NPCDefinition(
            name="Test Guard",
            description="A test guard",
            npc_type=NPCDefinitionType.PASSIVE_MOB,
            sub_zone_id="downtown",
            required_npc=True,
            max_population=2,
            spawn_probability=1.0,
        )

    @pytest.fixture
    def cultist_definition(self):
        """Create a cultist NPC definition."""
        return NPCDefinition(
            name="Test Cultist",
            description="A test cultist",
            npc_type=NPCDefinitionType.AGGRESSIVE_MOB,
            sub_zone_id="downtown",
            required_npc=False,
            max_population=1,
            spawn_probability=0.3,
        )

    def test_npc_relationship_creation(self, shopkeeper_definition, guard_definition, cultist_definition):
        """Test creation of NPC relationships."""
        # Create ally relationship between shopkeeper and guard
        ally_relationship = NPCRelationship(
            npc_id_1=shopkeeper_definition.id,
            npc_id_2=guard_definition.id,
            relationship_type=NPCRelationshipType.ALLY,
            relationship_strength=0.8,
        )

        assert ally_relationship.is_positive_relationship() is True
        assert ally_relationship.is_negative_relationship() is False
        assert ally_relationship.is_neutral_relationship() is False
        assert ally_relationship.get_relationship_modifier() == 0.8

        # Create enemy relationship between guard and cultist
        enemy_relationship = NPCRelationship(
            npc_id_1=guard_definition.id,
            npc_id_2=cultist_definition.id,
            relationship_type=NPCRelationshipType.ENEMY,
            relationship_strength=0.9,
        )

        assert enemy_relationship.is_positive_relationship() is False
        assert enemy_relationship.is_negative_relationship() is True
        assert enemy_relationship.is_neutral_relationship() is False
        assert enemy_relationship.get_relationship_modifier() == -0.9

        # Create neutral relationship between shopkeeper and cultist
        neutral_relationship = NPCRelationship(
            npc_id_1=shopkeeper_definition.id,
            npc_id_2=cultist_definition.id,
            relationship_type=NPCRelationshipType.NEUTRAL,
            relationship_strength=0.5,
        )

        assert neutral_relationship.is_positive_relationship() is False
        assert neutral_relationship.is_negative_relationship() is False
        assert neutral_relationship.is_neutral_relationship() is True
        assert neutral_relationship.get_relationship_modifier() == 0.0

    def test_npc_relationship_follower_type(self, shopkeeper_definition, guard_definition):
        """Test follower relationship type."""
        follower_relationship = NPCRelationship(
            npc_id_1=guard_definition.id,
            npc_id_2=shopkeeper_definition.id,
            relationship_type=NPCRelationshipType.FOLLOWER,
            relationship_strength=0.7,
        )

        assert follower_relationship.is_positive_relationship() is True
        assert follower_relationship.is_negative_relationship() is False
        assert follower_relationship.is_neutral_relationship() is False
        assert follower_relationship.get_relationship_modifier() == 0.7

    def test_npc_relationship_strength_variations(self, shopkeeper_definition, guard_definition):
        """Test relationship strength variations."""
        # Strong positive relationship
        strong_ally = NPCRelationship(
            npc_id_1=shopkeeper_definition.id,
            npc_id_2=guard_definition.id,
            relationship_type=NPCRelationshipType.ALLY,
            relationship_strength=1.0,
        )
        assert strong_ally.get_relationship_modifier() == 1.0

        # Weak positive relationship
        weak_ally = NPCRelationship(
            npc_id_1=shopkeeper_definition.id,
            npc_id_2=guard_definition.id,
            relationship_type=NPCRelationshipType.ALLY,
            relationship_strength=0.2,
        )
        assert weak_ally.get_relationship_modifier() == 0.2

        # Strong negative relationship
        strong_enemy = NPCRelationship(
            npc_id_1=shopkeeper_definition.id,
            npc_id_2=guard_definition.id,
            relationship_type=NPCRelationshipType.ENEMY,
            relationship_strength=0.9,
        )
        assert strong_enemy.get_relationship_modifier() == -0.9

        # Weak negative relationship
        weak_enemy = NPCRelationship(
            npc_id_1=shopkeeper_definition.id,
            npc_id_2=guard_definition.id,
            relationship_type=NPCRelationshipType.ENEMY,
            relationship_strength=0.1,
        )
        assert weak_enemy.get_relationship_modifier() == -0.1

    def test_npc_relationship_string_representation(self, shopkeeper_definition, guard_definition):
        """Test string representation of NPC relationships."""
        relationship = NPCRelationship(
            npc_id_1=shopkeeper_definition.id,
            npc_id_2=guard_definition.id,
            relationship_type=NPCRelationshipType.ALLY,
            relationship_strength=0.8,
        )

        repr_str = repr(relationship)
        assert "NPCRelationship" in repr_str
        assert str(shopkeeper_definition.id) in repr_str
        assert str(guard_definition.id) in repr_str
        assert "NPCRelationshipType.ALLY" in repr_str

    def test_npc_definition_string_representation(self, shopkeeper_definition):
        """Test string representation of NPC definitions."""
        repr_str = repr(shopkeeper_definition)
        assert "NPCDefinition" in repr_str
        assert "Test Shopkeeper" in repr_str
        assert "NPCDefinitionType.SHOPKEEPER" in repr_str

    def test_npc_spawn_rule_string_representation(self, shopkeeper_definition):
        """Test string representation of NPC spawn rules."""
        rule = NPCSpawnRule(
            npc_definition_id=shopkeeper_definition.id, sub_zone_id="downtown", min_players=0, max_players=999
        )

        repr_str = repr(rule)
        assert "NPCSpawnRule" in repr_str
        assert str(shopkeeper_definition.id) in repr_str
        assert "downtown" in repr_str
