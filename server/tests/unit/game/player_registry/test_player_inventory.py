"""Unit tests for the inventory part: parsing, validated synchronous changes, rollback, and its narrow write."""

from __future__ import annotations

import json
import re
import uuid

import pytest

from server.game.player_registry import PlayerInventoryPart
from server.game.player_registry.player_inventory import UPDATE_PLAYER_INVENTORY_SQL
from server.schemas.shared import InventorySchemaValidationError

from .fakes import FakeDatabase, raw_row

AMULET = {"item_id": "jade_amulet", "item_name": "Jade Amulet", "slot_type": "backpack", "quantity": 1}


def _part() -> PlayerInventoryPart:
    return PlayerInventoryPart.from_row(raw_row())


def test_from_row_reads_carried_from_inventory_and_equipped_from_equipped_json() -> None:
    part = PlayerInventoryPart.from_row(raw_row(equipped_json='{"head": {"item_id": "cap"}}'))

    assert part.carried[0]["item_name"] == "Sling"
    assert part.equipped == {"head": {"item_id": "cap"}}


def test_changes_are_synchronous_and_a_no_op_change_is_not_dirty() -> None:
    part = _part()
    part.set_carried(list(part.carried))
    assert not part.dirty

    part.set_carried([*part.carried, AMULET])
    assert part.dirty and part.sync_required


def test_an_invalid_inventory_is_refused_in_memory() -> None:
    part = _part()
    with pytest.raises(InventorySchemaValidationError):
        part.set_equipped({"main_hand": {"item_id": "x"}})
    assert part.equipped == {} and not part.dirty


def test_replace_moves_a_stack_between_carried_and_equipped_in_one_change() -> None:
    part = _part()
    sling = dict(part.carried[0])

    part.replace([], {"main_hand": {**sling, "slot_type": "main_hand"}})

    assert part.carried == [] and part.equipped["main_hand"] == {**sling, "slot_type": "main_hand"}


def test_rollback_restores_state_and_flags() -> None:
    part = _part()
    part.begin()
    part.set_carried([])
    part.rollback()

    assert len(part.carried) == 1
    assert not part.dirty and not part.sync_required


def test_write_params_cover_every_procedure_argument_and_nothing_else() -> None:
    instance_id = uuid.uuid4()
    part = _part()
    part.set_carried([*part.carried, {**AMULET, "item_instance_id": instance_id}])

    params = part.write_params()

    assert set(params) == set(re.findall(r":(\w+)", str(UPDATE_PLAYER_INVENTORY_SQL)))
    assert params["inventory"] == params["inventory_json"]  # both carried copies get the same payload
    assert str(instance_id) in str(params["inventory_json"])
    assert json.loads(str(params["equipped_json"])) == {}


async def test_captured_write_sends_the_inventory_and_clears_the_flags() -> None:
    part = _part()
    part.set_carried([AMULET])
    write = part.take_write()
    assert write is not None and not part.dirty and not part.sync_required

    db = FakeDatabase()
    async with db.session() as session:
        await write(session)
    params = db.executed[-1]
    assert params is not None and "Jade Amulet" in str(params["inventory_json"])
