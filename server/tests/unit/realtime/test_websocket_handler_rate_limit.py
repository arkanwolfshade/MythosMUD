"""
Unit tests for websocket handler rate limiting.

Tests the rate limiting functions in websocket_handler.py.
"""

from unittest.mock import AsyncMock, MagicMock

import pytest

from server.realtime.websocket_handler import _check_rate_limit


@pytest.fixture
def mock_websocket():
    """Create a mock WebSocket."""
    return MagicMock()


@pytest.fixture
def mock_connection_manager():
    """Create a mock connection manager."""
    manager = MagicMock()
    manager.rate_limiter = MagicMock()
    return manager


@pytest.mark.asyncio
async def test_check_rate_limit_no_connection_id(mock_websocket, mock_connection_manager):
    """Test _check_rate_limit() returns True when no connection_id."""
    result = await _check_rate_limit(mock_websocket, None, "player_001", mock_connection_manager)
    assert result is True


@pytest.mark.asyncio
async def test_check_rate_limit_passed(mock_websocket, mock_connection_manager):
    """Test _check_rate_limit() returns True when rate limit check passes."""
    mock_connection_manager.rate_limiter.check_message_rate_limit = MagicMock(return_value=True)
    result = await _check_rate_limit(mock_websocket, "conn_001", "player_001", mock_connection_manager)
    assert result is True


@pytest.mark.asyncio
async def test_check_rate_limit_exceeded(mock_websocket, mock_connection_manager):
    """Test _check_rate_limit() returns False when rate limit exceeded."""
    mock_connection_manager.rate_limiter.check_message_rate_limit = MagicMock(return_value=False)
    mock_connection_manager.rate_limiter.get_message_rate_limit_info = MagicMock(
        return_value={"max_attempts": 10, "reset_time": 1000.0}
    )
    mock_websocket.send_json = AsyncMock()
    result = await _check_rate_limit(mock_websocket, "conn_001", "player_001", mock_connection_manager)
    assert result is False
    mock_websocket.send_json.assert_awaited_once()
