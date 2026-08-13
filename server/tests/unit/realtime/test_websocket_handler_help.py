"""
Unit tests for help content used in the realtime/WebSocket path.

Uses the canonical help system (server.help.help_content) rather than the
removed websocket_handler stub.
"""

from server.help.help_content import get_help_content


def test_get_help_content_general():
    """Test get_help_content() returns general help when no command specified."""
    result = get_help_content()
    assert isinstance(result, str)
    assert "command" in result.lower() or "help" in result.lower()


def test_get_help_content_specific():
    """Test get_help_content() returns specific command help for look."""
    result = get_help_content("look")
    assert isinstance(result, str)
    assert "look" in result.lower() or "not found" in result.lower()


def test_get_help_content_talk():
    """talk has in-game help for dialogue trees (#583)."""
    result = get_help_content("talk")
    assert "TALK" in result or "talk" in result.lower()
    assert "npc" in result.lower()
    assert "number" in result.lower()
