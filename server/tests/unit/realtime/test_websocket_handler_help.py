"""
Unit tests for websocket handler help functions.

Tests the help content functions in websocket_handler.py.
"""

from server.realtime.websocket_handler import get_help_content


def test_get_help_content_general():
    """Test get_help_content() returns general help when no command specified."""
    result = get_help_content()
    assert isinstance(result, str)
    assert "Available Commands" in result or "Commands" in result


def test_get_help_content_specific():
    """Test get_help_content() returns specific command help."""
    result = get_help_content("look")
    assert isinstance(result, str)
    assert "look" in result.lower() or "not found" in result.lower()
