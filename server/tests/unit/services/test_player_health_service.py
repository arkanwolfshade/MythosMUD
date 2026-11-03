"""PlayerHealthService: DP changes as sync units on the player registry (ADR-029 step 6a)."""

from __future__ import annotations

import json
import uuid

import pytest

from server.game.player_registry import PlayerNotFoundError
from server.models.game import PositionState
from server.services.player_health_service import PlayerHealthService
from server.tests.fixtures.shared.player_registry import LucidityHarness, lucidity_registry


def _harness(player_id: uuid.UUID, **stats: object) -> LucidityHarness:
    return lucidity_registry({player_id: None}, stats={"current_dp": 20, "max_dp": 20, **stats})


def _written_stats(harness: LucidityHarness) -> list[dict[str, object]]:
    """The stats changes of every row write, in order."""
    return [
        json.loads(str(params["stats_changes"]))
        for params in harness.db.executed
        if params is not None and "stats_changes" in params
    ]


@pytest.mark.asyncio
async def test_damage_commits_only_the_new_dp() -> None:
    player_id = uuid.uuid4()
    harness = _harness(player_id, cold_resistance=50)

    change = await PlayerHealthService(harness.registry).damage(player_id, 10, "cold")

    assert (change.old_dp, change.new_dp) == (20, 15)
    assert harness.stats(player_id)["current_dp"] == 15
    assert _written_stats(harness) == [{"current_dp": 15}]  # sync: committed before the call returned


@pytest.mark.asyncio
async def test_heal_at_full_dp_writes_nothing() -> None:
    player_id = uuid.uuid4()
    harness = _harness(player_id)

    change = await PlayerHealthService(harness.registry).heal(player_id, 5)

    assert change.new_dp == 20
    assert not _written_stats(harness)


@pytest.mark.asyncio
@pytest.mark.parametrize("method", ["damage", "heal"])
async def test_negative_amounts_are_refused(method: str) -> None:
    player_id = uuid.uuid4()
    service = PlayerHealthService(_harness(player_id).registry)

    with pytest.raises(ValueError, match="must be positive"):
        _ = await (service.damage(player_id, -1) if method == "damage" else service.heal(player_id, -1))


@pytest.mark.asyncio
async def test_set_dp_writes_the_dp_and_its_posture() -> None:
    player_id = uuid.uuid4()
    harness = _harness(player_id)

    change = await PlayerHealthService(harness.registry).set_dp(player_id, -2)

    assert change.became_mortally_wounded
    assert harness.stats(player_id)["position"] == PositionState.LYING
    assert _written_stats(harness) == [{"current_dp": -2, "position": "lying"}]


@pytest.mark.asyncio
async def test_decay_skips_a_dead_player() -> None:
    player_id = uuid.uuid4()
    harness = _harness(player_id, current_dp=-10)

    assert await PlayerHealthService(harness.registry).decay(player_id) is None
    assert not _written_stats(harness)


@pytest.mark.asyncio
async def test_decay_bleeds_a_mortally_wounded_player() -> None:
    player_id = uuid.uuid4()
    harness = _harness(player_id, current_dp=-9, position="lying")

    change = await PlayerHealthService(harness.registry).decay(player_id)

    assert change is not None and change.became_dead
    assert _written_stats(harness) == [{"current_dp": -10}]


@pytest.mark.asyncio
async def test_an_unknown_player_raises() -> None:
    service = PlayerHealthService(_harness(uuid.uuid4()).registry)

    with pytest.raises(PlayerNotFoundError):
        _ = await service.damage(uuid.uuid4(), 1)
