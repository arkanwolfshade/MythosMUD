"""
Unit tests for position command helper functions.

Tests helper functions in position_commands.py module.
"""

from server.commands.position_commands import _format_room_posture_message


def test_format_room_posture_message_sitting():
    """Test _format_room_posture_message() formats sitting message."""
    result = _format_room_posture_message("TestPlayer", None, "sitting")
    assert "settles" in result.lower() or "seated" in result.lower()
    assert "TestPlayer" in result


def test_format_room_posture_message_lying():
    """Test _format_room_posture_message() formats lying message."""
    result = _format_room_posture_message("TestPlayer", None, "lying")
    assert "stretches" in result.lower() or "lies" in result.lower()
    assert "TestPlayer" in result


def test_format_room_posture_message_standing_from_lying():
    """Test _format_room_posture_message() formats standing from lying message."""
    result = _format_room_posture_message("TestPlayer", "lying", "standing")
    assert "pushes" in result.lower() or "stands" in result.lower()
    assert "TestPlayer" in result


def test_format_room_posture_message_standing_from_sitting():
    """Test _format_room_posture_message() formats standing from sitting message."""
    result = _format_room_posture_message("TestPlayer", "sitting", "standing")
    assert "rises" in result.lower() or "stands" in result.lower()
    assert "TestPlayer" in result


def test_format_room_posture_message_standing_no_previous():
    """Test _format_room_posture_message() formats standing with no previous position."""
    result = _format_room_posture_message("TestPlayer", None, "standing")
    assert "straightens" in result.lower() or "stands" in result.lower()
    assert "TestPlayer" in result


def test_format_room_posture_message_unknown():
    """Test _format_room_posture_message() handles unknown position."""
    result = _format_room_posture_message("TestPlayer", None, "unknown")
    assert "shifts" in result.lower() or "posture" in result.lower()
    assert "TestPlayer" in result
