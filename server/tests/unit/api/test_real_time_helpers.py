"""Unit tests for real_time API helper functions."""

# pyright: reportPrivateUsage=false
# Reason: Unit tests intentionally exercise real_time private helpers.

import json
import uuid
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from server.api import real_time
from server.exceptions import LoggedHTTPException
from server.schemas.realtime.presence_data import ErrorStatistics, PresenceStatistics, SessionStatistics


def _request_with_connection_manager(connection_manager: MagicMock | None) -> MagicMock:
    container: MagicMock = MagicMock()
    container.connection_manager = connection_manager
    app_state: MagicMock = MagicMock()
    app_state.container = container
    app: MagicMock = MagicMock()
    app.state = app_state
    request: MagicMock = MagicMock()
    request.app = app
    return request


def _websocket_with_app(connection_manager: MagicMock) -> MagicMock:
    container: MagicMock = MagicMock()
    container.connection_manager = connection_manager
    app_state: MagicMock = MagicMock()
    app_state.container = container
    app: MagicMock = MagicMock()
    app.state = app_state
    websocket: MagicMock = MagicMock()
    websocket.app = app
    return websocket


def test_websocket_player_id_fallback_allowed_default_off(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.delenv("MYTHOSMUD_ALLOW_WEBSOCKET_PLAYER_ID_FALLBACK", raising=False)
    assert real_time.websocket_player_id_fallback_allowed() is False


def test_extract_bearer_token_last_part() -> None:
    assert real_time._extract_bearer_token(["token-only"]) == "token-only"


def test_extract_bearer_token_empty() -> None:
    assert real_time._extract_bearer_token([]) is None


def test_parse_subprotocol_token() -> None:
    assert real_time._parse_subprotocol_token("bearer, secret-token") == "secret-token"


def test_resolve_connection_manager_from_state() -> None:
    cm = MagicMock()
    state = MagicMock()
    state.container = MagicMock(connection_manager=cm)
    with patch("server.api.real_time.resolve_connection_manager", return_value=cm):
        assert real_time._resolve_connection_manager_from_state(state) is cm


def test_resolve_connection_manager_returns_candidate() -> None:
    cm = MagicMock()
    assert real_time.resolve_connection_manager(cm) is cm


def test_resolve_connection_manager_delegates_when_none() -> None:
    sentinel = MagicMock()
    resolve_connection_manager: MagicMock = MagicMock(return_value=sentinel)
    fake = MagicMock()
    fake.resolve_connection_manager = resolve_connection_manager
    with patch("server.api.real_time.importlib.import_module", return_value=fake) as mocked:
        assert real_time.resolve_connection_manager(None) is sentinel
        mocked.assert_called_once_with("server.realtime.connection_manager_utils")


def test_ensure_connection_manager_missing() -> None:
    request = _request_with_connection_manager(None)
    with patch("server.api.real_time.resolve_connection_manager", return_value=None):
        with pytest.raises(LoggedHTTPException):
            _ = real_time._ensure_connection_manager(request)


@pytest.mark.asyncio
async def test_validate_and_accept_websocket_valid() -> None:
    accept: MagicMock = MagicMock()
    websocket: MagicMock = MagicMock()
    websocket.accept = accept
    cm = MagicMock(async_persistence=MagicMock())
    assert await real_time._validate_and_accept_websocket(websocket, cm) is True
    accept.assert_not_called()


@pytest.mark.asyncio
async def test_validate_and_accept_websocket_unavailable() -> None:
    accept: AsyncMock = AsyncMock()
    websocket: MagicMock = MagicMock()
    websocket.accept = accept
    websocket.send_json = AsyncMock()
    websocket.close = AsyncMock()
    assert await real_time._validate_and_accept_websocket(websocket, None) is False
    accept.assert_awaited_once()


@pytest.mark.asyncio
async def test_resolve_player_id_from_test() -> None:
    player_id = uuid.uuid4()
    player = MagicMock(player_id=player_id)
    persistence = MagicMock()
    persistence.get_player_by_id = AsyncMock(return_value=player)
    with patch("server.container.async_persistence_access.get_container_async_persistence", return_value=persistence):
        resolved = await real_time._resolve_player_id_from_test(MagicMock(), str(player_id), MagicMock())
    assert resolved == player_id


@pytest.mark.asyncio
async def test_resolve_player_id_from_token_no_player() -> None:
    persistence = MagicMock()
    persistence.get_player_by_user_id = AsyncMock(return_value=None)
    with patch("server.container.async_persistence_access.get_container_async_persistence", return_value=persistence):
        with pytest.raises(LoggedHTTPException):
            _ = await real_time._resolve_player_id_from_token(MagicMock(), {"sub": "user-1"})


@pytest.mark.asyncio
async def test_get_player_connections() -> None:
    player_id = uuid.uuid4()
    request = MagicMock()
    cm = MagicMock()
    get_player_presence_info: MagicMock = MagicMock(return_value={"is_online": True, "connection_count": 1})
    get_player_session: MagicMock = MagicMock(return_value="session-1")
    get_session_connections: MagicMock = MagicMock(return_value=["conn-1"])
    validate_session: MagicMock = MagicMock(return_value=True)
    cm.get_player_presence_info = get_player_presence_info
    cm.get_player_session = get_player_session
    cm.get_session_connections = get_session_connections
    cm.check_connection_health = AsyncMock(return_value={"is_healthy": True})
    cm.validate_session = validate_session
    with patch("server.api.real_time._ensure_connection_manager", return_value=cm):
        response = await real_time.get_player_connections(player_id, request)
    assert response.player_id == str(player_id)


def test_parse_websocket_token_from_query() -> None:
    websocket = MagicMock()
    websocket.query_params = {"token": "query-token"}
    websocket.headers = {}
    assert real_time._parse_websocket_token(websocket, MagicMock()) == "query-token"


def test_parse_websocket_token_from_subprotocol() -> None:
    websocket = MagicMock()
    websocket.query_params = {}
    websocket.headers = {"sec-websocket-protocol": "bearer, subproto-token"}
    assert real_time._parse_websocket_token(websocket, MagicMock()) == "subproto-token"


@pytest.mark.asyncio
async def test_resolve_player_id_missing_token_and_player_id() -> None:
    websocket = MagicMock()
    websocket.query_params = {}
    with pytest.raises(LoggedHTTPException):
        _ = await real_time._resolve_player_id(websocket, None, MagicMock())


@pytest.mark.asyncio
async def test_resolve_player_id_query_rejected_when_fallback_off(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("MYTHOSMUD_ALLOW_WEBSOCKET_PLAYER_ID_FALLBACK", "")
    player_id = uuid.uuid4()
    websocket = MagicMock()
    websocket.query_params = {"player_id": str(player_id)}
    with pytest.raises(LoggedHTTPException) as exc:
        _ = await real_time._resolve_player_id(websocket, None, MagicMock())
    assert exc.value.status_code == 401


@pytest.mark.asyncio
async def test_resolve_player_id_query_allowed_when_fallback_on(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("MYTHOSMUD_ALLOW_WEBSOCKET_PLAYER_ID_FALLBACK", "true")
    player_id = uuid.uuid4()
    player = MagicMock(player_id=player_id)
    persistence = MagicMock()
    persistence.get_player_by_id = AsyncMock(return_value=player)
    websocket = MagicMock()
    websocket.query_params = {"player_id": str(player_id)}
    with (
        patch("server.api.real_time.decode_access_token", return_value=None),
        patch("server.container.async_persistence_access.get_container_async_persistence", return_value=persistence),
    ):
        resolved = await real_time._resolve_player_id(websocket, None, MagicMock())
    assert resolved == player_id


@pytest.mark.asyncio
async def test_get_connection_statistics() -> None:
    request = MagicMock()
    cm = MagicMock()
    get_presence_statistics: MagicMock = MagicMock(return_value=PresenceStatistics(total_online=1))
    get_session_stats: MagicMock = MagicMock(return_value=SessionStatistics(active_sessions=1))
    get_error_statistics: MagicMock = MagicMock(return_value=ErrorStatistics(total_errors=0))
    cm.get_presence_statistics = get_presence_statistics
    cm.get_session_stats = get_session_stats
    cm.get_error_statistics = get_error_statistics
    with patch("server.api.real_time._ensure_connection_manager", return_value=cm):
        stats = await real_time.get_connection_statistics(request)
    assert stats.presence.total_online == 1


@pytest.mark.asyncio
async def test_handle_new_game_session() -> None:
    player_id = uuid.uuid4()
    request = MagicMock()
    request.json = AsyncMock(return_value={"session_id": "s1"})
    cm = MagicMock()
    cm.handle_new_game_session = AsyncMock(return_value={"success": True, "session_id": "s1"})
    with patch("server.api.real_time._ensure_connection_manager", return_value=cm):
        result = await real_time.handle_new_game_session(player_id, request)
    assert result.session_id == "s1"


@pytest.mark.asyncio
async def test_validate_websocket_connection_manager() -> None:
    cm = MagicMock(async_persistence=MagicMock())
    websocket = _websocket_with_app(cm)
    with patch("server.api.real_time.resolve_connection_manager", return_value=cm):
        assert await real_time._validate_websocket_connection_manager(websocket) is cm


@pytest.mark.asyncio
async def test_handle_new_game_session_missing_session_id() -> None:
    player_id = uuid.uuid4()
    request = MagicMock()
    request.json = AsyncMock(return_value={})
    cm = MagicMock()
    with patch("server.api.real_time._ensure_connection_manager", return_value=cm):
        with pytest.raises(LoggedHTTPException):
            _ = await real_time.handle_new_game_session(player_id, request)


@pytest.mark.asyncio
async def test_resolve_player_id_from_token_with_character_id() -> None:
    player_id = uuid.uuid4()
    user_id = str(uuid.uuid4())
    player = MagicMock(player_id=player_id, user_id=user_id, is_deleted=False)
    persistence = MagicMock()
    persistence.get_player_by_id = AsyncMock(return_value=player)
    websocket = MagicMock()
    websocket.query_params = {"character_id": str(player_id)}
    with patch("server.container.async_persistence_access.get_container_async_persistence", return_value=persistence):
        resolved = await real_time._resolve_player_id_from_token(websocket, {"sub": user_id})
    assert resolved == player_id


@pytest.mark.asyncio
async def test_handle_new_game_session_invalid_json() -> None:
    player_id = uuid.uuid4()
    request = MagicMock()
    request.json = AsyncMock(side_effect=json.JSONDecodeError("bad", "doc", 0))
    cm = MagicMock()
    with patch("server.api.real_time._ensure_connection_manager", return_value=cm):
        with pytest.raises(LoggedHTTPException):
            _ = await real_time.handle_new_game_session(player_id, request)


@pytest.mark.asyncio
async def test_resolve_player_id_from_path_or_token_uuid_without_jwt_rejected() -> None:
    player_id = uuid.uuid4()
    resolved = await real_time._resolve_player_id_from_path_or_token(str(player_id), None)
    assert resolved is None


@pytest.mark.asyncio
async def test_resolve_player_id_from_path_or_token_uuid_jwt_mismatch_rejected() -> None:
    path_id = uuid.uuid4()
    token_player = uuid.uuid4()
    user_id = str(uuid.uuid4())
    persistence = MagicMock()
    persistence.get_player_by_user_id = AsyncMock(return_value=MagicMock(player_id=token_player))
    with patch("server.api.real_time.decode_access_token", return_value={"sub": user_id}):
        resolved = await real_time._resolve_player_id_from_path_or_token(str(path_id), "token", persistence)
    assert resolved is None


@pytest.mark.asyncio
async def test_resolve_player_id_from_path_or_token_uuid_jwt_match() -> None:
    player_id = uuid.uuid4()
    user_id = str(uuid.uuid4())
    persistence = MagicMock()
    persistence.get_player_by_user_id = AsyncMock(return_value=MagicMock(player_id=player_id))
    with patch("server.api.real_time.decode_access_token", return_value={"sub": user_id}):
        resolved = await real_time._resolve_player_id_from_path_or_token(str(player_id), "token", persistence)
    assert resolved == player_id


@pytest.mark.asyncio
async def test_resolve_player_id_from_path_or_token_via_token() -> None:
    player_id = uuid.uuid4()
    user_id = str(uuid.uuid4())
    persistence = MagicMock()
    persistence.get_player_by_user_id = AsyncMock(return_value=MagicMock(player_id=player_id))
    with patch("server.api.real_time.decode_access_token", return_value={"sub": user_id}):
        resolved = await real_time._resolve_player_id_from_path_or_token("not-a-uuid", "token", persistence)
    assert resolved == player_id


@pytest.mark.asyncio
async def test_websocket_endpoint_route_unresolved_player() -> None:
    websocket = MagicMock()
    websocket.query_params = {}
    cm = MagicMock(async_persistence=MagicMock())
    with (
        patch("server.api.real_time._validate_websocket_connection_manager", new_callable=AsyncMock, return_value=cm),
        patch("server.api.real_time._resolve_player_id_from_path_or_token", new_callable=AsyncMock, return_value=None),
        patch("server.realtime.websocket_handler.handle_websocket_connection", new_callable=AsyncMock),
    ):
        with pytest.raises(LoggedHTTPException):
            await real_time.websocket_endpoint_route(websocket, "bad-id")


@pytest.mark.asyncio
async def test_parse_websocket_token_header_parse_error() -> None:
    websocket = MagicMock()
    websocket.query_params = {}
    get_header: MagicMock = MagicMock(side_effect=AttributeError("no header"))
    headers: MagicMock = MagicMock()
    headers.get = get_header
    websocket.headers = headers
    assert real_time._parse_websocket_token(websocket, MagicMock()) is None
