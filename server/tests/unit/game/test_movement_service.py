"""
Unit tests for movement service.

Tests the MovementService class.
"""

import uuid
from unittest.mock import MagicMock

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
