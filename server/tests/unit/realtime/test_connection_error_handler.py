"""Unit tests for ConnectionErrorHandler."""

import uuid
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from server.realtime.errors.error_handler import ConnectionErrorHandler


@pytest.fixture
def handler() -> ConnectionErrorHandler:
    player_id = uuid.uuid4()
    return ConnectionErrorHandler(
        force_disconnect_callback=AsyncMock(),
        disconnect_connection_callback=AsyncMock(return_value=True),
        cleanup_dead_connections_callback=AsyncMock(return_value={"connections_cleaned": 1}),
        get_player_session_callback=MagicMock(return_value="session-1"),
        get_session_connections_callback=MagicMock(return_value=["conn-1"]),
        get_player_websockets=MagicMock(return_value=["conn-1"]),
        get_online_players=MagicMock(return_value={player_id: {"name": "Armitage"}}),
        get_session_connections=MagicMock(return_value={"session-1": ["conn-1"]}),
        get_player_sessions=MagicMock(return_value={player_id: "session-1"}),
    )


@pytest.mark.asyncio
async def test_fatal_error_force_disconnect(handler: ConnectionErrorHandler) -> None:
    player_id = uuid.uuid4()
    with patch("server.realtime.errors.error_handler.get_config") as cfg:
        cfg.return_value.logging.log_base = "logs"
        cfg.return_value.logging.environment = "unit_test"
        with patch("server.realtime.errors.error_handler._resolve_log_base", return_value=MagicMock()):
            with patch("builtins.open", MagicMock()):
                result = await handler.detect_and_handle_error_state(player_id, "AUTHENTICATION_FAILURE", "bad token")
    assert result["fatal_error"] is True
    assert result["success"] is True
    handler.force_disconnect.assert_awaited_once_with(player_id)


@pytest.mark.asyncio
async def test_connection_specific_error(handler: ConnectionErrorHandler) -> None:
    player_id = uuid.uuid4()
    with patch("server.realtime.errors.error_handler.get_config") as cfg:
        cfg.return_value.logging.log_base = "logs"
        cfg.return_value.logging.environment = "unit_test"
        with patch("server.realtime.errors.error_handler._resolve_log_base", return_value=MagicMock()):
            with patch("builtins.open", MagicMock()):
                result = await handler.detect_and_handle_error_state(
                    player_id, "WEBSOCKET_ERROR", "frame error", connection_id="conn-1"
                )
    assert result["connections_terminated"] == 1
    handler.disconnect_connection.assert_awaited_once_with("conn-1")


@pytest.mark.asyncio
async def test_handle_websocket_critical_error(handler: ConnectionErrorHandler) -> None:
    player_id = uuid.uuid4()
    with patch.object(handler, "detect_and_handle_error_state", new_callable=AsyncMock) as detect:
        detect.return_value = {"success": True}
        await handler.handle_websocket_error(player_id, "conn-1", "PROTOCOL_ERROR", "bad frame")
    detect.assert_awaited_once()
    assert detect.await_args.args[1] == "CRITICAL_WEBSOCKET_ERROR"


@pytest.mark.asyncio
async def test_recover_from_error_full(handler: ConnectionErrorHandler) -> None:
    player_id = uuid.uuid4()
    sessions = {player_id: "session-1"}
    session_connections = {"session-1": ["conn-1"]}
    handler.get_player_sessions = MagicMock(return_value=sessions)
    handler.get_session_connections_dict = MagicMock(return_value=session_connections)
    result = await handler.recover_from_error(player_id, recovery_type="FULL")
    assert result["success"] is True
    assert result["connections_restored"] == 1
    assert result["sessions_cleared"] == 1


def test_get_error_statistics(handler: ConnectionErrorHandler) -> None:
    player_id = uuid.uuid4()
    with patch("server.realtime.errors.error_handler.get_config") as cfg:
        cfg.return_value.logging.log_base = "logs"
        cfg.return_value.logging.environment = "unit_test"
        with patch("server.realtime.errors.error_handler._resolve_log_base", return_value=MagicMock()):
            stats = handler.get_error_statistics({player_id: {}}, {player_id: ["conn-1"]})
    assert stats["total_players"] == 1
    assert stats["total_connections"] == 1


@pytest.mark.asyncio
async def test_non_fatal_error_keeps_connections(handler: ConnectionErrorHandler) -> None:
    player_id = uuid.uuid4()
    with patch("server.realtime.errors.error_handler.get_config") as cfg:
        cfg.return_value.logging.log_base = "logs"
        cfg.return_value.logging.environment = "unit_test"
        with patch("server.realtime.errors.error_handler._resolve_log_base", return_value=MagicMock()):
            with patch("builtins.open", MagicMock()):
                result = await handler.detect_and_handle_error_state(player_id, "MINOR_ERROR", "minor")
    assert result["fatal_error"] is False
    assert result["connections_terminated"] == 0


@pytest.mark.asyncio
async def test_disconnect_failure_records_error(handler: ConnectionErrorHandler) -> None:
    player_id = uuid.uuid4()
    handler.disconnect_connection = AsyncMock(return_value=False)
    with patch("server.realtime.errors.error_handler.get_config") as cfg:
        cfg.return_value.logging.log_base = "logs"
        cfg.return_value.logging.environment = "unit_test"
        with patch("server.realtime.errors.error_handler._resolve_log_base", return_value=MagicMock()):
            with patch("builtins.open", MagicMock()):
                result = await handler.detect_and_handle_error_state(
                    player_id, "WEBSOCKET_ERROR", "bad", connection_id="conn-x"
                )
    assert result["errors"]
    handler.disconnect_connection.assert_awaited_once_with("conn-x")


@pytest.mark.asyncio
async def test_handle_authentication_error(handler: ConnectionErrorHandler) -> None:
    player_id = uuid.uuid4()
    with patch.object(handler, "detect_and_handle_error_state", new_callable=AsyncMock) as detect:
        detect.return_value = {"success": True}
        await handler.handle_authentication_error(player_id, "TOKEN_EXPIRED", "expired")
    assert detect.await_args.args[1] == "AUTHENTICATION_FAILURE"


@pytest.mark.asyncio
async def test_handle_security_violation(handler: ConnectionErrorHandler) -> None:
    player_id = uuid.uuid4()
    with patch.object(handler, "detect_and_handle_error_state", new_callable=AsyncMock) as detect:
        detect.return_value = {"success": True}
        await handler.handle_security_violation(player_id, "INJECTION", "bad payload")
    assert detect.await_args.args[1] == "SECURITY_VIOLATION"


@pytest.mark.asyncio
async def test_recover_connections_only(handler: ConnectionErrorHandler) -> None:
    player_id = uuid.uuid4()
    result = await handler.recover_from_error(player_id, recovery_type="CONNECTIONS_ONLY")
    assert result["success"] is True
    assert result["sessions_cleared"] == 0
