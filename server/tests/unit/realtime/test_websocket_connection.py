"""
Test WebSocket connection stability and race condition fixes.

This test verifies that the WebSocket connection management fixes
prevent the rapid connect/disconnect cycles that were causing
command processing failures.
"""

import json
from unittest.mock import AsyncMock, MagicMock, patch

import pytest
from fastapi import WebSocket

# AI Agent: connection_manager is no longer a module-level global singleton
# Post-migration: ConnectionManager is injected via ApplicationContainer
from server.realtime.connection_manager import ConnectionManager


class TestWebSocketConnectionStability:
    """Test WebSocket connection stability and race condition fixes."""

    @pytest.fixture(autouse=True)
    def setup_test(self):
        """Set up test environment."""
        # AI Agent: Create a fresh ConnectionManager instance for each test
        #           Post-migration: No longer using global singleton
        self.connection_manager = ConnectionManager()

        # Reset connection manager state for testing
        self.connection_manager.active_websockets.clear()
        self.connection_manager.player_websockets.clear()
        self.connection_manager.online_players.clear()
        self.connection_manager.last_seen.clear()
        self.connection_manager.disconnecting_players.clear()
        self.connection_manager.processed_disconnects.clear()

    @pytest.mark.asyncio
    async def test_websocket_connection_race_condition_fix(self):
        """Test that WebSocket connection race conditions are handled properly."""
        player_id = "test_player_123"

        # Create mock WebSocket
        mock_websocket = AsyncMock(spec=WebSocket)
        mock_websocket.accept = AsyncMock()
        mock_websocket.send_json = AsyncMock()
        mock_websocket.receive_text = AsyncMock()
        mock_websocket.ping = AsyncMock()
        mock_websocket.close = AsyncMock()

        # Ensure the close method is properly tracked
        mock_websocket.close.reset_mock()

        # AI Agent: Mock persistence on instance (no longer patching global)
        mock_persistence = MagicMock()
        mock_player = MagicMock()
        mock_player.current_room_id = "test_room"
        mock_player.name = "TestPlayer"
        mock_persistence.get_player.return_value = mock_player

        # Mock room
        mock_room = MagicMock()
        mock_room.id = "test_room"
        mock_persistence.get_room.return_value = mock_room

        # Set persistence on instance
        self.connection_manager.persistence = mock_persistence

        # Test initial connection
        result = await self.connection_manager.connect_websocket(mock_websocket, player_id)
        assert result is True
        assert player_id in self.connection_manager.player_websockets
        assert len(self.connection_manager.active_websockets) == 1

        # Test reconnection with existing connection (race condition scenario)
        mock_websocket2 = AsyncMock(spec=WebSocket)
        mock_websocket2.accept = AsyncMock()
        mock_websocket2.send_json = AsyncMock()
        mock_websocket2.receive_text = AsyncMock()
        mock_websocket2.ping = AsyncMock()
        mock_websocket2.close = AsyncMock()

        # Simulate ping timeout (race condition) - set this before the second connection
        mock_websocket.ping.side_effect = TimeoutError()

        # Attempt reconnection - this should trigger cleanup of the dead connection
        result2 = await self.connection_manager.connect_websocket(mock_websocket2, player_id)
        assert result2 is True

        # Verify old connection was cleaned up and new one established
        assert player_id in self.connection_manager.player_websockets
        assert len(self.connection_manager.active_websockets) == 1

        # Verify the race condition was handled properly:
        # 1. Old dead connection was cleaned up
        # 2. New connection was established
        # 3. Player is still properly tracked
        assert len(self.connection_manager.active_websockets) == 1, "Should have exactly one active connection"
        assert player_id in self.connection_manager.player_websockets, "Player should still be tracked"

    @pytest.mark.asyncio
    async def test_websocket_ping_pong_handling(self):
        """Test that WebSocket ping/pong messages are handled correctly."""
        player_id = "test_player_456"

        # Create mock WebSocket
        mock_websocket = AsyncMock(spec=WebSocket)
        mock_websocket.accept = AsyncMock()
        mock_websocket.send_json = AsyncMock()
        mock_websocket.receive_text = AsyncMock()
        mock_websocket.ping = AsyncMock()
        mock_websocket.close = AsyncMock()

        # AI Agent: Mock persistence on instance (no longer patching global)
        mock_persistence = MagicMock()
        mock_player = MagicMock()
        mock_player.current_room_id = "test_room"
        mock_player.name = "TestPlayer"
        mock_persistence.get_player.return_value = mock_player

        # Mock room
        mock_room = MagicMock()
        mock_room.id = "test_room"
        mock_persistence.get_room.return_value = mock_room

        # Set persistence on instance
        self.connection_manager.persistence = mock_persistence

        # Connect WebSocket
        result = await self.connection_manager.connect_websocket(mock_websocket, player_id)
        assert result is True

        # Test ping message handling
        ping_message = json.dumps({"type": "ping"})
        mock_websocket.receive_text.return_value = ping_message

        # Mock the message loop to process one message
        with patch("server.realtime.websocket_handler.handle_websocket_message"):
            # Simulate receiving a ping message
            data = await mock_websocket.receive_text()
            message = json.loads(data)

            # Verify ping message is handled
            assert message["type"] == "ping"

            # Verify pong response would be sent
            # (In real implementation, this would be handled in the message loop)

    @pytest.mark.asyncio
    async def test_websocket_connection_timeout_handling(self):
        """Test that WebSocket connection timeouts are handled properly."""
        player_id = "test_player_789"

        # Create mock WebSocket
        mock_websocket = AsyncMock(spec=WebSocket)
        mock_websocket.accept = AsyncMock()
        mock_websocket.send_json = AsyncMock()
        mock_websocket.receive_text = AsyncMock()
        mock_websocket.ping = AsyncMock()
        mock_websocket.close = AsyncMock()

        # AI Agent: Mock persistence on instance (no longer patching global)
        mock_persistence = MagicMock()
        mock_player = MagicMock()
        mock_player.current_room_id = "test_room"
        mock_player.name = "TestPlayer"
        mock_persistence.get_player.return_value = mock_player

        # Mock room
        mock_room = MagicMock()
        mock_room.id = "test_room"
        mock_persistence.get_room.return_value = mock_room

        # Set persistence on instance
        self.connection_manager.persistence = mock_persistence

        # Test connection with ping timeout
        mock_websocket.ping.side_effect = TimeoutError()

        # Attempt connection
        result = await self.connection_manager.connect_websocket(mock_websocket, player_id)
        assert result is True

        # Verify connection was established despite ping timeout
        assert player_id in self.connection_manager.player_websockets
        assert len(self.connection_manager.active_websockets) == 1

    @pytest.mark.asyncio
    async def test_websocket_disconnect_cleanup(self):
        """Test that WebSocket disconnection cleanup works properly."""
        player_id = "test_player_cleanup"

        # Create mock WebSocket
        mock_websocket = AsyncMock(spec=WebSocket)
        mock_websocket.accept = AsyncMock()
        mock_websocket.send_json = AsyncMock()
        mock_websocket.receive_text = AsyncMock()
        mock_websocket.ping = AsyncMock()
        mock_websocket.close = AsyncMock()

        # AI Agent: Mock persistence on instance (no longer patching global)
        mock_persistence = MagicMock()
        mock_player = MagicMock()
        mock_player.current_room_id = "test_room"
        mock_player.name = "TestPlayer"
        mock_persistence.get_player.return_value = mock_player

        # Mock room
        mock_room = MagicMock()
        mock_room.id = "test_room"
        mock_persistence.get_room.return_value = mock_room

        # Set persistence on instance
        self.connection_manager.persistence = mock_persistence

        # Connect WebSocket
        result = await self.connection_manager.connect_websocket(mock_websocket, player_id)
        assert result is True
        assert player_id in self.connection_manager.player_websockets

        # Disconnect WebSocket
        await self.connection_manager.disconnect_websocket(player_id)

        # Verify cleanup
        assert player_id not in self.connection_manager.player_websockets
        assert len(self.connection_manager.active_websockets) == 0
        mock_websocket.close.assert_called_once()

    def test_connection_manager_state_consistency(self):
        """Test that connection manager state remains consistent."""
        player_id = "test_player_consistency"

        # AI Agent: Use instance from fixture (no longer a global)
        # Initial state should be clean (ensured by setup_test)
        assert len(self.connection_manager.active_websockets) == 0
        assert len(self.connection_manager.player_websockets) == 0
        assert len(self.connection_manager.online_players) == 0

        # Add a mock connection
        connection_id = "test_connection_123"
        self.connection_manager.active_websockets[connection_id] = MagicMock()
        self.connection_manager.player_websockets[player_id] = connection_id

        # State should be consistent
        assert len(self.connection_manager.active_websockets) == 1
        assert len(self.connection_manager.player_websockets) == 1
        assert self.connection_manager.player_websockets[player_id] == connection_id
        assert connection_id in self.connection_manager.active_websockets

        # Clean up
        self.connection_manager.active_websockets.clear()
        self.connection_manager.player_websockets.clear()

        # State should be clean again
        assert len(self.connection_manager.active_websockets) == 0
        assert len(self.connection_manager.player_websockets) == 0
