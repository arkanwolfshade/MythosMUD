"""
Unit tests for wearable container service.

Tests the WearableContainerService class for managing wearable container operations.
"""

import uuid
from unittest.mock import AsyncMock, MagicMock

import pytest

from server.services.wearable_container_service import (
    WearableContainerService,
    WearableContainerServiceError,
)

# pylint: disable=protected-access  # Reason: Test file - accessing protected members is standard practice for unit testing
# pylint: disable=redefined-outer-name  # Reason: Test file - pytest fixture parameter names must match fixture names, causing intentional redefinitions


@pytest.fixture
def mock_persistence():
    """Create mock persistence layer."""
    persistence = MagicMock()
    persistence.get_containers_by_entity_id = AsyncMock(return_value=[])
    persistence.create_container = MagicMock(return_value={"container_id": str(uuid.uuid4())})
    return persistence


@pytest.fixture
def wearable_service(mock_persistence):
    """Create WearableContainerService instance."""
    return WearableContainerService(mock_persistence)


def test_wearable_container_service_init_no_persistence():
    """Test WearableContainerService raises error when persistence is None."""
    with pytest.raises(ValueError, match="required"):
        WearableContainerService(None)


def test_wearable_container_service_init(wearable_service, mock_persistence):
    """Test WearableContainerService initialization."""
    assert wearable_service.persistence == mock_persistence


@pytest.mark.asyncio
async def test_handle_equip_wearable_container_no_inner_container(wearable_service):
    """Test handle_equip_wearable_container returns None when no inner_container."""
    item_stack = {"item_id": "item_001"}
    result = await wearable_service.handle_equip_wearable_container(uuid.uuid4(), item_stack)
    assert result is None


@pytest.mark.asyncio
async def test_handle_equip_wearable_container_existing(wearable_service, mock_persistence):
    """Test handle_equip_wearable_container returns existing container."""
    player_id = uuid.uuid4()
    item_instance_id = "item_instance_001"
    container_id = uuid.uuid4()
    existing_container = {
        "container_id": str(container_id),
        "source_type": "equipment",
        "metadata": {"item_instance_id": item_instance_id},
    }
    mock_persistence.get_containers_by_entity_id = AsyncMock(return_value=[existing_container])
    item_stack = {
        "item_id": "item_001",
        "item_instance_id": item_instance_id,
        "inner_container": {"capacity_slots": 10, "items": []},
    }
    result = await wearable_service.handle_equip_wearable_container(player_id, item_stack)
    assert result is not None
    assert result["container_id"] == container_id


@pytest.mark.asyncio
async def test_handle_equip_wearable_container_creates_new(wearable_service, mock_persistence):
    """Test handle_equip_wearable_container creates new container."""
    player_id = uuid.uuid4()
    new_container_id = uuid.uuid4()
    mock_persistence.create_container = MagicMock(return_value={"container_id": str(new_container_id)})
    item_stack = {
        "item_id": "item_001",
        "item_instance_id": "item_instance_001",
        "inner_container": {"capacity_slots": 10, "items": []},
    }
    result = await wearable_service.handle_equip_wearable_container(player_id, item_stack)
    assert result is not None
    assert result["container_id"] == new_container_id
    mock_persistence.create_container.assert_called_once()


@pytest.mark.asyncio
async def test_handle_equip_wearable_container_capacity_exceeded(wearable_service):
    """Test handle_equip_wearable_container raises error when capacity exceeded."""
    player_id = uuid.uuid4()
    item_stack = {
        "item_id": "item_001",
        "item_instance_id": "item_instance_001",
        "inner_container": {"capacity_slots": 5, "items": [1, 2, 3, 4, 5, 6]},  # 6 items > 5 capacity
    }
    with pytest.raises(WearableContainerServiceError, match="capacity exceeded"):
        await wearable_service.handle_equip_wearable_container(player_id, item_stack)


@pytest.mark.asyncio
async def test_handle_unequip_wearable_container_no_item_instance(wearable_service):
    """Test handle_unequip_wearable_container returns None when no item_instance_id."""
    item_stack = {"item_id": "item_001"}
    result = await wearable_service.handle_unequip_wearable_container(uuid.uuid4(), item_stack)
    assert result is None


@pytest.mark.asyncio
async def test_handle_unequip_wearable_container_preserves(wearable_service, mock_persistence):
    """Test handle_unequip_wearable_container preserves container."""
    player_id = uuid.uuid4()
    item_instance_id = "item_instance_001"
    container_id = uuid.uuid4()
    existing_container = {
        "container_id": str(container_id),
        "source_type": "equipment",
        "entity_id": str(player_id),  # Required for equipment containers
        "capacity_slots": 10,
        "items": [{"item_id": "item_001"}],
        "lock_state": "unlocked",
        "metadata": {"item_instance_id": item_instance_id},
    }
    mock_persistence.get_containers_by_entity_id = AsyncMock(return_value=[existing_container])
    item_stack = {"item_instance_id": item_instance_id}
    result = await wearable_service.handle_unequip_wearable_container(player_id, item_stack)
    assert result is not None
    assert "inner_container" in result


@pytest.mark.asyncio
async def test_handle_unequip_wearable_container_not_found(wearable_service, mock_persistence):
    """Test handle_unequip_wearable_container returns None when container not found."""
    player_id = uuid.uuid4()
    mock_persistence.get_containers_by_entity_id = AsyncMock(return_value=[])
    item_stack = {"item_instance_id": "nonexistent"}
    result = await wearable_service.handle_unequip_wearable_container(player_id, item_stack)
    assert result is None


@pytest.mark.asyncio
async def test_get_wearable_containers_for_player(wearable_service, mock_persistence):
    """Test get_wearable_containers_for_player returns containers."""
    player_id = uuid.uuid4()
    container_data = {
        "container_id": str(uuid.uuid4()),
        "source_type": "equipment",
        "capacity_slots": 10,
        "items": [],
        "lock_state": "unlocked",
    }
    mock_persistence.get_containers_by_entity_id = AsyncMock(return_value=[container_data])
    result = await wearable_service.get_wearable_containers_for_player(player_id)
    assert isinstance(result, list)


@pytest.mark.asyncio
async def test_get_wearable_containers_for_player_empty(wearable_service, mock_persistence):
    """Test get_wearable_containers_for_player returns empty list when no containers."""
    player_id = uuid.uuid4()
    mock_persistence.get_containers_by_entity_id = AsyncMock(return_value=[])
    result = await wearable_service.get_wearable_containers_for_player(player_id)
    assert result == []


@pytest.mark.asyncio
async def test_get_wearable_containers_for_player_error(wearable_service, mock_persistence):
    """Test get_wearable_containers_for_player handles errors gracefully."""
    player_id = uuid.uuid4()
    container_data = {"source_type": "equipment", "invalid": "data"}
    mock_persistence.get_containers_by_entity_id = AsyncMock(return_value=[container_data])
    result = await wearable_service.get_wearable_containers_for_player(player_id)
    # Should return empty list or skip invalid containers
    assert isinstance(result, list)


@pytest.mark.asyncio
async def test_add_items_to_wearable_container(wearable_service, mock_persistence):
    """Test add_items_to_wearable_container adds items."""
    player_id = uuid.uuid4()
    container_id = uuid.uuid4()
    container_data = {
        "container_id": str(container_id),
        "source_type": "equipment",
        "entity_id": str(player_id),
        "capacity_slots": 10,
        "items": [],
        "lock_state": "unlocked",
    }
    mock_persistence.get_container = AsyncMock(return_value=container_data)
    mock_persistence.update_container = MagicMock(
        return_value={"container_id": str(container_id), "items": [{"item_id": "item_001"}]}
    )
    items = [{"item_id": "item_001"}]
    result = await wearable_service.add_items_to_wearable_container(player_id, container_id, items)
    assert result is not None


@pytest.mark.asyncio
async def test_add_items_to_wearable_container_not_found(wearable_service, mock_persistence):
    """Test add_items_to_wearable_container raises error when container not found."""
    player_id = uuid.uuid4()
    container_id = uuid.uuid4()
    mock_persistence.get_container = AsyncMock(return_value=None)
    items = [{"item_id": "item_001"}]
    with pytest.raises(WearableContainerServiceError, match="not found"):
        await wearable_service.add_items_to_wearable_container(player_id, container_id, items)


@pytest.mark.asyncio
async def test_add_items_to_wearable_container_capacity_exceeded(wearable_service, mock_persistence):
    """Test add_items_to_wearable_container raises error when capacity exceeded."""
    player_id = uuid.uuid4()
    container_id = uuid.uuid4()
    container_data = {
        "container_id": str(container_id),
        "source_type": "equipment",
        "entity_id": str(player_id),
        "capacity_slots": 2,
        "items": [{"item_id": "item_001"}, {"item_id": "item_002"}],
        "lock_state": "unlocked",
    }
    mock_persistence.get_container = AsyncMock(return_value=container_data)
    items = [{"item_id": "item_003"}]  # Would exceed capacity
    with pytest.raises(WearableContainerServiceError, match="capacity exceeded"):
        await wearable_service.add_items_to_wearable_container(player_id, container_id, items)


@pytest.mark.asyncio
async def test_update_wearable_container_items(wearable_service, mock_persistence):
    """Test update_wearable_container_items updates items."""
    player_id = uuid.uuid4()
    container_id = uuid.uuid4()
    container_data = {
        "container_id": str(container_id),
        "source_type": "equipment",
        "entity_id": str(player_id),
        "capacity_slots": 10,
        "items": [],
        "lock_state": "unlocked",
    }
    mock_persistence.get_container = AsyncMock(return_value=container_data)
    mock_persistence.update_container = MagicMock(
        return_value={"container_id": str(container_id), "items": [{"item_id": "item_001"}]}
    )
    items = [{"item_id": "item_001"}]
    result = await wearable_service.update_wearable_container_items(player_id, container_id, items)
    assert result is not None


@pytest.mark.asyncio
async def test_handle_container_overflow(wearable_service, mock_persistence):
    """Test handle_container_overflow handles overflow."""
    player_id = uuid.uuid4()
    container_id = uuid.uuid4()
    mock_player = MagicMock()
    mock_player.inventory = []
    mock_player.current_room_id = "room_001"
    mock_player.set_inventory = MagicMock()
    mock_persistence.get_player_by_id = AsyncMock(return_value=mock_player)
    mock_persistence.save_player = AsyncMock()
    mock_persistence.create_container = MagicMock()
    overflow_items = [{"item_id": "item_001"}]
    result = await wearable_service.handle_container_overflow(player_id, container_id, overflow_items)
    assert isinstance(result, dict)
    assert "spilled_items" in result


@pytest.mark.asyncio
async def test_handle_container_overflow_player_not_found(wearable_service, mock_persistence):
    """Test handle_container_overflow raises error when player not found."""
    player_id = uuid.uuid4()
    container_id = uuid.uuid4()
    mock_persistence.get_player_by_id = AsyncMock(return_value=None)
    overflow_items = [{"item_id": "item_001"}]
    with pytest.raises(WearableContainerServiceError, match="not found"):
        await wearable_service.handle_container_overflow(player_id, container_id, overflow_items)


@pytest.mark.asyncio
async def test_handle_container_overflow_inventory_full(wearable_service, mock_persistence):
    """Test handle_container_overflow drops to ground when inventory full."""
    player_id = uuid.uuid4()
    container_id = uuid.uuid4()
    mock_player = MagicMock()
    # Fill inventory to max capacity (20 slots)
    mock_player.inventory = [{"item_id": f"item_{i}"} for i in range(20)]
    mock_player.current_room_id = "room_001"
    mock_player.set_inventory = MagicMock()
    mock_persistence.get_player_by_id = AsyncMock(return_value=mock_player)
    mock_persistence.save_player = AsyncMock()
    mock_persistence.create_container = MagicMock()
    overflow_items = [{"item_id": "overflow_item"}]
    result = await wearable_service.handle_container_overflow(player_id, container_id, overflow_items)
    assert isinstance(result, dict)
    assert len(result["spilled_items"]) == 0
    assert len(result["ground_items"]) == 1
    mock_persistence.create_container.assert_called_once()


@pytest.mark.asyncio
async def test_handle_container_overflow_no_room_id(wearable_service, mock_persistence):
    """Test handle_container_overflow handles player without room_id."""
    player_id = uuid.uuid4()
    container_id = uuid.uuid4()
    mock_player = MagicMock()
    mock_player.inventory = []
    # No current_room_id attribute
    if hasattr(mock_player, "current_room_id"):
        delattr(mock_player, "current_room_id")
    mock_persistence.get_player_by_id = AsyncMock(return_value=mock_player)
    mock_persistence.save_player = AsyncMock()
    overflow_items = [{"item_id": "item_001"}]
    result = await wearable_service.handle_container_overflow(player_id, container_id, overflow_items)
    assert isinstance(result, dict)
    # Should add to inventory, not create ground container (no room_id)


@pytest.mark.asyncio
async def test_handle_container_overflow_ground_container_error(wearable_service, mock_persistence):
    """Test handle_container_overflow handles ground container creation error."""
    player_id = uuid.uuid4()
    container_id = uuid.uuid4()
    mock_player = MagicMock()
    mock_player.inventory = [{"item_id": f"item_{i}"} for i in range(20)]  # Full
    mock_player.current_room_id = "room_001"
    mock_persistence.get_player_by_id = AsyncMock(return_value=mock_player)
    mock_persistence.create_container = MagicMock(side_effect=Exception("Container creation failed"))
    overflow_items = [{"item_id": "overflow_item"}]
    # Should not raise, just log error
    result = await wearable_service.handle_container_overflow(player_id, container_id, overflow_items)
    assert isinstance(result, dict)


@pytest.mark.asyncio
async def test_handle_equip_wearable_container_creation_error(wearable_service, mock_persistence):
    """Test handle_equip_wearable_container handles container creation error."""
    player_id = uuid.uuid4()
    mock_persistence.get_containers_by_entity_id = AsyncMock(return_value=[])
    mock_persistence.create_container = MagicMock(side_effect=Exception("Creation failed"))
    item_stack = {
        "item_id": "item_001",
        "item_instance_id": "item_instance_001",
        "inner_container": {"capacity_slots": 10, "items": []},
    }
    with pytest.raises(WearableContainerServiceError, match="Failed to create"):
        await wearable_service.handle_equip_wearable_container(player_id, item_stack)


@pytest.mark.asyncio
async def test_handle_equip_wearable_container_with_lock_state(wearable_service, mock_persistence):
    """Test handle_equip_wearable_container with lock_state and allowed_roles."""
    player_id = uuid.uuid4()
    new_container_id = uuid.uuid4()
    mock_persistence.create_container = MagicMock(return_value={"container_id": str(new_container_id)})
    item_stack = {
        "item_id": "item_001",
        "item_instance_id": "item_instance_001",
        "inner_container": {
            "capacity_slots": 10,
            "items": [],
            "lock_state": "locked",
            "allowed_roles": ["admin"],
        },
    }
    result = await wearable_service.handle_equip_wearable_container(player_id, item_stack)
    assert result is not None
    # Verify create_container was called with lock_state and allowed_roles
    call_kwargs = mock_persistence.create_container.call_args[1]
    assert call_kwargs["lock_state"] == "locked"
    assert call_kwargs["allowed_roles"] == ["admin"]


@pytest.mark.asyncio
async def test_handle_unequip_wearable_container_with_allowed_roles(wearable_service, mock_persistence):
    """Test handle_unequip_wearable_container preserves allowed_roles."""
    player_id = uuid.uuid4()
    item_instance_id = "item_instance_001"
    container_id = uuid.uuid4()
    existing_container = {
        "container_id": str(container_id),
        "source_type": "equipment",
        "entity_id": str(player_id),  # Required for equipment containers
        "capacity_slots": 10,
        "items": [{"item_id": "item_001"}],
        "lock_state": "unlocked",
        "allowed_roles": ["admin", "moderator"],
        "metadata": {"item_instance_id": item_instance_id},
    }
    mock_persistence.get_containers_by_entity_id = AsyncMock(return_value=[existing_container])
    item_stack = {"item_instance_id": item_instance_id}
    result = await wearable_service.handle_unequip_wearable_container(player_id, item_stack)
    assert result is not None
    assert "allowed_roles" in result["inner_container"]
    assert result["inner_container"]["allowed_roles"] == ["admin", "moderator"]


@pytest.mark.asyncio
async def test_add_items_to_wearable_container_wrong_player(wearable_service, mock_persistence):
    """Test add_items_to_wearable_container raises error when container belongs to different player."""
    player_id = uuid.uuid4()
    other_player_id = uuid.uuid4()
    container_id = uuid.uuid4()
    container_data = {
        "container_id": str(container_id),
        "source_type": "equipment",
        "entity_id": str(other_player_id),  # Different player
        "capacity_slots": 10,
        "items": [],
        "lock_state": "unlocked",
    }
    mock_persistence.get_container = AsyncMock(return_value=container_data)
    items = [{"item_id": "item_001"}]
    with pytest.raises(WearableContainerServiceError, match="not a wearable container"):
        await wearable_service.add_items_to_wearable_container(player_id, container_id, items)


@pytest.mark.asyncio
async def test_add_items_to_wearable_container_wrong_source_type(wearable_service, mock_persistence):
    """Test add_items_to_wearable_container raises error when container is not equipment."""
    player_id = uuid.uuid4()
    container_id = uuid.uuid4()
    container_data = {
        "container_id": str(container_id),
        "source_type": "environment",  # Not equipment
        "room_id": "room_001",  # Required for environment containers
        "capacity_slots": 10,
        "items": [],
        "lock_state": "unlocked",
    }
    mock_persistence.get_container = AsyncMock(return_value=container_data)
    items = [{"item_id": "item_001"}]
    with pytest.raises(WearableContainerServiceError, match="not a wearable container"):
        await wearable_service.add_items_to_wearable_container(player_id, container_id, items)


@pytest.mark.asyncio
async def test_add_items_to_wearable_container_update_fails(wearable_service, mock_persistence):
    """Test add_items_to_wearable_container raises error when update fails."""
    player_id = uuid.uuid4()
    container_id = uuid.uuid4()
    container_data = {
        "container_id": str(container_id),
        "source_type": "equipment",
        "entity_id": str(player_id),
        "capacity_slots": 10,
        "items": [],
        "lock_state": "unlocked",
    }
    mock_persistence.get_container = AsyncMock(return_value=container_data)
    mock_persistence.update_container = MagicMock(return_value=None)  # Update fails
    items = [{"item_id": "item_001"}]
    with pytest.raises(WearableContainerServiceError, match="Failed to update"):
        await wearable_service.add_items_to_wearable_container(player_id, container_id, items)


@pytest.mark.asyncio
async def test_update_wearable_container_items_not_found(wearable_service, mock_persistence):
    """Test update_wearable_container_items raises error when container not found."""
    player_id = uuid.uuid4()
    container_id = uuid.uuid4()
    mock_persistence.get_container = AsyncMock(return_value=None)
    items = [{"item_id": "item_001"}]
    with pytest.raises(WearableContainerServiceError, match="not found"):
        await wearable_service.update_wearable_container_items(player_id, container_id, items)


@pytest.mark.asyncio
async def test_update_wearable_container_items_capacity_exceeded(wearable_service, mock_persistence):
    """Test update_wearable_container_items raises error when capacity exceeded."""
    player_id = uuid.uuid4()
    container_id = uuid.uuid4()
    container_data = {
        "container_id": str(container_id),
        "source_type": "equipment",
        "entity_id": str(player_id),
        "capacity_slots": 5,
        "items": [],
        "lock_state": "unlocked",
    }
    mock_persistence.get_container = AsyncMock(return_value=container_data)
    items = [{"item_id": f"item_{i}"} for i in range(6)]  # 6 items > 5 capacity
    with pytest.raises(WearableContainerServiceError, match="capacity exceeded"):
        await wearable_service.update_wearable_container_items(player_id, container_id, items)


@pytest.mark.asyncio
async def test_update_wearable_container_items_update_fails(wearable_service, mock_persistence):
    """Test update_wearable_container_items raises error when update fails."""
    player_id = uuid.uuid4()
    container_id = uuid.uuid4()
    container_data = {
        "container_id": str(container_id),
        "source_type": "equipment",
        "entity_id": str(player_id),
        "capacity_slots": 10,
        "items": [],
        "lock_state": "unlocked",
    }
    mock_persistence.get_container = AsyncMock(return_value=container_data)
    mock_persistence.update_container = MagicMock(return_value=None)
    items = [{"item_id": "item_001"}]
    with pytest.raises(WearableContainerServiceError, match="Failed to update"):
        await wearable_service.update_wearable_container_items(player_id, container_id, items)


def test_get_enum_value_with_enum():
    """Test _get_enum_value returns value from enum instance."""
    from server.models.container import ContainerSourceType
    from server.services.wearable_container_service import _get_enum_value

    result = _get_enum_value(ContainerSourceType.EQUIPMENT)
    assert isinstance(result, str)


def test_get_enum_value_with_string():
    """Test _get_enum_value returns string value unchanged."""
    from server.services.wearable_container_service import _get_enum_value

    result = _get_enum_value("equipment")
    assert result == "equipment"


def test_filter_container_data():
    """Test _filter_container_data filters database-only fields."""
    from server.services.wearable_container_service import _filter_container_data

    container_data = {
        "container_id": str(uuid.uuid4()),
        "capacity_slots": 10,
        "created_at": "2024-01-01",
        "updated_at": "2024-01-02",
    }
    filtered = _filter_container_data(container_data)
    assert "created_at" not in filtered
    assert "updated_at" not in filtered
    assert "container_id" in filtered


@pytest.mark.asyncio
async def test_handle_equip_wearable_container_existing_id_uuid(wearable_service, mock_persistence):
    """Test handle_equip_wearable_container when existing_id is already UUID."""
    player_id = uuid.uuid4()
    item_instance_id = "item_instance_001"
    container_id = uuid.uuid4()
    existing_container = {
        "container_id": container_id,  # Already UUID, not string
        "source_type": "equipment",
        "metadata": {"item_instance_id": item_instance_id},
    }
    mock_persistence.get_containers_by_entity_id = AsyncMock(return_value=[existing_container])
    item_stack = {
        "item_id": "item_001",
        "item_instance_id": item_instance_id,
        "inner_container": {"capacity_slots": 10, "items": []},
    }
    result = await wearable_service.handle_equip_wearable_container(player_id, item_stack)
    assert result is not None
    assert result["container_id"] == container_id


@pytest.mark.asyncio
async def test_handle_equip_wearable_container_filters_non_equipment(wearable_service, mock_persistence):
    """Test handle_equip_wearable_container filters out non-equipment containers."""
    player_id = uuid.uuid4()
    item_instance_id = "item_instance_001"
    environment_container = {
        "container_id": str(uuid.uuid4()),
        "source_type": "environment",  # Not equipment
        "metadata": {"item_instance_id": item_instance_id},
    }
    mock_persistence.get_containers_by_entity_id = AsyncMock(return_value=[environment_container])
    new_container_id = uuid.uuid4()
    mock_persistence.create_container = MagicMock(return_value={"container_id": str(new_container_id)})
    item_stack = {
        "item_id": "item_001",
        "item_instance_id": item_instance_id,
        "inner_container": {"capacity_slots": 10, "items": []},
    }
    # Should create new container since environment container doesn't match
    result = await wearable_service.handle_equip_wearable_container(player_id, item_stack)
    assert result is not None
    assert result["container_id"] == new_container_id
    mock_persistence.create_container.assert_called_once()


@pytest.mark.asyncio
async def test_handle_unequip_wearable_container_no_allowed_roles(wearable_service, mock_persistence):
    """Test handle_unequip_wearable_container when container has no allowed_roles."""
    player_id = uuid.uuid4()
    item_instance_id = "item_instance_001"
    container_id = uuid.uuid4()
    existing_container = {
        "container_id": str(container_id),
        "source_type": "equipment",
        "entity_id": str(player_id),
        "capacity_slots": 10,
        "items": [{"item_id": "item_001"}],
        "lock_state": "unlocked",
        "metadata": {"item_instance_id": item_instance_id},
        # No allowed_roles field
    }
    mock_persistence.get_containers_by_entity_id = AsyncMock(return_value=[existing_container])
    item_stack = {"item_instance_id": item_instance_id}
    result = await wearable_service.handle_unequip_wearable_container(player_id, item_stack)
    assert result is not None
    assert "inner_container" in result
    # Should not have allowed_roles when not present
    assert "allowed_roles" not in result["inner_container"]


@pytest.mark.asyncio
async def test_add_items_to_wearable_container_non_dict_items(wearable_service, mock_persistence):
    """Test add_items_to_wearable_container handles non-dict items."""
    player_id = uuid.uuid4()
    container_id = uuid.uuid4()
    container_data = {
        "container_id": str(container_id),
        "source_type": "equipment",
        "entity_id": str(player_id),
        "capacity_slots": 10,
        "items": [{"item_id": "item_001"}],
        "lock_state": "unlocked",
    }
    mock_persistence.get_container = AsyncMock(return_value=container_data)

    # Mock item objects (not dicts) that can be converted
    # The code does: dict(item) if not isinstance(item, dict) else item
    # So we need an object that can be converted to dict
    class MockItem:
        """Mock item class that can be converted to dict for testing."""

        def __init__(self):
            self.item_id = "item_002"

        def __iter__(self):
            return iter([("item_id", "item_002")])

    items = [MockItem()]  # Non-dict item that can be converted to dict
    mock_persistence.update_container = MagicMock(
        return_value={"container_id": str(container_id), "items": [{"item_id": "item_001"}, {"item_id": "item_002"}]}
    )
    result = await wearable_service.add_items_to_wearable_container(player_id, container_id, items)
    assert result is not None
    mock_persistence.update_container.assert_called_once()


@pytest.mark.asyncio
async def test_handle_container_overflow_partial_spill(wearable_service, mock_persistence):
    """Test handle_container_overflow handles partial inventory spill."""
    player_id = uuid.uuid4()
    container_id = uuid.uuid4()
    mock_player = MagicMock()
    # Fill inventory to 19 slots (1 space remaining)
    mock_player.inventory = [{"item_id": f"item_{i}"} for i in range(19)]
    mock_player.current_room_id = "room_001"
    mock_player.set_inventory = MagicMock()
    mock_persistence.get_player_by_id = AsyncMock(return_value=mock_player)
    mock_persistence.save_player = AsyncMock()
    mock_persistence.create_container = MagicMock()
    overflow_items = [{"item_id": "spill_1"}, {"item_id": "spill_2"}]  # 2 items, only 1 space
    result = await wearable_service.handle_container_overflow(player_id, container_id, overflow_items)
    assert len(result["spilled_items"]) == 1
    assert len(result["ground_items"]) == 1


@pytest.mark.asyncio
async def test_handle_container_overflow_save_player_error(wearable_service, mock_persistence):
    """Test handle_container_overflow handles save_player error gracefully."""
    player_id = uuid.uuid4()
    container_id = uuid.uuid4()
    mock_player = MagicMock()
    mock_player.inventory = []
    mock_player.current_room_id = "room_001"
    mock_player.set_inventory = MagicMock()
    mock_persistence.get_player_by_id = AsyncMock(return_value=mock_player)
    mock_persistence.save_player = AsyncMock(side_effect=Exception("Save failed"))
    overflow_items = [{"item_id": "item_001"}]
    # Should not raise, just log error
    result = await wearable_service.handle_container_overflow(player_id, container_id, overflow_items)
    assert isinstance(result, dict)


@pytest.mark.asyncio
async def test_handle_container_overflow_empty_overflow(wearable_service, mock_persistence):
    """Test handle_container_overflow handles empty overflow list."""
    player_id = uuid.uuid4()
    container_id = uuid.uuid4()
    mock_player = MagicMock()
    mock_player.inventory = []
    mock_player.current_room_id = "room_001"
    mock_persistence.get_player_by_id = AsyncMock(return_value=mock_player)
    overflow_items = []
    result = await wearable_service.handle_container_overflow(player_id, container_id, overflow_items)
    assert len(result["spilled_items"]) == 0
    assert len(result["ground_items"]) == 0


@pytest.mark.asyncio
async def test_get_wearable_containers_for_player_exception_in_validation(wearable_service, mock_persistence):
    """Test get_wearable_containers_for_player handles validation errors gracefully."""
    player_id = uuid.uuid4()
    # Container data that will fail validation
    invalid_container_data = {
        "source_type": "equipment",
        "container_id": str(uuid.uuid4()),
        "invalid_field": "invalid",  # Missing required fields
    }
    mock_persistence.get_containers_by_entity_id = AsyncMock(return_value=[invalid_container_data])
    # Should not raise, just skip invalid containers
    result = await wearable_service.get_wearable_containers_for_player(player_id)
    assert isinstance(result, list)


@pytest.mark.asyncio
async def test_get_wearable_containers_for_player_multiple_containers(wearable_service, mock_persistence):
    """Test get_wearable_containers_for_player returns multiple containers."""
    player_id = uuid.uuid4()
    container1_data = {
        "container_id": str(uuid.uuid4()),
        "source_type": "equipment",
        "entity_id": str(player_id),
        "capacity_slots": 10,
        "items": [],
        "lock_state": "unlocked",
    }
    container2_data = {
        "container_id": str(uuid.uuid4()),
        "source_type": "equipment",
        "entity_id": str(player_id),
        "capacity_slots": 5,
        "items": [{"item_id": "item_001"}],
        "lock_state": "locked",
    }
    mock_persistence.get_containers_by_entity_id = AsyncMock(return_value=[container1_data, container2_data])
    result = await wearable_service.get_wearable_containers_for_player(player_id)
    assert len(result) == 2


@pytest.mark.asyncio
async def test_get_wearable_containers_for_player_filters_non_equipment(wearable_service, mock_persistence):
    """Test get_wearable_containers_for_player filters out non-equipment containers."""
    player_id = uuid.uuid4()
    equipment_container = {
        "container_id": str(uuid.uuid4()),
        "source_type": "equipment",
        "entity_id": str(player_id),
        "capacity_slots": 10,
        "items": [],
        "lock_state": "unlocked",
    }
    environment_container = {
        "container_id": str(uuid.uuid4()),
        "source_type": "environment",
        "room_id": "room_001",  # Required for environment containers
        "capacity_slots": 20,
        "items": [],
        "lock_state": "unlocked",
    }
    mock_persistence.get_containers_by_entity_id = AsyncMock(return_value=[equipment_container, environment_container])
    result = await wearable_service.get_wearable_containers_for_player(player_id)
    assert len(result) == 1
    # source_type is an enum after validation
    from server.models.container import ContainerSourceType

    assert result[0].source_type == ContainerSourceType.EQUIPMENT


@pytest.mark.asyncio
async def test_handle_unequip_wearable_container_empty_allowed_roles(wearable_service, mock_persistence):
    """Test handle_unequip_wearable_container when allowed_roles is empty list."""
    player_id = uuid.uuid4()
    item_instance_id = "item_instance_001"
    container_id = uuid.uuid4()
    existing_container = {
        "container_id": str(container_id),
        "source_type": "equipment",
        "entity_id": str(player_id),
        "capacity_slots": 10,
        "items": [{"item_id": "item_001"}],
        "lock_state": "unlocked",
        "allowed_roles": [],  # Empty list
        "metadata": {"item_instance_id": item_instance_id},
    }
    mock_persistence.get_containers_by_entity_id = AsyncMock(return_value=[existing_container])
    item_stack = {"item_instance_id": item_instance_id}
    result = await wearable_service.handle_unequip_wearable_container(player_id, item_stack)
    assert result is not None
    assert "inner_container" in result
    # Should not have allowed_roles when empty
    assert "allowed_roles" not in result["inner_container"]


@pytest.mark.asyncio
async def test_add_items_to_wearable_container_dict_items(wearable_service, mock_persistence):
    """Test add_items_to_wearable_container handles dict items correctly."""
    player_id = uuid.uuid4()
    container_id = uuid.uuid4()
    container_data = {
        "container_id": str(container_id),
        "source_type": "equipment",
        "entity_id": str(player_id),
        "capacity_slots": 10,
        "items": [{"item_id": "item_001"}],
        "lock_state": "unlocked",
    }
    mock_persistence.get_container = AsyncMock(return_value=container_data)
    items = [{"item_id": "item_002"}]  # Dict items
    mock_persistence.update_container = MagicMock(
        return_value={"container_id": str(container_id), "items": [{"item_id": "item_001"}, {"item_id": "item_002"}]}
    )
    result = await wearable_service.add_items_to_wearable_container(player_id, container_id, items)
    assert result is not None
    mock_persistence.update_container.assert_called_once()


@pytest.mark.asyncio
async def test_handle_container_overflow_no_spilled_items(wearable_service, mock_persistence):
    """Test handle_container_overflow when no items spill to inventory."""
    player_id = uuid.uuid4()
    container_id = uuid.uuid4()
    mock_player = MagicMock()
    # Fill inventory to max capacity (20 slots)
    mock_player.inventory = [{"item_id": f"item_{i}"} for i in range(20)]
    mock_player.current_room_id = "room_001"
    mock_player.set_inventory = MagicMock()
    mock_persistence.get_player_by_id = AsyncMock(return_value=mock_player)
    mock_persistence.save_player = AsyncMock()
    mock_persistence.create_container = MagicMock()
    overflow_items = [{"item_id": "overflow_1"}, {"item_id": "overflow_2"}]
    result = await wearable_service.handle_container_overflow(player_id, container_id, overflow_items)
    assert len(result["spilled_items"]) == 0
    assert len(result["ground_items"]) == 2
    # Should not save player when no items spilled
    mock_persistence.save_player.assert_not_awaited()


@pytest.mark.asyncio
async def test_handle_container_overflow_spilled_items_save_player(wearable_service, mock_persistence):
    """Test handle_container_overflow saves player when items spill."""
    player_id = uuid.uuid4()
    container_id = uuid.uuid4()
    mock_player = MagicMock()
    mock_player.inventory = []
    mock_player.current_room_id = "room_001"
    mock_player.set_inventory = MagicMock()
    mock_persistence.get_player_by_id = AsyncMock(return_value=mock_player)
    mock_persistence.save_player = AsyncMock()
    mock_persistence.create_container = MagicMock()
    overflow_items = [{"item_id": "spill_1"}]
    result = await wearable_service.handle_container_overflow(player_id, container_id, overflow_items)
    assert len(result["spilled_items"]) == 1
    assert len(result["ground_items"]) == 0
    # Should save player when items spilled
    mock_persistence.save_player.assert_awaited_once()


@pytest.mark.asyncio
async def test_handle_equip_wearable_container_multiple_existing_containers(wearable_service, mock_persistence):
    """Test handle_equip_wearable_container with multiple existing containers."""
    player_id = uuid.uuid4()
    item_instance_id = "item_instance_001"
    container_id = uuid.uuid4()
    other_container_id = uuid.uuid4()
    existing_container = {
        "container_id": str(container_id),
        "source_type": "equipment",
        "metadata": {"item_instance_id": item_instance_id},
    }
    other_container = {
        "container_id": str(other_container_id),
        "source_type": "equipment",
        "metadata": {"item_instance_id": "different_instance"},
    }
    mock_persistence.get_containers_by_entity_id = AsyncMock(return_value=[existing_container, other_container])
    item_stack = {
        "item_id": "item_001",
        "item_instance_id": item_instance_id,
        "inner_container": {"capacity_slots": 10, "items": []},
    }
    result = await wearable_service.handle_equip_wearable_container(player_id, item_stack)
    assert result is not None
    assert result["container_id"] == container_id
    # Should not create new container
    mock_persistence.create_container.assert_not_called()


@pytest.mark.asyncio
async def test_handle_equip_wearable_container_existing_container_no_metadata(wearable_service, mock_persistence):
    """Test handle_equip_wearable_container when existing container has no metadata."""
    player_id = uuid.uuid4()
    item_instance_id = "item_instance_001"
    container_id = uuid.uuid4()
    existing_container = {
        "container_id": str(container_id),
        "source_type": "equipment",
        "metadata": {},  # No item_instance_id
    }
    mock_persistence.get_containers_by_entity_id = AsyncMock(return_value=[existing_container])
    new_container_id = uuid.uuid4()
    mock_persistence.create_container = MagicMock(return_value={"container_id": str(new_container_id)})
    item_stack = {
        "item_id": "item_001",
        "item_instance_id": item_instance_id,
        "inner_container": {"capacity_slots": 10, "items": []},
    }
    # Should create new container since metadata doesn't match
    result = await wearable_service.handle_equip_wearable_container(player_id, item_stack)
    assert result is not None
    assert result["container_id"] == new_container_id
    mock_persistence.create_container.assert_called_once()


@pytest.mark.asyncio
async def test_handle_equip_wearable_container_existing_container_different_item_instance(
    wearable_service, mock_persistence
):
    """Test handle_equip_wearable_container when existing container has different item_instance_id."""
    player_id = uuid.uuid4()
    item_instance_id = "item_instance_001"
    container_id = uuid.uuid4()
    existing_container = {
        "container_id": str(container_id),
        "source_type": "equipment",
        "metadata": {"item_instance_id": "different_instance"},
    }
    mock_persistence.get_containers_by_entity_id = AsyncMock(return_value=[existing_container])
    new_container_id = uuid.uuid4()
    mock_persistence.create_container = MagicMock(return_value={"container_id": str(new_container_id)})
    item_stack = {
        "item_id": "item_001",
        "item_instance_id": item_instance_id,
        "inner_container": {"capacity_slots": 10, "items": []},
    }
    # Should create new container since item_instance_id doesn't match
    result = await wearable_service.handle_equip_wearable_container(player_id, item_stack)
    assert result is not None
    assert result["container_id"] == new_container_id
    mock_persistence.create_container.assert_called_once()


@pytest.mark.asyncio
async def test_handle_container_overflow_room_id_empty_string(wearable_service, mock_persistence):
    """Test handle_container_overflow handles empty string room_id."""
    player_id = uuid.uuid4()
    container_id = uuid.uuid4()
    mock_player = MagicMock()
    mock_player.inventory = [{"item_id": f"item_{i}"} for i in range(20)]  # Full
    mock_player.current_room_id = ""  # Empty string
    mock_persistence.get_player_by_id = AsyncMock(return_value=mock_player)
    mock_persistence.save_player = AsyncMock()
    mock_persistence.create_container = MagicMock()
    overflow_items = [{"item_id": "overflow_item"}]
    result = await wearable_service.handle_container_overflow(player_id, container_id, overflow_items)
    # Should add to inventory since room_id is falsy
    assert isinstance(result, dict)
    # Should not create ground container when room_id is empty
    mock_persistence.create_container.assert_not_called()


@pytest.mark.asyncio
async def test_update_wearable_container_items_wrong_player(wearable_service, mock_persistence):
    """Test update_wearable_container_items raises error when container belongs to different player."""
    player_id = uuid.uuid4()
    other_player_id = uuid.uuid4()
    container_id = uuid.uuid4()
    container_data = {
        "container_id": str(container_id),
        "source_type": "equipment",
        "entity_id": str(other_player_id),  # Different player
        "capacity_slots": 10,
        "items": [],
        "lock_state": "unlocked",
    }
    mock_persistence.get_container = AsyncMock(return_value=container_data)
    items = [{"item_id": "item_001"}]
    with pytest.raises(WearableContainerServiceError, match="not a wearable container"):
        await wearable_service.update_wearable_container_items(player_id, container_id, items)


@pytest.mark.asyncio
async def test_update_wearable_container_items_wrong_source_type(wearable_service, mock_persistence):
    """Test update_wearable_container_items raises error when container is not equipment."""
    player_id = uuid.uuid4()
    container_id = uuid.uuid4()
    container_data = {
        "container_id": str(container_id),
        "source_type": "environment",  # Not equipment
        "room_id": "room_001",  # Required for environment containers
        "capacity_slots": 10,
        "items": [],
        "lock_state": "unlocked",
    }
    mock_persistence.get_container = AsyncMock(return_value=container_data)
    items = [{"item_id": "item_001"}]
    with pytest.raises(WearableContainerServiceError, match="not a wearable container"):
        await wearable_service.update_wearable_container_items(player_id, container_id, items)
