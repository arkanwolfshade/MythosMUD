"""
Unit tests for message handlers.

Tests the message_handlers module functions.
"""

from unittest.mock import AsyncMock, MagicMock, patch

import pytest
from fastapi import WebSocket

from server.realtime.message_handlers import handle_chat_message, handle_command_message, handle_ping_message


@pytest.mark.asyncio
async def test_handle_command_message():
    """Test handle_command_message() delegates to handle_game_command."""
    mock_websocket = AsyncMock(spec=WebSocket)
    player_id = "player_123"
    data = {"command": "look", "args": []}

    with patch("server.realtime.websocket_handler.handle_game_command") as mock_handle:
        await handle_command_message(mock_websocket, player_id, data)

        mock_handle.assert_called_once_with(mock_websocket, player_id, "look", [])


@pytest.mark.asyncio
async def test_handle_command_message_no_command():
    """Test handle_command_message() handles missing command."""
    mock_websocket = AsyncMock(spec=WebSocket)
    player_id = "player_123"
    data = {"args": []}

    with patch("server.realtime.websocket_handler.handle_game_command") as mock_handle:
        await handle_command_message(mock_websocket, player_id, data)

        mock_handle.assert_called_once_with(mock_websocket, player_id, "", [])


@pytest.mark.asyncio
async def test_handle_command_message_no_args():
    """Test handle_command_message() handles missing args."""
    mock_websocket = AsyncMock(spec=WebSocket)
    player_id = "player_123"
    data = {"command": "look"}

    with patch("server.realtime.websocket_handler.handle_game_command") as mock_handle:
        await handle_command_message(mock_websocket, player_id, data)

        mock_handle.assert_called_once_with(mock_websocket, player_id, "look", [])


@pytest.mark.asyncio
async def test_handle_chat_message():
    """Test handle_chat_message() delegates to websocket_handler.handle_chat_message."""
    mock_websocket = AsyncMock(spec=WebSocket)
    player_id = "player_123"
    data = {"message": "Hello world"}

    with patch("server.realtime.websocket_handler.handle_chat_message") as mock_handle:
        await handle_chat_message(mock_websocket, player_id, data)

        mock_handle.assert_called_once_with(mock_websocket, player_id, "Hello world")


@pytest.mark.asyncio
async def test_handle_chat_message_no_message():
    """Test handle_chat_message() handles missing message."""
    mock_websocket = AsyncMock(spec=WebSocket)
    player_id = "player_123"
    data = {}

    with patch("server.realtime.websocket_handler.handle_chat_message") as mock_handle:
        await handle_chat_message(mock_websocket, player_id, data)

        mock_handle.assert_called_once_with(mock_websocket, player_id, "")


@pytest.mark.asyncio
async def test_handle_ping_message():
    """Test handle_ping_message() sends pong response."""
    mock_websocket = AsyncMock(spec=WebSocket)
    player_id = "player_123"
    data = {}

    with patch("server.realtime.envelope.build_event") as mock_build_event:
        mock_build_event.return_value = {"type": "pong", "data": {}}
        await handle_ping_message(mock_websocket, player_id, data)

        mock_build_event.assert_called_once_with("pong", {}, player_id=player_id)
        mock_websocket.send_json.assert_called_once()


@pytest.mark.asyncio
async def test_handle_ping_message_with_data():
    """Test handle_ping_message() ignores data and sends pong."""
    mock_websocket = AsyncMock(spec=WebSocket)
    player_id = "player_123"
    data = {"timestamp": 1234567890}

    with patch("server.realtime.envelope.build_event") as mock_build_event:
        mock_build_event.return_value = {"type": "pong", "data": {}}
        await handle_ping_message(mock_websocket, player_id, data)

        mock_build_event.assert_called_once_with("pong", {}, player_id=player_id)
        mock_websocket.send_json.assert_called_once()
