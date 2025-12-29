"""
Unit tests for movement service.

Tests the MovementService class.
"""

import uuid
from unittest.mock import AsyncMock, MagicMock

import pytest

from server.game.movement_service import MovementService


@pytest.fixture
def mock_persistence():
    """Create a mock persistence layer."""
    return MagicMock()


@pytest.fixture
def mock_event_bus():
    """Create a mock event bus."""
    return MagicMock()


@pytest.fixture
def movement_service(mock_persistence, mock_event_bus):
    """Create a MovementService instance."""
    return MovementService(
        event_bus=mock_event_bus,
        async_persistence=mock_persistence,
    )


def test_movement_service_init_no_persistence():
    """Test MovementService initialization without persistence raises error."""
    with pytest.raises(ValueError, match="async_persistence is required"):
        MovementService(async_persistence=None)


def test_movement_service_init(mock_persistence):
    """Test MovementService initialization."""
    service = MovementService(async_persistence=mock_persistence)
    assert service._persistence == mock_persistence


@pytest.mark.asyncio
async def test_move_player_empty_player_id(movement_service):
    """Test move_player() with empty player_id."""
    from server.exceptions import ValidationError

    with pytest.raises(ValidationError, match="Player ID cannot be empty"):
        await movement_service.move_player("", "room_001", "room_002")


@pytest.mark.asyncio
async def test_move_player_same_room(movement_service):
    """Test move_player() when from and to rooms are the same."""
    result = await movement_service.move_player(uuid.uuid4(), "room_001", "room_001")
    assert result is False


@pytest.mark.asyncio
async def test_move_player_invalid_from_room(movement_service):
    """Test move_player() with invalid from_room_id."""
    from server.exceptions import ValidationError

    with pytest.raises(ValidationError, match="From room ID cannot be empty"):
        await movement_service.move_player(uuid.uuid4(), "", "room_002")


@pytest.mark.asyncio
async def test_move_player_invalid_to_room(movement_service):
    """Test move_player() with invalid to_room_id."""
    from server.exceptions import ValidationError

    with pytest.raises(ValidationError, match="To room ID cannot be empty"):
        await movement_service.move_player(uuid.uuid4(), "room_001", "")


@pytest.mark.asyncio
async def test_add_player_to_room_success(movement_service, mock_persistence):
    """Test add_player_to_room() successfully adds player."""
    player_id = uuid.uuid4()
    room_id = "room_001"
    mock_room = MagicMock()
    mock_room.room_id = room_id
    mock_persistence.get_room_by_id = MagicMock(return_value=mock_room)
    mock_persistence.get_player_by_id = AsyncMock(return_value=MagicMock())
    result = await movement_service.add_player_to_room(player_id, room_id)
    assert result is True


@pytest.mark.asyncio
async def test_add_player_to_room_room_not_found(movement_service, mock_persistence):
    """Test add_player_to_room() when room is not found."""
    player_id = uuid.uuid4()
    room_id = "room_001"
    mock_persistence.get_room_by_id = MagicMock(return_value=None)
    result = await movement_service.add_player_to_room(player_id, room_id)
    assert result is False


@pytest.mark.asyncio
async def test_add_player_to_room_player_not_found(movement_service, mock_persistence):
    """Test add_player_to_room() when player is not found."""
    player_id = uuid.uuid4()
    room_id = "room_001"
    mock_room = MagicMock()
    mock_room.room_id = room_id
    mock_room.has_player = MagicMock(return_value=False)
    mock_room.add_player_silently = MagicMock()
    mock_persistence.get_room_by_id = MagicMock(return_value=mock_room)
    mock_persistence.get_player_by_id = AsyncMock(return_value=None)
    # The method returns True even if player not found (line 669)
    result = await movement_service.add_player_to_room(player_id, room_id)
    assert result is True


def test_remove_player_from_room_success(movement_service, mock_persistence):
    """Test remove_player_from_room() successfully removes player."""
    player_id = uuid.uuid4()
    room_id = "room_001"
    mock_room = MagicMock()
    mock_room.room_id = room_id
    mock_persistence.get_room_by_id = MagicMock(return_value=mock_room)
    result = movement_service.remove_player_from_room(player_id, room_id)
    assert result is True


def test_remove_player_from_room_room_not_found(movement_service, mock_persistence):
    """Test remove_player_from_room() when room is not found."""
    player_id = uuid.uuid4()
    room_id = "room_001"
    mock_persistence.get_room_by_id = MagicMock(return_value=None)
    result = movement_service.remove_player_from_room(player_id, room_id)
    assert result is False


@pytest.mark.asyncio
async def test_get_player_room_success(movement_service, mock_persistence):
    """Test get_player_room() returns player's room."""
    player_id = uuid.uuid4()
    mock_player = MagicMock()
    mock_player.current_room_id = "room_001"
    mock_persistence.get_player_by_id = AsyncMock(return_value=mock_player)
    result = await movement_service.get_player_room(player_id)
    assert result == "room_001"


@pytest.mark.asyncio
async def test_get_player_room_player_not_found(movement_service, mock_persistence):
    """Test get_player_room() when player is not found."""
    player_id = uuid.uuid4()
    mock_persistence.get_player_by_id = AsyncMock(return_value=None)
    result = await movement_service.get_player_room(player_id)
    assert result is None


def test_get_room_players(movement_service, mock_persistence):
    """Test get_room_players() returns list of player IDs."""
    room_id = "room_001"
    mock_room = MagicMock()
    mock_room.room_id = room_id
    mock_room.get_players = MagicMock(return_value=["player_001", "player_002"])
    mock_persistence.get_room_by_id = MagicMock(return_value=mock_room)
    result = movement_service.get_room_players(room_id)
    assert result == ["player_001", "player_002"]


def test_get_room_players_room_not_found(movement_service, mock_persistence):
    """Test get_room_players() when room is not found."""
    room_id = "room_001"
    mock_persistence.get_room_by_id = MagicMock(return_value=None)
    result = movement_service.get_room_players(room_id)
    assert result == []


def test_validate_player_location_true(movement_service, mock_persistence):
    """Test validate_player_location() returns True when player is in room."""
    player_id = "player_001"
    room_id = "room_001"
    mock_room = MagicMock()
    mock_room.has_player = MagicMock(return_value=True)
    mock_persistence.get_room_by_id = MagicMock(return_value=mock_room)
    result = movement_service.validate_player_location(player_id, room_id)
    assert result is True


def test_validate_player_location_false(movement_service, mock_persistence):
    """Test validate_player_location() returns False when player is not in room."""
    player_id = "player_001"
    room_id = "room_001"
    mock_room = MagicMock()
    mock_room.has_player = MagicMock(return_value=False)
    mock_persistence.get_room_by_id = MagicMock(return_value=mock_room)
    result = movement_service.validate_player_location(player_id, room_id)
    assert result is False


def test_validate_player_location_room_not_found(movement_service, mock_persistence):
    """Test validate_player_location() returns False when room is not found."""
    player_id = "player_001"
    room_id = "room_001"
    mock_persistence.get_room_by_id = MagicMock(return_value=None)
    result = movement_service.validate_player_location(player_id, room_id)
    assert result is False
