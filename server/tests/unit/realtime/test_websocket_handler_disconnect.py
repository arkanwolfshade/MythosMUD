"""
Unit tests for websocket handler disconnect handling.

Tests the disconnect handling functions in websocket_handler.py.
"""

from pytest_mock import MockerFixture

from server.realtime.websocket_handler import _handle_websocket_disconnect


def test_handle_websocket_disconnect():
    """Test _handle_websocket_disconnect() returns True."""
    result = _handle_websocket_disconnect("player_001", "conn_001")
    assert result is True


def test_handle_websocket_disconnect_no_connection_id():
    """Test _handle_websocket_disconnect() with no connection_id."""
    result = _handle_websocket_disconnect("player_001", None)
    assert result is True


def test_handle_websocket_disconnect_logs_close_code_and_reason(mocker: MockerFixture):
    """The WebSocket close code/reason must reach the log, not be silently discarded.

    Regression: this info was previously dropped entirely, leaving no server-side way to tell a
    client-initiated close (1000) from a server rejection (1008/1011) or a raw network-level drop
    (1006) -- the exact question that blocked diagnosing the #297 e2e reconnect investigation.
    """
    mock_logger_info = mocker.patch("server.realtime.websocket_handler_message_loop.logger.info")

    result = _handle_websocket_disconnect("player_001", "conn_001", 1006, "abnormal closure")

    assert result is True
    mock_logger_info.assert_called_once_with(
        "WebSocket disconnected",
        player_id="player_001",
        connection_id="conn_001",
        code=1006,
        reason="abnormal closure",
    )
