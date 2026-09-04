"""
Unit tests for player repository.

Tests the PlayerRepository class which handles player persistence operations.
Uses procedure-based persistence; mocks return rows compatible with row_to_player.
"""

import uuid
from datetime import UTC, datetime
from typing import Any
from unittest.mock import AsyncMock, MagicMock, patch

import pytest
from sqlalchemy.exc import SQLAlchemyError

from server.exceptions import DatabaseError
from server.models.player import Player
from server.persistence.repositories.player_repository import PlayerRepository

# pylint: disable=protected-access  # Reason: Test file - accessing protected members is standard practice for unit testing
# pylint: disable=redefined-outer-name  # Reason: Test file - pytest fixture parameter names must match fixture names, causing intentional redefinitions
# pylint: disable=too-many-lines  # Reason: Comprehensive test file for AsyncPersistenceLayer requires extensive test coverage across many scenarios


def _make_mock_row(
    player_id: uuid.UUID | None = None,
    user_id: uuid.UUID | None = None,
    name: str = "TestPlayer",
) -> MagicMock:
    """Create a mock procedure result row for row_to_player."""
    pid = player_id or uuid.uuid4()
    uid = user_id or uuid.uuid4()
    row = MagicMock()
    row.player_id = pid
    row.user_id = uid
    row.name = name
    row.inventory = "[]"
    row.status_effects = "[]"
    row.current_room_id = "earth_arkhamcity_sanitarium_room_foyer_001"
    row.respawn_room_id = "earth_arkhamcity_sanitarium_room_foyer_001"
    row.experience_points = 0
    row.level = 1
    row.is_admin = 0
    row.profession_id = None
    row.created_at = datetime.now(UTC)
    row.last_active = datetime.now(UTC)
    row.stats = {"current_dp": 20, "constitution": 50, "size": 50}
    row.is_deleted = False
    row.deleted_at = None
    row.tutorial_instance_id = None
    row.inventory_json = "[]"
    row.equipped_json = "{}"
    return row


@pytest.fixture
def player_repository():
    """Create a PlayerRepository instance."""
    room_cache = {
        "arkham_square": MagicMock(),
        "room1": MagicMock(),
        "earth_arkhamcity_sanitarium_room_foyer_001": MagicMock(),  # Fallback room
    }
    # Reason: Using MagicMock for Room objects in tests - compatible at runtime
    return PlayerRepository(room_cache=room_cache)  # type: ignore[arg-type]


@pytest.fixture
def mock_player():
    """Create a mock player for save operations."""
    player = MagicMock(spec=Player)
    player.player_id = str(uuid.uuid4())
    player.user_id = str(uuid.uuid4())
    player.name = "TestPlayer"
    player.inventory = "[]"
    player.status_effects = "[]"
    player.current_room_id = "arkham_square"
    player.respawn_room_id = "arkham_square"
    player.experience_points = 0
    player.level = 1
    player.is_admin = 0
    player.profession_id = None
    player.created_at = datetime.now(UTC)
    player.last_active = datetime.now(UTC)
    player.stats = {}
    player.is_deleted = False
    player.deleted_at = None
    player.tutorial_instance_id = None
    player.get_inventory.return_value = []
    player.get_equipped_items.return_value = {}
    player.get_stats.return_value = {"current_dp": 20, "constitution": 50, "size": 50}
    return player


def test_player_repository_initialization():
    """Test PlayerRepository initializes correctly."""
    # PlayerRepository now requires room_cache to not be None
    room_cache: dict[str, Any] = {}
    repo = PlayerRepository(room_cache=room_cache)

    assert repo._room_cache == room_cache
    assert repo._event_bus is None


def test_player_repository_initialization_with_cache():
    """Test PlayerRepository initializes with room cache."""
    room_cache = {"room1": MagicMock(), "room2": MagicMock()}
    # Reason: Using MagicMock for Room objects in tests - compatible at runtime
    repo = PlayerRepository(room_cache=room_cache)  # type: ignore[arg-type]

    assert repo._room_cache == room_cache


def test_player_repository_initialization_with_event_bus():
    """Test PlayerRepository initializes with event bus."""
    # PlayerRepository now requires room_cache to not be None
    room_cache: dict[str, Any] = {}
    event_bus = MagicMock()
    repo = PlayerRepository(room_cache=room_cache, event_bus=event_bus)

    assert repo._room_cache == room_cache
    assert repo._event_bus == event_bus


def test_validate_and_fix_player_room_valid(player_repository, mock_player):
    """Test validate_and_fix_player_room returns False for valid room."""
    mock_player.current_room_id = "arkham_square"

    result = player_repository.validate_and_fix_player_room(mock_player)

    assert result is False
    assert mock_player.current_room_id == "arkham_square"


def test_validate_and_fix_player_room_invalid(player_repository, mock_player):
    """Test validate_and_fix_player_room fixes invalid room."""
    mock_player.current_room_id = "invalid_room"

    result = player_repository.validate_and_fix_player_room(mock_player)

    assert result is True
    assert mock_player.current_room_id == "earth_arkhamcity_sanitarium_room_foyer_001"


@pytest.mark.asyncio
async def test_get_player_by_name_success(player_repository):
    """Test get_player_by_name successfully retrieves player."""
    mock_row = _make_mock_row()
    mock_session = AsyncMock()
    mock_result = MagicMock()
    mock_result.fetchall.return_value = [mock_row]
    mock_session.execute.return_value = mock_result

    with patch("server.persistence.repositories.player_repository.get_session_maker") as mock_get_session:
        mock_get_session.return_value = MagicMock()
        mock_get_session.return_value.return_value.__aenter__ = AsyncMock(return_value=mock_session)
        mock_get_session.return_value.return_value.__aexit__ = AsyncMock(return_value=None)

        result = await player_repository.get_player_by_name("TestPlayer")

        assert result is not None
        assert isinstance(result, Player)
        assert result.name == "TestPlayer"


@pytest.mark.asyncio
async def test_get_player_by_name_not_found(player_repository):
    """Test get_player_by_name returns None when player not found."""
    mock_session = AsyncMock()
    mock_result = MagicMock()
    mock_result.fetchall.return_value = []
    mock_session.execute.return_value = mock_result

    with patch("server.persistence.repositories.player_repository.get_session_maker") as mock_get_session:
        mock_get_session.return_value = MagicMock()
        mock_get_session.return_value.return_value.__aenter__ = AsyncMock(return_value=mock_session)
        mock_get_session.return_value.return_value.__aexit__ = AsyncMock(return_value=None)

        result = await player_repository.get_player_by_name("NonExistent")

        assert result is None


@pytest.mark.asyncio
async def test_get_player_by_name_database_error(player_repository):
    """Test get_player_by_name handles database errors."""
    mock_session = AsyncMock()
    mock_session.execute.side_effect = SQLAlchemyError("Database error")

    with patch("server.persistence.repositories.player_repository.get_session_maker") as mock_get_session:
        mock_get_session.return_value = MagicMock()
        mock_get_session.return_value.return_value.__aenter__ = AsyncMock(return_value=mock_session)
        mock_get_session.return_value.return_value.__aexit__ = AsyncMock(return_value=None)

        with pytest.raises(DatabaseError):
            await player_repository.get_player_by_name("TestPlayer")


@pytest.mark.asyncio
async def test_save_player_success(player_repository, mock_player):
    """Test save_player successfully saves player."""
    mock_session = AsyncMock()
    mock_session.execute = AsyncMock()
    mock_session.commit = AsyncMock()

    with patch("server.persistence.repositories.player_repository.get_session_maker") as mock_get_session:
        mock_get_session.return_value = MagicMock()
        mock_get_session.return_value.return_value.__aenter__ = AsyncMock(return_value=mock_session)
        mock_get_session.return_value.return_value.__aexit__ = AsyncMock(return_value=None)

        await player_repository.save_player(mock_player)

        mock_session.execute.assert_awaited()
        mock_session.commit.assert_awaited_once()


@pytest.mark.asyncio
async def test_save_player_with_bool_is_admin(player_repository, mock_player):
    """Test save_player converts bool is_admin to int."""
    mock_player.is_admin = True
    mock_session = AsyncMock()
    mock_session.execute = AsyncMock()
    mock_session.commit = AsyncMock()

    with patch("server.persistence.repositories.player_repository.get_session_maker") as mock_get_session:
        mock_get_session.return_value = MagicMock()
        mock_get_session.return_value.return_value.__aenter__ = AsyncMock(return_value=mock_session)
        mock_get_session.return_value.return_value.__aexit__ = AsyncMock(return_value=None)

        await player_repository.save_player(mock_player)

        assert mock_player.is_admin == 1


@pytest.mark.asyncio
async def test_save_player_database_error(player_repository, mock_player):
    """Test save_player handles database errors."""
    mock_session = AsyncMock()
    mock_session.execute.side_effect = SQLAlchemyError("Database error")

    with patch("server.persistence.repositories.player_repository.get_session_maker") as mock_get_session:
        mock_get_session.return_value = MagicMock()
        mock_get_session.return_value.return_value.__aenter__ = AsyncMock(return_value=mock_session)
        mock_get_session.return_value.return_value.__aexit__ = AsyncMock(return_value=None)

        with pytest.raises(DatabaseError):
            await player_repository.save_player(mock_player)


@pytest.mark.asyncio
async def test_list_players_success(player_repository):
    """Test list_players successfully retrieves players."""
    mock_row1 = _make_mock_row(name="Player1")
    mock_row2 = _make_mock_row(name="Player2")

    mock_session = AsyncMock()
    mock_result = MagicMock()
    mock_result.fetchall.return_value = [mock_row1, mock_row2]
    mock_session.execute.return_value = mock_result

    with patch("server.persistence.repositories.player_repository.get_session_maker") as mock_get_session:
        mock_get_session.return_value = MagicMock()
        mock_get_session.return_value.return_value.__aenter__ = AsyncMock(return_value=mock_session)
        mock_get_session.return_value.return_value.__aexit__ = AsyncMock(return_value=None)

        result = await player_repository.list_players()

        assert len(result) == 2
        assert result[0].name == "Player1"
        assert result[1].name == "Player2"


@pytest.mark.asyncio
async def test_list_players_empty(player_repository):
    """Test list_players returns empty list when no players."""
    mock_session = AsyncMock()
    mock_result = MagicMock()
    mock_result.fetchall.return_value = []
    mock_session.execute.return_value = mock_result

    with patch("server.persistence.repositories.player_repository.get_session_maker") as mock_get_session:
        mock_get_session.return_value = MagicMock()
        mock_get_session.return_value.return_value.__aenter__ = AsyncMock(return_value=mock_session)
        mock_get_session.return_value.return_value.__aexit__ = AsyncMock(return_value=None)

        result = await player_repository.list_players()

        assert result == []


@pytest.mark.asyncio
async def test_list_players_database_error(player_repository):
    """Test list_players handles database errors."""
    mock_session = AsyncMock()
    mock_session.execute.side_effect = SQLAlchemyError("Database error")

    with patch("server.persistence.repositories.player_repository.get_session_maker") as mock_get_session:
        mock_get_session.return_value = MagicMock()
        mock_get_session.return_value.return_value.__aenter__ = AsyncMock(return_value=mock_session)
        mock_get_session.return_value.return_value.__aexit__ = AsyncMock(return_value=None)

        with pytest.raises(DatabaseError):
            await player_repository.list_players()


@pytest.mark.asyncio
async def test_get_player_by_id_success(player_repository):
    """Test get_player_by_id successfully retrieves player."""
    player_id = uuid.uuid4()
    mock_row = _make_mock_row(player_id=player_id)

    mock_session = AsyncMock()
    mock_result = MagicMock()
    mock_result.fetchall.return_value = [mock_row]
    mock_session.execute.return_value = mock_result

    with patch("server.persistence.repositories.player_repository.get_session_maker") as mock_get_session:
        mock_get_session.return_value = MagicMock()
        mock_get_session.return_value.return_value.__aenter__ = AsyncMock(return_value=mock_session)
        mock_get_session.return_value.return_value.__aexit__ = AsyncMock(return_value=None)

        result = await player_repository.get_player_by_id(player_id)

        assert result is not None
        assert str(result.player_id) == str(player_id)


@pytest.mark.asyncio
async def test_get_player_by_id_not_found(player_repository):
    """Test get_player_by_id returns None when player not found."""
    player_id = uuid.uuid4()

    mock_session = AsyncMock()
    mock_result = MagicMock()
    mock_result.fetchall.return_value = []
    mock_session.execute.return_value = mock_result

    with patch("server.persistence.repositories.player_repository.get_session_maker") as mock_get_session:
        mock_get_session.return_value = MagicMock()
        mock_get_session.return_value.return_value.__aenter__ = AsyncMock(return_value=mock_session)
        mock_get_session.return_value.return_value.__aexit__ = AsyncMock(return_value=None)

        result = await player_repository.get_player_by_id(player_id)

        assert result is None


@pytest.mark.asyncio
async def test_get_players_by_user_id_success(player_repository):
    """Test get_players_by_user_id successfully retrieves players."""
    user_id = uuid.uuid4()
    mock_row1 = _make_mock_row(user_id=user_id, name="Player1")
    mock_row2 = _make_mock_row(user_id=user_id, name="Player2")

    mock_session = AsyncMock()
    mock_result = MagicMock()
    mock_result.fetchall.return_value = [mock_row1, mock_row2]
    mock_session.execute.return_value = mock_result

    with patch("server.persistence.repositories.player_repository.get_session_maker") as mock_get_session:
        mock_get_session.return_value = MagicMock()
        mock_get_session.return_value.return_value.__aenter__ = AsyncMock(return_value=mock_session)
        mock_get_session.return_value.return_value.__aexit__ = AsyncMock(return_value=None)

        result = await player_repository.get_players_by_user_id(str(user_id))

        assert len(result) == 2


@pytest.mark.asyncio
async def test_get_active_players_by_user_id_success(player_repository):
    """Test get_active_players_by_user_id successfully retrieves active players."""
    user_id = uuid.uuid4()
    mock_row = _make_mock_row(user_id=user_id)

    mock_session = AsyncMock()
    mock_result = MagicMock()
    mock_result.fetchall.return_value = [mock_row]
    mock_session.execute.return_value = mock_result

    with patch("server.persistence.repositories.player_repository.get_session_maker") as mock_get_session:
        mock_get_session.return_value = MagicMock()
        mock_get_session.return_value.return_value.__aenter__ = AsyncMock(return_value=mock_session)
        mock_get_session.return_value.return_value.__aexit__ = AsyncMock(return_value=None)

        result = await player_repository.get_active_players_by_user_id(str(user_id))

        assert len(result) == 1


@pytest.mark.asyncio
async def test_get_player_by_user_id_success(player_repository):
    """Test get_player_by_user_id returns first active player."""
    user_id = "user123"
    mock_player = MagicMock(spec=Player)

    with patch.object(player_repository, "get_active_players_by_user_id", return_value=[mock_player]):
        result = await player_repository.get_player_by_user_id(user_id)

        assert result == mock_player


@pytest.mark.asyncio
async def test_get_player_by_user_id_not_found(player_repository):
    """Test get_player_by_user_id returns None when no players."""
    user_id = "user123"

    with patch.object(player_repository, "get_active_players_by_user_id", return_value=[]):
        result = await player_repository.get_player_by_user_id(user_id)

        assert result is None


@pytest.mark.asyncio
async def test_get_players_in_room_success(player_repository):
    """Test get_players_in_room successfully retrieves players."""
    room_id = "arkham_square"
    mock_row = _make_mock_row()
    mock_row.current_room_id = room_id

    mock_session = AsyncMock()
    mock_result = MagicMock()
    mock_result.fetchall.return_value = [mock_row]
    mock_session.execute.return_value = mock_result

    with patch("server.persistence.repositories.player_repository.get_session_maker") as mock_get_session:
        mock_get_session.return_value = MagicMock()
        mock_get_session.return_value.return_value.__aenter__ = AsyncMock(return_value=mock_session)
        mock_get_session.return_value.return_value.__aexit__ = AsyncMock(return_value=None)

        result = await player_repository.get_players_in_room(room_id)

        assert len(result) == 1


@pytest.mark.asyncio
async def test_save_players_success(player_repository, mock_player):
    """Test save_players successfully saves multiple players."""
    mock_player2 = MagicMock(spec=Player)
    mock_player2.is_admin = False
    mock_player2.player_id = str(uuid.uuid4())
    mock_player2.user_id = str(uuid.uuid4())
    mock_player2.name = "Player2"
    mock_player2.inventory = "[]"
    mock_player2.status_effects = "[]"
    mock_player2.current_room_id = "arkham_square"
    mock_player2.respawn_room_id = "arkham_square"
    mock_player2.experience_points = 0
    mock_player2.level = 1
    mock_player2.profession_id = None
    mock_player2.created_at = datetime.now(UTC)
    mock_player2.last_active = datetime.now(UTC)
    mock_player2.stats = {}
    mock_player2.is_deleted = False
    mock_player2.deleted_at = None
    mock_player2.tutorial_instance_id = None
    mock_player2.get_inventory.return_value = []
    mock_player2.get_equipped_items.return_value = {}
    mock_player2.get_stats.return_value = {}
    players: list[Any] = [mock_player, mock_player2]

    mock_session = AsyncMock()
    mock_session.execute = AsyncMock()
    mock_session.commit = AsyncMock()

    with patch("server.persistence.repositories.player_repository.get_session_maker") as mock_get_session:
        mock_get_session.return_value = MagicMock()
        mock_get_session.return_value.return_value.__aenter__ = AsyncMock(return_value=mock_session)
        mock_get_session.return_value.return_value.__aexit__ = AsyncMock(return_value=None)

        await player_repository.save_players(players)

        assert mock_session.execute.await_count == 2
        mock_session.commit.assert_awaited_once()


@pytest.mark.asyncio
async def test_soft_delete_player_success(player_repository):
    """Test soft_delete_player successfully soft deletes player."""
    player_id = uuid.uuid4()

    mock_session = AsyncMock()
    mock_result = MagicMock()
    mock_result.scalar.return_value = True
    mock_session.execute.return_value = mock_result
    mock_session.commit = AsyncMock()

    with patch("server.persistence.repositories.player_repository.get_session_maker") as mock_get_session:
        mock_get_session.return_value = MagicMock()
        mock_get_session.return_value.return_value.__aenter__ = AsyncMock(return_value=mock_session)
        mock_get_session.return_value.return_value.__aexit__ = AsyncMock(return_value=None)

        result = await player_repository.soft_delete_player(player_id)

        assert result is True


@pytest.mark.asyncio
async def test_soft_delete_player_not_found(player_repository):
    """Test soft_delete_player returns False when player not found."""
    player_id = uuid.uuid4()

    mock_session = AsyncMock()
    mock_result = MagicMock()
    mock_result.scalar.return_value = False
    mock_session.execute.return_value = mock_result
    mock_session.commit = AsyncMock()

    with patch("server.persistence.repositories.player_repository.get_session_maker") as mock_get_session:
        mock_get_session.return_value = MagicMock()
        mock_get_session.return_value.return_value.__aenter__ = AsyncMock(return_value=mock_session)
        mock_get_session.return_value.return_value.__aexit__ = AsyncMock(return_value=None)

        result = await player_repository.soft_delete_player(player_id)

        assert result is False


@pytest.mark.asyncio
async def test_delete_player_success(player_repository):
    """Test delete_player successfully deletes player."""
    player_id = uuid.uuid4()

    mock_session = AsyncMock()
    mock_result = MagicMock()
    mock_result.scalar.return_value = True
    mock_session.execute.return_value = mock_result
    mock_session.commit = AsyncMock()

    with patch("server.persistence.repositories.player_repository.get_session_maker") as mock_get_session:
        mock_get_session.return_value = MagicMock()
        mock_get_session.return_value.return_value.__aenter__ = AsyncMock(return_value=mock_session)
        mock_get_session.return_value.return_value.__aexit__ = AsyncMock(return_value=None)

        result = await player_repository.delete_player(player_id)

        assert result is True
        mock_session.execute.assert_awaited()
        mock_session.commit.assert_awaited_once()


@pytest.mark.asyncio
async def test_delete_player_not_found(player_repository):
    """Test delete_player returns False when player not found."""
    player_id = uuid.uuid4()

    mock_session = AsyncMock()
    mock_result = MagicMock()
    mock_result.scalar.return_value = False
    mock_session.execute.return_value = mock_result
    mock_session.commit = AsyncMock()

    with patch("server.persistence.repositories.player_repository.get_session_maker") as mock_get_session:
        mock_get_session.return_value = MagicMock()
        mock_get_session.return_value.return_value.__aenter__ = AsyncMock(return_value=mock_session)
        mock_get_session.return_value.return_value.__aexit__ = AsyncMock(return_value=None)

        result = await player_repository.delete_player(player_id)

        assert result is False


@pytest.mark.asyncio
async def test_update_player_last_active_success(player_repository):
    """Test update_player_last_active successfully updates timestamp."""
    player_id = uuid.uuid4()

    mock_session = AsyncMock()
    mock_session.execute = AsyncMock()
    mock_session.commit = AsyncMock()

    with patch("server.persistence.repositories.player_repository.get_session_maker") as mock_get_session:
        mock_get_session.return_value = MagicMock()
        mock_get_session.return_value.return_value.__aenter__ = AsyncMock(return_value=mock_session)
        mock_get_session.return_value.return_value.__aexit__ = AsyncMock(return_value=None)

        await player_repository.update_player_last_active(player_id)

        mock_session.execute.assert_awaited_once()
        mock_session.commit.assert_awaited_once()


@pytest.mark.asyncio
async def test_update_player_last_active_with_timestamp(player_repository):
    """Test update_player_last_active with provided timestamp."""
    player_id = uuid.uuid4()
    last_active = datetime.now(UTC)

    mock_session = AsyncMock()
    mock_session.execute = AsyncMock()
    mock_session.commit = AsyncMock()

    with patch("server.persistence.repositories.player_repository.get_session_maker") as mock_get_session:
        mock_get_session.return_value = MagicMock()
        mock_get_session.return_value.return_value.__aenter__ = AsyncMock(return_value=mock_session)
        mock_get_session.return_value.return_value.__aexit__ = AsyncMock(return_value=None)

        await player_repository.update_player_last_active(player_id, last_active)

        mock_session.execute.assert_awaited_once()
        mock_session.commit.assert_awaited_once()


@pytest.mark.asyncio
async def test_get_players_batch_success(player_repository):
    """Test get_players_batch successfully retrieves multiple players."""
    player_ids = [uuid.uuid4(), uuid.uuid4()]
    mock_row1 = _make_mock_row(player_id=player_ids[0], name="Player1")
    mock_row2 = _make_mock_row(player_id=player_ids[1], name="Player2")

    mock_session = AsyncMock()
    mock_result = MagicMock()
    mock_result.fetchall.return_value = [mock_row1, mock_row2]
    mock_session.execute.return_value = mock_result

    with patch("server.persistence.repositories.player_repository.get_session_maker") as mock_get_session:
        mock_get_session.return_value = MagicMock()
        mock_get_session.return_value.return_value.__aenter__ = AsyncMock(return_value=mock_session)
        mock_get_session.return_value.return_value.__aexit__ = AsyncMock(return_value=None)

        result = await player_repository.get_players_batch(player_ids)

        assert len(result) == 2
