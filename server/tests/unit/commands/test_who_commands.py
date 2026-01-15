"""
Unit tests for who commands.
"""

from datetime import UTC, datetime, timedelta
from unittest.mock import AsyncMock, MagicMock

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


def test_filter_players_by_name_no_filter():
    """Test filtering players with no filter term."""
    alice = MagicMock()
    alice.name = "Alice"
    bob = MagicMock()
    bob.name = "Bob"
    charlie = MagicMock()
    charlie.name = "Charlie"
    players = [alice, bob, charlie]

    result = filter_players_by_name(players, "")
    assert result == players


def test_filter_players_by_name_exact_match():
    """Test filtering players with exact match."""
    alice = MagicMock()
    alice.name = "Alice"
    bob = MagicMock()
    bob.name = "Bob"
    charlie = MagicMock()
    charlie.name = "Charlie"
    players = [alice, bob, charlie]

    result = filter_players_by_name(players, "Alice")
    assert len(result) == 1
    assert result[0].name == "Alice"


def test_filter_players_by_name_partial_match():
    """Test filtering players with partial match."""
    alice = MagicMock()
    alice.name = "Alice"
    bob = MagicMock()
    bob.name = "Bob"
    charlie = MagicMock()
    charlie.name = "Charlie"
    players = [alice, bob, charlie]

    result = filter_players_by_name(players, "Al")
    assert len(result) == 1
    assert result[0].name == "Alice"


def test_filter_players_by_name_case_insensitive():
    """Test filtering players is case-insensitive."""
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


def test_format_player_location_valid():
    """Test formatting valid player location."""
    room_id = "earth_arkhamcity_northside_intersection_derby_high"
    result = format_player_location(room_id)

    assert "Arkhamcity" in result
    assert "Northside" in result
    assert "Intersection Derby High" in result


def test_format_player_location_invalid():
    """Test formatting invalid player location."""
    result = format_player_location("")
    assert result == "Unknown Location"


def test_format_player_location_none():
    """Test formatting None location."""
    result = format_player_location(None)
    assert result == "Unknown Location"


def test_format_player_entry_basic():
    """Test formatting basic player entry."""
    player = MagicMock()
    player.name = "TestPlayer"
    player.level = 5
    player.current_room_id = "earth_arkhamcity_northside_intersection_derby_high"
    player.is_admin = False

    result = format_player_entry(player)

    assert "TestPlayer" in result
    assert "[5]" in result
    assert "Arkhamcity" in result


def test_format_player_entry_admin():
    """Test formatting admin player entry."""
    player = MagicMock()
    player.name = "AdminPlayer"
    player.level = 10
    player.current_room_id = "earth_arkhamcity_northside_intersection_derby_high"
    player.is_admin = True

    result = format_player_entry(player)

    assert "AdminPlayer" in result
    assert "[ADMIN]" in result


def test_format_player_entry_missing_attributes():
    """Test formatting player entry with missing attributes."""
    player = MagicMock()
    # Remove current_room_id to trigger error handling
    del player.current_room_id
    player.name = "TestPlayer"
    player.level = 5
    player.is_admin = False

    result = format_player_entry(player)

    # Should still format with fallback
    assert "TestPlayer" in result


def test_parse_last_active_datetime_none():
    """Test parse_last_active_datetime with None."""
    assert parse_last_active_datetime(None) is None


def test_parse_last_active_datetime_empty_string():
    """Test parse_last_active_datetime with empty string."""
    assert parse_last_active_datetime("") is None


def test_parse_last_active_datetime_string_with_z():
    """Test parse_last_active_datetime with string ending in Z."""
    result = parse_last_active_datetime("2025-01-01T12:00:00Z")
    assert isinstance(result, datetime)
    assert result.tzinfo is not None


def test_parse_last_active_datetime_string_with_timezone():
    """Test parse_last_active_datetime with string containing timezone."""
    result = parse_last_active_datetime("2025-01-01T12:00:00+00:00")
    assert isinstance(result, datetime)
    assert result.tzinfo is not None


def test_parse_last_active_datetime_string_without_timezone():
    """Test parse_last_active_datetime with string without timezone."""
    result = parse_last_active_datetime("2025-01-01T12:00:00")
    assert isinstance(result, datetime)
    assert result.tzinfo is not None


def test_parse_last_active_datetime_datetime_naive():
    """Test parse_last_active_datetime with naive datetime."""
    naive_dt = datetime(2025, 1, 1, 12, 0, 0)
    result = parse_last_active_datetime(naive_dt)
    assert isinstance(result, datetime)
    assert result.tzinfo is not None


def test_parse_last_active_datetime_datetime_aware():
    """Test parse_last_active_datetime with timezone-aware datetime."""
    aware_dt = datetime(2025, 1, 1, 12, 0, 0, tzinfo=UTC)
    result = parse_last_active_datetime(aware_dt)
    assert isinstance(result, datetime)
    assert result.tzinfo is not None
    assert result == aware_dt


def test_parse_last_active_datetime_invalid_string():
    """Test parse_last_active_datetime with invalid string."""
    assert parse_last_active_datetime("invalid") is None


@pytest.mark.asyncio
async def test_filter_online_players_all_online():
    """Test filter_online_players with all players online."""
    threshold = datetime.now(UTC) - timedelta(minutes=5)
    player1 = MagicMock()
    player1.name = "Player1"
    player1.last_active = datetime.now(UTC).isoformat()
    player2 = MagicMock()
    player2.name = "Player2"
    player2.last_active = datetime.now(UTC).isoformat()

    result = await filter_online_players([player1, player2], threshold)

    assert len(result) == 2


@pytest.mark.asyncio
async def test_filter_online_players_some_offline():
    """Test filter_online_players with some players offline."""
    threshold = datetime.now(UTC) - timedelta(minutes=5)
    player1 = MagicMock()
    player1.name = "Player1"
    player1.last_active = datetime.now(UTC).isoformat()
    player2 = MagicMock()
    player2.name = "Player2"
    player2.last_active = (datetime.now(UTC) - timedelta(minutes=10)).isoformat()

    result = await filter_online_players([player1, player2], threshold)

    assert len(result) == 1
    assert result[0].name == "Player1"


@pytest.mark.asyncio
async def test_filter_online_players_no_last_active():
    """Test filter_online_players with players without last_active."""
    threshold = datetime.now(UTC) - timedelta(minutes=5)
    player1 = MagicMock()
    player1.name = "Player1"
    player1.last_active = None
    player2 = MagicMock()
    player2.name = "Player2"
    player2.last_active = datetime.now(UTC).isoformat()

    result = await filter_online_players([player1, player2], threshold)

    assert len(result) == 1
    assert result[0].name == "Player2"


def test_format_who_result_no_players():
    """Test format_who_result with no players."""
    result = format_who_result([])
    assert "No players are currently online" in result


def test_format_who_result_no_players_with_filter():
    """Test format_who_result with no players and filter term."""
    result = format_who_result([], filter_term="test")
    assert "No players found matching" in result
    assert "test" in result


def test_format_who_result_with_players():
    """Test format_who_result with players."""
    player1 = MagicMock()
    player1.name = "Alice"
    player1.level = 5
    player1.current_room_id = "earth_arkhamcity_northside_intersection_derby_high"
    player1.is_admin = False
    player2 = MagicMock()
    player2.name = "Bob"
    player2.level = 10
    player2.current_room_id = "earth_arkhamcity_northside_intersection_derby_high"
    player2.is_admin = False

    result = format_who_result([player1, player2])

    assert "Online Players (2)" in result
    assert "Alice" in result
    assert "Bob" in result


def test_format_who_result_with_players_and_filter():
    """Test format_who_result with players and filter term."""
    player1 = MagicMock()
    player1.name = "Alice"
    player1.level = 5
    player1.current_room_id = "earth_arkhamcity_northside_intersection_derby_high"
    player1.is_admin = False

    result = format_who_result([player1], filter_term="al")

    assert "Players matching 'al' (1)" in result
    assert "Alice" in result


def test_get_players_for_who_no_filter():
    """Test get_players_for_who without filter."""
    players = [MagicMock(name="Alice"), MagicMock(name="Bob")]
    result_players, filter_term = get_players_for_who(players, "")

    assert result_players == players
    assert filter_term is None


def test_get_players_for_who_with_filter():
    """Test get_players_for_who with filter."""
    alice = MagicMock()
    alice.name = "Alice"
    bob = MagicMock()
    bob.name = "Bob"
    players = [alice, bob]

    result_players, filter_term = get_players_for_who(players, "al")

    assert len(result_players) == 1
    assert result_players[0].name == "Alice"
    assert filter_term == "al"


@pytest.mark.asyncio
async def test_handle_who_command_no_persistence():
    """Test handle_who_command when persistence is not available."""
    mock_request = MagicMock()
    mock_request.app = None

    result = await handle_who_command(
        command_data={},
        _current_user={},
        request=mock_request,
        _alias_storage=None,
        player_name="TestPlayer",
    )

    assert "not available" in result["result"]


@pytest.mark.asyncio
async def test_handle_who_command_no_players():
    """Test handle_who_command when no players are found."""
    mock_request = MagicMock()
    mock_request.app = MagicMock()
    mock_request.app.state = MagicMock()
    mock_request.app.state.container = MagicMock()
    mock_persistence = AsyncMock()
    mock_persistence.list_players = AsyncMock(return_value=[])
    mock_request.app.state.container.async_persistence = mock_persistence

    result = await handle_who_command(
        command_data={},
        _current_user={},
        request=mock_request,
        _alias_storage=None,
        player_name="TestPlayer",
    )

    assert "No players found" in result["result"]


@pytest.mark.asyncio
async def test_handle_who_command_success():
    """Test handle_who_command successful execution."""
    mock_request = MagicMock()
    mock_request.app = MagicMock()
    mock_request.app.state = MagicMock()
    mock_request.app.state.container = MagicMock()
    mock_persistence = AsyncMock()

    # Create mock players with recent last_active
    player1 = MagicMock()
    player1.name = "Alice"
    player1.level = 5
    player1.current_room_id = "earth_arkhamcity_northside_intersection_derby_high"
    player1.is_admin = False
    player1.last_active = datetime.now(UTC).isoformat()

    mock_persistence.list_players = AsyncMock(return_value=[player1])
    mock_request.app.state.container.async_persistence = mock_persistence

    result = await handle_who_command(
        command_data={},
        _current_user={},
        request=mock_request,
        _alias_storage=None,
        player_name="TestPlayer",
    )

    assert "Online Players" in result["result"]
    assert "Alice" in result["result"]


@pytest.mark.asyncio
async def test_handle_who_command_with_filter():
    """Test handle_who_command with filter term."""
    mock_request = MagicMock()
    mock_request.app = MagicMock()
    mock_request.app.state = MagicMock()
    mock_request.app.state.container = MagicMock()
    mock_persistence = AsyncMock()

    player1 = MagicMock()
    player1.name = "Alice"
    player1.level = 5
    player1.current_room_id = "earth_arkhamcity_northside_intersection_derby_high"
    player1.is_admin = False
    player1.last_active = datetime.now(UTC).isoformat()

    player2 = MagicMock()
    player2.name = "Bob"
    player2.level = 10
    player2.current_room_id = "earth_arkhamcity_northside_intersection_derby_high"
    player2.is_admin = False
    player2.last_active = datetime.now(UTC).isoformat()

    mock_persistence.list_players = AsyncMock(return_value=[player1, player2])
    mock_request.app.state.container.async_persistence = mock_persistence

    result = await handle_who_command(
        command_data={"target_player": "al"},
        _current_user={},
        request=mock_request,
        _alias_storage=None,
        player_name="TestPlayer",
    )

    assert "Players matching 'al'" in result["result"]
    assert "Alice" in result["result"]


@pytest.mark.asyncio
async def test_handle_who_command_error_handling():
    """Test handle_who_command handles exceptions gracefully."""
    mock_request = MagicMock()
    mock_request.app = MagicMock()
    mock_request.app.state = MagicMock()
    mock_request.app.state.container = MagicMock()
    mock_persistence = AsyncMock()
    mock_persistence.list_players = AsyncMock(side_effect=ValueError("Test error"))
    mock_request.app.state.container.async_persistence = mock_persistence

    result = await handle_who_command(
        command_data={},
        _current_user={},
        request=mock_request,
        _alias_storage=None,
        player_name="TestPlayer",
    )

    assert "Error retrieving player list" in result["result"]
    assert "Test error" in result["result"]


def test_format_player_location_short_format():
    """Test format_player_location() with short room ID format."""
    room_id = "earth_zone_room"
    result = format_player_location(room_id)
    # Should use fallback formatting
    assert "Zone Room" in result or "Unknown" in result


def test_format_player_location_non_string():
    """Test format_player_location() with non-string input."""
    result = format_player_location(123)
    assert result == "Unknown Location"


def test_format_player_entry_error_handling():
    """Test format_player_entry() handles errors gracefully."""
    player = MagicMock()
    # Make accessing attributes raise errors
    player.name = "TestPlayer"
    player.level = 5
    # Make current_room_id raise AttributeError
    type(player).current_room_id = property(lambda self: (_ for _ in ()).throw(AttributeError("test")))
    player.is_admin = False
    result = format_player_entry(player)
    # Should still return a formatted string
    assert "TestPlayer" in result or "Unknown Player" in result


@pytest.mark.asyncio
async def test_filter_online_players_invalid_last_active():
    """Test filter_online_players() handles invalid last_active."""
    threshold = datetime.now(UTC) - timedelta(minutes=5)
    player1 = MagicMock()
    player1.name = "Player1"
    player1.last_active = "invalid_datetime"
    player2 = MagicMock()
    player2.name = "Player2"
    player2.last_active = datetime.now(UTC).isoformat()
    result = await filter_online_players([player1, player2], threshold)
    # Player1 should be skipped due to invalid last_active
    assert len(result) == 1
    assert result[0].name == "Player2"


def test_parse_last_active_datetime_invalid_format():
    """Test parse_last_active_datetime() with invalid format."""
    result = parse_last_active_datetime("not-a-date")
    assert result is None
