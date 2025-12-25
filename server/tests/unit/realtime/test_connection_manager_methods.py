import uuid
from typing import cast

from fastapi import WebSocket

from server.realtime.connection_manager import ConnectionManager
from server.realtime.connection_manager_methods import (
    get_active_connection_count_impl,
    get_connection_count_impl,
    get_connection_id_from_websocket_impl,
    get_player_websocket_connection_id_impl,
    get_session_connections_impl,
    has_websocket_connection_impl,
    validate_session_impl,
)


def test_connection_id_lookup_and_counts() -> None:
    manager = ConnectionManager()
    player_id = uuid.uuid4()
    # Use cast to satisfy type checker - test uses object() as WebSocket mock
    websocket = cast(WebSocket, object())

    manager.active_websockets["conn-1"] = websocket
    manager.player_websockets[player_id] = ["conn-1"]

    assert get_connection_id_from_websocket_impl(manager, websocket) == "conn-1"
    assert get_active_connection_count_impl(manager) == 1
    assert has_websocket_connection_impl(manager, player_id) is True
    assert get_player_websocket_connection_id_impl(manager, player_id) == "conn-1"


def test_connection_session_validation() -> None:
    manager = ConnectionManager()
    player_id = uuid.uuid4()
    session_id = "session-123"

    manager.player_sessions[player_id] = session_id
    manager.session_connections[session_id] = ["conn-1", "conn-2"]

    assert validate_session_impl(manager, player_id, session_id) is True
    assert validate_session_impl(manager, player_id, "other-session") is False
    assert get_session_connections_impl(manager, session_id) == ["conn-1", "conn-2"]


def test_connection_counts_for_player_without_connections() -> None:
    manager = ConnectionManager()
    player_id = uuid.uuid4()

    assert has_websocket_connection_impl(manager, player_id) is False
    assert get_connection_count_impl(manager, player_id) == {"websocket": 0, "total": 0}
    assert get_player_websocket_connection_id_impl(manager, player_id) is None
