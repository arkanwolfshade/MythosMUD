"""
Unit tests for equipment service.

Tests the EquipmentService class for equip/unequip operations.
"""

from typing import Any

import pytest

from server.services.equipment_service import (
    EquipmentCapacityError,
    EquipmentService,
    SlotValidationError,
)
from server.services.inventory_service import InventoryService


@pytest.fixture
def inventory_service():
    """Create an InventoryService instance."""
    return InventoryService(max_slots=20)


@pytest.fixture
def equipment_service(inventory_service):
    """Create an EquipmentService instance."""
    return EquipmentService(inventory_service=inventory_service)


def test_equip_from_inventory_success(equipment_service):
    """Test equip_from_inventory successful equip."""
    inventory = [
        {
            "item_instance_id": "inst1",
            "item_id": "item1",
            "prototype_id": "proto1",
            "item_name": "sword",
            "slot_type": "main_hand",
            "quantity": 1,
        }
    ]
    equipped: dict[str, Any] = {}

    new_inventory, new_equipped = equipment_service.equip_from_inventory(inventory, equipped, slot_index=0)

    assert len(new_inventory) == 0
    assert "main_hand" in new_equipped
    assert new_equipped["main_hand"]["item_name"] == "sword"


def test_equip_from_inventory_invalid_slot_index(equipment_service):
    """Test equip_from_inventory with invalid slot index."""
    inventory = [{"item_name": "sword", "slot_type": "main_hand", "quantity": 1}]
    equipped: dict[str, Any] = {}

    with pytest.raises(SlotValidationError, match="invalid"):
        equipment_service.equip_from_inventory(inventory, equipped, slot_index=10)


def test_equip_from_inventory_no_slot_type(equipment_service):
    """Test equip_from_inventory with item missing slot_type."""
    inventory = [{"item_name": "sword", "quantity": 1}]
    equipped: dict[str, Any] = {}

    with pytest.raises(SlotValidationError, match="slot_type"):
        equipment_service.equip_from_inventory(inventory, equipped, slot_index=0)


def test_equip_from_inventory_slot_mismatch(equipment_service):
    """Test equip_from_inventory with slot type mismatch."""
    inventory = [
        {
            "item_instance_id": "inst1",
            "item_id": "item1",
            "prototype_id": "proto1",
            "item_name": "sword",
            "slot_type": "main_hand",
            "quantity": 1,
        }
    ]
    equipped: dict[str, Any] = {}

    with pytest.raises(SlotValidationError, match="does not match"):
        equipment_service.equip_from_inventory(inventory, equipped, slot_index=0, target_slot="off_hand")


def test_equip_from_inventory_quantity_split(equipment_service):
    """Test equip_from_inventory with quantity > 1."""
    inventory = [
        {
            "item_instance_id": "inst1",
            "item_id": "item1",
            "prototype_id": "proto1",
            "item_name": "potion",
            "slot_type": "consumable",
            "quantity": 5,
        }
    ]
    equipped: dict[str, Any] = {}

    new_inventory, new_equipped = equipment_service.equip_from_inventory(inventory, equipped, slot_index=0)

    assert len(new_inventory) == 1
    assert new_inventory[0]["quantity"] == 4
    assert new_equipped["consumable"]["quantity"] == 1


def test_equip_from_inventory_swap_item(equipment_service):
    """Test equip_from_inventory swaps previously equipped item."""
    inventory = [
        {
            "item_instance_id": "inst2",
            "item_id": "item2",
            "prototype_id": "proto2",
            "item_name": "better_sword",
            "slot_type": "main_hand",
            "quantity": 1,
        }
    ]
    equipped = {
        "main_hand": {
            "item_instance_id": "inst1",
            "item_id": "item1",
            "prototype_id": "proto1",
            "item_name": "sword",
            "slot_type": "main_hand",
            "quantity": 1,
        }
    }

    new_inventory, new_equipped = equipment_service.equip_from_inventory(inventory, equipped, slot_index=0)

    assert len(new_inventory) == 1
    assert new_inventory[0]["item_name"] == "sword"
    assert new_equipped["main_hand"]["item_name"] == "better_sword"


def test_equip_from_inventory_capacity_error(equipment_service):
    """Test equip_from_inventory raises EquipmentCapacityError when inventory full."""
    # Create inventory at capacity
    inventory = [
        {
            "item_instance_id": f"inst{i}",
            "item_id": f"item{i}",
            "prototype_id": f"proto{i}",
            "item_name": f"item{i}",
            "slot_type": "inventory",
            "quantity": 1,
        }
        for i in range(20)
    ]
    equipped = {
        "main_hand": {
            "item_instance_id": "inst_equipped",
            "item_id": "item_equipped",
            "prototype_id": "proto_equipped",
            "item_name": "equipped_sword",
            "slot_type": "main_hand",
            "quantity": 1,
        }
    }
    inventory.append(
        {
            "item_instance_id": "inst_new",
            "item_id": "item_new",
            "prototype_id": "proto_new",
            "item_name": "new_sword",
            "slot_type": "main_hand",
            "quantity": 1,
        }
    )

    with pytest.raises(EquipmentCapacityError, match="capacity reached"):
        equipment_service.equip_from_inventory(inventory, equipped, slot_index=20)


def test_unequip_to_inventory_success(equipment_service):
    """Test unequip_to_inventory successful unequip."""
    inventory: list[dict[str, Any]] = []
    equipped = {
        "main_hand": {
            "item_instance_id": "inst1",
            "item_id": "item1",
            "prototype_id": "proto1",
            "item_name": "sword",
            "slot_type": "main_hand",
            "quantity": 1,
        }
    }

    new_inventory, new_equipped = equipment_service.unequip_to_inventory(inventory, equipped, slot_type="main_hand")

    assert len(new_inventory) == 1
    assert new_inventory[0]["item_name"] == "sword"
    assert "main_hand" not in new_equipped


def test_unequip_to_inventory_empty_slot(equipment_service):
    """Test unequip_to_inventory with empty slot."""
    inventory: list[dict[str, Any]] = []
    equipped: dict[str, Any] = {}

    with pytest.raises(SlotValidationError, match="No equipped item"):
        equipment_service.unequip_to_inventory(inventory, equipped, slot_type="main_hand")


def test_unequip_to_inventory_no_slot_type(equipment_service):
    """Test unequip_to_inventory with no slot type."""
    inventory: list[dict[str, Any]] = []
    equipped: dict[str, Any] = {}

    with pytest.raises(SlotValidationError, match="must be provided"):
        equipment_service.unequip_to_inventory(inventory, equipped, slot_type="")


def test_unequip_to_inventory_capacity_error(equipment_service):
    """Test unequip_to_inventory raises EquipmentCapacityError when inventory full."""
    # Create inventory at capacity
    inventory = [
        {
            "item_instance_id": f"inst{i}",
            "item_id": f"item{i}",
            "prototype_id": f"proto{i}",
            "item_name": f"item{i}",
            "slot_type": "inventory",
            "quantity": 1,
        }
        for i in range(20)
    ]
    equipped = {
        "main_hand": {
            "item_instance_id": "inst_equipped",
            "item_id": "item_equipped",
            "prototype_id": "proto_equipped",
            "item_name": "equipped_sword",
            "slot_type": "main_hand",
            "quantity": 1,
        }
    }

    with pytest.raises(EquipmentCapacityError, match="capacity reached"):
        equipment_service.unequip_to_inventory(inventory, equipped, slot_type="main_hand")
