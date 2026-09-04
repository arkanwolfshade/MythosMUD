"""
Unit tests for websocket handler message validation.

Tests the message validation functions in websocket_handler.py.
"""

from unittest.mock import AsyncMock, MagicMock

import pytest

from server.realtime.websocket_handler import _validate_message


@pytest.fixture
def mock_websocket():
    """Create a mock WebSocket."""
    return MagicMock()


@pytest.fixture
def mock_validator():
    """Create a mock message validator."""
    validator = MagicMock()
    return validator


@pytest.mark.asyncio
async def test_validate_message_success(mock_websocket, mock_validator):
    """Test _validate_message() returns message when validation succeeds."""
    mock_message = {"type": "test", "data": "test"}
    mock_validator.parse_and_validate = MagicMock(return_value=mock_message)
    result = await _validate_message(mock_websocket, '{"type": "test"}', "player_001", mock_validator)
    assert result == mock_message


@pytest.mark.asyncio
async def test_validate_message_failure(mock_websocket, mock_validator):
    """Test _validate_message() returns None when validation fails."""
    from server.realtime.message_validator import MessageValidationError

    mock_validator.parse_and_validate = MagicMock(
        side_effect=MessageValidationError("Invalid message", "validation_error")
    )
    mock_websocket.send_json = AsyncMock()
    result = await _validate_message(mock_websocket, '{"invalid": "json"}', "player_001", mock_validator)
    assert result is None
    mock_websocket.send_json.assert_awaited_once()
