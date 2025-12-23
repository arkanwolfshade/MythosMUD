"""Inventory service stacking and capacity logic tests."""

from __future__ import annotations

import copy

import pytest

from server.services.inventory_mutation_guard import InventoryMutationGuard
from server.services.inventory_service import (
    InventoryCapacityError,
    InventoryService,
    InventorySplitError,
)


def build_service(max_slots: int = 20) -> InventoryService:
    """Helper to build the service with canonical limits."""
    return InventoryService(max_slots=max_slots)


def test_add_stack_merges_matching_payload(partial_inventory):
    service = build_service()
    original_snapshot = copy.deepcopy(partial_inventory)

    incoming = {
        "item_instance_id": "instance-tonic_laudanum-new",
        "prototype_id": "tonic_laudanum",
        "item_id": "tonic_laudanum",
        "item_name": "Laudanum Tonic",
        "slot_type": "backpack",
        "quantity": 2,
        "metadata": {"dose_size_ml": 10, "apothecary": "Ma's Apotheca"},
    }

    updated = service.add_stack(partial_inventory, incoming)

    assert len(updated) == len(partial_inventory)
    laudanum_stack = next(item for item in updated if item["prototype_id"] == "tonic_laudanum")
    assert laudanum_stack["quantity"] == 5
    # merge should retain original stack instance identifier
    assert laudanum_stack["item_instance_id"] == "instance-tonic_laudanum"
    assert partial_inventory == original_snapshot  # input not mutated


def test_add_stack_creates_new_slot_when_metadata_differs(partial_inventory):
    service = build_service()

    incoming = {
        "item_instance_id": "instance-tonic_laudanum-variant",
        "prototype_id": "tonic_laudanum",
        "item_id": "tonic_laudanum",
        "item_name": "Laudanum Tonic",
        "slot_type": "backpack",
        "quantity": 1,
        "metadata": {"dose_size_ml": 12, "apothecary": "Ma's Apotheca"},
    }

    updated = service.add_stack(partial_inventory, incoming)

    assert len(updated) == len(partial_inventory) + 1
    # original stack remains unchanged
    original_stack = next(item for item in updated if item["metadata"].get("dose_size_ml") == 10)
    assert original_stack["quantity"] == 3


def test_add_stack_raises_when_inventory_full(full_inventory):
    service = build_service()

    incoming = {
        "item_instance_id": "instance-verdict_journal",
        "prototype_id": "verdict_journal",
        "item_id": "verdict_journal",
        "item_name": "Journal of Judgements",
        "slot_type": "backpack",
        "quantity": 1,
    }

    with pytest.raises(InventoryCapacityError):
        service.add_stack(full_inventory, incoming)


@pytest.mark.serial  # Flaky in parallel execution - likely due to shared state
def test_split_stack_creates_new_stack_and_preserves_original_inventory(partial_inventory):
    service = build_service()
    partial_inventory[2]["quantity"] = 5
    original_snapshot = copy.deepcopy(partial_inventory)

    updated = service.split_stack(partial_inventory, slot_index=2, split_quantity=2)

    assert len(updated) == len(partial_inventory) + 1
    first_segment = updated[2]
    split_segment = updated[3]
    assert first_segment["quantity"] == 3
    assert split_segment["quantity"] == 2
    assert split_segment["prototype_id"] == first_segment["prototype_id"]
    assert split_segment["item_instance_id"] == first_segment["item_instance_id"]
    assert partial_inventory == original_snapshot  # original inventory untouched


def test_split_stack_raises_when_inventory_full(full_inventory):
    service = build_service()
    full_inventory[0]["quantity"] = 2

    with pytest.raises(InventoryCapacityError):
        service.split_stack(full_inventory, slot_index=0, split_quantity=1)


@pytest.mark.parametrize(
    "slot_index,split_quantity",
    [
        (-1, 1),
        (5, 1),
        (0, 0),
        (0, 5),
    ],
)
def test_split_stack_rejects_invalid_requests(partial_inventory, slot_index, split_quantity):
    service = build_service()
    partial_inventory[0]["quantity"] = 4

    with pytest.raises(InventorySplitError):
        service.split_stack(partial_inventory, slot_index=slot_index, split_quantity=split_quantity)


def test_add_stack_is_pure_function(partial_inventory):
    service = build_service()
    frozen = copy.deepcopy(partial_inventory)

    incoming = {
        "item_instance_id": "instance-mysterious_sand",
        "prototype_id": "mysterious_sand",
        "item_id": "mysterious_sand",
        "item_name": "Vial of Desert Sand",
        "slot_type": "backpack",
        "quantity": 1,
    }

    service.add_stack(partial_inventory, incoming)

    assert partial_inventory == frozen


def test_begin_mutation_delegates_to_guard():
    guard = InventoryMutationGuard()
    service = InventoryService(mutation_guard=guard)

    with service.begin_mutation("investigator-5", "unique-token") as decision:
        assert decision.should_apply
