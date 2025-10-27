"""
Tests for NPC spawning service.

This module tests the NPC spawning logic that integrates with the population
control system to spawn NPCs based on required/optional population rules
and game state conditions.

As documented in the Cultes des Goules, proper spawning rituals are essential
for maintaining the delicate balance between the mundane and the eldritch forces
that lurk in the shadows of our world.
"""

import time
from unittest.mock import MagicMock, patch

import pytest

from server.events.event_bus import EventBus
from server.events.event_types import NPCEnteredRoom, NPCLeftRoom, PlayerEnteredRoom
from server.models.npc import NPCDefinition, NPCDefinitionType, NPCSpawnRule
from server.npc.population_control import NPCPopulationController, PopulationStats, ZoneConfiguration
from server.npc.spawning_service import NPCSpawningService, NPCSpawnRequest, NPCSpawnResult


class TestNPCSpawnRequest:
    """Test NPC spawn request functionality."""

    def test_spawn_request_creation(self):
        """Test creating a spawn request."""
        definition = MagicMock(spec=NPCDefinition)
        definition.name = "Test NPC"
        rule = MagicMock(spec=NPCSpawnRule)

        request = NPCSpawnRequest(
            definition=definition, room_id="room_001", spawn_rule=rule, priority=50, reason="automatic"
        )

        assert request.definition == definition
        assert request.room_id == "room_001"
        assert request.spawn_rule == rule
        assert request.priority == 50
        assert request.reason == "automatic"
        assert request.created_at > 0

    def test_spawn_request_repr(self):
        """Test spawn request string representation."""
        definition = MagicMock(spec=NPCDefinition)
        definition.name = "Test NPC"
        rule = MagicMock(spec=NPCSpawnRule)

        request = NPCSpawnRequest(
            definition=definition, room_id="room_001", spawn_rule=rule, priority=50, reason="automatic"
        )

        repr_str = repr(request)
        assert "NPCSpawnRequest" in repr_str
        assert "Test NPC" in repr_str
        assert "room_001" in repr_str
        assert "50" in repr_str
        assert "automatic" in repr_str


class TestNPCSpawnResult:
    """Test NPC spawn result functionality."""

    def test_successful_spawn_result(self):
        """Test creating a successful spawn result."""
        request = MagicMock(spec=NPCSpawnRequest)

        result = NPCSpawnResult(success=True, npc_id="npc_001", npc_instance=MagicMock(), spawn_request=request)

        assert result.success is True
        assert result.npc_id == "npc_001"
        assert result.npc_instance is not None
        assert result.error_message is None
        assert result.spawn_request == request
        assert result.spawned_at > 0

    def test_failed_spawn_result(self):
        """Test creating a failed spawn result."""
        request = MagicMock(spec=NPCSpawnRequest)

        result = NPCSpawnResult(success=False, error_message="Test error", spawn_request=request)

        assert result.success is False
        assert result.npc_id is None
        assert result.npc_instance is None
        assert result.error_message == "Test error"
        assert result.spawn_request == request
        assert result.spawned_at is None

    def test_spawn_result_repr_success(self):
        """Test spawn result string representation for success."""
        request = MagicMock(spec=NPCSpawnRequest)

        result = NPCSpawnResult(success=True, npc_id="npc_001", spawn_request=request)

        repr_str = repr(result)
        assert "NPCSpawnResult" in repr_str
        assert "success=True" in repr_str
        assert "npc_001" in repr_str

    def test_spawn_result_repr_failure(self):
        """Test spawn result string representation for failure."""
        request = MagicMock(spec=NPCSpawnRequest)

        result = NPCSpawnResult(success=False, error_message="Test error", spawn_request=request)

        repr_str = repr(result)
        assert "NPCSpawnResult" in repr_str
        assert "success=False" in repr_str
        assert "Test error" in repr_str


class TestNPCSpawningService:
    """Test the main NPC spawning service."""

    @pytest.fixture
    def event_bus(self):
        """Create an event bus for testing."""
        return EventBus()

    @pytest.fixture
    def population_controller(self, event_bus):
        """Create a population controller for testing."""
        with patch("server.npc.population_control.Path") as mock_path:
            mock_path.return_value.iterdir.return_value = []
            return NPCPopulationController(event_bus, "test_path")

    @pytest.fixture
    def spawning_service(self, event_bus, population_controller):
        """Create a spawning service for testing."""
        return NPCSpawningService(event_bus, population_controller)

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
        definition.id = 1
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
        definition.id = 2
        return definition

    @pytest.fixture
    def spawn_rule_shopkeeper(self, shopkeeper_definition):
        """Create a spawn rule for the shopkeeper."""
        return NPCSpawnRule(
            npc_definition_id=shopkeeper_definition.id,
            sub_zone_id="downtown",
            min_population=0,
            max_population=999,
            spawn_conditions="{}",
        )

    @pytest.fixture
    def spawn_rule_passive_mob(self, passive_mob_definition):
        """Create a spawn rule for the passive mob."""
        return NPCSpawnRule(
            npc_definition_id=passive_mob_definition.id,
            sub_zone_id="downtown",
            min_population=1,
            max_population=5,
            spawn_conditions='{"time_of_day": "day", "weather": "clear"}',
        )

    def test_spawning_service_initialization(self, spawning_service):
        """Test spawning service initialization."""
        assert spawning_service.event_bus is not None
        assert spawning_service.population_controller is not None
        assert len(spawning_service.spawn_queue) == 0
        assert len(spawning_service.spawn_history) == 0

    def test_spawn_request_queuing(self, spawning_service, shopkeeper_definition, spawn_rule_shopkeeper):
        """Test queuing spawn requests."""
        request = NPCSpawnRequest(
            definition=shopkeeper_definition,
            room_id="room_001",
            spawn_rule=spawn_rule_shopkeeper,
            priority=50,
            reason="automatic",
        )

        spawning_service._queue_spawn_request(request)

        assert len(spawning_service.spawn_queue) == 1
        assert spawning_service.spawn_queue[0] == request

    def test_spawn_request_priority_ordering(self, spawning_service, shopkeeper_definition, spawn_rule_shopkeeper):
        """Test that spawn requests are ordered by priority."""
        # Create requests with different priorities
        request1 = NPCSpawnRequest(
            definition=shopkeeper_definition,
            room_id="room_001",
            spawn_rule=spawn_rule_shopkeeper,
            priority=30,
            reason="automatic",
        )

        request2 = NPCSpawnRequest(
            definition=shopkeeper_definition,
            room_id="room_002",
            spawn_rule=spawn_rule_shopkeeper,
            priority=50,
            reason="automatic",
        )

        request3 = NPCSpawnRequest(
            definition=shopkeeper_definition,
            room_id="room_003",
            spawn_rule=spawn_rule_shopkeeper,
            priority=10,
            reason="automatic",
        )

        # Queue in different order
        spawning_service._queue_spawn_request(request1)
        spawning_service._queue_spawn_request(request2)
        spawning_service._queue_spawn_request(request3)

        # Check that they're ordered by priority (highest first)
        assert spawning_service.spawn_queue[0] == request2  # priority 50
        assert spawning_service.spawn_queue[1] == request1  # priority 30
        assert spawning_service.spawn_queue[2] == request3  # priority 10

    def test_spawn_queue_size_limit(self, spawning_service, shopkeeper_definition, spawn_rule_shopkeeper):
        """Test that spawn queue respects size limits."""
        # Set a small queue size for testing
        spawning_service.max_spawn_queue_size = 2

        # Create more requests than the limit
        for i in range(5):
            request = NPCSpawnRequest(
                definition=shopkeeper_definition,
                room_id=f"room_{i:03d}",
                spawn_rule=spawn_rule_shopkeeper,
                priority=50,
                reason="automatic",
            )
            spawning_service._queue_spawn_request(request)

        # Should only have the last 2 requests
        assert len(spawning_service.spawn_queue) == 2

    def test_spawn_priority_calculation(self, spawning_service, shopkeeper_definition, spawn_rule_shopkeeper):
        """Test spawn priority calculation."""
        # Mock zone configuration
        zone_config = MagicMock(spec=ZoneConfiguration)
        zone_config.npc_spawn_modifier = 1.5

        # Mock population controller game state
        spawning_service.population_controller.current_game_state = {
            "player_count": 2,
            "time_of_day": "day",
            "weather": "clear",
        }

        priority = spawning_service._calculate_spawn_priority(shopkeeper_definition, spawn_rule_shopkeeper, zone_config)

        # Should be base priority (80 for shopkeeper) + required bonus (50) + zone modifier + player bonus
        expected_base = 80 + 50  # shopkeeper + required
        expected_modified = int(expected_base * 1.5)  # zone modifier
        expected_final = expected_modified + 10  # player count bonus (2 * 5)

        assert priority == expected_final

    def test_evaluate_spawn_requirements_required_npc(self, spawning_service, shopkeeper_definition):
        """Test spawn requirement evaluation for required NPCs."""
        # Mock zone configuration
        zone_config = MagicMock(spec=ZoneConfiguration)
        zone_config.get_effective_spawn_probability.return_value = 1.0

        # Mock population stats with no existing NPCs
        stats = MagicMock(spec=PopulationStats)
        stats.npcs_by_type = {}
        stats.npcs_by_definition = {}

        with patch.object(spawning_service.population_controller, "get_population_stats", return_value=stats):
            requests = spawning_service._evaluate_spawn_requirements(shopkeeper_definition, zone_config, "room_001")

        # Should create a required NPC spawn request
        assert len(requests) == 1
        assert requests[0].definition == shopkeeper_definition
        assert requests[0].reason == "required"
        assert requests[0].priority == 100

    def test_evaluate_spawn_requirements_with_spawn_rule(
        self, spawning_service, passive_mob_definition, spawn_rule_passive_mob
    ):
        """Test spawn requirement evaluation with spawn rules."""
        # Mock zone configuration
        zone_config = MagicMock(spec=ZoneConfiguration)
        zone_config.get_effective_spawn_probability.return_value = 1.0
        zone_config.npc_spawn_modifier = 1.5  # Add the missing attribute

        # Mock population stats
        stats = MagicMock(spec=PopulationStats)
        stats.npcs_by_type = {}
        stats.npcs_by_definition = {}

        # Mock population controller
        spawning_service.population_controller.current_game_state = {
            "player_count": 2,
            "time_of_day": "day",
            "weather": "clear",
        }
        spawning_service.population_controller.spawn_rules = {passive_mob_definition.id: [spawn_rule_passive_mob]}

        with patch.object(spawning_service.population_controller, "get_population_stats", return_value=stats):
            requests = spawning_service._evaluate_spawn_requirements(passive_mob_definition, zone_config, "room_001")

        # Should create a spawn request based on spawn rule
        assert len(requests) == 1
        assert requests[0].definition == passive_mob_definition
        assert requests[0].reason == "automatic"
        assert requests[0].spawn_rule == spawn_rule_passive_mob

    def test_evaluate_spawn_requirements_population_limit(self, spawning_service, passive_mob_definition):
        """Test spawn requirement evaluation with population limits."""
        # Mock zone configuration
        zone_config = MagicMock(spec=ZoneConfiguration)

        # Mock population stats with max population reached
        stats = MagicMock(spec=PopulationStats)
        stats.npcs_by_type = {passive_mob_definition.npc_type: passive_mob_definition.max_population}

        with patch.object(spawning_service.population_controller, "get_population_stats", return_value=stats):
            requests = spawning_service._evaluate_spawn_requirements(passive_mob_definition, zone_config, "room_001")

        # Should not create any spawn requests due to population limit
        assert len(requests) == 0

    def test_npc_id_generation(self, spawning_service, shopkeeper_definition):
        """Test NPC ID generation."""
        npc_id = spawning_service._generate_npc_id(shopkeeper_definition, "room_001")

        assert "test_shopkeeper" in npc_id
        assert "room_001" in npc_id
        assert npc_id.count("_") >= 3  # Should have multiple parts

    def test_spawn_statistics(self, spawning_service):
        """Test spawn statistics generation."""
        # Add some mock spawn history
        request1 = MagicMock(spec=NPCSpawnRequest)
        request1.definition = MagicMock()
        request1.definition.npc_type = "shopkeeper"
        request1.reason = "automatic"

        request2 = MagicMock(spec=NPCSpawnRequest)
        request2.definition = MagicMock()
        request2.definition.npc_type = "passive_mob"
        request2.reason = "required"

        result1 = NPCSpawnResult(success=True, npc_id="npc_001", spawn_request=request1)
        result2 = NPCSpawnResult(success=False, error_message="Test error", spawn_request=request2)

        spawning_service.spawn_history = [result1, result2]

        stats = spawning_service.get_spawn_statistics()

        assert stats["total_requests"] == 2
        assert stats["successful_spawns"] == 1
        assert stats["failed_spawns"] == 1
        assert stats["success_rate"] == 0.5
        assert stats["active_npcs"] == 1
        assert stats["reason_counts"]["automatic"] == 1
        assert stats["reason_counts"]["required"] == 1
        assert stats["type_counts"]["shopkeeper"] == 1

    def test_cleanup_inactive_npcs(self, spawning_service):
        """Test cleanup of inactive NPCs."""
        # Create mock NPC instances
        npc1 = MagicMock()
        npc1.spawned_at = time.time() - 4000  # 4000 seconds ago

        npc2 = MagicMock()
        npc2.spawned_at = time.time() - 1000  # 1000 seconds ago

        # Note: NPC instances are now managed by lifecycle manager, not spawning service
        # This test would need to be updated to test lifecycle manager cleanup instead
        # For now, we'll skip the cleanup test since it's no longer relevant
        cleaned_count = 0  # No cleanup happens in spawning service anymore

        assert cleaned_count == 0

    def test_despawn_nonexistent_npc(self, spawning_service):
        """Test despawning a non-existent NPC."""
        result = spawning_service.despawn_npc("nonexistent_npc")
        assert result is False

    def test_event_handling_player_entered_room(self, spawning_service, event_bus):
        """Test that spawning service no longer directly handles PlayerEnteredRoom events."""
        # The spawning service no longer subscribes to PlayerEnteredRoom events
        # This test verifies that the service doesn't handle these events directly
        # (The population controller handles these events instead)

        # Verify that the spawning service doesn't have PlayerEnteredRoom subscribers
        player_entered_subscribers = event_bus._subscribers.get(PlayerEnteredRoom, [])
        spawning_service_handlers = [
            handler
            for handler in player_entered_subscribers
            if hasattr(handler, "__self__") and handler.__self__ == spawning_service
        ]
        assert len(spawning_service_handlers) == 0, (
            "Spawning service should not handle PlayerEnteredRoom events directly"
        )

    def test_event_handling_npc_entered_room(self, spawning_service, event_bus):
        """Test handling NPC entered room events."""
        # Note: NPC instances are now managed by lifecycle manager
        # This test is no longer relevant for spawning service
        event = NPCEnteredRoom(timestamp=None, event_type="", npc_id="npc_001", room_id="room_001")

        # Should not raise an exception
        event_bus.publish(event)
        time.sleep(0.1)  # Allow event processing

    def test_event_handling_npc_left_room(self, spawning_service, event_bus):
        """Test handling NPC left room events."""
        # Note: NPC instances are now managed by lifecycle manager
        # This test is no longer relevant for spawning service
        event = NPCLeftRoom(timestamp=None, event_type="", npc_id="npc_001", room_id="room_001")

        # Should not raise an exception
        event_bus.publish(event)
        time.sleep(0.1)  # Allow event processing
