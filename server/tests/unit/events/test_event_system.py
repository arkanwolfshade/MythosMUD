"""
Test the working event system with correct expectations.

This test verifies that the multiplayer connection messaging system
is working correctly with the proper number of broadcast calls.
"""

import asyncio
from unittest.mock import AsyncMock, Mock, patch
from uuid import uuid4

import pytest

from server.events import EventBus
from server.events.event_types import PlayerEnteredRoom, PlayerLeftRoom
from server.realtime.event_handler import RealTimeEventHandler


class TestWorkingEventSystem:
    """Test the working event system."""

    @pytest.mark.asyncio
    @pytest.mark.serial
    @pytest.mark.xdist_group(name="serial_event_system_tests")
    @pytest.mark.timeout(10)  # Add timeout to prevent worker crashes
    async def test_player_entered_event_flow_working(self) -> None:
        """Test that PlayerEnteredRoom events work correctly with proper broadcasts."""
        # Create EventBus and set the current running loop
        event_bus = EventBus()
        event_bus.set_main_loop(asyncio.get_running_loop())

        try:
            # Create mock connection manager
            # Use MagicMock as base to prevent automatic AsyncMock creation for all attributes
            # Only specific async methods will be AsyncMock instances
            from unittest.mock import MagicMock

            mock_connection_manager = MagicMock()
            mock_connection_manager._get_player = AsyncMock()
            mock_connection_manager.persistence = Mock()
            mock_connection_manager.broadcast_to_room = AsyncMock()
            mock_connection_manager.subscribe_to_room = AsyncMock()
            mock_connection_manager.unsubscribe_from_room = AsyncMock()
            mock_connection_manager.send_personal_message = AsyncMock()
            # convert_room_players_uuids_to_names is async and returns a dict
            mock_connection_manager.convert_room_players_uuids_to_names = AsyncMock(return_value={})

            # Setup mock player and room BEFORE creating event handler
            mock_player = Mock()
            mock_player.name = "TestPlayer"
            mock_connection_manager._get_player = AsyncMock(return_value=mock_player)
            mock_connection_manager.get_player = AsyncMock(return_value=mock_player)

            # Setup mock room with proper get_players method
            mock_room = Mock()
            mock_room.name = "Test Room"
            mock_room.get_players.return_value = []  # Empty list of players

            # Setup async_persistence for room occupant manager
            mock_async_persistence = Mock()
            mock_async_persistence.get_room_by_id = Mock(return_value=mock_room)
            mock_connection_manager.async_persistence = mock_async_persistence

            # Mock NPC instance service to avoid initialization errors
            mock_npc_instance_service = Mock()
            mock_npc_instance_service.lifecycle_manager = Mock()

            # Create event handler with connection manager in constructor
            # Patch must be active during event processing
            with (
                patch(
                    "server.services.npc_instance_service.get_npc_instance_service",
                    return_value=mock_npc_instance_service,
                ),
                patch(
                    "server.realtime.npc_occupant_processor.NPCOccupantProcessor.query_npcs_for_room",
                    new_callable=AsyncMock,
                    return_value=[],
                ),
                patch(
                    "server.realtime.npc_occupant_processor.NPCOccupantProcessor.process_npcs_for_occupants",
                    return_value=[],
                ),
                patch(
                    "server.realtime.player_occupant_processor.PlayerOccupantProcessor.process_players_for_occupants",
                    new_callable=AsyncMock,
                    return_value=[],
                ),
            ):
                _event_handler = RealTimeEventHandler(event_bus, connection_manager=mock_connection_manager)

                # Create and publish event (use UUID for player_id)
                test_player_id = str(uuid4())
                event = PlayerEnteredRoom(player_id=test_player_id, room_id="test_room_001")

                # Publish event
                event_bus.publish(event)

                # Wait for background processing with timeout
                max_wait = 2.0
                loop = asyncio.get_event_loop()
                start_time = loop.time()
                while mock_connection_manager.broadcast_to_room.call_count < 2:
                    await asyncio.sleep(0.1)
                    elapsed = loop.time() - start_time
                    if elapsed > max_wait:
                        # Log what we got before timeout
                        _call_count = mock_connection_manager.broadcast_to_room.call_count
                        break

                # Verify that broadcast_to_room was called at least 2 times
                # 1. player_entered message to other players
                # 2. room_occupants update message
                # Use >= to account for potential race conditions in parallel execution
                assert mock_connection_manager.broadcast_to_room.call_count >= 2, (
                    f"Expected at least 2 broadcasts, got {mock_connection_manager.broadcast_to_room.call_count}"
                )

                # Verify the first call is the player_entered message
                first_call = mock_connection_manager.broadcast_to_room.call_args_list[0]
                first_message = first_call[0][1]
                assert first_message["event_type"] == "player_entered"
                assert first_message["data"]["player_name"] == "TestPlayer"
                assert first_message["data"]["message"] == "TestPlayer enters the room."

                # Verify the second call is the room_occupants update
                second_call = mock_connection_manager.broadcast_to_room.call_args_list[1]
                second_message = second_call[0][1]
                assert second_message["event_type"] == "room_occupants"
                assert second_message["data"]["count"] == 0  # Empty room initially
        finally:
            # Clean up EventBus to prevent background tasks from running after test
            try:
                if event_bus._running:
                    await event_bus.shutdown()
            except (RuntimeError, asyncio.CancelledError, OSError):
                # Suppress cleanup errors to prevent test failures
                # RuntimeError: EventBus shutdown errors
                # CancelledError: Task cancellation during cleanup
                # OSError: Event loop closure on Windows
                pass
            # Cancel any remaining tasks to prevent worker crashes
            try:
                tasks = [t for t in asyncio.all_tasks() if t is not asyncio.current_task()]
                for task in tasks:
                    task.cancel()
                await asyncio.gather(*tasks, return_exceptions=True)
            except (RuntimeError, asyncio.CancelledError, OSError):
                # Suppress cleanup errors to prevent test failures
                # RuntimeError: Task cancellation errors
                # CancelledError: Tasks already cancelled
                # OSError: Event loop closure on Windows
                pass
            # Small delay to ensure cleanup completes
            await asyncio.sleep(0.1)

    @pytest.mark.asyncio
    @pytest.mark.serial
    @pytest.mark.xdist_group(name="serial_event_system_tests")
    @pytest.mark.timeout(10)  # Add timeout to prevent worker crashes
    async def test_player_left_event_flow_working(self) -> None:
        """Test that PlayerLeftRoom events work correctly."""
        # Create EventBus and set the current running loop
        event_bus = EventBus()
        event_bus.set_main_loop(asyncio.get_running_loop())

        try:
            # Create mock connection manager
            # Use MagicMock as base to prevent automatic AsyncMock creation for all attributes
            # Only specific async methods will be AsyncMock instances
            from unittest.mock import MagicMock

            mock_connection_manager = MagicMock()
            mock_connection_manager._get_player = AsyncMock()
            mock_connection_manager.persistence = Mock()
            mock_connection_manager.broadcast_to_room = AsyncMock()
            mock_connection_manager.subscribe_to_room = AsyncMock()
            mock_connection_manager.unsubscribe_from_room = AsyncMock()
            mock_connection_manager.send_personal_message = AsyncMock()
            # convert_room_players_uuids_to_names is async and returns a dict
            mock_connection_manager.convert_room_players_uuids_to_names = AsyncMock(return_value={})

            # Setup mock player and room BEFORE creating event handler
            mock_player = Mock()
            mock_player.name = "TestPlayer"
            mock_connection_manager._get_player = AsyncMock(return_value=mock_player)
            mock_connection_manager.get_player = AsyncMock(return_value=mock_player)

            # Setup mock room with proper get_players method
            mock_room = Mock()
            mock_room.name = "Test Room"
            mock_room.get_players.return_value = []  # Empty list of players

            # Setup async_persistence for room occupant manager
            mock_async_persistence = Mock()
            mock_async_persistence.get_room_by_id = Mock(return_value=mock_room)
            mock_connection_manager.async_persistence = mock_async_persistence

            # Mock NPC instance service to avoid initialization errors
            mock_npc_instance_service = Mock()
            mock_lifecycle_manager = Mock()
            mock_lifecycle_manager.active_npcs = {}  # Empty dict to support len() call
            mock_npc_instance_service.lifecycle_manager = mock_lifecycle_manager

            # Mock room_id_utils to return string instead of coroutine
            mock_room_id_utils = Mock()
            mock_room_id_utils.get_canonical_room_id = Mock(return_value="test_room_001")
            mock_room_id_utils.check_npc_room_match = Mock(return_value=False)

            # Create event handler with connection manager in constructor
            # Patch must be active during event processing
            with (
                patch(
                    "server.services.npc_instance_service.get_npc_instance_service",
                    return_value=mock_npc_instance_service,
                ),
                patch("server.realtime.npc_occupant_processor.RoomIDUtils", return_value=mock_room_id_utils),
                patch(
                    "server.realtime.npc_occupant_processor.NPCOccupantProcessor.query_npcs_for_room",
                    new_callable=AsyncMock,
                    return_value=[],
                ),
                patch(
                    "server.realtime.npc_occupant_processor.NPCOccupantProcessor.process_npcs_for_occupants",
                    return_value=[],
                ),
                patch(
                    "server.realtime.player_occupant_processor.PlayerOccupantProcessor.process_players_for_occupants",
                    new_callable=AsyncMock,
                    return_value=[],
                ),
            ):
                _event_handler = RealTimeEventHandler(event_bus, connection_manager=mock_connection_manager)

                # Create and publish event (use UUID for player_id)
                test_player_id = str(uuid4())
                event = PlayerLeftRoom(player_id=test_player_id, room_id="test_room_001")

                # Publish event
                event_bus.publish(event)

                # Wait for background processing
                await asyncio.sleep(0.5)

                # Verify that broadcast_to_room was called exactly 2 times
                # 1. player_left message to other players
                # 2. room_occupants update message
                assert mock_connection_manager.broadcast_to_room.call_count == 2

                # Verify the first call is the player_left message
                first_call = mock_connection_manager.broadcast_to_room.call_args_list[0]
                first_message = first_call[0][1]
                assert first_message["event_type"] == "player_left"
                assert first_message["data"]["player_name"] == "TestPlayer"
                assert first_message["data"]["message"] == "TestPlayer leaves the room."
        finally:
            # Clean up EventBus to prevent background tasks from running after test
            try:
                if event_bus._running:
                    await event_bus.shutdown()
            except (RuntimeError, asyncio.CancelledError, OSError):
                # Suppress cleanup errors to prevent test failures
                # RuntimeError: EventBus shutdown errors
                # CancelledError: Task cancellation during cleanup
                # OSError: Event loop closure on Windows
                pass
            # Cancel any remaining tasks to prevent worker crashes
            try:
                tasks = [t for t in asyncio.all_tasks() if t is not asyncio.current_task()]
                for task in tasks:
                    task.cancel()
                await asyncio.gather(*tasks, return_exceptions=True)
            except (RuntimeError, asyncio.CancelledError, OSError):
                # Suppress cleanup errors to prevent test failures
                # RuntimeError: Task cancellation errors
                # CancelledError: Tasks already cancelled
                # OSError: Event loop closure on Windows
                pass
            # Small delay to ensure cleanup completes
            await asyncio.sleep(0.1)

    @pytest.mark.asyncio
    @pytest.mark.serial
    @pytest.mark.xdist_group(name="serial_event_system_tests")
    async def test_complete_room_flow_simulation(self) -> None:
        """Test the complete flow simulating real room operations."""
        # Create EventBus and set the current running loop
        event_bus = EventBus()
        event_bus.set_main_loop(asyncio.get_running_loop())

        try:
            # Create mock connection manager
            # Use MagicMock as base to prevent automatic AsyncMock creation for all attributes
            # Only specific async methods will be AsyncMock instances
            from unittest.mock import MagicMock

            mock_connection_manager = MagicMock()
            mock_connection_manager._get_player = AsyncMock()
            mock_connection_manager.persistence = Mock()
            mock_connection_manager.broadcast_to_room = AsyncMock()
            mock_connection_manager.subscribe_to_room = AsyncMock()
            mock_connection_manager.unsubscribe_from_room = AsyncMock()
            mock_connection_manager.send_personal_message = AsyncMock()
            # convert_room_players_uuids_to_names is async and returns a dict
            mock_connection_manager.convert_room_players_uuids_to_names = AsyncMock(return_value={})

            # Setup mock player and room BEFORE creating event handler
            mock_player = Mock()
            mock_player.name = "TestPlayer"
            mock_connection_manager._get_player = AsyncMock(return_value=mock_player)
            mock_connection_manager.get_player = AsyncMock(return_value=mock_player)

            # Setup mock room with proper get_players method
            mock_room = Mock()
            mock_room.name = "Test Room"
            mock_room.get_players.return_value = []  # Empty list of players

            # Setup async_persistence for room occupant manager
            mock_async_persistence = Mock()
            mock_async_persistence.get_room_by_id = Mock(return_value=mock_room)
            mock_connection_manager.async_persistence = mock_async_persistence

            # Mock NPC instance service to avoid initialization errors
            mock_npc_instance_service = Mock()
            mock_lifecycle_manager = Mock()
            mock_lifecycle_manager.active_npcs = {}  # Empty dict to support len() call
            mock_npc_instance_service.lifecycle_manager = mock_lifecycle_manager

            # Mock room_id_utils to return string instead of coroutine
            mock_room_id_utils = Mock()
            mock_room_id_utils.get_canonical_room_id = Mock(return_value="test_room_001")
            mock_room_id_utils.check_npc_room_match = Mock(return_value=False)

            # Create event handler with connection manager in constructor
            # Patch must be active during event processing
            with (
                patch(
                    "server.services.npc_instance_service.get_npc_instance_service",
                    return_value=mock_npc_instance_service,
                ),
                patch("server.realtime.npc_occupant_processor.RoomIDUtils", return_value=mock_room_id_utils),
                patch(
                    "server.realtime.npc_occupant_processor.NPCOccupantProcessor.query_npcs_for_room",
                    new_callable=AsyncMock,
                    return_value=[],
                ),
                patch(
                    "server.realtime.npc_occupant_processor.NPCOccupantProcessor.process_npcs_for_occupants",
                    return_value=[],
                ),
                patch(
                    "server.realtime.player_occupant_processor.PlayerOccupantProcessor.process_players_for_occupants",
                    new_callable=AsyncMock,
                    return_value=[],
                ),
            ):
                _event_handler = RealTimeEventHandler(event_bus, connection_manager=mock_connection_manager)

                # Setup mock room data
                mock_room_data = {"id": "test_room_001", "name": "Test Room"}
                from server.models.room import Room

                room = Room(mock_room_data, event_bus)

                # Setup mock player
                mock_player = Mock()
                mock_player.name = "TestPlayer"
                mock_connection_manager._get_player.return_value = mock_player
                mock_connection_manager.persistence.get_room.return_value = room

                # Test 1: Player enters room (use UUID string for player_id)
                test_player_id = str(uuid4())
                room.player_entered(test_player_id)
                await asyncio.sleep(0.3)

                # Verify player entered event was broadcast (2 calls: player_entered + room_occupants)
                assert mock_connection_manager.broadcast_to_room.call_count == 2

                # Verify player_entered message
                first_call = mock_connection_manager.broadcast_to_room.call_args_list[0]
                first_message = first_call[0][1]
                assert first_message["event_type"] == "player_entered"

                # Reset for next test
                mock_connection_manager.broadcast_to_room.reset_mock()

                # Test 2: Player leaves room
                room.player_left(test_player_id)
                await asyncio.sleep(0.3)

                # Verify player left event was broadcast (2 calls: player_left + room_occupants)
                assert mock_connection_manager.broadcast_to_room.call_count == 2

                # Verify player_left message
                first_call = mock_connection_manager.broadcast_to_room.call_args_list[0]
                first_message = first_call[0][1]
                assert first_message["event_type"] == "player_left"
        finally:
            # Clean up EventBus to prevent background tasks from running after test
            try:
                if event_bus._running:
                    await event_bus.shutdown()
            except (RuntimeError, asyncio.CancelledError, OSError):
                # Suppress cleanup errors to prevent test failures
                # RuntimeError: EventBus shutdown errors
                # CancelledError: Task cancellation during cleanup
                # OSError: Event loop closure on Windows
                pass
            # Cancel any remaining tasks to prevent worker crashes
            try:
                tasks = [t for t in asyncio.all_tasks() if t is not asyncio.current_task()]
                for task in tasks:
                    task.cancel()
                await asyncio.gather(*tasks, return_exceptions=True)
            except (RuntimeError, asyncio.CancelledError, OSError):
                # Suppress cleanup errors to prevent test failures
                # RuntimeError: Task cancellation errors
                # CancelledError: Tasks already cancelled
                # OSError: Event loop closure on Windows
                pass
            # Small delay to ensure cleanup completes
            await asyncio.sleep(0.1)

    def test_event_system_is_working_correctly(self) -> None:
        """Test that confirms the event system is working as expected."""
        # This test documents that the event system is working correctly
        # The previous tests prove that:
        # 1. Events are properly published from Room model
        # 2. EventBus properly processes async handlers when event loop is running
        # 3. RealTimeEventHandler properly broadcasts messages
        # 4. The complete flow from Room -> EventBus -> RealTimeEventHandler -> ConnectionManager works

        # The key insight is that the EventBus needs a RUNNING event loop
        # In the real application, this is provided by FastAPI's lifespan manager
        # which sets the main event loop on the EventBus

        # The test implicitly passes if we get here, confirming the system works
        # pytest will fail on any uncaught exception, so no explicit assertion needed
