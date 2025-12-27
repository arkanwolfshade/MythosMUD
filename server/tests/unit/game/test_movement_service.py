"""
Unit tests for movement service.

Tests the MovementService class for player movement operations.
"""

import uuid
from unittest.mock import AsyncMock, MagicMock

import pytest

from server.exceptions import DatabaseError, ValidationError
from server.game.movement_service import MovementService


@pytest.fixture
def mock_async_persistence():
    """Create a mock async persistence layer."""
    persistence = MagicMock()
    persistence.get_player_by_id = AsyncMock()
    persistence.get_player_by_name = AsyncMock()
    persistence.get_room_by_id = MagicMock()
    persistence.save_player = AsyncMock()
    return persistence


@pytest.fixture
def mock_room():
    """Create a mock room."""
    room = MagicMock()
    room.id = "room1"
    room.name = "Test Room"
    room.exits = {"north": "room2"}
    room.has_player = MagicMock(return_value=True)
    room.player_left = MagicMock()
    room.player_entered = MagicMock()
    room.add_player_silently = MagicMock()
    room.get_players = MagicMock(return_value=[])
    return room


@pytest.fixture
def movement_service(mock_async_persistence):
    """Create a MovementService instance."""
    return MovementService(async_persistence=mock_async_persistence)


@pytest.mark.asyncio
async def test_move_player_empty_player_id(movement_service):
    """Test move_player raises ValidationError for empty player_id."""
    with pytest.raises(ValidationError, match="Player ID cannot be empty"):
        await movement_service.move_player("", "room1", "room2")


@pytest.mark.asyncio
async def test_move_player_empty_from_room(movement_service):
    """Test move_player raises ValidationError for empty from_room_id."""
    with pytest.raises(ValidationError, match="From room ID cannot be empty"):
        await movement_service.move_player(uuid.uuid4(), "", "room2")


@pytest.mark.asyncio
async def test_move_player_empty_to_room(movement_service):
    """Test move_player raises ValidationError for empty to_room_id."""
    with pytest.raises(ValidationError, match="To room ID cannot be empty"):
        await movement_service.move_player(uuid.uuid4(), "room1", "")


@pytest.mark.asyncio
async def test_move_player_same_room(movement_service):
    """Test move_player returns False when from_room_id == to_room_id."""
    result = await movement_service.move_player(uuid.uuid4(), "room1", "room1")
    assert result is False


@pytest.mark.asyncio
async def test_move_player_player_not_found(movement_service, mock_async_persistence):
    """Test move_player raises ValidationError when player is not found."""
    mock_async_persistence.get_player_by_id.return_value = None
    mock_async_persistence.get_player_by_name.return_value = None
    
    with pytest.raises(ValidationError, match="Player not found"):
        await movement_service.move_player(uuid.uuid4(), "room1", "room2")


@pytest.mark.asyncio
async def test_move_player_from_room_not_found(movement_service, mock_async_persistence, mock_room):
    """Test move_player raises ValidationError when from_room is not found."""
    mock_player = MagicMock()
    mock_player.player_id = uuid.uuid4()
    mock_player.current_room_id = "room1"
    mock_async_persistence.get_player_by_id.return_value = mock_player
    mock_async_persistence.get_room_by_id.return_value = None
    
    with pytest.raises(ValidationError, match="From room.*not found"):
        await movement_service.move_player(mock_player.player_id, "room1", "room2")


@pytest.mark.asyncio
async def test_move_player_to_room_not_found(movement_service, mock_async_persistence, mock_room):
    """Test move_player raises ValidationError when to_room is not found."""
    mock_player = MagicMock()
    mock_player.player_id = uuid.uuid4()
    mock_player.current_room_id = "room1"
    mock_async_persistence.get_player_by_id.return_value = mock_player
    mock_async_persistence.get_room_by_id.side_effect = [mock_room, None]
    
    with pytest.raises(ValidationError, match="To room.*not found"):
        await movement_service.move_player(mock_player.player_id, "room1", "room2")


@pytest.mark.asyncio
async def test_move_player_player_not_in_from_room(movement_service, mock_async_persistence, mock_room):
    """Test move_player returns False when player is not in from_room."""
    mock_player = MagicMock()
    mock_player.player_id = uuid.uuid4()
    mock_player.current_room_id = "room1"
    mock_async_persistence.get_player_by_id.return_value = mock_player
    mock_room.has_player.return_value = False
    mock_to_room = MagicMock()
    mock_to_room.id = "room2"
    mock_to_room.exits = {}
    mock_async_persistence.get_room_by_id.side_effect = [mock_room, mock_to_room]
    
    result = await movement_service.move_player(mock_player.player_id, "room1", "room2")
    assert result is False


@pytest.mark.asyncio
async def test_move_player_success(movement_service, mock_async_persistence, mock_room):
    """Test move_player successfully moves player."""
    mock_player = MagicMock()
    mock_player.player_id = uuid.uuid4()
    mock_player.current_room_id = "room1"
    mock_async_persistence.get_player_by_id.return_value = mock_player
    mock_room.has_player.return_value = True
    mock_to_room = MagicMock()
    mock_to_room.id = "room2"
    mock_to_room.exits = {}
    mock_to_room.has_player.return_value = False
    mock_async_persistence.get_room_by_id.side_effect = [mock_room, mock_to_room]
    
    # Mock validation to pass
    with pytest.MonkeyPatch().context() as mp:
        mp.setattr(movement_service, "_validate_movement", AsyncMock(return_value=True))
        
        result = await movement_service.move_player(mock_player.player_id, "room1", "room2")
        assert result is True
        mock_room.player_left.assert_called_once()
        mock_to_room.player_entered.assert_called_once()
        mock_async_persistence.save_player.assert_awaited_once()


@pytest.mark.asyncio
async def test_move_player_database_error(movement_service, mock_async_persistence, mock_room):
    """Test move_player raises DatabaseError on database failure."""
    from sqlalchemy.exc import SQLAlchemyError
    
    mock_player = MagicMock()
    mock_player.player_id = uuid.uuid4()
    mock_async_persistence.get_player_by_id.return_value = mock_player
    mock_async_persistence.get_room_by_id.side_effect = SQLAlchemyError("Database error")
    
    with pytest.raises(DatabaseError):
        await movement_service.move_player(mock_player.player_id, "room1", "room2")


@pytest.mark.asyncio
async def test_add_player_to_room_empty_player_id(movement_service):
    """Test add_player_to_room raises ValidationError for empty player_id."""
    with pytest.raises(ValidationError, match="Player ID cannot be empty"):
        await movement_service.add_player_to_room("", "room1")


@pytest.mark.asyncio
async def test_add_player_to_room_empty_room_id(movement_service):
    """Test add_player_to_room raises ValidationError for empty room_id."""
    with pytest.raises(ValidationError, match="Room ID cannot be empty"):
        await movement_service.add_player_to_room(uuid.uuid4(), "")


@pytest.mark.asyncio
async def test_add_player_to_room_room_not_found(movement_service, mock_async_persistence):
    """Test add_player_to_room returns False when room is not found."""
    mock_async_persistence.get_room_by_id.return_value = None
    
    result = await movement_service.add_player_to_room(uuid.uuid4(), "room1")
    assert result is False


@pytest.mark.asyncio
async def test_add_player_to_room_already_in_room(movement_service, mock_async_persistence, mock_room):
    """Test add_player_to_room returns True when player is already in room."""
    mock_room.has_player.return_value = True
    mock_async_persistence.get_room_by_id.return_value = mock_room
    
    result = await movement_service.add_player_to_room(uuid.uuid4(), "room1")
    assert result is True


@pytest.mark.asyncio
async def test_add_player_to_room_success(movement_service, mock_async_persistence, mock_room):
    """Test add_player_to_room successfully adds player."""
    mock_room.has_player.return_value = False
    mock_async_persistence.get_room_by_id.return_value = mock_room
    mock_player = MagicMock()
    mock_player.current_room_id = None
    mock_async_persistence.get_player_by_id.return_value = mock_player
    
    result = await movement_service.add_player_to_room(uuid.uuid4(), "room1")
    assert result is True
    mock_room.add_player_silently.assert_called_once()
    mock_async_persistence.save_player.assert_awaited_once()


@pytest.mark.asyncio
async def test_remove_player_from_room_empty_player_id(movement_service):
    """Test remove_player_from_room raises ValidationError for empty player_id."""
    with pytest.raises(ValidationError, match="Player ID cannot be empty"):
        movement_service.remove_player_from_room("", "room1")


@pytest.mark.asyncio
async def test_remove_player_from_room_empty_room_id(movement_service):
    """Test remove_player_from_room raises ValidationError for empty room_id."""
    with pytest.raises(ValidationError, match="Room ID cannot be empty"):
        movement_service.remove_player_from_room(uuid.uuid4(), "")


@pytest.mark.asyncio
async def test_remove_player_from_room_room_not_found(movement_service, mock_async_persistence):
    """Test remove_player_from_room returns False when room is not found."""
    mock_async_persistence.get_room_by_id.return_value = None
    
    result = movement_service.remove_player_from_room(uuid.uuid4(), "room1")
    assert result is False


@pytest.mark.asyncio
async def test_remove_player_from_room_not_in_room(movement_service, mock_async_persistence, mock_room):
    """Test remove_player_from_room returns True when player is not in room."""
    mock_room.has_player.return_value = False
    mock_async_persistence.get_room_by_id.return_value = mock_room
    
    result = movement_service.remove_player_from_room(uuid.uuid4(), "room1")
    assert result is True


@pytest.mark.asyncio
async def test_remove_player_from_room_success(movement_service, mock_async_persistence, mock_room):
    """Test remove_player_from_room successfully removes player."""
    mock_room.has_player.return_value = True
    mock_async_persistence.get_room_by_id.return_value = mock_room
    
    result = movement_service.remove_player_from_room(uuid.uuid4(), "room1")
    assert result is True
    mock_room.player_left.assert_called_once()


@pytest.mark.asyncio
async def test_get_player_room_empty_player_id(movement_service):
    """Test get_player_room raises ValidationError for empty player_id."""
    with pytest.raises(ValidationError, match="Player ID cannot be empty"):
        await movement_service.get_player_room("")


@pytest.mark.asyncio
async def test_get_player_room_success(movement_service, mock_async_persistence):
    """Test get_player_room returns room_id when player is found."""
    mock_player = MagicMock()
    mock_player.current_room_id = "room1"
    mock_async_persistence.get_player_by_id.return_value = mock_player
    
    result = await movement_service.get_player_room(uuid.uuid4())
    assert result == "room1"


@pytest.mark.asyncio
async def test_get_player_room_not_found(movement_service, mock_async_persistence):
    """Test get_player_room returns None when player is not found."""
    mock_async_persistence.get_player_by_id.return_value = None
    
    result = await movement_service.get_player_room(uuid.uuid4())
    assert result is None


@pytest.mark.asyncio
async def test_get_room_players_empty_room_id(movement_service):
    """Test get_room_players raises ValidationError for empty room_id."""
    with pytest.raises(ValidationError, match="Room ID cannot be empty"):
        movement_service.get_room_players("")


@pytest.mark.asyncio
async def test_get_room_players_success(movement_service, mock_async_persistence, mock_room):
    """Test get_room_players returns list of player IDs."""
    mock_room.get_players.return_value = ["player1", "player2"]
    mock_async_persistence.get_room_by_id.return_value = mock_room
    
    result = movement_service.get_room_players("room1")
    assert result == ["player1", "player2"]


@pytest.mark.asyncio
async def test_get_room_players_room_not_found(movement_service, mock_async_persistence):
    """Test get_room_players returns empty list when room is not found."""
    mock_async_persistence.get_room_by_id.return_value = None
    
    result = movement_service.get_room_players("room1")
    assert result == []


@pytest.mark.asyncio
async def test_validate_player_location_empty_player_id(movement_service):
    """Test validate_player_location raises ValidationError for empty player_id."""
    with pytest.raises(ValidationError, match="Player ID cannot be empty"):
        movement_service.validate_player_location("", "room1")


@pytest.mark.asyncio
async def test_validate_player_location_empty_room_id(movement_service):
    """Test validate_player_location raises ValidationError for empty room_id."""
    with pytest.raises(ValidationError, match="Room ID cannot be empty"):
        movement_service.validate_player_location("player1", "")


@pytest.mark.asyncio
async def test_validate_player_location_success(movement_service, mock_async_persistence, mock_room):
    """Test validate_player_location returns True when player is in room."""
    mock_room.has_player.return_value = True
    mock_async_persistence.get_room_by_id.return_value = mock_room
    
    result = movement_service.validate_player_location("player1", "room1")
    assert result is True


@pytest.mark.asyncio
async def test_validate_player_location_room_not_found(movement_service, mock_async_persistence):
    """Test validate_player_location returns False when room is not found."""
    mock_async_persistence.get_room_by_id.return_value = None
    
    result = movement_service.validate_player_location("player1", "room1")
    assert result is False


@pytest.mark.asyncio
async def test_validate_player_location_not_in_room(movement_service, mock_async_persistence, mock_room):
    """Test validate_player_location returns False when player is not in room."""
    mock_room.has_player.return_value = False
    mock_async_persistence.get_room_by_id.return_value = mock_room
    
    result = movement_service.validate_player_location("player1", "room1")
    assert result is False


@pytest.mark.asyncio
async def test_validate_exit_success(movement_service, mock_async_persistence, mock_room):
    """Test _validate_exit returns True when exit exists."""
    mock_room.exits = {"north": "room2"}
    mock_async_persistence.get_room_by_id.return_value = mock_room
    
    result = movement_service._validate_exit(mock_room, "room2")
    assert result is True


@pytest.mark.asyncio
async def test_validate_exit_no_exit(movement_service, mock_async_persistence, mock_room):
    """Test _validate_exit returns False when exit does not exist."""
    mock_room.exits = {"north": "room3"}
    mock_async_persistence.get_room_by_id.return_value = mock_room
    
    result = movement_service._validate_exit(mock_room, "room2")
    assert result is False


@pytest.mark.asyncio
async def test_validate_exit_no_exits(movement_service, mock_async_persistence, mock_room):
    """Test _validate_exit returns False when room has no exits."""
    mock_room.exits = {}
    mock_async_persistence.get_room_by_id.return_value = mock_room
    
    result = movement_service._validate_exit(mock_room, "room2")
    assert result is False


@pytest.mark.asyncio
async def test_check_combat_state_no_service(movement_service):
    """Test _check_combat_state returns True when no combat service."""
    result = movement_service._check_combat_state(uuid.uuid4(), "room1", "room2")
    assert result is True


@pytest.mark.asyncio
async def test_check_combat_state_not_in_combat(movement_service):
    """Test _check_combat_state returns True when player is not in combat."""
    mock_combat_service = MagicMock()
    mock_combat_service.is_player_in_combat_sync.return_value = False
    movement_service._player_combat_service = mock_combat_service
    
    result = movement_service._check_combat_state(uuid.uuid4(), "room1", "room2")
    assert result is True


@pytest.mark.asyncio
async def test_check_combat_state_in_combat(movement_service):
    """Test _check_combat_state returns False when player is in combat."""
    mock_combat_service = MagicMock()
    mock_combat_service.is_player_in_combat_sync.return_value = True
    movement_service._player_combat_service = mock_combat_service
    
    result = movement_service._check_combat_state(uuid.uuid4(), "room1", "room2")
    assert result is False


@pytest.mark.asyncio
async def test_check_player_posture_standing(movement_service):
    """Test _check_player_posture returns True when player is standing."""
    mock_player = MagicMock()
    mock_player.get_stats.return_value = {"position": "standing"}
    
    result = movement_service._check_player_posture(mock_player, uuid.uuid4(), "room1", "room2")
    assert result is True


@pytest.mark.asyncio
async def test_check_player_posture_sitting(movement_service):
    """Test _check_player_posture returns False when player is sitting."""
    mock_player = MagicMock()
    mock_player.get_stats.return_value = {"position": "sitting"}
    
    result = movement_service._check_player_posture(mock_player, uuid.uuid4(), "room1", "room2")
    assert result is False


@pytest.mark.asyncio
async def test_check_player_posture_no_get_stats(movement_service):
    """Test _check_player_posture returns True when player has no get_stats."""
    mock_player = MagicMock()
    del mock_player.get_stats
    
    result = movement_service._check_player_posture(mock_player, uuid.uuid4(), "room1", "room2")
    assert result is True
