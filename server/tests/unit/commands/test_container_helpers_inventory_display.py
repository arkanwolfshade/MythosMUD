"""Unit tests for container_helpers_inventory_display."""

from types import SimpleNamespace
from unittest.mock import AsyncMock, MagicMock, patch
from uuid import uuid4

import pytest

from server.commands.container_helpers_inventory_display import (
    _equipped_matches_container_metadata,
    _lock_state_as_str,
    get_container_data_for_inventory,
    match_container_to_slot,
    update_equipped_with_container_info,
)


def test_equipped_matches_by_name() -> None:
    equipped = {"item_name": "Backpack", "item_id": "p1"}
    assert _equipped_matches_container_metadata(equipped, "Backpack", None) is True


def test_equipped_matches_by_id() -> None:
    equipped = {"item_name": "Pack", "item_id": "inst-1"}
    assert _equipped_matches_container_metadata(equipped, None, "inst-1") is True


def test_equipped_no_match() -> None:
    equipped = {"item_name": "Sword", "item_id": "s1"}
    assert _equipped_matches_container_metadata(equipped, "Backpack", "b1") is False


def test_match_container_to_slot_found() -> None:
    component = SimpleNamespace(metadata={"item_name": "Backpack", "item_id": "p1"})
    equipped = {"back": {"item_name": "Backpack", "item_id": "p1"}}
    assert match_container_to_slot(component, equipped) == "back"


def test_match_container_to_slot_not_found() -> None:
    component = SimpleNamespace(metadata={"item_name": "Pouch"})
    equipped = {"hand": {"item_name": "Sword"}}
    assert match_container_to_slot(component, equipped) is None


def test_lock_state_as_str_with_value_attr() -> None:
    lock = SimpleNamespace(value="locked")
    assert _lock_state_as_str(lock) == "locked"


def test_lock_state_as_str_fallback() -> None:
    assert _lock_state_as_str("unlocked") == "unlocked"


@pytest.mark.asyncio
async def test_get_container_data_for_inventory_success() -> None:
    player = MagicMock()
    player.player_id = uuid4()
    player.name = "Tester"
    equipped = {"back": {"item_name": "Pack", "item_id": "p1", "metadata": {}}}
    item_stack = {"item_name": "Key", "quantity": 1}
    container = SimpleNamespace(
        metadata={"item_name": "Pack", "item_id": "p1"},
        items=[item_stack],
        capacity_slots=5,
        lock_state=SimpleNamespace(value="unlocked"),
    )
    wearable_svc = MagicMock()
    wearable_svc.get_wearable_containers_for_player = AsyncMock(return_value=[container])

    with patch(
        "server.commands.container_helpers_inventory_display.get_shared_services",
        return_value=(None, wearable_svc, None),
    ):
        contents, capacities, locks = await get_container_data_for_inventory(MagicMock(), player, equipped)

    assert contents["back"] == [item_stack]
    assert capacities["back"] == 5
    assert locks["back"] == "unlocked"


@pytest.mark.asyncio
async def test_get_container_data_for_inventory_handles_error() -> None:
    player = MagicMock()
    player.player_id = uuid4()
    player.name = "Tester"

    with patch(
        "server.commands.container_helpers_inventory_display.get_shared_services",
        side_effect=RuntimeError("svc down"),
    ):
        contents, capacities, locks = await get_container_data_for_inventory(MagicMock(), player, {})

    assert contents == {}
    assert capacities == {}
    assert locks == {}


def test_update_equipped_with_container_info() -> None:
    equipped = {"back": {"item_name": "Pack", "metadata": {}}}
    contents = {"back": [{"item_name": "Key"}]}
    capacities = {"back": 10}
    locks = {"back": "locked"}

    update_equipped_with_container_info(equipped, contents, capacities, locks)

    container_meta = equipped["back"]["metadata"]["container"]
    assert container_meta["lock_state"] == "locked"
    assert container_meta["capacity_slots"] == 10
    assert container_meta["slots_in_use"] == 1


def test_update_equipped_skips_missing_slot() -> None:
    equipped = {"hand": {"item_name": "Sword", "metadata": {}}}
    update_equipped_with_container_info(equipped, {}, {}, {})
    assert "container" not in equipped["hand"]["metadata"]
