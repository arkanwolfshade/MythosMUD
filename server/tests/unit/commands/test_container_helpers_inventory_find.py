"""Unit tests for container_helpers_inventory_find (search and room container lookup)."""

from __future__ import annotations

import uuid
from unittest.mock import MagicMock

from server.commands.container_helpers_inventory_find import (
    check_item_matches_target,
    find_container_in_room,
    find_item_in_inventory,
    find_matching_equipped_containers,
    try_inner_container_by_id,
)


def test_find_item_in_inventory_by_index() -> None:
    inv = [
        {"item_name": "a"},
        {"name": "b"},
    ]
    item, idx = find_item_in_inventory(inv, "2")
    assert idx == 1
    assert item == {"name": "b"}


def test_find_item_in_inventory_by_name_substring() -> None:
    inv = [{"item_name": "Iron Sword"}]
    item, idx = find_item_in_inventory(inv, "sword")
    assert idx == 0
    assert item == inv[0]


def test_find_item_in_inventory_miss() -> None:
    inv = [{"item_name": "a"}]
    assert find_item_in_inventory(inv, "99") == (None, None)
    assert find_item_in_inventory(inv, "zzz") == (None, None)


def test_check_item_matches_target() -> None:
    item = {"item_name": "Backpack", "name": "x"}
    nm, sm = check_item_matches_target(item, "Back", "back")
    assert nm is True
    assert sm is True


def test_find_matching_equipped_containers_by_name() -> None:
    equipped = {
        "slot1": {"item_name": "Satchel", "item_id": "p1"},
    }
    out = find_matching_equipped_containers(equipped, "satchel")
    assert len(out) == 1
    assert out[0][0] == "slot1"


def test_find_matching_equipped_containers_inner_without_name_match() -> None:
    equipped = {"s": {"item_name": "Other", "inner_container": str(uuid.uuid4())}}
    out = find_matching_equipped_containers(equipped, "box")
    assert out == []


def test_try_inner_container_by_id_none() -> None:
    pers = MagicMock()
    assert try_inner_container_by_id(pers, None, "hand", "p") == (None, None)


def test_try_inner_container_by_id_resolves() -> None:
    cid = uuid.uuid4()
    pers = MagicMock()
    pers.get_container = MagicMock(return_value={"container_id": str(cid), "items": []})
    data, uid = try_inner_container_by_id(pers, str(cid), "hand", "player1")
    assert uid == cid
    assert data is not None
    assert data.get("items") == []


def test_find_container_in_room_with_metadata_name() -> None:
    rm = MagicMock()
    cid = uuid.uuid4()
    rm.get_containers = MagicMock(
        return_value=[
            {
                "container_id": str(cid),
                "metadata": {"name": "Wooden Chest"},
            },
        ],
    )
    c, uid = find_container_in_room(rm, "room1", "chest")
    assert uid == cid
    assert c is not None


def test_find_container_in_room_no_match() -> None:
    rm = MagicMock()
    rm.get_containers = MagicMock(return_value=[])
    assert find_container_in_room(rm, "room1", "x") == (None, None)


def test_find_container_in_room_non_dict_entries_skipped() -> None:
    rm = MagicMock()
    rm.get_containers = MagicMock(return_value=["bad", 1])
    assert find_container_in_room(rm, "room1", "x") == (None, None)
