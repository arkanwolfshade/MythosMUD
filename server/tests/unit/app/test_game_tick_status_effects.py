"""Unit tests for the status-effect tick over player_effects rows (ADR-029 step 3b-i)."""

from __future__ import annotations

import uuid
from dataclasses import dataclass, field
from typing import cast
from unittest.mock import AsyncMock, patch

import pytest
from fastapi import FastAPI

from server.app import game_tick_status_effects as module
from server.app.game_tick_protocols import _TickContainer
from server.events.event_types import PlayerDPUpdated
from server.exceptions import DatabaseError
from server.models.player import Player
from server.models.player_effect import PlayerEffect

SECOND = 10  # tick_count on a game second (ticks are 0.1 s)


def _effect(effect_type: str, payload: dict[str, object] | None = None, *, scoped: bool = False) -> PlayerEffect:
    return PlayerEffect(
        id=str(uuid.uuid4()),
        player_id=str(uuid.uuid4()),
        effect_type=effect_type,
        category="scripted",
        remaining_seconds=None,
        payload=payload or {},
        instance_scoped=scoped,
        intensity=1,
        visibility_level="visible",
    )


@dataclass
class FakePersistence:
    """The AsyncPersistenceLayer effect and health surface the tick uses, recording every write."""

    effects: dict[uuid.UUID, list[PlayerEffect]] = field(default_factory=dict)
    players: dict[uuid.UUID, Player] = field(default_factory=dict)
    expired: list[tuple[str, str]] = field(default_factory=list)
    removed: list[str] = field(default_factory=list)
    payloads: list[tuple[str, dict[str, object]]] = field(default_factory=list)
    advanced: list[list[uuid.UUID]] = field(default_factory=list)
    healed: list[int] = field(default_factory=list)
    damaged: list[int] = field(default_factory=list)
    loads: int = 0
    fail_effects_for: set[uuid.UUID] = field(default_factory=set)
    fail_advance: bool = False

    async def get_active_player_effects(self, player_id: uuid.UUID) -> list[PlayerEffect]:
        if player_id in self.fail_effects_for:
            raise DatabaseError("effects unavailable")
        return self.effects.get(player_id, [])

    async def get_player_by_id(self, player_id: uuid.UUID) -> Player | None:
        self.loads += 1
        return self.players.get(player_id)

    async def remove_player_effect_by_id(self, effect_id: str) -> None:
        self.removed.append(effect_id)

    async def update_player_effect_payload(self, effect_id: str, payload: dict[str, object]) -> None:
        self.payloads.append((effect_id, dict(payload)))

    async def advance_player_effects(self, player_ids: list[uuid.UUID]) -> list[tuple[str, str]]:
        if self.fail_advance:
            raise DatabaseError("advance failed")
        self.advanced.append(list(player_ids))
        return self.expired

    async def heal_player(self, player: Player, amount: int) -> None:
        self.healed.append(amount)
        stats = player.get_stats()
        stats["current_dp"] = int(cast(int, stats.get("current_dp", 0))) + amount
        player.set_stats(stats)

    async def damage_player(self, player: Player, amount: int, damage_type: str) -> None:
        _ = player, damage_type
        self.damaged.append(amount)


class FakeConnections:
    def __init__(self, online: list[uuid.UUID]) -> None:
        self.online_players: dict[uuid.UUID, dict[str, object]] = {pid: {} for pid in online}
        self.player_websockets: dict[uuid.UUID, list[str]] = {}


class FakeBus:
    def __init__(self) -> None:
        self.published: list[object] = []

    def publish(self, event: object) -> None:
        self.published.append(event)


@dataclass
class FakeContainer:
    async_persistence: FakePersistence
    connection_manager: FakeConnections
    event_bus: FakeBus = field(default_factory=FakeBus)


def _player(pid: uuid.UUID, dp: int = 5) -> Player:
    player = Player(player_id=str(pid), name="Ticked")
    player.set_stats({"current_dp": dp, "max_dp": 20})
    return player


def _rig(*pids: uuid.UUID) -> tuple[FastAPI, FakeContainer]:
    container = FakeContainer(FakePersistence(), FakeConnections(list(pids)))
    for pid in pids:
        container.async_persistence.players[pid] = _player(pid)
    app = FastAPI()
    app.state.container = container
    return app, container


def _as_tick(container: FakeContainer) -> _TickContainer:
    return cast(_TickContainer, cast(object, container))


@pytest.mark.asyncio
async def test_effects_run_only_on_a_game_second() -> None:
    pid = uuid.uuid4()
    app, container = _rig(pid)
    container.async_persistence.effects[pid] = [_effect("heal_over_time", {"healing": 5})]

    await module.process_status_effects(app, tick_count=SECOND + 3)
    assert container.async_persistence.healed == []
    assert container.async_persistence.advanced == []

    await module.process_status_effects(app, tick_count=SECOND)
    assert container.async_persistence.healed == [5]
    assert container.async_persistence.advanced == [[pid]]


@pytest.mark.asyncio
async def test_nobody_online_means_nothing_runs_or_advances() -> None:
    app, container = _rig()

    await module.process_status_effects(app, tick_count=SECOND)

    assert container.async_persistence.advanced == []  # effects pause while their player is offline


@pytest.mark.asyncio
async def test_heal_over_time_heals_publishes_dp_and_leaves_the_row_alone() -> None:
    pid = uuid.uuid4()
    app, container = _rig(pid)
    heal = _effect("heal_over_time", {"healing": 5, "duration": 15})
    container.async_persistence.effects[pid] = [heal]

    await module.process_status_effects(app, tick_count=SECOND)

    assert container.async_persistence.healed == [5]
    [event] = container.event_bus.published
    assert isinstance(event, PlayerDPUpdated) and (event.old_dp, event.new_dp) == (5, 10)
    assert container.async_persistence.removed == []  # the advance procedure ends it when its seconds run out
    assert container.async_persistence.payloads == []


@pytest.mark.asyncio
async def test_damage_over_time_is_blocked_during_the_login_grace_period() -> None:
    pid = uuid.uuid4()
    _app, container = _rig(pid)
    effect: dict[str, object] = {"type": "damage_over_time", "damage": 3}
    player = container.async_persistence.players[pid]

    with patch.object(module, "is_player_in_login_grace_period", return_value=True):
        blocked = await module._process_damage_over_time_effect(_as_tick(container), player, effect, str(pid))
    with patch.object(module, "is_player_in_login_grace_period", return_value=False):
        applied = await module._process_damage_over_time_effect(_as_tick(container), player, effect, str(pid))

    assert (blocked, applied) == (False, True)
    assert container.async_persistence.damaged == [3]


@pytest.mark.asyncio
async def test_a_drain_second_writes_back_its_state_and_a_finished_drain_is_deleted() -> None:
    pid = uuid.uuid4()
    app, container = _rig(pid)
    drain = _effect("lucidity_drain_over_time", {"rate": 1, "elapsed": 4}, scoped=True)
    container.async_persistence.effects[pid] = [drain]

    async def one_second(_container: object, _player: Player, effect: dict[str, object]):
        return {**effect, "elapsed": 5}, True

    with patch.object(module, "process_lucidity_drain", side_effect=one_second):
        await module.process_status_effects(app, tick_count=SECOND)
    # type and instance_scoped are columns, not payload
    assert container.async_persistence.payloads == [(drain.id, {"rate": 1, "elapsed": 5})]

    async def finished(_container: object, _player: Player, _effect: dict[str, object]):
        return None, True

    with patch.object(module, "process_lucidity_drain", side_effect=finished):
        await module.process_status_effects(app, tick_count=SECOND)
    assert container.async_persistence.removed == [drain.id]


@pytest.mark.asyncio
async def test_a_spell_effect_only_counts_down() -> None:
    pid = uuid.uuid4()
    app, container = _rig(pid)
    container.async_persistence.effects[pid] = [_effect("blinded")]

    await module.process_status_effects(app, tick_count=SECOND)

    assert container.async_persistence.removed == []
    assert container.async_persistence.payloads == []
    assert container.async_persistence.advanced == [[pid]]


@pytest.mark.asyncio
async def test_a_player_without_effects_is_never_loaded() -> None:
    pid = uuid.uuid4()
    app, container = _rig(pid)

    await module.process_status_effects(app, tick_count=SECOND)

    assert container.async_persistence.loads == 0


@pytest.mark.asyncio
async def test_an_expired_login_ward_ends_the_grace_period() -> None:
    pid = uuid.uuid4()
    app, container = _rig(pid)
    container.async_persistence.expired = [(str(pid), "login_warded"), (str(pid), "heal_over_time")]

    with patch.object(module, "handle_login_grace_period_expiration", new_callable=AsyncMock) as ended:
        await module.process_status_effects(app, tick_count=SECOND)

    ended.assert_awaited_once()
    assert ended.await_args is not None and ended.await_args.args[0] == pid


@pytest.mark.asyncio
async def test_one_players_failure_does_not_stop_the_others() -> None:
    broken, fine = uuid.uuid4(), uuid.uuid4()
    app, container = _rig(broken, fine)
    container.async_persistence.fail_effects_for = {broken}
    container.async_persistence.effects[fine] = [_effect("heal_over_time", {"healing": 2})]

    await module.process_status_effects(app, tick_count=SECOND)

    assert container.async_persistence.healed == [2]
    assert container.async_persistence.advanced == [[broken, fine]]


@pytest.mark.asyncio
async def test_a_database_error_is_tracked_and_never_kills_the_tick_loop() -> None:
    pid = uuid.uuid4()
    app, container = _rig(pid)
    container.async_persistence.fail_advance = True

    with patch.object(module, "track_exception") as tracked:
        await module.process_status_effects(app, tick_count=SECOND)  # must not raise

    tracked.assert_called_once()
