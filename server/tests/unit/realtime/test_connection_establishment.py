"""
Unit tests for connection establishment.

Tests the connection_establishment module functions.
"""

# pyright: reportPrivateUsage=false
# Reason: this module unit-tests private helpers in connection_establishment.

from __future__ import annotations

import asyncio
import uuid
from typing import cast, final
from unittest.mock import AsyncMock, MagicMock, patch

import pytest
from fastapi import WebSocket

from server.realtime.connection_establishment import (
    _cleanup_dead_connections,
    _cleanup_failed_connection,
    _EstablishmentConnectionManager,
    _find_dead_connections,
    _register_new_connection,
    _remove_dead_connection,
    _setup_connection_metadata,
    _setup_player_and_room,
    _setup_session_tracking,
    _track_player_presence,
    _update_player_connection_list,
)
from server.realtime.connection_models import ConnectionMetadata


@final
class _FakeClientState:
    name: str

    def __init__(self, name: str) -> None:
        self.name = name


@final
class _FakeWebSocket:
    client_state: _FakeClientState
    accept_calls: int
    close_calls: int
    accept_error: BaseException | None

    def __init__(self, state_name: str = "CONNECTED") -> None:
        self.client_state = _FakeClientState(state_name)
        self.accept_calls = 0
        self.close_calls = 0
        self.accept_error = None

    async def accept(self) -> None:
        if self.accept_error is not None:
            raise self.accept_error
        self.accept_calls += 1

    async def close(self, code: int = 1000, reason: str = "") -> None:
        del code, reason
        self.close_calls += 1


@final
class _FakeRoomManager:
    subscribe_calls: list[tuple[str, str]]
    remove_calls: list[str]

    def __init__(self) -> None:
        self.subscribe_calls = []
        self.remove_calls = []

    def subscribe_to_room(self, player_id: str, room_id: str) -> None:
        self.subscribe_calls.append((player_id, room_id))

    def remove_player_from_all_rooms(self, player_id: str) -> bool:
        self.remove_calls.append(player_id)
        return True


@final
class _FakePerformanceTracker:
    establish_calls: int

    def __init__(self) -> None:
        self.establish_calls = 0

    def record_connection_establishment(self, connection_type: str, duration_ms: float) -> None:
        del connection_type, duration_ms
        self.establish_calls += 1


class _FakeEstablishmentManager:
    """Typed stand-in for ConnectionManager; MagicMock attributes are Any."""

    def __init__(self) -> None:
        self.active_websockets: dict[str, WebSocket] = {}
        self.connection_metadata: dict[str, ConnectionMetadata] = {}
        self.player_websockets: dict[uuid.UUID, list[str]] = {}
        self.disconnect_lock: asyncio.Lock = asyncio.Lock()
        self.session_connections: dict[str, list[str]] = {}
        self.player_sessions: dict[uuid.UUID, str] = {}
        self.async_persistence: object | None = MagicMock()
        self.room_manager: _FakeRoomManager = _FakeRoomManager()
        self.online_players: dict[uuid.UUID, dict[str, object]] = {}
        self.performance_tracker: _FakePerformanceTracker = _FakePerformanceTracker()
        self.session_disconnect_times: dict[str, float] = {}
        self.last_seen: dict[uuid.UUID, float] = {}
        self.last_active_update_times: dict[uuid.UUID, float] = {}
        self.rate_limiter: MagicMock = MagicMock()
        self.message_queue: MagicMock = MagicMock()
        self.grace_period_players: dict[uuid.UUID, object] = {}
        self.resting_players: dict[uuid.UUID, asyncio.Task[None]] = {}
        self.get_player: AsyncMock = AsyncMock(return_value=None)
        self.track_player_connected: AsyncMock = AsyncMock()
        self.broadcast_connection_message: AsyncMock = AsyncMock()


def _make_manager() -> _FakeEstablishmentManager:
    return _FakeEstablishmentManager()


def _as_ws(websocket: _FakeWebSocket) -> WebSocket:
    return cast(WebSocket, cast(object, websocket))


def _as_mgr(manager: _FakeEstablishmentManager) -> _EstablishmentConnectionManager:
    return cast(_EstablishmentConnectionManager, cast(object, manager))


def _meta(connection_id: str, player_id: uuid.UUID) -> ConnectionMetadata:
    return ConnectionMetadata(
        connection_id=connection_id,
        player_id=player_id,
        connection_type="websocket",
        established_at=0.0,
        last_seen=0.0,
        is_healthy=True,
    )


def test_find_dead_connections_no_player():
    """Test _find_dead_connections() returns empty list when player not found."""
    player_id = uuid.uuid4()
    mock_manager = _make_manager()

    result = _find_dead_connections(player_id, _as_mgr(mock_manager))

    assert result == []


def test_find_dead_connections_all_active():
    """Test _find_dead_connections() returns empty list when all connections are active."""
    player_id = uuid.uuid4()
    connection_id = "conn_123"
    mock_manager = _make_manager()
    mock_websocket = _FakeWebSocket("CONNECTED")
    mock_manager.player_websockets = {player_id: [connection_id]}
    mock_manager.active_websockets = {connection_id: _as_ws(mock_websocket)}

    result = _find_dead_connections(player_id, _as_mgr(mock_manager))

    assert result == []


def test_find_dead_connections_not_in_active():
    """Test _find_dead_connections() skips connections not in active_websockets."""
    player_id = uuid.uuid4()
    connection_id = "conn_123"
    mock_manager = _make_manager()
    mock_manager.player_websockets = {player_id: [connection_id]}

    result = _find_dead_connections(player_id, _as_mgr(mock_manager))

    assert result == []


def test_find_dead_connections_none_websocket():
    """Test _find_dead_connections() raises ConnectionError when websocket is None."""
    player_id = uuid.uuid4()
    connection_id = "conn_123"
    mock_manager = _make_manager()
    mock_manager.player_websockets = {player_id: [connection_id]}
    mock_manager.active_websockets = cast(dict[str, WebSocket], {connection_id: None})

    with pytest.raises(ConnectionError, match="WebSocket is None"):
        _ = _find_dead_connections(player_id, _as_mgr(mock_manager))


def test_find_dead_connections_not_connected():
    """Test _find_dead_connections() finds dead connections."""
    player_id = uuid.uuid4()
    connection_id = "conn_123"
    mock_manager = _make_manager()
    mock_websocket = _FakeWebSocket("DISCONNECTED")
    mock_manager.player_websockets = {player_id: [connection_id]}
    mock_manager.active_websockets = {connection_id: _as_ws(mock_websocket)}

    result = _find_dead_connections(player_id, _as_mgr(mock_manager))

    assert connection_id in result


def test_remove_dead_connection():
    """Test _remove_dead_connection() removes connection from tracking."""
    connection_id = "conn_123"
    player_id = uuid.uuid4()
    mock_manager = _make_manager()
    mock_manager.active_websockets = {connection_id: _as_ws(_FakeWebSocket())}
    mock_manager.connection_metadata = {connection_id: _meta(connection_id, player_id)}

    _remove_dead_connection(connection_id, _as_mgr(mock_manager))

    assert connection_id not in mock_manager.active_websockets
    assert connection_id not in mock_manager.connection_metadata


def test_remove_dead_connection_not_present():
    """Test _remove_dead_connection() handles connection not present."""
    connection_id = "conn_123"
    mock_manager = _make_manager()

    _remove_dead_connection(connection_id, _as_mgr(mock_manager))


def test_update_player_connection_list_no_player():
    """Test _update_player_connection_list() handles player not in player_websockets."""
    player_id = uuid.uuid4()
    mock_manager = _make_manager()

    _update_player_connection_list(player_id, _as_mgr(mock_manager))


def test_update_player_connection_list_with_active():
    """Test _update_player_connection_list() keeps active connections."""
    player_id = uuid.uuid4()
    active_conn = "conn_active"
    dead_conn = "conn_dead"
    mock_manager = _make_manager()
    mock_manager.player_websockets = {player_id: [active_conn, dead_conn]}
    mock_manager.active_websockets = {active_conn: _as_ws(_FakeWebSocket())}

    _update_player_connection_list(player_id, _as_mgr(mock_manager))

    assert mock_manager.player_websockets[player_id] == [active_conn]


def test_update_player_connection_list_no_active():
    """Test _update_player_connection_list() removes player when no active connections."""
    player_id = uuid.uuid4()
    dead_conn = "conn_dead"
    mock_manager = _make_manager()
    mock_manager.player_websockets = {player_id: [dead_conn]}

    _update_player_connection_list(player_id, _as_mgr(mock_manager))

    assert player_id not in mock_manager.player_websockets


@pytest.mark.asyncio
async def test_cleanup_dead_connections_empty_list():
    """Test _cleanup_dead_connections() handles empty list."""
    player_id = uuid.uuid4()
    mock_manager = _make_manager()

    await _cleanup_dead_connections([], player_id, _as_mgr(mock_manager))


@pytest.mark.asyncio
async def test_cleanup_dead_connections_with_dead():
    """Test _cleanup_dead_connections() cleans up dead connections."""
    player_id = uuid.uuid4()
    dead_conn = "conn_dead"
    mock_manager = _make_manager()
    mock_manager.connection_metadata = {dead_conn: _meta(dead_conn, player_id)}
    mock_manager.player_websockets = {player_id: [dead_conn]}

    await _cleanup_dead_connections([dead_conn], player_id, _as_mgr(mock_manager))

    assert dead_conn not in mock_manager.active_websockets
    assert dead_conn not in mock_manager.connection_metadata


def test_register_new_connection():
    """Test _register_new_connection() registers new connection."""
    mock_websocket = _as_ws(_FakeWebSocket())
    player_id = uuid.uuid4()
    mock_manager = _make_manager()

    connection_id = _register_new_connection(mock_websocket, player_id, _as_mgr(mock_manager))

    assert connection_id is not None
    assert connection_id in mock_manager.active_websockets
    assert mock_manager.active_websockets[connection_id] == mock_websocket
    assert player_id in mock_manager.player_websockets
    assert connection_id in mock_manager.player_websockets[player_id]


def test_register_new_connection_existing_player():
    """Test _register_new_connection() adds to existing player connections."""
    mock_websocket = _as_ws(_FakeWebSocket())
    player_id = uuid.uuid4()
    existing_conn = "existing_conn"
    mock_manager = _make_manager()
    mock_manager.player_websockets = {player_id: [existing_conn]}

    connection_id = _register_new_connection(mock_websocket, player_id, _as_mgr(mock_manager))

    assert connection_id in mock_manager.player_websockets[player_id]
    assert existing_conn in mock_manager.player_websockets[player_id]
    assert len(mock_manager.player_websockets[player_id]) == 2


def test_setup_connection_metadata():
    """Test _setup_connection_metadata() creates metadata."""
    connection_id = "conn_123"
    player_id = uuid.uuid4()
    session_id = "session_123"
    token = "jwt_token"
    mock_manager = _make_manager()

    _setup_connection_metadata(connection_id, player_id, _as_mgr(mock_manager), session_id, token)

    assert connection_id in mock_manager.connection_metadata
    metadata = mock_manager.connection_metadata[connection_id]
    assert metadata.connection_id == connection_id
    assert metadata.player_id == player_id
    assert metadata.session_id == session_id
    assert metadata.token == token


def test_setup_connection_metadata_no_session_token():
    """Test _setup_connection_metadata() handles None session and token."""
    connection_id = "conn_123"
    player_id = uuid.uuid4()
    mock_manager = _make_manager()

    _setup_connection_metadata(connection_id, player_id, _as_mgr(mock_manager), None, None)

    metadata = mock_manager.connection_metadata[connection_id]
    assert metadata.session_id is None
    assert metadata.token is None
    assert metadata.last_token_validation is None


def test_setup_session_tracking_no_session_id():
    """Test _setup_session_tracking() handles None session_id."""
    connection_id = "conn_123"
    player_id = uuid.uuid4()
    mock_manager = _make_manager()

    _setup_session_tracking(connection_id, player_id, None, _as_mgr(mock_manager))

    assert connection_id not in str(mock_manager.session_connections.values())


def test_setup_session_tracking_new_session():
    """Test _setup_session_tracking() creates new session entry."""
    connection_id = "conn_123"
    player_id = uuid.uuid4()
    session_id = "session_123"
    mock_manager = _make_manager()

    _setup_session_tracking(connection_id, player_id, session_id, _as_mgr(mock_manager))

    assert session_id in mock_manager.session_connections
    assert connection_id in mock_manager.session_connections[session_id]
    assert mock_manager.player_sessions[player_id] == session_id


def test_setup_session_tracking_existing_session():
    """Test _setup_session_tracking() adds to existing session."""
    connection_id = "conn_123"
    player_id = uuid.uuid4()
    session_id = "session_123"
    existing_conn = "existing_conn"
    mock_manager = _make_manager()
    mock_manager.session_connections = {session_id: [existing_conn]}
    mock_manager.player_sessions = {player_id: session_id}

    _setup_session_tracking(connection_id, player_id, session_id, _as_mgr(mock_manager))

    assert len(mock_manager.session_connections[session_id]) == 2
    assert connection_id in mock_manager.session_connections[session_id]


@pytest.mark.asyncio
async def test_setup_player_and_room_success():
    """Test _setup_player_and_room() successfully sets up player and room."""
    player_id = uuid.uuid4()
    room_id = "room_123"
    mock_manager = _make_manager()
    mock_player: MagicMock = MagicMock()
    mock_player.current_room_id = room_id
    mock_manager.get_player = AsyncMock(return_value=mock_player)

    success, player = await _setup_player_and_room(player_id, _as_mgr(mock_manager))

    assert success is True
    assert player == mock_player
    assert mock_manager.room_manager.subscribe_calls == [(str(player_id), room_id)]


@pytest.mark.asyncio
async def test_setup_player_and_room_no_player():
    """Test _setup_player_and_room() returns False when player not found."""
    player_id = uuid.uuid4()
    mock_manager = _make_manager()
    mock_manager.get_player = AsyncMock(return_value=None)

    success, player = await _setup_player_and_room(player_id, _as_mgr(mock_manager))

    assert success is False
    assert player is None


@pytest.mark.asyncio
async def test_setup_player_and_room_no_persistence():
    """Test _setup_player_and_room() handles no persistence."""
    player_id = uuid.uuid4()
    mock_manager = _make_manager()
    mock_manager.get_player = AsyncMock(return_value=None)
    mock_manager.async_persistence = None

    success, player = await _setup_player_and_room(player_id, _as_mgr(mock_manager))

    assert success is True
    assert player is None


@pytest.mark.asyncio
async def test_setup_player_and_room_no_room_id():
    """Test _setup_player_and_room() handles player with no room_id."""
    player_id = uuid.uuid4()
    mock_manager = _make_manager()
    mock_player: MagicMock = MagicMock()
    del mock_player.current_room_id
    mock_manager.get_player = AsyncMock(return_value=mock_player)

    success, player = await _setup_player_and_room(player_id, _as_mgr(mock_manager))

    assert success is True
    assert player == mock_player
    assert mock_manager.room_manager.subscribe_calls == []


@pytest.mark.asyncio
async def test_track_player_presence_new_player():
    """Test _track_player_presence() tracks new player."""
    player_id = uuid.uuid4()
    mock_player: MagicMock = MagicMock()
    mock_manager = _make_manager()
    mock_cancel_grace: AsyncMock = AsyncMock()
    mock_cancel_rest: AsyncMock = AsyncMock()

    with (
        patch("server.realtime.connection_establishment.cancel_grace_period", mock_cancel_grace),
        patch("server.commands.rest_command.cancel_rest_countdown", mock_cancel_rest),
    ):
        await _track_player_presence(player_id, mock_player, _as_mgr(mock_manager))

    mock_cancel_grace.assert_called_once_with(player_id, mock_manager)
    mock_cancel_rest.assert_called_once_with(player_id, mock_manager)
    mock_manager.track_player_connected.assert_called_once_with(player_id, mock_player, "websocket")


@pytest.mark.asyncio
async def test_track_player_presence_existing_player():
    """Already-online reconnect still goes through track_player_connected (occupancy setup)."""
    player_id = uuid.uuid4()
    mock_player: MagicMock = MagicMock()
    mock_manager = _make_manager()
    mock_manager.online_players = {player_id: {}}
    mock_cancel_grace: AsyncMock = AsyncMock()
    mock_cancel_rest: AsyncMock = AsyncMock()

    with (
        patch("server.realtime.connection_establishment.cancel_grace_period", mock_cancel_grace),
        patch("server.commands.rest_command.cancel_rest_countdown", mock_cancel_rest),
    ):
        await _track_player_presence(player_id, mock_player, _as_mgr(mock_manager))

    mock_manager.track_player_connected.assert_called_once_with(player_id, mock_player, "websocket")
    mock_cancel_grace.assert_called_once_with(player_id, mock_manager)
    mock_manager.broadcast_connection_message.assert_not_called()


@pytest.mark.asyncio
async def test_track_player_presence_reconnect_during_grace_runs_enter_setup():
    """Linkdead reconnect stays in online_players; enter setup must run before grace cancel."""
    player_id = uuid.uuid4()
    mock_player: MagicMock = MagicMock()
    mock_manager = _make_manager()
    mock_manager.online_players = {player_id: {}}
    mock_manager.grace_period_players = {player_id: MagicMock()}
    mock_cancel_grace: AsyncMock = AsyncMock()
    mock_cancel_rest: AsyncMock = AsyncMock()
    call_order: list[str] = []

    async def track_connected(*_args: object, **_kwargs: object) -> None:
        call_order.append("track")
        assert player_id in mock_manager.grace_period_players

    async def cancel_grace(*_args: object, **_kwargs: object) -> None:
        call_order.append("cancel_grace")

    mock_manager.track_player_connected = AsyncMock(side_effect=track_connected)
    mock_cancel_grace.side_effect = cancel_grace

    with (
        patch("server.realtime.connection_establishment.cancel_grace_period", mock_cancel_grace),
        patch("server.commands.rest_command.cancel_rest_countdown", mock_cancel_rest),
    ):
        await _track_player_presence(player_id, mock_player, _as_mgr(mock_manager))

    mock_manager.track_player_connected.assert_called_once_with(player_id, mock_player, "websocket")
    mock_cancel_grace.assert_called_once_with(player_id, mock_manager)
    mock_cancel_rest.assert_called_once_with(player_id, mock_manager)
    assert call_order == ["track", "cancel_grace"]


@pytest.mark.asyncio
async def test_track_player_presence_cancels_leftover_rest():
    """WS reconnect must cancel leftover /rest so the countdown cannot kill the new session."""
    player_id = uuid.uuid4()
    mock_player: MagicMock = MagicMock()
    mock_manager = _make_manager()
    leftover: asyncio.Task[None] = asyncio.create_task(asyncio.sleep(100))
    mock_manager.resting_players = {player_id: leftover}
    mock_cancel_grace: AsyncMock = AsyncMock()
    mock_cancel_rest: AsyncMock = AsyncMock()

    with (
        patch("server.realtime.connection_establishment.cancel_grace_period", mock_cancel_grace),
        patch("server.commands.rest_command.cancel_rest_countdown", mock_cancel_rest),
    ):
        await _track_player_presence(player_id, mock_player, _as_mgr(mock_manager))

    mock_cancel_rest.assert_called_once_with(player_id, mock_manager)
    _ = leftover.cancel()
    with pytest.raises(asyncio.CancelledError):
        await leftover


def test_cleanup_failed_connection_none():
    """Test _cleanup_failed_connection() handles None connection_id."""
    player_id = uuid.uuid4()
    mock_manager = _make_manager()

    _cleanup_failed_connection(None, player_id, _as_mgr(mock_manager))


def test_cleanup_failed_connection_success():
    """Test _cleanup_failed_connection() cleans up connection."""
    connection_id = "conn_123"
    player_id = uuid.uuid4()
    mock_manager = _make_manager()
    mock_manager.active_websockets = {connection_id: _as_ws(_FakeWebSocket())}
    mock_manager.connection_metadata = {connection_id: _meta(connection_id, player_id)}

    _cleanup_failed_connection(connection_id, player_id, _as_mgr(mock_manager))

    assert connection_id not in mock_manager.active_websockets
    assert connection_id not in mock_manager.connection_metadata


def test_cleanup_failed_connection_error():
    """Test _cleanup_failed_connection() handles errors during cleanup."""

    class _BrokenManager(_FakeEstablishmentManager):
        pass

    connection_id = "conn_123"
    player_id = uuid.uuid4()
    mock_manager = _BrokenManager()
    del mock_manager.connection_metadata

    _cleanup_failed_connection(connection_id, player_id, _as_mgr(mock_manager))
