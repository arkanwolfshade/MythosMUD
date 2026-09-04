"""
Unit tests for websocket handler helper functions.

Tests the helper functions in websocket_handler.py.
"""

from server.realtime.websocket_handler import _is_websocket_disconnected


def test_is_websocket_disconnected_true():
    """Test _is_websocket_disconnected() returns True for disconnection messages."""
    assert _is_websocket_disconnected("WebSocket is not connected") is True
    assert _is_websocket_disconnected('Need to call "accept" first') is True


def test_is_websocket_disconnected_false():
    """Test _is_websocket_disconnected() returns False for other messages."""
    assert _is_websocket_disconnected("Some other error") is False
    assert _is_websocket_disconnected("") is False
