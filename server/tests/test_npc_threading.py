"""
Tests for NPC threading and message queue infrastructure.

This module tests the NPC thread management system, message queue operations,
and thread-safe communication between NPC and main game threads.

As noted in the Pnakotic Manuscripts, proper thread management is essential
for maintaining the delicate balance between order and chaos in our eldritch
processing systems.
"""

import asyncio
import threading
import time
from unittest.mock import MagicMock

import pytest

from ..logging_config import get_logger

logger = get_logger(__name__)


class TestNPCMessageQueue:
    """Test NPC message queue operations."""

    @pytest.fixture
    def mock_npc_message_queue(self):
        """Create a mock NPC message queue for testing."""
        from ..npc.threading import NPCMessageQueue

        queue = NPCMessageQueue()
        return queue

    def test_message_queue_initialization(self, mock_npc_message_queue):
        """Test that NPC message queue initializes correctly."""
        assert mock_npc_message_queue is not None
        assert hasattr(mock_npc_message_queue, "pending_messages")
        assert hasattr(mock_npc_message_queue, "max_messages_per_npc")

    def test_add_npc_message(self, mock_npc_message_queue):
        """Test adding messages to NPC message queue."""
        npc_id = "test_npc_1"
        message = {
            "type": "move",
            "target_room": "earth_arkham_city_downtown_room_derby_st_001",
            "timestamp": time.time(),
        }

        result = mock_npc_message_queue.add_message(npc_id, message)
        assert result is True
        assert npc_id in mock_npc_message_queue.pending_messages
        assert len(mock_npc_message_queue.pending_messages[npc_id]) == 1

    def test_get_npc_messages(self, mock_npc_message_queue):
        """Test retrieving messages from NPC message queue."""
        npc_id = "test_npc_1"
        message1 = {"type": "move", "target_room": "room_1"}
        message2 = {"type": "attack", "target": "player_1"}

        mock_npc_message_queue.add_message(npc_id, message1)
        mock_npc_message_queue.add_message(npc_id, message2)

        messages = mock_npc_message_queue.get_messages(npc_id)
        assert len(messages) == 2
        assert messages[0]["type"] == "move"
        assert messages[1]["type"] == "attack"

    def test_clear_npc_messages(self, mock_npc_message_queue):
        """Test clearing messages from NPC message queue."""
        npc_id = "test_npc_1"
        message = {"type": "move", "target_room": "room_1"}

        mock_npc_message_queue.add_message(npc_id, message)
        assert len(mock_npc_message_queue.pending_messages[npc_id]) == 1

        mock_npc_message_queue.clear_messages(npc_id)
        assert len(mock_npc_message_queue.pending_messages[npc_id]) == 0

    def test_message_queue_size_limit(self, mock_npc_message_queue):
        """Test that message queue respects size limits."""
        npc_id = "test_npc_1"
        mock_npc_message_queue.max_messages_per_npc = 2

        # Add more messages than the limit
        for i in range(5):
            message = {"type": "test", "id": i}
            mock_npc_message_queue.add_message(npc_id, message)

        messages = mock_npc_message_queue.get_messages(npc_id)
        assert len(messages) == 2  # Should be limited to max_messages_per_npc
        assert messages[0]["id"] == 3  # Should keep the most recent messages
        assert messages[1]["id"] == 4

    def test_message_queue_thread_safety(self, mock_npc_message_queue):
        """Test that message queue operations are thread-safe."""
        npc_id = "test_npc_1"
        results = []
        errors = []

        def add_messages():
            try:
                for i in range(100):
                    message = {"type": "test", "id": i}
                    result = mock_npc_message_queue.add_message(npc_id, message)
                    results.append(result)
            except Exception as e:
                errors.append(e)

        def get_messages():
            try:
                for _ in range(100):
                    messages = mock_npc_message_queue.get_messages(npc_id)
                    results.append(len(messages))
            except Exception as e:
                errors.append(e)

        # Create multiple threads
        threads = []
        for _ in range(5):
            threads.append(threading.Thread(target=add_messages))
            threads.append(threading.Thread(target=get_messages))

        # Start all threads
        for thread in threads:
            thread.start()

        # Wait for all threads to complete
        for thread in threads:
            thread.join()

        # Verify no errors occurred
        assert len(errors) == 0
        assert len(results) > 0


class TestNPCThreadManager:
    """Test NPC thread management operations."""

    @pytest.fixture
    def mock_npc_thread_manager(self):
        """Create a mock NPC thread manager for testing."""
        from ..npc.threading import NPCThreadManager

        manager = NPCThreadManager()
        return manager

    @pytest.mark.asyncio
    async def test_thread_manager_initialization(self, mock_npc_thread_manager):
        """Test that NPC thread manager initializes correctly."""
        assert mock_npc_thread_manager is not None
        assert hasattr(mock_npc_thread_manager, "active_threads")
        assert hasattr(mock_npc_thread_manager, "message_queue")
        assert hasattr(mock_npc_thread_manager, "is_running")

    @pytest.mark.asyncio
    async def test_start_npc_thread(self, mock_npc_thread_manager):
        """Test starting an NPC thread."""
        npc_id = "test_npc_1"
        npc_definition = MagicMock()
        npc_definition.id = 1
        npc_definition.name = "Test NPC"
        npc_definition.npc_type = "passive_mob"

        # Start the thread manager first
        await mock_npc_thread_manager.start()

        result = await mock_npc_thread_manager.start_npc_thread(npc_id, npc_definition)
        assert result is True
        assert npc_id in mock_npc_thread_manager.active_threads

    @pytest.mark.asyncio
    async def test_stop_npc_thread(self, mock_npc_thread_manager):
        """Test stopping an NPC thread."""
        npc_id = "test_npc_1"
        npc_definition = MagicMock()
        npc_definition.id = 1
        npc_definition.name = "Test NPC"
        npc_definition.npc_type = "passive_mob"

        # Start the thread manager first
        await mock_npc_thread_manager.start()

        # Start the thread first
        await mock_npc_thread_manager.start_npc_thread(npc_id, npc_definition)
        assert npc_id in mock_npc_thread_manager.active_threads

        # Stop the thread
        result = await mock_npc_thread_manager.stop_npc_thread(npc_id)
        assert result is True
        assert npc_id not in mock_npc_thread_manager.active_threads

    @pytest.mark.asyncio
    async def test_restart_npc_thread(self, mock_npc_thread_manager):
        """Test restarting an NPC thread."""
        npc_id = "test_npc_1"
        npc_definition = MagicMock()
        npc_definition.id = 1
        npc_definition.name = "Test NPC"
        npc_definition.npc_type = "passive_mob"

        # Start the thread manager first
        await mock_npc_thread_manager.start()

        # Start the thread
        await mock_npc_thread_manager.start_npc_thread(npc_id, npc_definition)
        assert npc_id in mock_npc_thread_manager.active_threads

        # Restart the thread
        result = await mock_npc_thread_manager.restart_npc_thread(npc_id, npc_definition)
        assert result is True
        assert npc_id in mock_npc_thread_manager.active_threads

    @pytest.mark.asyncio
    async def test_get_active_npc_threads(self, mock_npc_thread_manager):
        """Test getting list of active NPC threads."""
        npc_definition = MagicMock()
        npc_definition.id = 1
        npc_definition.name = "Test NPC"
        npc_definition.npc_type = "passive_mob"

        # Start the thread manager first
        await mock_npc_thread_manager.start()

        # Start multiple threads
        await mock_npc_thread_manager.start_npc_thread("npc_1", npc_definition)
        await mock_npc_thread_manager.start_npc_thread("npc_2", npc_definition)

        active_threads = mock_npc_thread_manager.get_active_npc_threads()
        assert len(active_threads) == 2
        assert "npc_1" in active_threads
        assert "npc_2" in active_threads

    @pytest.mark.asyncio
    async def test_thread_manager_lifecycle(self, mock_npc_thread_manager):
        """Test complete thread manager lifecycle."""
        # Start the manager
        result = await mock_npc_thread_manager.start()
        assert result is True
        assert mock_npc_thread_manager.is_running is True

        # Stop the manager
        result = await mock_npc_thread_manager.stop()
        assert result is True
        assert mock_npc_thread_manager.is_running is False


class TestNPCActionMessageTypes:
    """Test NPC action message types and serialization."""

    def test_move_action_message(self):
        """Test move action message creation and serialization."""
        from ..npc.threading import NPCActionMessage, NPCActionType

        message = NPCActionMessage(
            action_type=NPCActionType.MOVE,
            npc_id="test_npc_1",
            target_room="earth_arkham_city_downtown_room_derby_st_001",
            timestamp=time.time(),
        )

        # Test serialization
        serialized = message.to_dict()
        assert serialized["action_type"] == "move"
        assert serialized["npc_id"] == "test_npc_1"
        assert serialized["target_room"] == "earth_arkham_city_downtown_room_derby_st_001"
        assert "timestamp" in serialized

        # Test deserialization
        deserialized = NPCActionMessage.from_dict(serialized)
        assert deserialized.action_type == NPCActionType.MOVE
        assert deserialized.npc_id == "test_npc_1"
        assert deserialized.target_room == "earth_arkham_city_downtown_room_derby_st_001"

    def test_attack_action_message(self):
        """Test attack action message creation and serialization."""
        from ..npc.threading import NPCActionMessage, NPCActionType

        message = NPCActionMessage(
            action_type=NPCActionType.ATTACK,
            npc_id="test_npc_1",
            target_player="player_1",
            damage=25,
            timestamp=time.time(),
        )

        serialized = message.to_dict()
        assert serialized["action_type"] == "attack"
        assert serialized["target_player"] == "player_1"
        assert serialized["damage"] == 25

        deserialized = NPCActionMessage.from_dict(serialized)
        assert deserialized.action_type == NPCActionType.ATTACK
        assert deserialized.target_player == "player_1"
        assert deserialized.damage == 25

    def test_speak_action_message(self):
        """Test speak action message creation and serialization."""
        from ..npc.threading import NPCActionMessage, NPCActionType

        message = NPCActionMessage(
            action_type=NPCActionType.SPEAK,
            npc_id="test_npc_1",
            message="Hello, traveler!",
            channel="local",
            timestamp=time.time(),
        )

        serialized = message.to_dict()
        assert serialized["action_type"] == "speak"
        assert serialized["message"] == "Hello, traveler!"
        assert serialized["channel"] == "local"

        deserialized = NPCActionMessage.from_dict(serialized)
        assert deserialized.action_type == NPCActionType.SPEAK
        assert deserialized.message == "Hello, traveler!"
        assert deserialized.channel == "local"

    def test_json_serialization(self):
        """Test JSON serialization and deserialization of action messages."""
        from ..npc.threading import NPCActionMessage, NPCActionType

        message = NPCActionMessage(
            action_type=NPCActionType.MOVE, npc_id="test_npc_1", target_room="room_1", timestamp=time.time()
        )

        # Test JSON serialization
        json_str = message.to_json()
        assert isinstance(json_str, str)

        # Test JSON deserialization
        deserialized = NPCActionMessage.from_json(json_str)
        assert deserialized.action_type == NPCActionType.MOVE
        assert deserialized.npc_id == "test_npc_1"
        assert deserialized.target_room == "room_1"


class TestNPCThreadSafeCommunication:
    """Test thread-safe communication between NPC and main game threads."""

    @pytest.fixture
    def mock_communication_bridge(self):
        """Create a mock communication bridge for testing."""
        from ..npc.threading import NPCCommunicationBridge

        bridge = NPCCommunicationBridge()
        return bridge

    @pytest.mark.asyncio
    async def test_send_message_to_npc(self, mock_communication_bridge):
        """Test sending messages to NPC threads."""
        npc_id = "test_npc_1"
        message = {"type": "player_entered_room", "player_id": "player_1", "room_id": "room_1"}

        result = await mock_communication_bridge.send_message_to_npc(npc_id, message)
        assert result is True

    @pytest.mark.asyncio
    async def test_receive_message_from_npc(self, mock_communication_bridge):
        """Test receiving messages from NPC threads."""
        npc_id = "test_npc_1"
        message = {"type": "npc_moved", "npc_id": npc_id, "from_room": "room_1", "to_room": "room_2"}

        # Send message from NPC
        await mock_communication_bridge.receive_message_from_npc(npc_id, message)

        # Check if message was received
        messages = await mock_communication_bridge.get_pending_messages()
        assert len(messages) > 0
        assert any(msg["type"] == "npc_moved" for msg in messages)

    @pytest.mark.asyncio
    async def test_broadcast_to_all_npcs(self, mock_communication_bridge):
        """Test broadcasting messages to all NPC threads."""
        message = {"type": "game_tick", "tick_number": 1, "timestamp": time.time()}

        result = await mock_communication_bridge.broadcast_to_all_npcs(message)
        assert result is True

    @pytest.mark.asyncio
    async def test_communication_bridge_thread_safety(self, mock_communication_bridge):
        """Test that communication bridge operations are thread-safe."""
        results = []
        errors = []

        async def send_messages():
            try:
                for i in range(50):
                    message = {"type": "test", "id": i}
                    result = await mock_communication_bridge.send_message_to_npc(f"npc_{i % 5}", message)
                    results.append(result)
            except Exception as e:
                errors.append(e)

        async def receive_messages():
            try:
                for i in range(50):
                    message = {"type": "response", "id": i}
                    await mock_communication_bridge.receive_message_from_npc(f"npc_{i % 5}", message)
            except Exception as e:
                errors.append(e)

        # Run concurrent operations
        tasks = []
        for _ in range(5):
            tasks.append(asyncio.create_task(send_messages()))
            tasks.append(asyncio.create_task(receive_messages()))

        await asyncio.gather(*tasks)

        # Verify no errors occurred
        assert len(errors) == 0
        assert len(results) > 0


class TestNPCThreadLifecycleManagement:
    """Test NPC thread lifecycle management operations."""

    @pytest.fixture
    def mock_npc_lifecycle_manager(self):
        """Create a mock NPC lifecycle manager for testing."""
        from ..npc.threading import NPCLifecycleManager

        manager = NPCLifecycleManager()
        return manager

    @pytest.mark.asyncio
    async def test_spawn_npc_thread(self, mock_npc_lifecycle_manager):
        """Test spawning an NPC thread."""
        npc_definition = MagicMock()
        npc_definition.id = 1
        npc_definition.name = "Test NPC"
        npc_definition.npc_type = "passive_mob"
        npc_definition.sub_zone_id = "downtown"
        npc_definition.room_id = "room_1"

        # Start the thread manager first
        await mock_npc_lifecycle_manager.thread_manager.start()

        result = await mock_npc_lifecycle_manager.spawn_npc(npc_definition)
        assert result is True

    @pytest.mark.asyncio
    async def test_despawn_npc_thread(self, mock_npc_lifecycle_manager):
        """Test despawning an NPC thread."""
        npc_definition = MagicMock()
        npc_definition.id = 1
        npc_definition.name = "Test NPC"
        npc_definition.npc_type = "passive_mob"

        # Start the thread manager first
        await mock_npc_lifecycle_manager.thread_manager.start()

        # Spawn first
        await mock_npc_lifecycle_manager.spawn_npc(npc_definition)

        # Then despawn
        result = await mock_npc_lifecycle_manager.despawn_npc(1)
        assert result is True

    @pytest.mark.asyncio
    async def test_respawn_npc_thread(self, mock_npc_lifecycle_manager):
        """Test respawning an NPC thread."""
        npc_definition = MagicMock()
        npc_definition.id = 1
        npc_definition.name = "Test NPC"
        npc_definition.npc_type = "passive_mob"

        # Start the thread manager first
        await mock_npc_lifecycle_manager.thread_manager.start()

        # Spawn first
        await mock_npc_lifecycle_manager.spawn_npc(npc_definition)

        # Then respawn
        result = await mock_npc_lifecycle_manager.respawn_npc(1, npc_definition)
        assert result is True

    @pytest.mark.asyncio
    async def test_get_npc_status(self, mock_npc_lifecycle_manager):
        """Test getting NPC thread status."""
        npc_definition = MagicMock()
        npc_definition.id = 1
        npc_definition.name = "Test NPC"
        npc_definition.npc_type = "passive_mob"

        # Start the thread manager first
        await mock_npc_lifecycle_manager.thread_manager.start()

        # Spawn NPC
        await mock_npc_lifecycle_manager.spawn_npc(npc_definition)

        # Get status
        status = await mock_npc_lifecycle_manager.get_npc_status(1)
        assert status is not None
        assert status["npc_definition_id"] == 1
        assert status["status"] == "active"

    @pytest.mark.asyncio
    async def test_lifecycle_manager_cleanup(self, mock_npc_lifecycle_manager):
        """Test lifecycle manager cleanup operations."""
        npc_definition = MagicMock()
        npc_definition.id = 1
        npc_definition.name = "Test NPC"
        npc_definition.npc_type = "passive_mob"

        # Spawn multiple NPCs
        await mock_npc_lifecycle_manager.spawn_npc(npc_definition)

        # Cleanup all
        result = await mock_npc_lifecycle_manager.cleanup_all_npcs()
        assert result is True


class TestNPCThreadingIntegration:
    """Integration tests for NPC threading system."""

    @pytest.mark.asyncio
    async def test_full_npc_threading_workflow(self):
        """Test complete NPC threading workflow."""
        from ..npc.threading import (
            NPCActionMessage,
            NPCActionType,
            NPCCommunicationBridge,
            NPCMessageQueue,
            NPCThreadManager,
        )

        # Initialize components
        thread_manager = NPCThreadManager()
        message_queue = NPCMessageQueue()
        communication_bridge = NPCCommunicationBridge()

        # Start thread manager
        await thread_manager.start()

        # Create mock NPC definition
        npc_definition = MagicMock()
        npc_definition.id = 1
        npc_definition.name = "Test NPC"
        npc_definition.npc_type = "passive_mob"
        npc_definition.sub_zone_id = "downtown"
        npc_definition.room_id = "room_1"

        # Start NPC thread
        npc_id = "test_npc_1"
        await thread_manager.start_npc_thread(npc_id, npc_definition)

        # Send action message
        action_message = NPCActionMessage(
            action_type=NPCActionType.MOVE, npc_id=npc_id, target_room="room_2", timestamp=time.time()
        )

        message_queue.add_message(npc_id, action_message.to_dict())

        # Verify message was queued
        messages = message_queue.get_messages(npc_id)
        assert len(messages) == 1
        assert messages[0]["action_type"] == "move"

        # Send communication message
        await communication_bridge.send_message_to_npc(
            npc_id, {"type": "player_entered_room", "player_id": "player_1", "room_id": "room_1"}
        )

        # Stop NPC thread
        await thread_manager.stop_npc_thread(npc_id)

        # Stop thread manager
        await thread_manager.stop()

        # Verify cleanup
        assert npc_id not in thread_manager.active_threads
        assert not thread_manager.is_running

    @pytest.mark.asyncio
    async def test_npc_threading_error_handling(self):
        """Test error handling in NPC threading system."""
        from ..npc.threading import NPCThreadManager

        thread_manager = NPCThreadManager()

        # Test starting thread with invalid NPC definition
        invalid_npc = None
        result = await thread_manager.start_npc_thread("invalid_npc", invalid_npc)
        assert result is False

        # Test stopping non-existent thread
        result = await thread_manager.stop_npc_thread("non_existent_npc")
        assert result is True  # Should return True for non-existent threads (no-op)

        # Test restarting non-existent thread
        result = await thread_manager.restart_npc_thread("non_existent_npc", invalid_npc)
        assert result is False

    @pytest.mark.asyncio
    async def test_npc_threading_performance(self):
        """Test NPC threading system performance."""
        from ..npc.threading import NPCMessageQueue, NPCThreadManager

        thread_manager = NPCThreadManager()
        message_queue = NPCMessageQueue()

        await thread_manager.start()

        # Create multiple NPCs
        npc_count = 10
        npc_definitions = []

        for i in range(npc_count):
            npc_definition = MagicMock()
            npc_definition.id = i + 1
            npc_definition.name = f"Test NPC {i + 1}"
            npc_definition.npc_type = "passive_mob"
            npc_definitions.append(npc_definition)

        # Start all NPC threads
        start_time = time.time()
        for i, npc_def in enumerate(npc_definitions):
            await thread_manager.start_npc_thread(f"npc_{i + 1}", npc_def)
        start_duration = time.time() - start_time

        # Verify all threads started
        active_threads = thread_manager.get_active_npc_threads()
        assert len(active_threads) == npc_count

        # Test message queue performance
        message_start_time = time.time()
        for i in range(npc_count):
            for j in range(10):  # 10 messages per NPC
                message = {"type": "test", "npc_id": f"npc_{i + 1}", "message_id": j}
                message_queue.add_message(f"npc_{i + 1}", message)
        message_duration = time.time() - message_start_time

        # Verify messages were queued
        total_messages = 0
        for i in range(npc_count):
            messages = message_queue.get_messages(f"npc_{i + 1}")
            total_messages += len(messages)

        assert total_messages == npc_count * 10

        # Stop all threads
        stop_start_time = time.time()
        for i in range(npc_count):
            await thread_manager.stop_npc_thread(f"npc_{i + 1}")
        stop_duration = time.time() - stop_start_time

        await thread_manager.stop()

        # Performance assertions (these are reasonable expectations)
        assert start_duration < 5.0  # Should start 10 NPCs in under 5 seconds
        assert message_duration < 1.0  # Should queue 100 messages in under 1 second
        assert stop_duration < 5.0  # Should stop 10 NPCs in under 5 seconds

        logger.info(
            f"Performance metrics - Start: {start_duration:.3f}s, "
            f"Messages: {message_duration:.3f}s, Stop: {stop_duration:.3f}s"
        )
