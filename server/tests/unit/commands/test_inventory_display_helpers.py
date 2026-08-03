"""Unit tests for inventory display helpers."""

from unittest.mock import MagicMock

from server.commands.inventory_display_helpers import (
    DEFAULT_SLOT_CAPACITY,
    build_container_metadata,
    build_equipped_lines,
    build_inventory_lines,
    filter_non_equipped_inventory,
    format_metadata,
    get_equipped_item_identifiers,
    render_inventory,
)


def test_format_metadata_empty() -> None:
    assert format_metadata(None) == ""
    assert format_metadata({}) == ""


def test_format_metadata_sorted_keys() -> None:
    result = format_metadata({"b": 2, "a": 1})
    assert result == " [a=1, b=2]"


def test_format_metadata_nested_dict() -> None:
    result = format_metadata({"container": {"lock_state": "locked"}})
    assert "container=" in result
    assert "lock_state" in result


def test_format_metadata_exception_returns_empty() -> None:
    bad = MagicMock()
    bad.items.side_effect = RuntimeError("boom")
    assert format_metadata(bad) == ""


def test_get_equipped_item_identifiers() -> None:
    equipped = {
        "main_hand": {"item_id": "sword", "item_instance_id": "inst-1"},
        "off_hand": {"item_id": "shield"},
    }
    ids, instance_ids = get_equipped_item_identifiers(equipped)
    assert ids == {"sword", "shield"}
    assert instance_ids == {"inst-1"}


def test_filter_non_equipped_inventory() -> None:
    inventory = [
        {"item_id": "sword", "slot_type": "inventory", "quantity": 1},
        {"item_instance_id": "inst-1", "slot_type": "inventory", "quantity": 1},
        {"item_id": "coin", "slot_type": "backpack", "quantity": 5},
    ]
    filtered = filter_non_equipped_inventory(inventory, {"sword"}, {"inst-1"})
    assert len(filtered) == 0


def test_filter_keeps_non_equipped_items() -> None:
    inventory = [{"item_id": "coin", "slot_type": "inventory", "quantity": 1}]
    filtered = filter_non_equipped_inventory(inventory, set(), set())
    assert filtered == inventory


def test_build_inventory_lines_empty() -> None:
    assert "No items" in build_inventory_lines([])[0]


def test_build_inventory_lines_with_item() -> None:
    lines = build_inventory_lines(
        [{"item_name": "Coin", "slot_type": "inventory", "quantity": 3, "metadata": {"weight": 1}}]
    )
    assert lines[0].startswith("1. Coin")
    assert "x3" in lines[0]
    assert "weight=1" in lines[0]


def test_build_container_metadata_without_contents() -> None:
    meta = build_container_metadata("backpack", {"weight": 2}, None, None, None)
    assert "weight=2" in meta


def test_build_container_metadata_with_contents() -> None:
    contents = {"backpack": [{"item_name": "Rope"}]}
    meta = build_container_metadata("backpack", {}, contents, {"backpack": 10}, {"backpack": "locked"})
    assert "lock_state" in meta
    assert "capacity_slots" in meta


def test_filter_equipped_by_item_id() -> None:
    inventory = [{"item_id": "sword", "slot_type": "inventory", "quantity": 1}]
    filtered = filter_non_equipped_inventory(inventory, {"sword"}, set())
    assert filtered == []


def test_build_equipped_lines_empty() -> None:
    assert build_equipped_lines({}, None, None, None) == ["- Nothing equipped."]


def test_build_equipped_lines_with_container_items() -> None:
    equipped = {"backpack": {"item_name": "Pack", "quantity": 1, "metadata": {}}}
    contents = {"backpack": [{"item_name": "Rope", "quantity": 2}, {"item_name": "Flask", "quantity": 1}]}
    lines = build_equipped_lines(equipped, contents, {"backpack": 5}, {"backpack": "unlocked"})
    assert any("Pack" in line for line in lines)
    assert any("Rope x2" in line for line in lines)
    assert any("Flask" in line and "x" not in line.split("Flask")[1][:3] for line in lines)


def test_render_inventory_capacity_line() -> None:
    output = render_inventory([], {})
    assert f"0 / {DEFAULT_SLOT_CAPACITY}" in output
    assert "Equipped:" in output


def test_render_inventory_full_flow() -> None:
    inventory = [{"item_id": "coin", "item_name": "Coin", "slot_type": "inventory", "quantity": 1}]
    equipped = {"ring": {"item_id": "ring", "item_name": "Ring", "quantity": 1}}
    output = render_inventory(inventory, equipped)
    assert "Coin" in output
    assert "Ring" in output
