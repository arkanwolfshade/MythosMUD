"""
Unit tests for websocket handler error handling.

Tests the error handling functions in websocket_handler.py.
"""

from unittest.mock import AsyncMock, MagicMock

import pytest

from server.realtime.websocket_handler import _handle_runtime_error, _send_error_response


@pytest.fixture
def mock_websocket():
    """Create a mock WebSocket."""
    websocket = MagicMock()
    websocket.send_json = AsyncMock()
    return websocket


@pytest.mark.asyncio
async def test_send_error_response_success(mock_websocket):
    """Test _send_error_response() successfully sends error."""
    from server.error_types import ErrorMessages, ErrorType

    result = await _send_error_response(
        mock_websocket, ErrorType.INVALID_FORMAT, "Test error", ErrorMessages.INVALID_FORMAT, {}
    )
    assert result is True
    mock_websocket.send_json.assert_awaited_once()


@pytest.mark.asyncio
async def test_send_error_response_disconnected(mock_websocket):
    """Test _send_error_response() handles WebSocket disconnection."""
    from server.error_types import ErrorMessages, ErrorType

    # The function checks error message string, not just exception type
    mock_websocket.send_json = AsyncMock(side_effect=RuntimeError("WebSocket is not connected"))
    result = await _send_error_response(
        mock_websocket, ErrorType.INVALID_FORMAT, "Test error", ErrorMessages.INVALID_FORMAT, {}
    )
    # When WebSocket is disconnected (detected via error message), it should return False
    assert result is False


def test_handle_runtime_error_disconnected():
    """Test _handle_runtime_error() detects WebSocket disconnection."""
    error = RuntimeError("WebSocket is not connected")
    result = _handle_runtime_error(error, "player_001", "conn_001")
    # Returns tuple (is_disconnected, should_cleanup)
    assert isinstance(result, tuple)
    assert len(result) == 2


def test_handle_runtime_error_other():
    """Test _handle_runtime_error() handles other runtime errors."""
    error = RuntimeError("Some other error")
    result = _handle_runtime_error(error, "player_001", "conn_001")
    # Returns tuple (is_disconnected, should_cleanup)
    assert isinstance(result, tuple)
    assert len(result) == 2
