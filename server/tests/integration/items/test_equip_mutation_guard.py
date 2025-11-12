from copy import deepcopy

from server.services.equipment_service import EquipmentService
from server.services.inventory_mutation_guard import InventoryMutationGuard
from server.services.inventory_service import InventoryService


def build_inventory_stack() -> dict[str, object]:
    return {
        "item_instance_id": "instance-tonic_laudanum",
        "prototype_id": "tonic_laudanum",
        "item_id": "tonic_laudanum",
        "item_name": "Laudanum Tonic",
        "slot_type": "backpack",
        "quantity": 2,
    }


def test_equip_flow_respects_mutation_guard():
    guard = InventoryMutationGuard()
    inventory_service = InventoryService(mutation_guard=guard)
    equipment_service = EquipmentService(inventory_service=inventory_service)

    inventory = [build_inventory_stack()]
    equipped: dict[str, dict[str, object]] = {}

    with inventory_service.begin_mutation("investigator-1", "token-equip") as decision:
        assert decision.should_apply
        new_inventory, new_equipped = equipment_service.equip_from_inventory(
            inventory,
            equipped,
            slot_index=0,
        )

    assert len(new_inventory) == 1
    assert new_inventory[0]["quantity"] == 1
    assert new_equipped["backpack"]["item_instance_id"] == "instance-tonic_laudanum"

    with inventory_service.begin_mutation("investigator-1", "token-equip") as decision:
        assert decision.should_apply is False
        assert decision.duplicate is True


def test_unequip_flow_respects_mutation_guard():
    guard = InventoryMutationGuard()
    inventory_service = InventoryService(mutation_guard=guard)
    equipment_service = EquipmentService(inventory_service=inventory_service)

    equipped_stack = {
        "item_instance_id": "instance-obsidian_helm",
        "prototype_id": "obsidian_helm",
        "item_id": "obsidian_helm",
        "item_name": "Obsidian Helm",
        "slot_type": "head",
        "quantity": 1,
    }
    inventory = []
    equipped = {"head": deepcopy(equipped_stack)}

    with inventory_service.begin_mutation("investigator-2", "token-unequip") as decision:
        assert decision.should_apply
        new_inventory, new_equipped = equipment_service.unequip_to_inventory(
            inventory, equipped, slot_type="head"
        )

    assert len(new_inventory) == 1
    assert new_equipped == {}

    with inventory_service.begin_mutation("investigator-2", "token-unequip") as decision:
        assert decision.should_apply is False
        assert decision.duplicate is True
