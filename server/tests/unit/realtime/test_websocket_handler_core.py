"""
Unit tests for core websocket handler functions.

Tests core WebSocket handler functions: error handling, message processing,
validation, chat/game commands, and basic app state resolution.
"""

import uuid
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from server.error_types import ErrorType
from server.realtime.websocket_handler import (
    _cleanup_connection,
    _handle_generic_exception,
    _handle_json_decode_error,
    _handle_message_loop_exception,
    _handle_runtime_error,
    _process_message,
    _resolve_and_setup_app_state_services,
    _send_error_response,
    _validate_player_and_persistence,
    get_help_content,
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


@pytest.mark.asyncio
async def test_send_error_response(mock_websocket):
    """Test _send_error_response sends error response."""
    await _send_error_response(mock_websocket, ErrorType.VALIDATION_ERROR, "Test error", "Error message", {})
    mock_websocket.send_json.assert_awaited_once()


@pytest.mark.asyncio
async def test_handle_json_decode_error(mock_websocket):
    """Test _handle_json_decode_error sends error response."""
    await _handle_json_decode_error(mock_websocket, uuid.uuid4(), "player_001")
    mock_websocket.send_json.assert_awaited_once()


def test_handle_runtime_error():
    """Test _handle_runtime_error handles runtime error."""
    error = RuntimeError("Test runtime error")
    should_break, should_raise = _handle_runtime_error(error, "player_001", "conn_001")
    assert isinstance(should_break, bool)
    assert isinstance(should_raise, bool)


@pytest.mark.asyncio
async def test_handle_generic_exception(mock_websocket):
    """Test _handle_generic_exception handles generic exception."""
    error = ValueError("Test error")
    should_break = await _handle_generic_exception(mock_websocket, error, "player_001", "conn_001")
    assert isinstance(should_break, bool)


@pytest.mark.asyncio
async def test_handle_generic_exception_should_break(mock_websocket):
    """Test _handle_generic_exception returns True when send_error_response fails."""
    error = ValueError("Test error")
    with patch("server.realtime.websocket_handler._send_error_response", new_callable=AsyncMock, return_value=False):
        should_break = await _handle_generic_exception(mock_websocket, error, "player_001", "conn_001")
        assert should_break is True


@pytest.mark.asyncio
async def test_handle_message_loop_exception_json_decode(mock_websocket):
    """Test _handle_message_loop_exception handles JSON decode error."""
    from json import JSONDecodeError

    error = JSONDecodeError("Invalid JSON", "doc", 0)
    should_break, should_raise = await _handle_message_loop_exception(
        mock_websocket, error, uuid.uuid4(), "player_001", "conn_001"
    )
    assert should_break is False
    assert should_raise is False


@pytest.mark.asyncio
async def test_handle_message_loop_exception_disconnect(mock_websocket):
    """Test _handle_message_loop_exception handles WebSocket disconnect."""
    from fastapi import WebSocketDisconnect

    error = WebSocketDisconnect(1000)
    should_break, should_raise = await _handle_message_loop_exception(
        mock_websocket, error, uuid.uuid4(), "player_001", "conn_001"
    )
    assert isinstance(should_break, bool)
    assert should_raise is False


@pytest.mark.asyncio
async def test_process_message(mock_websocket, mock_ws_connection_manager):
    """Test _process_message processes message."""
    mock_validator = MagicMock()
    mock_message = {"type": "test"}
    mock_validator.parse_and_validate = AsyncMock(return_value=mock_message)
    with patch("server.realtime.websocket_handler.handle_websocket_message", new_callable=AsyncMock) as mock_handle:
        result = await _process_message(
            mock_websocket,
            '{"type": "test"}',
            uuid.uuid4(),
            "player_001",
            "conn_001",
            mock_ws_connection_manager,
            mock_validator,
        )
        assert result is True
        mock_handle.assert_awaited_once()


@pytest.mark.asyncio
async def test_process_message_rate_limit_exceeded(mock_websocket, mock_ws_connection_manager):
    """Test _process_message returns True when rate limit exceeded."""
    mock_validator = MagicMock()
    with patch("server.realtime.websocket_handler._check_rate_limit", new_callable=AsyncMock, return_value=False):
        result = await _process_message(
            mock_websocket,
            '{"type": "test"}',
            uuid.uuid4(),
            "player_001",
            "conn_001",
            mock_ws_connection_manager,
            mock_validator,
        )
        assert result is True


@pytest.mark.asyncio
async def test_validate_player_and_persistence_success(mock_ws_connection_manager):
    """Test _validate_player_and_persistence validates successfully."""
    mock_player = MagicMock()
    mock_player.current_room_id = "room_001"
    mock_ws_connection_manager.get_player = AsyncMock(return_value=mock_player)
    player, error = await _validate_player_and_persistence(mock_ws_connection_manager, TEST_PLAYER_ID_STR)
    assert player == mock_player
    assert error is None


@pytest.mark.asyncio
async def test_validate_player_and_persistence_not_found(mock_ws_connection_manager):
    """Test _validate_player_and_persistence handles player not found."""
    mock_ws_connection_manager.get_player = AsyncMock(return_value=None)
    player, error = await _validate_player_and_persistence(mock_ws_connection_manager, TEST_PLAYER_ID_STR)
    assert player is None
    assert error is not None


@pytest.mark.asyncio
async def test_validate_player_and_persistence_no_persistence(mock_ws_connection_manager):
    """Test _validate_player_and_persistence handles no persistence."""
    mock_player = MagicMock()
    mock_player.current_room_id = "room_001"
    mock_ws_connection_manager.get_player = AsyncMock(return_value=mock_player)
    mock_ws_connection_manager.async_persistence = None
    player, error = await _validate_player_and_persistence(mock_ws_connection_manager, TEST_PLAYER_ID_STR)
    assert player is None
    assert error is not None


def test_get_help_content():
    """Test get_help_content returns help content."""
    result = get_help_content()
    assert isinstance(result, str)


def test_get_help_content_with_command():
    """Test get_help_content returns help for specific command."""
    result = get_help_content("look")
    assert isinstance(result, str)


@pytest.mark.asyncio
async def test_send_system_message(mock_websocket):
    """Test send_system_message sends system message."""
    await send_system_message(mock_websocket, "Test message", "info")
    mock_websocket.send_json.assert_awaited_once()


@pytest.mark.asyncio
async def test_handle_chat_message(mock_websocket, mock_ws_connection_manager):
    """Test handle_chat_message handles chat message."""
    with patch(
        "server.realtime.websocket_handler.process_websocket_command",
        new_callable=AsyncMock,
        return_value={"result": "ok"},
    ):
        await handle_chat_message(mock_websocket, TEST_PLAYER_ID_STR, "say Hello", mock_ws_connection_manager)
        mock_websocket.send_json.assert_awaited_once()


@pytest.mark.asyncio
async def test_handle_game_command(mock_websocket, mock_ws_connection_manager):
    """Test handle_game_command processes game command."""
    with patch(
        "server.realtime.websocket_handler.process_websocket_command",
        new_callable=AsyncMock,
        return_value={"result": "ok"},
    ):
        await handle_game_command(mock_websocket, TEST_PLAYER_ID_STR, "look", None, mock_ws_connection_manager)
        mock_websocket.send_json.assert_awaited_once()


@pytest.mark.asyncio
async def test_handle_game_command_empty_command(mock_websocket, mock_ws_connection_manager):
    """Test handle_game_command handles empty command."""
    await handle_game_command(mock_websocket, TEST_PLAYER_ID_STR, "", None, mock_ws_connection_manager)
    mock_websocket.send_json.assert_awaited_once()


@pytest.mark.asyncio
async def test_handle_game_command_whitespace_only(mock_websocket, mock_ws_connection_manager):
    """Test handle_game_command handles whitespace-only command."""
    await handle_game_command(mock_websocket, TEST_PLAYER_ID_STR, "   ", None, mock_ws_connection_manager)
    mock_websocket.send_json.assert_awaited_once()


@pytest.mark.asyncio
async def test_handle_game_command_single_word_no_args(mock_websocket, mock_ws_connection_manager):
    """Test handle_game_command handles single word command with no args."""
    with patch(
        "server.realtime.websocket_handler.process_websocket_command",
        new_callable=AsyncMock,
        return_value={"result": "ok"},
    ):
        await handle_game_command(mock_websocket, TEST_PLAYER_ID_STR, "look", None, mock_ws_connection_manager)
        mock_websocket.send_json.assert_awaited_once()


@pytest.mark.asyncio
async def test_handle_game_command_with_provided_args(mock_websocket, mock_ws_connection_manager):
    """Test handle_game_command processes command with provided args."""
    with patch(
        "server.realtime.websocket_handler.process_websocket_command",
        new_callable=AsyncMock,
        return_value={"result": "ok"},
    ):
        await handle_game_command(mock_websocket, TEST_PLAYER_ID_STR, "go", ["north"], mock_ws_connection_manager)
        mock_websocket.send_json.assert_awaited_once()


@pytest.mark.asyncio
async def test_handle_websocket_message(mock_websocket):
    """Test handle_websocket_message routes message."""
    message = {"type": "command", "command": "look"}
    with patch("server.realtime.message_handler_factory.message_handler_factory") as mock_factory:
        mock_factory.handle_message = AsyncMock()
        await handle_websocket_message(mock_websocket, TEST_PLAYER_ID_STR, message)
        mock_factory.handle_message.assert_awaited_once()


@pytest.mark.asyncio
async def test_handle_websocket_message_chat(mock_websocket):
    """Test handle_websocket_message routes chat message."""
    message = {"type": "chat", "message": "Hello"}
    with patch("server.realtime.websocket_handler.handle_chat_message", new_callable=AsyncMock) as mock_chat:
        await handle_websocket_message(mock_websocket, TEST_PLAYER_ID_STR, message)
        mock_chat.assert_awaited_once()


@pytest.mark.asyncio
async def test_handle_websocket_message_command(mock_websocket):
    """Test handle_websocket_message routes command message."""
    message = {"type": "command", "command": "look"}
    with patch("server.realtime.websocket_handler.handle_game_command", new_callable=AsyncMock) as mock_cmd:
        await handle_websocket_message(mock_websocket, TEST_PLAYER_ID_STR, message)
        mock_cmd.assert_awaited_once()


@pytest.mark.asyncio
async def test_process_websocket_command(mock_ws_connection_manager):
    """Test process_websocket_command processes command."""
    mock_player = MagicMock()
    mock_player.current_room_id = "room_001"
    mock_player.name = "TestPlayer"
    mock_ws_connection_manager.get_player = AsyncMock(return_value=mock_player)
    with patch(
        "server.command_handler_unified.process_command_unified", new_callable=AsyncMock, return_value={"result": "ok"}
    ):
        result = await process_websocket_command("look", [], TEST_PLAYER_ID_STR, mock_ws_connection_manager)
        assert isinstance(result, dict)


@pytest.mark.asyncio
async def test_process_websocket_command_no_player(mock_ws_connection_manager):
    """Test process_websocket_command handles player not found."""
    mock_ws_connection_manager.get_player = AsyncMock(return_value=None)
    result = await process_websocket_command("look", [], TEST_PLAYER_ID_STR, mock_ws_connection_manager)
    assert isinstance(result, dict)
    assert "result" in result


@pytest.mark.asyncio
async def test_process_websocket_command_no_app_state(mock_ws_connection_manager):
    """Test process_websocket_command handles no app state."""
    mock_player = MagicMock()
    mock_player.current_room_id = "room_001"
    mock_player.name = "TestPlayer"
    mock_ws_connection_manager.get_player = AsyncMock(return_value=mock_player)
    mock_ws_connection_manager.app = None
    result = await process_websocket_command("look", [], TEST_PLAYER_ID_STR, mock_ws_connection_manager)
    assert isinstance(result, dict)
    assert "result" in result
    assert "Server configuration error" in result["result"]


@pytest.mark.asyncio
async def test_process_websocket_command_no_app_in_connection_manager(mock_ws_connection_manager):
    """Test process_websocket_command handles connection_manager without app attribute."""
    mock_player = MagicMock()
    mock_player.current_room_id = "room_001"
    mock_player.name = "TestPlayer"
    mock_ws_connection_manager.get_player = AsyncMock(return_value=mock_player)
    del mock_ws_connection_manager.app
    result = await process_websocket_command("look", [], TEST_PLAYER_ID_STR, mock_ws_connection_manager)
    assert isinstance(result, dict)
    assert "result" in result
    assert "Server configuration error" in result["result"]


@pytest.mark.asyncio
async def test_process_websocket_command_type_error(mock_ws_connection_manager):
    """Test process_websocket_command handles TypeError when command handler returns non-dict."""
    mock_player = MagicMock()
    mock_player.current_room_id = "room_001"
    mock_player.name = "TestPlayer"
    mock_ws_connection_manager.get_player = AsyncMock(return_value=mock_player)
    mock_app_state = MagicMock()
    mock_ws_connection_manager.app = MagicMock()
    mock_ws_connection_manager.app.state = mock_app_state
    with patch(
        "server.command_handler_unified.process_command_unified", new_callable=AsyncMock, return_value="not a dict"
    ):
        with pytest.raises(TypeError, match="Command handler must return a dict"):
            await process_websocket_command("look", [], TEST_PLAYER_ID_STR, mock_ws_connection_manager)


@pytest.mark.asyncio
async def test_process_websocket_command_no_aliases_dir(mock_ws_connection_manager):
    """Test process_websocket_command handles None aliases_dir."""
    mock_player = MagicMock()
    mock_player.current_room_id = "room_001"
    mock_player.name = "TestPlayer"
    mock_ws_connection_manager.get_player = AsyncMock(return_value=mock_player)
    mock_app_state = MagicMock()
    mock_ws_connection_manager.app = MagicMock()
    mock_ws_connection_manager.app.state = mock_app_state
    with patch("server.config.get_config") as mock_get_config:
        mock_config = MagicMock()
        mock_config.game.aliases_dir = None
        mock_get_config.return_value = mock_config
        with patch(
            "server.command_handler_unified.process_command_unified",
            new_callable=AsyncMock,
            return_value={"result": "ok"},
        ):
            result = await process_websocket_command("look", [], TEST_PLAYER_ID_STR, mock_ws_connection_manager)
            assert isinstance(result, dict)


@pytest.mark.asyncio
async def test_cleanup_connection(mock_ws_connection_manager):
    """Test _cleanup_connection cleans up connection."""
    player_id = uuid.uuid4()
    mock_ws_connection_manager.disconnect_websocket = AsyncMock()
    await _cleanup_connection(player_id, str(player_id), mock_ws_connection_manager)
    mock_ws_connection_manager.disconnect_websocket.assert_awaited_once()


def test_resolve_and_setup_app_state_services():
    """Test _resolve_and_setup_app_state_services resolves services."""
    mock_app_state = MagicMock()
    mock_container = MagicMock()
    mock_player_service = MagicMock()
    mock_user_manager = MagicMock()
    mock_container.player_service = mock_player_service
    mock_container.user_manager = mock_user_manager
    mock_app_state.container = mock_container
    mock_request_context = MagicMock()
    mock_request_context.set_app_state_services = MagicMock()
    player_service, user_manager = _resolve_and_setup_app_state_services(mock_app_state, mock_request_context)
    assert player_service == mock_player_service
    assert user_manager == mock_user_manager


def test_resolve_and_setup_app_state_services_no_container():
    """Test _resolve_and_setup_app_state_services handles no container."""
    mock_app_state = MagicMock()
    mock_app_state.container = None
    mock_app_state.player_service = MagicMock()
    mock_app_state.user_manager = MagicMock()
    mock_request_context = MagicMock()
    mock_request_context.set_app_state_services = MagicMock()
    player_service, user_manager = _resolve_and_setup_app_state_services(mock_app_state, mock_request_context)
    assert player_service is not None
    assert user_manager is not None
