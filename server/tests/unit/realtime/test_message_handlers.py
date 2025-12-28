"""
Unit tests for message handlers.

Tests the message handler functions in message_handlers.py.
"""

from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from server.realtime.message_handlers import handle_chat_message, handle_command_message, handle_ping_message


@pytest.fixture
def mock_websocket():
    """Create a mock WebSocket."""
    websocket = MagicMock()
    websocket.send_json = AsyncMock()
    return websocket


@pytest.mark.asyncio
async def test_handle_command_message(mock_websocket):
    """Test handle_command_message() processes command."""
    data = {"command": "look", "args": []}
    with patch("server.realtime.websocket_handler.handle_game_command") as mock_handle:
        mock_handle.return_value = AsyncMock()
        await handle_command_message(mock_websocket, "player_001", data)
        mock_handle.assert_awaited_once_with(mock_websocket, "player_001", "look", [])


@pytest.mark.asyncio
async def test_handle_chat_message(mock_websocket):
    """Test handle_chat_message() processes chat."""
    data = {"message": "Hello"}
    # Mock the app.state.container that handle_chat_message tries to access
    with patch("server.main.app") as mock_app:
        mock_app.state = MagicMock()
        mock_app.state.container = MagicMock()
        mock_connection_manager = MagicMock()
        mock_connection_manager.get_player = AsyncMock(return_value=MagicMock(current_room_id="room_001"))
        mock_connection_manager.broadcast_to_room = AsyncMock()
        mock_app.state.container.connection_manager = mock_connection_manager
        with patch("server.realtime.websocket_handler.handle_chat_message") as mock_handle_chat:
            mock_handle_chat.return_value = AsyncMock()
            await handle_chat_message(mock_websocket, "player_001", data)
            # The function imports handle_chat_message from websocket_handler and calls it
            mock_handle_chat.assert_awaited_once()


@pytest.mark.asyncio
async def test_handle_ping_message(mock_websocket):
    """Test handle_ping_message() responds with pong."""
    await handle_ping_message(mock_websocket, "player_001", {})
    mock_websocket.send_json.assert_awaited_once()
