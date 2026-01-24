"""
Unit tests for connection delegates.

Tests the connection_delegates module functions.
"""

import uuid
from typing import Any
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from server.realtime.connection_delegates import (
    cleanup_dead_websocket_impl,
    delegate_connection_cleaner,
    delegate_connection_cleaner_sync,
    delegate_error_handler,
    delegate_game_state_provider,
    delegate_game_state_provider_sync,
    delegate_health_monitor,
    delegate_health_monitor_sync,
    delegate_message_broadcaster,
    delegate_personal_message_sender,
    delegate_personal_message_sender_sync,
    delegate_room_event_handler,
    validate_token_impl,
)


@pytest.mark.asyncio
async def test_delegate_error_handler_success():
    """Test delegate_error_handler() successfully delegates to handler."""
    mock_handler = MagicMock()
    mock_method = AsyncMock(return_value={"error": "handled"})
    mock_handler.handle_error = mock_method
    default_error = {"error": "default"}

    result = await delegate_error_handler(mock_handler, "handle_error", default_error, "arg1", key="value")

    assert result == {"error": "handled"}
    mock_method.assert_called_once_with("arg1", key="value")


@pytest.mark.asyncio
async def test_delegate_error_handler_none():
    """Test delegate_error_handler() returns default when handler is None."""
    default_error = {"error": "default"}

    result = await delegate_error_handler(None, "handle_error", default_error)

    assert result == default_error


@pytest.mark.asyncio
async def test_cleanup_dead_websocket_impl_success():
    """Test cleanup_dead_websocket_impl() successfully cleans up websocket."""
    player_id = uuid.uuid4()
    connection_id = "conn_123"
    mock_manager = MagicMock()
    mock_websocket = AsyncMock()
    # Mock client_state to indicate the websocket is connected (so close() is called)
    mock_client_state = MagicMock()
    mock_client_state.name = "CONNECTED"
    mock_websocket.client_state = mock_client_state
    mock_manager.active_websockets = {connection_id: mock_websocket}
    # Use a real dict so we can test deletion - key must match player_id type
    player_websockets_dict = {player_id: [connection_id]}
    mock_manager.player_websockets = player_websockets_dict
    connection_metadata_dict = {connection_id: {"key": "value"}}
    mock_manager.connection_metadata = connection_metadata_dict
    mock_manager.rate_limiter = MagicMock()
    mock_manager.rate_limiter.remove_connection_message_data = MagicMock()

    await cleanup_dead_websocket_impl(player_id, connection_id, mock_manager)

    mock_websocket.close.assert_called_once()
    assert connection_id not in mock_manager.active_websockets
    # After removing connection_id, the list becomes empty, so player_id key is deleted
    assert player_id not in player_websockets_dict
    assert connection_id not in connection_metadata_dict
    mock_manager.rate_limiter.remove_connection_message_data.assert_called_once_with(connection_id)


@pytest.mark.asyncio
async def test_cleanup_dead_websocket_impl_none_websocket():
    """Test cleanup_dead_websocket_impl() handles None websocket."""
    player_id = uuid.uuid4()
    connection_id = "conn_123"
    mock_manager = MagicMock()
    mock_manager.active_websockets = {connection_id: None}
    mock_manager.player_websockets = {}
    mock_manager.connection_metadata = {}
    mock_manager.rate_limiter = MagicMock()
    mock_manager.rate_limiter.remove_connection_message_data = MagicMock()

    await cleanup_dead_websocket_impl(player_id, connection_id, mock_manager)

    assert connection_id not in mock_manager.active_websockets


@pytest.mark.asyncio
async def test_cleanup_dead_websocket_impl_not_in_active():
    """Test cleanup_dead_websocket_impl() handles websocket not in active_websockets."""
    player_id = uuid.uuid4()
    connection_id = "conn_123"
    mock_manager = MagicMock()
    mock_manager.active_websockets = {}
    # Use a real dict so we can test deletion - key must match player_id type
    player_websockets_dict = {player_id: [connection_id]}
    mock_manager.player_websockets = player_websockets_dict
    mock_manager.connection_metadata = {}
    mock_manager.rate_limiter = MagicMock()
    mock_manager.rate_limiter.remove_connection_message_data = MagicMock()

    await cleanup_dead_websocket_impl(player_id, connection_id, mock_manager)

    # After removing connection_id, the list becomes empty, so player_id key is deleted
    assert player_id not in player_websockets_dict


@pytest.mark.asyncio
async def test_cleanup_dead_websocket_impl_close_timeout():
    """Test cleanup_dead_websocket_impl() handles close timeout."""
    player_id = uuid.uuid4()
    connection_id = "conn_123"
    mock_manager = MagicMock()
    mock_websocket = AsyncMock()
    mock_websocket.close = AsyncMock(side_effect=TimeoutError())
    mock_manager.active_websockets = {connection_id: mock_websocket}
    mock_manager.player_websockets = {}
    mock_manager.connection_metadata = {}
    mock_manager.rate_limiter = MagicMock()
    mock_manager.rate_limiter.remove_connection_message_data = MagicMock()

    await cleanup_dead_websocket_impl(player_id, connection_id, mock_manager)

    assert connection_id not in mock_manager.active_websockets


@pytest.mark.asyncio
async def test_cleanup_dead_websocket_impl_error():
    """Test cleanup_dead_websocket_impl() handles errors."""
    player_id = uuid.uuid4()
    connection_id = "conn_123"
    mock_manager = MagicMock()
    mock_manager.active_websockets = {}
    del mock_manager.player_websockets  # Cause AttributeError

    await cleanup_dead_websocket_impl(player_id, connection_id, mock_manager)

    # Should not raise, just log error


@pytest.mark.asyncio
async def test_validate_token_impl_success():
    """Test validate_token_impl() successfully validates token."""
    token = "valid_token"
    player_id = uuid.uuid4()
    mock_manager = MagicMock()
    mock_player = MagicMock()
    mock_player.player_id = player_id
    mock_manager.async_persistence = AsyncMock()
    mock_manager.async_persistence.get_player_by_user_id = AsyncMock(return_value=mock_player)

    with patch("server.auth_utils.decode_access_token") as mock_decode:
        mock_decode.return_value = {"sub": str(player_id)}

        result = await validate_token_impl(token, player_id, mock_manager)

        assert result is True


@pytest.mark.asyncio
async def test_validate_token_impl_invalid_payload():
    """Test validate_token_impl() returns False for invalid payload."""
    token = "invalid_token"
    player_id = uuid.uuid4()
    mock_manager = MagicMock()

    with patch("server.auth_utils.decode_access_token", return_value=None):
        result = await validate_token_impl(token, player_id, mock_manager)

        assert result is False


@pytest.mark.asyncio
async def test_validate_token_impl_no_persistence():
    """Test validate_token_impl() returns False when persistence not available."""
    token = "valid_token"
    player_id = uuid.uuid4()
    mock_manager = MagicMock()
    mock_manager.async_persistence = None

    with patch("server.auth_utils.decode_access_token") as mock_decode:
        mock_decode.return_value = {"sub": str(player_id)}

        result = await validate_token_impl(token, player_id, mock_manager)

        assert result is False


@pytest.mark.asyncio
async def test_validate_token_impl_player_mismatch():
    """Test validate_token_impl() returns False for player mismatch."""
    token = "valid_token"
    player_id = uuid.uuid4()
    other_player_id = uuid.uuid4()
    mock_manager = MagicMock()
    mock_player = MagicMock()
    mock_player.player_id = other_player_id
    mock_manager.async_persistence = AsyncMock()
    mock_manager.async_persistence.get_player_by_user_id = AsyncMock(return_value=mock_player)

    with patch("server.auth_utils.decode_access_token") as mock_decode:
        mock_decode.return_value = {"sub": str(player_id)}

        result = await validate_token_impl(token, player_id, mock_manager)

        assert result is False


@pytest.mark.asyncio
async def test_validate_token_impl_database_error():
    """Test validate_token_impl() handles DatabaseError."""
    from server.exceptions import DatabaseError

    token = "valid_token"
    player_id = uuid.uuid4()
    mock_manager = MagicMock()
    mock_manager.async_persistence = AsyncMock()
    mock_manager.async_persistence.get_player_by_user_id = AsyncMock(side_effect=DatabaseError("Database error"))

    with patch("server.auth_utils.decode_access_token") as mock_decode:
        mock_decode.return_value = {"sub": str(player_id)}

        result = await validate_token_impl(token, player_id, mock_manager)

        assert result is False


@pytest.mark.asyncio
async def test_delegate_health_monitor_success():
    """Test delegate_health_monitor() successfully delegates to monitor."""
    mock_monitor = MagicMock()
    mock_method = AsyncMock()
    mock_monitor.check_health = mock_method
    active_websockets: dict[str, Any] = {}
    connection_metadata: dict[str, Any] = {}
    player_websockets: dict[str, Any] = {}

    await delegate_health_monitor(
        mock_monitor, "check_health", active_websockets, connection_metadata, player_websockets
    )

    mock_method.assert_called_once_with(
        active_websockets=active_websockets,
        connection_metadata=connection_metadata,
        player_websockets=player_websockets,
    )


@pytest.mark.asyncio
async def test_delegate_health_monitor_none():
    """Test delegate_health_monitor() handles None monitor."""
    await delegate_health_monitor(None, "check_health", {}, {}, {})

    # Should not raise, just log error


def test_delegate_health_monitor_sync_success():
    """Test delegate_health_monitor_sync() successfully delegates to monitor."""
    mock_monitor = MagicMock()
    mock_method = MagicMock()
    mock_monitor.get_stats = mock_method
    active_websockets: dict[str, Any] = {}
    connection_metadata: dict[str, Any] = {}
    player_websockets: dict[str, Any] = {}

    delegate_health_monitor_sync(mock_monitor, "get_stats", active_websockets, connection_metadata, player_websockets)

    mock_method.assert_called_once_with(
        active_websockets=active_websockets,
        connection_metadata=connection_metadata,
        player_websockets=player_websockets,
    )


def test_delegate_health_monitor_sync_none():
    """Test delegate_health_monitor_sync() handles None monitor."""
    delegate_health_monitor_sync(None, "get_stats", {}, {}, {})

    # Should not raise, just log error


@pytest.mark.asyncio
async def test_delegate_connection_cleaner_success():
    """Test delegate_connection_cleaner() successfully delegates to cleaner."""
    mock_cleaner = MagicMock()
    mock_method = AsyncMock(return_value={"cleaned": True})
    mock_cleaner.cleanup = mock_method
    default_error = {"error": "default"}

    result = await delegate_connection_cleaner(mock_cleaner, "cleanup", default_error, "arg1", key="value")

    assert result == {"cleaned": True}
    mock_method.assert_called_once_with("arg1", key="value")


@pytest.mark.asyncio
async def test_delegate_connection_cleaner_none():
    """Test delegate_connection_cleaner() returns default when cleaner is None."""
    default_error = {"error": "default"}

    result = await delegate_connection_cleaner(None, "cleanup", default_error)

    assert result == default_error


def test_delegate_connection_cleaner_sync_success():
    """Test delegate_connection_cleaner_sync() successfully delegates to cleaner."""
    mock_cleaner = MagicMock()
    mock_method = MagicMock()
    mock_cleaner.cleanup_sync = mock_method

    delegate_connection_cleaner_sync(mock_cleaner, "cleanup_sync", key="value")

    mock_method.assert_called_once_with(key="value")


def test_delegate_connection_cleaner_sync_none():
    """Test delegate_connection_cleaner_sync() handles None cleaner."""
    delegate_connection_cleaner_sync(None, "cleanup_sync")

    # Should not raise, just log error


@pytest.mark.asyncio
async def test_delegate_game_state_provider_success():
    """Test delegate_game_state_provider() successfully delegates to provider."""
    mock_provider = MagicMock()
    mock_method = AsyncMock(return_value={"state": "ready"})
    mock_provider.get_state = mock_method
    default_return: dict[str, Any] = {"state": "default"}

    result = await delegate_game_state_provider(mock_provider, "get_state", default_return, "arg1", key="value")

    assert result == {"state": "ready"}
    mock_method.assert_called_once_with("arg1", key="value")


@pytest.mark.asyncio
async def test_delegate_game_state_provider_none():
    """Test delegate_game_state_provider() returns default when provider is None."""
    default_return: dict[str, Any] = {"state": "default"}

    result = await delegate_game_state_provider(None, "get_state", default_return)

    assert result == default_return


def test_delegate_game_state_provider_sync_success():
    """Test delegate_game_state_provider_sync() successfully delegates to provider."""
    mock_provider = MagicMock()
    mock_method = MagicMock(return_value={"state": "ready"})
    mock_provider.get_state_sync = mock_method
    default_return: dict[str, Any] = {"state": "default"}

    result = delegate_game_state_provider_sync(mock_provider, "get_state_sync", default_return, "arg1", key="value")

    assert result == {"state": "ready"}
    mock_method.assert_called_once_with("arg1", key="value")


def test_delegate_game_state_provider_sync_none():
    """Test delegate_game_state_provider_sync() returns default when provider is None."""
    default_return: dict[str, Any] = {"state": "default"}

    result = delegate_game_state_provider_sync(None, "get_state_sync", default_return)

    assert result == default_return


@pytest.mark.asyncio
async def test_delegate_message_broadcaster_success():
    """Test delegate_message_broadcaster() successfully delegates to broadcaster."""
    mock_broadcaster = MagicMock()
    mock_method = AsyncMock(return_value={"sent": True})
    mock_broadcaster.broadcast = mock_method
    default_return = {"error": "default"}
    player_websockets: dict[str, Any] = {}

    result = await delegate_message_broadcaster(
        mock_broadcaster, "broadcast", default_return, player_websockets, "arg1", key="value"
    )

    assert result == {"sent": True}
    mock_method.assert_called_once_with(player_websockets, "arg1", key="value")


@pytest.mark.asyncio
async def test_delegate_message_broadcaster_broadcast_global():
    """Test delegate_message_broadcaster() handles broadcast_global method."""
    mock_broadcaster = MagicMock()
    mock_method = AsyncMock(return_value={"sent": True})
    mock_broadcaster.broadcast_global = mock_method
    default_return: dict[str, Any] = {}
    player_websockets: dict[str, Any] = {}
    event = {"type": "chat", "message": "Hello"}
    exclude_player = uuid.uuid4()

    result = await delegate_message_broadcaster(
        mock_broadcaster, "broadcast_global", default_return, player_websockets, event, exclude_player=exclude_player
    )

    assert result == {"sent": True}
    mock_method.assert_called_once_with(event, str(exclude_player), player_websockets)


@pytest.mark.asyncio
async def test_delegate_message_broadcaster_broadcast_to_room():
    """Test delegate_message_broadcaster() handles broadcast_to_room method."""
    mock_broadcaster = MagicMock()
    mock_method = AsyncMock(return_value={"sent": True})
    mock_broadcaster.broadcast_to_room = mock_method
    default_return: dict[str, Any] = {}
    player_websockets: dict[str, Any] = {}
    room_id = "room_123"
    event = {"type": "chat", "message": "Hello"}
    exclude_player = uuid.uuid4()

    result = await delegate_message_broadcaster(
        mock_broadcaster,
        "broadcast_to_room",
        default_return,
        player_websockets,
        room_id=room_id,
        event=event,
        exclude_player=exclude_player,
    )

    assert result == {"sent": True}
    mock_method.assert_called_once_with(room_id, event, exclude_player, player_websockets)


@pytest.mark.asyncio
async def test_delegate_message_broadcaster_none():
    """Test delegate_message_broadcaster() returns default when broadcaster is None."""
    default_return = {"error": "default"}

    result = await delegate_message_broadcaster(None, "broadcast", default_return, {})

    assert result == default_return


@pytest.mark.asyncio
async def test_delegate_personal_message_sender_success():
    """Test delegate_personal_message_sender() successfully delegates to sender."""
    mock_sender = MagicMock()
    mock_method = AsyncMock(return_value={"sent": True})
    mock_sender.send = mock_method
    default_return = {"error": "default"}
    player_websockets: dict[str, Any] = {}
    active_websockets: dict[str, Any] = {}

    result = await delegate_personal_message_sender(
        mock_sender, "send", default_return, player_websockets, active_websockets, "arg1", key="value"
    )

    assert result == {"sent": True}
    mock_method.assert_called_once_with(player_websockets, active_websockets, "arg1", key="value")


@pytest.mark.asyncio
async def test_delegate_personal_message_sender_send_message():
    """Test delegate_personal_message_sender() handles send_message method."""
    mock_sender = MagicMock()
    mock_method = AsyncMock(return_value={"sent": True})
    mock_sender.send_message = mock_method
    default_return: dict[str, Any] = {}
    player_websockets: dict[str, Any] = {}
    active_websockets: dict[str, Any] = {}
    player_id = uuid.uuid4()
    event = {"type": "chat", "message": "Hello"}

    result = await delegate_personal_message_sender(
        mock_sender,
        "send_message",
        default_return,
        player_websockets,
        active_websockets,
        player_id=player_id,
        event=event,
    )

    assert result == {"sent": True}
    mock_method.assert_called_once_with(player_id, event, player_websockets, active_websockets)


@pytest.mark.asyncio
async def test_delegate_personal_message_sender_none():
    """Test delegate_personal_message_sender() returns default when sender is None."""
    default_return = {"error": "default"}

    result = await delegate_personal_message_sender(None, "send", default_return, {}, {})

    assert result == default_return


def test_delegate_personal_message_sender_sync_success():
    """Test delegate_personal_message_sender_sync() successfully delegates to sender."""
    mock_sender = MagicMock()
    mock_method = MagicMock(return_value={"sent": True})
    mock_sender.send_sync = mock_method
    default_return = {"error": "default"}
    player_websockets: dict[str, Any] = {}

    result = delegate_personal_message_sender_sync(
        mock_sender, "send_sync", default_return, player_websockets, "arg1", key="value"
    )

    assert result == {"sent": True}
    mock_method.assert_called_once_with(player_websockets, "arg1", key="value")


def test_delegate_personal_message_sender_sync_none():
    """Test delegate_personal_message_sender_sync() returns default when sender is None."""
    default_return = {"error": "default"}

    result = delegate_personal_message_sender_sync(None, "send_sync", default_return, {})

    assert result == default_return


@pytest.mark.asyncio
async def test_delegate_room_event_handler_success():
    """Test delegate_room_event_handler() successfully delegates to handler."""
    mock_handler = MagicMock()
    mock_method = AsyncMock()
    mock_handler.handle_event = mock_method

    await delegate_room_event_handler(mock_handler, "handle_event", "arg1", key="value")

    mock_method.assert_called_once_with("arg1", key="value")


@pytest.mark.asyncio
async def test_delegate_room_event_handler_none():
    """Test delegate_room_event_handler() handles None handler."""
    await delegate_room_event_handler(None, "handle_event")

    # Should not raise, just log error
