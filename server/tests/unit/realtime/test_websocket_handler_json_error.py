"""
Unit tests for websocket handler JSON error handling.

Tests the JSON decode error handling functions in websocket_handler.py.
"""

import uuid
from unittest.mock import AsyncMock, MagicMock

import pytest

from server.realtime.websocket_handler import _handle_json_decode_error


@pytest.fixture
def mock_websocket():
    """Create a mock WebSocket."""
    websocket = MagicMock()
    websocket.send_json = AsyncMock()
    return websocket


@pytest.mark.asyncio
async def test_handle_json_decode_error(mock_websocket):
    """Test _handle_json_decode_error() sends error response."""
    player_id = uuid.uuid4()
    await _handle_json_decode_error(mock_websocket, player_id, str(player_id))
    mock_websocket.send_json.assert_awaited_once()
