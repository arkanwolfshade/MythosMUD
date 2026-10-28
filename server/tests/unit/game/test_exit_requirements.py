"""Unit tests for exit_requirements: room exits that stay shut until the player holds an item or has done a quest activity."""

import uuid
from collections.abc import Iterator
from typing import cast

import pytest

from server.game.instance_manager import InstanceManager
from server.game.movement_helpers import (
    DEFAULT_EXIT_REFUSAL,
    exit_refusal,
    room_exit_refusal,
    set_quest_activity_reader,
)
from server.models.player import Player
from server.models.room import Room

AMULET = "jade_amulet"
REFUSAL = "The ghoul bars the tunnel. 'Not with empty hands.'"
LOOKED = "cmd_look"
LOOK_REFUSAL = "Dusk is thick and you are not yet sure where you stand."


@pytest.fixture(autouse=True)
def _no_reader() -> Iterator[None]:
    """Every test starts with no quest-progress reader wired, and leaves none behind."""
    set_quest_activity_reader(None)
    yield
    set_quest_activity_reader(None)


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
LOOK_GATED_UP = {"up": {"quest_activity": LOOKED, "refusal": LOOK_REFUSAL}}


@pytest.mark.asyncio
async def test_a_room_without_requirements_never_refuses() -> None:
    assert await exit_refusal(_player(), _room(None), "down") is None


@pytest.mark.asyncio
async def test_a_gated_exit_refuses_a_player_without_the_item() -> None:
    assert await exit_refusal(_player(), _room(GATED_DOWN), "down") == REFUSAL


@pytest.mark.asyncio
async def test_a_gated_exit_opens_for_a_player_holding_the_item() -> None:
    assert await exit_refusal(_player(inventory=[_stack(AMULET)]), _room(GATED_DOWN), "down") is None


@pytest.mark.asyncio
async def test_the_item_counts_when_equipped() -> None:
    player = _player()
    player.set_equipped_items({"amulet": _stack(AMULET)})  # type: ignore[dict-item]  # Reason: stack dict stands in for the equipped mapping

    assert await exit_refusal(player, _room(GATED_DOWN), "down") is None


@pytest.mark.asyncio
async def test_the_item_counts_inside_a_carried_container() -> None:
    backpack = _stack("backpack", inner_container={"items": [_stack(AMULET)]})

    assert await exit_refusal(_player(inventory=[backpack]), _room(GATED_DOWN), "down") is None


@pytest.mark.asyncio
async def test_only_the_gated_direction_is_closed() -> None:
    assert await exit_refusal(_player(), _room(GATED_DOWN), "up") is None


@pytest.mark.asyncio
async def test_a_missing_refusal_text_falls_back_to_the_default() -> None:
    room = _room({"down": {"item": AMULET}})

    assert await exit_refusal(_player(), room, "down") == DEFAULT_EXIT_REFUSAL


@pytest.mark.asyncio
async def test_malformed_requirements_fail_open_rather_than_trap_the_player() -> None:
    for broken in (
        "not a mapping",
        {"down": "not a mapping"},
        {"down": {"refusal": "no item named"}},
        {"down": {"item": ""}},
        {"down": {"quest_activity": ""}},
        {"down": {"quest_activity": 7}},
    ):
        assert await exit_refusal(_player(), _room(broken), "down") is None


@pytest.mark.asyncio
async def test_room_exit_refusal_refuses_when_every_way_to_the_room_is_gated() -> None:
    assert await room_exit_refusal(_player(), _room(GATED_DOWN), "room_b") == REFUSAL


@pytest.mark.asyncio
async def test_room_exit_refusal_allows_the_move_when_any_way_to_the_room_is_open() -> None:
    """Two exits lead to room_b; one is gated and one is not, so the move is allowed."""
    room = _room(GATED_DOWN, exits={"down": "room_b", "hatch": "room_b"})

    assert await room_exit_refusal(_player(), room, "room_b") is None


@pytest.mark.asyncio
async def test_room_exit_refusal_ignores_rooms_that_are_not_exits() -> None:
    assert await room_exit_refusal(_player(), _room(GATED_DOWN), "room_elsewhere") is None


@pytest.mark.asyncio
async def test_a_gate_survives_instance_cloning_with_its_exit_target_remapped() -> None:
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
    assert await exit_refusal(_player(), clone, "down") == REFUSAL
    assert await room_exit_refusal(_player(), clone, vault_clone_id) == REFUSAL
    assert await room_exit_refusal(_player(inventory=[_stack(AMULET)]), clone, vault_clone_id) is None


# --- exits a quest unlocks (#1111) ---------------------------------------------------------------------------


def _wire(done: set[str]) -> list[tuple[uuid.UUID, str]]:
    """Wire a reader that knows ``done`` activities; returns the (player, target) asks it received."""
    asked: list[tuple[uuid.UUID, str]] = []

    async def reader(player_id: uuid.UUID, target: str) -> bool:
        asked.append((player_id, target))
        return target in done

    set_quest_activity_reader(reader)
    return asked


@pytest.mark.asyncio
async def test_a_quest_gated_exit_refuses_until_the_activity_is_done() -> None:
    asked = _wire(set())
    player = _player()

    assert await exit_refusal(player, _room(LOOK_GATED_UP), "up") == LOOK_REFUSAL
    assert asked == [(uuid.UUID(player.player_id), LOOKED)]


@pytest.mark.asyncio
async def test_a_quest_gated_exit_opens_once_the_activity_is_done() -> None:
    _ = _wire({LOOKED})

    assert await exit_refusal(_player(), _room(LOOK_GATED_UP), "up") is None


@pytest.mark.asyncio
async def test_an_exit_needing_an_item_and_an_activity_needs_both() -> None:
    _ = _wire({LOOKED})
    room = _room({"down": {"item": AMULET, "quest_activity": LOOKED, "refusal": REFUSAL}})

    assert await exit_refusal(_player(), room, "down") == REFUSAL  # the activity is done, the item is not
    assert await exit_refusal(_player(inventory=[_stack(AMULET)]), room, "down") is None

    _ = _wire(set())
    assert (
        await exit_refusal(_player(inventory=[_stack(AMULET)]), room, "down") == REFUSAL
    )  # the item, not the activity


@pytest.mark.asyncio
async def test_the_quest_is_not_asked_when_the_item_already_refuses() -> None:
    asked = _wire({LOOKED})
    room = _room({"down": {"item": AMULET, "quest_activity": LOOKED}})

    assert await exit_refusal(_player(), room, "down") == DEFAULT_EXIT_REFUSAL
    assert asked == []


@pytest.mark.asyncio
async def test_a_quest_gate_with_no_reader_wired_stays_open_rather_than_trap_the_player() -> None:
    assert await exit_refusal(_player(), _room(LOOK_GATED_UP), "up") is None


@pytest.mark.asyncio
async def test_a_quest_gate_with_an_unreadable_player_id_stays_open() -> None:
    _ = _wire(set())
    player = Player(player_id="not-a-uuid", name="Tester")

    assert await exit_refusal(player, _room(LOOK_GATED_UP), "up") is None


@pytest.mark.asyncio
async def test_room_exit_refusal_applies_a_quest_gate_to_flee_and_follow() -> None:
    _ = _wire(set())
    room = _room(LOOK_GATED_UP, exits={"up": "room_c"})

    assert await room_exit_refusal(_player(), room, "room_c") == LOOK_REFUSAL
