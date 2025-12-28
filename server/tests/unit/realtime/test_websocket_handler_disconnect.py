"""
Unit tests for websocket handler disconnect handling.

Tests the disconnect handling functions in websocket_handler.py.
"""

from server.realtime.websocket_handler import _handle_websocket_disconnect


def test_handle_websocket_disconnect():
    """Test _handle_websocket_disconnect() returns True."""
    result = _handle_websocket_disconnect("player_001", "conn_001")
    assert result is True


def test_handle_websocket_disconnect_no_connection_id():
    """Test _handle_websocket_disconnect() with no connection_id."""
    result = _handle_websocket_disconnect("player_001", None)
    assert result is True
