"""
Unit tests for player service.

Tests the PlayerService class.
"""

import uuid
from datetime import UTC, datetime
from unittest.mock import AsyncMock, MagicMock

import pytest

from server.game.player_service import PlayerService


@pytest.fixture
def mock_persistence():
    """Create a mock persistence layer."""
    return AsyncMock()


@pytest.fixture
def player_service(mock_persistence):
    """Create a PlayerService instance."""
    return PlayerService(mock_persistence)


@pytest.mark.asyncio
async def test_player_service_init(mock_persistence):
    """Test PlayerService initialization."""
    service = PlayerService(mock_persistence)
    assert service.persistence == mock_persistence


@pytest.mark.asyncio
async def test_create_player_success(player_service, mock_persistence):
    """Test create_player() successful creation."""
    mock_persistence.get_player_by_name = AsyncMock(return_value=None)
    mock_persistence.save_player = AsyncMock()
    # Mock the player object that will be created and then retrieved
    mock_player = MagicMock()
    mock_player.player_id = uuid.uuid4()
    mock_player.name = "TestPlayer"
    mock_player.user_id = uuid.uuid4()
    mock_player.get_stats = MagicMock(
        return_value={
            "lucidity": 100,
            "current_dp": 0,
            "position": "standing",
            "constitution": 50,
            "size": 50,
            "power": 50,
            "education": 50,
        }
    )
    mock_player.get_inventory = MagicMock(return_value=[])
    mock_player.get_status_effects = MagicMock(return_value=[])
    mock_player.profession_id = 0
    mock_player.current_room_id = "room_001"
    mock_player.experience_points = 0
    mock_player.level = 1
    mock_player.created_at = datetime.now(UTC).replace(tzinfo=None)
    mock_player.last_active = datetime.now(UTC).replace(tzinfo=None)
    # Mock profession from persistence
    mock_profession = MagicMock()
    mock_profession.name = "Tramp"
    mock_profession.description = "A wanderer"
    mock_profession.flavor_text = "Lost in the streets"
    mock_persistence.get_profession_by_id = AsyncMock(return_value=mock_profession)
    mock_persistence.get_player_by_id = AsyncMock(return_value=mock_player)
    result = await player_service.create_player("TestPlayer")
    assert result is not None
    mock_persistence.save_player.assert_awaited_once()


@pytest.mark.asyncio
async def test_create_player_name_exists(player_service, mock_persistence):
    """Test create_player() when name already exists."""
    from server.exceptions import ValidationError

    existing_player = MagicMock()
    existing_player.player_id = uuid.uuid4()
    mock_persistence.get_player_by_name = AsyncMock(return_value=existing_player)
    with pytest.raises(ValidationError, match="Player name already exists"):
        await player_service.create_player("TestPlayer")


@pytest.mark.asyncio
async def test_get_player_by_id_found(player_service, mock_persistence):
    """Test get_player_by_id() when player is found."""
    mock_player = MagicMock()
    mock_player.player_id = uuid.uuid4()
    mock_player.name = "TestPlayer"
    mock_player.user_id = uuid.uuid4()
    mock_player.get_stats = MagicMock(
        return_value={
            "lucidity": 100,
            "current_dp": 0,
            "position": "standing",
            "constitution": 50,
            "size": 50,
            "power": 50,
            "education": 50,
        }
    )
    mock_player.get_inventory = MagicMock(return_value=[])
    mock_player.get_status_effects = MagicMock(return_value=[])
    mock_player.profession_id = 0
    mock_player.current_room_id = "room_001"
    mock_player.experience_points = 0
    mock_player.level = 1
    mock_player.created_at = datetime.now(UTC).replace(tzinfo=None)
    mock_player.last_active = datetime.now(UTC).replace(tzinfo=None)
    mock_profession = MagicMock()
    mock_profession.name = "Tramp"
    mock_profession.description = "A wanderer"
    mock_profession.flavor_text = "Lost in the streets"
    mock_persistence.get_profession_by_id = AsyncMock(return_value=mock_profession)
    mock_persistence.get_player_by_id = AsyncMock(return_value=mock_player)
    result = await player_service.get_player_by_id(uuid.uuid4())
    assert result is not None


@pytest.mark.asyncio
async def test_get_player_by_id_not_found(player_service, mock_persistence):
    """Test get_player_by_id() when player is not found."""
    mock_persistence.get_player_by_id = AsyncMock(return_value=None)
    result = await player_service.get_player_by_id(uuid.uuid4())
    assert result is None


@pytest.mark.asyncio
async def test_get_player_by_name_found(player_service, mock_persistence):
    """Test get_player_by_name() when player is found."""
    mock_player = MagicMock()
    mock_player.player_id = uuid.uuid4()
    mock_player.name = "TestPlayer"
    mock_player.user_id = uuid.uuid4()
    mock_player.get_stats = MagicMock(
        return_value={
            "lucidity": 100,
            "current_dp": 0,
            "position": "standing",
            "constitution": 50,
            "size": 50,
            "power": 50,
            "education": 50,
        }
    )
    mock_player.get_inventory = MagicMock(return_value=[])
    mock_player.get_status_effects = MagicMock(return_value=[])
    mock_player.profession_id = 0
    mock_player.current_room_id = "room_001"
    mock_player.experience_points = 0
    mock_player.level = 1
    mock_player.created_at = datetime.now(UTC).replace(tzinfo=None)
    mock_player.last_active = datetime.now(UTC).replace(tzinfo=None)
    mock_profession = MagicMock()
    mock_profession.name = "Tramp"
    mock_profession.description = "A wanderer"
    mock_profession.flavor_text = "Lost in the streets"
    mock_persistence.get_profession_by_id = AsyncMock(return_value=mock_profession)
    mock_persistence.get_player_by_name = AsyncMock(return_value=mock_player)
    result = await player_service.get_player_by_name("TestPlayer")
    assert result is not None


@pytest.mark.asyncio
async def test_get_player_by_name_not_found(player_service, mock_persistence):
    """Test get_player_by_name() when player is not found."""
    mock_persistence.get_player_by_name = AsyncMock(return_value=None)
    result = await player_service.get_player_by_name("TestPlayer")
    assert result is None


@pytest.mark.asyncio
async def test_list_players(player_service, mock_persistence):
    """Test list_players() returns list of players."""
    mock_players = [MagicMock(), MagicMock()]
    mock_persistence.get_all_players = AsyncMock(return_value=mock_players)
    result = await player_service.list_players()
    assert isinstance(result, list)


@pytest.mark.asyncio
async def test_resolve_player_name_found(player_service, mock_persistence):
    """Test resolve_player_name() when player is found."""
    from datetime import UTC, datetime

    # Create a proper mock player with all required fields
    mock_player = MagicMock()
    mock_player.player_id = uuid.uuid4()
    mock_player.name = "TestPlayer"
    mock_player.user_id = uuid.uuid4()
    mock_player.get_stats = MagicMock(
        return_value={
            "lucidity": 100,
            "current_dp": 0,
            "position": "standing",
            "constitution": 50,
            "size": 50,
            "power": 50,
            "education": 50,
        }
    )
    mock_player.get_inventory = MagicMock(return_value=[])
    mock_player.get_status_effects = MagicMock(return_value=[])
    mock_player.profession_id = 0
    mock_player.current_room_id = "room_001"
    mock_player.experience_points = 0
    mock_player.level = 1
    mock_player.created_at = datetime.now(UTC).replace(tzinfo=None)
    mock_player.last_active = datetime.now(UTC).replace(tzinfo=None)
    mock_profession = MagicMock()
    mock_profession.name = "Tramp"
    mock_profession.description = "A wanderer"
    mock_profession.flavor_text = "Lost in the streets"
    mock_persistence.get_profession_by_id = AsyncMock(return_value=mock_profession)
    mock_persistence.get_player_by_name = AsyncMock(return_value=mock_player)
    mock_persistence.list_players = AsyncMock(return_value=[])
    result = await player_service.resolve_player_name("TestPlayer")
    assert result is not None


@pytest.mark.asyncio
async def test_resolve_player_name_not_found(player_service, mock_persistence):
    """Test resolve_player_name() when player is not found."""
    mock_persistence.get_player_by_name = AsyncMock(return_value=None)
    result = await player_service.resolve_player_name("TestPlayer")
    assert result is None
