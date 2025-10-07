"""
Tests for NPC lifecycle management system.

This module tests the NPC lifecycle management including spawning, despawning,
respawning, and state tracking throughout an NPC's existence in the game world.

As documented in the Cultes des Goules, proper lifecycle management is essential
for maintaining the delicate balance between the mundane and the eldritch forces
that lurk in the shadows of our world.
"""

import asyncio
import time
from unittest.mock import MagicMock, patch

import pytest

from server.events.event_bus import EventBus
from server.events.event_types import NPCEnteredRoom, NPCLeftRoom
from server.models.npc import NPCDefinition, NPCDefinitionType
from server.npc.lifecycle_manager import (
    NPCLifecycleEvent,
    NPCLifecycleManager,
    NPCLifecycleRecord,
    NPCLifecycleState,
)
from server.npc.population_control import NPCPopulationController
from server.npc.spawning_service import NPCSpawningService


class TestNPCLifecycleRecord:
    """Test NPC lifecycle record functionality."""

    def test_lifecycle_record_creation(self):
        """Test creating a lifecycle record."""
        definition = MagicMock(spec=NPCDefinition)
        definition.name = "Test NPC"
        definition.npc_type = "shopkeeper"

        record = NPCLifecycleRecord("npc_001", definition)

        assert record.npc_id == "npc_001"
        assert record.definition == definition
        assert record.current_state == NPCLifecycleState.SPAWNING
        assert record.created_at > 0
        assert record.last_updated > 0
        assert len(record.events) == 0
        assert record.spawn_count == 0
        assert record.despawn_count == 0
        assert record.total_active_time == 0.0
        assert record.error_count == 0
        assert record.last_error is None

    def test_add_event(self):
        """Test adding events to lifecycle record."""
        definition = MagicMock(spec=NPCDefinition)
        record = NPCLifecycleRecord("npc_001", definition)

        record.add_event(NPCLifecycleEvent.SPAWNED, {"room_id": "room_001"})

        assert len(record.events) == 1
        event = record.events[0]
        assert event["event_type"] == NPCLifecycleEvent.SPAWNED
        assert event["details"]["room_id"] == "room_001"
        assert event["timestamp"] > 0
        assert record.spawn_count == 1

    def test_change_state(self):
        """Test changing lifecycle state."""
        definition = MagicMock(spec=NPCDefinition)
        record = NPCLifecycleRecord("npc_001", definition)

        record.change_state(NPCLifecycleState.ACTIVE, "entered room")

        assert record.current_state == NPCLifecycleState.ACTIVE
        assert len(record.events) == 1
        event = record.events[0]
        assert event["event_type"] == NPCLifecycleEvent.ACTIVATED
        assert event["details"]["new_state"] == NPCLifecycleState.ACTIVE
        assert event["details"]["reason"] == "entered room"

    def test_get_statistics(self):
        """Test getting lifecycle statistics."""
        definition = MagicMock(spec=NPCDefinition)
        definition.name = "Test NPC"
        definition.npc_type = "shopkeeper"

        record = NPCLifecycleRecord("npc_001", definition)
        record.add_event(NPCLifecycleEvent.SPAWNED)
        record.add_event(NPCLifecycleEvent.DESPAWNED)
        record.add_event(NPCLifecycleEvent.ERROR_OCCURRED, {"error": "Test error"})

        stats = record.get_statistics()

        assert stats["npc_id"] == "npc_001"
        assert stats["definition_name"] == "Test NPC"
        assert stats["npc_type"] == "shopkeeper"
        assert stats["current_state"] == NPCLifecycleState.SPAWNING
        assert stats["spawn_count"] == 1
        assert stats["despawn_count"] == 1
        assert stats["error_count"] == 1
        assert stats["last_error"]["error"] == "Test error"
        assert stats["events_count"] == 3
        assert stats["age_seconds"] >= 0  # Allow for very fast test execution


class TestNPCLifecycleManager:
    """Test the main NPC lifecycle manager."""

    @pytest.fixture
    def event_bus(self):
        """Create an event bus for testing."""
        return EventBus()

    @pytest.fixture
    def population_controller(self, event_bus):
        """Create a population controller for testing."""
        with patch("server.npc.population_control.Path") as mock_path:
            mock_path.return_value.iterdir.return_value = []
            return NPCPopulationController(event_bus, spawning_service=None, rooms_data_path="test_path")

    @pytest.fixture
    def spawning_service(self, event_bus, population_controller):
        """Create a spawning service for testing."""
        spawning_service = NPCSpawningService(event_bus, population_controller)
        # Set the spawning service on the population controller
        population_controller.spawning_service = spawning_service
        # Ensure the spawning service uses the same event bus as the lifecycle manager
        spawning_service.event_bus = event_bus
        return spawning_service

    @pytest.fixture
    def lifecycle_manager(self, event_bus, population_controller, spawning_service):
        """Create a lifecycle manager for testing."""
        return NPCLifecycleManager(event_bus, population_controller, spawning_service)

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

    def test_lifecycle_manager_initialization(self, lifecycle_manager):
        """Test lifecycle manager initialization."""
        assert lifecycle_manager.event_bus is not None
        assert lifecycle_manager.population_controller is not None
        assert lifecycle_manager.spawning_service is not None
        assert len(lifecycle_manager.lifecycle_records) == 0
        assert len(lifecycle_manager.active_npcs) == 0
        assert len(lifecycle_manager.respawn_queue) == 0

    @pytest.mark.asyncio
    async def test_spawn_npc_success(self, lifecycle_manager, shopkeeper_definition):
        """Test successful NPC spawning."""
        with patch.object(lifecycle_manager, "_can_spawn_npc", return_value=True):
            with patch.object(lifecycle_manager.spawning_service, "_create_npc_instance") as mock_create:
                mock_npc = MagicMock()
                mock_npc.room_id = "room_001"
                mock_create.return_value = mock_npc

                npc_id = lifecycle_manager.spawn_npc(shopkeeper_definition, "room_001", "test")

                # Allow time for the NPCEnteredRoom event to be processed and state to transition
                await asyncio.sleep(0.1)

                assert npc_id is not None
                assert npc_id in lifecycle_manager.lifecycle_records
                assert npc_id in lifecycle_manager.active_npcs
                assert lifecycle_manager.lifecycle_records[npc_id].current_state == NPCLifecycleState.ACTIVE

    def test_spawn_npc_failure(self, lifecycle_manager, shopkeeper_definition):
        """Test NPC spawning failure."""
        with patch.object(lifecycle_manager, "_can_spawn_npc", return_value=False):
            npc_id = lifecycle_manager.spawn_npc(shopkeeper_definition, "room_001", "test")

            assert npc_id is None

    def test_despawn_npc_success(self, lifecycle_manager, shopkeeper_definition):
        """Test successful NPC despawning."""
        # First spawn an NPC
        with patch.object(lifecycle_manager, "_can_spawn_npc", return_value=True):
            with patch.object(lifecycle_manager.spawning_service, "_create_npc_instance") as mock_create:
                mock_npc = MagicMock()
                mock_npc.room_id = "room_001"
                mock_create.return_value = mock_npc

                npc_id = lifecycle_manager.spawn_npc(shopkeeper_definition, "room_001", "test")
                assert npc_id is not None

                # Now despawn it
                result = lifecycle_manager.despawn_npc(npc_id, "test")

                assert result is True
                assert npc_id not in lifecycle_manager.active_npcs
                assert lifecycle_manager.lifecycle_records[npc_id].current_state == NPCLifecycleState.DESPAWNED

    def test_despawn_nonexistent_npc(self, lifecycle_manager):
        """Test despawning a non-existent NPC."""
        result = lifecycle_manager.despawn_npc("nonexistent_npc", "test")
        assert result is False

    def test_respawn_npc(self, lifecycle_manager, shopkeeper_definition):
        """Test scheduling NPC respawn."""
        # Create a lifecycle record first
        record = NPCLifecycleRecord("npc_001", shopkeeper_definition)
        lifecycle_manager.lifecycle_records["npc_001"] = record

        result = lifecycle_manager.respawn_npc("npc_001", delay=1.0, reason="test")

        assert result is True
        assert "npc_001" in lifecycle_manager.respawn_queue
        respawn_data = lifecycle_manager.respawn_queue["npc_001"]
        assert respawn_data["definition"] == shopkeeper_definition
        assert respawn_data["reason"] == "test"
        assert respawn_data["attempts"] == 0

    def test_respawn_nonexistent_npc(self, lifecycle_manager):
        """Test respawning a non-existent NPC."""
        result = lifecycle_manager.respawn_npc("nonexistent_npc", reason="test")
        assert result is False

    def test_process_respawn_queue(self, lifecycle_manager, shopkeeper_definition):
        """Test processing the respawn queue."""
        # Create a lifecycle record
        record = NPCLifecycleRecord("npc_001", shopkeeper_definition)
        lifecycle_manager.lifecycle_records["npc_001"] = record

        # Schedule a respawn for immediate execution
        respawn_data = {
            "npc_id": "npc_001",
            "definition": shopkeeper_definition,
            "room_id": "room_001",
            "scheduled_time": time.time() - 1,  # Past time
            "reason": "test",
            "attempts": 0,
        }
        lifecycle_manager.respawn_queue["npc_001"] = respawn_data

        with patch.object(lifecycle_manager, "_can_spawn_npc", return_value=True):
            with patch.object(lifecycle_manager.spawning_service, "_create_npc_instance") as mock_create:
                mock_npc = MagicMock()
                mock_npc.room_id = "room_001"
                mock_create.return_value = mock_npc

                respawned_count = lifecycle_manager.process_respawn_queue()

                assert respawned_count == 1
                assert "npc_001" not in lifecycle_manager.respawn_queue

    def test_get_npc_lifecycle_record(self, lifecycle_manager, shopkeeper_definition):
        """Test getting NPC lifecycle record."""
        record = NPCLifecycleRecord("npc_001", shopkeeper_definition)
        lifecycle_manager.lifecycle_records["npc_001"] = record

        retrieved_record = lifecycle_manager.get_npc_lifecycle_record("npc_001")
        assert retrieved_record == record

        # Test non-existent NPC
        retrieved_record = lifecycle_manager.get_npc_lifecycle_record("nonexistent")
        assert retrieved_record is None

    def test_get_lifecycle_statistics(self, lifecycle_manager, shopkeeper_definition):
        """Test getting lifecycle statistics."""
        # Create some lifecycle records
        record1 = NPCLifecycleRecord("npc_001", shopkeeper_definition)
        record1.add_event(NPCLifecycleEvent.SPAWNED)
        record1.add_event(NPCLifecycleEvent.DESPAWNED)
        record1.change_state(NPCLifecycleState.ACTIVE)

        record2 = NPCLifecycleRecord("npc_002", shopkeeper_definition)
        record2.add_event(NPCLifecycleEvent.ERROR_OCCURRED, {"error": "Test error"})
        record2.change_state(NPCLifecycleState.ERROR)

        lifecycle_manager.lifecycle_records["npc_001"] = record1
        lifecycle_manager.lifecycle_records["npc_002"] = record2
        lifecycle_manager.active_npcs["npc_001"] = MagicMock()

        stats = lifecycle_manager.get_lifecycle_statistics()

        assert stats["total_npcs"] == 2
        assert stats["active_npcs"] == 1
        assert stats["respawn_queue_size"] == 0
        assert stats["total_spawns"] == 1
        assert stats["total_despawns"] == 1
        assert stats["total_errors"] == 1
        assert stats["state_counts"][NPCLifecycleState.ACTIVE] == 1
        assert stats["state_counts"][NPCLifecycleState.ERROR] == 1
        assert stats["type_counts"]["shopkeeper"] == 2

    def test_cleanup_old_records(self, lifecycle_manager, shopkeeper_definition):
        """Test cleaning up old lifecycle records."""
        # Create old records
        old_record = NPCLifecycleRecord("npc_001", shopkeeper_definition)
        old_record.created_at = time.time() - 90000  # 25 hours ago
        old_record.change_state(NPCLifecycleState.DESPAWNED)

        new_record = NPCLifecycleRecord("npc_002", shopkeeper_definition)
        new_record.created_at = time.time() - 3600  # 1 hour ago
        new_record.change_state(NPCLifecycleState.ACTIVE)

        lifecycle_manager.lifecycle_records["npc_001"] = old_record
        lifecycle_manager.lifecycle_records["npc_002"] = new_record

        cleaned_count = lifecycle_manager.cleanup_old_records(max_age_seconds=86400)  # 24 hours

        assert cleaned_count == 1
        assert "npc_001" not in lifecycle_manager.lifecycle_records
        assert "npc_002" in lifecycle_manager.lifecycle_records

    def test_periodic_maintenance(self, lifecycle_manager, shopkeeper_definition):
        """Test periodic maintenance tasks."""
        # Create a respawn queue entry
        respawn_data = {
            "npc_id": "npc_001",
            "definition": shopkeeper_definition,
            "room_id": "room_001",
            "scheduled_time": time.time() - 1,
            "reason": "test",
            "attempts": 0,
        }
        lifecycle_manager.respawn_queue["npc_001"] = respawn_data

        with patch.object(lifecycle_manager, "_can_spawn_npc", return_value=True):
            with patch.object(lifecycle_manager.spawning_service, "_create_npc_instance") as mock_create:
                mock_npc = MagicMock()
                mock_npc.room_id = "room_001"
                mock_create.return_value = mock_npc

                results = lifecycle_manager.periodic_maintenance()

                assert "respawned_npcs" in results
                assert results["respawned_npcs"] == 1

    @pytest.mark.asyncio
    async def test_event_handling_npc_entered_room(self, lifecycle_manager, shopkeeper_definition):
        """Test handling NPC entered room events."""
        # Create a lifecycle record in spawning state
        record = NPCLifecycleRecord("npc_001", shopkeeper_definition)
        lifecycle_manager.lifecycle_records["npc_001"] = record

        event = NPCEnteredRoom(timestamp=None, event_type="", npc_id="npc_001", room_id="room_001")

        # Use the lifecycle manager's event bus
        lifecycle_manager.event_bus.publish(event)
        await asyncio.sleep(0.1)  # Allow async event processing

        assert record.current_state == NPCLifecycleState.ACTIVE
        assert len(record.events) == 2  # Both ACTIVATED and SPAWNED events
        # Check that we have both events
        event_types = [event["event_type"] for event in record.events]
        assert NPCLifecycleEvent.ACTIVATED in event_types
        assert NPCLifecycleEvent.SPAWNED in event_types

    @pytest.mark.asyncio
    async def test_event_handling_npc_left_room(self, lifecycle_manager, shopkeeper_definition):
        """Test handling NPC left room events."""
        # Create a lifecycle record
        record = NPCLifecycleRecord("npc_001", shopkeeper_definition)
        lifecycle_manager.lifecycle_records["npc_001"] = record

        event = NPCLeftRoom(timestamp=None, event_type="", npc_id="npc_001", room_id="room_001")

        # Use the lifecycle manager's event bus
        lifecycle_manager.event_bus.publish(event)
        await asyncio.sleep(0.1)  # Allow async event processing

        assert len(record.events) == 1
        assert record.events[0]["event_type"] == NPCLifecycleEvent.DEACTIVATED

    def test_can_spawn_npc(self, lifecycle_manager, shopkeeper_definition):
        """Test NPC spawn eligibility checking."""
        # Mock population stats
        mock_stats = MagicMock()
        mock_stats.npcs_by_type = {}

        with patch.object(lifecycle_manager.population_controller, "get_population_stats", return_value=mock_stats):
            can_spawn = lifecycle_manager._can_spawn_npc(shopkeeper_definition, "room_001")
            assert can_spawn is True

        # Test with population limit reached
        mock_stats.npcs_by_type = {shopkeeper_definition.npc_type: shopkeeper_definition.max_population}
        with patch.object(lifecycle_manager.population_controller, "get_population_stats", return_value=mock_stats):
            can_spawn = lifecycle_manager._can_spawn_npc(shopkeeper_definition, "room_001")
            assert can_spawn is False

    def test_generate_npc_id(self, lifecycle_manager, shopkeeper_definition):
        """Test NPC ID generation."""
        npc_id = lifecycle_manager._generate_npc_id(shopkeeper_definition, "room_001")

        assert "test_shopkeeper" in npc_id
        assert "room_001" in npc_id
        assert npc_id.count("_") >= 3  # Should have multiple parts
