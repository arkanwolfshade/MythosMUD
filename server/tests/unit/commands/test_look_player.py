"""
Unit tests for player look functionality.

Tests the helper functions for looking at players in rooms.
"""

import uuid
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from server.commands.look_player import (
    _find_matching_players,
    _format_player_look_display,
    _get_players_in_room,
    _handle_player_look,
    _select_target_player,
    _try_lookup_player_implicit,
)


@pytest.fixture
def mock_player():
    """Create a mock player."""
    player = MagicMock()
    player.player_id = uuid.uuid4()
    player.name = "TestPlayer"
    player.get_stats.return_value = {
        "current_hp": 50,
        "max_hp": 100,
        "current_lcd": 75,
        "max_lcd": 100,
        "position": "standing",
    }
    player.get_equipped_items.return_value = {
        "torso": {"item_name": "armor", "prototype_id": "armor_plate_001"},
    }
    return player


@pytest.fixture
def mock_room():
    """Create a mock room."""
    room = MagicMock()
    room.id = "earth_arkhamcity_street_room_001"
    room.get_players.return_value = [str(uuid.uuid4())]
    return room


@pytest.fixture
def mock_persistence(mock_player):
    """Create a mock persistence layer."""
    persistence = MagicMock()
    persistence.get_player_by_id = AsyncMock(return_value=mock_player)
    return persistence


@pytest.mark.asyncio
async def test_get_players_in_room_success(mock_room, mock_persistence, mock_player):
    """Test getting players in room successfully."""
    result = await _get_players_in_room(mock_room, mock_persistence)
    assert len(result) == 1
    assert result[0] == mock_player


@pytest.mark.asyncio
async def test_get_players_in_room_empty():
    """Test getting players in room when empty."""
    room = MagicMock()
    room.get_players.return_value = []
    persistence = MagicMock()
    persistence.get_player_by_id = AsyncMock(return_value=None)

    result = await _get_players_in_room(room, persistence)
    assert len(result) == 0


@pytest.mark.asyncio
async def test_get_players_in_room_invalid_uuid(mock_room, mock_persistence):
    """Test getting players in room with invalid UUID."""
    mock_room.get_players.return_value = ["not-a-uuid"]
    mock_persistence.get_player_by_id = AsyncMock(return_value=None)

    result = await _get_players_in_room(mock_room, mock_persistence)
    assert len(result) == 0


@pytest.mark.asyncio
async def test_get_players_in_room_non_iterable():
    """Test getting players in room when get_players returns non-iterable."""
    room = MagicMock()
    room.get_players.return_value = None
    persistence = MagicMock()

    result = await _get_players_in_room(room, persistence)
    assert len(result) == 0


@pytest.mark.asyncio
async def test_find_matching_players_success(mock_room, mock_persistence, mock_player):
    """Test finding matching players successfully."""
    result = await _find_matching_players("test", mock_room, mock_persistence)
    assert len(result) == 1
    assert result[0] == mock_player


@pytest.mark.asyncio
async def test_find_matching_players_no_match(mock_room, mock_persistence, mock_player):
    """Test finding matching players when no match."""
    result = await _find_matching_players("other", mock_room, mock_persistence)
    assert len(result) == 0


def test_select_target_player_single_match(mock_player):
    """Test selecting target player with single match."""
    matching_players = [mock_player]
    target_player, error_result = _select_target_player(matching_players, "test", None, "TestPlayer")
    assert target_player == mock_player
    assert error_result is None


def test_select_target_player_no_matches():
    """Test selecting target player when no matches."""
    matching_players = []
    target_player, error_result = _select_target_player(matching_players, "test", None, "TestPlayer")
    assert target_player is None
    assert error_result is not None
    assert "don't see" in error_result["result"].lower()


def test_select_target_player_with_instance_number(mock_player):
    """Test selecting target player with instance number."""
    matching_players = [mock_player]
    target_player, error_result = _select_target_player(matching_players, "test", 1, "TestPlayer")
    assert target_player == mock_player
    assert error_result is None


def test_select_target_player_instance_number_out_of_range(mock_player):
    """Test selecting target player with invalid instance number."""
    matching_players = [mock_player]
    target_player, error_result = _select_target_player(matching_players, "test", 2, "TestPlayer")
    assert target_player is None
    assert error_result is not None
    assert "aren't that many" in error_result["result"].lower()


def test_select_target_player_multiple_matches(mock_player):
    """Test selecting target player with multiple matches."""
    player2 = MagicMock()
    player2.name = "TestPlayer2"
    matching_players = [mock_player, player2]
    target_player, error_result = _select_target_player(matching_players, "test", None, "TestPlayer")
    assert target_player is None
    assert error_result is not None
    assert "multiple players" in error_result["result"].lower()


def test_format_player_look_display_basic(mock_player):
    """Test formatting player look display with basic info."""
    result = _format_player_look_display(mock_player)
    assert "TestPlayer" in result
    assert "Position:" in result
    assert "Health:" in result
    assert "lucidity:" in result


def test_format_player_look_display_with_equipment(mock_player):
    """Test formatting player look display with equipment."""
    # Use visible slot (torso is visible, chest is not)
    result = _format_player_look_display(mock_player)
    assert "Visible Equipment:" in result
    assert "armor" in result
    assert "torso" in result


def test_format_player_look_display_no_equipment():
    """Test formatting player look display without equipment."""
    player = MagicMock()
    player.name = "TestPlayer"
    player.get_stats.return_value = {"position": "standing"}
    player.get_equipped_items.return_value = {}

    result = _format_player_look_display(player)
    assert "TestPlayer" in result
    assert "Visible Equipment:" not in result


@pytest.mark.asyncio
async def test_handle_player_look_success(mock_room, mock_persistence, mock_player):
    """Test handling player look successfully."""
    result = await _handle_player_look("test", "test", None, mock_room, mock_persistence, "TestPlayer")
    assert result is not None
    assert "result" in result
    assert "TestPlayer" in result["result"]


@pytest.mark.asyncio
async def test_handle_player_look_not_found(mock_room, mock_persistence):
    """Test handling player look when player not found."""
    mock_room.get_players.return_value = []
    result = await _handle_player_look("other", "other", None, mock_room, mock_persistence, "TestPlayer")
    assert result is not None
    assert "don't see" in result["result"].lower()


@pytest.mark.asyncio
async def test_handle_player_look_multiple_matches(mock_room, mock_persistence, mock_player):
    """Test handling player look with multiple matches."""
    player2 = MagicMock()
    player2.name = "TestPlayer2"
    player2.player_id = uuid.uuid4()
    mock_persistence.get_player_by_id = AsyncMock(side_effect=[mock_player, player2])
    mock_room.get_players.return_value = [str(mock_player.player_id), str(player2.player_id)]

    result = await _handle_player_look("test", "test", None, mock_room, mock_persistence, "TestPlayer")
    assert result is not None
    assert "multiple players" in result["result"].lower()


@pytest.mark.asyncio
async def test_handle_player_look_with_instance_number(mock_room, mock_persistence, mock_player):
    """Test handling player look with instance number."""
    result = await _handle_player_look("test", "test", 1, mock_room, mock_persistence, "TestPlayer")
    assert result is not None
    assert "TestPlayer" in result["result"]


@pytest.mark.asyncio
async def test_try_lookup_player_implicit_success(mock_room, mock_persistence, mock_player):
    """Test trying implicit player lookup successfully."""
    result = await _try_lookup_player_implicit("test", "test", None, mock_room, mock_persistence, "TestPlayer")
    assert result is not None
    assert "TestPlayer" in result["result"]


@pytest.mark.asyncio
async def test_try_lookup_player_implicit_not_found(mock_room, mock_persistence):
    """Test trying implicit player lookup when not found."""
    mock_room.get_players.return_value = []
    result = await _try_lookup_player_implicit("other", "other", None, mock_room, mock_persistence, "TestPlayer")
    assert result is None


@pytest.mark.asyncio
async def test_try_lookup_player_implicit_multiple_matches(mock_room, mock_persistence, mock_player):
    """Test trying implicit player lookup with multiple matches."""
    player2 = MagicMock()
    player2.name = "TestPlayer2"
    player2.player_id = uuid.uuid4()
    mock_persistence.get_player_by_id = AsyncMock(side_effect=[mock_player, player2])
    mock_room.get_players.return_value = [str(mock_player.player_id), str(player2.player_id)]

    result = await _try_lookup_player_implicit("test", "test", None, mock_room, mock_persistence, "TestPlayer")
    assert result is not None
    assert "multiple players" in result["result"].lower()
