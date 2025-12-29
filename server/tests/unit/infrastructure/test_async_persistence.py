"""
Unit tests for async persistence layer.

Tests the AsyncPersistenceLayer class and related functions.
"""

import uuid
from datetime import UTC, datetime
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from server.async_persistence import (
    PLAYER_COLUMNS,
    PROFESSION_COLUMNS,
    AsyncPersistenceLayer,
    get_async_persistence,
    reset_async_persistence,
)
from server.exceptions import DatabaseError
from server.models.player import Player
from server.models.profession import Profession
from server.models.user import User


@pytest.fixture
def mock_event_bus():
    """Create a mock event bus."""
    return MagicMock()


@pytest.fixture
def async_persistence_layer(mock_event_bus):
    """Create an AsyncPersistenceLayer instance with skipped room cache."""
    return AsyncPersistenceLayer(event_bus=mock_event_bus, _skip_room_cache=True)


def test_async_persistence_layer_init_skip_room_cache(mock_event_bus):
    """Test AsyncPersistenceLayer initialization with skipped room cache."""
    layer = AsyncPersistenceLayer(event_bus=mock_event_bus, _skip_room_cache=True)

    assert layer._event_bus == mock_event_bus
    assert layer._room_cache == {}
    assert layer._room_repo is not None
    assert layer._player_repo is not None
    assert layer._profession_repo is not None
    assert layer._experience_repo is not None
    assert layer._health_repo is not None
    assert layer._container_repo is not None
    assert layer._item_repo is not None


def test_async_persistence_layer_init_with_room_cache(mock_event_bus):
    """Test AsyncPersistenceLayer initialization with room cache loading."""
    with patch.object(AsyncPersistenceLayer, "_load_room_cache") as mock_load:
        _layer = AsyncPersistenceLayer(event_bus=mock_event_bus, _skip_room_cache=False)
        mock_load.assert_called_once()


def test_async_persistence_layer_init_deprecated_params(mock_event_bus):
    """Test AsyncPersistenceLayer initialization with deprecated parameters."""
    layer = AsyncPersistenceLayer(
        _db_path="test.db",
        _log_path="test.log",
        event_bus=mock_event_bus,
        _skip_room_cache=True,
    )

    # Deprecated params should be accepted but not used
    assert layer._event_bus == mock_event_bus


@pytest.mark.asyncio
async def test_close(async_persistence_layer):
    """Test close method (no-op for backward compatibility)."""
    # Should not raise
    await async_persistence_layer.close()


@pytest.mark.asyncio
async def test_get_player_by_name_delegates(async_persistence_layer):
    """Test get_player_by_name delegates to PlayerRepository."""
    mock_player = MagicMock(spec=Player)
    async_persistence_layer._player_repo.get_player_by_name = AsyncMock(return_value=mock_player)

    result = await async_persistence_layer.get_player_by_name("TestPlayer")

    assert result == mock_player
    async_persistence_layer._player_repo.get_player_by_name.assert_awaited_once_with("TestPlayer")


@pytest.mark.asyncio
async def test_get_player_by_name_not_found(async_persistence_layer):
    """Test get_player_by_name when player not found."""
    async_persistence_layer._player_repo.get_player_by_name = AsyncMock(return_value=None)

    result = await async_persistence_layer.get_player_by_name("NonExistent")

    assert result is None


@pytest.mark.asyncio
async def test_get_player_by_id_delegates(async_persistence_layer):
    """Test get_player_by_id delegates to PlayerRepository."""
    player_id = uuid.uuid4()
    mock_player = MagicMock(spec=Player)
    async_persistence_layer._player_repo.get_player_by_id = AsyncMock(return_value=mock_player)

    result = await async_persistence_layer.get_player_by_id(player_id)

    assert result == mock_player
    async_persistence_layer._player_repo.get_player_by_id.assert_awaited_once_with(player_id)


@pytest.mark.asyncio
async def test_get_players_by_user_id_delegates(async_persistence_layer):
    """Test get_players_by_user_id delegates to PlayerRepository."""
    user_id = str(uuid.uuid4())
    mock_players = [MagicMock(spec=Player), MagicMock(spec=Player)]
    async_persistence_layer._player_repo.get_players_by_user_id = AsyncMock(return_value=mock_players)

    result = await async_persistence_layer.get_players_by_user_id(user_id)

    assert result == mock_players
    async_persistence_layer._player_repo.get_players_by_user_id.assert_awaited_once_with(user_id)


@pytest.mark.asyncio
async def test_get_active_players_by_user_id_delegates(async_persistence_layer):
    """Test get_active_players_by_user_id delegates to PlayerRepository."""
    user_id = str(uuid.uuid4())
    mock_players = [MagicMock(spec=Player)]
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

    with patch("server.async_persistence.get_async_session", side_effect=mock_get_async_session):
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

    with patch("server.async_persistence.get_async_session", side_effect=mock_get_async_session):
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

    with patch("server.async_persistence.get_async_session", side_effect=mock_get_async_session):
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
    mock_players = [MagicMock(spec=Player), MagicMock(spec=Player)]
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
    mock_players = [MagicMock(spec=Player)]
    async_persistence_layer._player_repo.get_players_in_room = AsyncMock(return_value=mock_players)

    result = await async_persistence_layer.get_players_in_room("test_room_id")

    assert result == mock_players
    async_persistence_layer._player_repo.get_players_in_room.assert_awaited_once_with("test_room_id")


@pytest.mark.asyncio
async def test_save_players_delegates(async_persistence_layer):
    """Test save_players delegates to PlayerRepository."""
    mock_players = [MagicMock(spec=Player), MagicMock(spec=Player)]
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
    mock_result.scalars = MagicMock(return_value=MagicMock(all=MagicMock(return_value=[mock_profession1, mock_profession2])))
    mock_session.execute = AsyncMock(return_value=mock_result)

    async def mock_get_async_session():
        yield mock_session

    with patch("server.async_persistence.get_async_session", side_effect=mock_get_async_session):
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

    with patch("server.async_persistence.get_async_session", side_effect=mock_get_async_session):
        result = await async_persistence_layer.get_professions()

    assert result == []
    mock_session.execute.assert_awaited_once()


@pytest.mark.asyncio
async def test_get_professions_database_error(async_persistence_layer):
    """Test get_professions with database error."""
    from sqlalchemy.exc import SQLAlchemyError

    mock_session = AsyncMock()
    mock_session.execute = AsyncMock(side_effect=SQLAlchemyError("DB error", None, None))

    async def mock_get_async_session():
        yield mock_session

    with patch("server.async_persistence.get_async_session", side_effect=mock_get_async_session):
        with pytest.raises(DatabaseError, match="Database error retrieving professions"):
            await async_persistence_layer.get_professions()


@pytest.mark.asyncio
async def test_get_professions_os_error(async_persistence_layer):
    """Test get_professions with OSError."""
    mock_session = AsyncMock()
    mock_session.execute = AsyncMock(side_effect=OSError("Connection error"))

    async def mock_get_async_session():
        yield mock_session

    with patch("server.async_persistence.get_async_session", side_effect=mock_get_async_session):
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


def test_validate_and_fix_player_room_delegates(async_persistence_layer):
    """Test validate_and_fix_player_room delegates to PlayerRepository."""
    mock_player = MagicMock(spec=Player)
    async_persistence_layer._player_repo.validate_and_fix_player_room = MagicMock(return_value=True)

    result = async_persistence_layer.validate_and_fix_player_room(mock_player)

    assert result is True
    async_persistence_layer._player_repo.validate_and_fix_player_room.assert_called_once_with(mock_player)


@pytest.mark.asyncio
async def test_apply_lucidity_loss_delegates(async_persistence_layer):
    """Test apply_lucidity_loss delegates to ExperienceRepository."""
    mock_player = MagicMock(spec=Player)
    mock_player.player_id = uuid.uuid4()
    async_persistence_layer._experience_repo.update_player_stat_field = AsyncMock()

    await async_persistence_layer.apply_lucidity_loss(mock_player, 10, "test_source")

    async_persistence_layer._experience_repo.update_player_stat_field.assert_awaited_once_with(
        uuid.UUID(str(mock_player.player_id)),
        "lucidity",
        -10,
        "test_source: lucidity loss",
    )


@pytest.mark.asyncio
async def test_apply_fear_delegates(async_persistence_layer):
    """Test apply_fear delegates to ExperienceRepository."""
    mock_player = MagicMock(spec=Player)
    mock_player.player_id = uuid.uuid4()
    async_persistence_layer._experience_repo.update_player_stat_field = AsyncMock()

    await async_persistence_layer.apply_fear(mock_player, 5, "test_source")

    async_persistence_layer._experience_repo.update_player_stat_field.assert_awaited_once_with(
        uuid.UUID(str(mock_player.player_id)),
        "fear",
        5,
        "test_source: fear increase",
    )


@pytest.mark.asyncio
async def test_apply_corruption_delegates(async_persistence_layer):
    """Test apply_corruption delegates to ExperienceRepository."""
    mock_player = MagicMock(spec=Player)
    mock_player.player_id = uuid.uuid4()
    async_persistence_layer._experience_repo.update_player_stat_field = AsyncMock()

    await async_persistence_layer.apply_corruption(mock_player, 3, "test_source")

    async_persistence_layer._experience_repo.update_player_stat_field.assert_awaited_once_with(
        uuid.UUID(str(mock_player.player_id)),
        "corruption",
        3,
        "test_source: corruption increase",
    )


@pytest.mark.asyncio
async def test_heal_player_delegates(async_persistence_layer):
    """Test heal_player delegates to HealthRepository."""
    mock_player = MagicMock(spec=Player)
    async_persistence_layer._health_repo.heal_player = AsyncMock()

    await async_persistence_layer.heal_player(mock_player, 20)

    async_persistence_layer._health_repo.heal_player.assert_awaited_once_with(mock_player, 20)


@pytest.mark.asyncio
async def test_async_heal_player_delegates(async_persistence_layer):
    """Test async_heal_player delegates to HealthRepository."""
    mock_player = MagicMock(spec=Player)
    async_persistence_layer._health_repo.heal_player = AsyncMock()

    await async_persistence_layer.async_heal_player(mock_player, 20)

    async_persistence_layer._health_repo.heal_player.assert_awaited_once_with(mock_player, 20)


@pytest.mark.asyncio
async def test_damage_player_delegates(async_persistence_layer):
    """Test damage_player delegates to HealthRepository."""
    mock_player = MagicMock(spec=Player)
    async_persistence_layer._health_repo.damage_player = AsyncMock()

    await async_persistence_layer.damage_player(mock_player, 15, "physical")

    async_persistence_layer._health_repo.damage_player.assert_awaited_once_with(mock_player, 15, "physical")


@pytest.mark.asyncio
async def test_async_damage_player_delegates(async_persistence_layer):
    """Test async_damage_player delegates to HealthRepository."""
    mock_player = MagicMock(spec=Player)
    async_persistence_layer._health_repo.damage_player = AsyncMock()

    await async_persistence_layer.async_damage_player(mock_player, 15, "magical")

    async_persistence_layer._health_repo.damage_player.assert_awaited_once_with(mock_player, 15, "magical")


@pytest.mark.asyncio
async def test_create_container_with_params(async_persistence_layer):
    """Test create_container with ContainerCreateParams."""
    from server.persistence.repositories.container_repository import ContainerCreateParams

    params = ContainerCreateParams(
        owner_id=uuid.uuid4(),
        room_id="test_room",
        capacity_slots=10,
    )
    mock_container = {"container_id": str(uuid.uuid4())}
    async_persistence_layer._container_repo.create_container = AsyncMock(return_value=mock_container)

    result = await async_persistence_layer.create_container("room", params=params)

    assert result == mock_container
    async_persistence_layer._container_repo.create_container.assert_awaited_once_with("room", params)


@pytest.mark.asyncio
async def test_create_container_with_kwargs(async_persistence_layer):
    """Test create_container with kwargs (backward compatibility)."""
    from server.persistence.repositories.container_repository import ContainerCreateParams

    mock_container = {"container_id": str(uuid.uuid4())}
    async_persistence_layer._container_repo.create_container = AsyncMock(return_value=mock_container)

    result = await async_persistence_layer.create_container(
        "room",
        owner_id=uuid.uuid4(),
        room_id="test_room",
        capacity_slots=10,
    )

    assert result == mock_container
    # Verify params object was created from kwargs
    call_args = async_persistence_layer._container_repo.create_container.call_args
    assert call_args[0][0] == "room"
    assert isinstance(call_args[0][1], ContainerCreateParams)


@pytest.mark.asyncio
async def test_get_container_delegates(async_persistence_layer):
    """Test get_container delegates to ContainerRepository."""
    container_id = uuid.uuid4()
    mock_container = {"container_id": str(container_id)}
    async_persistence_layer._container_repo.get_container = AsyncMock(return_value=mock_container)

    result = await async_persistence_layer.get_container(container_id)

    assert result == mock_container
    async_persistence_layer._container_repo.get_container.assert_awaited_once_with(container_id)


@pytest.mark.asyncio
async def test_get_containers_by_room_id_delegates(async_persistence_layer):
    """Test get_containers_by_room_id delegates to ContainerRepository."""
    mock_containers = [{"container_id": str(uuid.uuid4())}, {"container_id": str(uuid.uuid4())}]
    async_persistence_layer._container_repo.get_containers_by_room_id = AsyncMock(return_value=mock_containers)

    result = await async_persistence_layer.get_containers_by_room_id("test_room")

    assert result == mock_containers
    async_persistence_layer._container_repo.get_containers_by_room_id.assert_awaited_once_with("test_room")


@pytest.mark.asyncio
async def test_get_containers_by_entity_id_delegates(async_persistence_layer):
    """Test get_containers_by_entity_id delegates to ContainerRepository."""
    entity_id = uuid.uuid4()
    mock_containers = [{"container_id": str(uuid.uuid4())}]
    async_persistence_layer._container_repo.get_containers_by_entity_id = AsyncMock(return_value=mock_containers)

    result = await async_persistence_layer.get_containers_by_entity_id(entity_id)

    assert result == mock_containers
    async_persistence_layer._container_repo.get_containers_by_entity_id.assert_awaited_once_with(entity_id)


@pytest.mark.asyncio
async def test_update_container_delegates(async_persistence_layer):
    """Test update_container delegates to ContainerRepository."""
    container_id = uuid.uuid4()
    items_json = [{"item_id": "test_item"}]
    mock_container = {"container_id": str(container_id), "items": items_json}
    async_persistence_layer._container_repo.update_container = AsyncMock(return_value=mock_container)

    result = await async_persistence_layer.update_container(container_id, items_json=items_json, lock_state="locked")

    assert result == mock_container
    async_persistence_layer._container_repo.update_container.assert_awaited_once_with(
        container_id, items_json, "locked", None
    )


@pytest.mark.asyncio
async def test_get_decayed_containers_delegates(async_persistence_layer):
    """Test get_decayed_containers delegates to ContainerRepository."""
    current_time = datetime.now(UTC)
    mock_containers = [{"container_id": str(uuid.uuid4())}]
    async_persistence_layer._container_repo.get_decayed_containers = AsyncMock(return_value=mock_containers)

    result = await async_persistence_layer.get_decayed_containers(current_time)

    assert result == mock_containers
    async_persistence_layer._container_repo.get_decayed_containers.assert_awaited_once_with(current_time)


@pytest.mark.asyncio
async def test_get_decayed_containers_none_time(async_persistence_layer):
    """Test get_decayed_containers with None time."""
    mock_containers = []
    async_persistence_layer._container_repo.get_decayed_containers = AsyncMock(return_value=mock_containers)

    result = await async_persistence_layer.get_decayed_containers(None)

    assert result == mock_containers
    async_persistence_layer._container_repo.get_decayed_containers.assert_awaited_once_with(None)


@pytest.mark.asyncio
async def test_delete_container_delegates(async_persistence_layer):
    """Test delete_container delegates to ContainerRepository."""
    container_id = uuid.uuid4()
    async_persistence_layer._container_repo.delete_container = AsyncMock(return_value=True)

    result = await async_persistence_layer.delete_container(container_id)

    assert result is True
    async_persistence_layer._container_repo.delete_container.assert_awaited_once_with(container_id)


@pytest.mark.asyncio
async def test_create_item_instance_delegates(async_persistence_layer):
    """Test create_item_instance delegates to ItemRepository."""
    async_persistence_layer._item_repo.create_item_instance = AsyncMock()

    await async_persistence_layer.create_item_instance(
        "item_instance_1",
        "prototype_1",
        owner_type="room",
        owner_id="room_1",
    )

    async_persistence_layer._item_repo.create_item_instance.assert_awaited_once()


@pytest.mark.asyncio
async def test_ensure_item_instance_delegates(async_persistence_layer):
    """Test ensure_item_instance delegates to ItemRepository."""
    async_persistence_layer._item_repo.ensure_item_instance = AsyncMock()

    await async_persistence_layer.ensure_item_instance(
        "item_instance_1",
        "prototype_1",
        owner_type="room",
    )

    async_persistence_layer._item_repo.ensure_item_instance.assert_awaited_once()


@pytest.mark.asyncio
async def test_item_instance_exists_delegates(async_persistence_layer):
    """Test item_instance_exists delegates to ItemRepository."""
    async_persistence_layer._item_repo.item_instance_exists = AsyncMock(return_value=True)

    result = await async_persistence_layer.item_instance_exists("item_instance_1")

    assert result is True
    async_persistence_layer._item_repo.item_instance_exists.assert_awaited_once_with("item_instance_1")


def test_get_async_persistence_creates_instance():
    """Test get_async_persistence creates singleton instance."""
    reset_async_persistence()  # Reset first

    with patch("server.async_persistence.AsyncPersistenceLayer") as mock_class:
        mock_instance = MagicMock()
        mock_class.return_value = mock_instance

        result1 = get_async_persistence()
        result2 = get_async_persistence()

        assert result1 == mock_instance
        assert result2 == mock_instance
        # Should only create one instance
        assert mock_class.call_count == 1


def test_get_async_persistence_returns_same_instance():
    """Test get_async_persistence returns same instance on multiple calls."""
    reset_async_persistence()  # Reset first

    with patch("server.async_persistence.AsyncPersistenceLayer") as mock_class:
        mock_instance = MagicMock()
        mock_class.return_value = mock_instance

        instance1 = get_async_persistence()
        instance2 = get_async_persistence()

        assert instance1 is instance2


def test_reset_async_persistence():
    """Test reset_async_persistence resets the singleton."""
    reset_async_persistence()  # Reset first

    with patch("server.async_persistence.AsyncPersistenceLayer") as mock_class:
        mock_instance = MagicMock()
        mock_class.return_value = mock_instance

        _instance1 = get_async_persistence()
        reset_async_persistence()
        _instance2 = get_async_persistence()

        # Should create new instance after reset
        assert mock_class.call_count == 2
        # But they're the same mock, so we can't test identity
        # Just verify reset doesn't raise


def test_player_columns_constant():
    """Test PLAYER_COLUMNS constant is defined."""
    assert isinstance(PLAYER_COLUMNS, str)
    assert len(PLAYER_COLUMNS) > 0
    assert "player_id" in PLAYER_COLUMNS


def test_profession_columns_constant():
    """Test PROFESSION_COLUMNS constant is defined."""
    assert isinstance(PROFESSION_COLUMNS, str)
    assert len(PROFESSION_COLUMNS) > 0
    assert "id" in PROFESSION_COLUMNS


@pytest.mark.asyncio
async def test_soft_delete_player_delegates(async_persistence_layer):
    """Test soft_delete_player delegates to PlayerRepository."""
    player_id = uuid.uuid4()
    async_persistence_layer._player_repo.soft_delete_player = AsyncMock(return_value=True)

    result = await async_persistence_layer.soft_delete_player(player_id)

    assert result is True
    async_persistence_layer._player_repo.soft_delete_player.assert_awaited_once_with(player_id)


@pytest.mark.asyncio
async def test_get_player_by_user_id_delegates(async_persistence_layer):
    """Test get_player_by_user_id delegates to PlayerRepository."""
    user_id = str(uuid.uuid4())
    mock_player = MagicMock(spec=Player)
    async_persistence_layer._player_repo.get_player_by_user_id = AsyncMock(return_value=mock_player)

    result = await async_persistence_layer.get_player_by_user_id(user_id)

    assert result == mock_player
    async_persistence_layer._player_repo.get_player_by_user_id.assert_awaited_once_with(user_id)

