"""Delirium and sanitarium respawns reset lucidity through the player registry, after their commit (ADR-029 step 5b-i)."""

from __future__ import annotations

import uuid
from collections.abc import Sequence
from dataclasses import dataclass, field
from datetime import datetime
from typing import cast

import pytest
from sqlalchemy.ext.asyncio import AsyncSession

from server.constants.spawn_defaults import RECOVERY_WARD_ROOM_ID
from server.events.event_types import BaseEvent, PlayerDeliriumRespawnedEvent, PlayerRespawnedEvent
from server.exceptions import DatabaseError
from server.game.player_registry import LucidityData
from server.models.game import PositionState
from server.models.player import Player
from server.services import player_respawn_service as module
from server.services.lucidity_helpers import LIABILITY_CATALOG, decode_liabilities, encode_liabilities, resolve_tier
from server.services.player_respawn_service import PlayerRespawnService, raise_sanitarium_liabilities
from server.tests.fixtures.shared.player_registry import LucidityHarness, lucidity_registry


@dataclass
class Rig:
    player: Player
    lucidity: LucidityHarness
    commits: int = 0
    rollbacks: int = 0
    fail_commit: bool = False
    events: list[BaseEvent] = field(default_factory=lambda: cast(list[BaseEvent], []))
    combat_cleared: list[uuid.UUID] = field(default_factory=lambda: cast(list[uuid.UUID], []))
    combat_clear_fails: bool = False

    @property
    def player_id(self) -> uuid.UUID:
        return uuid.UUID(str(self.player.player_id))

    def stored(self) -> LucidityData:
        return self.lucidity.lucidity(self.player_id)


class FakeSession:
    _rig: Rig

    def __init__(self, rig: Rig) -> None:
        self._rig = rig

    async def get(self, model: type[object], player_id: uuid.UUID, options: Sequence[object] = ()) -> object | None:
        _ = model, player_id, options
        return self._rig.player

    async def commit(self) -> None:
        if self._rig.fail_commit:
            raise DatabaseError("Database error")
        self._rig.commits += 1

    async def rollback(self) -> None:
        self._rig.rollbacks += 1


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
def _rig(monkeypatch: pytest.MonkeyPatch) -> Rig:
    player = Player(player_id=str(uuid.uuid4()), name="Tester")
    player.current_room_id = "limbo"
    player.set_stats({"current_dp": 1, "max_dp": 100, "position": PositionState.LYING})
    rig = Rig(player, lucidity_registry({uuid.UUID(str(player.player_id)): LucidityData(-10, "catatonic")}))

    class FakeLucidityRepository:
        def __init__(self, session: FakeSession) -> None:
            _ = session

        async def set_cooldown(self, player_id: uuid.UUID, action_code: str, expires_at: datetime) -> None:
            _ = player_id, action_code, expires_at

    monkeypatch.setattr(module, "LucidityRepository", FakeLucidityRepository)
    return rig


def _session(rig: Rig) -> AsyncSession:
    return cast(AsyncSession, cast(object, FakeSession(rig)))


def _service(rig: Rig, *, with_deps: bool = True) -> PlayerRespawnService:
    if not with_deps:
        return PlayerRespawnService(player_registry=rig.lucidity.registry)
    return PlayerRespawnService(
        event_bus=FakeEventBus(rig),
        player_combat_service=FakeCombat(rig),
        player_registry=rig.lucidity.registry,
    )


async def _seed(rig: Rig, lcd: int, tier: str, liabilities: str = "[]") -> None:
    async with rig.lucidity.registry.mutate(rig.player_id) as player:
        _ = player.lucidity.set(lcd=lcd, tier=tier, liabilities=liabilities)


@pytest.mark.asyncio
async def test_a_delirium_respawn_restores_lucidity_10_after_the_commit(rig: Rig) -> None:
    respawned = await _service(rig).respawn_player_from_delirium(rig.player_id, _session(rig))

    assert respawned is True
    # The tier is derived from the restored value (10 is "deranged"), not hardcoded.
    assert (rig.stored().lcd, rig.stored().tier) == (10, resolve_tier(10)) == (10, "deranged")
    assert rig.player.current_room_id == RECOVERY_WARD_ROOM_ID
    assert rig.commits == 1
    [event] = rig.events
    assert isinstance(event, PlayerDeliriumRespawnedEvent) and event.player_id == rig.player_id


@pytest.mark.asyncio
async def test_a_delirium_respawn_clears_combat_state(rig: Rig) -> None:
    _ = await _service(rig).respawn_player_from_delirium(rig.player_id, _session(rig))

    assert rig.combat_cleared == [rig.player_id]


@pytest.mark.asyncio
async def test_a_delirium_respawn_without_event_bus_or_combat_service_still_succeeds(rig: Rig) -> None:
    respawned = await _service(rig, with_deps=False).respawn_player_from_delirium(rig.player_id, _session(rig))

    assert respawned is True and rig.commits == 1


@pytest.mark.asyncio
async def test_a_failed_combat_clear_does_not_fail_the_respawn(rig: Rig) -> None:
    rig.combat_clear_fails = True

    respawned = await _service(rig).respawn_player_from_delirium(rig.player_id, _session(rig))

    assert respawned is True and rig.commits == 1


@pytest.mark.asyncio
async def test_a_failed_commit_rolls_back_and_leaves_lucidity_alone(rig: Rig) -> None:
    rig.fail_commit = True

    respawned = await _service(rig).respawn_player_from_delirium(rig.player_id, _session(rig))

    assert respawned is False and rig.rollbacks == 1
    assert rig.stored().lcd == -10  # set only once the respawn has committed


@pytest.mark.asyncio
@pytest.mark.parametrize("sanitarium", [False, True])
async def test_a_player_the_registry_does_not_know_is_not_respawned(rig: Rig, sanitarium: bool) -> None:
    service = PlayerRespawnService(player_registry=lucidity_registry({}).registry)

    if sanitarium:
        respawned = await service.respawn_player_from_sanitarium(rig.player_id, _session(rig))
    else:
        respawned = await service.respawn_player_from_delirium(rig.player_id, _session(rig))

    assert respawned is False and rig.commits == 0


@pytest.mark.asyncio
async def test_a_sanitarium_respawn_resets_lucidity_to_1_and_adds_a_liability(rig: Rig) -> None:
    await _seed(rig, -100, "catatonic")

    respawned = await _service(rig).respawn_player_from_sanitarium(rig.player_id, _session(rig))

    assert respawned is True
    assert (rig.stored().lcd, rig.stored().tier) == (1, resolve_tier(1))
    [liability] = decode_liabilities(rig.stored().liabilities)
    assert liability["code"] in LIABILITY_CATALOG and liability["stacks"] == 1
    assert rig.player.get_stats()["position"] == PositionState.STANDING
    assert rig.player.current_room_id == RECOVERY_WARD_ROOM_ID
    [event] = rig.events
    assert isinstance(event, PlayerRespawnedEvent)


@pytest.mark.asyncio
async def test_a_sanitarium_respawn_raises_existing_liabilities_to_at_most_five(rig: Rig) -> None:
    await _seed(
        rig, -100, "catatonic", encode_liabilities([{"code": "paranoia", "stacks": 4}, {"code": "x", "stacks": 5}])
    )

    _ = await _service(rig).respawn_player_from_sanitarium(rig.player_id, _session(rig))

    assert decode_liabilities(rig.stored().liabilities) == [
        {"code": "paranoia", "stacks": 5},
        {"code": "x", "stacks": 5},
    ]


class _PickThird:
    def choice(self, seq: Sequence[str]) -> str:
        return seq[2]


def test_raise_sanitarium_liabilities_picks_one_new_liability_when_there_are_none() -> None:
    assert raise_sanitarium_liabilities([], _PickThird()) == [{"code": LIABILITY_CATALOG[2], "stacks": 1}]
