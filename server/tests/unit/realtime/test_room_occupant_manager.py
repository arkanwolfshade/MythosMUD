"""
Unit tests for room occupant manager.

Tests the RoomOccupantManager class for querying and processing room occupants.
"""

from unittest.mock import AsyncMock, MagicMock

import pytest

from server.realtime.room_occupant_manager import RoomOccupantManager

# pylint: disable=protected-access  # Reason: Test file - accessing protected members is standard practice for unit testing
# pylint: disable=redefined-outer-name  # Reason: Test file - pytest fixture parameter names must match fixture names, causing intentional redefinitions


@pytest.fixture
def mock_connection_manager():
    """Create mock connection manager."""
    manager = MagicMock()
    manager.async_persistence = MagicMock()
    return manager


@pytest.fixture
def occupant_manager(mock_connection_manager):
    """Create RoomOccupantManager instance."""
    return RoomOccupantManager(mock_connection_manager)


@pytest.mark.asyncio
async def test_room_occupant_manager_init(occupant_manager, mock_connection_manager):
    """Test RoomOccupantManager initialization."""
    assert occupant_manager.connection_manager == mock_connection_manager
    assert occupant_manager.room_id_utils is not None
    assert occupant_manager.npc_processor is not None
    assert occupant_manager.player_processor is not None


@pytest.mark.asyncio
async def test_get_room_occupants_no_connection_manager():
    """Test get_room_occupants returns empty when no connection manager."""
    manager = RoomOccupantManager(None)
    result = await manager.get_room_occupants("room_001")
    assert result == []


@pytest.mark.asyncio
async def test_get_room_occupants_no_persistence(occupant_manager, mock_connection_manager):
    """Test get_room_occupants returns empty when no persistence."""
    mock_connection_manager.async_persistence = None
    result = await occupant_manager.get_room_occupants("room_001")
    assert result == []


@pytest.mark.asyncio
async def test_get_room_occupants_no_room(occupant_manager, mock_connection_manager):
    """Test get_room_occupants returns empty when room not found."""
    mock_connection_manager.async_persistence.get_room_by_id = MagicMock(return_value=None)
    result = await occupant_manager.get_room_occupants("room_001")
    assert result == []


@pytest.mark.asyncio
async def test_get_room_occupants_success(occupant_manager, mock_connection_manager):
    """Test get_room_occupants returns occupants."""
    mock_room = MagicMock()
    mock_room.get_players = MagicMock(return_value=["player_001"])
    mock_connection_manager.async_persistence.get_room_by_id = MagicMock(return_value=mock_room)
    occupant_manager.player_processor.process_players_for_occupants = AsyncMock(return_value=[])
    occupant_manager.npc_processor.query_npcs_for_room = AsyncMock(return_value=[])
    occupant_manager.npc_processor.process_npcs_for_occupants = MagicMock(return_value=[])
    result = await occupant_manager.get_room_occupants("room_001")
    assert isinstance(result, list)


@pytest.mark.asyncio
async def test_get_room_occupants_error(occupant_manager, mock_connection_manager):
    """Test get_room_occupants handles errors gracefully."""
    mock_connection_manager.async_persistence.get_room_by_id = MagicMock(side_effect=ValueError("Error"))
    result = await occupant_manager.get_room_occupants("room_001")
    assert result == []


def test_separate_occupants_by_type(occupant_manager):
    """Test separate_occupants_by_type separates occupants."""
    occupants = [
        {"player_name": "PlayerOne"},  # Dict with player_name
        {"npc_name": "NPCOne"},  # Dict with npc_name
        "PlayerTwo",  # String format
    ]
    players, npcs, all_occupants = occupant_manager.separate_occupants_by_type(occupants, "room_001")
    assert len(players) == 1  # Only dict with player_name
    assert len(npcs) == 1  # Only dict with npc_name
    assert len(all_occupants) == 3  # All three occupants


@pytest.mark.asyncio
async def test_get_room_occupants_with_ensure_player(occupant_manager, mock_connection_manager):
    """Test get_room_occupants with ensure_player_included."""
    player_id = "player_001"
    mock_room = MagicMock()
    mock_room.get_players = MagicMock(return_value=[])
    mock_connection_manager.async_persistence.get_room_by_id = MagicMock(return_value=mock_room)
    occupant_manager.player_processor.process_players_for_occupants = AsyncMock(return_value=[])
    occupant_manager.npc_processor.query_npcs_for_room = AsyncMock(return_value=[])
    occupant_manager.npc_processor.process_npcs_for_occupants = MagicMock(return_value=[])
    result = await occupant_manager.get_room_occupants("room_001", ensure_player_included=player_id)
    assert isinstance(result, list)
    occupant_manager.player_processor.process_players_for_occupants.assert_awaited_once_with("room_001", [], player_id)


@pytest.mark.asyncio
async def test_get_room_occupants_with_players_and_npcs(occupant_manager, mock_connection_manager):
    """Test get_room_occupants returns both players and NPCs."""
    mock_room = MagicMock()
    mock_room.get_players = MagicMock(return_value=["player_001", "player_002"])
    mock_connection_manager.async_persistence.get_room_by_id = MagicMock(return_value=mock_room)
    player_occupants = [{"player_id": "player_001"}, {"player_id": "player_002"}]
    npc_occupants = [{"npc_id": "npc_001"}]
    occupant_manager.player_processor.process_players_for_occupants = AsyncMock(return_value=player_occupants)
    occupant_manager.npc_processor.query_npcs_for_room = AsyncMock(return_value=["npc_001"])
    occupant_manager.npc_processor.process_npcs_for_occupants = MagicMock(return_value=npc_occupants)
    result = await occupant_manager.get_room_occupants("room_001")
    assert len(result) == 3  # 2 players + 1 NPC


@pytest.mark.asyncio
async def test_get_room_occupants_get_players_error(occupant_manager, mock_connection_manager):
    """Test get_room_occupants handles get_players error."""
    mock_room = MagicMock()
    mock_room.get_players = MagicMock(side_effect=AttributeError("No get_players"))
    mock_connection_manager.async_persistence.get_room_by_id = MagicMock(return_value=mock_room)
    result = await occupant_manager.get_room_occupants("room_001")
    assert result == []


def test_separate_occupants_by_type_empty_list(occupant_manager):
    """Test separate_occupants_by_type with empty list."""
    players, npcs, strings = occupant_manager.separate_occupants_by_type([], "room_001")
    assert players == []
    assert npcs == []
    assert strings == []
