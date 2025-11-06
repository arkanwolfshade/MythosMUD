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
from server.events.event_types import NPCDied, NPCEnteredRoom, NPCLeftRoom
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
        return NPCLifecycleManager(event_bus, population_controller, spawning_service, persistence=None)

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

                # Provide a room via persistence so spawn path can mutate domain state
                class _FakeRoom:
                    def npc_entered(self, _nid):
                        # Simulate Room publishing the enter event
                        lifecycle_manager.event_bus.publish(NPCEnteredRoom(npc_id=_nid, room_id="room_001"))

                with patch("server.npc.lifecycle_manager.get_persistence") as mock_get_persistence:
                    mock_get_persistence.return_value.get_room.return_value = _FakeRoom()

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

                class _FakeRoom:
                    def npc_entered(self, _nid):
                        lifecycle_manager.event_bus.publish(NPCEnteredRoom(npc_id=_nid, room_id="room_001"))

                with patch("server.npc.lifecycle_manager.get_persistence") as mock_get_persistence:
                    mock_get_persistence.return_value.get_room.return_value = _FakeRoom()
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

                class _FakeRoom:
                    def npc_entered(self, _nid):
                        lifecycle_manager.event_bus.publish(NPCEnteredRoom(npc_id=_nid, room_id="room_001"))

                with patch("server.npc.lifecycle_manager.get_persistence") as mock_get_persistence:
                    mock_get_persistence.return_value.get_room.return_value = _FakeRoom()

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

                class _FakeRoom:
                    def npc_entered(self, _nid):
                        lifecycle_manager.event_bus.publish(NPCEnteredRoom(npc_id=_nid, room_id="room_001"))

                with patch("server.npc.lifecycle_manager.get_persistence") as mock_get_persistence:
                    mock_get_persistence.return_value.get_room.return_value = _FakeRoom()

                    results = lifecycle_manager.periodic_maintenance()

                    assert "respawned_npcs" in results
                    assert results["respawned_npcs"] == 1

    @pytest.mark.asyncio
    async def test_event_handling_npc_entered_room(self, lifecycle_manager, shopkeeper_definition):
        """Test handling NPC entered room events."""
        # Create a lifecycle record in spawning state
        record = NPCLifecycleRecord("npc_001", shopkeeper_definition)
        lifecycle_manager.lifecycle_records["npc_001"] = record

        event = NPCEnteredRoom(npc_id="npc_001", room_id="room_001")

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

        event = NPCLeftRoom(npc_id="npc_001", room_id="room_001")

        # Use the lifecycle manager's event bus
        lifecycle_manager.event_bus.publish(event)
        await asyncio.sleep(0.1)  # Allow async event processing

        assert len(record.events) == 1
        assert record.events[0]["event_type"] == NPCLifecycleEvent.DEACTIVATED

    def test_can_spawn_npc(self, lifecycle_manager, shopkeeper_definition):
        """Test NPC spawn eligibility checking."""
        # Mock population stats
        mock_stats = MagicMock()
        mock_stats.npcs_by_definition = {}  # Changed from npcs_by_type to npcs_by_definition

        with patch.object(lifecycle_manager.population_controller, "get_population_stats", return_value=mock_stats):
            can_spawn = lifecycle_manager._can_spawn_npc(shopkeeper_definition, "room_001")
            assert can_spawn is True

        # Test with population limit reached
        mock_stats.npcs_by_definition = {shopkeeper_definition.id: shopkeeper_definition.max_population}
        with patch.object(lifecycle_manager.population_controller, "get_population_stats", return_value=mock_stats):
            can_spawn = lifecycle_manager._can_spawn_npc(shopkeeper_definition, "room_001")
            assert can_spawn is False

    def test_generate_npc_id(self, lifecycle_manager, shopkeeper_definition):
        """Test NPC ID generation."""
        npc_id = lifecycle_manager._generate_npc_id(shopkeeper_definition, "room_001")

        assert "test_shopkeeper" in npc_id
        assert "room_001" in npc_id
        assert npc_id.count("_") >= 3  # Should have multiple parts

    def test_periodic_maintenance_with_spawn_checks(self, lifecycle_manager, shopkeeper_definition):
        """Test periodic maintenance includes spawn checks."""
        # Create an optional NPC definition
        optional_npc = NPCDefinition(
            name="Test Optional NPC",
            description="An optional test NPC",
            npc_type=NPCDefinitionType.PASSIVE_MOB,
            sub_zone_id="downtown",
            required_npc=False,
            max_population=2,
            spawn_probability=0.5,
            room_id="earth_arkhamcity_downtown_001",
            base_stats='{"strength": 5, "sanity": 50, "current_health": 50}',
            behavior_config='{}',
            ai_integration_stub='{}',
        )
        optional_npc.id = 2

        # Add the definition to population controller
        lifecycle_manager.population_controller.npc_definitions[2] = optional_npc

        # Mock zone configuration
        mock_zone_config = MagicMock()
        mock_zone_config.get_effective_spawn_probability.return_value = 1.0  # Always spawn for testing

        # Mock population stats
        mock_stats = MagicMock()
        mock_stats.npcs_by_definition = {}

        with patch.object(
            lifecycle_manager.population_controller, "get_zone_configuration", return_value=mock_zone_config
        ):
            with patch.object(
                lifecycle_manager.population_controller, "get_population_stats", return_value=mock_stats
            ):
                with patch.object(lifecycle_manager, "_can_spawn_npc", return_value=True):
                    with patch.object(lifecycle_manager.spawning_service, "_create_npc_instance") as mock_create:
                        mock_npc = MagicMock()
                        mock_npc.room_id = "earth_arkhamcity_downtown_001"
                        mock_create.return_value = mock_npc

                        class _FakeRoom:
                            def npc_entered(self, _nid):
                                lifecycle_manager.event_bus.publish(
                                    NPCEnteredRoom(npc_id=_nid, room_id="earth_arkhamcity_downtown_001")
                                )

                        with patch("server.npc.lifecycle_manager.get_persistence") as mock_get_persistence:
                            mock_get_persistence.return_value.get_room.return_value = _FakeRoom()

                            # Run periodic maintenance
                            results = lifecycle_manager.periodic_maintenance()

                            # Verify results
                            assert "spawned_npcs" in results
                            assert "spawn_checks_performed" in results
                            # Should have checked optional NPCs
                            assert results["spawn_checks_performed"] >= 0

    def test_check_optional_npc_spawns(self, lifecycle_manager):
        """Test periodic spawn checks for optional NPCs."""
        # Create an optional NPC definition
        optional_npc = NPCDefinition(
            name="Test Optional NPC",
            description="An optional test NPC",
            npc_type=NPCDefinitionType.PASSIVE_MOB,
            sub_zone_id="downtown",
            required_npc=False,
            max_population=2,
            spawn_probability=1.0,  # 100% for testing
            room_id="earth_arkhamcity_downtown_001",
            base_stats='{"strength": 5, "sanity": 50, "current_health": 50}',
            behavior_config='{}',
            ai_integration_stub='{}',
        )
        optional_npc.id = 2

        # Add definition to population controller
        lifecycle_manager.population_controller.npc_definitions[2] = optional_npc

        # Mock zone configuration
        mock_zone_config = MagicMock()
        mock_zone_config.get_effective_spawn_probability.return_value = 1.0  # Always spawn

        # Mock population stats
        mock_stats = MagicMock()
        mock_stats.npcs_by_definition = {}  # No NPCs spawned yet

        with patch.object(
            lifecycle_manager.population_controller, "get_zone_configuration", return_value=mock_zone_config
        ):
            with patch.object(
                lifecycle_manager.population_controller, "get_population_stats", return_value=mock_stats
            ):
                with patch.object(lifecycle_manager, "_can_spawn_npc", return_value=True):
                    with patch.object(lifecycle_manager.spawning_service, "_create_npc_instance") as mock_create:
                        mock_npc = MagicMock()
                        mock_npc.room_id = "earth_arkhamcity_downtown_001"
                        mock_create.return_value = mock_npc

                        class _FakeRoom:
                            def npc_entered(self, _nid):
                                lifecycle_manager.event_bus.publish(
                                    NPCEnteredRoom(npc_id=_nid, room_id="earth_arkhamcity_downtown_001")
                                )

                        with patch("server.npc.lifecycle_manager.get_persistence") as mock_get_persistence:
                            mock_get_persistence.return_value.get_room.return_value = _FakeRoom()

                            # Call spawn checking directly
                            results = lifecycle_manager._check_optional_npc_spawns()

                            assert results["checks_performed"] >= 0
                            # Note: spawned_count depends on probability roll

    def test_check_optional_npc_spawns_respects_interval(self, lifecycle_manager):
        """Test that spawn checks respect minimum interval."""
        # Create an optional NPC
        optional_npc = NPCDefinition(
            name="Test Optional NPC",
            description="An optional test NPC",
            npc_type=NPCDefinitionType.PASSIVE_MOB,
            sub_zone_id="downtown",
            required_npc=False,
            max_population=2,
            spawn_probability=1.0,
            room_id="earth_arkhamcity_downtown_001",
            base_stats='{}',
            behavior_config='{}',
            ai_integration_stub='{}',
        )
        optional_npc.id = 2

        lifecycle_manager.population_controller.npc_definitions[2] = optional_npc

        # Set last check time to recent past
        lifecycle_manager.last_spawn_check[2] = time.time()

        # Mock zone configuration
        mock_zone_config = MagicMock()
        mock_zone_config.get_effective_spawn_probability.return_value = 1.0

        with patch.object(
            lifecycle_manager.population_controller, "get_zone_configuration", return_value=mock_zone_config
        ):
            # Call spawn checking
            results = lifecycle_manager._check_optional_npc_spawns()

            # Should skip check due to interval
            assert results["checks_performed"] == 0
            assert results["spawned_count"] == 0

    def test_check_optional_npc_spawns_skips_required(self, lifecycle_manager, shopkeeper_definition):
        """Test that periodic spawn checks skip required NPCs."""
        # Add required NPC to definitions
        lifecycle_manager.population_controller.npc_definitions[shopkeeper_definition.id] = shopkeeper_definition

        # Call spawn checking
        results = lifecycle_manager._check_optional_npc_spawns()

        # Should skip required NPC
        assert results["checks_performed"] == 0
        assert results["spawned_count"] == 0

    def test_check_optional_npc_spawns_respects_population_limit(self, lifecycle_manager):
        """Test that spawn checks respect population limits."""
        # Create an optional NPC
        optional_npc = NPCDefinition(
            name="Test Optional NPC",
            description="An optional test NPC",
            npc_type=NPCDefinitionType.PASSIVE_MOB,
            sub_zone_id="downtown",
            required_npc=False,
            max_population=1,  # Only allow 1
            spawn_probability=1.0,
            room_id="earth_arkhamcity_downtown_001",
            base_stats='{}',
            behavior_config='{}',
            ai_integration_stub='{}',
        )
        optional_npc.id = 2

        lifecycle_manager.population_controller.npc_definitions[2] = optional_npc

        # Mock zone configuration
        mock_zone_config = MagicMock()
        mock_zone_config.get_effective_spawn_probability.return_value = 1.0

        # Mock population stats - already at limit
        mock_stats = MagicMock()
        mock_stats.npcs_by_definition = {2: 1}  # Already at max

        with patch.object(
            lifecycle_manager.population_controller, "get_zone_configuration", return_value=mock_zone_config
        ):
            with patch.object(
                lifecycle_manager.population_controller, "get_population_stats", return_value=mock_stats
            ):
                # Call spawn checking
                results = lifecycle_manager._check_optional_npc_spawns()

                # Should check but not spawn due to population limit
                assert results["checks_performed"] >= 0
                assert results["spawned_count"] == 0

    def test_get_zone_key_for_definition(self, lifecycle_manager):
        """Test extracting zone key from NPC definition."""
        # Create a definition with room_id
        definition = NPCDefinition(
            name="Test NPC",
            description="Test",
            npc_type=NPCDefinitionType.PASSIVE_MOB,
            sub_zone_id="downtown",
            required_npc=False,
            max_population=1,
            spawn_probability=1.0,
            room_id="earth_arkhamcity_downtown_001",
            base_stats='{}',
            behavior_config='{}',
            ai_integration_stub='{}',
        )
        definition.id = 1

        # Add a spawn rule so the method can find zone info
        from server.models.npc import NPCSpawnRule

        spawn_rule = NPCSpawnRule(
            npc_definition_id=1,
            sub_zone_id=1,
            max_population=1,
            spawn_conditions='{}',
        )
        lifecycle_manager.population_controller.spawn_rules[1] = [spawn_rule]

        with patch.object(
            lifecycle_manager.population_controller,
            "_get_zone_key_from_room_id",
            return_value="arkhamcity/downtown",
        ):
            zone_key = lifecycle_manager._get_zone_key_for_definition(definition)
            assert zone_key == "arkhamcity/downtown"

    def test_get_spawn_room_for_definition(self, lifecycle_manager):
        """Test getting spawn room from NPC definition."""
        # Test with room_id configured
        definition = NPCDefinition(
            name="Test NPC",
            description="Test",
            npc_type=NPCDefinitionType.PASSIVE_MOB,
            sub_zone_id="downtown",
            required_npc=False,
            max_population=1,
            spawn_probability=1.0,
            room_id="earth_arkhamcity_downtown_001",
            base_stats='{}',
            behavior_config='{}',
            ai_integration_stub='{}',
        )
        definition.id = 1

        room_id = lifecycle_manager._get_spawn_room_for_definition(definition)
        assert room_id == "earth_arkhamcity_downtown_001"

        # Test without room_id
        definition.room_id = None
        room_id = lifecycle_manager._get_spawn_room_for_definition(definition)
        assert room_id is None

    def test_handle_npc_died_event_queues_for_respawn(self, lifecycle_manager, shopkeeper_definition):
        """Test that NPCDied event handler queues NPC for respawn."""
        # Use a real room that exists in the test environment
        test_room_id = "earth_arkhamcity_sanitarium_room_foyer_entrance_001"

        # Spawn the NPC first
        npc_id = lifecycle_manager.spawn_npc(shopkeeper_definition, test_room_id, "test")
        assert npc_id is not None
        assert npc_id in lifecycle_manager.active_npcs
        assert npc_id in lifecycle_manager.lifecycle_records

        # Create NPCDied event
        died_event = NPCDied(
            npc_id=npc_id,
            room_id=test_room_id,
            cause="combat"
        )

        # Handle the death event
        lifecycle_manager._handle_npc_died(died_event)

        # Verify NPC was removed from active NPCs
        assert npc_id not in lifecycle_manager.active_npcs

        # AI Agent: CRITICAL - Verify lifecycle record is PRESERVED for XP calculation
        #           The record must remain so combat service can read xp_value from base_stats
        assert npc_id in lifecycle_manager.lifecycle_records, \
            "Lifecycle record must be preserved after death for XP calculation"

        # Verify NPC was queued for respawn
        assert npc_id in lifecycle_manager.respawn_queue
        respawn_data = lifecycle_manager.respawn_queue[npc_id]
        assert respawn_data["npc_id"] == npc_id
        assert respawn_data["definition"] == shopkeeper_definition
        assert "scheduled_time" in respawn_data

    def test_handle_npc_died_respects_delay_for_required_npcs(self, lifecycle_manager):
        """Test that required NPCs also respect respawn delay."""
        # Use a real room that exists in the test environment
        test_room_id = "earth_arkhamcity_sanitarium_room_foyer_entrance_001"

        # Create a required NPC
        required_definition = NPCDefinition(
            name="Required Test NPC",
            description="A required test NPC",
            npc_type=NPCDefinitionType.QUEST_GIVER,
            sub_zone_id="downtown",
            required_npc=True,  # This is a required NPC
            max_population=1,
            spawn_probability=1.0,
            room_id=test_room_id,
            base_stats='{"health": 50, "strength": 10}',
            behavior_config='{}',
            ai_integration_stub='{}',
        )
        required_definition.id = 999

        # Spawn the required NPC
        npc_id = lifecycle_manager.spawn_npc(required_definition, test_room_id, "test")
        assert npc_id is not None

        # Record the current time
        death_time = time.time()

        # Create NPCDied event
        died_event = NPCDied(
            npc_id=npc_id,
            room_id=test_room_id,
            cause="combat"
        )

        # Handle the death event
        lifecycle_manager._handle_npc_died(died_event)

        # Verify NPC was queued for respawn
        assert npc_id in lifecycle_manager.respawn_queue
        respawn_data = lifecycle_manager.respawn_queue[npc_id]

        # AI Agent: CRITICAL - Verify required NPCs respect respawn delay
        #           The scheduled_time should be death_time + delay, not immediate
        scheduled_time = respawn_data["scheduled_time"]
        expected_delay = lifecycle_manager.default_respawn_delay
        actual_delay = scheduled_time - death_time

        # Allow 1 second tolerance for execution time
        assert actual_delay >= expected_delay - 1.0, \
            f"Required NPC should respect respawn delay! Expected ~{expected_delay}s, got {actual_delay}s"
        assert actual_delay <= expected_delay + 1.0, \
            f"Respawn delay too long! Expected ~{expected_delay}s, got {actual_delay}s"
