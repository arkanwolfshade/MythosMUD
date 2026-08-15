"""
Unit tests for connection session management.

Tests the connection_session_management module functions.
"""

# pyright: reportPrivateUsage=false
# Reason: this module unit-tests private helpers in connection_session_management.

from __future__ import annotations

import uuid
from typing import cast, final, override

import pytest
from fastapi import WebSocket

from server.realtime.connection_models import ConnectionMetadata
from server.realtime.connection_session_management import (
    _cleanup_old_session_tracking,
    _cleanup_player_data_for_session,
    _disconnect_all_connections_for_session,
    _disconnect_connection_for_session,
    _is_websocket_connected,
    _SessionConnectionManager,
    handle_new_game_session_impl,
)


@final
class _FakeClientState:
    name: str

    def __init__(self, name: str) -> None:
        self.name = name


@final
class _FakeWebSocket:
    client_state: _FakeClientState
    close_calls: int
    close_error: BaseException | None

    def __init__(self, state_name: str = "CONNECTED") -> None:
        self.client_state = _FakeClientState(state_name)
        self.close_calls = 0
        self.close_error = None

    async def close(self, code: int = 1000, reason: str = "") -> None:
        del code, reason
        if self.close_error is not None:
            raise self.close_error
        self.close_calls += 1


@final
class _WsMissingClientState:
    """Stand-in whose missing client_state trips AttributeError in the helper."""


@final
class _EmptyClientState:
    """client_state without a name attribute."""


@final
class _WsMissingName:
    client_state: _EmptyClientState

    def __init__(self) -> None:
        self.client_state = _EmptyClientState()


@final
class _FakeRateLimiter:
    removed: list[str]

    def __init__(self) -> None:
        self.removed = []

    def remove_player_data(self, player_id: str) -> None:
        self.removed.append(player_id)


@final
class _FakeMessageQueue:
    removed: list[str]

    def __init__(self) -> None:
        self.removed = []

    def remove_player_messages(self, player_id: str) -> None:
        self.removed.append(player_id)


@final
class _FakeRoomManager:
    remove_calls: list[str]

    def __init__(self) -> None:
        self.remove_calls = []

    def remove_player_from_all_rooms(self, player_id: str) -> bool:
        self.remove_calls.append(player_id)
        return True


class _DelKeyErrorSockets(dict[str, WebSocket]):
    @override
    def __delitem__(self, key: str) -> None:
        raise KeyError(key)


class _FakeSessionManager:
    """Typed stand-in for ConnectionManager; MagicMock attributes are Any."""

    def __init__(self) -> None:
        self.active_websockets: dict[str, WebSocket] = {}
        self.connection_metadata: dict[str, ConnectionMetadata] = {}
        self.player_websockets: dict[uuid.UUID, list[str]] = {}
        self.player_sessions: dict[uuid.UUID, str] = {}
        self.session_connections: dict[str, list[str]] = {}
        self.session_disconnect_times: dict[str, float] = {}
        self.last_seen: dict[uuid.UUID, float] = {}
        self.last_active_update_times: dict[uuid.UUID, float] = {}
        self.rate_limiter: _FakeRateLimiter = _FakeRateLimiter()
        self.message_queue: _FakeMessageQueue = _FakeMessageQueue()
        self.room_manager: _FakeRoomManager = _FakeRoomManager()


def _make_manager() -> _FakeSessionManager:
    return _FakeSessionManager()


def _as_ws(websocket: object) -> WebSocket:
    return cast(WebSocket, websocket)


def _as_mgr(manager: _FakeSessionManager) -> _SessionConnectionManager:
    return cast(_SessionConnectionManager, cast(object, manager))


def _meta(connection_id: str, player_id: uuid.UUID) -> ConnectionMetadata:
    return ConnectionMetadata(
        connection_id=connection_id,
        player_id=player_id,
        connection_type="websocket",
        established_at=0.0,
        last_seen=0.0,
        is_healthy=True,
    )


def test_is_websocket_connected_connected():
    """Test _is_websocket_connected() returns True for connected websocket."""
    result = _is_websocket_connected(_as_ws(_FakeWebSocket("CONNECTED")))

    assert result is True


def test_is_websocket_connected_disconnected():
    """Test _is_websocket_connected() returns False for disconnected websocket."""
    result = _is_websocket_connected(_as_ws(_FakeWebSocket("DISCONNECTED")))

    assert result is False


def test_is_websocket_connected_no_client_state():
    """Test _is_websocket_connected() handles missing client_state."""
    result = _is_websocket_connected(_as_ws(_WsMissingClientState()))

    assert result is False


def test_is_websocket_connected_no_name():
    """Test _is_websocket_connected() handles missing name attribute."""
    result = _is_websocket_connected(_as_ws(_WsMissingName()))

    assert result is False


@pytest.mark.asyncio
async def test_disconnect_connection_for_session_success():
    """Test _disconnect_connection_for_session() successfully disconnects connection."""
    connection_id = "conn_123"
    player_id = uuid.uuid4()
    mock_manager = _make_manager()
    mock_websocket = _FakeWebSocket("CONNECTED")
    mock_manager.active_websockets = {connection_id: _as_ws(mock_websocket)}

    result = await _disconnect_connection_for_session(connection_id, player_id, _as_mgr(mock_manager))

    assert result is True
    assert mock_websocket.close_calls == 1
    assert connection_id not in mock_manager.active_websockets


@pytest.mark.asyncio
async def test_disconnect_connection_for_session_not_in_active():
    """Test _disconnect_connection_for_session() returns False when not in active_websockets."""
    connection_id = "conn_123"
    player_id = uuid.uuid4()
    mock_manager = _make_manager()

    result = await _disconnect_connection_for_session(connection_id, player_id, _as_mgr(mock_manager))

    assert result is False


@pytest.mark.asyncio
async def test_disconnect_connection_for_session_none_websocket():
    """Test _disconnect_connection_for_session() handles None websocket."""
    connection_id = "conn_123"
    player_id = uuid.uuid4()
    mock_manager = _make_manager()
    mock_manager.active_websockets = cast(dict[str, WebSocket], {connection_id: None})

    result = await _disconnect_connection_for_session(connection_id, player_id, _as_mgr(mock_manager))

    assert result is False
    assert connection_id not in mock_manager.active_websockets


@pytest.mark.asyncio
async def test_disconnect_connection_for_session_not_connected():
    """Test _disconnect_connection_for_session() handles disconnected websocket."""
    connection_id = "conn_123"
    player_id = uuid.uuid4()
    mock_manager = _make_manager()
    mock_websocket = _FakeWebSocket("DISCONNECTED")
    mock_manager.active_websockets = {connection_id: _as_ws(mock_websocket)}

    result = await _disconnect_connection_for_session(connection_id, player_id, _as_mgr(mock_manager))

    assert result is True
    assert mock_websocket.close_calls == 0
    assert connection_id not in mock_manager.active_websockets


@pytest.mark.asyncio
async def test_disconnect_connection_for_session_close_error():
    """Test _disconnect_connection_for_session() handles close error."""
    from server.exceptions import DatabaseError

    connection_id = "conn_123"
    player_id = uuid.uuid4()
    mock_manager = _make_manager()
    mock_websocket = _FakeWebSocket("CONNECTED")
    mock_websocket.close_error = DatabaseError("Close error")
    mock_manager.active_websockets = {connection_id: _as_ws(mock_websocket)}

    result = await _disconnect_connection_for_session(connection_id, player_id, _as_mgr(mock_manager))

    assert result is True
    assert connection_id not in mock_manager.active_websockets


@pytest.mark.asyncio
async def test_disconnect_connection_for_session_key_error():
    """Test _disconnect_connection_for_session() handles KeyError when deleting."""
    connection_id = "conn_123"
    player_id = uuid.uuid4()
    mock_manager = _make_manager()
    mock_websocket = _FakeWebSocket("CONNECTED")
    mock_manager.active_websockets = _DelKeyErrorSockets({connection_id: _as_ws(mock_websocket)})

    result = await _disconnect_connection_for_session(connection_id, player_id, _as_mgr(mock_manager))

    assert result is True


@pytest.mark.asyncio
async def test_disconnect_all_connections_for_session():
    """Test _disconnect_all_connections_for_session() disconnects all connections."""
    connection_id1 = "conn_1"
    connection_id2 = "conn_2"
    player_id = uuid.uuid4()
    mock_manager = _make_manager()
    mock_manager.active_websockets = {
        connection_id1: _as_ws(_FakeWebSocket("CONNECTED")),
        connection_id2: _as_ws(_FakeWebSocket("CONNECTED")),
    }
    mock_manager.connection_metadata = {
        connection_id1: _meta(connection_id1, player_id),
        connection_id2: _meta(connection_id2, player_id),
    }
    mock_manager.player_websockets = {player_id: [connection_id1, connection_id2]}

    result = await _disconnect_all_connections_for_session(
        [connection_id1, connection_id2], player_id, _as_mgr(mock_manager)
    )

    assert result == 2
    assert connection_id1 not in mock_manager.active_websockets
    assert connection_id2 not in mock_manager.active_websockets
    assert connection_id1 not in mock_manager.connection_metadata
    assert connection_id2 not in mock_manager.connection_metadata
    assert player_id not in mock_manager.player_websockets


@pytest.mark.asyncio
async def test_disconnect_all_connections_for_session_empty_list():
    """Test _disconnect_all_connections_for_session() handles empty list."""
    player_id = uuid.uuid4()
    mock_manager = _make_manager()

    result = await _disconnect_all_connections_for_session([], player_id, _as_mgr(mock_manager))

    assert result == 0


@pytest.mark.asyncio
async def test_disconnect_all_connections_for_session_partial_success():
    """Test _disconnect_all_connections_for_session() handles partial disconnections."""
    connection_id1 = "conn_1"
    connection_id2 = "conn_2"
    player_id = uuid.uuid4()
    mock_manager = _make_manager()
    mock_manager.active_websockets = {connection_id1: _as_ws(_FakeWebSocket("CONNECTED"))}
    mock_manager.connection_metadata = {connection_id1: _meta(connection_id1, player_id)}
    mock_manager.player_websockets = {player_id: [connection_id1, connection_id2]}

    result = await _disconnect_all_connections_for_session(
        [connection_id1, connection_id2], player_id, _as_mgr(mock_manager)
    )

    assert result == 1
    assert connection_id1 not in mock_manager.active_websockets


def test_cleanup_old_session_tracking_no_player():
    """Test _cleanup_old_session_tracking() handles player not in player_sessions."""
    player_id = uuid.uuid4()
    mock_manager = _make_manager()

    _cleanup_old_session_tracking(player_id, _as_mgr(mock_manager))


def test_cleanup_old_session_tracking_success():
    """Test _cleanup_old_session_tracking() cleans up old session on reconnect."""
    player_id = uuid.uuid4()
    old_session_id = "old_session"
    mock_manager = _make_manager()
    mock_manager.player_sessions = {player_id: old_session_id}
    mock_manager.session_connections = {old_session_id: ["conn_1", "conn_2"]}
    mock_manager.session_disconnect_times = {old_session_id: 1234567890.0}

    _cleanup_old_session_tracking(player_id, _as_mgr(mock_manager))

    assert old_session_id not in mock_manager.session_connections
    assert old_session_id not in mock_manager.session_disconnect_times


def test_cleanup_old_session_tracking_session_not_in_connections():
    """Test _cleanup_old_session_tracking() handles session not in session_connections."""
    player_id = uuid.uuid4()
    old_session_id = "old_session"
    mock_manager = _make_manager()
    mock_manager.player_sessions = {player_id: old_session_id}

    _cleanup_old_session_tracking(player_id, _as_mgr(mock_manager))


def test_cleanup_player_data_for_session():
    """Test _cleanup_player_data_for_session() cleans up all player data."""
    player_id = uuid.uuid4()
    mock_manager = _make_manager()
    mock_manager.last_seen = {player_id: 1234567890.0}
    mock_manager.last_active_update_times = {player_id: 1234567890.0}

    _cleanup_player_data_for_session(player_id, _as_mgr(mock_manager))

    assert mock_manager.rate_limiter.removed == [str(player_id)]
    assert mock_manager.message_queue.removed == [str(player_id)]
    assert player_id not in mock_manager.last_seen
    assert player_id not in mock_manager.last_active_update_times
    assert mock_manager.room_manager.remove_calls == [str(player_id)]


def test_cleanup_player_data_for_session_no_last_seen():
    """Test _cleanup_player_data_for_session() handles player not in last_seen."""
    player_id = uuid.uuid4()
    mock_manager = _make_manager()

    _cleanup_player_data_for_session(player_id, _as_mgr(mock_manager))


@pytest.mark.asyncio
async def test_handle_new_game_session_impl_success():
    """Test handle_new_game_session_impl() successfully handles new session."""
    player_id = uuid.uuid4()
    new_session_id = "new_session"
    old_session_id = "old_session"
    connection_id = "conn_123"
    mock_manager = _make_manager()
    mock_websocket = _FakeWebSocket("CONNECTED")
    mock_manager.player_websockets = {player_id: [connection_id]}
    mock_manager.active_websockets = {connection_id: _as_ws(mock_websocket)}
    mock_manager.connection_metadata = {connection_id: _meta(connection_id, player_id)}
    mock_manager.player_sessions = {player_id: old_session_id}
    mock_manager.session_connections = {old_session_id: [connection_id]}

    result = await handle_new_game_session_impl(player_id, new_session_id, _as_mgr(mock_manager))

    assert result["success"] is True
    assert result["player_id"] == player_id
    assert result["new_session_id"] == new_session_id
    assert result["previous_session_id"] == old_session_id
    assert result["connections_disconnected"] == 1
    assert result["websocket_connections"] == 1
    assert mock_manager.player_sessions[player_id] == new_session_id
    assert new_session_id in mock_manager.session_connections
    assert old_session_id not in mock_manager.session_connections


@pytest.mark.asyncio
async def test_handle_new_game_session_impl_same_session_is_noop():
    """Same session_id must not close the live socket (HTTP after WS, recover)."""
    player_id = uuid.uuid4()
    session_id = "same_session"
    connection_id = "conn_live"
    mock_manager = _make_manager()
    mock_websocket = _FakeWebSocket("CONNECTED")
    mock_manager.player_websockets = {player_id: [connection_id]}
    mock_manager.active_websockets = {connection_id: _as_ws(mock_websocket)}
    mock_manager.connection_metadata = {connection_id: _meta(connection_id, player_id)}
    mock_manager.player_sessions = {player_id: session_id}
    mock_manager.session_connections = {session_id: [connection_id]}

    result = await handle_new_game_session_impl(player_id, session_id, _as_mgr(mock_manager))

    assert result["success"] is True
    assert result["connections_disconnected"] == 0
    assert mock_manager.player_websockets[player_id] == [connection_id]
    assert mock_websocket.close_calls == 0
    assert mock_manager.room_manager.remove_calls == []


@pytest.mark.asyncio
async def test_handle_new_game_session_impl_no_existing_session():
    """Test handle_new_game_session_impl() handles player with no existing session."""
    player_id = uuid.uuid4()
    new_session_id = "new_session"
    mock_manager = _make_manager()

    result = await handle_new_game_session_impl(player_id, new_session_id, _as_mgr(mock_manager))

    assert result["success"] is True
    assert result["previous_session_id"] is None
    assert result["connections_disconnected"] == 0
    assert result["websocket_connections"] == 0


@pytest.mark.asyncio
async def test_handle_new_game_session_impl_error():
    """Test handle_new_game_session_impl() handles errors."""
    player_id = uuid.uuid4()
    new_session_id = "new_session"
    mock_manager = _make_manager()
    del mock_manager.player_sessions

    result = await handle_new_game_session_impl(player_id, new_session_id, _as_mgr(mock_manager))

    assert result["success"] is False
    assert len(result["errors"]) > 0
