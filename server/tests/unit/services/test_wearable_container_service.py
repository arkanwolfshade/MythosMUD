"""
Tests for wearable container service.

This module tests the WearableContainerService class and its methods for managing
wearable container operations including equip/unequip, item management, and overflow handling.
"""

from unittest.mock import AsyncMock, MagicMock, patch
from uuid import uuid4

import pytest

from server.models.container import ContainerSourceType
from server.services.wearable_container_service import (
    WearableContainerService,
    WearableContainerServiceError,
    _filter_container_data,
    _get_enum_value,
)


class TestGetEnumValue:
    """Test _get_enum_value helper function."""

    def test_get_enum_value_with_enum(self):
        """Test getting enum value from enum instance."""
        result = _get_enum_value(ContainerSourceType.EQUIPMENT)
        assert result == "equipment"

    def test_get_enum_value_with_string(self):
        """Test getting enum value from string."""
        result = _get_enum_value("environment")
        assert result == "environment"


class TestFilterContainerData:
    """Test _filter_container_data helper function."""

    def test_filter_container_data_removes_timestamps(self):
        """Test that created_at and updated_at are removed."""
        container_data = {
            "container_id": str(uuid4()),
            "items": [],
            "created_at": "2024-01-01T00:00:00Z",
            "updated_at": "2024-01-01T00:00:00Z",
        }

        result = _filter_container_data(container_data)

        assert "created_at" not in result
        assert "updated_at" not in result
        assert "container_id" in result

    def test_filter_container_data_preserves_other_fields(self):
        """Test that other fields are preserved."""
        container_data = {
            "container_id": str(uuid4()),
            "items": [],
            "capacity_slots": 10,
            "source_type": "equipment",
        }

        result = _filter_container_data(container_data)

        assert result["container_id"] == container_data["container_id"]
        assert result["capacity_slots"] == 10
        assert result["source_type"] == "equipment"


class TestWearableContainerServiceInit:
    """Test WearableContainerService initialization."""

    def test_wearable_container_service_init_with_persistence(self):
        """Test initialization with persistence provided."""
        mock_persistence = MagicMock()

        service = WearableContainerService(persistence=mock_persistence)

        assert service.persistence == mock_persistence

    def test_wearable_container_service_init_without_persistence(self):
        """Test initialization without persistence raises error."""
        with pytest.raises(ValueError, match="persistence.*required"):
            WearableContainerService(persistence=None)


class TestHandleEquipWearableContainer:
    """Test handle_equip_wearable_container method."""

    @pytest.mark.asyncio
    async def test_handle_equip_no_inner_container(self):
        """Test equipping item without inner container."""
        mock_persistence = MagicMock()
        service = WearableContainerService(persistence=mock_persistence)

        item_stack = {"item_id": "item-1"}

        result = await service.handle_equip_wearable_container(uuid4(), item_stack)

        assert result is None

    @pytest.mark.asyncio
    async def test_handle_equip_capacity_exceeded(self):
        """Test equipping container with capacity exceeded."""
        mock_persistence = MagicMock()
        service = WearableContainerService(persistence=mock_persistence)

        item_stack = {
            "item_id": "item-1",
            "inner_container": {
                "capacity_slots": 5,
                "items": [{"item_id": f"item-{i}"} for i in range(10)],  # 10 items > 5 capacity
            },
        }

        with pytest.raises(WearableContainerServiceError, match="Container capacity exceeded"):
            await service.handle_equip_wearable_container(uuid4(), item_stack)

    @pytest.mark.asyncio
    async def test_handle_equip_existing_container(self):
        """Test equipping item with existing container."""
        mock_persistence = AsyncMock()
        player_id = uuid4()
        item_instance_id = str(uuid4())

        existing_container = {
            "container_id": str(uuid4()),
            "source_type": "equipment",
            "metadata": {"item_instance_id": item_instance_id},
        }
        mock_persistence.get_containers_by_entity_id.return_value = [existing_container]

        service = WearableContainerService(persistence=mock_persistence)

        item_stack = {
            "item_id": "item-1",
            "item_instance_id": item_instance_id,
            "inner_container": {"capacity_slots": 10, "items": []},
        }

        result = await service.handle_equip_wearable_container(player_id, item_stack)

        assert result is not None
        assert "container_id" in result

    @pytest.mark.asyncio
    async def test_handle_equip_create_new_container(self):
        """Test creating new container on equip."""
        mock_persistence = MagicMock()
        player_id = uuid4()
        item_instance_id = str(uuid4())

        mock_persistence.get_containers_by_entity_id = AsyncMock(return_value=[])
        mock_persistence.create_container.return_value = {"container_id": str(uuid4())}

        service = WearableContainerService(persistence=mock_persistence)

        item_stack = {
            "item_id": "item-1",
            "item_name": "Test Item",
            "item_instance_id": item_instance_id,
            "inner_container": {"capacity_slots": 10, "items": [], "lock_state": "unlocked"},
        }

        with patch("server.services.wearable_container_service.logger"):
            result = await service.handle_equip_wearable_container(player_id, item_stack)

            assert result is not None
            assert "container_id" in result
            mock_persistence.create_container.assert_called_once()


class TestHandleUnequipWearableContainer:
    """Test handle_unequip_wearable_container method."""

    @pytest.mark.asyncio
    async def test_handle_unequip_no_item_instance_id(self):
        """Test unequipping item without item_instance_id."""
        mock_persistence = MagicMock()
        service = WearableContainerService(persistence=mock_persistence)

        item_stack = {"item_id": "item-1"}

        result = await service.handle_unequip_wearable_container(uuid4(), item_stack)

        assert result is None

    @pytest.mark.asyncio
    async def test_handle_unequip_container_found(self):
        """Test unequipping item with existing container."""
        mock_persistence = AsyncMock()
        player_id = uuid4()
        item_instance_id = str(uuid4())
        container_id = uuid4()

        existing_container = {
            "container_id": str(container_id),
            "source_type": "equipment",
            "entity_id": player_id,
            "capacity_slots": 10,
            "items": [{"item_id": "item-1"}],
            "lock_state": "unlocked",
            "allowed_roles": [],
            "room_id": None,
            "owner_id": None,
            "metadata": {"item_instance_id": item_instance_id},
        }
        mock_persistence.get_containers_by_entity_id.return_value = [existing_container]

        service = WearableContainerService(persistence=mock_persistence)

        item_stack = {"item_instance_id": item_instance_id}

        with patch("server.services.wearable_container_service.logger"):
            result = await service.handle_unequip_wearable_container(player_id, item_stack)

            assert result is not None
            assert "inner_container" in result
            assert result["inner_container"]["capacity_slots"] == 10

    @pytest.mark.asyncio
    async def test_handle_unequip_no_container(self):
        """Test unequipping item with no container."""
        mock_persistence = AsyncMock()
        mock_persistence.get_containers_by_entity_id.return_value = []

        service = WearableContainerService(persistence=mock_persistence)

        item_stack = {"item_instance_id": str(uuid4())}

        result = await service.handle_unequip_wearable_container(uuid4(), item_stack)

        assert result is None


class TestGetWearableContainersForPlayer:
    """Test get_wearable_containers_for_player method."""

    @pytest.mark.asyncio
    async def test_get_wearable_containers_success(self):
        """Test getting wearable containers for player."""
        mock_persistence = AsyncMock()
        player_id = uuid4()

        container_data = {
            "container_id": str(uuid4()),
            "source_type": "equipment",
            "entity_id": player_id,
            "capacity_slots": 10,
            "items": [],
            "lock_state": "unlocked",
        }
        mock_persistence.get_containers_by_entity_id.return_value = [container_data]

        service = WearableContainerService(persistence=mock_persistence)

        result = await service.get_wearable_containers_for_player(player_id)

        assert len(result) == 1
        assert result[0].source_type == ContainerSourceType.EQUIPMENT

    @pytest.mark.asyncio
    async def test_get_wearable_containers_no_containers(self):
        """Test getting containers when none exist."""
        mock_persistence = AsyncMock()
        mock_persistence.get_containers_by_entity_id.return_value = []

        service = WearableContainerService(persistence=mock_persistence)

        result = await service.get_wearable_containers_for_player(uuid4())

        assert result == []

    @pytest.mark.asyncio
    async def test_get_wearable_containers_filters_non_equipment(self):
        """Test that non-equipment containers are filtered out."""
        mock_persistence = AsyncMock()

        container_data = {
            "container_id": str(uuid4()),
            "source_type": "environment",  # Not equipment
            "capacity_slots": 10,
            "items": [],
        }
        mock_persistence.get_containers_by_entity_id.return_value = [container_data]

        service = WearableContainerService(persistence=mock_persistence)

        result = await service.get_wearable_containers_for_player(uuid4())

        assert len(result) == 0


class TestAddItemsToWearableContainer:
    """Test add_items_to_wearable_container method."""

    @pytest.mark.asyncio
    async def test_add_items_success(self):
        """Test successfully adding items to container."""
        mock_persistence = AsyncMock()
        player_id = uuid4()
        container_id = uuid4()

        container_data = {
            "container_id": str(container_id),
            "source_type": "equipment",
            "entity_id": player_id,
            "capacity_slots": 10,
            "items": [{"item_id": "item-1"}],
        }
        mock_persistence.get_container.return_value = container_data
        mock_persistence.update_container.return_value = {"container_id": str(container_id), "items": []}

        service = WearableContainerService(persistence=mock_persistence)

        new_items = [{"item_id": "item-2"}]

        with patch("server.services.wearable_container_service.logger"):
            result = await service.add_items_to_wearable_container(player_id, container_id, new_items)

            assert result is not None
            mock_persistence.update_container.assert_called_once()

    @pytest.mark.asyncio
    async def test_add_items_container_not_found(self):
        """Test adding items when container doesn't exist."""
        mock_persistence = AsyncMock()
        mock_persistence.get_container.return_value = None

        service = WearableContainerService(persistence=mock_persistence)

        with pytest.raises(WearableContainerServiceError, match="Container not found"):
            await service.add_items_to_wearable_container(uuid4(), uuid4(), [])

    @pytest.mark.asyncio
    async def test_add_items_capacity_exceeded(self):
        """Test adding items when capacity would be exceeded."""
        mock_persistence = AsyncMock()
        player_id = uuid4()
        container_id = uuid4()

        container_data = {
            "container_id": str(container_id),
            "source_type": "equipment",
            "entity_id": player_id,
            "capacity_slots": 5,
            "items": [{"item_id": f"item-{i}"} for i in range(5)],  # Already full
        }
        mock_persistence.get_container.return_value = container_data

        service = WearableContainerService(persistence=mock_persistence)

        new_items = [{"item_id": "item-6"}]

        with pytest.raises(WearableContainerServiceError, match="Container capacity exceeded"):
            await service.add_items_to_wearable_container(player_id, container_id, new_items)


class TestUpdateWearableContainerItems:
    """Test update_wearable_container_items method."""

    @pytest.mark.asyncio
    async def test_update_items_success(self):
        """Test successfully updating container items."""
        mock_persistence = AsyncMock()
        player_id = uuid4()
        container_id = uuid4()

        container_data = {
            "container_id": str(container_id),
            "source_type": "equipment",
            "entity_id": player_id,
            "capacity_slots": 10,
            "items": [],
        }
        mock_persistence.get_container.return_value = container_data
        mock_persistence.update_container.return_value = {"container_id": str(container_id), "items": []}

        service = WearableContainerService(persistence=mock_persistence)

        new_items = [{"item_id": "item-1"}]

        with patch("server.services.wearable_container_service.logger"):
            result = await service.update_wearable_container_items(player_id, container_id, new_items)

            assert result is not None
            mock_persistence.update_container.assert_called_once()

    @pytest.mark.asyncio
    async def test_update_items_capacity_exceeded(self):
        """Test updating items when capacity would be exceeded."""
        mock_persistence = AsyncMock()
        player_id = uuid4()
        container_id = uuid4()

        container_data = {
            "container_id": str(container_id),
            "source_type": "equipment",
            "entity_id": player_id,
            "capacity_slots": 5,
            "items": [],
        }
        mock_persistence.get_container.return_value = container_data

        service = WearableContainerService(persistence=mock_persistence)

        new_items = [{"item_id": f"item-{i}"} for i in range(10)]  # 10 items > 5 capacity

        with pytest.raises(WearableContainerServiceError, match="Container capacity exceeded"):
            await service.update_wearable_container_items(player_id, container_id, new_items)


class TestHandleContainerOverflow:
    """Test handle_container_overflow method."""

    @pytest.mark.asyncio
    async def test_handle_overflow_all_to_inventory(self):
        """Test overflow handling when all items fit in inventory."""
        mock_persistence = AsyncMock()
        player_id = uuid4()
        container_id = uuid4()

        mock_player = MagicMock()
        mock_player.inventory = []
        mock_player.set_inventory = MagicMock()
        mock_persistence.get_player_by_id = AsyncMock(return_value=mock_player)
        mock_persistence.save_player = AsyncMock()

        service = WearableContainerService(persistence=mock_persistence)

        overflow_items = [{"item_id": "item-1"}, {"item_id": "item-2"}]

        with patch("server.services.wearable_container_service.logger"):
            result = await service.handle_container_overflow(player_id, container_id, overflow_items)

            assert len(result["spilled_items"]) == 2
            assert len(result["ground_items"]) == 0
            mock_persistence.save_player.assert_called_once()

    @pytest.mark.asyncio
    async def test_handle_overflow_some_to_ground(self):
        """Test overflow handling when some items go to ground."""
        mock_persistence = MagicMock()
        player_id = uuid4()
        container_id = uuid4()

        mock_player = MagicMock()
        # Fill inventory to capacity (20 slots)
        mock_player.inventory = [{"item_id": f"item-{i}"} for i in range(20)]
        mock_player.current_room_id = "room-123"
        mock_player.set_inventory = MagicMock()
        mock_persistence.get_player_by_id = AsyncMock(return_value=mock_player)
        mock_persistence.save_player = AsyncMock()
        mock_persistence.create_container.return_value = {"container_id": str(uuid4())}

        service = WearableContainerService(persistence=mock_persistence)

        overflow_items = [{"item_id": f"overflow-{i}"} for i in range(5)]

        with patch("server.services.wearable_container_service.logger"):
            result = await service.handle_container_overflow(player_id, container_id, overflow_items)

            assert len(result["spilled_items"]) == 0
            assert len(result["ground_items"]) == 5

    @pytest.mark.asyncio
    async def test_handle_overflow_player_not_found(self):
        """Test overflow handling when player is not found."""
        mock_persistence = AsyncMock()
        mock_persistence.get_player_by_id.return_value = None

        service = WearableContainerService(persistence=mock_persistence)

        with pytest.raises(WearableContainerServiceError, match="Player not found"):
            await service.handle_container_overflow(uuid4(), uuid4(), [])
