"""
Unit tests for WebSocket handler validation, rate limiting, and error paths.

Tests _check_rate_limit, _validate_message, _send_error_response variants,
_handle_websocket_disconnect, _handle_runtime_error, cleanup/chat/game command errors.
"""

import uuid
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from server.error_types import ErrorType
from server.realtime.websocket_handler import (
    _check_rate_limit,
    _cleanup_connection,
    _handle_runtime_error,
    _handle_websocket_disconnect,
    _is_websocket_disconnected,
    _process_exception_in_message_loop,
    _send_error_response,
    _validate_message,
    _validate_player_and_persistence,
    handle_chat_message,
    handle_game_command,
    handle_websocket_message,
    process_websocket_command,
    send_system_message,
)

# Test UUID constant for player IDs
TEST_PLAYER_ID = uuid.UUID("12345678-1234-5678-1234-567812345678")
TEST_PLAYER_ID_STR = str(TEST_PLAYER_ID)

# pylint: disable=protected-access  # Reason: Test file - accessing protected members is standard practice


def test_is_websocket_disconnected():
    """Test _is_websocket_disconnected detects disconnection messages."""
    assert _is_websocket_disconnected("WebSocket is not connected") is True
    assert _is_websocket_disconnected('Need to call "accept" first') is True
    assert _is_websocket_disconnected("Some other error") is False


@pytest.mark.asyncio
async def test_check_rate_limit_no_connection_id(mock_websocket, mock_ws_connection_manager):
    """Test _check_rate_limit returns True when no connection_id."""
    result = await _check_rate_limit(mock_websocket, None, TEST_PLAYER_ID_STR, mock_ws_connection_manager)
    assert result is True
    mock_websocket.send_json.assert_not_awaited()


@pytest.mark.asyncio
async def test_check_rate_limit_passed(mock_websocket, mock_ws_connection_manager):
    """Test _check_rate_limit returns True when rate limit check passes."""
    mock_rate_limiter = MagicMock()
    mock_rate_limiter.check_message_rate_limit = MagicMock(return_value=True)
    mock_ws_connection_manager.rate_limiter = mock_rate_limiter
    result = await _check_rate_limit(mock_websocket, "conn_001", TEST_PLAYER_ID_STR, mock_ws_connection_manager)
    assert result is True
    mock_websocket.send_json.assert_not_awaited()


@pytest.mark.asyncio
async def test_check_rate_limit_exceeded(mock_websocket, mock_ws_connection_manager):
    """Test _check_rate_limit returns False and sends error when rate limit exceeded."""
    mock_rate_limiter = MagicMock()
    mock_rate_limiter.check_message_rate_limit = MagicMock(return_value=False)
    mock_rate_limiter.get_message_rate_limit_info = MagicMock(return_value={"max_attempts": 10, "reset_time": 1000})
    mock_ws_connection_manager.rate_limiter = mock_rate_limiter
    result = await _check_rate_limit(mock_websocket, "conn_001", TEST_PLAYER_ID_STR, mock_ws_connection_manager)
    assert result is False
    mock_websocket.send_json.assert_awaited_once()


@pytest.mark.asyncio
async def test_validate_message_success(mock_websocket):
    """Test _validate_message returns message when validation succeeds."""
    mock_validator = MagicMock()
    mock_message = {"type": "test"}
    mock_validator.parse_and_validate = MagicMock(return_value=mock_message)
    result = await _validate_message(mock_websocket, '{"type": "test"}', TEST_PLAYER_ID_STR, mock_validator)
    assert result == mock_message
    mock_websocket.send_json.assert_not_awaited()


@pytest.mark.asyncio
async def test_validate_message_validation_error(mock_websocket):
    """Test _validate_message returns None and sends error when validation fails."""
    from server.realtime.message_validator import MessageValidationError

    mock_validator = MagicMock()
    mock_error = MessageValidationError("Invalid message", ErrorType.INVALID_FORMAT.value)
    mock_validator.parse_and_validate = MagicMock(side_effect=mock_error)
    result = await _validate_message(mock_websocket, "invalid", TEST_PLAYER_ID_STR, mock_validator)
    assert result is None
    mock_websocket.send_json.assert_awaited_once()


@pytest.mark.asyncio
async def test_send_error_response_websocket_disconnect(mock_websocket):
    """Test _send_error_response handles WebSocket disconnect."""
    from fastapi import WebSocketDisconnect

    mock_websocket.send_json = AsyncMock(side_effect=WebSocketDisconnect(1000))
    result = await _send_error_response(mock_websocket, ErrorType.VALIDATION_ERROR, "Test error", "Error message", {})
    assert result is True


@pytest.mark.asyncio
async def test_send_error_response_runtime_error_disconnected(mock_websocket):
    """Test _send_error_response handles RuntimeError with disconnect message."""
    mock_websocket.send_json = AsyncMock(side_effect=RuntimeError("WebSocket is not connected"))
    result = await _send_error_response(mock_websocket, ErrorType.VALIDATION_ERROR, "Test error", "Error message", {})
    assert result is False


@pytest.mark.asyncio
async def test_send_error_response_runtime_error_close_message(mock_websocket):
    """Test _send_error_response handles RuntimeError with close message."""
    mock_websocket.send_json = AsyncMock(side_effect=RuntimeError("close message has been sent"))
    result = await _send_error_response(mock_websocket, ErrorType.VALIDATION_ERROR, "Test error", "Error message", {})
    assert result is False


@pytest.mark.asyncio
async def test_send_error_response_runtime_error_other(mock_websocket):
    """Test _send_error_response handles other RuntimeError."""
    mock_websocket.send_json = AsyncMock(side_effect=RuntimeError("Some other error"))
    result = await _send_error_response(mock_websocket, ErrorType.VALIDATION_ERROR, "Test error", "Error message", {})
    assert result is True


def test_handle_websocket_disconnect():
    """Test _handle_websocket_disconnect returns True."""
    result = _handle_websocket_disconnect(TEST_PLAYER_ID_STR, "conn_001")
    assert result is True


def test_handle_websocket_disconnect_no_connection_id():
    """Test _handle_websocket_disconnect handles None connection_id."""
    result = _handle_websocket_disconnect(TEST_PLAYER_ID_STR, None)
    assert result is True


def test_handle_runtime_error_disconnected():
    """Test _handle_runtime_error returns (True, False) for disconnected error."""
    error = RuntimeError("WebSocket is not connected")
    should_break, should_raise = _handle_runtime_error(error, TEST_PLAYER_ID_STR, "conn_001")
    assert should_break is True
    assert should_raise is False


def test_handle_runtime_error_other():
    """Test _handle_runtime_error returns (False, True) for other runtime error."""
    error = RuntimeError("Some other runtime error")
    should_break, should_raise = _handle_runtime_error(error, TEST_PLAYER_ID_STR, "conn_001")
    assert should_break is False
    assert should_raise is True


@pytest.mark.asyncio
async def test_process_exception_in_message_loop(mock_websocket):
    """Test _process_exception_in_message_loop processes exception."""
    error = ValueError("Test error")
    with patch(
        "server.realtime.websocket_handler._handle_message_loop_exception",
        new_callable=AsyncMock,
        return_value=(False, False),
    ):
        should_break, should_raise = await _process_exception_in_message_loop(
            mock_websocket, error, uuid.uuid4(), TEST_PLAYER_ID_STR, "conn_001"
        )
        assert isinstance(should_break, bool)
        assert isinstance(should_raise, bool)


@pytest.mark.asyncio
async def test_cleanup_connection_exception(mock_ws_connection_manager):
    """Test _cleanup_connection handles exception during disconnect."""
    from fastapi import WebSocketDisconnect

    player_id = uuid.uuid4()
    mock_ws_connection_manager.disconnect_websocket = AsyncMock(side_effect=WebSocketDisconnect(1000))
    await _cleanup_connection(player_id, str(player_id), mock_ws_connection_manager)
    mock_ws_connection_manager.disconnect_websocket.assert_awaited_once()


@pytest.mark.asyncio
async def test_cleanup_connection_runtime_error(mock_ws_connection_manager):
    """Test _cleanup_connection handles RuntimeError during disconnect."""
    player_id = uuid.uuid4()
    mock_ws_connection_manager.disconnect_websocket = AsyncMock(side_effect=RuntimeError("Test error"))
    await _cleanup_connection(player_id, str(player_id), mock_ws_connection_manager)


@pytest.mark.asyncio
async def test_validate_player_and_persistence_no_current_room_id(mock_ws_connection_manager):
    """Test _validate_player_and_persistence handles player without current_room_id."""
    mock_player = MagicMock()
    del mock_player.current_room_id
    mock_ws_connection_manager.get_player = AsyncMock(return_value=mock_player)
    player, error = await _validate_player_and_persistence(mock_ws_connection_manager, TEST_PLAYER_ID_STR)
    assert player is None
    assert error is not None


@pytest.mark.asyncio
async def test_handle_chat_message_no_player(mock_websocket, mock_ws_connection_manager):
    """Test handle_chat_message handles player not found."""
    mock_ws_connection_manager.get_player = AsyncMock(return_value=None)
    await handle_chat_message(mock_websocket, TEST_PLAYER_ID_STR, "Hello", mock_ws_connection_manager)


@pytest.mark.asyncio
async def test_handle_chat_message_error(mock_websocket, mock_ws_connection_manager):
    """Test handle_chat_message handles WebSocket error."""
    from fastapi import WebSocketDisconnect

    mock_player = MagicMock()
    mock_player.current_room_id = "room_001"
    mock_ws_connection_manager.get_player = AsyncMock(return_value=mock_player)
    mock_ws_connection_manager.broadcast_to_room = AsyncMock()
    call_count = 0

    async def mock_send_json(*_args, **_kwargs):
        nonlocal call_count
        call_count += 1
        if call_count == 2:
            raise WebSocketDisconnect(1000)

    mock_websocket.send_json = AsyncMock(side_effect=mock_send_json)
    await handle_chat_message(mock_websocket, TEST_PLAYER_ID_STR, "Hello", mock_ws_connection_manager)


@pytest.mark.asyncio
async def test_handle_game_command_with_broadcast(mock_websocket, mock_ws_connection_manager):
    """Test handle_game_command handles broadcast."""
    mock_player = MagicMock()
    mock_player.current_room_id = "room_001"
    mock_ws_connection_manager.get_player = AsyncMock(return_value=mock_player)
    with patch(
        "server.realtime.websocket_handler.process_websocket_command",
        new_callable=AsyncMock,
        return_value={"result": "ok", "broadcast": "message", "broadcast_type": "say"},
    ):
        await handle_game_command(mock_websocket, TEST_PLAYER_ID_STR, "say Hello", None, mock_ws_connection_manager)
        mock_ws_connection_manager.broadcast_to_room.assert_awaited()


@pytest.mark.asyncio
async def test_handle_game_command_broadcast_no_player(mock_websocket, mock_ws_connection_manager):
    """Test handle_game_command handles broadcast when player not found."""
    mock_ws_connection_manager.get_player = AsyncMock(return_value=None)
    with patch(
        "server.realtime.websocket_handler.process_websocket_command",
        new_callable=AsyncMock,
        return_value={"result": "ok", "broadcast": "message", "broadcast_type": "say"},
    ):
        await handle_game_command(mock_websocket, TEST_PLAYER_ID_STR, "say Hello", None, mock_ws_connection_manager)


@pytest.mark.asyncio
async def test_handle_game_command_broadcast_no_current_room_id(mock_websocket, mock_ws_connection_manager):
    """Test handle_game_command handles broadcast when player has no current_room_id."""
    mock_player = MagicMock()
    del mock_player.current_room_id
    mock_ws_connection_manager.get_player = AsyncMock(return_value=mock_player)
    with patch(
        "server.realtime.websocket_handler.process_websocket_command",
        new_callable=AsyncMock,
        return_value={"result": "ok", "broadcast": "message", "broadcast_type": "say"},
    ):
        await handle_game_command(mock_websocket, TEST_PLAYER_ID_STR, "say Hello", None, mock_ws_connection_manager)


@pytest.mark.asyncio
async def test_handle_game_command_with_args(mock_websocket, mock_ws_connection_manager):
    """Test handle_game_command processes command with provided args."""
    with patch(
        "server.realtime.websocket_handler.process_websocket_command",
        new_callable=AsyncMock,
        return_value={"result": "ok"},
    ):
        await handle_game_command(mock_websocket, TEST_PLAYER_ID_STR, "look", ["north"], mock_ws_connection_manager)
        mock_websocket.send_json.assert_awaited_once()


@pytest.mark.asyncio
async def test_handle_game_command_error(mock_websocket, mock_ws_connection_manager):
    """Test handle_game_command handles error."""
    from fastapi import WebSocketDisconnect

    call_count = 0

    async def mock_send_json(*_args, **_kwargs):
        nonlocal call_count
        call_count += 1
        if call_count == 2:
            raise WebSocketDisconnect(1000)

    mock_websocket.send_json = AsyncMock(side_effect=mock_send_json)
    with patch(
        "server.realtime.websocket_handler.process_websocket_command",
        new_callable=AsyncMock,
        return_value={"result": "ok"},
    ):
        await handle_game_command(mock_websocket, TEST_PLAYER_ID_STR, "look", None, mock_ws_connection_manager)


@pytest.mark.asyncio
async def test_handle_websocket_message_error(mock_websocket):
    """Test handle_websocket_message handles error."""
    from fastapi import WebSocketDisconnect

    message = {"type": "command", "command": "look"}
    call_count = 0

    async def mock_send_json(*_args, **_kwargs):
        nonlocal call_count
        call_count += 1
        if call_count == 1:
            return
        raise WebSocketDisconnect(1000)

    mock_websocket.send_json = AsyncMock(side_effect=mock_send_json)
    with patch("server.realtime.message_handler_factory.message_handler_factory") as mock_factory:
        mock_factory.handle_message = AsyncMock(side_effect=RuntimeError("Error"))
        await handle_websocket_message(mock_websocket, TEST_PLAYER_ID_STR, message)


@pytest.mark.asyncio
async def test_send_system_message_error(mock_websocket):
    """Test send_system_message handles error."""
    from fastapi import WebSocketDisconnect

    mock_websocket.send_json = AsyncMock(side_effect=WebSocketDisconnect(1000))
    await send_system_message(mock_websocket, "Test message", "info")


@pytest.mark.asyncio
async def test_process_websocket_command_player_no_current_room_id(mock_ws_connection_manager):
    """Test process_websocket_command handles player without current_room_id."""
    mock_player = MagicMock()
    del mock_player.current_room_id
    mock_player.name = "TestPlayer"
    mock_ws_connection_manager.get_player = AsyncMock(return_value=mock_player)
    result = await process_websocket_command("look", [], TEST_PLAYER_ID_STR, mock_ws_connection_manager)
    assert isinstance(result, dict)
    assert "result" in result
