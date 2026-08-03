"""Unit tests for ItemInstance model."""

from server.game.items.item_instance import ItemInstance


def test_item_instance_to_inventory_stack_minimal() -> None:
    inst = ItemInstance(item_instance_id="inst-1", prototype_id="proto-1", name="Lantern")
    stack = inst.to_inventory_stack()
    assert stack["item_instance_id"] == "inst-1"
    assert stack["prototype_id"] == "proto-1"
    assert stack["item_id"] == "proto-1"
    assert stack["item_name"] == "Lantern"
    assert stack["quantity"] == 1
    assert "created_at" in stack


def test_item_instance_to_inventory_stack_includes_optional_fields() -> None:
    inst = ItemInstance(
        item_instance_id="inst-2",
        prototype_id="proto-2",
        name="Tome",
        flags=["cursed"],
        metadata={"pages": 3},
        origin={"source": "loot"},
    )
    stack = inst.to_inventory_stack()
    assert stack["flags"] == ["cursed"]
    assert stack["metadata"] == {"pages": 3}
    assert stack["origin"] == {"source": "loot"}
