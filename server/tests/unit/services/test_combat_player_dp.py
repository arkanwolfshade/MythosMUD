"""A combat hit on a player runs on the player's live DP, as one registry unit (ADR-029 step 6c).

The participant's ``current_dp`` starts as a snapshot. Every other DP writer (heals, bleeding, admin set) changes only
the registry, so a hit that trusted the snapshot wrote a stale absolute value over them.
"""

from __future__ import annotations

import uuid
from types import SimpleNamespace
from typing import cast

import pytest
from sqlalchemy.exc import SQLAlchemyError

from server.events.event_bus import EventBus
from server.events.event_types import BaseEvent, PlayerDPUpdated
from server.models.combat import CombatInstance, CombatParticipant, CombatParticipantType
from server.models.game import PositionState
from server.services.combat_service import CombatService
from server.services.player_health_service import PlayerHealthService
from server.tests.fixtures.shared.player_registry import LucidityHarness, lucidity_registry

# pyright: reportPrivateUsage=false
# Reason: rounds run from the tick loop, which is too much to stand up for one test of CombatTurnProcessor.


class RecordingBus:
    """The event bus as combat uses it."""

    def __init__(self) -> None:
        self.events: list[BaseEvent] = []

    def publish(self, event: BaseEvent) -> None:
        self.events.append(event)


class Fight:
    """One player in one combat, with a real registry behind them."""

    def __init__(self, *, snapshot_dp: int, live_dp: int) -> None:
        self.player_id: uuid.UUID = uuid.uuid4()
        self.harness: LucidityHarness = lucidity_registry(
            {self.player_id: None}, stats={"current_dp": live_dp, "max_dp": 20}
        )
        self.bus: RecordingBus = RecordingBus()
        self.service: CombatService = CombatService(event_bus=cast(EventBus, cast(object, self.bus)))
        self.service.player_registry = self.harness.registry
        self.target: CombatParticipant = CombatParticipant(
            participant_id=self.player_id,
            participant_type=CombatParticipantType.PLAYER,
            name="Tester",
            current_dp=snapshot_dp,
            max_dp=20,
            dexterity=10,
        )
        self.combat: CombatInstance = CombatInstance(room_id="room_001")
        self.combat.participants[self.player_id] = self.target

    def live_dp(self) -> object:
        return self.harness.stats(self.player_id)["current_dp"]

    def dp_events(self) -> list[tuple[int, int]]:
        return [(e.old_dp, e.new_dp) for e in self.bus.events if isinstance(e, PlayerDPUpdated)]


@pytest.fixture(autouse=True)
def _ordinary_room(monkeypatch: pytest.MonkeyPatch) -> None:
    def no_room(_room_id: str) -> None:
        return None

    monkeypatch.setattr(
        "server.container.async_persistence_access.get_container_async_persistence",
        lambda: SimpleNamespace(get_room_by_id=no_room),
    )


@pytest.mark.asyncio
async def test_a_heal_during_combat_survives_the_next_hit() -> None:
    fight = Fight(snapshot_dp=20, live_dp=20)
    _ = await fight.service.apply_attack_damage(fight.combat, fight.target, 10)
    _ = await PlayerHealthService(fight.harness.registry).heal(fight.player_id, 8)

    old_dp, died, wounded = await fight.service.apply_attack_damage(fight.combat, fight.target, 3)

    assert (old_dp, died, wounded) == (18, False, False)
    assert fight.target.current_dp == 15
    assert fight.live_dp() == 15


@pytest.mark.asyncio
async def test_a_hit_counts_from_damage_taken_outside_combat_and_never_raises_dp() -> None:
    fight = Fight(snapshot_dp=20, live_dp=20)
    _ = await PlayerHealthService(fight.harness.registry).damage(fight.player_id, 12)  # a damage-over-time effect

    old_dp, _died, _wounded = await fight.service.apply_attack_damage(fight.combat, fight.target, 2)

    assert old_dp == 8
    assert fight.live_dp() == 6


@pytest.mark.asyncio
async def test_a_hit_that_crosses_the_death_line_from_live_dp_reports_the_death() -> None:
    fight = Fight(snapshot_dp=20, live_dp=-8)  # an admin set during the fight

    old_dp, died, _wounded = await fight.service.apply_attack_damage(fight.combat, fight.target, 2)

    assert (old_dp, died) == (-8, True)
    assert fight.live_dp() == -10


@pytest.mark.asyncio
async def test_the_dp_is_committed_with_its_posture_before_the_client_hears_of_it() -> None:
    fight = Fight(snapshot_dp=5, live_dp=5)

    _old_dp, _died, wounded = await fight.service.apply_attack_damage(fight.combat, fight.target, 7)

    assert wounded
    assert fight.harness.db.commits == 1  # no background task to wait for
    assert fight.harness.stats(fight.player_id)["position"] == PositionState.LYING
    assert fight.dp_events() == [(5, -2)]


@pytest.mark.asyncio
async def test_a_hit_that_changes_nothing_writes_nothing() -> None:
    fight = Fight(snapshot_dp=20, live_dp=20)

    _ = await fight.service.apply_attack_damage(fight.combat, fight.target, 0)

    assert fight.harness.db.commits == 0
    assert fight.live_dp() == 20


@pytest.mark.asyncio
async def test_a_failed_commit_lands_no_damage_and_tells_nobody() -> None:
    fight = Fight(snapshot_dp=20, live_dp=20)
    fight.harness.db.fail_commits = 1
    fight.harness.db.commit_error = SQLAlchemyError("database unavailable")

    result = await fight.service.apply_attack_damage(fight.combat, fight.target, 25)

    assert result == (20, False, False)
    assert fight.target.current_dp == 20
    assert fight.live_dp() == 20
    assert not fight.dp_events()


@pytest.mark.asyncio
async def test_a_hit_on_a_player_with_no_row_still_lands_on_the_participant() -> None:
    fight = Fight(snapshot_dp=20, live_dp=20)
    stranger = uuid.uuid4()  # the registry has no such player, as after a character delete mid-fight
    fight.target.participant_id = stranger

    old_dp, _died, _wounded = await fight.service.apply_attack_damage(fight.combat, fight.target, 5)

    assert old_dp == 20
    assert fight.target.current_dp == 15  # the fight can still finish


@pytest.mark.asyncio
async def test_an_npc_target_never_touches_the_registry() -> None:
    fight = Fight(snapshot_dp=20, live_dp=20)
    fight.target.participant_type = CombatParticipantType.NPC

    _ = await fight.service.apply_attack_damage(fight.combat, fight.target, 5)

    assert fight.target.current_dp == 15
    assert fight.harness.db.commits == 0
    assert not fight.dp_events()


@pytest.mark.asyncio
async def test_a_refresh_lets_a_healed_player_act_again() -> None:
    fight = Fight(snapshot_dp=0, live_dp=9)
    assert not fight.target.can_act_in_combat()

    await fight.service.refresh_player_participants(fight.combat)

    assert fight.target.current_dp == 9
    assert fight.target.can_act_in_combat()


@pytest.mark.asyncio
async def test_a_round_acts_on_the_refreshed_dp(monkeypatch: pytest.MonkeyPatch) -> None:
    fight = Fight(snapshot_dp=0, live_dp=9)
    dp_when_acting: list[int] = []

    async def act(_combat: CombatInstance, participant: CombatParticipant, _round: int, _tick: int) -> None:
        dp_when_acting.append(participant.current_dp)

    processor = fight.service._turn_processor  # pylint: disable=protected-access  # Reason: rounds run from the tick loop, which is too much to stand up here
    monkeypatch.setattr(processor, "_execute_participant_action", act)

    await processor._execute_round(fight.combat, 0)  # pylint: disable=protected-access  # Reason: rounds run from the tick loop, which is too much to stand up here

    assert dp_when_acting == [9]


@pytest.mark.asyncio
async def test_a_refresh_leaves_npcs_alone() -> None:
    fight = Fight(snapshot_dp=20, live_dp=9)
    fight.target.participant_type = CombatParticipantType.NPC

    await fight.service.refresh_player_participants(fight.combat)

    assert fight.target.current_dp == 20


@pytest.mark.asyncio
async def test_a_refresh_keeps_the_last_known_dp_for_a_player_with_no_row() -> None:
    fight = Fight(snapshot_dp=20, live_dp=9)
    fight.target.participant_id = uuid.uuid4()

    await fight.service.refresh_player_participants(fight.combat)

    assert fight.target.current_dp == 20
