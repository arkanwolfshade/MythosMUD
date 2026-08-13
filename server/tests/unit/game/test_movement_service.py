"""
Unit tests for movement service.

Tests the MovementService class.
"""

import uuid
from unittest.mock import AsyncMock, MagicMock, patch

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


@pytest.mark.asyncio
async def test_validate_movement_allows_ghost_in_destination(movement_service, mock_persistence):
    """Foyer go-east must not abort when hallway still lists the player (co-locate ghost)."""
    player_id = uuid.uuid4()
    player = MagicMock()
    player.player_id = player_id
    foyer = MagicMock()
    foyer.id = "earth_arkhamcity_sanitarium_room_foyer_001"
    foyer.has_player = MagicMock(return_value=True)
    foyer.exits = {"east": "earth_arkhamcity_sanitarium_room_hallway_001"}
    hallway = MagicMock()
    hallway.id = "earth_arkhamcity_sanitarium_room_hallway_001"
    hallway.has_player = MagicMock(return_value=True)

    mock_persistence.get_player_by_id = AsyncMock(return_value=player)
    mock_persistence.get_room_by_id = MagicMock(
        side_effect=lambda rid: foyer if "foyer" in rid else hallway if "hallway" in rid else None
    )

    with (
        patch.object(movement_service, "_check_combat_state", return_value=True),
        patch.object(movement_service, "_check_player_posture", return_value=True),
        patch.object(movement_service, "_validate_player_room_membership", new_callable=AsyncMock, return_value=True),
        patch.object(movement_service, "_validate_exit", return_value=True),
    ):
        result = await movement_service._validate_movement(
            player,
            "earth_arkhamcity_sanitarium_room_foyer_001",
            "earth_arkhamcity_sanitarium_room_hallway_001",
        )

    assert result is True


def test_set_player_combat_service(movement_service):
    """Test set_player_combat_service updates combat service reference."""
    combat_svc = MagicMock()
    movement_service.set_player_combat_service(combat_svc)
    assert movement_service._player_combat_service is combat_svc


def test_validate_move_params_same_room(movement_service):
    """Test _validate_move_params returns False for same room."""
    player_id = uuid.uuid4()
    assert movement_service._validate_move_params(player_id, "room_a", "room_a") is False


@pytest.mark.asyncio
async def test_move_player_success(movement_service, mock_persistence):
    """Test move_player completes a valid room transfer."""
    player_id = uuid.uuid4()
    mock_player = MagicMock()
    mock_player.player_id = player_id
    mock_player.current_room_id = "room_001"
    mock_from = MagicMock()
    mock_from.id = "room_001"
    mock_from.has_player = MagicMock(return_value=True)
    mock_to = MagicMock()
    mock_to.id = "room_002"
    mock_persistence.get_player_by_id = AsyncMock(return_value=mock_player)
    mock_persistence.get_room_by_id = MagicMock(side_effect=lambda rid: mock_from if rid == "room_001" else mock_to)
    mock_persistence.save_player = AsyncMock()

    with (
        patch.object(movement_service, "_validate_movement", new=AsyncMock(return_value=True)),
        patch.object(movement_service, "_validate_exit", return_value=True),
        patch("server.game.movement_service.get_movement_monitor") as monitor_mock,
    ):
        monitor_mock.return_value.record_movement = MagicMock()
        result = await movement_service.move_player(player_id, "room_001", "room_002")

    assert result is True
    mock_from.player_left.assert_called_once()
    mock_to.player_entered.assert_called_once()
    mock_persistence.save_player.assert_awaited_once()


@pytest.mark.asyncio
async def test_resolve_player_by_name(movement_service, mock_persistence):
    """Test _resolve_player_for_movement resolves player by name."""
    player_id = uuid.uuid4()
    mock_player = MagicMock()
    mock_player.player_id = player_id
    mock_persistence.get_player_by_name = AsyncMock(return_value=mock_player)

    player, resolved = await movement_service._resolve_player_for_movement("Arkan", {})
    assert player is mock_player
    assert str(resolved) == str(player_id)


def test_remove_player_invalid_params(movement_service):
    """Test remove_player_from_room validates empty player_id."""
    from server.exceptions import ValidationError

    with pytest.raises(ValidationError, match="Player ID cannot be empty"):
        movement_service.remove_player_from_room("", "room_001")


def test_check_combat_state_blocks_when_in_combat(movement_service):
    """Test _check_combat_state returns False when player is in combat."""
    combat_svc = MagicMock()
    combat_svc.is_player_in_combat_sync.return_value = True
    movement_service.set_player_combat_service(combat_svc)
    player_id = uuid.uuid4()
    assert movement_service._check_combat_state(player_id, "room_a", "room_b") is False


def test_check_combat_state_allows_without_service(movement_service):
    """Test _check_combat_state allows movement when no combat service."""
    movement_service._player_combat_service = None
    assert movement_service._check_combat_state(uuid.uuid4(), "room_a", "room_b") is True


def test_check_player_posture_blocks_sitting(movement_service):
    """Test _check_player_posture blocks non-standing posture."""
    player = MagicMock()
    player.get_stats.return_value = {"position": "sitting"}
    assert movement_service._check_player_posture(player, uuid.uuid4(), "room_a", "room_b") is False


def test_validate_exit_no_exits(movement_service):
    """Test _validate_exit returns False when room has no exits."""
    room = MagicMock()
    room.id = "room_a"
    room.name = "Room A"
    room.exits = {}
    assert movement_service._validate_exit(room, "room_b") is False


def test_validate_exit_found(movement_service):
    """Test _validate_exit returns True when exit matches target."""
    room = MagicMock()
    room.id = "room_a"
    room.name = "Room A"
    room.exits = {"north": "room_b"}
    assert movement_service._validate_exit(room, "room_b") is True


@pytest.mark.asyncio
async def test_move_player_player_not_found(movement_service, mock_persistence):
    """Test move_player returns False when player is missing."""
    player_id = uuid.uuid4()
    mock_persistence.get_player_by_id = AsyncMock(return_value=None)
    result = await movement_service.move_player(player_id, "room_001", "room_002")
    assert result is False


@pytest.mark.asyncio
async def test_validate_movement_success(movement_service, mock_persistence):
    """Test _validate_movement returns True for valid movement."""
    player_id = uuid.uuid4()
    player = MagicMock()
    player.player_id = str(player_id)
    from_room = MagicMock()
    from_room.id = "room_a"
    from_room.exits = {"north": "room_b"}
    to_room = MagicMock()
    to_room.id = "room_b"
    to_room.has_player.return_value = False
    mock_persistence.get_room_by_id = MagicMock(side_effect=lambda rid: from_room if rid == "room_a" else to_room)
    mock_persistence.get_player_by_id = AsyncMock(return_value=player)

    with patch.object(movement_service, "_validate_player_room_membership", new=AsyncMock(return_value=True)):
        result = await movement_service._validate_movement(player, "room_a", "room_b")
    assert result is True


@pytest.mark.asyncio
async def test_validate_movement_combat_blocks(movement_service, mock_persistence):
    """Test _validate_movement returns False when in combat."""
    player_id = uuid.uuid4()
    player = MagicMock()
    player.player_id = str(player_id)
    combat_svc = MagicMock()
    combat_svc.is_player_in_combat_sync.return_value = True
    movement_service.set_player_combat_service(combat_svc)
    result = await movement_service._validate_movement(player, "room_a", "room_b")
    assert result is False


@pytest.mark.asyncio
async def test_validate_movement_target_room_missing(movement_service, mock_persistence):
    """Test _validate_movement returns False when destination room missing."""
    player_id = uuid.uuid4()
    player = MagicMock()
    player.player_id = str(player_id)
    from_room = MagicMock()
    mock_persistence.get_room_by_id = MagicMock(side_effect=lambda rid: from_room if rid == "room_a" else None)
    mock_persistence.get_player_by_id = AsyncMock(return_value=player)

    result = await movement_service._validate_movement(player, "room_a", "room_b")
    assert result is False


def test_mark_room_explored_with_service(movement_service):
    """Test _mark_room_explored delegates to exploration service."""
    exploration = MagicMock()
    movement_service._exploration_service = exploration
    player_id = uuid.uuid4()
    movement_service._mark_room_explored(player_id, "room_x")
    exploration.mark_room_as_explored_sync.assert_called_once()


@pytest.mark.asyncio
async def test_move_player_validation_fails(movement_service, mock_persistence):
    """Test move_player returns False when validation fails."""
    player_id = uuid.uuid4()
    mock_player = MagicMock()
    mock_player.player_id = player_id
    mock_persistence.get_player_by_id = AsyncMock(return_value=mock_player)

    with patch.object(movement_service, "_validate_movement", new=AsyncMock(return_value=False)):
        result = await movement_service.move_player(player_id, "room_001", "room_002")
    assert result is False


def test_validate_exit_target_missing_in_persistence(movement_service, mock_persistence):
    """Test _validate_exit logs when target room missing from persistence."""
    room = MagicMock()
    room.id = "room_a"
    room.name = "Room A"
    room.exits = {"north": "other_room"}
    mock_persistence.get_room_by_id = MagicMock(return_value=None)
    assert movement_service._validate_exit(room, "room_missing") is False


@pytest.mark.asyncio
async def test_validate_movement_player_already_in_target(movement_service, mock_persistence):
    """Test _validate_movement returns False when player already in destination."""
    player_id = uuid.uuid4()
    player = MagicMock()
    player.player_id = str(player_id)
    from_room = MagicMock()
    from_room.id = "room_a"
    from_room.exits = {"north": "room_b"}
    to_room = MagicMock()
    to_room.id = "room_b"
    to_room.has_player.return_value = True
    mock_persistence.get_room_by_id = MagicMock(side_effect=lambda rid: from_room if rid == "room_a" else to_room)
    mock_persistence.get_player_by_id = AsyncMock(return_value=player)

    with patch.object(movement_service, "_validate_player_room_membership", new=AsyncMock(return_value=True)):
        result = await movement_service._validate_movement(player, "room_a", "room_b")
    assert result is False
    """Test _validate_player_room_membership fails when DB room differs."""
    player_id = uuid.uuid4()
    room = MagicMock()
    room.has_player.return_value = False
    db_player = MagicMock()
    db_player.current_room_id = "other_room"
    mock_persistence.get_player_by_id = AsyncMock(return_value=db_player)
    result = await movement_service._validate_player_room_membership(player_id, room, "room_001")
    assert result is False


@pytest.mark.asyncio
async def test_validate_player_room_membership_auto_add(movement_service, mock_persistence):
    """Test _validate_player_room_membership adds player when DB room matches."""
    player_id = uuid.uuid4()
    room = MagicMock()
    room.has_player.return_value = False
    room.add_player_silently = MagicMock()
    db_player = MagicMock()
    db_player.current_room_id = "room_001"
    mock_persistence.get_player_by_id = AsyncMock(return_value=db_player)
    result = await movement_service._validate_player_room_membership(player_id, room, "room_001")
    assert result is True
    room.add_player_silently.assert_called_once_with(player_id)
