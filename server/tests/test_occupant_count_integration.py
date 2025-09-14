"""
Integration tests for occupant count synchronization.

This module tests the complete end-to-end flow of occupant count updates,
including server-side event broadcasting, client-side event handling,
and synchronization across multiple connected clients.
"""

import asyncio
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from server.events import EventBus
from server.events.event_types import PlayerEnteredRoom, PlayerLeftRoom
from server.models import Player
from server.realtime.connection_manager import ConnectionManager
from server.realtime.envelope import build_event


class TestOccupantCountIntegration:
    """Test occupant count synchronization integration."""

    @pytest.fixture
    def event_bus(self):
        """Create a test event bus."""
        return EventBus()

    @pytest.fixture
    def connection_manager(self, event_bus):
        """Create a connection manager with event bus integration."""
        manager = ConnectionManager()

        # Mock the persistence layer to return our event bus
        with patch("server.persistence.get_persistence") as mock_persistence:
            mock_persistence_instance = MagicMock()
            mock_persistence_instance._event_bus = event_bus
            mock_persistence.return_value = mock_persistence_instance

            # Initialize the manager
            manager._get_event_bus = lambda: event_bus

        return manager

    @pytest.fixture
    def mock_room_manager(self):
        """Create a mock room manager."""
        room_manager = MagicMock()
        room_manager.get_room_occupants = MagicMock(return_value=[])
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
        for player_id, websocket in mock_websockets.items():
            await connection_manager.connect_websocket(websocket, player_id, session_id)
            connected_players.append(player_id)

        # Subscribe to room events
        await connection_manager.subscribe_to_room_events()

        # Simulate a player entering the room
        player_id = "player_4"
        new_player = MagicMock(spec=Player)
        new_player.name = "Player4"
        new_player.player_id = player_id
        new_player.current_room_id = room_id

        # Create player entered event
        enter_event = PlayerEnteredRoom(
            timestamp=None, event_type="player_entered", player_id=player_id, room_id=room_id
        )

        # Update mock to include new player in occupants
        updated_occupants = sample_occupants + [{"player_name": "Player4", "player_id": "player_4"}]
        mock_room_manager.get_room_occupants.return_value = updated_occupants

        # Publish the event (publish is synchronous)
        event_bus.publish(enter_event)

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

        for player_id, websocket in mock_websockets.items():
            await connection_manager.connect_websocket(websocket, player_id, session_id)

        await connection_manager.subscribe_to_room_events()

        # Simulate a player leaving the room
        leaving_player_id = "player_2"

        # Create player left event
        leave_event = PlayerLeftRoom(
            timestamp=None, event_type="player_left", player_id=leaving_player_id, room_id=room_id
        )

        # Update mock to reflect player leaving (remove player_2)
        updated_occupants = [occ for occ in sample_occupants if occ["player_id"] != "player_2"]
        mock_room_manager.get_room_occupants.return_value = updated_occupants

        # Publish the event (publish is synchronous)
        event_bus.publish(leave_event)

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

        for player_id, websocket in mock_websockets.items():
            await connection_manager.connect_websocket(websocket, player_id, session_id)

        await connection_manager.subscribe_to_room_events()

        # Simulate rapid movement: player enters, then immediately leaves
        player_id = "player_5"

        # Player enters
        enter_event = PlayerEnteredRoom(
            timestamp=None, event_type="player_entered", player_id=player_id, room_id=room_id
        )

        # Update mock for player entering
        updated_occupants = sample_occupants + [{"player_name": "Player5", "player_id": "player_5"}]
        mock_room_manager.get_room_occupants.return_value = updated_occupants

        event_bus.publish(enter_event)

        # Player immediately leaves
        leave_event = PlayerLeftRoom(timestamp=None, event_type="player_left", player_id=player_id, room_id=room_id)

        # Update mock for player leaving
        mock_room_manager.get_room_occupants.return_value = sample_occupants

        event_bus.publish(leave_event)

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

        for player_id, websocket in mock_websockets.items():
            await connection_manager.connect_websocket(websocket, player_id, session_id)

        # Make one connection fail
        failing_websocket = mock_websockets["player_3"]
        failing_websocket.send_json.side_effect = Exception("Connection failed")

        await connection_manager.subscribe_to_room_events()

        # Simulate a player entering
        player_id = "player_6"
        enter_event = PlayerEnteredRoom(
            timestamp=None, event_type="player_entered", player_id=player_id, room_id=room_id
        )

        updated_occupants = sample_occupants + [{"player_name": "Player6", "player_id": "player_6"}]
        mock_room_manager.get_room_occupants.return_value = updated_occupants

        event_bus.publish(enter_event)

        # Wait for event processing
        await asyncio.sleep(0.1)

        # Verify that successful connections received the event
        for player_id, websocket in mock_websockets.items():
            if player_id != "player_3":  # Skip the failing connection
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

        # Connect some players to room 1
        await connection_manager.connect_websocket(mock_websockets["player_1"], "player_1", session_id)
        await connection_manager.connect_websocket(mock_websockets["player_2"], "player_2", session_id)

        # Connect some players to room 2
        await connection_manager.connect_websocket(mock_websockets["player_3"], "player_3", session_id)
        await connection_manager.connect_websocket(mock_websockets["player_4"], "player_4", session_id)

        await connection_manager.subscribe_to_room_events()

        # Simulate player entering room 1
        player_id = "player_5"
        enter_event = PlayerEnteredRoom(
            timestamp=None, event_type="player_entered", player_id=player_id, room_id=room1_id
        )

        # Mock room 1 occupants
        room1_occupants = sample_occupants[:2] + [{"player_name": "Player5", "player_id": "player_5"}]

        def mock_get_occupants(room_id, players):
            if room_id == room1_id:
                return room1_occupants
            elif room_id == room2_id:
                return sample_occupants[2:4]  # Different occupants for room 2
            return []

        mock_room_manager.get_room_occupants.side_effect = mock_get_occupants

        event_bus.publish(enter_event)

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
            websocket.send_json.assert_not_called()

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
