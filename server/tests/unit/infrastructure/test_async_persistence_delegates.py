"""
Unit tests for async persistence layer: health, container, item, singleton, constants.

Part of split from test_async_persistence.py to satisfy file-nloc limit.
"""

# pylint: disable=protected-access  # Reason: Test file - accessing protected members for unit testing
# pylint: disable=redefined-outer-name  # Reason: pytest fixture parameter names must match fixture names

import uuid
from datetime import UTC, datetime
from typing import Any
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from server.async_persistence import (
    PLAYER_COLUMNS,
    PROFESSION_COLUMNS,
    get_async_persistence,
    reset_async_persistence,
)
from server.models.player import Player


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
    mock_containers: list[dict[str, Any]] = [{"container_id": str(uuid.uuid4())}, {"container_id": str(uuid.uuid4())}]
    async_persistence_layer._container_repo.get_containers_by_room_id = AsyncMock(return_value=mock_containers)

    result = await async_persistence_layer.get_containers_by_room_id("test_room")

    assert result == mock_containers
    async_persistence_layer._container_repo.get_containers_by_room_id.assert_awaited_once_with("test_room")


@pytest.mark.asyncio
async def test_get_containers_by_entity_id_delegates(async_persistence_layer):
    """Test get_containers_by_entity_id delegates to ContainerRepository."""
    entity_id = uuid.uuid4()
    mock_containers: list[dict[str, Any]] = [{"container_id": str(uuid.uuid4())}]
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
    mock_containers: list[dict[str, Any]] = [{"container_id": str(uuid.uuid4())}]
    async_persistence_layer._container_repo.get_decayed_containers = AsyncMock(return_value=mock_containers)

    result = await async_persistence_layer.get_decayed_containers(current_time)

    assert result == mock_containers
    async_persistence_layer._container_repo.get_decayed_containers.assert_awaited_once_with(current_time)


@pytest.mark.asyncio
async def test_get_decayed_containers_none_time(async_persistence_layer):
    """Test get_decayed_containers with None time."""
    mock_containers: list[Any] = []
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
        {"owner_type": "room", "owner_id": "room_1"},
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
    reset_async_persistence()

    with patch("server.async_persistence.AsyncPersistenceLayer") as mock_class:
        mock_instance = MagicMock()
        mock_class.return_value = mock_instance

        result1 = get_async_persistence()
        result2 = get_async_persistence()

        assert result1 == mock_instance
        assert result2 == mock_instance
        assert mock_class.call_count == 1


def test_get_async_persistence_returns_same_instance():
    """Test get_async_persistence returns same instance on multiple calls."""
    reset_async_persistence()

    with patch("server.async_persistence.AsyncPersistenceLayer") as mock_class:
        mock_instance = MagicMock()
        mock_class.return_value = mock_instance

        instance1 = get_async_persistence()
        instance2 = get_async_persistence()

        assert instance1 is instance2


def test_reset_async_persistence():
    """Test reset_async_persistence resets the singleton."""
    reset_async_persistence()

    with patch("server.async_persistence.AsyncPersistenceLayer") as mock_class:
        mock_instance = MagicMock()
        mock_class.return_value = mock_instance

        _instance1 = get_async_persistence()
        reset_async_persistence()
        _instance2 = get_async_persistence()

        assert mock_class.call_count == 2


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
    async_persistence_layer._ensure_room_cache_loaded = AsyncMock()
    user_id = str(uuid.uuid4())
    mock_player = MagicMock(spec=Player)
    async_persistence_layer._player_repo.get_player_by_user_id = AsyncMock(return_value=mock_player)

    result = await async_persistence_layer.get_player_by_user_id(user_id)

    assert result == mock_player
    async_persistence_layer._player_repo.get_player_by_user_id.assert_awaited_once_with(user_id)
