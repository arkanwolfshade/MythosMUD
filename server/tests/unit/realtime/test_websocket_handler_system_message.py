"""
Unit tests for websocket handler system message functions.

Tests the system message functions in websocket_handler.py.
"""

from unittest.mock import AsyncMock, MagicMock

import pytest

from server.realtime.websocket_handler import send_system_message


@pytest.fixture
def mock_websocket():
    """Create a mock WebSocket."""
    websocket = MagicMock()
    websocket.send_json = AsyncMock()
    return websocket


@pytest.mark.asyncio
async def test_send_system_message_success(mock_websocket):
    """Test send_system_message() successfully sends message."""
    await send_system_message(mock_websocket, "Test message", "info")
    mock_websocket.send_json.assert_awaited_once()


@pytest.mark.asyncio
async def test_send_system_message_warning(mock_websocket):
    """Test send_system_message() with warning type."""
    await send_system_message(mock_websocket, "Warning message", "warning")
    mock_websocket.send_json.assert_awaited_once()


@pytest.mark.asyncio
async def test_send_system_message_error(mock_websocket):
    """Test send_system_message() with error type."""
    await send_system_message(mock_websocket, "Error message", "error")
    mock_websocket.send_json.assert_awaited_once()


@pytest.mark.asyncio
async def test_send_system_message_disconnected(mock_websocket):
    """Test send_system_message() handles WebSocket disconnection."""
    from fastapi import WebSocketDisconnect

    mock_websocket.send_json = AsyncMock(side_effect=WebSocketDisconnect())
    # Should not raise
    await send_system_message(mock_websocket, "Test message", "info")
