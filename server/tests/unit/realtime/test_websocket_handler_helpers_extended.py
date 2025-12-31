"""
Extended unit tests for websocket handler helper functions.

Tests additional helper functions in websocket_handler.py.
"""

import uuid
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from server.error_types import ErrorMessages, ErrorType
from server.realtime.websocket_handler import (
    _check_rate_limit,
    _handle_json_decode_error,
    _handle_websocket_disconnect,
    _send_error_response,
    _validate_message,
)


@pytest.fixture
def mock_websocket():
    """Create a mock WebSocket."""
    websocket = MagicMock()
    websocket.send_json = AsyncMock()
    return websocket


@pytest.fixture
def mock_connection_manager():
    """Create a mock connection manager."""
    manager = MagicMock()
    manager.rate_limiter = MagicMock()
    manager.rate_limiter.check_message_rate_limit = MagicMock(return_value=True)
    manager.rate_limiter.get_message_rate_limit_info = MagicMock(
        return_value={"max_attempts": 60, "reset_time": 1000.0}
    )
    return manager


@pytest.fixture
def mock_validator():
    """Create a mock message validator."""
    validator = MagicMock()
    validator.parse_and_validate = MagicMock(return_value={"type": "test"})
    return validator


@pytest.mark.asyncio
async def test_check_rate_limit_no_connection_id(mock_websocket, mock_connection_manager):
    """Test _check_rate_limit() returns True when no connection_id."""
    result = await _check_rate_limit(mock_websocket, None, "player_001", mock_connection_manager)
    assert result is True
    mock_connection_manager.rate_limiter.check_message_rate_limit.assert_not_called()


@pytest.mark.asyncio
async def test_check_rate_limit_passed(mock_websocket, mock_connection_manager):
    """Test _check_rate_limit() returns True when rate limit check passes."""
    mock_connection_manager.rate_limiter.check_message_rate_limit = MagicMock(return_value=True)
    result = await _check_rate_limit(mock_websocket, "conn_001", "player_001", mock_connection_manager)
    assert result is True
    mock_websocket.send_json.assert_not_called()


@pytest.mark.asyncio
async def test_check_rate_limit_exceeded(mock_websocket, mock_connection_manager):
    """Test _check_rate_limit() returns False when rate limit exceeded."""
    mock_connection_manager.rate_limiter.check_message_rate_limit = MagicMock(return_value=False)
    result = await _check_rate_limit(mock_websocket, "conn_001", "player_001", mock_connection_manager)
    assert result is False
    mock_websocket.send_json.assert_awaited_once()


@pytest.mark.asyncio
async def test_validate_message_success(mock_websocket, mock_validator):
    """Test _validate_message() returns message when validation succeeds."""
    result = await _validate_message(mock_websocket, '{"type": "test"}', "player_001", mock_validator)
    assert result == {"type": "test"}
    mock_websocket.send_json.assert_not_called()


@pytest.mark.asyncio
async def test_validate_message_failure(mock_websocket, mock_validator):
    """Test _validate_message() returns None when validation fails."""
    from server.realtime.message_validator import MessageValidationError

    mock_validator.parse_and_validate = MagicMock(
        side_effect=MessageValidationError("Invalid message", ErrorType.INVALID_FORMAT)
    )
    result = await _validate_message(mock_websocket, "invalid", "player_001", mock_validator)
    assert result is None
    mock_websocket.send_json.assert_awaited_once()


@pytest.mark.asyncio
async def test_send_error_response_success(mock_websocket):
    """Test _send_error_response() returns True when sent successfully."""
    result = await _send_error_response(
        mock_websocket, ErrorType.INVALID_FORMAT, "Test error", ErrorMessages.INVALID_FORMAT, {}
    )
    assert result is True
    mock_websocket.send_json.assert_awaited_once()


@pytest.mark.asyncio
async def test_send_error_response_websocket_disconnect(mock_websocket):
    """Test _send_error_response() handles WebSocketDisconnect."""
    from fastapi import WebSocketDisconnect

    # WebSocketDisconnect() when converted to string is empty string
    # which doesn't match _is_websocket_disconnected check, so it returns True
    mock_websocket.send_json = AsyncMock(side_effect=WebSocketDisconnect())
    result = await _send_error_response(
        mock_websocket, ErrorType.INVALID_FORMAT, "Test error", ErrorMessages.INVALID_FORMAT, {}
    )
    # The function checks str(send_error) which for WebSocketDisconnect() is empty string
    # This doesn't match "WebSocket is not connected" or 'Need to call "accept" first'
    # So it goes to the else branch and returns True
    assert result is True


@pytest.mark.asyncio
async def test_send_error_response_runtime_error_disconnected(mock_websocket):
    """Test _send_error_response() returns False for RuntimeError indicating disconnect."""
    mock_websocket.send_json = AsyncMock(side_effect=RuntimeError("WebSocket is not connected"))
    result = await _send_error_response(
        mock_websocket, ErrorType.INVALID_FORMAT, "Test error", ErrorMessages.INVALID_FORMAT, {}
    )
    assert result is False


@pytest.mark.asyncio
async def test_send_error_response_runtime_error_close_message(mock_websocket):
    """Test _send_error_response() returns False for RuntimeError with close message."""
    mock_websocket.send_json = AsyncMock(side_effect=RuntimeError("close message has been sent"))
    result = await _send_error_response(
        mock_websocket, ErrorType.INVALID_FORMAT, "Test error", ErrorMessages.INVALID_FORMAT, {}
    )
    assert result is False


@pytest.mark.asyncio
async def test_send_error_response_other_error(mock_websocket):
    """Test _send_error_response() returns True for other errors."""
    mock_websocket.send_json = AsyncMock(side_effect=RuntimeError("Some other error"))
    result = await _send_error_response(
        mock_websocket, ErrorType.INVALID_FORMAT, "Test error", ErrorMessages.INVALID_FORMAT, {}
    )
    assert result is True


@pytest.mark.asyncio
async def test_handle_json_decode_error(mock_websocket):
    """Test _handle_json_decode_error() sends error response."""
    player_id = uuid.uuid4()
    await _handle_json_decode_error(mock_websocket, player_id, str(player_id))
    mock_websocket.send_json.assert_awaited_once()


def test_handle_websocket_disconnect(mock_connection_manager):
    """Test _handle_websocket_disconnect() returns True."""
    result = _handle_websocket_disconnect("player_001", "conn_001")
    assert result is True


def test_handle_websocket_disconnect_no_connection_id(mock_connection_manager):
    """Test _handle_websocket_disconnect() returns True even without connection_id."""
    result = _handle_websocket_disconnect("player_001", None)
    assert result is True


def test_handle_runtime_error_disconnected():
    """Test _handle_runtime_error() returns (True, False) for disconnected WebSocket."""
    from server.realtime.websocket_handler import _handle_runtime_error

    error = RuntimeError("WebSocket is not connected")
    should_break, should_raise = _handle_runtime_error(error, "player_001", "conn_001")
    assert should_break is True
    assert should_raise is False


def test_handle_runtime_error_other():
    """Test _handle_runtime_error() returns (False, True) for other RuntimeError."""
    from server.realtime.websocket_handler import _handle_runtime_error

    error = RuntimeError("Some other error")
    should_break, should_raise = _handle_runtime_error(error, "player_001", "conn_001")
    assert should_break is False
    assert should_raise is True


@pytest.mark.asyncio
async def test_handle_generic_exception_success(mock_websocket):
    """Test _handle_generic_exception() returns False when error sent successfully."""
    from server.realtime.websocket_handler import _handle_generic_exception

    error = ValueError("Test error")
    result = await _handle_generic_exception(mock_websocket, error, "player_001", "conn_001")
    assert result is False
    mock_websocket.send_json.assert_awaited_once()


@pytest.mark.asyncio
async def test_handle_generic_exception_disconnected(mock_websocket):
    """Test _handle_generic_exception() returns True when WebSocket disconnected."""
    from server.realtime.websocket_handler import _handle_generic_exception

    mock_websocket.send_json = AsyncMock(side_effect=RuntimeError("WebSocket is not connected"))
    error = ValueError("Test error")
    result = await _handle_generic_exception(mock_websocket, error, "player_001", "conn_001")
    assert result is True


@pytest.mark.asyncio
async def test_process_message_rate_limit_exceeded(mock_websocket, mock_connection_manager, mock_validator):
    """Test _process_message() continues when rate limit exceeded."""
    from server.realtime.websocket_handler import _process_message

    player_id = uuid.uuid4()
    mock_connection_manager.rate_limiter.check_message_rate_limit = MagicMock(return_value=False)
    mock_connection_manager.rate_limiter.get_message_rate_limit_info = MagicMock(
        return_value={"max_attempts": 60, "reset_time": 1000.0}
    )
    result = await _process_message(
        mock_websocket,
        '{"type": "test"}',
        player_id,
        str(player_id),
        "conn_001",
        mock_connection_manager,
        mock_validator,
    )
    assert result is True
    mock_validator.parse_and_validate.assert_not_called()


@pytest.mark.asyncio
async def test_process_message_validation_failed(mock_websocket, mock_connection_manager, mock_validator):
    """Test _process_message() continues when validation fails."""
    from server.realtime.message_validator import MessageValidationError
    from server.realtime.websocket_handler import _process_message

    player_id = uuid.uuid4()
    mock_validator.parse_and_validate = MagicMock(
        side_effect=MessageValidationError("Invalid", ErrorType.INVALID_FORMAT)
    )
    result = await _process_message(
        mock_websocket,
        '{"type": "test"}',
        player_id,
        str(player_id),
        "conn_001",
        mock_connection_manager,
        mock_validator,
    )
    assert result is True
    mock_connection_manager.mark_player_seen.assert_not_called()


@pytest.mark.asyncio
async def test_process_message_success(mock_websocket, mock_connection_manager, mock_validator):
    """Test _process_message() processes message successfully."""
    from server.realtime.websocket_handler import _process_message

    player_id = uuid.uuid4()
    mock_connection_manager.mark_player_seen = MagicMock()
    with patch("server.realtime.websocket_handler.handle_websocket_message", new_callable=AsyncMock) as mock_handle:
        result = await _process_message(
            mock_websocket,
            '{"type": "test"}',
            player_id,
            str(player_id),
            "conn_001",
            mock_connection_manager,
            mock_validator,
        )
        assert result is True
        mock_connection_manager.mark_player_seen.assert_called_once_with(player_id)
        mock_handle.assert_awaited_once()


@pytest.mark.asyncio
async def test_handle_message_loop_exception_json_decode_error(mock_websocket):
    """Test _handle_message_loop_exception() handles JSONDecodeError."""
    import json

    from server.realtime.websocket_handler import _handle_message_loop_exception

    player_id = uuid.uuid4()
    error = json.JSONDecodeError("Invalid JSON", "", 0)
    should_break, should_raise = await _handle_message_loop_exception(
        mock_websocket, error, player_id, str(player_id), "conn_001"
    )
    assert should_break is False
    assert should_raise is False
    mock_websocket.send_json.assert_awaited_once()


@pytest.mark.asyncio
async def test_handle_message_loop_exception_websocket_disconnect(mock_websocket):
    """Test _handle_message_loop_exception() handles WebSocketDisconnect."""
    from fastapi import WebSocketDisconnect

    from server.realtime.websocket_handler import _handle_message_loop_exception

    player_id = uuid.uuid4()
    error = WebSocketDisconnect()
    should_break, should_raise = await _handle_message_loop_exception(
        mock_websocket, error, player_id, str(player_id), "conn_001"
    )
    assert should_break is True
    assert should_raise is False


@pytest.mark.asyncio
async def test_handle_message_loop_exception_runtime_error(mock_websocket):
    """Test _handle_message_loop_exception() handles RuntimeError."""
    from server.realtime.websocket_handler import _handle_message_loop_exception

    player_id = uuid.uuid4()
    error = RuntimeError("WebSocket is not connected")
    should_break, should_raise = await _handle_message_loop_exception(
        mock_websocket, error, player_id, str(player_id), "conn_001"
    )
    assert should_break is True
    assert should_raise is False


@pytest.mark.asyncio
async def test_handle_message_loop_exception_generic(mock_websocket):
    """Test _handle_message_loop_exception() handles generic exception."""
    from server.realtime.websocket_handler import _handle_message_loop_exception

    player_id = uuid.uuid4()
    error = ValueError("Test error")
    should_break, should_raise = await _handle_message_loop_exception(
        mock_websocket, error, player_id, str(player_id), "conn_001"
    )
    assert isinstance(should_break, bool)
    assert should_raise is False
