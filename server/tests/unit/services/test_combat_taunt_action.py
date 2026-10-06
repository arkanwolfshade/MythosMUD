"""Unit tests for the queued taunt (#833): graded roll -> hate-list change -> room line -> aggro switch."""

# pyright: reportPrivateUsage=false
# Reason: CombatTurnProcessor._execute_queued_action is the dispatch point under test.

from __future__ import annotations

import uuid
from dataclasses import dataclass
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from server.game.skill_service import SuccessLevel
from server.models.combat import CombatAction, CombatInstance, CombatParticipant, CombatParticipantType
from server.services import aggro_threat, combat_taunt_action
from server.services.combat_turn_processor import CombatTurnProcessor

PLAYER = CombatParticipantType.PLAYER
NPC = CombatParticipantType.NPC


def _p(name: str, ptype: CombatParticipantType = PLAYER, dp: int = 50) -> CombatParticipant:
    return CombatParticipant(
        participant_id=uuid.uuid4(),
        participant_type=ptype,
        name=name,
        current_dp=dp,
        max_dp=100,
        dexterity=10,
    )


@dataclass
class _Fight:
    """A healer holding the ghoul's attention (50 threat) with a tank (10) who is about to taunt."""

    combat: CombatInstance
    ghoul: CombatParticipant
    tank: CombatParticipant
    healer: CombatParticipant
    action: CombatAction


def _fight(*, ghoul_dp: int = 50) -> _Fight:
    ghoul, tank, healer = _p("Ghoul", NPC, dp=ghoul_dp), _p("Tank"), _p("Healer")
    combat = CombatInstance(combat_id=uuid.uuid4(), room_id="r1")
    for p in (ghoul, tank, healer):
        combat.participants[p.participant_id] = p
    combat.npc_hate_lists[ghoul.participant_id] = {healer.participant_id: 50.0, tank.participant_id: 10.0}
    combat.npc_current_target[ghoul.participant_id] = healer.participant_id
    action = CombatAction(
        combat_id=combat.combat_id,
        attacker_id=tank.participant_id,
        target_id=ghoul.participant_id,
        action_type="taunt",
    )
    return _Fight(combat, ghoul, tank, healer, action)


def _doubles(
    level: SuccessLevel, *, room: str | None = "r1", skill_linked: bool = True
) -> tuple[MagicMock, AsyncMock, AsyncMock, AsyncMock]:
    """A CombatService stand-in plus the typed mocks to assert on: (service, roll, announce, switches)."""
    roll: AsyncMock = AsyncMock(return_value=level)
    announce: AsyncMock = AsyncMock()
    switches: AsyncMock = AsyncMock()
    skill_service: MagicMock = MagicMock()
    skill_service.roll_best_skill_check = roll
    messaging: MagicMock = MagicMock()
    messaging.broadcast_taunt_result = announce
    integration: MagicMock = MagicMock()
    integration.get_messaging_integration = MagicMock(return_value=messaging)
    service: MagicMock = MagicMock()
    service.skill_service = skill_service if skill_linked else None
    service.get_participant_current_room = AsyncMock(return_value=room)
    service.get_npc_combat_integration_service = MagicMock(return_value=integration)
    service.broadcast_aggro_target_switches = switches
    return service, roll, announce, switches


def _hate(fight: _Fight) -> dict[uuid.UUID, float]:
    return fight.combat.npc_hate_lists[fight.ghoul.participant_id]


@pytest.mark.asyncio
async def test_regular_success_makes_the_taunter_top_and_pulls_the_npc_off_the_healer() -> None:
    f = _fight()
    service, roll, announce, switches = _doubles(SuccessLevel.REGULAR)

    await combat_taunt_action.resolve_taunt_action(service, f.combat, f.tank, f.action)

    assert _hate(f)[f.tank.participant_id] == pytest.approx(56.0)  # 50 top + (10% of 50 + 1)
    assert f.combat.npc_current_target[f.ghoul.participant_id] == f.tank.participant_id
    roll.assert_awaited_once_with(f.tank.participant_id, ("intimidate", "fighting"))
    announce.assert_awaited_once_with("r1", str(f.combat.combat_id), "Tank bellows a challenge at Ghoul!")
    switches.assert_awaited_once_with("r1", f.combat.combat_id, [(f.ghoul.participant_id, "Ghoul", "Tank")])


@pytest.mark.asyncio
@pytest.mark.parametrize("level", [SuccessLevel.HARD, SuccessLevel.EXTREME])
async def test_hard_and_extreme_successes_double_the_lead(level: SuccessLevel) -> None:
    f = _fight()
    service, _, announce, _ = _doubles(level)

    await combat_taunt_action.resolve_taunt_action(service, f.combat, f.tank, f.action)

    assert _hate(f)[f.tank.participant_id] == pytest.approx(62.0)  # 50 top + 2 * (10% of 50 + 1)
    announce.assert_awaited_once_with("r1", str(f.combat.combat_id), "Tank bellows a challenge at Ghoul!")


@pytest.mark.asyncio
async def test_failure_changes_nothing_but_still_announces() -> None:
    f = _fight()
    service, _, announce, switches = _doubles(SuccessLevel.FAILURE)

    await combat_taunt_action.resolve_taunt_action(service, f.combat, f.tank, f.action)

    assert _hate(f) == {f.healer.participant_id: 50.0, f.tank.participant_id: 10.0}
    assert f.combat.npc_current_target[f.ghoul.participant_id] == f.healer.participant_id
    announce.assert_awaited_once_with("r1", str(f.combat.combat_id), "Tank's bluster fails to impress Ghoul.")
    switches.assert_not_awaited()


@pytest.mark.asyncio
async def test_fumble_wipes_the_taunter_from_the_hate_list() -> None:
    f = _fight()
    service, _, announce, switches = _doubles(SuccessLevel.FUMBLE)

    await combat_taunt_action.resolve_taunt_action(service, f.combat, f.tank, f.action)

    assert f.tank.participant_id not in _hate(f)
    assert _hate(f)[f.healer.participant_id] == 50.0
    announce.assert_awaited_once_with("r1", str(f.combat.combat_id), "Tank's voice cracks; Ghoul dismisses them.")
    switches.assert_not_awaited()


@pytest.mark.asyncio
async def test_a_fumble_by_the_current_tank_hands_the_npc_to_the_next_in_line() -> None:
    """The backfire has teeth: the tank holding aggro fumbles and the healer is suddenly the target."""
    f = _fight()
    service, _, _, switches = _doubles(SuccessLevel.FUMBLE)
    _hate(f)[f.tank.participant_id] = 80.0
    f.combat.npc_current_target[f.ghoul.participant_id] = f.tank.participant_id

    await combat_taunt_action.resolve_taunt_action(service, f.combat, f.tank, f.action)

    assert f.combat.npc_current_target[f.ghoul.participant_id] == f.healer.participant_id
    switches.assert_awaited_once_with("r1", f.combat.combat_id, [(f.ghoul.participant_id, "Ghoul", "Healer")])


@pytest.mark.asyncio
async def test_dead_target_is_dropped_without_rolling() -> None:
    f = _fight(ghoul_dp=0)
    service, roll, announce, _ = _doubles(SuccessLevel.EXTREME)

    await combat_taunt_action.resolve_taunt_action(service, f.combat, f.tank, f.action)

    roll.assert_not_awaited()
    announce.assert_not_awaited()


@pytest.mark.asyncio
async def test_a_target_that_is_not_an_npc_in_this_combat_is_dropped() -> None:
    f = _fight()
    service, roll, _, _ = _doubles(SuccessLevel.EXTREME)
    f.action.target_id = f.healer.participant_id  # an ally, not an NPC
    await combat_taunt_action.resolve_taunt_action(service, f.combat, f.tank, f.action)
    f.action.target_id = uuid.uuid4()  # not in the fight at all
    await combat_taunt_action.resolve_taunt_action(service, f.combat, f.tank, f.action)

    roll.assert_not_awaited()


@pytest.mark.asyncio
@pytest.mark.parametrize("room", ["r2", None])
async def test_taunt_stays_room_local_if_the_taunter_has_left(room: str | None) -> None:
    f = _fight()
    service, roll, _, _ = _doubles(SuccessLevel.EXTREME, room=room)

    await combat_taunt_action.resolve_taunt_action(service, f.combat, f.tank, f.action)

    roll.assert_not_awaited()
    assert _hate(f)[f.tank.participant_id] == 10.0


@pytest.mark.asyncio
async def test_taunt_is_skipped_when_no_skill_service_is_linked() -> None:
    f = _fight()
    service, _, announce, _ = _doubles(SuccessLevel.EXTREME, skill_linked=False)

    await combat_taunt_action.resolve_taunt_action(service, f.combat, f.tank, f.action)

    announce.assert_not_awaited()
    assert _hate(f)[f.tank.participant_id] == 10.0


@pytest.mark.asyncio
async def test_no_messaging_integration_still_resolves_the_taunt() -> None:
    f = _fight()
    service, _, announce, _ = _doubles(SuccessLevel.REGULAR)
    service.get_npc_combat_integration_service = MagicMock(return_value=None)

    await combat_taunt_action.resolve_taunt_action(service, f.combat, f.tank, f.action)

    assert _hate(f)[f.tank.participant_id] == pytest.approx(56.0)
    announce.assert_not_awaited()


@pytest.mark.parametrize(
    ("level", "line"),
    [
        (SuccessLevel.EXTREME, "Ann bellows a challenge at the ghoul!"),
        (SuccessLevel.HARD, "Ann bellows a challenge at the ghoul!"),
        (SuccessLevel.REGULAR, "Ann bellows a challenge at the ghoul!"),
        (SuccessLevel.FAILURE, "Ann's bluster fails to impress the ghoul."),
        (SuccessLevel.FUMBLE, "Ann's voice cracks; the ghoul dismisses them."),
    ],
)
def test_taunt_outcome_lines(level: SuccessLevel, line: str) -> None:
    assert combat_taunt_action.taunt_outcome_line(level, "Ann", "the ghoul") == line


# --- the margin multiplier on apply_taunt itself -----------------------------------------------------------------


def test_apply_taunt_default_multiplier_is_the_original_ten_percent_plus_one() -> None:
    f = _fight()
    assert aggro_threat.apply_taunt(f.combat, f.ghoul.participant_id, f.tank.participant_id, "r1", "r1")
    assert _hate(f)[f.tank.participant_id] == pytest.approx(56.0)


def test_apply_taunt_multiplier_scales_the_lead() -> None:
    f = _fight()
    assert aggro_threat.apply_taunt(
        f.combat, f.ghoul.participant_id, f.tank.participant_id, "r1", "r1", margin_multiplier=2.0
    )
    assert _hate(f)[f.tank.participant_id] == pytest.approx(62.0)


def test_apply_taunt_still_refuses_another_room_whatever_the_multiplier() -> None:
    f = _fight()
    assert not aggro_threat.apply_taunt(
        f.combat, f.ghoul.participant_id, f.tank.participant_id, "r1", "r2", margin_multiplier=2.0
    )
    assert _hate(f)[f.tank.participant_id] == 10.0


# --- the turn processor dispatches the 'taunt' action ------------------------------------------------------------


@pytest.mark.asyncio
async def test_turn_processor_dispatches_a_queued_taunt_and_spends_the_turn() -> None:
    f = _fight()
    resolve: AsyncMock = AsyncMock()
    combat_service: MagicMock = MagicMock()
    processor = CombatTurnProcessor(combat_service)

    with patch.object(combat_taunt_action, "resolve_taunt_action", new=resolve):
        await processor._execute_queued_action(f.combat, f.tank, f.action, current_tick=77)

    resolve.assert_awaited_once_with(combat_service, f.combat, f.tank, f.action)
    assert f.tank.last_action_tick == 77


@pytest.mark.asyncio
async def test_a_failing_taunt_does_not_break_the_round() -> None:
    f = _fight()
    resolve: AsyncMock = AsyncMock(side_effect=RuntimeError("db down"))
    processor = CombatTurnProcessor(MagicMock())

    with patch.object(combat_taunt_action, "resolve_taunt_action", new=resolve):
        await processor._execute_queued_action(f.combat, f.tank, f.action, current_tick=5)

    assert f.tank.last_action_tick == 5  # the turn is still spent and the round carries on
