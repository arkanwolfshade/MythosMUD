"""
Simple integration tests for occupant count synchronization.

This module tests the core occupant count functionality with a simplified
approach that focuses on the essential integration between server and client.
"""

from unittest.mock import AsyncMock, MagicMock

import pytest

from server.realtime.connection_manager import ConnectionManager
from server.realtime.envelope import build_event


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

        for player_id, websocket in mock_websockets.items():
            await connection_manager.connect_websocket(websocket, player_id, session_id)

        # Set up room manager to return connected players as room subscribers
        connected_player_ids = list(mock_websockets.keys())
        mock_room_manager.get_room_subscribers.return_value = connected_player_ids

        # Manually trigger room_occupants event broadcasting
        # This simulates what happens when a player enters/leaves a room
        room_occupants_event = build_event(
            "room_occupants", {"occupants": ["Player1", "Player2"], "count": 2}, room_id=room_id
        )

        # Broadcast to all connected players in the room
        await connection_manager.broadcast_to_room(room_id, room_occupants_event)

        # Verify that all connected players received the event
        for _player_id, websocket in mock_websockets.items():
            websocket.send_json.assert_called()

            # Get the call arguments to verify event structure
            call_args = websocket.send_json.call_args[0][0]
            assert call_args["event_type"] == "room_occupants"
            assert call_args["room_id"] == room_id
            assert call_args["data"]["count"] == 2
            assert len(call_args["data"]["occupants"]) == 2
            assert "Player1" in call_args["data"]["occupants"]
            assert "Player2" in call_args["data"]["occupants"]

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

        # Connect some players to room 1
        await connection_manager.connect_websocket(mock_websockets["player_1"], "player_1", session_id)
        await connection_manager.connect_websocket(mock_websockets["player_2"], "player_2", session_id)

        # Connect some players to room 2
        await connection_manager.connect_websocket(mock_websockets["player_3"], "player_3", session_id)

        # Set up room manager to return appropriate players for each room
        def mock_get_room_subscribers(room_id):
            if room_id == room1_id:
                return ["player_1", "player_2"]
            elif room_id == room2_id:
                return ["player_3"]
            return []

        mock_room_manager.get_room_subscribers.side_effect = mock_get_room_subscribers

        # Simulate player entering room 1
        room1_occupants = [
            {"player_name": "Player1", "player_id": "player_1"},
            {"player_name": "Player2", "player_id": "player_2"},
            {"player_name": "Player4", "player_id": "player_4"},  # New player
        ]

        def mock_get_occupants(room_id, players):
            if room_id == room1_id:
                return room1_occupants
            elif room_id == room2_id:
                return [{"player_name": "Player3", "player_id": "player_3"}]
            return []

        mock_room_manager.get_room_occupants.side_effect = mock_get_occupants

        # Create room_occupants event for room 1
        room1_event = build_event(
            "room_occupants", {"occupants": ["Player1", "Player2", "Player4"], "count": 3}, room_id=room1_id
        )

        # Broadcast to room 1
        await connection_manager.broadcast_to_room(room1_id, room1_event)

        # Verify that only players in room 1 received the update
        room1_players = ["player_1", "player_2"]
        room2_players = ["player_3"]

        for player_id in room1_players:
            websocket = mock_websockets[player_id]
            websocket.send_json.assert_called()
            call_args = websocket.send_json.call_args[0][0]
            assert call_args["room_id"] == room1_id
            assert call_args["data"]["count"] == 3

        for player_id in room2_players:
            websocket = mock_websockets[player_id]
            websocket.send_json.assert_not_called()

    @pytest.mark.asyncio
    async def test_connection_failure_handling(self, connection_manager, mock_room_manager, mock_websockets):
        """Test occupant count updates when some connections fail."""
        # Setup connection manager
        connection_manager.room_manager = mock_room_manager

        # Connect players
        room_id = "arkham_001"
        session_id = "test_session"

        for player_id, websocket in mock_websockets.items():
            await connection_manager.connect_websocket(websocket, player_id, session_id)

        # Set up room manager to return connected players as room subscribers
        connected_player_ids = list(mock_websockets.keys())
        mock_room_manager.get_room_subscribers.return_value = connected_player_ids

        # Make one connection fail
        failing_websocket = mock_websockets["player_2"]
        failing_websocket.send_json.side_effect = Exception("Connection failed")

        # Create room_occupants event
        occupants_event = build_event(
            "room_occupants", {"occupants": ["Player1", "Player2", "Player3"], "count": 3}, room_id=room_id
        )

        # Broadcast to room
        await connection_manager.broadcast_to_room(room_id, occupants_event)

        # Verify that successful connections received the event
        for player_id, websocket in mock_websockets.items():
            if player_id != "player_2":  # Skip the failing connection
                websocket.send_json.assert_called()
                call_args = websocket.send_json.call_args[0][0]
                assert call_args["event_type"] == "room_occupants"
                assert call_args["data"]["count"] == 3

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
    async def test_multiple_rapid_updates(self, connection_manager, mock_room_manager, mock_websockets):
        """Test multiple rapid occupant count updates."""
        # Setup connection manager
        connection_manager.room_manager = mock_room_manager

        # Connect players
        room_id = "arkham_001"
        session_id = "test_session"

        for player_id, websocket in mock_websockets.items():
            await connection_manager.connect_websocket(websocket, player_id, session_id)

        # Set up room manager to return connected players as room subscribers
        connected_player_ids = list(mock_websockets.keys())
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
            assert len(final_call_args["data"]["occupants"]) == 3
