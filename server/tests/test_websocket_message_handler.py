"""
Tests for WebSocket message handler functionality.

This module tests the message type routing and command processing
before and after refactoring to ensure no regressions.
"""

from unittest.mock import AsyncMock, MagicMock, patch

import pytest
from fastapi import WebSocket

from ..error_types import ErrorType
from ..realtime.websocket_handler import handle_game_command, handle_websocket_message


class TestWebSocketMessageHandler:
    """Test suite for WebSocket message handling."""

    @pytest.fixture
    def mock_websocket(self):
        """Create a mock WebSocket for testing."""
        websocket = AsyncMock(spec=WebSocket)
        websocket.send_json = AsyncMock()
        return websocket

    @pytest.fixture
    def mock_connection_manager(self):
        """Mock the connection manager."""
        with patch("server.realtime.websocket_handler.connection_manager") as mock_cm:
            mock_cm._get_player.return_value = MagicMock()
            mock_cm._get_player.return_value.current_room_id = "test_room"
            yield mock_cm

    @pytest.mark.asyncio
    async def test_handle_command_message(self, mock_websocket, mock_connection_manager):
        """Test handling of command message type."""
        message = {"type": "command", "data": {"command": "look", "args": []}}

        with patch("server.realtime.websocket_handler.handle_game_command") as mock_handler:
            await handle_websocket_message(mock_websocket, "test_player", message)

            mock_handler.assert_called_once_with(mock_websocket, "test_player", "look", [])

    @pytest.mark.asyncio
    async def test_handle_chat_message(self, mock_websocket, mock_connection_manager):
        """Test handling of chat message type."""
        message = {"type": "chat", "data": {"message": "Hello, world!"}}

        with patch("server.realtime.websocket_handler.handle_chat_message") as mock_handler:
            await handle_websocket_message(mock_websocket, "test_player", message)

            mock_handler.assert_called_once_with(mock_websocket, "test_player", "Hello, world!")

    @pytest.mark.asyncio
    async def test_handle_ping_message(self, mock_websocket):
        """Test handling ping message."""
        message = {"type": "ping", "data": {}}

        await handle_websocket_message(mock_websocket, "test_player", message)

        # Verify pong event was sent with new envelope format
        mock_websocket.send_json.assert_called_once()
        call_args = mock_websocket.send_json.call_args[0][0]
        assert call_args["event_type"] == "pong"
        assert "timestamp" in call_args
        assert "sequence_number" in call_args
        assert call_args["data"] == {}
        assert call_args["player_id"] == "test_player"

    @pytest.mark.asyncio
    async def test_handle_unknown_message_type(self, mock_websocket, mock_connection_manager):
        """Test handling of unknown message type."""
        message = {"type": "unknown_type", "data": {}}

        await handle_websocket_message(mock_websocket, "test_player", message)

        # Verify error response was sent
        mock_websocket.send_json.assert_called_once()
        call_args = mock_websocket.send_json.call_args[0][0]
        assert call_args["error_type"] == ErrorType.INVALID_COMMAND.value
        assert "Unknown message type: unknown_type" in call_args["message"]

    @pytest.mark.asyncio
    async def test_handle_message_with_exception(self, mock_websocket, mock_connection_manager):
        """Test handling of message that raises an exception."""
        message = {"type": "command", "data": {"command": "look", "args": []}}

        with patch("server.realtime.websocket_handler.handle_game_command", side_effect=Exception("Test error")):
            await handle_websocket_message(mock_websocket, "test_player", message)

            # Verify error response was sent
            mock_websocket.send_json.assert_called_once()
            call_args = mock_websocket.send_json.call_args[0][0]
            assert call_args["error_type"] == ErrorType.MESSAGE_PROCESSING_ERROR.value
            assert "Error processing message: Test error" in call_args["message"]

    @pytest.mark.asyncio
    async def test_handle_game_command_with_args(self, mock_websocket, mock_connection_manager):
        """Test game command handling with provided args."""
        with patch("server.realtime.websocket_handler.process_websocket_command") as mock_process:
            mock_process.return_value = {"result": "You see a dark room."}

            await handle_game_command(mock_websocket, "test_player", "look", ["north"])

            mock_process.assert_called_once_with("look", ["north"], "test_player")

    @pytest.mark.asyncio
    async def test_handle_game_command_without_args(self, mock_websocket, mock_connection_manager):
        """Test game command handling without provided args."""
        with patch("server.realtime.websocket_handler.process_websocket_command") as mock_process:
            mock_process.return_value = {"result": "You see a dark room."}

            await handle_game_command(mock_websocket, "test_player", "look north")

            mock_process.assert_called_once_with("look", ["north"], "test_player")

    @pytest.mark.asyncio
    async def test_handle_empty_command(self, mock_websocket, mock_connection_manager):
        """Test handling of empty command."""
        await handle_game_command(mock_websocket, "test_player", "   ")

        # Verify error response was sent
        mock_websocket.send_json.assert_called_once()
        call_args = mock_websocket.send_json.call_args[0][0]
        assert call_args["error_type"] == ErrorType.INVALID_COMMAND.value
        assert "Empty command" in call_args["message"]

    @pytest.mark.asyncio
    async def test_handle_command_with_broadcast(self, mock_websocket, mock_connection_manager):
        """Test command handling with broadcast result."""
        with patch("server.realtime.websocket_handler.process_websocket_command") as mock_process:
            mock_process.return_value = {
                "result": "You say hello!",
                "broadcast": "TestPlayer says hello!",
                "broadcast_type": "say",
            }

            with patch("server.realtime.websocket_handler.build_event") as mock_build:
                mock_build.return_value = {"type": "command_response", "data": {"result": "You say hello!"}}

                await handle_game_command(mock_websocket, "test_player", "say hello")

                # Verify broadcast was called
                mock_connection_manager.broadcast_to_room.assert_called_once()

    @pytest.mark.asyncio
    async def test_handle_command_with_room_change(self, mock_websocket, mock_connection_manager):
        """Test command handling with room change result."""
        with patch("server.realtime.websocket_handler.process_websocket_command") as mock_process:
            mock_process.return_value = {"result": "You move north.", "room_changed": True, "room_id": "new_room"}

            with patch("server.realtime.websocket_handler.broadcast_room_update") as mock_broadcast:
                await handle_game_command(mock_websocket, "test_player", "go north")

                mock_broadcast.assert_called_once_with("test_player", "new_room")

    @pytest.mark.asyncio
    async def test_handle_go_command_with_room_update(self, mock_websocket, mock_connection_manager):
        """Test go command handling with room update."""
        with patch("server.realtime.websocket_handler.process_websocket_command") as mock_process:
            mock_process.return_value = {"result": "You move north."}

            with patch("server.realtime.websocket_handler.broadcast_room_update") as mock_broadcast:
                await handle_game_command(mock_websocket, "test_player", "go north")

                mock_broadcast.assert_called_once_with("test_player", "test_room")
