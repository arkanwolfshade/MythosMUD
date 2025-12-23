"""
Tests for who command handler.

This module tests the who command handler and related helper functions.
"""


# pylint: disable=redefined-outer-name
# Justification: pytest fixtures redefine names

from datetime import UTC, datetime, timedelta
from unittest.mock import AsyncMock, MagicMock, Mock, patch

import pytest

from server.commands.who_commands import (
    filter_online_players,
    filter_players_by_name,
    format_player_entry,
    format_player_location,
    format_who_result,
    get_players_for_who,
    handle_who_command,
    parse_last_active_datetime,
)


class TestFilterPlayersByName:
    """Test filter_players_by_name function."""

    def test_filter_players_by_name_exact_match(self):
        """Test filtering players with exact name match."""
        alice = Mock()
        alice.name = "Alice"
        bob = Mock()
        bob.name = "Bob"
        charlie = Mock()
        charlie.name = "Charlie"
        players = [alice, bob, charlie]
        result = filter_players_by_name(players, "Bob")

        assert len(result) == 1
        assert result[0].name == "Bob"

    def test_filter_players_by_name_partial_match(self):
        """Test filtering players with partial name match."""
        alice = Mock()
        alice.name = "Alice"
        bob = Mock()
        bob.name = "Bob"
        charlie = Mock()
        charlie.name = "Charlie"
        players = [alice, bob, charlie]
        result = filter_players_by_name(players, "ch")

        assert len(result) == 1
        assert result[0].name == "Charlie"

    def test_filter_players_by_name_case_insensitive(self):
        """Test filtering players is case-insensitive."""
        alice = Mock()
        alice.name = "Alice"
        bob = Mock()
        bob.name = "Bob"
        charlie = Mock()
        charlie.name = "Charlie"
        players = [alice, bob, charlie]
        result = filter_players_by_name(players, "ALICE")

        assert len(result) == 1
        assert result[0].name == "Alice"

    def test_filter_players_by_name_multiple_matches(self):
        """Test filtering players with multiple matches."""
        alice = Mock()
        alice.name = "Alice"
        bob = Mock()
        bob.name = "Bob"
        alfred = Mock()
        alfred.name = "Alfred"
        players = [alice, bob, alfred]
        result = filter_players_by_name(players, "al")

        assert len(result) == 2
        assert any(p.name == "Alice" for p in result)
        assert any(p.name == "Alfred" for p in result)

    def test_filter_players_by_name_empty_filter(self):
        """Test filtering players with empty filter returns all players."""
        alice = Mock()
        alice.name = "Alice"
        bob = Mock()
        bob.name = "Bob"
        players = [alice, bob]
        result = filter_players_by_name(players, "")

        assert len(result) == 2

    def test_filter_players_by_name_no_match(self):
        """Test filtering players with no matches."""
        alice = Mock()
        alice.name = "Alice"
        bob = Mock()
        bob.name = "Bob"
        players = [alice, bob]
        result = filter_players_by_name(players, "Zed")

        assert len(result) == 0


class TestFormatPlayerLocation:
    """Test format_player_location function."""

    def test_format_player_location_standard_format(self):
        """Test formatting location with standard room ID format."""
        room_id = "earth_arkhamcity_northside_intersection_derby_high"
        result = format_player_location(room_id)

        assert "Arkhamcity" in result
        assert "Northside" in result
        assert "Intersection Derby High" in result

    def test_format_player_location_minimal_format(self):
        """Test formatting location with minimal parts."""
        room_id = "earth_zone_subzone_room"
        result = format_player_location(room_id)

        assert "Zone" in result
        assert "Subzone" in result
        assert "Room" in result

    def test_format_player_location_unexpected_format(self):
        """Test formatting location with unexpected format."""
        room_id = "short_id"
        result = format_player_location(room_id)

        assert "Short Id" in result

    def test_format_player_location_empty_string(self):
        """Test formatting location with empty string."""
        result = format_player_location("")

        assert result == "Unknown Location"

    def test_format_player_location_none(self):
        """Test formatting location with None."""
        result = format_player_location(None)  # type: ignore[arg-type]

        assert result == "Unknown Location"

    def test_format_player_location_invalid_type(self):
        """Test formatting location with invalid type."""
        result = format_player_location(12345)  # type: ignore[arg-type]

        assert result == "Unknown Location"


class TestFormatPlayerEntry:
    """Test format_player_entry function."""

    def test_format_player_entry_basic(self):
        """Test formatting basic player entry."""
        player = Mock()
        player.name = "TestPlayer"
        player.level = 5
        player.current_room_id = "earth_arkhamcity_northside_test_room"
        player.is_admin = False

        with patch("server.commands.who_commands.format_player_location", return_value="Test Location"):
            result = format_player_entry(player)

            assert "TestPlayer" in result
            assert "[5]" in result
            assert "Test Location" in result

    def test_format_player_entry_admin(self):
        """Test formatting player entry with admin indicator."""
        player = Mock()
        player.name = "AdminPlayer"
        player.level = 10
        player.current_room_id = "earth_arkhamcity_northside_test_room"
        player.is_admin = True

        with patch("server.commands.who_commands.format_player_location", return_value="Test Location"):
            result = format_player_entry(player)

            assert "AdminPlayer" in result
            assert "[ADMIN]" in result

    def test_format_player_entry_missing_attributes(self):
        """Test formatting player entry with missing attributes."""
        player = Mock()
        player.name = "TestPlayer"
        player.level = 5
        del player.current_room_id  # Remove attribute to trigger error handling

        with patch("server.commands.who_commands.format_player_location", return_value="Unknown location"):
            with patch("server.commands.who_commands.logger"):
                result = format_player_entry(player)

                assert "TestPlayer" in result
                assert "Unknown location" in result


class TestParseLastActiveDatetime:
    """Test parse_last_active_datetime function."""

    def test_parse_last_active_datetime_string_with_z(self):
        """Test parsing datetime string ending with Z."""
        last_active = "2024-01-01T12:00:00Z"
        result = parse_last_active_datetime(last_active)

        assert result is not None
        assert isinstance(result, datetime)
        assert result.tzinfo is not None

    def test_parse_last_active_datetime_string_with_timezone(self):
        """Test parsing datetime string with timezone offset."""
        last_active = "2024-01-01T12:00:00+05:00"
        result = parse_last_active_datetime(last_active)

        assert result is not None
        assert isinstance(result, datetime)

    def test_parse_last_active_datetime_string_naive(self):
        """Test parsing naive datetime string (no timezone)."""
        last_active = "2024-01-01T12:00:00"
        result = parse_last_active_datetime(last_active)

        assert result is not None
        assert isinstance(result, datetime)
        assert result.tzinfo is not None  # Should be converted to UTC

    def test_parse_last_active_datetime_datetime_naive(self):
        """Test parsing naive datetime object."""
        last_active = datetime(2024, 1, 1, 12, 0, 0)
        result = parse_last_active_datetime(last_active)

        assert result is not None
        assert result.tzinfo is not None  # Should be converted to UTC

    def test_parse_last_active_datetime_datetime_aware(self):
        """Test parsing timezone-aware datetime object."""
        last_active = datetime(2024, 1, 1, 12, 0, 0, tzinfo=UTC)
        result = parse_last_active_datetime(last_active)

        assert result is not None
        assert result.tzinfo is not None
        assert result == last_active

    def test_parse_last_active_datetime_none(self):
        """Test parsing None."""
        result = parse_last_active_datetime(None)

        assert result is None

    def test_parse_last_active_datetime_empty_string(self):
        """Test parsing empty string."""
        result = parse_last_active_datetime("")

        assert result is None

    def test_parse_last_active_datetime_invalid_string(self):
        """Test parsing invalid datetime string."""
        last_active = "not-a-date"

        with patch("server.commands.who_commands.logger"):
            result = parse_last_active_datetime(last_active)

            assert result is None


class TestFilterOnlinePlayers:
    """Test filter_online_players function."""

    @pytest.mark.asyncio
    async def test_filter_online_players_recent_activity(self):
        """Test filtering players with recent activity."""
        now = datetime.now(UTC)
        threshold = now - timedelta(minutes=5)

        player1 = Mock()
        player1.name = "RecentPlayer"
        player1.last_active = now - timedelta(minutes=2)

        player2 = Mock()
        player2.name = "OldPlayer"
        player2.last_active = now - timedelta(minutes=10)

        players = [player1, player2]

        with patch("server.commands.who_commands.parse_last_active_datetime") as mock_parse:
            mock_parse.side_effect = lambda x: x if isinstance(x, datetime) else datetime.now(UTC)
            with patch("server.commands.who_commands.logger"):
                result = await filter_online_players(players, threshold)

                assert len(result) == 1
                assert result[0].name == "RecentPlayer"

    @pytest.mark.asyncio
    async def test_filter_online_players_no_last_active(self):
        """Test filtering players without last_active."""
        threshold = datetime.now(UTC) - timedelta(minutes=5)

        player = Mock()
        player.name = "NoTimestampPlayer"
        player.last_active = None

        players = [player]

        with patch("server.commands.who_commands.logger"):
            result = await filter_online_players(players, threshold)

            assert len(result) == 0

    @pytest.mark.asyncio
    async def test_filter_online_players_all_online(self):
        """Test filtering when all players are online."""
        now = datetime.now(UTC)
        threshold = now - timedelta(minutes=5)

        player1 = Mock()
        player1.name = "Player1"
        player1.last_active = now - timedelta(minutes=1)

        player2 = Mock()
        player2.name = "Player2"
        player2.last_active = now - timedelta(minutes=2)

        players = [player1, player2]

        with patch("server.commands.who_commands.parse_last_active_datetime") as mock_parse:
            mock_parse.side_effect = lambda x: x if isinstance(x, datetime) else datetime.now(UTC)
            with patch("server.commands.who_commands.logger"):
                result = await filter_online_players(players, threshold)

                assert len(result) == 2


class TestFormatWhoResult:
    """Test format_who_result function."""

    def test_format_who_result_no_players(self):
        """Test formatting result with no players."""
        result = format_who_result([])

        assert "No players are currently online" in result

    def test_format_who_result_no_players_with_filter(self):
        """Test formatting result with no players and filter term."""
        result = format_who_result([], filter_term="test")

        assert "No players found matching" in result
        assert "test" in result

    def test_format_who_result_with_players(self):
        """Test formatting result with players."""
        player1 = Mock()
        player1.name = "Alice"
        player1.level = 5
        player1.current_room_id = "test_room"
        player1.is_admin = False

        player2 = Mock()
        player2.name = "Bob"
        player2.level = 3
        player2.current_room_id = "test_room"
        player2.is_admin = False

        players = [player1, player2]

        with patch("server.commands.who_commands.format_player_entry") as mock_format:
            mock_format.side_effect = lambda p: f"{p.name} [{p.level}]"
            result = format_who_result(players)

            assert "Online Players (2)" in result
            assert "Alice" in result
            assert "Bob" in result

    def test_format_who_result_with_filter(self):
        """Test formatting result with filter term."""
        player = Mock()
        player.name = "Alice"
        player.level = 5
        player.current_room_id = "test_room"
        player.is_admin = False

        players = [player]

        with patch("server.commands.who_commands.format_player_entry") as mock_format:
            mock_format.return_value = "Alice [5]"
            result = format_who_result(players, filter_term="al")

            assert "Players matching 'al' (1)" in result
            assert "Alice" in result


class TestGetPlayersForWho:
    """Test get_players_for_who function."""

    def test_get_players_for_who_with_filter(self):
        """Test getting players with filter term."""
        player1 = Mock()
        player1.name = "Alice"
        player2 = Mock()
        player2.name = "Bob"
        players = [player1, player2]

        with patch("server.commands.who_commands.filter_players_by_name", return_value=[player1]):
            result_players, filter_term = get_players_for_who(players, "al")

            assert len(result_players) == 1
            assert result_players[0].name == "Alice"
            assert filter_term == "al"

    def test_get_players_for_who_no_filter(self):
        """Test getting players without filter term."""
        player1 = Mock()
        player1.name = "Alice"
        player2 = Mock()
        player2.name = "Bob"
        players = [player1, player2]

        result_players, filter_term = get_players_for_who(players, None)  # type: ignore[arg-type]

        assert len(result_players) == 2
        assert filter_term is None

    def test_get_players_for_who_empty_filter(self):
        """Test getting players with empty filter term."""
        player1 = Mock()
        player1.name = "Alice"
        player2 = Mock()
        player2.name = "Bob"
        players = [player1, player2]

        result_players, filter_term = get_players_for_who(players, "")

        assert len(result_players) == 2
        assert filter_term is None


class TestHandleWhoCommand:
    """Test handle_who_command function."""

    @pytest.mark.asyncio
    async def test_handle_who_command_success(self):
        """Test successful who command."""
        command_data = {"target_player": ""}
        mock_request = MagicMock()
        mock_app = MagicMock()
        mock_persistence = AsyncMock()

        player = Mock()
        player.name = "TestPlayer"
        player.level = 5
        player.current_room_id = "test_room"
        player.last_active = datetime.now(UTC)
        player.is_admin = False

        mock_persistence.list_players.return_value = [player]
        mock_app.state.persistence = mock_persistence
        mock_request.app = mock_app

        with patch("server.commands.who_commands.filter_online_players", return_value=[player]):
            with patch("server.commands.who_commands.format_who_result", return_value="Online Players (1): TestPlayer"):
                with patch("server.commands.who_commands.logger"):
                    result = await handle_who_command(command_data, {}, mock_request, None, "testuser")

                    assert "result" in result
                    assert "Online Players" in result["result"]

    @pytest.mark.asyncio
    async def test_handle_who_command_no_request(self):
        """Test who command when request is None."""
        command_data = {"target_player": ""}

        with patch("server.commands.who_commands.logger"):
            result = await handle_who_command(command_data, {}, None, None, "testuser")

            assert "Player information is not available" in result["result"]

    @pytest.mark.asyncio
    async def test_handle_who_command_no_persistence(self):
        """Test who command when persistence is not available."""
        command_data = {"target_player": ""}
        mock_request = MagicMock()
        mock_app = MagicMock()
        mock_app.state.persistence = None
        mock_request.app = mock_app

        with patch("server.commands.who_commands.logger"):
            result = await handle_who_command(command_data, {}, mock_request, None, "testuser")

            assert "Player information is not available" in result["result"]

    @pytest.mark.asyncio
    async def test_handle_who_command_no_players(self):
        """Test who command when no players found."""
        command_data = {"target_player": ""}
        mock_request = MagicMock()
        mock_app = MagicMock()
        mock_persistence = AsyncMock()
        mock_persistence.list_players.return_value = []
        mock_app.state.persistence = mock_persistence
        mock_request.app = mock_app

        with patch("server.commands.who_commands.logger"):
            result = await handle_who_command(command_data, {}, mock_request, None, "testuser")

            assert "No players found" in result["result"]

    @pytest.mark.asyncio
    async def test_handle_who_command_with_filter(self):
        """Test who command with filter term."""
        command_data = {"target_player": "test"}
        mock_request = MagicMock()
        mock_app = MagicMock()
        mock_persistence = AsyncMock()

        player = Mock()
        player.name = "TestPlayer"
        player.level = 5
        player.current_room_id = "test_room"
        player.last_active = datetime.now(UTC)
        player.is_admin = False

        mock_persistence.list_players.return_value = [player]
        mock_app.state.persistence = mock_persistence
        mock_request.app = mock_app

        with patch("server.commands.who_commands.filter_online_players", return_value=[player]):
            with patch("server.commands.who_commands.get_players_for_who", return_value=([player], "test")):
                with patch(
                    "server.commands.who_commands.format_who_result",
                    return_value="Players matching 'test' (1): TestPlayer",
                ):
                    with patch("server.commands.who_commands.logger"):
                        result = await handle_who_command(command_data, {}, mock_request, None, "testuser")

                        assert "result" in result
                        assert "test" in result["result"]

    @pytest.mark.asyncio
    async def test_handle_who_command_error(self):
        """Test who command when error occurs."""
        command_data = {"target_player": ""}
        mock_request = MagicMock()
        mock_app = MagicMock()
        mock_persistence = AsyncMock()
        mock_persistence.list_players.side_effect = ValueError("Test error")
        mock_app.state.persistence = mock_persistence
        mock_request.app = mock_app

        with patch("server.commands.who_commands.logger"):
            result = await handle_who_command(command_data, {}, mock_request, None, "testuser")

            assert "Error retrieving player list" in result["result"]
            assert "Test error" in result["result"]
