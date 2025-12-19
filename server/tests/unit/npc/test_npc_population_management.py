"""
Tests for NPC population management and spawn rules.

This module tests the NPC spawning logic, population limits, spawn conditions,
and JSON serialization for NPC definitions and spawn rules.

As documented in the Cultes des Goules, proper population management is essential
for maintaining the delicate balance between the mundane and the eldritch forces
that lurk in the shadows of our world.
"""

from typing import Any

import pytest

from server.events.event_bus import EventBus
from server.models.npc import NPCDefinition, NPCDefinitionType, NPCSpawnRule
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
            base_stats='{"strength": 10, "dexterity": 50, "constitution": 50, "size": 50, "intelligence": 50, "power": 50, "education": 50, "charisma": 50, "luck": 50, "lucidity": 80, "occult": 0, "corruption": 0, "determination_points": 20, "max_dp": 20, "magic_points": 10, "max_magic_points": 10, "xp_value": 1}',
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
            base_stats='{"strength": 40, "dexterity": 60, "constitution": 50, "size": 50, "intelligence": 40, "power": 50, "education": 50, "charisma": 30, "luck": 50, "lucidity": 60, "occult": 0, "corruption": 0, "determination_points": 20, "max_dp": 20, "magic_points": 10, "max_magic_points": 10, "xp_value": 1}',
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
            base_stats='{"strength": 70, "dexterity": 50, "constitution": 60, "size": 50, "intelligence": 30, "power": 50, "education": 40, "charisma": 20, "luck": 50, "lucidity": 40, "occult": 0, "corruption": 0, "determination_points": 22, "max_dp": 22, "magic_points": 10, "max_magic_points": 10, "xp_value": 1}',
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

    def test_npc_spawn_rule_range_conditions(self) -> None:
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
            spawn_conditions='{"player_level": {"min": 5, "max": 15}, "lucidity": {"min": 50, "max": 100}}',
        )

        # Test valid ranges
        game_state_valid = {"player_level": 10, "lucidity": 75}
        assert rule.check_spawn_conditions(game_state_valid) is True

        # Test edge cases
        game_state_min_edge = {"player_level": 5, "lucidity": 50}
        assert rule.check_spawn_conditions(game_state_min_edge) is True

        game_state_max_edge = {"player_level": 15, "lucidity": 100}
        assert rule.check_spawn_conditions(game_state_max_edge) is True

        # Test invalid ranges
        game_state_too_low = {"player_level": 4, "lucidity": 75}
        assert rule.check_spawn_conditions(game_state_too_low) is False

        game_state_too_high = {"player_level": 16, "lucidity": 75}
        assert rule.check_spawn_conditions(game_state_too_high) is False

        game_state_Lucidity_too_low = {"player_level": 10, "lucidity": 49}
        assert rule.check_spawn_conditions(game_state_Lucidity_too_low) is False

    def test_npc_spawn_rule_list_conditions(self) -> None:
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

    def test_npc_spawn_rule_missing_conditions(self) -> None:
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

    def test_npc_spawn_rule_empty_conditions(self) -> None:
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
        game_state_empty: dict[str, Any] = {}
        assert rule.check_spawn_conditions(game_state_empty) is True

    def test_npc_definition_json_serialization(self, shopkeeper_definition):
        """Test that NPC definitions properly serialize and deserialize JSON data."""
        # Test base stats
        stats = shopkeeper_definition.get_base_stats()
        assert isinstance(stats, dict)
        assert "strength" in stats
        assert "lucidity" in stats
        assert stats["strength"] == 10
        assert stats["lucidity"] == 80

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
        new_stats = {"strength": 15, "dexterity": 12, "lucidity": 90, "current_dp": 120}
        shopkeeper_definition.set_base_stats(new_stats)

        retrieved_stats = shopkeeper_definition.get_base_stats()
        assert retrieved_stats["strength"] == 15
        assert retrieved_stats["lucidity"] == 90

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

    def test_npc_definition_invalid_json_handling(self) -> None:
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

    def test_npc_spawn_rule_invalid_json_handling(self) -> None:
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
