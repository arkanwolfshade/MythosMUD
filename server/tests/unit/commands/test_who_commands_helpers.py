"""
Unit tests for who command helper functions.

Tests the helper functions in who_commands.py.
"""

from unittest.mock import MagicMock

from server.commands.who_commands import (
    filter_players_by_name,
    format_player_entry,
    format_player_location,
)


def test_filter_players_by_name_found():
    """Test filter_players_by_name() filters players by name."""
    alice = MagicMock()
    alice.name = "Alice"
    bob = MagicMock()
    bob.name = "Bob"
    charlie = MagicMock()
    charlie.name = "Charlie"
    players = [alice, bob, charlie]
    result = filter_players_by_name(players, "al")
    assert len(result) == 1
    assert result[0].name == "Alice"


def test_filter_players_by_name_not_found():
    """Test filter_players_by_name() returns empty list when no matches."""
    players = [MagicMock(name="Alice"), MagicMock(name="Bob")]
    result = filter_players_by_name(players, "z")
    assert result == []


def test_filter_players_by_name_empty_filter():
    """Test filter_players_by_name() returns all players when filter is empty."""
    players = [MagicMock(name="Alice"), MagicMock(name="Bob")]
    result = filter_players_by_name(players, "")
    assert len(result) == 2


def test_format_player_location_valid():
    """Test format_player_location() formats valid room ID."""
    room_id = "earth_arkhamcity_northside_intersection_derby_high"
    result = format_player_location(room_id)
    assert "Arkhamcity" in result
    assert "Northside" in result


def test_format_player_location_invalid():
    """Test format_player_location() handles invalid room ID."""
    result = format_player_location("")
    assert result == "Unknown Location"


def test_format_player_entry():
    """Test format_player_entry() formats player entry."""
    player = MagicMock()
    player.name = "TestPlayer"
    player.level = 5
    player.current_room_id = "earth_arkhamcity_northside_intersection_derby_high"
    player.is_admin = False
    result = format_player_entry(player)
    assert "TestPlayer" in result
    assert "[5]" in result


def test_format_player_entry_admin():
    """Test format_player_entry() includes admin indicator."""
    player = MagicMock()
    player.name = "AdminPlayer"
    player.level = 10
    player.current_room_id = "earth_arkhamcity_northside_intersection_derby_high"
    player.is_admin = True
    result = format_player_entry(player)
    assert "AdminPlayer" in result
    assert "[ADMIN]" in result
