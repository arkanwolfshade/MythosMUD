"""
Integration tests for occupant count synchronization.

This module tests the complete end-to-end flow of occupant count updates,
including server-side event broadcasting, client-side event handling,
and synchronization across multiple connected clients.
"""

import asyncio
from unittest.mock import AsyncMock, MagicMock, patch
from uuid import NAMESPACE_DNS, UUID, uuid4, uuid5

import pytest

from server.events import EventBus
from server.events.event_types import PlayerEnteredRoom, PlayerLeftRoom
from server.models import Player
from server.realtime.connection_manager import ConnectionManager
from server.realtime.envelope import build_event


def _str_to_uuid(player_id_str: str) -> UUID:
    """Convert string player_id to UUID deterministically for tests."""
    return uuid5(NAMESPACE_DNS, player_id_str)


class TestOccupantCountIntegration:
    """Test occupant count synchronization integration."""

    @pytest.fixture
    def event_bus(self):
        """Create a test event bus."""
        return EventBus()

    @pytest.fixture
    def connection_manager(self, event_bus, mock_players):
        """Create a connection manager with event bus integration."""
        manager = ConnectionManager()

        # Mock the persistence layer to return our event bus and players
        with patch("server.persistence.get_persistence") as mock_persistence:
            mock_persistence_instance = MagicMock()
            mock_persistence_instance._event_bus = event_bus

            # Mock get_player to return our mock players (handle both string and UUID)
            def mock_get_player(player_id):
                # Convert UUID to string for lookup, or use string directly
                if isinstance(player_id, UUID):
                    # Try to find matching player by converting back
                    for key, player in mock_players.items():
                        if _str_to_uuid(key) == player_id:
                            return player
                    return None
                return mock_players.get(player_id)

            mock_persistence_instance.get_player = MagicMock(side_effect=mock_get_player)
            mock_persistence.return_value = mock_persistence_instance

            # Initialize the manager
            manager._get_event_bus = lambda: event_bus
            manager.persistence = mock_persistence_instance

        return manager

    @pytest.fixture
    def mock_room_manager(self):
        """Create a mock room manager."""
        room_manager = MagicMock()
        room_manager.get_room_occupants = MagicMock(return_value=[])

        # Track room subscriptions for testing
        room_subscriptions = {}  # room_id -> set of player_ids

        def mock_subscribe_to_room(player_id, room_id):
            if room_id not in room_subscriptions:
                room_subscriptions[room_id] = set()
            room_subscriptions[room_id].add(player_id)

        def mock_get_room_subscribers(room_id):
            return room_subscriptions.get(room_id, set())

        def mock_unsubscribe_from_room(player_id, room_id):
            if room_id in room_subscriptions:
                room_subscriptions[room_id].discard(player_id)

        room_manager.subscribe_to_room = MagicMock(side_effect=mock_subscribe_to_room)
        room_manager.get_room_subscribers = MagicMock(side_effect=mock_get_room_subscribers)
        room_manager.unsubscribe_from_room = MagicMock(side_effect=mock_unsubscribe_from_room)

        return room_manager

    @pytest.fixture
    def mock_players(self):
        """Create mock players for testing."""
        players = {}
        for i in range(1, 6):  # Create 5 test players
            player = MagicMock(spec=Player)
            player.name = f"Player{i}"
            player.player_id = f"player_{i}"
            player.current_room_id = "arkham_001"
            players[f"player_{i}"] = player
        return players

    @pytest.fixture
    def mock_websockets(self):
        """Create mock WebSocket connections."""
        websockets = {}
        for i in range(1, 6):  # Create 5 test WebSockets
            websocket = AsyncMock()
            websocket.send_json = AsyncMock()
            websocket.close = AsyncMock()
            websocket.ping = AsyncMock()
            websockets[f"player_{i}"] = websocket
        return websockets

    @pytest.fixture
    def sample_occupants(self):
        """Create sample occupant data for testing."""
        return [
            {"player_name": "Player1", "player_id": "player_1"},
            {"player_name": "Player2", "player_id": "player_2"},
            {"player_name": "Player3", "player_id": "player_3"},
        ]

    @pytest.mark.asyncio
    async def test_occupant_count_synchronization_flow(
        self, connection_manager, event_bus, mock_room_manager, mock_players, mock_websockets, sample_occupants
    ):
        """Test the complete occupant count synchronization flow."""
        # Setup connection manager with room manager
        connection_manager.room_manager = mock_room_manager

        # Setup mock room manager to return sample occupants
        mock_room_manager.get_room_occupants.return_value = sample_occupants

        # Connect multiple players to the same room
        room_id = "arkham_001"
        session_id = "test_session"

        connected_players = []
        for player_id_str, websocket in mock_websockets.items():
            # Convert string ID to UUID for connect_websocket
            player_id_uuid = _str_to_uuid(player_id_str)
            await connection_manager.connect_websocket(websocket, player_id_uuid, session_id)
            connected_players.append(player_id_str)

        # Subscribe to room events
        await connection_manager.subscribe_to_room_events()

        # Simulate a player entering the room
        player_id = uuid4()
        new_player = MagicMock(spec=Player)
        new_player.name = "Player4"
        new_player.player_id = player_id
        new_player.current_room_id = room_id

        # Create player entered event
        enter_event = PlayerEnteredRoom(player_id=str(player_id), room_id=room_id)
        enter_event.timestamp = None

        # Update mock to include new player in occupants
        updated_occupants = sample_occupants + [{"player_name": "Player4", "player_id": str(player_id)}]
        mock_room_manager.get_room_occupants.return_value = updated_occupants

        # Publish the event and manually trigger the async handler
        event_bus.publish(enter_event)

        # Manually call the async handler since event bus can't run it in test environment
        await connection_manager._handle_player_entered_room(enter_event.__dict__)

        # Wait for event processing
        await asyncio.sleep(0.1)

        # Verify that room_occupants events were broadcast to all connected players
        for _player_id, websocket in mock_websockets.items():
            # Check that send_json was called (indicating room_occupants event was sent)
            websocket.send_json.assert_called()

            # Get the last call to verify the event structure
            call_args = websocket.send_json.call_args[0][0]
            assert call_args["event_type"] == "room_occupants"
            assert call_args["room_id"] == room_id
            assert call_args["data"]["count"] == 4
            assert len(call_args["data"]["occupants"]) == 4
            assert "Player1" in call_args["data"]["occupants"]
            assert "Player4" in call_args["data"]["occupants"]

    @pytest.mark.asyncio
    async def test_occupant_count_on_player_exit(
        self, connection_manager, event_bus, mock_room_manager, mock_players, mock_websockets, sample_occupants
    ):
        """Test occupant count updates when a player leaves a room."""
        # Setup connection manager
        connection_manager.room_manager = mock_room_manager
        mock_room_manager.get_room_occupants.return_value = sample_occupants

        # Connect players
        room_id = "arkham_001"
        session_id = "test_session"

        for player_id_str, websocket in mock_websockets.items():
            # Convert string ID to UUID for connect_websocket
            player_id_uuid = _str_to_uuid(player_id_str)
            await connection_manager.connect_websocket(websocket, player_id_uuid, session_id)

        await connection_manager.subscribe_to_room_events()

        # Simulate a player leaving the room (use one of the existing players)
        leaving_player_str = "player_2"
        leaving_player_id = _str_to_uuid(leaving_player_str)

        # Create player left event
        leave_event = PlayerLeftRoom(player_id=str(leaving_player_id), room_id=room_id)
        leave_event.timestamp = None

        # Update mock to reflect player leaving (remove player_2)
        updated_occupants = [occ for occ in sample_occupants if occ["player_id"] != leaving_player_str]
        mock_room_manager.get_room_occupants.return_value = updated_occupants

        # Publish the event and manually trigger the async handler
        event_bus.publish(leave_event)

        # Manually call the async handler since event bus can't run it in test environment
        await connection_manager._handle_player_left_room(leave_event.__dict__)

        # Wait for event processing
        await asyncio.sleep(0.1)

        # Verify that room_occupants events were broadcast with updated count
        for _player_id, websocket in mock_websockets.items():
            websocket.send_json.assert_called()

            call_args = websocket.send_json.call_args[0][0]
            assert call_args["event_type"] == "room_occupants"
            assert call_args["room_id"] == room_id
            assert call_args["data"]["count"] == 2
            assert len(call_args["data"]["occupants"]) == 2
            assert "Player2" not in call_args["data"]["occupants"]

    @pytest.mark.asyncio
    async def test_rapid_movement_scenario(
        self, connection_manager, event_bus, mock_room_manager, mock_players, mock_websockets, sample_occupants
    ):
        """Test occupant count updates during rapid player movement."""
        # Setup connection manager
        connection_manager.room_manager = mock_room_manager
        mock_room_manager.get_room_occupants.return_value = sample_occupants

        # Connect players
        room_id = "arkham_001"
        session_id = "test_session"

        for player_id_str, websocket in mock_websockets.items():
            # Convert string ID to UUID for connect_websocket
            player_id_uuid = _str_to_uuid(player_id_str)
            await connection_manager.connect_websocket(websocket, player_id_uuid, session_id)

        await connection_manager.subscribe_to_room_events()

        # Simulate rapid movement: player enters, then immediately leaves
        player_id = uuid4()

        # Player enters
        enter_event = PlayerEnteredRoom(player_id=str(player_id), room_id=room_id)
        enter_event.timestamp = None

        # Update mock for player entering
        updated_occupants = sample_occupants + [{"player_name": "Player5", "player_id": str(player_id)}]
        mock_room_manager.get_room_occupants.return_value = updated_occupants

        event_bus.publish(enter_event)

        # Manually call the async handler since event bus can't run it in test environment
        await connection_manager._handle_player_entered_room(enter_event.__dict__)

        # Player immediately leaves
        leave_event = PlayerLeftRoom(player_id=str(player_id), room_id=room_id)
        leave_event.timestamp = None

        # Update mock for player leaving
        mock_room_manager.get_room_occupants.return_value = sample_occupants

        event_bus.publish(leave_event)

        # Manually call the async handler since event bus can't run it in test environment
        await connection_manager._handle_player_left_room(leave_event.__dict__)

        # Wait for event processing
        await asyncio.sleep(0.2)

        # Verify that multiple room_occupants events were sent
        for _player_id, websocket in mock_websockets.items():
            # Should have received at least 2 room_occupants events (enter + leave)
            assert websocket.send_json.call_count >= 2

            # Check the final state (after player left)
            final_call_args = websocket.send_json.call_args[0][0]
            assert final_call_args["event_type"] == "room_occupants"
            assert final_call_args["data"]["count"] == 3  # Back to original count

    @pytest.mark.asyncio
    async def test_connection_failure_handling(
        self, connection_manager, event_bus, mock_room_manager, mock_players, mock_websockets, sample_occupants
    ):
        """Test occupant count updates when some connections fail."""
        # Setup connection manager
        connection_manager.room_manager = mock_room_manager
        mock_room_manager.get_room_occupants.return_value = sample_occupants

        # Connect players
        room_id = "arkham_001"
        session_id = "test_session"

        for player_id_str, websocket in mock_websockets.items():
            # Convert string ID to UUID for connect_websocket
            player_id_uuid = _str_to_uuid(player_id_str)
            await connection_manager.connect_websocket(websocket, player_id_uuid, session_id)

        # Make one connection fail
        failing_websocket = mock_websockets["player_3"]
        failing_websocket.send_json.side_effect = Exception("Connection failed")

        await connection_manager.subscribe_to_room_events()

        # Simulate a player entering
        player_id = uuid4()
        enter_event = PlayerEnteredRoom(player_id=str(player_id), room_id=room_id)
        enter_event.timestamp = None

        updated_occupants = sample_occupants + [{"player_name": "Player6", "player_id": str(player_id)}]
        mock_room_manager.get_room_occupants.return_value = updated_occupants

        event_bus.publish(enter_event)

        # Manually call the async handler since event bus can't run it in test environment
        await connection_manager._handle_player_entered_room(enter_event.__dict__)

        # Wait for event processing
        await asyncio.sleep(0.1)

        # Verify that successful connections received the event
        for player_id_str, websocket in mock_websockets.items():
            if player_id_str != "player_3":  # Skip the failing connection
                websocket.send_json.assert_called()
                call_args = websocket.send_json.call_args[0][0]
                assert call_args["event_type"] == "room_occupants"
                assert call_args["data"]["count"] == 4

    @pytest.mark.asyncio
    async def test_multiple_room_scenario(
        self, connection_manager, event_bus, mock_room_manager, mock_players, mock_websockets, sample_occupants
    ):
        """Test occupant count updates across multiple rooms."""
        # Setup connection manager
        connection_manager.room_manager = mock_room_manager

        # Connect players to different rooms
        room1_id = "arkham_001"
        room2_id = "arkham_002"
        session_id = "test_session"

        # Set different room IDs for different players
        mock_players["player_1"].current_room_id = room1_id
        mock_players["player_2"].current_room_id = room1_id
        mock_players["player_3"].current_room_id = room2_id
        mock_players["player_4"].current_room_id = room2_id

        # Connect some players to room 1 (convert string IDs to UUIDs)
        await connection_manager.connect_websocket(mock_websockets["player_1"], _str_to_uuid("player_1"), session_id)
        await connection_manager.connect_websocket(mock_websockets["player_2"], _str_to_uuid("player_2"), session_id)

        # Connect some players to room 2
        await connection_manager.connect_websocket(mock_websockets["player_3"], _str_to_uuid("player_3"), session_id)
        await connection_manager.connect_websocket(mock_websockets["player_4"], _str_to_uuid("player_4"), session_id)

        await connection_manager.subscribe_to_room_events()

        # Simulate player entering room 1
        player_id = uuid4()
        enter_event = PlayerEnteredRoom(player_id=str(player_id), room_id=room1_id)
        enter_event.timestamp = None

        # Mock room 1 occupants
        room1_occupants = sample_occupants[:2] + [{"player_name": "Player5", "player_id": str(player_id)}]

        def mock_get_occupants(room_id, players):
            if room_id == room1_id:
                return room1_occupants
            elif room_id == room2_id:
                return sample_occupants[2:4]  # Different occupants for room 2
            return []

        mock_room_manager.get_room_occupants.side_effect = mock_get_occupants

        event_bus.publish(enter_event)

        # Manually call the async handler since event bus can't run it in test environment
        await connection_manager._handle_player_entered_room(enter_event.__dict__)

        # Wait for event processing
        await asyncio.sleep(0.1)

        # Verify that only players in room 1 received the update
        room1_players = ["player_1", "player_2"]
        room2_players = ["player_3", "player_4"]

        for player_id in room1_players:
            websocket = mock_websockets[player_id]
            websocket.send_json.assert_called()
            call_args = websocket.send_json.call_args[0][0]
            assert call_args["event_type"] == "room_occupants"
            assert call_args["room_id"] == room1_id
            assert call_args["data"]["count"] == 3

        for player_id in room2_players:
            websocket = mock_websockets[player_id]
            # Check that they didn't receive room_occupants events
            calls = websocket.send_json.call_args_list
            room_occupants_calls = [call for call in calls if call[0][0].get("event_type") == "room_occupants"]
            assert len(room_occupants_calls) == 0, f"Player {player_id} should not have received room_occupants events"

    def test_room_occupants_event_structure(self):
        """Test that room_occupants events have the correct structure."""
        room_id = "arkham_001"
        occupants = ["Player1", "Player2", "Player3"]
        count = len(occupants)

        event = build_event("room_occupants", {"occupants": occupants, "count": count}, room_id=room_id)

        # Verify event structure
        assert event["event_type"] == "room_occupants"
        assert event["room_id"] == room_id
        assert "timestamp" in event
        assert "sequence_number" in event

        # Verify data structure
        data = event["data"]
        assert data["occupants"] == occupants
        assert data["count"] == count
        assert isinstance(data["occupants"], list)
        assert isinstance(data["count"], int)

    @pytest.mark.asyncio
    async def test_event_subscription_lifecycle(self, connection_manager, event_bus):
        """Test the lifecycle of event subscriptions."""
        # Initially no subscriptions
        assert len(event_bus._subscribers.get(PlayerEnteredRoom, [])) == 0
        assert len(event_bus._subscribers.get(PlayerLeftRoom, [])) == 0

        # Subscribe to room events
        await connection_manager.subscribe_to_room_events()

        # Verify subscriptions were created
        assert len(event_bus._subscribers.get(PlayerEnteredRoom, [])) == 1
        assert len(event_bus._subscribers.get(PlayerLeftRoom, [])) == 1

        # Unsubscribe from room events
        await connection_manager.unsubscribe_from_room_events()

        # Verify subscriptions were removed
        assert len(event_bus._subscribers.get(PlayerEnteredRoom, [])) == 0
        assert len(event_bus._subscribers.get(PlayerLeftRoom, [])) == 0


# ============================================================================
# Tests merged from test_occupant_count_simple_legacy.py
# ============================================================================


class TestOccupantCountSimpleIntegration:
    """Test occupant count synchronization with simplified setup."""

    @pytest.fixture
    def connection_manager(self):
        """Create a connection manager for testing."""
        return ConnectionManager()

    @pytest.fixture
    def mock_room_manager(self):
        """Create a mock room manager."""
        room_manager = MagicMock()
        room_manager.get_room_occupants = MagicMock(return_value=[])
        room_manager.get_room_subscribers = MagicMock(return_value=[])
        return room_manager

    @pytest.fixture
    def mock_websockets(self):
        """Create mock WebSocket connections."""
        websockets = {}
        for i in range(1, 4):  # Create 3 test WebSockets
            websocket = AsyncMock()
            websocket.send_json = AsyncMock()
            websocket.close = AsyncMock()
            websocket.ping = AsyncMock()
            websockets[f"player_{i}"] = websocket
        return websockets

    @pytest.mark.asyncio
    async def test_room_occupants_event_broadcasting(self, connection_manager, mock_room_manager, mock_websockets):
        """Test that room_occupants events are properly broadcast."""
        # Setup connection manager with room manager
        connection_manager.room_manager = mock_room_manager

        # Setup mock room manager to return sample occupants
        sample_occupants = [
            {"player_name": "Player1", "player_id": "player_1"},
            {"player_name": "Player2", "player_id": "player_2"},
        ]
        mock_room_manager.get_room_occupants.return_value = sample_occupants

        # Connect players
        room_id = "arkham_001"
        session_id = "test_session"

        for player_id_str, websocket in mock_websockets.items():
            # Convert string ID to UUID for connect_websocket
            player_id_uuid = _str_to_uuid(player_id_str)
            await connection_manager.connect_websocket(websocket, player_id_uuid, session_id)

        # Set up room manager to return connected players as room subscribers
        connected_player_ids = list(mock_websockets.keys())
        mock_room_manager.get_room_subscribers.return_value = connected_player_ids

        # Set up room manager to return connected players as room subscribers
        # Convert string IDs to UUID strings to match what broadcast_to_room expects
        connected_player_ids = [str(_str_to_uuid(pid)) for pid in mock_websockets.keys()]
        mock_room_manager.get_room_subscribers.return_value = connected_player_ids

        # Manually trigger room_occupants event broadcasting
        room_occupants_event = build_event(
            "room_occupants", {"occupants": ["Player1", "Player2"], "count": 2}, room_id=room_id
        )

        # Broadcast to all connected players in the room
        await connection_manager.broadcast_to_room(room_id, room_occupants_event)

        # Verify that all connected players received the event
        for _player_id, websocket in mock_websockets.items():
            websocket.send_json.assert_called()
            call_args = websocket.send_json.call_args[0][0]
            assert call_args["event_type"] == "room_occupants"
            assert call_args["room_id"] == room_id
            assert call_args["data"]["count"] == 2

    @pytest.mark.asyncio
    async def test_occupant_count_update_on_player_movement(
        self, connection_manager, mock_room_manager, mock_websockets
    ):
        """Test occupant count updates when players move between rooms."""
        # Setup connection manager
        connection_manager.room_manager = mock_room_manager

        # Connect players to different rooms
        room1_id = "arkham_001"
        room2_id = "arkham_002"
        session_id = "test_session"

        # Connect some players to room 1 (convert string IDs to UUIDs)
        await connection_manager.connect_websocket(mock_websockets["player_1"], _str_to_uuid("player_1"), session_id)
        await connection_manager.connect_websocket(mock_websockets["player_2"], _str_to_uuid("player_2"), session_id)

        # Connect some players to room 2
        await connection_manager.connect_websocket(mock_websockets["player_3"], _str_to_uuid("player_3"), session_id)

        # Set up room manager to return appropriate players for each room
        # Convert string IDs to UUID strings to match what broadcast_to_room expects
        def mock_get_room_subscribers(room_id):
            if room_id == room1_id:
                return [str(_str_to_uuid("player_1")), str(_str_to_uuid("player_2"))]
            elif room_id == room2_id:
                return [str(_str_to_uuid("player_3"))]
            return []

        mock_room_manager.get_room_subscribers.side_effect = mock_get_room_subscribers

        # Broadcast to room 1
        room1_event = build_event(
            "room_occupants", {"occupants": ["Player1", "Player2", "Player4"], "count": 3}, room_id=room1_id
        )
        await connection_manager.broadcast_to_room(room1_id, room1_event)

        # Verify that only players in room 1 received the update
        for player_id in ["player_1", "player_2"]:
            websocket = mock_websockets[player_id]
            websocket.send_json.assert_called()
            call_args = websocket.send_json.call_args[0][0]
            assert call_args["room_id"] == room1_id
            assert call_args["data"]["count"] == 3

        # Verify player_3 didn't receive room1 updates
        mock_websockets["player_3"].send_json.assert_not_called()

    @pytest.mark.asyncio
    async def test_multiple_rapid_updates(self, connection_manager, mock_room_manager, mock_websockets):
        """Test multiple rapid occupant count updates."""
        # Setup connection manager
        connection_manager.room_manager = mock_room_manager

        # Connect players
        room_id = "arkham_001"
        session_id = "test_session"

        for player_id_str, websocket in mock_websockets.items():
            # Convert string ID to UUID for connect_websocket
            player_id_uuid = _str_to_uuid(player_id_str)
            await connection_manager.connect_websocket(websocket, player_id_uuid, session_id)

        # Set up room manager to return connected players as room subscribers
        # Convert string IDs to UUID strings to match what broadcast_to_room expects
        connected_player_ids = [str(_str_to_uuid(pid)) for pid in mock_websockets.keys()]
        mock_room_manager.get_room_subscribers.return_value = connected_player_ids

        # Send multiple rapid updates
        for i in range(3):
            occupants_event = build_event(
                "room_occupants", {"occupants": [f"Player{j}" for j in range(i + 1)], "count": i + 1}, room_id=room_id
            )
            await connection_manager.broadcast_to_room(room_id, occupants_event)

        # Verify that all players received all updates
        for _player_id, websocket in mock_websockets.items():
            assert websocket.send_json.call_count == 3
            # Check the final update
            final_call_args = websocket.send_json.call_args[0][0]
            assert final_call_args["event_type"] == "room_occupants"
            assert final_call_args["data"]["count"] == 3
