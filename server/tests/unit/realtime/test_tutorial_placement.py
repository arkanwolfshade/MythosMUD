"""The tutorial reconnect placement is one registry unit (ADR-029 step 8a)."""

from __future__ import annotations

import json
import uuid
from typing import cast

import pytest

from server.game.instance_state import place_in_instance
from server.game.player_registry import PlayerRegistry
from server.models.player import Player
from server.tests.fixtures.shared.player_registry import FakeDatabase, raw_row
from server.tests.unit.game.player_registry.fakes import FakeLoader

ROOM = "instance_abc_earth_demo_zone_room_square_001"


def _player(player_id: uuid.UUID) -> Player:
    return Player(player_id=str(player_id), name="Placed", current_room_id=ROOM, tutorial_instance_id="instance_abc")


@pytest.mark.asyncio
async def test_placement_commits_the_room_and_the_instance_in_one_synchronous_unit() -> None:
    player_id = uuid.uuid4()
    db = FakeDatabase()
    registry = PlayerRegistry(db.session, loader=FakeLoader({player_id: raw_row(player_id)}))

    await place_in_instance(registry, _player(player_id), ROOM)

    assert db.commits == 1
    written = [cast(dict[str, object], json.loads(str(p["changes"]))) for p in db.executed if p and "changes" in p]
    assert written == [{"current_room_id": ROOM, "tutorial_instance_id": "instance_abc"}]


@pytest.mark.asyncio
async def test_placement_without_a_registry_writes_nothing_and_does_not_raise() -> None:
    await place_in_instance(None, _player(uuid.uuid4()), ROOM)
