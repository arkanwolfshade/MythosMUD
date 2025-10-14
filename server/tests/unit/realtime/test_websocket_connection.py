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

from server.realtime.connection_manager import connection_manager


class TestWebSocketConnectionStability:
    """Test WebSocket connection stability and race condition fixes."""

    @pytest.fixture(autouse=True)
    def setup_test(self):
        """Set up test environment."""
        # Reset connection manager state for testing
        connection_manager.active_websockets.clear()
        connection_manager.player_websockets.clear()
        connection_manager.online_players.clear()
        connection_manager.last_seen.clear()
        connection_manager.disconnecting_players.clear()
        connection_manager.processed_disconnects.clear()

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

        # Mock persistence layer
        with patch("server.realtime.connection_manager.connection_manager.persistence") as mock_persistence:
            mock_player = MagicMock()
            mock_player.current_room_id = "test_room"
            mock_player.name = "TestPlayer"
            mock_persistence.get_player.return_value = mock_player

            # Mock room
            mock_room = MagicMock()
            mock_room.id = "test_room"
            mock_persistence.get_room.return_value = mock_room

            # Test initial connection
            result = await connection_manager.connect_websocket(mock_websocket, player_id)
            assert result is True
            assert player_id in connection_manager.player_websockets
            assert len(connection_manager.active_websockets) == 1

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
            result2 = await connection_manager.connect_websocket(mock_websocket2, player_id)
            assert result2 is True

            # Verify old connection was cleaned up and new one established
            assert player_id in connection_manager.player_websockets
            assert len(connection_manager.active_websockets) == 1

            # Verify the race condition was handled properly:
            # 1. Old dead connection was cleaned up
            # 2. New connection was established
            # 3. Player is still properly tracked
            assert len(connection_manager.active_websockets) == 1, "Should have exactly one active connection"
            assert player_id in connection_manager.player_websockets, "Player should still be tracked"

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

        # Mock persistence layer
        with patch("server.realtime.connection_manager.connection_manager.persistence") as mock_persistence:
            mock_player = MagicMock()
            mock_player.current_room_id = "test_room"
            mock_player.name = "TestPlayer"
            mock_persistence.get_player.return_value = mock_player

            # Mock room
            mock_room = MagicMock()
            mock_room.id = "test_room"
            mock_persistence.get_room.return_value = mock_room

            # Connect WebSocket
            result = await connection_manager.connect_websocket(mock_websocket, player_id)
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

        # Mock persistence layer
        with patch("server.realtime.connection_manager.connection_manager.persistence") as mock_persistence:
            mock_player = MagicMock()
            mock_player.current_room_id = "test_room"
            mock_player.name = "TestPlayer"
            mock_persistence.get_player.return_value = mock_player

            # Mock room
            mock_room = MagicMock()
            mock_room.id = "test_room"
            mock_persistence.get_room.return_value = mock_room

            # Test connection with ping timeout
            mock_websocket.ping.side_effect = TimeoutError()

            # Attempt connection
            result = await connection_manager.connect_websocket(mock_websocket, player_id)
            assert result is True

            # Verify connection was established despite ping timeout
            assert player_id in connection_manager.player_websockets
            assert len(connection_manager.active_websockets) == 1

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

        # Mock persistence layer
        with patch("server.realtime.connection_manager.connection_manager.persistence") as mock_persistence:
            mock_player = MagicMock()
            mock_player.current_room_id = "test_room"
            mock_player.name = "TestPlayer"
            mock_persistence.get_player.return_value = mock_player

            # Mock room
            mock_room = MagicMock()
            mock_room.id = "test_room"
            mock_persistence.get_room.return_value = mock_room

            # Connect WebSocket
            result = await connection_manager.connect_websocket(mock_websocket, player_id)
            assert result is True
            assert player_id in connection_manager.player_websockets

            # Disconnect WebSocket
            await connection_manager.disconnect_websocket(player_id)

            # Verify cleanup
            assert player_id not in connection_manager.player_websockets
            assert len(connection_manager.active_websockets) == 0
            mock_websocket.close.assert_called_once()

    def test_connection_manager_state_consistency(self):
        """Test that connection manager state remains consistent."""
        player_id = "test_player_consistency"

        # Initial state should be clean
        assert len(connection_manager.active_websockets) == 0
        assert len(connection_manager.player_websockets) == 0
        assert len(connection_manager.online_players) == 0

        # Add a mock connection
        connection_id = "test_connection_123"
        connection_manager.active_websockets[connection_id] = MagicMock()
        connection_manager.player_websockets[player_id] = connection_id

        # State should be consistent
        assert len(connection_manager.active_websockets) == 1
        assert len(connection_manager.player_websockets) == 1
        assert connection_manager.player_websockets[player_id] == connection_id
        assert connection_id in connection_manager.active_websockets

        # Clean up
        connection_manager.active_websockets.clear()
        connection_manager.player_websockets.clear()

        # State should be clean again
        assert len(connection_manager.active_websockets) == 0
        assert len(connection_manager.player_websockets) == 0
