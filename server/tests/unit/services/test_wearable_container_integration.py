"""
Tests for wearable container integration.

As documented in the restricted archives of Miskatonic University, wearable
container integration requires careful testing to ensure proper handling
of equip/unequip transitions, nested container capacity, and inventory spill.
"""

from __future__ import annotations

import uuid
from unittest.mock import MagicMock

import pytest

from server.models.container import ContainerSourceType
from server.services.wearable_container_service import (
    WearableContainerService,
    WearableContainerServiceError,
)


@pytest.fixture
def mock_persistence():
    """Create a mock persistence layer."""
    persistence = MagicMock()
    return persistence


@pytest.fixture
def sample_player_id():
    """Generate a sample player UUID."""
    return uuid.uuid4()


@pytest.fixture
def sample_backpack_item():
    """Create a sample backpack item with inner_container."""
    return {
        "item_instance_id": "inst_backpack_001",
        "prototype_id": "backpack",
        "item_id": "backpack",
        "item_name": "Leather Backpack",
        "slot_type": "backpack",
        "quantity": 1,
        "inner_container": {
            "capacity_slots": 8,
            "items": [],
            "lock_state": "unlocked",
        },
    }


@pytest.fixture
def sample_backpack_with_items():
    """Create a backpack with items inside."""
    return {
        "item_instance_id": "inst_backpack_002",
        "prototype_id": "backpack",
        "item_id": "backpack",
        "item_name": "Leather Backpack",
        "slot_type": "backpack",
        "quantity": 1,
        "inner_container": {
            "capacity_slots": 8,
            "items": [
                {
                    "item_instance_id": "inst_potion_001",
                    "prototype_id": "healing_potion",
                    "item_id": "healing_potion",
                    "item_name": "Healing Potion",
                    "slot_type": "backpack",
                    "quantity": 1,
                },
            ],
            "lock_state": "unlocked",
        },
    }


class TestWearableContainerEquipUnequip:
    """Test wearable container equip/unequip transitions."""

    def test_equip_backpack_creates_container(self, mock_persistence, sample_player_id, sample_backpack_item):
        """Test that equipping a backpack creates a container in PostgreSQL."""
        service = WearableContainerService(persistence=mock_persistence)

        # Mock container creation
        container_id = uuid.uuid4()
        mock_persistence.create_container.return_value = {
            "container_instance_id": str(container_id),
        }

        # Equip backpack
        result = service.handle_equip_wearable_container(
            player_id=sample_player_id,
            item_stack=sample_backpack_item,
        )

        assert result is not None
        assert "container_id" in result
        mock_persistence.create_container.assert_called_once()

        # Verify container was created with correct parameters
        call_args = mock_persistence.create_container.call_args
        assert call_args.kwargs["source_type"] == "equipment"
        assert call_args.kwargs["entity_id"] == sample_player_id
        assert call_args.kwargs["capacity_slots"] == 8

    def test_unequip_backpack_preserves_container(self, mock_persistence, sample_player_id, sample_backpack_with_items):
        """Test that unequipping a backpack preserves the container and its items."""
        # Mock existing container
        container_id = uuid.uuid4()
        container_data = {
            "container_instance_id": str(container_id),
            "source_type": "equipment",
            "entity_id": sample_player_id,
            "capacity_slots": 8,
            "items_json": [
                {
                    "item_instance_id": "inst_potion_001",
                    "prototype_id": "healing_potion",
                    "item_id": "healing_potion",
                    "item_name": "Healing Potion",
                    "slot_type": "backpack",
                    "quantity": 1,
                },
            ],
        }

        mock_persistence.get_containers_by_entity_id.return_value = [container_data]

        service = WearableContainerService(persistence=mock_persistence)

        # Unequip backpack
        result = service.handle_unequip_wearable_container(
            player_id=sample_player_id,
            item_stack=sample_backpack_with_items,
        )

        assert result is not None
        assert "inner_container" in result
        assert len(result["inner_container"]["items"]) == 1

    def test_equip_backpack_without_inner_container(self, mock_persistence, sample_player_id):
        """Test that equipping a non-container item doesn't create a container."""
        regular_item = {
            "item_instance_id": "inst_sword_001",
            "prototype_id": "sword",
            "item_id": "sword",
            "item_name": "Sword",
            "slot_type": "right_hand",
            "quantity": 1,
        }

        service = WearableContainerService(persistence=mock_persistence)

        result = service.handle_equip_wearable_container(
            player_id=sample_player_id,
            item_stack=regular_item,
        )

        assert result is None
        mock_persistence.create_container.assert_not_called()


class TestNestedContainerCapacity:
    """Test nested container capacity enforcement."""

    def test_nested_container_capacity_enforcement(self, mock_persistence, sample_player_id, sample_backpack_item):
        """Test that nested containers enforce capacity limits."""
        service = WearableContainerService(persistence=mock_persistence)

        # Create container
        container_id = uuid.uuid4()
        mock_persistence.create_container.return_value = {
            "container_instance_id": str(container_id),
        }
        mock_persistence.get_container.return_value = {
            "container_instance_id": str(container_id),
            "source_type": "equipment",
            "entity_id": sample_player_id,
            "capacity_slots": 8,
            "items_json": [],
        }

        # Try to add more items than capacity allows
        items_to_add = [
            {
                "item_instance_id": f"inst_item_{i}",
                "prototype_id": "test_item",
                "item_id": "test_item",
                "item_name": f"Test Item {i}",
                "slot_type": "backpack",
                "quantity": 1,
            }
            for i in range(10)  # More than capacity of 8
        ]

        with pytest.raises(WearableContainerServiceError, match="capacity"):
            service.add_items_to_wearable_container(
                player_id=sample_player_id,
                container_id=container_id,
                items=items_to_add,
            )

    def test_nested_container_validates_capacity_on_equip(self, mock_persistence, sample_player_id):
        """Test that equipping a backpack validates nested container capacity."""
        # Backpack with too many items
        overloaded_backpack = {
            "item_instance_id": "inst_backpack_003",
            "prototype_id": "backpack",
            "item_id": "backpack",
            "item_name": "Overloaded Backpack",
            "slot_type": "backpack",
            "quantity": 1,
            "inner_container": {
                "capacity_slots": 8,
                "items": [
                    {
                        "item_instance_id": f"inst_item_{i}",
                        "prototype_id": "test_item",
                        "item_id": "test_item",
                        "item_name": f"Test Item {i}",
                        "slot_type": "backpack",
                        "quantity": 1,
                    }
                    for i in range(10)  # More than capacity
                ],
            },
        }

        service = WearableContainerService(persistence=mock_persistence)

        with pytest.raises(WearableContainerServiceError, match="capacity"):
            service.handle_equip_wearable_container(
                player_id=sample_player_id,
                item_stack=overloaded_backpack,
            )


class TestInventorySpillRules:
    """Test inventory spill rules for wearable container overflow."""

    def test_inventory_spill_on_container_overflow(self, mock_persistence, sample_player_id):
        """Test that items spill to player inventory when container overflows."""
        service = WearableContainerService(persistence=mock_persistence)

        # Create container at capacity
        container_id = uuid.uuid4()
        container_data = {
            "container_instance_id": str(container_id),
            "source_type": "equipment",
            "entity_id": sample_player_id,
            "capacity_slots": 8,
            "items_json": [
                {
                    "item_instance_id": f"inst_item_{i}",
                    "prototype_id": "test_item",
                    "item_id": "test_item",
                    "item_name": f"Test Item {i}",
                    "slot_type": "backpack",
                    "quantity": 1,
                }
                for i in range(8)  # At capacity
            ],
        }

        mock_persistence.get_container.return_value = container_data

        # Try to add more items
        overflow_items = [
            {
                "item_instance_id": "inst_overflow_001",
                "prototype_id": "overflow_item",
                "item_id": "overflow_item",
                "item_name": "Overflow Item",
                "slot_type": "backpack",
                "quantity": 1,
            },
        ]

        # Mock player inventory
        player = MagicMock()
        player.inventory = []
        mock_persistence.get_player.return_value = player

        result = service.handle_container_overflow(
            player_id=sample_player_id,
            container_id=container_id,
            overflow_items=overflow_items,
        )

        assert result is not None
        assert "spilled_items" in result
        assert len(result["spilled_items"]) == 1

    def test_inventory_spill_to_ground_when_inventory_full(self, mock_persistence, sample_player_id):
        """Test that items spill to ground when both container and inventory are full."""
        service = WearableContainerService(persistence=mock_persistence)

        # Create container at capacity
        container_id = uuid.uuid4()
        container_data = {
            "container_instance_id": str(container_id),
            "source_type": "equipment",
            "entity_id": sample_player_id,
            "capacity_slots": 8,
            "items_json": [
                {
                    "item_instance_id": f"inst_item_{i}",
                    "prototype_id": "test_item",
                    "item_id": "test_item",
                    "item_name": f"Test Item {i}",
                    "slot_type": "backpack",
                    "quantity": 1,
                }
                for i in range(8)
            ],
        }

        mock_persistence.get_container.return_value = container_data

        # Mock player with full inventory
        player = MagicMock()
        player.inventory = [
            {
                "item_instance_id": f"inst_inv_{i}",
                "prototype_id": "inv_item",
                "item_id": "inv_item",
                "item_name": f"Inventory Item {i}",
                "slot_type": "backpack",
                "quantity": 1,
            }
            for i in range(20)  # Full inventory
        ]
        player.current_room_id = "earth_arkhamcity_sanitarium_room_foyer_001"
        mock_persistence.get_player.return_value = player

        overflow_items = [
            {
                "item_instance_id": "inst_overflow_001",
                "prototype_id": "overflow_item",
                "item_id": "overflow_item",
                "item_name": "Overflow Item",
                "slot_type": "backpack",
                "quantity": 1,
            },
        ]

        result = service.handle_container_overflow(
            player_id=sample_player_id,
            container_id=container_id,
            overflow_items=overflow_items,
        )

        assert result is not None
        assert "ground_items" in result
        assert len(result["ground_items"]) == 1


class TestWearableContainerPersistence:
    """Test wearable container persistence operations."""

    def test_get_containers_by_entity_id(self, mock_persistence, sample_player_id):
        """Test getting containers for a player entity."""
        container_data = {
            "container_instance_id": str(uuid.uuid4()),
            "source_type": "equipment",
            "entity_id": sample_player_id,
            "capacity_slots": 8,
            "items_json": [],
        }

        mock_persistence.get_containers_by_entity_id.return_value = [container_data]

        service = WearableContainerService(persistence=mock_persistence)

        containers = service.get_wearable_containers_for_player(sample_player_id)

        assert len(containers) == 1
        assert containers[0].source_type == ContainerSourceType.EQUIPMENT
        assert containers[0].entity_id == sample_player_id

    def test_update_wearable_container_items(self, mock_persistence, sample_player_id):
        """Test updating items in a wearable container."""
        container_id = uuid.uuid4()
        container_data = {
            "container_instance_id": str(container_id),
            "source_type": "equipment",
            "entity_id": sample_player_id,
            "capacity_slots": 8,
            "items_json": [],
        }

        mock_persistence.get_container.return_value = container_data
        mock_persistence.update_container.return_value = container_data

        service = WearableContainerService(persistence=mock_persistence)

        new_items = [
            {
                "item_instance_id": "inst_new_001",
                "prototype_id": "new_item",
                "item_id": "new_item",
                "item_name": "New Item",
                "slot_type": "backpack",
                "quantity": 1,
            },
        ]

        result = service.update_wearable_container_items(
            player_id=sample_player_id,
            container_id=container_id,
            items=new_items,
        )

        assert result is not None
        mock_persistence.update_container.assert_called_once()
