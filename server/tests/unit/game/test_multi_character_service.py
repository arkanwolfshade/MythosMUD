"""
Unit tests for multi-character support in PlayerService.

Tests character limit enforcement, soft deletion, and character retrieval.
"""

import uuid
from unittest.mock import AsyncMock, MagicMock

import pytest

from server.exceptions import ValidationError
from server.game.player_service import PlayerService
from server.models import Stats


@pytest.fixture
def mock_persistence():
    """Create a mock persistence layer."""
    persistence = MagicMock()
    return persistence


@pytest.fixture
def player_service(mock_persistence):
    """Create a PlayerService instance with mock persistence."""
    return PlayerService(persistence=mock_persistence)


@pytest.mark.asyncio
async def test_create_player_with_stats_character_limit(player_service, mock_persistence):
    """Test that character creation fails when user has 3 active characters."""
    user_id = uuid.uuid4()

    # Mock 3 active characters
    from server.models.player import Player

    mock_characters = [
        Player(player_id=uuid.uuid4(), user_id=user_id, name=f"Char{i}", is_deleted=False) for i in range(3)
    ]

    mock_persistence.get_active_players_by_user_id = AsyncMock(return_value=mock_characters)
    mock_persistence.get_player_by_name = AsyncMock(return_value=None)  # Name is available
    mock_persistence.save_player = AsyncMock()

    stats = Stats(
        strength=50,
        dexterity=50,
        constitution=50,
        size=50,
        intelligence=50,
        power=50,
        education=50,
        charisma=50,
        luck=50,
    )

    with pytest.raises(ValidationError) as exc_info:
        await player_service.create_player_with_stats(
            name="NewCharacter",
            stats=stats,
            user_id=user_id,
        )

    assert "limit" in str(exc_info.value).lower() or "maximum" in str(exc_info.value).lower()
    mock_persistence.save_player.assert_not_called()


@pytest.mark.asyncio
async def test_create_player_with_stats_case_insensitive_name_conflict(player_service, mock_persistence):
    """Test that character creation fails with case-insensitive name conflict."""
    user_id = uuid.uuid4()

    from server.models.player import Player

    # Mock existing character with different case
    existing_player = Player(player_id=uuid.uuid4(), user_id=uuid.uuid4(), name="Ithaqua", is_deleted=False)

    mock_persistence.get_active_players_by_user_id = AsyncMock(return_value=[])  # Under limit
    mock_persistence.get_player_by_name = AsyncMock(return_value=existing_player)  # Name conflict (case-insensitive)
    mock_persistence.save_player = AsyncMock()

    stats = Stats(
        strength=50,
        dexterity=50,
        constitution=50,
        size=50,
        intelligence=50,
        power=50,
        education=50,
        charisma=50,
        luck=50,
    )

    with pytest.raises(ValidationError) as exc_info:
        await player_service.create_player_with_stats(
            name="ithaqua",  # Different case
            stats=stats,
            user_id=user_id,
        )

    assert "name" in str(exc_info.value).lower() or "exists" in str(exc_info.value).lower()
    mock_persistence.save_player.assert_not_called()


@pytest.mark.asyncio
async def test_get_user_characters(player_service, mock_persistence):
    """Test retrieving user characters."""
    user_id = uuid.uuid4()

    from server.models.player import Player

    mock_characters = [
        Player(player_id=uuid.uuid4(), user_id=user_id, name="Char1", is_deleted=False),
        Player(player_id=uuid.uuid4(), user_id=user_id, name="Char2", is_deleted=False),
    ]

    mock_persistence.get_active_players_by_user_id = AsyncMock(return_value=mock_characters)

    result = await player_service.get_user_characters(user_id)

    assert len(result) == 2
    assert result[0].name == "Char1"
    assert result[1].name == "Char2"
    mock_persistence.get_active_players_by_user_id.assert_called_once_with(str(user_id))


@pytest.mark.asyncio
async def test_soft_delete_character_success(player_service, mock_persistence):
    """Test successful character soft deletion."""
    user_id = uuid.uuid4()
    character_id = uuid.uuid4()

    from server.models.player import Player

    mock_player = Player(player_id=character_id, user_id=user_id, name="TestChar", is_deleted=False)

    mock_persistence.get_player_by_id = AsyncMock(return_value=mock_player)
    mock_persistence.soft_delete_player = AsyncMock(return_value=True)

    success, message = await player_service.soft_delete_character(character_id, user_id)

    assert success is True
    assert "deleted" in message.lower()
    mock_persistence.soft_delete_player.assert_called_once_with(character_id)


@pytest.mark.asyncio
async def test_soft_delete_character_wrong_user(player_service, mock_persistence):
    """Test that soft deletion fails if character doesn't belong to user."""
    user_id = uuid.uuid4()
    other_user_id = uuid.uuid4()
    character_id = uuid.uuid4()

    from server.models.player import Player

    mock_player = Player(player_id=character_id, user_id=other_user_id, name="TestChar", is_deleted=False)

    mock_persistence.get_player_by_id = AsyncMock(return_value=mock_player)

    with pytest.raises(ValidationError) as exc_info:
        await player_service.soft_delete_character(character_id, user_id)

    assert "belong" in str(exc_info.value).lower() or "own" in str(exc_info.value).lower()
    mock_persistence.soft_delete_player.assert_not_called()
