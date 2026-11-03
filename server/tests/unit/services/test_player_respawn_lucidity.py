"""Delirium and sanitarium respawns reset lucidity in the same registry unit as the move (ADR-029 steps 5b-i, 6a)."""

from __future__ import annotations

import uuid
from collections.abc import Sequence
from dataclasses import dataclass, field
from typing import cast

import pytest

from server.constants.spawn_defaults import RECOVERY_WARD_ROOM_ID
from server.events.event_types import BaseEvent, PlayerDeliriumRespawnedEvent, PlayerRespawnedEvent
from server.exceptions import DatabaseError
from server.game.player_registry import LucidityData
from server.models.game import PositionState
from server.services.lucidity_helpers import LIABILITY_CATALOG, decode_liabilities, encode_liabilities, resolve_tier
from server.services.player_respawn_service import PlayerRespawnService, raise_sanitarium_liabilities
from server.tests.fixtures.shared.player_registry import LucidityHarness, lucidity_registry

PLAYER_ID = uuid.uuid4()


@dataclass
class Rig:
    harness: LucidityHarness
    events: list[BaseEvent] = field(default_factory=lambda: cast(list[BaseEvent], []))
    combat_cleared: list[uuid.UUID] = field(default_factory=lambda: cast(list[uuid.UUID], []))
    combat_clear_fails: bool = False

    def stored(self) -> LucidityData:
        return self.harness.lucidity(PLAYER_ID)


class FakeEventBus:
    def __init__(self, rig: Rig) -> None:
        self._rig: Rig = rig

    def publish(self, event: BaseEvent) -> None:
        self._rig.events.append(event)


class FakeCombat:
    def __init__(self, rig: Rig) -> None:
        self._rig: Rig = rig

    async def clear_player_combat_state(self, player_id: uuid.UUID) -> None:
        if self._rig.combat_clear_fails:
            raise DatabaseError("Combat clear error")
        self._rig.combat_cleared.append(player_id)


@pytest.fixture(name="rig")
def _rig() -> Rig:
    return Rig(
        lucidity_registry(
            {PLAYER_ID: LucidityData(-10, "catatonic")},
            stats={"current_dp": 1, "max_dp": 100, "position": PositionState.LYING},
            row={"current_room_id": "limbo"},
        )
    )


def _service(rig: Rig, *, with_deps: bool = True) -> PlayerRespawnService:
    if not with_deps:
        return PlayerRespawnService(player_registry=rig.harness.registry)
    return PlayerRespawnService(
        event_bus=FakeEventBus(rig),
        player_combat_service=FakeCombat(rig),
        player_registry=rig.harness.registry,
    )


async def _seed(rig: Rig, lcd: int, tier: str, liabilities: str = "[]") -> None:
    async with rig.harness.registry.mutate(PLAYER_ID) as player:  # pylint: disable=contextmanager-generator-missing-cleanup  # Reason: @asynccontextmanager always drives this generator to completion; pylint cannot see through the wrapper
        _ = player.lucidity.set(lcd=lcd, tier=tier, liabilities=liabilities)


@pytest.mark.asyncio
async def test_a_delirium_respawn_restores_lucidity_10_with_the_move(rig: Rig) -> None:
    respawned = await _service(rig).respawn_player_from_delirium(PLAYER_ID)

    assert respawned is True
    # The tier is derived from the restored value (10 is "deranged"), not hardcoded.
    assert (rig.stored().lcd, rig.stored().tier) == (10, resolve_tier(10)) == (10, "deranged")
    assert rig.harness.room(PLAYER_ID) == RECOVERY_WARD_ROOM_ID
    assert rig.harness.db.commits == 1
    [event] = rig.events
    assert isinstance(event, PlayerDeliriumRespawnedEvent) and event.player_id == PLAYER_ID


@pytest.mark.asyncio
async def test_a_delirium_respawn_clears_combat_state(rig: Rig) -> None:
    _ = await _service(rig).respawn_player_from_delirium(PLAYER_ID)

    assert rig.combat_cleared == [PLAYER_ID]


@pytest.mark.asyncio
async def test_a_delirium_respawn_without_event_bus_or_combat_service_still_succeeds(rig: Rig) -> None:
    respawned = await _service(rig, with_deps=False).respawn_player_from_delirium(PLAYER_ID)

    assert respawned is True and rig.harness.db.commits == 1


@pytest.mark.asyncio
async def test_a_failed_combat_clear_does_not_fail_the_respawn(rig: Rig) -> None:
    rig.combat_clear_fails = True

    respawned = await _service(rig).respawn_player_from_delirium(PLAYER_ID)

    assert respawned is True and rig.harness.db.commits == 1


@pytest.mark.asyncio
async def test_a_failed_commit_rolls_back_the_move_and_the_lucidity(rig: Rig) -> None:
    rig.harness.db.fail_commits, rig.harness.db.commit_error = 1, DatabaseError("Database error")

    respawned = await _service(rig).respawn_player_from_delirium(PLAYER_ID)

    assert respawned is False
    assert rig.stored().lcd == -10  # one unit: nothing of it survives the failed commit
    assert rig.harness.room(PLAYER_ID) == "limbo"
    assert rig.events == []


@pytest.mark.asyncio
@pytest.mark.parametrize("sanitarium", [False, True])
async def test_a_player_the_registry_does_not_know_is_not_respawned(sanitarium: bool) -> None:
    harness = lucidity_registry({})
    service = PlayerRespawnService(player_registry=harness.registry)

    if sanitarium:
        respawned = await service.respawn_player_from_sanitarium(PLAYER_ID)
    else:
        respawned = await service.respawn_player_from_delirium(PLAYER_ID)

    assert respawned is False and harness.db.commits == 0


@pytest.mark.asyncio
async def test_a_sanitarium_respawn_resets_lucidity_to_1_and_adds_a_liability(rig: Rig) -> None:
    await _seed(rig, -100, "catatonic")

    respawned = await _service(rig).respawn_player_from_sanitarium(PLAYER_ID)

    assert respawned is True
    assert (rig.stored().lcd, rig.stored().tier) == (1, resolve_tier(1))
    [liability] = decode_liabilities(rig.stored().liabilities)
    assert liability["code"] in LIABILITY_CATALOG and liability["stacks"] == 1
    assert rig.harness.stats(PLAYER_ID)["position"] == PositionState.STANDING
    assert rig.harness.room(PLAYER_ID) == RECOVERY_WARD_ROOM_ID
    [event] = rig.events
    assert isinstance(event, PlayerRespawnedEvent)


@pytest.mark.asyncio
async def test_a_sanitarium_respawn_raises_existing_liabilities_to_at_most_five(rig: Rig) -> None:
    await _seed(
        rig, -100, "catatonic", encode_liabilities([{"code": "paranoia", "stacks": 4}, {"code": "x", "stacks": 5}])
    )

    _ = await _service(rig).respawn_player_from_sanitarium(PLAYER_ID)

    assert decode_liabilities(rig.stored().liabilities) == [
        {"code": "paranoia", "stacks": 5},
        {"code": "x", "stacks": 5},
    ]


class _PickThird:
    def choice(self, seq: Sequence[str]) -> str:
        return seq[2]


def test_raise_sanitarium_liabilities_picks_one_new_liability_when_there_are_none() -> None:
    assert raise_sanitarium_liabilities([], _PickThird()) == [{"code": LIABILITY_CATALOG[2], "stacks": 1}]
