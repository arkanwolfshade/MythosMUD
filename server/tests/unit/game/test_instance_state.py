"""Unit tests for instance_state: clearing what belongs only to a dead instance from a player."""

import uuid
from typing import cast

from server.game.instance_state import (
    INSTANCE_SCOPED_EFFECT_KEY,
    reset_instance_scoped_state,
    strip_instance_bound_items,
    strip_instance_scoped_effects,
)
from server.game.items.constants import INSTANCE_BOUND_FLAG
from server.models.player import Player


def _player() -> Player:
    return Player(player_id=str(uuid.uuid4()), name="Tester")


def _stack(item_id: str, *flags: str) -> dict[str, object]:
    stack: dict[str, object] = {"item_id": item_id, "prototype_id": item_id, "quantity": 1}
    if flags:
        stack["flags"] = list(flags)
    return stack


def test_strips_instance_bound_items_from_the_inventory_and_keeps_the_rest() -> None:
    player = _player()
    player.set_inventory([_stack("lantern"), _stack("jade_amulet", INSTANCE_BOUND_FLAG), _stack("tonic", "CONSUMABLE")])

    removed = strip_instance_bound_items(player)

    assert removed == 1
    assert [stack["item_id"] for stack in player.get_inventory()] == ["lantern", "tonic"]


def test_strips_instance_bound_items_inside_a_carried_container() -> None:
    backpack = _stack("backpack")
    backpack["inner_container"] = {"items": [_stack("jade_amulet", INSTANCE_BOUND_FLAG), _stack("bandage")]}
    player = _player()
    player.set_inventory([backpack])

    assert strip_instance_bound_items(player) == 1

    [kept] = player.get_inventory()
    assert kept["item_id"] == "backpack"
    inner = cast(dict[str, list[dict[str, object]]], kept["inner_container"])
    assert [item["item_id"] for item in inner["items"]] == ["bandage"]


def test_strips_instance_bound_items_that_are_equipped() -> None:
    player = _player()
    player.set_equipped_items(
        {"amulet": _stack("jade_amulet", INSTANCE_BOUND_FLAG), "main_hand": _stack("cane")}  # type: ignore[arg-type]
    )

    assert strip_instance_bound_items(player) == 1

    assert list(player.get_equipped_items()) == ["main_hand"]


def test_nothing_to_strip_changes_nothing() -> None:
    player = _player()
    player.set_inventory([_stack("lantern")])

    assert strip_instance_bound_items(player) == 0
    assert player.get_inventory() == [_stack("lantern")]


def test_strips_instance_scoped_status_effects_and_keeps_the_rest() -> None:
    player = _player()
    player.set_status_effects(
        [
            {"type": "lucidity_drain_over_time", INSTANCE_SCOPED_EFFECT_KEY: True},
            {"type": "heal_over_time", "healing": 1},
        ]
    )

    assert strip_instance_scoped_effects(player) == 1

    assert [effect["type"] for effect in player.get_status_effects()] == ["heal_over_time"]


def test_reset_instance_scoped_state_clears_items_and_effects_together() -> None:
    player = _player()
    player.set_inventory([_stack("jade_amulet", INSTANCE_BOUND_FLAG)])
    player.set_status_effects([{"type": "lucidity_drain_over_time", INSTANCE_SCOPED_EFFECT_KEY: True}])

    assert reset_instance_scoped_state(player) == 2

    assert player.get_inventory() == []
    assert player.get_status_effects() == []
