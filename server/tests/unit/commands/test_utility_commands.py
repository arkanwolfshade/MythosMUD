"""
Tests for Utility Commands.

This module tests utility command handlers and helper functions including
player filtering, location formatting, and basic command handlers.

AI Agent: Tests for utility command functions covering player filtering,
         location formatting, and player entry formatting with various inputs.
"""


# pylint: disable=redefined-outer-name
# Justification: pytest fixtures redefine names

from typing import Any, cast
from unittest.mock import Mock

import pytest

from server.commands.utility_commands import (
    filter_players_by_name,
    format_player_entry,
    format_player_location,
)


@pytest.fixture
def mock_player():
    """Provide mock player for testing."""
    player = Mock()
    player.name = "TestPlayer"
    player.level = 5
    player.current_room_id = "earth_arkhamcity_northside_intersection_derby_high"
    player.is_admin = False
    return player


@pytest.fixture
def mock_admin_player():
    """Provide mock admin player for testing."""
    player = Mock()
    player.name = "AdminPlayer"
    player.level = 10
    player.current_room_id = "earth_arkhamcity_french_hill_miskatonic_university"
    player.is_admin = True
    return player


class TestFilterPlayersByName:
    """Test player name filtering."""

    def test_filter_with_empty_term_returns_all(self, mock_player):
        """Test filtering with empty term returns all players."""
        players = [mock_player]
        result = filter_players_by_name(players, "")

        assert result == players

    def test_filter_with_exact_match(self, mock_player):
        """Test filtering with exact name match."""
        players = [mock_player]
        result = filter_players_by_name(players, "TestPlayer")

        assert len(result) == 1
        assert result[0] == mock_player

    def test_filter_with_partial_match_case_insensitive(self, mock_player):
        """Test filtering with partial case-insensitive match."""
        players = [mock_player]
        result = filter_players_by_name(players, "test")

        assert len(result) == 1
        assert result[0] == mock_player

    def test_filter_with_uppercase_term(self, mock_player):
        """Test filtering with uppercase term matches lowercase."""
        players = [mock_player]
        result = filter_players_by_name(players, "TEST")

        assert len(result) == 1

    def test_filter_with_no_matches(self, mock_player):
        """Test filtering with no matches returns empty list."""
        players = [mock_player]
        result = filter_players_by_name(players, "NonExistent")

        assert result == []

    def test_filter_multiple_players(self, mock_player):
        """Test filtering multiple players."""
        player2 = Mock()
        player2.name = "AnotherPlayer"
        players = [mock_player, player2]

        result = filter_players_by_name(players, "Test")

        assert len(result) == 1
        assert result[0] == mock_player


class TestFormatPlayerLocation:
    """Test player location formatting."""

    def test_format_standard_room_id(self) -> None:
        """Test formatting standard hierarchical room ID."""
        room_id = "earth_arkhamcity_northside_intersection_derby_high"
        result = format_player_location(room_id)

        assert "Arkhamcity" in result
        assert "Northside" in result
        assert "Intersection Derby High" in result
        assert ":" in result

    def test_format_room_with_underscores_in_name(self) -> None:
        """Test formatting room ID with underscores in room name."""
        room_id = "earth_miskatonic_campus_library_forbidden_section"
        result = format_player_location(room_id)

        assert "Miskatonic" in result
        assert "Campus" in result
        assert "Library Forbidden Section" in result

    def test_format_short_room_id_fallback(self) -> None:
        """Test formatting short room ID uses fallback."""
        room_id = "earth_zone"
        result = format_player_location(room_id)

        # Should return formatted version of the ID
        assert "Earth Zone" in result

    def test_format_invalid_room_id_returns_unknown(self) -> None:
        """Test formatting invalid room ID returns Unknown Location."""
        result = format_player_location("")

        assert result == "Unknown Location"

    def test_format_none_room_id_returns_unknown(self) -> None:
        """Test formatting None room ID returns Unknown Location."""
        result = format_player_location(cast(Any, None))

        assert result == "Unknown Location"

    def test_format_non_string_room_id_returns_unknown(self) -> None:
        """Test formatting non-string room ID returns Unknown Location."""
        result = format_player_location(cast(Any, 12345))

        assert result == "Unknown Location"


class TestFormatPlayerEntry:
    """Test player entry formatting for who command."""

    def test_format_regular_player(self, mock_player):
        """Test formatting regular player entry."""
        result = format_player_entry(mock_player)

        assert "TestPlayer" in result
        assert "[5]" in result
        assert "Arkhamcity" in result
        assert "[ADMIN]" not in result

    def test_format_admin_player(self, mock_admin_player):
        """Test formatting admin player entry includes [ADMIN] tag."""
        result = format_player_entry(mock_admin_player)

        assert "AdminPlayer" in result
        assert "[10]" in result
        assert "[ADMIN]" in result

    def test_format_player_with_error_uses_fallback(self) -> None:
        """Test formatting player with error uses fallback formatting."""
        player = Mock()
        player.name = "ErrorPlayer"
        player.level = 3
        player.is_admin = False
        player.current_room_id = None  # Will cause error in format_player_location

        result = format_player_entry(player)

        assert "ErrorPlayer" in result
        assert "[3]" in result
        assert "Unknown" in result

    def test_format_player_entry_includes_level(self, mock_player):
        """Test player entry includes level in brackets."""
        mock_player.level = 99

        result = format_player_entry(mock_player)

        assert "[99]" in result
