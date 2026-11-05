"""PlayerMpService: MP changes as sync units on the player registry (ADR-029 step 6b)."""

from __future__ import annotations

import json
import uuid

import pytest

from server.game.player_registry import PlayerNotFoundError
from server.services.player_mp_service import PlayerMpService
from server.tests.fixtures.shared.player_registry import LucidityHarness, lucidity_registry

PLAYER_ID = uuid.uuid4()


def _harness() -> LucidityHarness:
    return lucidity_registry({PLAYER_ID: None}, stats={"magic_points": 5, "max_magic_points": 10, "current_dp": 20})


def _written(harness: LucidityHarness) -> list[dict[str, object]]:
    return [
        json.loads(str(params["stats_changes"]))
        for params in harness.db.executed
        if params is not None and "stats_changes" in params
    ]


@pytest.mark.asyncio
async def test_spend_commits_only_the_new_mp() -> None:
    harness = _harness()

    change = await PlayerMpService(harness.registry).spend(PLAYER_ID, 2)

    assert (change.old_mp, change.new_mp) == (5, 3)
    assert harness.stats(PLAYER_ID)["magic_points"] == 3
    assert harness.db.commits == 1  # sync: committed before the call returned
    assert _written(harness) == [{"magic_points": 3}]  # DP and the rest are not written back


@pytest.mark.asyncio
async def test_restore_caps_at_max() -> None:
    harness = _harness()

    change = await PlayerMpService(harness.registry).restore(PLAYER_ID, 50)

    assert (change.new_mp, change.gained) == (10, 5)
    assert harness.stats(PLAYER_ID)["magic_points"] == 10


@pytest.mark.asyncio
async def test_restore_at_max_writes_nothing() -> None:
    harness = lucidity_registry({PLAYER_ID: None}, stats={"magic_points": 10, "max_magic_points": 10})

    _ = await PlayerMpService(harness.registry).restore(PLAYER_ID, 5)

    assert harness.db.commits == 0


@pytest.mark.asyncio
async def test_drain_moves_what_the_target_loses_in_one_commit() -> None:
    caster = uuid.uuid4()
    harness = lucidity_registry({PLAYER_ID: None, caster: None}, stats={"magic_points": 4, "max_magic_points": 10})

    lost, received = await PlayerMpService(harness.registry).drain(PLAYER_ID, caster, 10)

    assert (lost.new_mp, lost.gained) == (0, -4)  # only what the target had
    assert (received.new_mp, received.gained) == (8, 4)
    assert harness.db.commits == 1


@pytest.mark.asyncio
async def test_set_mp_may_exceed_the_max() -> None:
    harness = _harness()

    _ = await PlayerMpService(harness.registry).set_mp(PLAYER_ID, 15)

    assert harness.stats(PLAYER_ID)["magic_points"] == 15


@pytest.mark.asyncio
async def test_an_unknown_player_raises() -> None:
    with pytest.raises(PlayerNotFoundError):
        _ = await PlayerMpService(_harness().registry).spend(uuid.uuid4(), 1)
