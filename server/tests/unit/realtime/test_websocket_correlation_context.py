"""
Unit tests for WebSocket correlation-context binding.

Covers the connection-level and per-message logging-context binding added in #754,
replacing the deleted (and non-functional) WebSocketCorrelationMiddleware.
"""

# pyright: reportMissingParameterType=false, reportUnknownParameterType=false, reportUnknownArgumentType=false, reportUnknownMemberType=false, reportUnusedFunction=false

import uuid
from unittest.mock import AsyncMock, patch

import pytest

from server.realtime.websocket_handler import handle_websocket_connection
from server.realtime.websocket_handler_message_loop import handle_websocket_message_loop
from server.structured_logging.logging_context import clear_request_context, get_current_context

TEST_PLAYER_ID = uuid.UUID("12345678-1234-5678-1234-567812345678")
TEST_PLAYER_ID_STR = str(TEST_PLAYER_ID)


@pytest.fixture(autouse=True)
def _clear_context_around_test():
    """Prevent bleed between tests sharing the same contextvars-backed process."""
    clear_request_context()
    yield
    clear_request_context()


@pytest.mark.asyncio
async def test_connection_binds_context_fields_before_message_loop(mock_websocket, mock_ws_connection_manager):
    """handle_websocket_connection binds player_id/session_id/connection_id/connection_type."""
    mock_ws_connection_manager.connect_websocket = AsyncMock(return_value=True)
    mock_ws_connection_manager.get_connection_id_from_websocket.return_value = "conn_001"

    captured_context: dict[str, object] = {}

    async def capture_and_exit(*_args: object, **_kwargs: object) -> None:
        captured_context.update(get_current_context())

    with (
        patch(
            "server.realtime.websocket_helpers.check_shutdown_and_reject", new_callable=AsyncMock, return_value=False
        ),
        patch("server.commands.admin_shutdown_command.is_shutdown_pending", return_value=False),
        patch("server.realtime.websocket_helpers.load_player_mute_data", new_callable=AsyncMock),
        patch(
            "server.realtime.websocket_initial_state.send_initial_game_state",
            new_callable=AsyncMock,
            return_value=(None, False),
        ),
        patch(
            "server.realtime.websocket_handler._handle_websocket_message_loop",
            new_callable=AsyncMock,
            side_effect=capture_and_exit,
        ),
        patch("server.realtime.websocket_handler._cleanup_connection", new_callable=AsyncMock),
    ):
        await handle_websocket_connection(mock_websocket, TEST_PLAYER_ID, "session_001", mock_ws_connection_manager)

    assert captured_context.get("player_id") == TEST_PLAYER_ID_STR
    assert captured_context.get("session_id") == "session_001"
    assert captured_context.get("connection_id") == "conn_001"
    assert captured_context.get("connection_type") == "websocket"
    # Cleared once the connection handler returns.
    assert not get_current_context()


@pytest.mark.asyncio
async def test_message_loop_assigns_fresh_correlation_id_per_message(mock_websocket, mock_ws_connection_manager):
    """Each inbound message gets its own server-generated correlation_id."""
    mock_websocket.receive_text = AsyncMock(side_effect=["{}", "{}", RuntimeError("stop the loop")])
    seen_ids: list[object] = []

    async def capture_id(*_args: object, **_kwargs: object) -> bool:
        seen_ids.append(get_current_context().get("correlation_id"))
        return True

    with (
        patch(
            "server.realtime.websocket_handler._process_message",
            new_callable=AsyncMock,
            side_effect=capture_id,
        ),
        patch(
            "server.realtime.websocket_handler._process_exception_in_message_loop",
            new_callable=AsyncMock,
            return_value=(True, False),
        ),
    ):
        await handle_websocket_message_loop(
            mock_websocket, TEST_PLAYER_ID, TEST_PLAYER_ID_STR, mock_ws_connection_manager
        )

    assert len(seen_ids) == 2
    assert all(seen_ids)
    assert seen_ids[0] != seen_ids[1]


@pytest.mark.asyncio
async def test_message_loop_ignores_client_supplied_correlation_id(mock_websocket, mock_ws_connection_manager):
    """A correlation_id sent by the client in the message body must not reach the log context."""
    mock_websocket.receive_text = AsyncMock(
        side_effect=['{"correlation_id": "client-injected"}', RuntimeError("stop the loop")]
    )
    seen_ids: list[object] = []

    async def capture_id(*_args: object, **_kwargs: object) -> bool:
        seen_ids.append(get_current_context().get("correlation_id"))
        return True

    with (
        patch(
            "server.realtime.websocket_handler._process_message",
            new_callable=AsyncMock,
            side_effect=capture_id,
        ),
        patch(
            "server.realtime.websocket_handler._process_exception_in_message_loop",
            new_callable=AsyncMock,
            return_value=(True, False),
        ),
    ):
        await handle_websocket_message_loop(
            mock_websocket, TEST_PLAYER_ID, TEST_PLAYER_ID_STR, mock_ws_connection_manager
        )

    assert len(seen_ids) == 1
    assert seen_ids[0] != "client-injected"
