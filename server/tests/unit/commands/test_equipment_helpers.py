"""Unit tests for equipment_helpers."""

from __future__ import annotations

import uuid
from typing import cast
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from server.commands.equipment_helpers import (
    find_equipped_item_after_equip,
    normalize_equipped_items,
    normalize_inventory_slots,
    resolve_equip_item_index,
    resolve_unequip_slot,
)
from server.constants.message_category import MessageCategory
from server.models.player import Player


def _player() -> MagicMock:
    player = MagicMock()
    player.player_id = uuid.uuid4()
    player.name = "Tester"
    return player


def test_resolve_equip_by_index() -> None:
    inventory = [{"item_id": "a", "slot_type": "main_hand"}]
    idx, stack = resolve_equip_item_index({"index": 1}, inventory, _player(), "room_001")
    assert idx == 0
    assert stack is not None
    assert stack["item_id"] == "a"


def test_resolve_equip_index_out_of_range() -> None:
    _, err = resolve_equip_item_index({"index": 5}, [], _player(), "room_001")
    assert err == {"result": "You do not have an item in that slot."}


def test_resolve_equip_by_search_term() -> None:
    inventory = [{"item_id": "blade", "item_name": "Switchblade", "slot_type": "main_hand"}]
    idx, stack = resolve_equip_item_index({"search_term": "switch"}, inventory, _player(), "room_001")
    assert idx == 0
    assert stack is not None


def test_resolve_equip_search_no_match() -> None:
    _, err = resolve_equip_item_index({"search_term": "missing"}, [{"item_id": "a"}], _player(), "room_001")
    assert "matching" in err["result"]


def test_resolve_equip_usage() -> None:
    _, err = resolve_equip_item_index({}, [], _player(), "room_001")
    assert err == {
        "result": "Usage: equip <inventory-number|item-name> [slot]",
        "category": MessageCategory.SYSTEM_ERROR,
    }


def test_normalize_inventory_slots() -> None:
    inventory = [{"slot_type": "Main_Hand"}]
    normalize_inventory_slots(inventory)
    assert inventory[0]["slot_type"] == "main_hand"


def test_normalize_equipped_items() -> None:
    equipped = {"Main_Hand": {"slot_type": "Main_Hand", "item_id": "x"}}
    normalized = normalize_equipped_items(equipped)
    assert "main_hand" in normalized


def test_find_equipped_item_after_equip_preferred_slot() -> None:
    equipped = {"main_hand": {"item_id": "x"}}
    slot, item = find_equipped_item_after_equip("main_hand", {"item_id": "x"}, equipped)
    assert slot == "main_hand"
    assert item == equipped["main_hand"]


def test_find_equipped_item_after_equip_by_item_id() -> None:
    equipped = {"off_hand": {"item_id": "shield"}}
    slot, item = find_equipped_item_after_equip(None, {"item_id": "shield"}, equipped)
    assert slot == "off_hand"
    assert item == equipped["off_hand"]


def test_resolve_unequip_by_slot() -> None:
    equipped = {"main_hand": {"item_id": "x"}}
    slot, err = resolve_unequip_slot({"slot": "main_hand"}, equipped)
    assert slot == "main_hand"
    assert err is None


def test_resolve_unequip_usage() -> None:
    slot, err = resolve_unequip_slot({}, {})
    assert slot is None
    assert err == {"result": "Usage: unequip <slot|item-name>", "category": MessageCategory.SYSTEM_ERROR}


def test_resolve_unequip_by_search() -> None:
    equipped = {"main_hand": {"item_id": "x", "item_name": "Blade"}}
    slot, err = resolve_unequip_slot({"search_term": "blade"}, equipped)
    assert slot == "main_hand"
    assert err is None


def test_resolve_unequip_search_no_match() -> None:
    slot, err = resolve_unequip_slot({"search_term": "missing"}, {"main_hand": {"item_name": "Blade"}})
    assert slot is None
    assert "matching" in err["result"]


def test_resolve_unequip_slot_missing() -> None:
    slot, err = resolve_unequip_slot({"slot": "off_hand"}, {"main_hand": {"item_id": "x"}})
    assert slot is None
    assert "equipped in that slot" in err["result"]


@pytest.mark.asyncio
async def test_handle_wearable_container_on_equip_no_inner() -> None:
    from server.commands.equipment_helpers import handle_wearable_container_on_equip

    player = _player()
    await handle_wearable_container_on_equip(MagicMock(), player, {"item_id": "x"})


@pytest.mark.asyncio
async def test_handle_wearable_container_on_equip_creates() -> None:
    from server.commands.equipment_helpers import handle_wearable_container_on_equip

    player = _player()
    svc = AsyncMock()
    svc.handle_equip_wearable_container = AsyncMock(return_value={"container_id": "c1"})
    with patch("server.commands.equipment_helpers.get_shared_services", return_value=(None, svc, None)):
        await handle_wearable_container_on_equip(MagicMock(), player, {"item_id": "x", "inner_container": True})

    svc.handle_equip_wearable_container.assert_awaited_once()


@pytest.mark.asyncio
async def test_handle_wearable_container_on_unequip_links_the_container_through_the_registry(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    """The inner_container link lands on the live carried stack, committed by the registry (ADR-029 4a)."""
    from server.commands.equipment_helpers import handle_wearable_container_on_unequip
    from server.tests.fixtures.shared.player_registry import install_player_registry

    from .test_change_inventory import StubPlayer

    backpack: dict[str, object] = {
        "item_instance_id": str(uuid.uuid4()),
        "prototype_id": "backpack_proto",
        "item_id": "backpack",
        "item_name": "Backpack",
        "slot_type": "inventory",
        "quantity": 1,
    }
    stub = StubPlayer([backpack])
    harness = install_player_registry(monkeypatch, stub)
    inner: dict[str, object] = {"capacity_slots": 10, "items": []}  # the shape the wearable service returns
    svc = AsyncMock()
    svc.handle_unequip_wearable_container = AsyncMock(return_value={"inner_container": inner})

    with patch("server.commands.equipment_helpers.get_shared_services", return_value=(None, svc, None)):
        await handle_wearable_container_on_unequip(
            MagicMock(), cast(Player, cast(object, stub)), {**backpack, "inner_container": inner}
        )

    saved = harness.saved_carried()
    assert saved is not None and saved[0]["inner_container"] == inner
