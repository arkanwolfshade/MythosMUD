"""
Unit tests for async persistence layer: init, close, player, user, room, profession.

Part of split from test_async_persistence.py to satisfy file-nloc limit.
"""

# pylint: disable=protected-access  # Reason: Test file - accessing protected members for unit testing
# pylint: disable=redefined-outer-name  # Reason: pytest fixture parameter names must match fixture names

import uuid
from datetime import UTC, datetime
from typing import Any
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from server.async_persistence import AsyncPersistenceLayer
from server.exceptions import DatabaseError
from server.models.player import Player
from server.models.profession import Profession
from server.models.user import User


def test_async_persistence_layer_init_skip_room_cache(mock_event_bus):
    """Test AsyncPersistenceLayer initialization with skipped room cache."""
    layer = AsyncPersistenceLayer(event_bus=mock_event_bus, _skip_room_cache=True)

    assert layer._event_bus == mock_event_bus
    assert not layer._room_cache
    assert layer._room_repo is not None
    assert layer._player_repo is not None
    assert layer._profession_repo is not None
    assert layer._experience_repo is not None
    assert layer._health_repo is not None
    assert layer._container_repo is not None
    assert layer._item_repo is not None


def test_async_persistence_layer_init_with_room_cache(mock_event_bus):
    """Test AsyncPersistenceLayer initialization - room cache is now loaded lazily, not during init."""
    layer = AsyncPersistenceLayer(event_bus=mock_event_bus, _skip_room_cache=False)

    assert layer._event_bus == mock_event_bus
    assert not layer._room_cache
    assert layer._room_cache_loaded is False


def test_async_persistence_layer_init_deprecated_params(mock_event_bus):
    """Test AsyncPersistenceLayer initialization with deprecated parameters."""
    layer = AsyncPersistenceLayer(
        _db_path="test.db",
        _log_path="test.log",
        event_bus=mock_event_bus,
        _skip_room_cache=True,
    )

    assert layer._event_bus == mock_event_bus


@pytest.mark.asyncio
async def test_close(async_persistence_layer):
    """Test close method (no-op for backward compatibility)."""
    await async_persistence_layer.close()


@pytest.mark.asyncio
async def test_get_player_by_name_delegates(async_persistence_layer):
    """Test get_player_by_name delegates to PlayerRepository."""
    async_persistence_layer._ensure_room_cache_loaded = AsyncMock()
    mock_player = MagicMock(spec=Player)
    async_persistence_layer._player_repo.get_player_by_name = AsyncMock(return_value=mock_player)

    result = await async_persistence_layer.get_player_by_name("TestPlayer")

    assert result == mock_player
    async_persistence_layer._player_repo.get_player_by_name.assert_awaited_once_with("TestPlayer")


@pytest.mark.asyncio
async def test_get_player_by_name_not_found(async_persistence_layer):
    """Test get_player_by_name when player not found."""
    async_persistence_layer._ensure_room_cache_loaded = AsyncMock()
    async_persistence_layer._player_repo.get_player_by_name = AsyncMock(return_value=None)

    result = await async_persistence_layer.get_player_by_name("NonExistent")

    assert result is None


@pytest.mark.asyncio
async def test_get_player_by_id_delegates(async_persistence_layer):
    """Test get_player_by_id delegates to PlayerRepository."""
    async_persistence_layer._ensure_room_cache_loaded = AsyncMock()
    player_id = uuid.uuid4()
    mock_player = MagicMock(spec=Player)
    async_persistence_layer._player_repo.get_player_by_id = AsyncMock(return_value=mock_player)

    result = await async_persistence_layer.get_player_by_id(player_id)

    assert result == mock_player
    async_persistence_layer._player_repo.get_player_by_id.assert_awaited_once_with(player_id)


@pytest.mark.asyncio
async def test_get_players_by_user_id_delegates(async_persistence_layer):
    """Test get_players_by_user_id delegates to PlayerRepository."""
    async_persistence_layer._ensure_room_cache_loaded = AsyncMock()
    user_id = str(uuid.uuid4())
    mock_players: list[Any] = [MagicMock(spec=Player), MagicMock(spec=Player)]
    async_persistence_layer._player_repo.get_players_by_user_id = AsyncMock(return_value=mock_players)

    result = await async_persistence_layer.get_players_by_user_id(user_id)

    assert result == mock_players
    async_persistence_layer._player_repo.get_players_by_user_id.assert_awaited_once_with(user_id)


@pytest.mark.asyncio
async def test_get_active_players_by_user_id_delegates(async_persistence_layer):
    """Test get_active_players_by_user_id delegates to PlayerRepository."""
    async_persistence_layer._ensure_room_cache_loaded = AsyncMock()
    user_id = str(uuid.uuid4())
    mock_players: list[Any] = [MagicMock(spec=Player)]
    async_persistence_layer._player_repo.get_active_players_by_user_id = AsyncMock(return_value=mock_players)

    result = await async_persistence_layer.get_active_players_by_user_id(user_id)

    assert result == mock_players
    async_persistence_layer._player_repo.get_active_players_by_user_id.assert_awaited_once_with(user_id)


@pytest.mark.asyncio
async def test_get_user_by_username_case_insensitive_success(async_persistence_layer):
    """Test get_user_by_username_case_insensitive with successful lookup."""
    user_id = str(uuid.uuid4())
    mock_user = User(
        id=user_id,
        username="TestUser",
        email="test@example.com",
        hashed_password="hashed",
        is_active=True,
        is_superuser=False,
        is_verified=True,
    )

    mock_session = AsyncMock()
    mock_result = MagicMock()
    mock_result.scalar_one_or_none = MagicMock(return_value=mock_user)
    mock_session.execute = AsyncMock(return_value=mock_result)

    async def mock_get_async_session():
        yield mock_session

    with patch("server.async_persistence_direct_queries.get_async_session", side_effect=mock_get_async_session):
        result = await async_persistence_layer.get_user_by_username_case_insensitive("testuser")

    assert result == mock_user
    mock_session.execute.assert_awaited_once()


@pytest.mark.asyncio
async def test_get_user_by_username_case_insensitive_not_found(async_persistence_layer):
    """Test get_user_by_username_case_insensitive when user not found."""
    mock_session = AsyncMock()
    mock_result = MagicMock()
    mock_result.scalar_one_or_none = MagicMock(return_value=None)
    mock_session.execute = AsyncMock(return_value=mock_result)

    async def mock_get_async_session():
        yield mock_session

    with patch("server.async_persistence_direct_queries.get_async_session", side_effect=mock_get_async_session):
        result = await async_persistence_layer.get_user_by_username_case_insensitive("nonexistent")

    assert result is None


@pytest.mark.asyncio
async def test_get_user_by_username_case_insensitive_database_error(async_persistence_layer):
    """Test get_user_by_username_case_insensitive with database error."""
    from sqlalchemy.exc import SQLAlchemyError

    mock_session = AsyncMock()
    mock_session.execute = AsyncMock(side_effect=SQLAlchemyError("DB error", None, None))

    async def mock_get_async_session():
        yield mock_session

    with patch("server.async_persistence_direct_queries.get_async_session", side_effect=mock_get_async_session):
        with pytest.raises(DatabaseError, match="Database error retrieving user"):
            await async_persistence_layer.get_user_by_username_case_insensitive("testuser")


@pytest.mark.asyncio
async def test_save_player_delegates(async_persistence_layer):
    """Test save_player delegates to PlayerRepository."""
    mock_player = MagicMock(spec=Player)
    async_persistence_layer._player_repo.save_player = AsyncMock()

    await async_persistence_layer.save_player(mock_player)

    async_persistence_layer._player_repo.save_player.assert_awaited_once_with(mock_player)


@pytest.mark.asyncio
async def test_list_players_delegates(async_persistence_layer):
    """Test list_players delegates to PlayerRepository."""
    async_persistence_layer._ensure_room_cache_loaded = AsyncMock()
    mock_players: list[Any] = [MagicMock(spec=Player), MagicMock(spec=Player)]
    async_persistence_layer._player_repo.list_players = AsyncMock(return_value=mock_players)

    result = await async_persistence_layer.list_players()

    assert result == mock_players
    async_persistence_layer._player_repo.list_players.assert_awaited_once()


def test_get_room_by_id_delegates(async_persistence_layer):
    """Test get_room_by_id delegates to RoomRepository."""
    mock_room = MagicMock()
    async_persistence_layer._room_repo.get_room_by_id = MagicMock(return_value=mock_room)

    result = async_persistence_layer.get_room_by_id("test_room_id")

    assert result == mock_room
    async_persistence_layer._room_repo.get_room_by_id.assert_called_once_with("test_room_id")


def test_get_room_by_id_not_found(async_persistence_layer):
    """Test get_room_by_id when room not found."""
    async_persistence_layer._room_repo.get_room_by_id = MagicMock(return_value=None)

    result = async_persistence_layer.get_room_by_id("nonexistent_room")

    assert result is None


def test_list_rooms_delegates(async_persistence_layer):
    """Test list_rooms delegates to RoomRepository."""
    mock_rooms = [MagicMock(), MagicMock()]
    async_persistence_layer._room_repo.list_rooms = MagicMock(return_value=mock_rooms)

    result = async_persistence_layer.list_rooms()

    assert result == mock_rooms
    async_persistence_layer._room_repo.list_rooms.assert_called_once()


@pytest.mark.asyncio
async def test_async_list_rooms_delegates(async_persistence_layer):
    """Test async_list_rooms delegates to RoomRepository."""
    mock_rooms = [MagicMock(), MagicMock()]
    async_persistence_layer._room_repo.list_rooms = MagicMock(return_value=mock_rooms)

    result = await async_persistence_layer.async_list_rooms()

    assert result == mock_rooms
    async_persistence_layer._room_repo.list_rooms.assert_called_once()


@pytest.mark.asyncio
async def test_get_players_in_room_delegates(async_persistence_layer):
    """Test get_players_in_room delegates to PlayerRepository."""
    async_persistence_layer._ensure_room_cache_loaded = AsyncMock()
    mock_players: list[Any] = [MagicMock(spec=Player)]
    async_persistence_layer._player_repo.get_players_in_room = AsyncMock(return_value=mock_players)

    result = await async_persistence_layer.get_players_in_room("test_room_id")

    assert result == mock_players
    async_persistence_layer._player_repo.get_players_in_room.assert_awaited_once_with("test_room_id")


@pytest.mark.asyncio
async def test_save_players_delegates(async_persistence_layer):
    """Test save_players delegates to PlayerRepository."""
    mock_players: list[Any] = [MagicMock(spec=Player), MagicMock(spec=Player)]
    async_persistence_layer._player_repo.save_players = AsyncMock()

    await async_persistence_layer.save_players(mock_players)

    async_persistence_layer._player_repo.save_players.assert_awaited_once_with(mock_players)


@pytest.mark.asyncio
async def test_delete_player_delegates(async_persistence_layer):
    """Test delete_player delegates to PlayerRepository."""
    player_id = uuid.uuid4()
    async_persistence_layer._player_repo.delete_player = AsyncMock(return_value=True)

    result = await async_persistence_layer.delete_player(player_id)

    assert result is True
    async_persistence_layer._player_repo.delete_player.assert_awaited_once_with(player_id)


@pytest.mark.asyncio
async def test_update_player_last_active_delegates(async_persistence_layer):
    """Test update_player_last_active delegates to PlayerRepository."""
    player_id = uuid.uuid4()
    last_active = datetime.now(UTC)
    async_persistence_layer._player_repo.update_player_last_active = AsyncMock()

    await async_persistence_layer.update_player_last_active(player_id, last_active)

    async_persistence_layer._player_repo.update_player_last_active.assert_awaited_once_with(player_id, last_active)


@pytest.mark.asyncio
async def test_update_player_last_active_none(async_persistence_layer):
    """Test update_player_last_active with None timestamp."""
    player_id = uuid.uuid4()
    async_persistence_layer._player_repo.update_player_last_active = AsyncMock()

    await async_persistence_layer.update_player_last_active(player_id, None)

    async_persistence_layer._player_repo.update_player_last_active.assert_awaited_once_with(player_id, None)


@pytest.mark.asyncio
async def test_get_professions_success(async_persistence_layer):
    """Test get_professions with successful query."""
    mock_profession1 = MagicMock(spec=Profession)
    mock_profession1.id = 1
    mock_profession2 = MagicMock(spec=Profession)
    mock_profession2.id = 2

    mock_session = AsyncMock()
    mock_result = MagicMock()
    mock_result.scalars = MagicMock(
        return_value=MagicMock(all=MagicMock(return_value=[mock_profession1, mock_profession2]))
    )
    mock_session.execute = AsyncMock(return_value=mock_result)

    async def mock_get_async_session():
        yield mock_session

    with patch("server.async_persistence_direct_queries.get_async_session", side_effect=mock_get_async_session):
        result = await async_persistence_layer.get_professions()

    assert len(result) == 2
    assert result[0] == mock_profession1
    assert result[1] == mock_profession2
    mock_session.execute.assert_awaited_once()


@pytest.mark.asyncio
async def test_get_professions_empty(async_persistence_layer):
    """Test get_professions when no professions found."""
    mock_session = AsyncMock()
    mock_result = MagicMock()
    mock_result.scalars = MagicMock(return_value=MagicMock(all=MagicMock(return_value=[])))
    mock_session.execute = AsyncMock(return_value=mock_result)

    async def mock_get_async_session():
        yield mock_session

    with patch("server.async_persistence_direct_queries.get_async_session", side_effect=mock_get_async_session):
        result = await async_persistence_layer.get_professions()

    assert not result
    mock_session.execute.assert_awaited_once()


@pytest.mark.asyncio
async def test_get_professions_database_error(async_persistence_layer):
    """Test get_professions with database error."""
    from sqlalchemy.exc import SQLAlchemyError

    mock_session = AsyncMock()
    mock_session.execute = AsyncMock(side_effect=SQLAlchemyError("DB error", None, None))

    async def mock_get_async_session():
        yield mock_session

    with patch("server.async_persistence_direct_queries.get_async_session", side_effect=mock_get_async_session):
        with pytest.raises(DatabaseError, match="Database error retrieving professions"):
            await async_persistence_layer.get_professions()


@pytest.mark.asyncio
async def test_get_professions_os_error(async_persistence_layer):
    """Test get_professions with OSError."""
    mock_session = AsyncMock()
    mock_session.execute = AsyncMock(side_effect=OSError("Connection error"))

    async def mock_get_async_session():
        yield mock_session

    with patch("server.async_persistence_direct_queries.get_async_session", side_effect=mock_get_async_session):
        with pytest.raises(DatabaseError, match="Database error retrieving professions"):
            await async_persistence_layer.get_professions()


@pytest.mark.asyncio
async def test_get_profession_by_id_delegates(async_persistence_layer):
    """Test get_profession_by_id delegates to ProfessionRepository."""
    mock_profession = MagicMock(spec=Profession)
    async_persistence_layer._profession_repo.get_profession_by_id = AsyncMock(return_value=mock_profession)

    result = await async_persistence_layer.get_profession_by_id(1)

    assert result == mock_profession
    async_persistence_layer._profession_repo.get_profession_by_id.assert_awaited_once_with(1)


@pytest.mark.asyncio
async def test_get_profession_by_id_not_found(async_persistence_layer):
    """Test get_profession_by_id when profession not found."""
    async_persistence_layer._profession_repo.get_profession_by_id = AsyncMock(return_value=None)

    result = await async_persistence_layer.get_profession_by_id(999)

    assert result is None
