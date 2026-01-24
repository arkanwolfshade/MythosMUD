"""
Unit tests to fill coverage gaps in websocket_handler.py.

These tests target specific uncovered lines to bring coverage from 84.64% to 90%+.
"""

import uuid
from unittest.mock import AsyncMock, MagicMock, patch

import pytest
from fastapi import WebSocketDisconnect

from server.realtime.websocket_handler import (
    _handle_websocket_message_loop,
    _process_exception_in_message_loop,
    handle_chat_message,
    handle_game_command,
    handle_websocket_connection,
    process_websocket_command,
)

# Test UUID constant for player IDs
TEST_PLAYER_ID = uuid.UUID("12345678-1234-5678-1234-567812345678")
TEST_PLAYER_ID_STR = str(TEST_PLAYER_ID)


@pytest.mark.asyncio
async def test_message_loop_should_raise_exception(mock_websocket, mock_ws_connection_manager):
    """Test _handle_websocket_message_loop re-raises exception when should_raise is True (lines 296-297)."""
    player_id = uuid.uuid4()
    player_id_str = str(player_id)

    # Mock receive_text to raise RuntimeError that should be re-raised
    error = RuntimeError("Some other runtime error")
    mock_websocket.receive_text = AsyncMock(side_effect=error)

    with patch("server.realtime.websocket_handler._process_exception_in_message_loop") as mock_process_exception:
        # Return should_break=False, should_raise=True to trigger re-raise
        mock_process_exception.return_value = (False, True)

        with pytest.raises(RuntimeError, match="Some other runtime error"):
            await _handle_websocket_message_loop(mock_websocket, player_id, player_id_str, mock_ws_connection_manager)


@pytest.mark.asyncio
async def test_handle_websocket_connection_full_flow(mock_websocket, mock_ws_connection_manager):
    """Test handle_websocket_connection full flow including message loop and cleanup (lines 371-374)."""
    player_id = uuid.uuid4()

    mock_ws_connection_manager.connect_websocket = AsyncMock(return_value=True)
    mock_ws_connection_manager.get_connection_id_from_websocket = MagicMock(return_value="conn_001")

    with patch(
        "server.realtime.websocket_helpers.check_shutdown_and_reject", new_callable=AsyncMock, return_value=False
    ):
        with patch("server.commands.admin_shutdown_command.is_shutdown_pending", return_value=False):
            with patch("server.realtime.websocket_helpers.load_player_mute_data", new_callable=AsyncMock):
                with patch(
                    "server.realtime.websocket_initial_state.send_initial_game_state",
                    new_callable=AsyncMock,
                    return_value=(None, False),
                ):
                    # Patch message loop and cleanup to verify try/finally block (lines 371-374) executes
                    # The mock_websocket fixture already provides send_json = AsyncMock(), so welcome event will succeed
                    with patch(
                        "server.realtime.websocket_handler._handle_websocket_message_loop", new_callable=AsyncMock
                    ):
                        with patch(
                            "server.realtime.websocket_handler._cleanup_connection", new_callable=AsyncMock
                        ) as mock_cleanup:
                            # Execute the connection handler - this should reach try/finally block
                            # The welcome event send (line 369) will succeed because mock_websocket.send_json is AsyncMock
                            await handle_websocket_connection(
                                mock_websocket, player_id, None, mock_ws_connection_manager
                            )

                            # Verify cleanup was called in finally block (line 374)
                            # If cleanup is called, the try block (line 371-372) must have executed
                            mock_cleanup.assert_awaited_once_with(player_id, str(player_id), mock_ws_connection_manager)


@pytest.mark.asyncio
async def test_handle_game_command_resolve_connection_manager_from_app(mock_websocket):
    """Test handle_game_command resolves connection_manager from app when None (lines 423-425)."""
    mock_connection_manager = MagicMock()
    mock_app = MagicMock()
    mock_app.state.container.connection_manager = mock_connection_manager

    with patch("server.main.app", mock_app):
        with patch(
            "server.realtime.websocket_handler.process_websocket_command",
            new_callable=AsyncMock,
            return_value={"result": "ok"},
        ):
            await handle_game_command(mock_websocket, TEST_PLAYER_ID_STR, "look", None, None)
            mock_websocket.send_json.assert_awaited_once()


@pytest.mark.asyncio
async def test_handle_game_command_exception_handling(mock_websocket, mock_ws_connection_manager):
    """Test handle_game_command exception handling path (lines 472-480)."""
    error = WebSocketDisconnect(1000)
    with patch(
        "server.realtime.websocket_handler.process_websocket_command",
        new_callable=AsyncMock,
        side_effect=error,
    ):
        await handle_game_command(mock_websocket, TEST_PLAYER_ID_STR, "look", None, mock_ws_connection_manager)
        # Should send error response
        mock_websocket.send_json.assert_awaited_once()


@pytest.mark.asyncio
async def test_handle_game_command_runtime_error_handling(mock_websocket, mock_ws_connection_manager):
    """Test handle_game_command RuntimeError handling path (lines 472-480)."""
    error = RuntimeError("Connection lost")
    with patch(
        "server.realtime.websocket_handler.process_websocket_command",
        new_callable=AsyncMock,
        side_effect=error,
    ):
        await handle_game_command(mock_websocket, TEST_PLAYER_ID_STR, "look", None, mock_ws_connection_manager)
        # Should send error response
        mock_websocket.send_json.assert_awaited_once()


@pytest.mark.asyncio
async def test_process_websocket_command_resolve_connection_manager_from_app(tmp_path):
    """Test process_websocket_command resolves connection_manager from app when None (lines 549-551)."""
    mock_player = MagicMock()
    mock_player.current_room_id = "room_001"
    mock_player.name = "TestPlayer"

    mock_connection_manager = MagicMock()
    mock_connection_manager.get_player = AsyncMock(return_value=mock_player)
    mock_connection_manager.async_persistence = MagicMock()
    mock_connection_manager.app = MagicMock()
    mock_connection_manager.app.state = MagicMock()

    mock_app = MagicMock()
    mock_app.state.container.connection_manager = mock_connection_manager

    aliases_dir = str(tmp_path / "aliases")
    with patch("server.main.app", mock_app):
        with patch("server.config.get_config") as mock_get_config:
            mock_config = MagicMock()
            mock_config.game.aliases_dir = aliases_dir
            mock_get_config.return_value = mock_config
            with patch(
                "server.command_handler_unified.process_command_unified",
                new_callable=AsyncMock,
                return_value={"result": "ok"},
            ):
                with patch("server.realtime.websocket_handler._resolve_and_setup_app_state_services"):
                    result = await process_websocket_command("look", [], TEST_PLAYER_ID_STR, None)
                    assert isinstance(result, dict)
                    assert "result" in result


@pytest.mark.asyncio
async def test_handle_chat_message_resolve_connection_manager_from_app(mock_websocket):
    """Test handle_chat_message resolves connection_manager from app when None (lines 644-646)."""
    mock_connection_manager = MagicMock()
    mock_player = MagicMock()
    mock_player.current_room_id = "room_001"
    mock_connection_manager.get_player = AsyncMock(return_value=mock_player)
    mock_connection_manager.broadcast_to_room = AsyncMock()

    mock_app = MagicMock()
    mock_app.state.container.connection_manager = mock_connection_manager

    with patch("server.main.app", mock_app):
        await handle_chat_message(mock_websocket, TEST_PLAYER_ID_STR, "Hello", None)
        # Should send confirmation
        mock_websocket.send_json.assert_awaited_once()


@pytest.mark.asyncio
async def test_handle_chat_message_exception_handling(mock_websocket, mock_ws_connection_manager):
    """Test handle_chat_message exception handling path (lines 666-674)."""
    error = WebSocketDisconnect(1000)
    mock_ws_connection_manager.get_player = AsyncMock(side_effect=error)

    await handle_chat_message(mock_websocket, TEST_PLAYER_ID_STR, "Hello", mock_ws_connection_manager)
    # Should send error response
    mock_websocket.send_json.assert_awaited_once()


@pytest.mark.asyncio
async def test_handle_chat_message_runtime_error_handling(mock_websocket, mock_ws_connection_manager):
    """Test handle_chat_message RuntimeError handling path (lines 666-674)."""
    error = RuntimeError("Connection lost")
    mock_ws_connection_manager.get_player = AsyncMock(side_effect=error)

    await handle_chat_message(mock_websocket, TEST_PLAYER_ID_STR, "Hello", mock_ws_connection_manager)
    # Should send error response
    mock_websocket.send_json.assert_awaited_once()


@pytest.mark.asyncio
async def test_process_exception_in_message_loop(mock_websocket):
    """Test _process_exception_in_message_loop delegates to _handle_message_loop_exception."""
    player_id = uuid.uuid4()
    player_id_str = str(player_id)
    connection_id = "conn_001"
    error = ValueError("Test error")

    with patch("server.realtime.websocket_handler._handle_message_loop_exception") as mock_handle:
        mock_handle.return_value = (False, False)
        should_break, should_raise = await _process_exception_in_message_loop(
            mock_websocket, error, player_id, player_id_str, connection_id
        )
        assert should_break is False
        assert should_raise is False
        mock_handle.assert_awaited_once_with(mock_websocket, error, player_id, player_id_str, connection_id)
