"""
Unit tests for establish_websocket_connection.

Split from test_connection_establishment.py to stay under lizard file-nloc.
"""

# pyright: reportPrivateUsage=false
# Reason: reuses private fakes from test_connection_establishment.

from __future__ import annotations

import asyncio
import uuid
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from server.exceptions import DatabaseError
from server.realtime.connection_establishment import establish_websocket_connection
from server.tests.unit.realtime.test_connection_establishment import (
    _as_mgr,
    _as_ws,
    _FakeWebSocket,
    _make_manager,
    _meta,
)


def _player_with_room() -> MagicMock:
    mock_player: MagicMock = MagicMock()
    mock_player.current_room_id = "room_123"
    return mock_player


@pytest.mark.asyncio
async def test_establish_websocket_connection_success():
    """Test establish_websocket_connection() successfully establishes connection."""
    mock_websocket = _FakeWebSocket()
    player_id = uuid.uuid4()
    session_id = "session_123"
    token = "jwt_token"
    mock_manager = _make_manager()
    mock_manager.get_player = AsyncMock(return_value=_player_with_room())

    success, connection_id = await establish_websocket_connection(
        _as_ws(mock_websocket), player_id, _as_mgr(mock_manager), session_id, token
    )

    assert success is True
    assert connection_id is not None
    assert mock_websocket.accept_calls == 1
    assert connection_id in mock_manager.active_websockets
    assert mock_manager.performance_tracker.establish_calls == 1


@pytest.mark.asyncio
async def test_establish_websocket_connection_player_not_found():
    """Test establish_websocket_connection() returns False when player not found."""
    mock_websocket = _FakeWebSocket()
    player_id = uuid.uuid4()
    mock_manager = _make_manager()
    mock_manager.get_player = AsyncMock(return_value=None)

    success, connection_id = await establish_websocket_connection(
        _as_ws(mock_websocket), player_id, _as_mgr(mock_manager)
    )

    assert success is False
    assert connection_id is not None


@pytest.mark.asyncio
async def test_establish_websocket_connection_error():
    """Test establish_websocket_connection() handles errors."""
    mock_websocket = _FakeWebSocket()
    mock_websocket.accept_error = DatabaseError("Database error")
    player_id = uuid.uuid4()
    mock_manager = _make_manager()
    mock_manager.async_persistence = None

    success, connection_id = await establish_websocket_connection(
        _as_ws(mock_websocket), player_id, _as_mgr(mock_manager)
    )

    assert success is False
    assert connection_id is None or connection_id not in mock_manager.active_websockets


@pytest.mark.asyncio
async def test_establish_websocket_connection_cleans_dead_connections():
    """Test establish_websocket_connection() cleans up dead connections."""
    mock_websocket = _FakeWebSocket()
    player_id = uuid.uuid4()
    dead_conn = "dead_conn"
    mock_manager = _make_manager()
    mock_manager.player_websockets = {player_id: [dead_conn]}
    mock_manager.active_websockets = {dead_conn: _as_ws(_FakeWebSocket("DISCONNECTED"))}
    mock_manager.get_player = AsyncMock(return_value=_player_with_room())

    success, _connection_id = await establish_websocket_connection(
        _as_ws(mock_websocket), player_id, _as_mgr(mock_manager)
    )

    assert success is True
    assert dead_conn not in mock_manager.active_websockets


@pytest.mark.asyncio
async def test_establish_websocket_connection_cancels_rest_countdown():
    """Reconnect cancels an in-progress rest countdown so it cannot poison the new session."""
    mock_websocket = _FakeWebSocket()
    player_id = uuid.uuid4()
    mock_manager = _make_manager()
    mock_manager.get_player = AsyncMock(return_value=_player_with_room())
    rest_task: asyncio.Task[None] = asyncio.create_task(asyncio.sleep(100))
    mock_manager.resting_players = {player_id: rest_task}

    success, _connection_id = await establish_websocket_connection(
        _as_ws(mock_websocket), player_id, _as_mgr(mock_manager)
    )

    assert success is True
    assert player_id not in mock_manager.resting_players
    assert rest_task.cancelled() or rest_task.done()


@pytest.mark.asyncio
async def test_establish_websocket_connection_new_session_disconnects_prior():
    """New session_id closes prior sockets before append-register (#610)."""
    mock_websocket = _FakeWebSocket()
    player_id = uuid.uuid4()
    old_conn = "old_conn"
    mock_manager = _make_manager()
    mock_manager.get_player = AsyncMock(return_value=_player_with_room())
    old_ws = _FakeWebSocket("CONNECTED")
    mock_manager.player_websockets = {player_id: [old_conn]}
    mock_manager.active_websockets = {old_conn: _as_ws(old_ws)}
    mock_manager.connection_metadata = {old_conn: _meta(old_conn, player_id)}
    mock_manager.player_sessions = {player_id: "old_session"}
    mock_manager.session_connections = {"old_session": [old_conn]}

    success, connection_id = await establish_websocket_connection(
        _as_ws(mock_websocket), player_id, _as_mgr(mock_manager), "new_session", "jwt"
    )

    assert success is True
    assert connection_id is not None
    assert old_ws.close_calls == 1
    assert old_conn not in mock_manager.active_websockets
    assert mock_manager.player_websockets[player_id] == [connection_id]
    assert mock_websocket.accept_calls == 1


@pytest.mark.asyncio
async def test_establish_websocket_connection_stale_session_does_not_replace():
    """A leaked session with no live sockets must not trigger the replacement path.

    Session tracking used to outlive every connection, so the next login for that player
    looked like a session change and tore down the socket it was still establishing,
    leaving the client permanently linkdead until the server restarted.
    """
    mock_websocket = _FakeWebSocket()
    player_id = uuid.uuid4()
    mock_manager = _make_manager()
    mock_manager.get_player = AsyncMock(return_value=_player_with_room())
    mock_manager.player_sessions = {player_id: "stale_session"}
    mock_manager.session_connections = {"stale_session": ["conn_from_dead_run"]}

    with patch(
        "server.realtime.connection_establishment.handle_new_game_session_impl",
        new_callable=AsyncMock,
    ) as new_session:
        success, connection_id = await establish_websocket_connection(
            _as_ws(mock_websocket), player_id, _as_mgr(mock_manager), "fresh_session", "jwt"
        )

    new_session.assert_not_awaited()
    assert success is True
    assert connection_id is not None
    assert connection_id in mock_manager.active_websockets
    assert mock_manager.player_websockets[player_id] == [connection_id]
    assert mock_manager.player_sessions[player_id] == "fresh_session"


@pytest.mark.asyncio
async def test_establish_websocket_connection_same_session_appends():
    """Same session_id appends; does not kill a healthy prior socket (#610)."""
    mock_websocket = _FakeWebSocket()
    player_id = uuid.uuid4()
    existing_conn = "existing_conn"
    mock_manager = _make_manager()
    mock_manager.get_player = AsyncMock(return_value=_player_with_room())
    existing_ws = _FakeWebSocket("CONNECTED")
    mock_manager.player_websockets = {player_id: [existing_conn]}
    mock_manager.active_websockets = {existing_conn: _as_ws(existing_ws)}
    mock_manager.connection_metadata = {existing_conn: _meta(existing_conn, player_id)}
    mock_manager.player_sessions = {player_id: "same_session"}
    mock_manager.session_connections = {"same_session": [existing_conn]}

    success, connection_id = await establish_websocket_connection(
        _as_ws(mock_websocket), player_id, _as_mgr(mock_manager), "same_session", "jwt"
    )

    assert success is True
    assert connection_id is not None
    assert existing_ws.close_calls == 0
    assert existing_conn in mock_manager.player_websockets[player_id]
    assert connection_id in mock_manager.player_websockets[player_id]
    assert len(mock_manager.player_websockets[player_id]) == 2


@pytest.mark.asyncio
async def test_establish_websocket_connection_first_session_does_not_replace():
    """No player_sessions entry: first session_id appends; does not close leftover sockets (#610)."""
    mock_websocket = _FakeWebSocket()
    player_id = uuid.uuid4()
    leftover_conn = "leftover_conn"
    mock_manager = _make_manager()
    mock_manager.get_player = AsyncMock(return_value=_player_with_room())
    leftover_ws = _FakeWebSocket("CONNECTED")
    mock_manager.player_websockets = {player_id: [leftover_conn]}
    mock_manager.active_websockets = {leftover_conn: _as_ws(leftover_ws)}
    mock_manager.connection_metadata = {leftover_conn: _meta(leftover_conn, player_id)}

    success, connection_id = await establish_websocket_connection(
        _as_ws(mock_websocket), player_id, _as_mgr(mock_manager), "first_session", "jwt"
    )

    assert success is True
    assert connection_id is not None
    assert leftover_ws.close_calls == 0
    assert leftover_conn in mock_manager.player_websockets[player_id]
    assert connection_id in mock_manager.player_websockets[player_id]


@pytest.mark.asyncio
async def test_establish_websocket_connection_missing_session_id_does_not_replace():
    """Absent session_id is grace/recover: append only, do not run new_game_session (#610)."""
    mock_websocket = _FakeWebSocket()
    player_id = uuid.uuid4()
    existing_conn = "existing_conn"
    mock_manager = _make_manager()
    mock_manager.get_player = AsyncMock(return_value=_player_with_room())
    existing_ws = _FakeWebSocket("CONNECTED")
    mock_manager.player_websockets = {player_id: [existing_conn]}
    mock_manager.active_websockets = {existing_conn: _as_ws(existing_ws)}
    mock_manager.connection_metadata = {existing_conn: _meta(existing_conn, player_id)}
    mock_manager.player_sessions = {player_id: "tracked_session"}
    mock_manager.session_connections = {"tracked_session": [existing_conn]}

    success, connection_id = await establish_websocket_connection(
        _as_ws(mock_websocket), player_id, _as_mgr(mock_manager), None, "jwt"
    )

    assert success is True
    assert connection_id is not None
    assert existing_ws.close_calls == 0
    assert existing_conn in mock_manager.player_websockets[player_id]
    assert connection_id in mock_manager.player_websockets[player_id]
