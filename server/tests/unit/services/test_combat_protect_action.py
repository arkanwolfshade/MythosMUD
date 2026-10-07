"""Unit tests for the queued protect (#991): graded roll -> cover -> threat share, and the redirect it gives."""

# pyright: reportPrivateUsage=false
# Reason: CombatTurnProcessor._execute_queued_action is the dispatch point under test.

from __future__ import annotations

import uuid
from dataclasses import dataclass
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from server.game.skill_service import SuccessLevel
from server.models.combat import CombatAction, CombatInstance, CombatParticipant, CombatParticipantType
from server.services import combat_protect_action
from server.services.combat_turn_processor import CombatTurnProcessor

PLAYER = CombatParticipantType.PLAYER
NPC = CombatParticipantType.NPC

_ROUND = 4  # the round being resolved: combat_round has not advanced yet


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
    """A healer holding the ghoul's attention (50 threat) with a tank (10) who is about to protect them."""

    combat: CombatInstance
    ghoul: CombatParticipant
    tank: CombatParticipant
    healer: CombatParticipant
    action: CombatAction


def _fight(*, tank_threat: float = 10.0) -> _Fight:
    ghoul, tank, healer = _p("Ghoul", NPC), _p("Tank"), _p("Healer")
    combat = CombatInstance(combat_id=uuid.uuid4(), room_id="r1", combat_round=_ROUND)
    for p in (ghoul, tank, healer):
        combat.participants[p.participant_id] = p
    combat.npc_hate_lists[ghoul.participant_id] = {healer.participant_id: 50.0, tank.participant_id: tank_threat}
    combat.npc_current_target[ghoul.participant_id] = healer.participant_id
    action = CombatAction(
        combat_id=combat.combat_id,
        attacker_id=tank.participant_id,
        target_id=healer.participant_id,
        action_type="protect",
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
    messaging.broadcast_protect_result = announce
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


# --- resolve_protect_action ----------------------------------------------------------------------------------------


@pytest.mark.asyncio
async def test_regular_success_covers_the_ally_for_this_round_and_the_next() -> None:
    f = _fight()
    service, roll, announce, _ = _doubles(SuccessLevel.REGULAR)

    await combat_protect_action.resolve_protect_action(service, f.combat, f.tank, f.action)

    guard = f.combat.active_guard(f.healer.participant_id)
    assert guard is not None
    assert guard.protector_id == f.tank.participant_id
    assert guard.expires_round == _ROUND + 1
    roll.assert_awaited_once_with(f.tank.participant_id, ("fighting",))
    announce.assert_awaited_once_with("r1", str(f.combat.combat_id), "Tank throws themselves in front of Healer!")


@pytest.mark.asyncio
@pytest.mark.parametrize("level", [SuccessLevel.HARD, SuccessLevel.EXTREME])
async def test_hard_and_extreme_successes_cover_one_round_longer(level: SuccessLevel) -> None:
    f = _fight()
    service, _, _, _ = _doubles(level)

    await combat_protect_action.resolve_protect_action(service, f.combat, f.tank, f.action)

    guard = f.combat.active_guard(f.healer.participant_id)
    assert guard is not None
    assert guard.expires_round == _ROUND + 2


@pytest.mark.asyncio
@pytest.mark.parametrize("level", [SuccessLevel.FAILURE, SuccessLevel.FUMBLE])
async def test_failure_and_fumble_do_nothing_but_still_announce(level: SuccessLevel) -> None:
    """There is no fumble case: any miss is just 'no cover, the round is spent'."""
    f = _fight()
    service, _, announce, switches = _doubles(level)

    await combat_protect_action.resolve_protect_action(service, f.combat, f.tank, f.action)

    assert f.combat.active_guard(f.healer.participant_id) is None
    assert _hate(f) == {f.healer.participant_id: 50.0, f.tank.participant_id: 10.0}
    announce.assert_awaited_once_with("r1", str(f.combat.combat_id), "Tank fails to reach Healer in time.")
    switches.assert_not_awaited()


@pytest.mark.asyncio
async def test_success_hands_the_protector_half_the_allys_threat() -> None:
    f = _fight()
    service, _, _, switches = _doubles(SuccessLevel.REGULAR)

    await combat_protect_action.resolve_protect_action(service, f.combat, f.tank, f.action)

    assert _hate(f)[f.tank.participant_id] == pytest.approx(35.0)  # 10 + 50% of the healer's 50
    assert _hate(f)[f.healer.participant_id] == 50.0  # the ally keeps theirs
    assert f.combat.npc_current_target[f.ghoul.participant_id] == f.healer.participant_id
    switches.assert_not_awaited()


@pytest.mark.asyncio
async def test_a_big_enough_share_pulls_the_npc_onto_the_protector() -> None:
    f = _fight(tank_threat=40.0)
    service, _, _, switches = _doubles(SuccessLevel.REGULAR)

    await combat_protect_action.resolve_protect_action(service, f.combat, f.tank, f.action)

    assert f.combat.npc_current_target[f.ghoul.participant_id] == f.tank.participant_id
    switches.assert_awaited_once_with("r1", f.combat.combat_id, [(f.ghoul.participant_id, "Ghoul", "Tank")])


@pytest.mark.asyncio
async def test_an_ally_with_no_threat_gives_nothing_to_share() -> None:
    f = _fight()
    del _hate(f)[f.healer.participant_id]
    service, _, _, switches = _doubles(SuccessLevel.REGULAR)

    await combat_protect_action.resolve_protect_action(service, f.combat, f.tank, f.action)

    assert _hate(f) == {f.tank.participant_id: 10.0}
    assert f.combat.active_guard(f.healer.participant_id) is not None  # cover still lands
    switches.assert_not_awaited()


@pytest.mark.asyncio
async def test_a_new_protect_replaces_the_protectors_old_cover() -> None:
    f = _fight()
    mage = _p("Mage")
    f.combat.participants[mage.participant_id] = mage
    service, _, _, _ = _doubles(SuccessLevel.REGULAR)

    await combat_protect_action.resolve_protect_action(service, f.combat, f.tank, f.action)
    f.action.target_id = mage.participant_id
    await combat_protect_action.resolve_protect_action(service, f.combat, f.tank, f.action)

    assert f.combat.active_guard(f.healer.participant_id) is None
    assert f.combat.active_guard(mage.participant_id) is not None


@pytest.mark.asyncio
async def test_protect_is_dropped_when_the_ally_or_protector_is_out() -> None:
    service, roll, announce, _ = _doubles(SuccessLevel.EXTREME)

    gone = _fight()
    gone.action.target_id = uuid.uuid4()  # not in the fight at all
    await combat_protect_action.resolve_protect_action(service, gone.combat, gone.tank, gone.action)

    dead = _fight()
    dead.healer.current_dp = -10
    await combat_protect_action.resolve_protect_action(service, dead.combat, dead.tank, dead.action)

    npc = _fight()
    npc.action.target_id = npc.ghoul.participant_id  # an NPC is not an ally
    await combat_protect_action.resolve_protect_action(service, npc.combat, npc.tank, npc.action)

    self_cover = _fight()
    self_cover.action.target_id = self_cover.tank.participant_id
    await combat_protect_action.resolve_protect_action(service, self_cover.combat, self_cover.tank, self_cover.action)

    downed = _fight()
    downed.tank.current_dp = 0  # mortally wounded: cannot interpose
    await combat_protect_action.resolve_protect_action(service, downed.combat, downed.tank, downed.action)

    roll.assert_not_awaited()
    announce.assert_not_awaited()


@pytest.mark.asyncio
@pytest.mark.parametrize("room", ["r2", None])
async def test_the_protector_must_still_be_in_the_combat_room(room: str | None) -> None:
    f = _fight()
    service, roll, _, _ = _doubles(SuccessLevel.EXTREME, room=room)

    await combat_protect_action.resolve_protect_action(service, f.combat, f.tank, f.action)

    roll.assert_not_awaited()
    assert f.combat.active_guard(f.healer.participant_id) is None


@pytest.mark.asyncio
async def test_protect_is_skipped_when_no_skill_service_is_linked() -> None:
    f = _fight()
    service, _, announce, _ = _doubles(SuccessLevel.EXTREME, skill_linked=False)

    await combat_protect_action.resolve_protect_action(service, f.combat, f.tank, f.action)

    announce.assert_not_awaited()
    assert f.combat.active_guard(f.healer.participant_id) is None


@pytest.mark.asyncio
async def test_no_messaging_integration_still_resolves_the_protect() -> None:
    f = _fight()
    service, _, announce, _ = _doubles(SuccessLevel.REGULAR)
    service.get_npc_combat_integration_service = MagicMock(return_value=None)

    await combat_protect_action.resolve_protect_action(service, f.combat, f.tank, f.action)

    assert f.combat.active_guard(f.healer.participant_id) is not None
    announce.assert_not_awaited()


@pytest.mark.parametrize(
    ("level", "line"),
    [
        (SuccessLevel.EXTREME, "Ann throws themselves in front of Bo!"),
        (SuccessLevel.HARD, "Ann throws themselves in front of Bo!"),
        (SuccessLevel.REGULAR, "Ann throws themselves in front of Bo!"),
        (SuccessLevel.FAILURE, "Ann fails to reach Bo in time."),
        (SuccessLevel.FUMBLE, "Ann fails to reach Bo in time."),
    ],
)
def test_protect_outcome_lines(level: SuccessLevel, line: str) -> None:
    assert combat_protect_action.protect_outcome_line(level, "Ann", "Bo") == line


# --- intercept_for_guard -------------------------------------------------------------------------------------------


def _covered_fight() -> _Fight:
    f = _fight()
    f.combat.set_guard(f.healer.participant_id, f.tank.participant_id, expires_round=_ROUND + 1)
    return f


@pytest.mark.asyncio
async def test_an_npc_blow_at_a_covered_player_lands_on_the_protector() -> None:
    f = _covered_fight()
    service, _, announce, _ = _doubles(SuccessLevel.REGULAR)

    landed = await combat_protect_action.intercept_for_guard(service, f.combat, f.ghoul, f.healer, 10)

    assert landed is f.tank
    announce.assert_awaited_once_with("r1", str(f.combat.combat_id), "Tank takes the blow meant for Healer!")


@pytest.mark.asyncio
async def test_an_intercepted_blow_earns_the_protector_threat_with_the_guarding_multiplier() -> None:
    f = _covered_fight()
    service, _, _, _ = _doubles(SuccessLevel.REGULAR)

    _ = await combat_protect_action.intercept_for_guard(service, f.combat, f.ghoul, f.healer, 10)

    assert _hate(f)[f.tank.participant_id] == pytest.approx(25.0)  # 10 held + 10 damage * 1.5 guarding
    assert _hate(f)[f.healer.participant_id] == 50.0


@pytest.mark.asyncio
async def test_an_uncovered_player_takes_their_own_blow() -> None:
    f = _fight()
    service, _, announce, _ = _doubles(SuccessLevel.REGULAR)

    landed = await combat_protect_action.intercept_for_guard(service, f.combat, f.ghoul, f.healer, 10)

    assert landed is f.healer
    announce.assert_not_awaited()
    assert _hate(f)[f.tank.participant_id] == 10.0


@pytest.mark.asyncio
async def test_cover_that_has_run_out_no_longer_redirects() -> None:
    f = _covered_fight()
    f.combat.combat_round = _ROUND + 2
    service, _, announce, _ = _doubles(SuccessLevel.REGULAR)

    landed = await combat_protect_action.intercept_for_guard(service, f.combat, f.ghoul, f.healer, 10)

    assert landed is f.healer
    announce.assert_not_awaited()


@pytest.mark.asyncio
async def test_only_npc_attacks_on_players_are_redirected() -> None:
    f = _covered_fight()
    service, _, announce, _ = _doubles(SuccessLevel.REGULAR)

    player_attack = await combat_protect_action.intercept_for_guard(service, f.combat, f.tank, f.healer, 10)
    attack_on_npc = await combat_protect_action.intercept_for_guard(service, f.combat, f.healer, f.ghoul, 10)

    assert player_attack is f.healer
    assert attack_on_npc is f.ghoul
    announce.assert_not_awaited()


@pytest.mark.asyncio
async def test_a_redirect_happens_once_it_never_chains_to_the_protectors_own_guardian() -> None:
    f = _covered_fight()
    bodyguard = _p("Bodyguard")
    f.combat.participants[bodyguard.participant_id] = bodyguard
    f.combat.set_guard(f.tank.participant_id, bodyguard.participant_id, expires_round=_ROUND + 1)
    service, _, _, _ = _doubles(SuccessLevel.REGULAR)

    landed = await combat_protect_action.intercept_for_guard(service, f.combat, f.ghoul, f.healer, 10)

    assert landed is f.tank


@pytest.mark.asyncio
async def test_a_redirect_still_works_without_a_messaging_integration() -> None:
    f = _covered_fight()
    service, _, announce, _ = _doubles(SuccessLevel.REGULAR)
    service.get_npc_combat_integration_service = MagicMock(return_value=None)

    landed = await combat_protect_action.intercept_for_guard(service, f.combat, f.ghoul, f.healer, 10)

    assert landed is f.tank
    announce.assert_not_awaited()


# --- the turn processor dispatches the 'protect' action ------------------------------------------------------------


@pytest.mark.asyncio
async def test_turn_processor_dispatches_a_queued_protect_and_spends_the_turn() -> None:
    f = _fight()
    resolve: AsyncMock = AsyncMock()
    combat_service: MagicMock = MagicMock()
    processor = CombatTurnProcessor(combat_service)

    with patch.object(combat_protect_action, "resolve_protect_action", new=resolve):
        await processor._execute_queued_action(f.combat, f.tank, f.action, current_tick=77)

    resolve.assert_awaited_once_with(combat_service, f.combat, f.tank, f.action)
    assert f.tank.last_action_tick == 77


@pytest.mark.asyncio
async def test_a_failing_protect_does_not_break_the_round() -> None:
    f = _fight()
    resolve: AsyncMock = AsyncMock(side_effect=RuntimeError("db down"))
    processor = CombatTurnProcessor(MagicMock())

    with patch.object(combat_protect_action, "resolve_protect_action", new=resolve):
        await processor._execute_queued_action(f.combat, f.tank, f.action, current_tick=5)

    assert f.tank.last_action_tick == 5  # the turn is still spent and the round carries on
