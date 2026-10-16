"""Unit tests for exit_requirements: room exits that stay shut until the player holds a given item."""

import uuid
from typing import cast

from server.game.instance_manager import InstanceManager
from server.game.movement_helpers import DEFAULT_EXIT_REFUSAL, exit_refusal, room_exit_refusal
from server.models.player import Player
from server.models.room import Room

AMULET = "jade_amulet"
REFUSAL = "The ghoul bars the tunnel. 'Not with empty hands.'"


def _room(requirements: object, exits: dict[str, str] | None = None) -> Room:
    attributes: dict[str, object] = {} if requirements is None else {"exit_requirements": requirements}
    return Room({"id": "room_a", "exits": exits or {"down": "room_b", "up": "room_c"}, "attributes": attributes})


def _player(*, inventory: list[dict[str, object]] | None = None) -> Player:
    player = Player(player_id=str(uuid.uuid4()), name="Tester")
    player.set_inventory(inventory or [])
    return player


def _stack(prototype_id: str, **extra: object) -> dict[str, object]:
    return {"prototype_id": prototype_id, "item_id": prototype_id, "quantity": 1, **extra}


GATED_DOWN = {"down": {"item": AMULET, "refusal": REFUSAL}}


def test_a_room_without_requirements_never_refuses() -> None:
    assert exit_refusal(_player(), _room(None), "down") is None


def test_a_gated_exit_refuses_a_player_without_the_item() -> None:
    assert exit_refusal(_player(), _room(GATED_DOWN), "down") == REFUSAL


def test_a_gated_exit_opens_for_a_player_holding_the_item() -> None:
    assert exit_refusal(_player(inventory=[_stack(AMULET)]), _room(GATED_DOWN), "down") is None


def test_the_item_counts_when_equipped() -> None:
    player = _player()
    player.set_equipped_items({"amulet": _stack(AMULET)})  # type: ignore[dict-item]  # Reason: stack dict stands in for the equipped mapping

    assert exit_refusal(player, _room(GATED_DOWN), "down") is None


def test_the_item_counts_inside_a_carried_container() -> None:
    backpack = _stack("backpack", inner_container={"items": [_stack(AMULET)]})

    assert exit_refusal(_player(inventory=[backpack]), _room(GATED_DOWN), "down") is None


def test_only_the_gated_direction_is_closed() -> None:
    assert exit_refusal(_player(), _room(GATED_DOWN), "up") is None


def test_a_missing_refusal_text_falls_back_to_the_default() -> None:
    room = _room({"down": {"item": AMULET}})

    assert exit_refusal(_player(), room, "down") == DEFAULT_EXIT_REFUSAL


def test_malformed_requirements_fail_open_rather_than_trap_the_player() -> None:
    for broken in (
        "not a mapping",
        {"down": "not a mapping"},
        {"down": {"refusal": "no item named"}},
        {"down": {"item": ""}},
    ):
        assert exit_refusal(_player(), _room(broken), "down") is None


def test_room_exit_refusal_refuses_when_every_way_to_the_room_is_gated() -> None:
    assert room_exit_refusal(_player(), _room(GATED_DOWN), "room_b") == REFUSAL


def test_room_exit_refusal_allows_the_move_when_any_way_to_the_room_is_open() -> None:
    """Two exits lead to room_b; one is gated and one is not, so the move is allowed."""
    room = _room(GATED_DOWN, exits={"down": "room_b", "hatch": "room_b"})

    assert room_exit_refusal(_player(), room, "room_b") is None


def test_room_exit_refusal_ignores_rooms_that_are_not_exits() -> None:
    assert room_exit_refusal(_player(), _room(GATED_DOWN), "room_elsewhere") is None


def test_a_gate_survives_instance_cloning_with_its_exit_target_remapped() -> None:
    """Instances are the point: the clone keeps the requirement, and its exit now leads to the instance's own room."""
    stair_id = "earth_demo_zone_room_stair_001"
    vault_id = "earth_demo_zone_room_vault_001"
    stair = Room(
        {
            "id": stair_id,
            "exits": {"down": vault_id},
            "attributes": {"instance_template_id": "demo", "exit_requirements": GATED_DOWN},
        }
    )
    vault = Room({"id": vault_id, "attributes": {"instance_template_id": "demo"}})
    manager = InstanceManager(room_cache={stair_id: stair, vault_id: vault})
    instance = manager.create_instance("demo", uuid.uuid4())
    clone = instance.rooms[f"{instance.instance_id}_{stair_id}"]
    vault_clone_id = f"{instance.instance_id}_{vault_id}"

    assert cast(dict[str, str], clone.exits)["down"] == vault_clone_id
    assert exit_refusal(_player(), clone, "down") == REFUSAL
    assert room_exit_refusal(_player(), clone, vault_clone_id) == REFUSAL
    assert room_exit_refusal(_player(inventory=[_stack(AMULET)]), clone, vault_clone_id) is None
