"""A delirium respawn from inside the First Exposure tutorial ends the tutorial (ADR-028, #1080).

The respawn is one registry unit (ADR-029 step 6a); the finisher runs once it has committed.
"""

from __future__ import annotations

import json
import uuid
from dataclasses import dataclass, field
from typing import cast

import pytest

from server.constants.spawn_defaults import RECOVERY_WARD_ROOM_ID
from server.game.items.constants import INSTANCE_BOUND_FLAG
from server.game.player_registry import LucidityData
from server.services.player_respawn_service import PlayerRespawnService
from server.tests.fixtures.shared.player_registry import LucidityHarness, lucidity_registry

INSTANCE_ID = "instance-abc"
PLAYER_ID = uuid.uuid4()
AMULET = {"item_id": "jade_amulet", "prototype_id": "jade_amulet", "quantity": 1, "flags": [INSTANCE_BOUND_FLAG]}


@dataclass
class Rig:
    harness: LucidityHarness
    commits_at_finish: list[int] = field(default_factory=lambda: cast(list[int], []))
    finished: list[tuple[uuid.UUID, str]] = field(default_factory=lambda: cast(list[tuple[uuid.UUID, str]], []))
    finish_fails: bool = False


def _rig(instance_id: str | None = INSTANCE_ID) -> Rig:
    return Rig(
        lucidity_registry(
            {PLAYER_ID: LucidityData(-10, "catatonic")},
            stats={"current_dp": 1, "max_dp": 100, "position": "lying"},
            row={
                "current_room_id": f"instance_{uuid.uuid4()}_vault",
                "tutorial_instance_id": instance_id,
                "inventory": json.dumps([AMULET]),
            },
        )
    )


def _service(rig: Rig) -> PlayerRespawnService:
    async def finish(player_id: uuid.UUID, instance_id: str) -> None:
        rig.commits_at_finish.append(rig.harness.db.commits)
        if rig.finish_fails:
            raise RuntimeError("quest store down")
        rig.finished.append((player_id, instance_id))

    return PlayerRespawnService(first_exposure_finish=finish, player_registry=rig.harness.registry)


def _tutorial_instance(rig: Rig) -> str | None:
    player = rig.harness.registry.peek(PLAYER_ID)
    assert player is not None
    return player.row.tutorial_instance_id


@pytest.mark.asyncio
async def test_a_tutorial_delirium_respawn_ends_the_tutorial() -> None:
    rig = _rig()

    respawned = await _service(rig).respawn_player_from_delirium(PLAYER_ID)

    assert respawned is True
    assert rig.harness.room(PLAYER_ID) == RECOVERY_WARD_ROOM_ID
    assert rig.harness.lucidity(PLAYER_ID).lcd == 70  # not the usual 10
    assert _tutorial_instance(rig) is None
    stats = rig.harness.stats(PLAYER_ID)
    assert stats["current_dp"] == stats["max_dp"]
    # The respawn leaves the inventory alone: the finisher strips the amulet after the commit (ADR-029 step 4c-i).
    player = rig.harness.registry.peek(PLAYER_ID)
    assert player is not None and [stack["item_id"] for stack in player.inventory.carried] == ["jade_amulet"]


@pytest.mark.asyncio
async def test_the_instance_is_finished_only_after_the_respawn_commits() -> None:
    rig = _rig()

    _ = await _service(rig).respawn_player_from_delirium(PLAYER_ID)

    assert rig.commits_at_finish == [1]
    assert rig.finished == [(PLAYER_ID, INSTANCE_ID)]


@pytest.mark.asyncio
async def test_a_failing_finish_does_not_undo_the_respawn() -> None:
    rig = _rig()
    rig.finish_fails = True

    respawned = await _service(rig).respawn_player_from_delirium(PLAYER_ID)

    assert respawned is True
    assert rig.harness.room(PLAYER_ID) == RECOVERY_WARD_ROOM_ID


@pytest.mark.asyncio
async def test_the_ending_works_without_a_finisher_wired() -> None:
    rig = _rig()

    respawned = await PlayerRespawnService(player_registry=rig.harness.registry).respawn_player_from_delirium(PLAYER_ID)

    assert respawned is True
    assert _tutorial_instance(rig) is None


@pytest.mark.asyncio
async def test_an_ordinary_delirium_respawn_is_unchanged() -> None:
    rig = _rig(instance_id=None)

    respawned = await _service(rig).respawn_player_from_delirium(PLAYER_ID)

    assert respawned is True
    assert rig.harness.lucidity(PLAYER_ID).lcd == 10
    assert rig.finished == []
    assert rig.harness.room(PLAYER_ID) == RECOVERY_WARD_ROOM_ID
