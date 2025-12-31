"""
Unit tests for look_room helper functions.

Tests the helper functions in look_room.py module.
"""

from unittest.mock import MagicMock

from server.commands.look_room import (
    _filter_other_players,
    _format_exits_list,
    _format_items_section,
    _format_players_section,
    _get_room_description,
    _get_room_id,
)


def test_format_items_section():
    """Test _format_items_section() formats room drops."""
    room_drops = [
        {"item_name": "Sword", "quantity": 1},
        {"item_name": "Arrow", "quantity": 10},
    ]

    result = _format_items_section(room_drops)

    assert len(result) > 0
    assert any("Sword" in line for line in result)


def test_format_items_section_empty():
    """Test _format_items_section() returns message for empty drops."""
    room_drops = []

    result = _format_items_section(room_drops)

    # Function returns message when drops are empty
    assert len(result) > 0
    assert any("no abandoned curios" in line.lower() for line in result)


def test_filter_other_players():
    """Test _filter_other_players() filters out current player."""
    player1 = MagicMock()
    player1.name = "Player1"
    player2 = MagicMock()
    player2.name = "Player2"
    players_in_room = [player1, player2]

    result = _filter_other_players(players_in_room, "Player1")

    assert "Player2" in result
    assert "Player1" not in result


def test_filter_other_players_all_filtered():
    """Test _filter_other_players() returns empty list when only current player."""
    player1 = MagicMock()
    player1.name = "Player1"
    players_in_room = [player1]

    result = _filter_other_players(players_in_room, "Player1")

    assert result == []


def test_format_players_section():
    """Test _format_players_section() formats player names."""
    player_names = ["Player1", "Player2"]

    result = _format_players_section(player_names)

    assert len(result) == 2
    assert "Also here:" in result[0]
    assert "Player1" in result[0]
    assert "Player2" in result[0]
    assert result[1] == ""


def test_format_players_section_empty():
    """Test _format_players_section() returns empty list for no players."""
    player_names = []

    result = _format_players_section(player_names)

    assert result == []


def test_get_room_description():
    """Test _get_room_description() returns room description."""
    room = MagicMock()
    room.description = "A test room."

    result = _get_room_description(room)

    assert result == "A test room."


def test_get_room_description_fallback():
    """Test _get_room_description() returns fallback when description is None."""
    room = MagicMock()
    room.description = None

    result = _get_room_description(room)

    assert result == "You see nothing special."


def test_get_room_id():
    """Test _get_room_id() returns room ID."""
    room = MagicMock()
    room.id = "room_001"

    result = _get_room_id(room)

    assert result == "room_001"


def test_get_room_id_no_id():
    """Test _get_room_id() returns None when room has no id attribute."""
    room = MagicMock()
    del room.id

    result = _get_room_id(room)

    assert result is None


def test_format_exits_list():
    """Test _format_exits_list() formats exits dictionary."""
    exits = {
        "north": "room_002",
        "south": "room_003",
    }

    result = _format_exits_list(exits)

    assert "north" in result.lower()
    assert "south" in result.lower()


def test_format_exits_list_empty():
    """Test _format_exits_list() handles empty exits."""
    exits = {}

    result = _format_exits_list(exits)

    assert isinstance(result, str)
