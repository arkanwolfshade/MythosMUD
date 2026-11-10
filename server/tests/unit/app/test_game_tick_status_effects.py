"""Unit tests for the status-effect tick over the player registry's effects part (ADR-029 steps 3b-i and 6d)."""

from __future__ import annotations

import uuid
from collections.abc import Sequence
from dataclasses import dataclass, field
from typing import cast
from unittest.mock import AsyncMock, patch

import pytest
from fastapi import FastAPI

from server.app import game_tick_status_effects as module
from server.events.event_types import PlayerDPUpdated
from server.exceptions import DatabaseError
from server.game.player_registry import EffectData, LucidityData, PlayerRegistry
from server.game.player_registry.player_effects import (
    ADVANCE_EFFECTS_SQL,
    DELETE_EFFECT_SQL,
    UPDATE_PAYLOAD_SQL,
)
from server.game.player_registry.player_lucidity import UPSERT_LUCIDITY_SQL
from server.services.lucidity_service import AppliedAdjustment, LucidityService
from server.tests.fixtures.shared.player_registry import LucidityHarness, lucidity_registry

SECOND = 10  # tick_count on a game second (ticks are 0.1 s)


def _effect(
    effect_type: str, remaining: int | None = None, payload: dict[str, object] | None = None, *, scoped: bool = False
) -> EffectData:
    return EffectData(
        id=uuid.uuid4(),
        effect_type=effect_type,
        category="scripted",
        remaining_seconds=remaining,
        payload=payload or {},
        instance_scoped=scoped,
    )


@dataclass
class FakePersistence:
    """The one AsyncPersistenceLayer call the tick makes: which of the online players have an effect."""

    with_effects: set[uuid.UUID] = field(default_factory=lambda: set[uuid.UUID]())
    asked: list[list[uuid.UUID]] = field(default_factory=lambda: list[list[uuid.UUID]]())
    fail: bool = False

    async def get_player_ids_with_effects(self, player_ids: Sequence[uuid.UUID]) -> list[uuid.UUID]:
        if self.fail:
            raise DatabaseError("effects unavailable")
        self.asked.append(list(player_ids))
        return [pid for pid in player_ids if pid in self.with_effects]


class FakeConnections:
    def __init__(self, online: list[uuid.UUID]) -> None:
        self.online_players: dict[uuid.UUID, dict[str, object]] = {pid: {} for pid in online}
        self.player_websockets: dict[uuid.UUID, list[str]] = {}


@dataclass
class FakeContainer:
    async_persistence: FakePersistence
    connection_manager: FakeConnections
    player_registry: PlayerRegistry


@dataclass
class Rig:
    app: FastAPI
    container: FakeContainer
    harness: LucidityHarness
    pids: list[uuid.UUID]

    @property
    def pid(self) -> uuid.UUID:
        return self.pids[0]

    def effects(self, pid: uuid.UUID | None = None) -> list[tuple[str, int | None]]:
        view = self.harness.effects(pid or self.pid)
        return [(effect.effect_type, effect.remaining_seconds) for effect in view.effects]

    def ran(self, statement: object) -> bool:
        """True if the unit's commit executed this exact statement (by identity: clauses define their own ==)."""
        return any(executed is statement for executed in self.harness.db.statements)

    def dp_events(self) -> list[PlayerDPUpdated]:
        return [event for event in self.harness.published if isinstance(event, PlayerDPUpdated)]


def _rig(*effects: EffectData, players: int = 1, dp: int = 5, lucidity: LucidityData | None = None) -> Rig:
    pids = [uuid.uuid4() for _ in range(players)]
    harness = lucidity_registry(dict.fromkeys(pids, lucidity), stats={"current_dp": dp, "max_dp": 20}, effects=effects)
    persistence = FakePersistence(with_effects=set(pids) if effects else set())
    container = FakeContainer(persistence, FakeConnections(pids), harness.registry)
    app = FastAPI()
    app.state.container = container
    return Rig(app, container, harness, pids)


@pytest.mark.asyncio
async def test_effects_run_only_on_a_game_second() -> None:
    rig = _rig(_effect("heal_over_time", 15, {"healing": 5}))

    await module.process_status_effects(rig.app, tick_count=SECOND + 3)
    assert rig.container.async_persistence.asked == []
    assert rig.harness.db.commits == 0

    await module.process_status_effects(rig.app, tick_count=SECOND)
    assert rig.harness.stats(rig.pid)["current_dp"] == 10


@pytest.mark.asyncio
async def test_nobody_online_means_nothing_runs_or_advances() -> None:
    rig = _rig(_effect("heal_over_time", 15, {"healing": 5}), players=0)

    await module.process_status_effects(rig.app, tick_count=SECOND)

    assert rig.container.async_persistence.asked == []  # effects pause while their player is offline


@pytest.mark.asyncio
async def test_a_player_without_effects_is_never_loaded() -> None:
    rig = _rig()

    await module.process_status_effects(rig.app, tick_count=SECOND)

    assert rig.container.async_persistence.asked == [rig.pids]
    assert not rig.harness.registry.is_loaded(rig.pid)
    assert rig.harness.db.commits == 0


@pytest.mark.asyncio
async def test_heal_over_time_heals_the_live_dp_and_tells_the_client_after_the_commit() -> None:
    rig = _rig(_effect("heal_over_time", 15, {"healing": 5, "duration": 15}))

    await module.process_status_effects(rig.app, tick_count=SECOND)

    assert rig.harness.stats(rig.pid)["current_dp"] == 10
    [event] = rig.dp_events()
    assert (event.old_dp, event.new_dp, event.damage_taken, event.source_id) == (5, 10, -5, "heal_over_time")
    assert event.player_id == rig.pid
    assert rig.effects() == [("heal_over_time", 14)]  # one second counted off
    assert rig.harness.db.commits == 1  # the heal and the countdown commit together
    assert rig.ran(ADVANCE_EFFECTS_SQL)


@pytest.mark.asyncio
async def test_healing_at_full_dp_sends_no_dp_event() -> None:
    rig = _rig(_effect("heal_over_time", 15, {"healing": 5}), dp=20)

    await module.process_status_effects(rig.app, tick_count=SECOND)

    assert rig.dp_events() == []


@pytest.mark.asyncio
async def test_damage_over_time_lowers_dp_and_tells_the_client() -> None:
    rig = _rig(_effect("damage_over_time", 5, {"damage": 3}), dp=10)

    with patch.object(module, "is_player_in_login_grace_period", return_value=False):
        await module.process_status_effects(rig.app, tick_count=SECOND)

    assert rig.harness.stats(rig.pid)["current_dp"] == 7
    [event] = rig.dp_events()
    assert (event.old_dp, event.new_dp, event.damage_taken, event.source_id) == (10, 7, 3, "damage_over_time")


@pytest.mark.asyncio
async def test_damage_over_time_is_blocked_during_the_login_grace_period() -> None:
    rig = _rig(_effect("damage_over_time", 5, {"damage": 3}), dp=10)

    with patch.object(module, "is_player_in_login_grace_period", return_value=True):
        await module.process_status_effects(rig.app, tick_count=SECOND)

    assert rig.harness.stats(rig.pid)["current_dp"] == 10
    assert rig.dp_events() == []
    assert rig.effects() == [("damage_over_time", 4)]  # the second still counts


@pytest.mark.asyncio
async def test_a_spell_effect_only_counts_down() -> None:
    rig = _rig(_effect("blinded", 5))

    await module.process_status_effects(rig.app, tick_count=SECOND)

    assert rig.effects() == [("blinded", 4)]
    assert not rig.ran(UPDATE_PAYLOAD_SQL)
    assert not rig.ran(DELETE_EFFECT_SQL)


@pytest.mark.asyncio
async def test_an_effect_on_its_last_second_runs_and_then_ends() -> None:
    rig = _rig(_effect("heal_over_time", 1, {"healing": 5}))

    await module.process_status_effects(rig.app, tick_count=SECOND)

    assert rig.harness.stats(rig.pid)["current_dp"] == 10
    assert rig.effects() == []


@pytest.mark.asyncio
async def test_a_drain_second_commits_the_lcd_loss_with_its_own_elapsed() -> None:
    drain = _effect("lucidity_drain_over_time", None, {"rate": 3, "elapsed": 4}, scoped=True)
    rig = _rig(drain, lucidity=LucidityData(lcd=50))
    announced: list[AppliedAdjustment] = []

    async def announce(_self: LucidityService, applied: AppliedAdjustment) -> None:
        announced.append(applied)

    with patch.object(LucidityService, "announce", announce):
        await module.process_status_effects(rig.app, tick_count=SECOND)

    assert rig.harness.lucidity(rig.pid).lcd == 47
    assert [effect.payload for effect in rig.harness.effects(rig.pid).effects] == [{"rate": 3, "elapsed": 5}]
    assert rig.ran(UPSERT_LUCIDITY_SQL) and rig.ran(UPDATE_PAYLOAD_SQL)
    assert rig.harness.db.commits == 1  # LCD and elapsed land together, so a retry cannot drain one second twice
    [adjustment] = announced
    assert (adjustment.result.previous_lcd, adjustment.result.new_lcd) == (50, 47)


@pytest.mark.asyncio
async def test_a_drain_that_reached_its_floor_is_deleted() -> None:
    drain = _effect("lucidity_drain_over_time", None, {"rate": 1, "floor": -10, "elapsed": 90})
    rig = _rig(drain, lucidity=LucidityData(lcd=-10))

    with patch.object(LucidityService, "announce", AsyncMock()):
        await module.process_status_effects(rig.app, tick_count=SECOND)

    assert rig.effects() == []
    assert rig.ran(DELETE_EFFECT_SQL)
    assert rig.harness.lucidity(rig.pid).lcd == -10


@pytest.mark.asyncio
async def test_a_failed_second_changes_nothing_and_tells_nobody() -> None:
    drain = _effect("lucidity_drain_over_time", None, {"rate": 3, "elapsed": 4})
    heal = _effect("heal_over_time", 9, {"healing": 5})
    rig = _rig(drain, heal, lucidity=LucidityData(lcd=50))
    rig.harness.db.fail_commits = 1

    with patch.object(LucidityService, "announce", AsyncMock()) as announce:
        await module.process_status_effects(rig.app, tick_count=SECOND)  # must not raise

    assert rig.harness.stats(rig.pid)["current_dp"] == 5
    assert rig.harness.lucidity(rig.pid).lcd == 50
    assert rig.effects() == [("lucidity_drain_over_time", None), ("heal_over_time", 9)]
    assert [effect.payload for effect in rig.harness.effects(rig.pid).effects][0] == {"rate": 3, "elapsed": 4}
    assert rig.dp_events() == []
    announce.assert_not_awaited()

    await module.process_status_effects(rig.app, tick_count=SECOND)  # the next second retries it whole

    assert rig.harness.stats(rig.pid)["current_dp"] == 10
    assert rig.harness.lucidity(rig.pid).lcd == 47


@pytest.mark.asyncio
async def test_one_players_failure_does_not_stop_the_others() -> None:
    rig = _rig(_effect("heal_over_time", 9, {"healing": 2}), players=2)
    broken, fine = rig.pids
    rig.harness.db.fail_commits = 1  # the first player's commit fails

    await module.process_status_effects(rig.app, tick_count=SECOND)

    assert rig.harness.stats(broken)["current_dp"] == 5
    assert rig.harness.stats(fine)["current_dp"] == 7


@pytest.mark.asyncio
async def test_an_expired_login_ward_ends_the_grace_period() -> None:
    rig = _rig(_effect("login_warded", 1))

    with patch.object(module, "handle_login_grace_period_expiration", new_callable=AsyncMock) as ended:
        await module.process_status_effects(rig.app, tick_count=SECOND)

    ended.assert_awaited_once()
    assert ended.await_args is not None and ended.await_args.args[0] == rig.pid
    assert rig.effects() == []


@pytest.mark.asyncio
async def test_another_expiring_effect_does_not_touch_the_grace_period() -> None:
    rig = _rig(_effect("blinded", 1))

    with patch.object(module, "handle_login_grace_period_expiration", new_callable=AsyncMock) as ended:
        await module.process_status_effects(rig.app, tick_count=SECOND)

    ended.assert_not_awaited()


@pytest.mark.asyncio
async def test_a_player_deleted_since_the_candidate_query_is_skipped() -> None:
    rig = _rig(_effect("heal_over_time", 9, {"healing": 2}), players=2)
    gone = uuid.uuid4()
    rig.container.async_persistence.with_effects.add(gone)
    rig.container.connection_manager.online_players[gone] = {}

    await module.process_status_effects(rig.app, tick_count=SECOND)

    assert [rig.harness.stats(pid)["current_dp"] for pid in rig.pids] == [7, 7]


@pytest.mark.asyncio
async def test_a_database_error_is_tracked_and_never_kills_the_tick_loop() -> None:
    rig = _rig(_effect("heal_over_time", 9, {"healing": 2}))
    rig.container.async_persistence.fail = True

    with patch.object(module, "track_exception") as tracked:
        await module.process_status_effects(rig.app, tick_count=SECOND)  # must not raise

    tracked.assert_called_once()


@pytest.mark.asyncio
async def test_a_follow_up_that_fails_does_not_undo_the_committed_second() -> None:
    drain = _effect("lucidity_drain_over_time", None, {"rate": 3, "elapsed": 0})
    rig = _rig(drain, lucidity=LucidityData(lcd=50))

    with patch.object(LucidityService, "announce", AsyncMock(side_effect=RuntimeError("nats down"))):
        await module.process_status_effects(rig.app, tick_count=SECOND)  # must not raise

    assert rig.harness.lucidity(rig.pid).lcd == 47


@pytest.mark.asyncio
async def test_the_tick_does_nothing_without_a_registry() -> None:
    rig = _rig(_effect("heal_over_time", 9, {"healing": 2}))
    rig.container.player_registry = cast(PlayerRegistry, cast(object, None))

    await module.process_status_effects(rig.app, tick_count=SECOND)

    assert rig.container.async_persistence.asked == []
    assert rig.harness.db.commits == 0
