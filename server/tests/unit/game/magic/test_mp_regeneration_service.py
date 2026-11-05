"""
Unit tests for MP regeneration service.

MP changes run on a real player registry (ADR-029 step 6b); the tick's per-tick read is the persistence layer's row.
"""

import json
import uuid
from collections.abc import Mapping
from types import SimpleNamespace
from typing import cast
from unittest.mock import AsyncMock, patch

import pytest
from sqlalchemy.exc import SQLAlchemyError

from server.game.magic.mp_regeneration_service import (
    MEDITATION_MP_REGEN_MULTIPLIER,
    REST_MP_REGEN_MULTIPLIER,
    MPRegenerationService,
)
from server.game.player_service import PlayerService
from server.models.player import Player
from server.tests.fixtures.shared.player_registry import LucidityHarness, lucidity_registry

PLAYER_ID = uuid.uuid4()
BELOW_MAX: dict[str, object] = {"magic_points": 5, "max_magic_points": 10, "current_dp": 20, "max_dp": 20}


class _Reader:
    """The persistence layer as the tick reads it: this player's row, whatever the registry has written since."""

    def __init__(self, stats: dict[str, object] | None) -> None:
        self._stats: dict[str, object] | None = stats

    async def get_player_by_id(self, player_id: uuid.UUID) -> Player | None:
        if self._stats is None:
            return None
        player = Player(player_id=str(player_id), name="Tester")
        player.set_stats(dict(self._stats))
        return player


def _service(
    stats: dict[str, object] | None = None, *, regen_rate: float = 0.01, registry: bool = True
) -> tuple[MPRegenerationService, LucidityHarness]:
    harness = lucidity_registry({PLAYER_ID: None} if stats is not None else {}, stats=stats)
    player_service = cast(PlayerService, cast(object, SimpleNamespace(persistence=_Reader(stats))))
    service = MPRegenerationService(player_service, regen_rate, harness.registry if registry else None)
    return service, harness


def _restored(result: Mapping[str, object]) -> int:
    return int(str(result["mp_restored"]))


def _mp(harness: LucidityHarness) -> object:
    return harness.stats(PLAYER_ID)["magic_points"]


def test_the_default_rate_is_one_mp_per_hundred_ticks() -> None:
    service, _ = _service()
    assert service.regen_rate == 0.01


@pytest.mark.asyncio
async def test_tick_for_an_unknown_player_is_a_no_op() -> None:
    service, _ = _service(None)

    assert await service.process_tick_regeneration(PLAYER_ID) == {"mp_restored": 0, "current_mp": 0, "max_mp": 0}


@pytest.mark.asyncio
async def test_tick_at_max_writes_nothing() -> None:
    service, harness = _service({"magic_points": 10, "max_magic_points": 10}, regen_rate=1.0)

    result = await service.process_tick_regeneration(PLAYER_ID)

    assert result == {"mp_restored": 0, "current_mp": 10, "max_mp": 10}
    assert harness.db.commits == 0


@pytest.mark.asyncio
async def test_ticks_write_only_when_a_whole_mp_has_accrued() -> None:
    """The point of the accrual: 10 Hz of ticks, one commit per MP (it used to be a full save every tick)."""
    service, harness = _service(dict(BELOW_MAX))

    results = [await service.process_tick_regeneration(PLAYER_ID) for _ in range(110)]

    assert harness.db.commits == 1
    assert sum(_restored(result) for result in results) == 1
    assert _mp(harness) == 6


@pytest.mark.asyncio
async def test_a_regenerated_mp_tells_the_client() -> None:
    service, _ = _service(dict(BELOW_MAX), regen_rate=1.0)

    with patch("server.realtime.connection_manager_api.send_game_event", new_callable=AsyncMock) as send:
        result = await service.process_tick_regeneration(PLAYER_ID)

    assert result == {"mp_restored": 1, "current_mp": 6, "max_mp": 10}
    send.assert_awaited_once_with(PLAYER_ID, "player_update", {"stats": {"magic_points": 6, "max_magic_points": 10}})


@pytest.mark.asyncio
async def test_tick_computes_max_from_power() -> None:
    service, harness = _service({"magic_points": 5, "power": 80}, regen_rate=1.0)  # ceil(80 * 0.2) = 16

    result = await service.process_tick_regeneration(PLAYER_ID)

    assert result["max_mp"] == 16
    assert _mp(harness) == 6


@pytest.mark.asyncio
async def test_tick_without_a_registry_writes_nothing() -> None:
    service, harness = _service(dict(BELOW_MAX), regen_rate=1.0, registry=False)

    result = await service.process_tick_regeneration(PLAYER_ID)

    assert result["mp_restored"] == 0
    assert harness.db.commits == 0


@pytest.mark.asyncio
async def test_a_failed_write_keeps_the_accrued_mp_for_the_next_tick() -> None:
    service, harness = _service(dict(BELOW_MAX), regen_rate=1.0)
    harness.db.fail_commits, harness.db.commit_error = 1, SQLAlchemyError("db down")

    failed = await service.process_tick_regeneration(PLAYER_ID)
    retried = await service.process_tick_regeneration(PLAYER_ID)

    assert failed["mp_restored"] == 0
    assert retried["mp_restored"] == 2  # the failed MP and this tick's


@pytest.mark.asyncio
async def test_a_write_removes_the_old_stored_fraction() -> None:
    service, harness = _service({**BELOW_MAX, "_mp_fractional": 0.4}, regen_rate=1.0)

    _ = await service.process_tick_regeneration(PLAYER_ID)

    assert "_mp_fractional" not in harness.stats(PLAYER_ID)
    written = [params for params in harness.db.executed if params is not None and "stats_changes" in params]
    assert json.loads(str(written[-1]["stats_changes"])) == {"magic_points": 6, "_mp_fractional": None}


@pytest.mark.asyncio
@pytest.mark.parametrize(("position", "whole_mp"), [("standing", 0), ("sitting", 1), ("lying", 1)])
async def test_resting_postures_regenerate_faster(position: str, whole_mp: int) -> None:
    service, _ = _service({**BELOW_MAX, "position": position}, regen_rate=0.34)  # sitting: 0.34 * 3 > 1

    assert (await service.process_tick_regeneration(PLAYER_ID))["mp_restored"] == whole_mp


@pytest.mark.parametrize(
    ("stats", "expected"),
    [
        ({"position": "standing"}, 1.0),
        ({"position": "sitting"}, REST_MP_REGEN_MULTIPLIER),
        ({"position": "lying"}, REST_MP_REGEN_MULTIPLIER * 1.2),
        ({}, 1.0),
    ],
)
def test_get_regen_multiplier(stats: dict[str, object], expected: float) -> None:
    service, _ = _service()
    assert service._get_regen_multiplier(stats) == expected  # pyright: ignore[reportPrivateUsage]  # pylint: disable=protected-access  # Reason: TEST_DOUBLE - the multiplier table is private to the tick  # Appropriate because: asserting it directly keeps the posture table readable without driving many ticks


@pytest.mark.asyncio
async def test_rest_restores_mp_through_the_registry() -> None:
    service, harness = _service({"magic_points": 2, "max_magic_points": 10})

    result = await service.restore_mp_from_rest(PLAYER_ID, 60)  # 0.01 * 3 * 60 = 1.8, whole MP kept

    assert result["success"] is True
    assert (result["mp_restored"], result["current_mp"], result["max_mp"]) == (1, 3, 10)
    assert result["message"] == "You rest and recover 1 magic points."
    assert _mp(harness) == 3
    assert harness.db.commits == 1


@pytest.mark.asyncio
async def test_meditation_restores_more_than_rest() -> None:
    rest, _ = _service({"magic_points": 0, "max_magic_points": 50})
    meditation, _ = _service({"magic_points": 0, "max_magic_points": 50})

    rested = await rest.restore_mp_from_rest(PLAYER_ID, 200)
    meditated = await meditation.restore_mp_from_meditation(PLAYER_ID, 200)

    assert MEDITATION_MP_REGEN_MULTIPLIER > REST_MP_REGEN_MULTIPLIER
    assert _restored(meditated) > _restored(rested)


@pytest.mark.asyncio
async def test_rest_and_meditation_at_max_say_so() -> None:
    service, _ = _service({"magic_points": 10, "max_magic_points": 10})
    full = {"success": True, "message": "Your magic points are already full.", "mp_restored": 0}

    assert await service.restore_mp_from_rest(PLAYER_ID) == full
    assert await service.restore_mp_from_meditation(PLAYER_ID) == full


@pytest.mark.asyncio
async def test_rest_and_meditation_for_an_unknown_player_fail() -> None:
    service, _ = _service(None)

    assert (await service.restore_mp_from_rest(PLAYER_ID))["success"] is False
    assert (await service.restore_mp_from_meditation(PLAYER_ID))["success"] is False


@pytest.mark.asyncio
async def test_rest_without_a_registry_fails() -> None:
    service, _ = _service(dict(BELOW_MAX), registry=False)

    assert (await service.restore_mp_from_rest(PLAYER_ID))["success"] is False


@pytest.mark.asyncio
async def test_item_restores_mp_capped_at_max() -> None:
    service, harness = _service({"magic_points": 8, "max_magic_points": 10})

    result = await service.restore_mp_from_item(PLAYER_ID, 5)

    assert (result["mp_restored"], result["current_mp"]) == (2, 10)
    assert _mp(harness) == 10


@pytest.mark.asyncio
async def test_item_computes_max_from_power() -> None:
    service, _ = _service({"magic_points": 0, "power": 50})

    assert (await service.restore_mp_from_item(PLAYER_ID, 100))["max_mp"] == 10


@pytest.mark.asyncio
async def test_item_for_an_unknown_player_fails() -> None:
    service, _ = _service(None)

    assert (await service.restore_mp_from_item(PLAYER_ID, 5))["success"] is False


@pytest.mark.asyncio
async def test_item_prefers_the_magic_service() -> None:
    restore_mp = AsyncMock(return_value={"success": True, "mp_restored": 3})
    player_service = SimpleNamespace(persistence=_Reader(None), magic_service=SimpleNamespace(restore_mp=restore_mp))
    service = MPRegenerationService(cast(PlayerService, cast(object, player_service)))

    assert await service.restore_mp_from_item(PLAYER_ID, 3) == {"success": True, "mp_restored": 3}
    restore_mp.assert_awaited_once_with(PLAYER_ID, 3)
