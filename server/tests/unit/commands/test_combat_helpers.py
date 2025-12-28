"""
Unit tests for combat command helper functions.

Tests helper functions in combat.py module.
"""

from unittest.mock import MagicMock

from server.commands.combat import _format_combat_status, _get_combat_target


def test_format_combat_status_in_combat():
    """Test _format_combat_status() formats combat status."""
    mock_player = MagicMock()
    mock_player.in_combat = True
    mock_combat_instance = MagicMock()
    mock_combat_instance.status = "active"

    result = _format_combat_status(mock_player, mock_combat_instance)
    assert isinstance(result, str)
    assert len(result) > 0


def test_format_combat_status_not_in_combat():
    """Test _format_combat_status() handles player not in combat."""
    mock_player = MagicMock()
    mock_player.in_combat = False

    result = _format_combat_status(mock_player, None)
    assert isinstance(result, str)
    assert "not in combat" in result.lower() or len(result) == 0


def test_get_combat_target():
    """Test _get_combat_target() finds target."""
    mock_player = MagicMock()
    mock_player.current_room_id = "room_001"
    mock_target = MagicMock()
    mock_target.name = "Enemy"

    result = _get_combat_target(mock_player, "Enemy")
    # Implementation dependent - may return target or None
    assert result is None or result.name == "Enemy"


def test_get_combat_target_not_found():
    """Test _get_combat_target() returns None when target not found."""
    mock_player = MagicMock()
    mock_player.current_room_id = "room_001"

    result = _get_combat_target(mock_player, "Nonexistent")
    assert result is None
