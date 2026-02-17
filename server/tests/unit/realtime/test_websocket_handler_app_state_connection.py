"""
Unit tests for WebSocket handler app state resolution and connection handling.

Tests _resolve_and_setup_app_state_services, _cleanup_connection mute cleanup,
_handle_websocket_message_loop, and handle_websocket_connection.
"""

import asyncio
import uuid
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from server.realtime.websocket_handler import (
    _cleanup_connection,
    _handle_websocket_message_loop,
    _resolve_and_setup_app_state_services,
    handle_websocket_connection,
)

# pylint: disable=protected-access  # Reason: Test file - accessing protected members is standard practice


def test_resolve_and_setup_app_state_services_services_already_set():
    """Test _resolve_and_setup_app_state_services when services already set."""
    mock_app_state = MagicMock()
    mock_container = MagicMock()
    mock_player_service = MagicMock()
    mock_user_manager = MagicMock()
    mock_container.player_service = mock_player_service
    mock_container.user_manager = mock_user_manager
    mock_app_state.container = mock_container
    mock_app_state.player_service = mock_player_service
    mock_app_state.user_manager = mock_user_manager
    mock_request_context = MagicMock()
    mock_request_context.set_app_state_services = MagicMock()
    player_service, user_manager = _resolve_and_setup_app_state_services(mock_app_state, mock_request_context)
    assert player_service == mock_player_service
    assert user_manager == mock_user_manager


def test_resolve_and_setup_app_state_services_missing_services():
    """Test _resolve_and_setup_app_state_services when services are missing."""
    mock_app_state = MagicMock()
    mock_app_state.container = None
    mock_app_state.player_service = None
    mock_app_state.user_manager = None
    mock_request_context = MagicMock()
    mock_request_context.set_app_state_services = MagicMock()
    player_service, user_manager = _resolve_and_setup_app_state_services(mock_app_state, mock_request_context)
    assert player_service is None
    assert user_manager is None


def test_resolve_and_setup_app_state_services_no_app_state():
    """Test _resolve_and_setup_app_state_services when app_state is None."""
    mock_request_context = MagicMock()
    mock_request_context.set_app_state_services = MagicMock()
    player_service, user_manager = _resolve_and_setup_app_state_services(None, mock_request_context)
    assert player_service is None
    assert user_manager is None


def test_resolve_and_setup_app_state_services_container_no_services():
    """Test _resolve_and_setup_app_state_services when container has no services."""
    mock_app_state = MagicMock()
    mock_container = MagicMock()
    mock_container.player_service = None
    mock_container.user_manager = None
    mock_app_state.container = mock_container
    mock_request_context = MagicMock()
    mock_request_context.set_app_state_services = MagicMock()
    player_service, user_manager = _resolve_and_setup_app_state_services(mock_app_state, mock_request_context)
    assert player_service is None
    assert user_manager is None


def test_resolve_and_setup_app_state_services_no_container_attribute():
    """Test _resolve_and_setup_app_state_services when app_state has no container attribute."""
    mock_app_state = MagicMock()
    del mock_app_state.container
    mock_app_state.player_service = MagicMock()
    mock_app_state.user_manager = MagicMock()
    mock_request_context = MagicMock()
    mock_request_context.set_app_state_services = MagicMock()
    player_service, user_manager = _resolve_and_setup_app_state_services(mock_app_state, mock_request_context)
    assert player_service is not None
    assert user_manager is not None


def test_resolve_and_setup_app_state_services_only_player_service():
    """Test _resolve_and_setup_app_state_services when only player_service is available."""
    mock_app_state = MagicMock()
    mock_app_state.container = None
    mock_app_state.player_service = MagicMock()
    mock_app_state.user_manager = None
    mock_request_context = MagicMock()
    mock_request_context.set_app_state_services = MagicMock()
    player_service, user_manager = _resolve_and_setup_app_state_services(mock_app_state, mock_request_context)
    assert player_service is not None
    assert user_manager is None
    mock_request_context.set_app_state_services.assert_not_called()


def test_resolve_and_setup_app_state_services_only_user_manager():
    """Test _resolve_and_setup_app_state_services when only user_manager is available."""
    mock_app_state = MagicMock()
    mock_app_state.container = None
    mock_app_state.player_service = None
    mock_app_state.user_manager = MagicMock()
    mock_request_context = MagicMock()
    mock_request_context.set_app_state_services = MagicMock()
    player_service, user_manager = _resolve_and_setup_app_state_services(mock_app_state, mock_request_context)
    assert player_service is None
    assert user_manager is not None
    mock_request_context.set_app_state_services.assert_not_called()


def test_resolve_and_setup_app_state_services_player_service_already_set():
    """Test _resolve_and_setup_app_state_services when player_service already set on app_state."""
    mock_app_state = MagicMock()
    mock_container = MagicMock()
    mock_player_service = MagicMock()
    mock_user_manager = MagicMock()
    mock_container.player_service = mock_player_service
    mock_container.user_manager = mock_user_manager
    mock_app_state.container = mock_container
    mock_app_state.player_service = mock_player_service
    # Ensure user_manager is not set so function will set it
    del mock_app_state.user_manager
    mock_request_context = MagicMock()
    mock_request_context.set_app_state_services = MagicMock()
    player_service, user_manager = _resolve_and_setup_app_state_services(mock_app_state, mock_request_context)
    assert player_service == mock_player_service
    assert user_manager == mock_user_manager
    assert mock_app_state.user_manager == mock_user_manager


def test_resolve_and_setup_app_state_services_user_manager_already_set():
    """Test _resolve_and_setup_app_state_services when user_manager already set on app_state."""
    mock_app_state = MagicMock()
    mock_container = MagicMock()
    mock_player_service = MagicMock()
    mock_user_manager = MagicMock()
    mock_container.player_service = mock_player_service
    mock_container.user_manager = mock_user_manager
    mock_app_state.container = mock_container
    mock_app_state.user_manager = mock_user_manager
    # Ensure player_service is not set so function will set it
    del mock_app_state.player_service
    mock_request_context = MagicMock()
    mock_request_context.set_app_state_services = MagicMock()
    player_service, user_manager = _resolve_and_setup_app_state_services(mock_app_state, mock_request_context)
    assert player_service == mock_player_service
    assert user_manager == mock_user_manager
    assert mock_app_state.player_service == mock_player_service


def test_resolve_and_setup_app_state_services_player_service_no_hasattr():
    """Test _resolve_and_setup_app_state_services when app_state has no player_service attribute."""
    mock_app_state = MagicMock()
    mock_container = MagicMock()
    mock_player_service = MagicMock()
    mock_user_manager = MagicMock()
    mock_container.player_service = mock_player_service
    mock_container.user_manager = mock_user_manager
    mock_app_state.container = mock_container
    del mock_app_state.player_service
    mock_request_context = MagicMock()
    mock_request_context.set_app_state_services = MagicMock()
    player_service, user_manager = _resolve_and_setup_app_state_services(mock_app_state, mock_request_context)
    assert player_service == mock_player_service
    assert user_manager == mock_user_manager
    assert mock_app_state.player_service == mock_player_service


def test_resolve_and_setup_app_state_services_user_manager_no_hasattr():
    """Test _resolve_and_setup_app_state_services when app_state has no user_manager attribute."""
    mock_app_state = MagicMock()
    mock_container = MagicMock()
    mock_player_service = MagicMock()
    mock_user_manager = MagicMock()
    mock_container.player_service = mock_player_service
    mock_container.user_manager = mock_user_manager
    mock_app_state.container = mock_container
    del mock_app_state.user_manager
    mock_request_context = MagicMock()
    mock_request_context.set_app_state_services = MagicMock()
    player_service, user_manager = _resolve_and_setup_app_state_services(mock_app_state, mock_request_context)
    assert player_service == mock_player_service
    assert user_manager == mock_user_manager
    assert mock_app_state.user_manager == mock_user_manager


@pytest.mark.asyncio
async def test_cleanup_connection_mute_cleanup_error(mock_ws_connection_manager):
    """Test _cleanup_connection handles error during mute cleanup."""
    player_id = uuid.uuid4()
    mock_ws_connection_manager.disconnect_websocket = AsyncMock()
    with patch("server.services.user_manager.user_manager") as mock_user_manager:
        mock_user_manager.cleanup_player_mutes = MagicMock(side_effect=RuntimeError("Cleanup error"))
        await _cleanup_connection(player_id, str(player_id), mock_ws_connection_manager)


@pytest.mark.asyncio
async def test_handle_websocket_message_loop(mock_websocket, mock_ws_connection_manager):
    """Test _handle_websocket_message_loop processes messages."""
    from fastapi import WebSocketDisconnect

    player_id = uuid.uuid4()
    call_count = 0

    async def mock_receive():
        nonlocal call_count
        call_count += 1
        if call_count == 1:
            return '{"type": "test"}'
        raise WebSocketDisconnect(1000)

    mock_websocket.receive_text = mock_receive
    mock_validator = MagicMock()
    mock_message = {"type": "test"}
    mock_validator.parse_and_validate = AsyncMock(return_value=mock_message)
    with patch("server.realtime.message_validator.get_message_validator", return_value=mock_validator):
        with patch("server.realtime.websocket_handler._process_message", new_callable=AsyncMock, return_value=True):
            try:
                await asyncio.wait_for(
                    _handle_websocket_message_loop(
                        mock_websocket, player_id, str(player_id), mock_ws_connection_manager
                    ),
                    timeout=2.0,
                )
            except TimeoutError:
                pytest.fail("Message loop did not terminate within timeout")


@pytest.mark.asyncio
async def test_handle_websocket_connection_shutdown_rejected(mock_websocket, mock_ws_connection_manager):
    """Test handle_websocket_connection handles shutdown rejection."""
    player_id = uuid.uuid4()
    with patch(
        "server.realtime.websocket_helpers.check_shutdown_and_reject", new_callable=AsyncMock, return_value=True
    ):
        await handle_websocket_connection(mock_websocket, player_id, None, mock_ws_connection_manager)
        mock_ws_connection_manager.connect_websocket.assert_not_called()


@pytest.mark.asyncio
async def test_handle_websocket_connection_connect_failure(mock_websocket, mock_ws_connection_manager):
    """Test handle_websocket_connection handles connection failure."""
    player_id = uuid.uuid4()
    mock_ws_connection_manager.connect_websocket = AsyncMock(return_value=False)
    with patch(
        "server.realtime.websocket_helpers.check_shutdown_and_reject", new_callable=AsyncMock, return_value=False
    ):
        await handle_websocket_connection(mock_websocket, player_id, None, mock_ws_connection_manager)


@pytest.mark.asyncio
async def test_handle_websocket_connection_initial_state_exit(mock_websocket, mock_ws_connection_manager):
    """Test handle_websocket_connection handles should_exit from initial state."""
    player_id = uuid.uuid4()
    mock_ws_connection_manager.connect_websocket = AsyncMock(return_value=True)
    with patch(
        "server.realtime.websocket_helpers.check_shutdown_and_reject", new_callable=AsyncMock, return_value=False
    ):
        with patch(
            "server.realtime.websocket_initial_state.send_initial_game_state",
            new_callable=AsyncMock,
            return_value=(None, True),
        ):
            with patch("server.realtime.websocket_helpers.load_player_mute_data", new_callable=AsyncMock):
                await handle_websocket_connection(mock_websocket, player_id, None, mock_ws_connection_manager)


@pytest.mark.asyncio
async def test_handle_websocket_connection_with_room_and_death(mock_websocket, mock_ws_connection_manager):
    """Test handle_websocket_connection handles room and death notification."""
    player_id = uuid.uuid4()
    mock_ws_connection_manager.connect_websocket = AsyncMock(return_value=True)
    mock_room = MagicMock()
    mock_async_persistence = MagicMock()
    mock_async_persistence.get_room_by_id = MagicMock(return_value=mock_room)
    mock_ws_connection_manager.async_persistence = mock_async_persistence
    with patch(
        "server.realtime.websocket_helpers.check_shutdown_and_reject", new_callable=AsyncMock, return_value=False
    ):
        with patch(
            "server.realtime.websocket_initial_state.send_initial_game_state",
            new_callable=AsyncMock,
            return_value=("room_001", False),
        ):
            with patch("server.realtime.websocket_helpers.load_player_mute_data", new_callable=AsyncMock):
                with patch(
                    "server.realtime.websocket_initial_state.check_and_send_death_notification",
                    new_callable=AsyncMock,
                ):
                    with patch(
                        "server.realtime.websocket_initial_state.send_initial_room_state",
                        new_callable=AsyncMock,
                    ):
                        with patch(
                            "server.realtime.websocket_handler._handle_websocket_message_loop",
                            new_callable=AsyncMock,
                        ):
                            with patch("server.realtime.websocket_handler._cleanup_connection", new_callable=AsyncMock):
                                await handle_websocket_connection(
                                    mock_websocket, player_id, None, mock_ws_connection_manager
                                )


@pytest.mark.asyncio
async def test_handle_websocket_connection_initial_setup_error(mock_websocket, mock_ws_connection_manager):
    """Test handle_websocket_connection handles error in initial setup."""
    from fastapi import WebSocketDisconnect

    player_id = uuid.uuid4()
    mock_ws_connection_manager.connect_websocket = AsyncMock(return_value=True)
    with patch(
        "server.realtime.websocket_helpers.check_shutdown_and_reject", new_callable=AsyncMock, return_value=False
    ):
        with patch(
            "server.realtime.websocket_initial_state.send_initial_game_state",
            new_callable=AsyncMock,
            side_effect=WebSocketDisconnect(1000),
        ):
            with patch("server.realtime.websocket_helpers.load_player_mute_data", new_callable=AsyncMock):
                with patch("server.realtime.websocket_handler._handle_websocket_message_loop", new_callable=AsyncMock):
                    with patch("server.realtime.websocket_handler._cleanup_connection", new_callable=AsyncMock):
                        await handle_websocket_connection(mock_websocket, player_id, None, mock_ws_connection_manager)
