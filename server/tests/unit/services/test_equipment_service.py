"""Equip and unequip service tests."""

from __future__ import annotations

import copy

import pytest

from server.services.equipment_service import (
    EquipmentCapacityError,
    EquipmentService,
    SlotValidationError,
)
from server.services.inventory_service import InventoryService


def build_service(max_slots: int = 20) -> EquipmentService:
    """Helper to build the equipment service with canonical limits."""
    return EquipmentService(inventory_service=InventoryService(max_slots=max_slots))


def test_equip_moves_item_to_equipped(partial_inventory):
    original_inventory = copy.deepcopy(partial_inventory)
    equipped: dict[str, dict] = {}
    service = build_service()

    new_inventory, new_equipped = service.equip_from_inventory(partial_inventory, equipped, slot_index=1)

    assert partial_inventory == original_inventory
    assert equipped == {}
    assert "left_hand" in new_equipped
    assert new_equipped["left_hand"]["quantity"] == 1
    assert new_equipped["left_hand"]["prototype_id"] == "lantern_battered"
    assert "item_instance_id" in new_equipped["left_hand"]
    assert len(new_inventory) == len(partial_inventory) - 1


def test_equip_decrements_stack_quantity(partial_inventory):
    service = build_service()
    inventory_copy = copy.deepcopy(partial_inventory)

    new_inventory, new_equipped = service.equip_from_inventory(partial_inventory, {}, slot_index=2)

    original_stack = next(item for item in inventory_copy if item["prototype_id"] == "tonic_laudanum")
    updated_stack = next(item for item in new_inventory if item["prototype_id"] == "tonic_laudanum")
    assert original_stack["quantity"] == 3
    assert updated_stack["quantity"] == 2
    assert new_equipped["backpack"]["prototype_id"] == "tonic_laudanum"
    assert new_equipped["backpack"]["item_instance_id"] == original_stack["item_instance_id"]


def test_equip_auto_swaps_existing_item(partial_inventory):
    service = build_service()
    inventory = copy.deepcopy(partial_inventory)
    headpiece = {
        "item_instance_id": "instance-mirror_mask",
        "prototype_id": "mirror_mask",
        "item_id": "mirror_mask",
        "item_name": "Mirror Mask",
        "slot_type": "head",
        "quantity": 1,
        "metadata": {"reflection": "eldritch"},
    }
    inventory.append(headpiece)
    equipped = {
        "head": {
            "item_instance_id": "instance-crown_of_tindalos",
            "prototype_id": "crown_of_tindalos",
            "item_id": "crown_of_tindalos",
            "item_name": "Crown of Tindalos",
            "slot_type": "head",
            "quantity": 1,
            "metadata": {"attuned": True},
        }
    }

    new_inventory, new_equipped = service.equip_from_inventory(inventory, equipped, slot_index=len(inventory) - 1)

    assert new_equipped["head"]["prototype_id"] == "mirror_mask"
    restored = [item for item in new_inventory if item["prototype_id"] == "crown_of_tindalos"]
    assert restored and restored[0]["quantity"] == 1
    assert equipped["head"]["prototype_id"] == "crown_of_tindalos"  # original untouched


def test_equip_validates_target_slot(partial_inventory):
    service = build_service()

    with pytest.raises(SlotValidationError):
        service.equip_from_inventory(partial_inventory, {}, slot_index=1, target_slot="head")


def test_equip_raises_when_swap_overflows(full_inventory):
    service = build_service()
    inventory = copy.deepcopy(full_inventory)
    inventory[0]["slot_type"] = "head"
    inventory[0]["prototype_id"] = "dual_tiara"
    inventory[0]["item_id"] = "dual_tiara"
    inventory[0]["item_name"] = "Dual Tiara"
    inventory[0]["quantity"] = 2
    equipped = {
        "head": {
            "item_instance_id": "instance-obsidian_helm",
            "prototype_id": "obsidian_helm",
            "item_id": "obsidian_helm",
            "item_name": "Obsidian Helm",
            "slot_type": "head",
            "quantity": 1,
        }
    }

    with pytest.raises(EquipmentCapacityError):
        service.equip_from_inventory(inventory, equipped, slot_index=0)


def test_unequip_moves_item_to_inventory(partial_inventory):
    service = build_service()
    equipped = {
        "head": {
            "item_instance_id": "instance-obsidian_helm",
            "prototype_id": "obsidian_helm",
            "item_id": "obsidian_helm",
            "item_name": "Obsidian Helm",
            "slot_type": "head",
            "quantity": 1,
            "metadata": {"ward": "shadows"},
        }
    }

    new_inventory, new_equipped = service.unequip_to_inventory(partial_inventory, equipped, slot_type="head")

    assert "head" not in new_equipped
    restored = [item for item in new_inventory if item["prototype_id"] == "obsidian_helm"]
    assert restored and restored[0]["metadata"]["ward"] == "shadows"
    assert equipped["head"]["metadata"]["ward"] == "shadows"


def test_unequip_requires_present_item(partial_inventory):
    service = build_service()

    with pytest.raises(SlotValidationError):
        service.unequip_to_inventory(partial_inventory, {}, slot_type="head")
