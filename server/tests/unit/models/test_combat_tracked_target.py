"""CombatInstance.living_tracked_target (#1006): the one rule auto-attack and assist share for "who am I hitting"."""

import uuid

from server.models.combat import CombatInstance, CombatParticipant, CombatParticipantType


def _p(name: str, ptype: CombatParticipantType, current_dp: int = 50) -> CombatParticipant:
    return CombatParticipant(
        participant_id=uuid.uuid4(), participant_type=ptype, name=name, current_dp=current_dp, max_dp=50, dexterity=10
    )


def _fight() -> tuple[CombatInstance, CombatParticipant, CombatParticipant]:
    player, ghoul = _p("Ashcroft", CombatParticipantType.PLAYER), _p("Ghoul", CombatParticipantType.NPC)
    combat = CombatInstance(room_id="r1", participants={p.participant_id: p for p in (player, ghoul)})
    return combat, player, ghoul


def test_no_tracked_target_is_none() -> None:
    combat, player, _ghoul = _fight()
    assert combat.living_tracked_target(player.participant_id) is None


def test_a_living_tracked_target_is_returned() -> None:
    combat, player, ghoul = _fight()
    combat.player_current_target[player.participant_id] = ghoul.participant_id
    assert combat.living_tracked_target(player.participant_id) is ghoul


def test_a_dead_tracked_target_is_none() -> None:
    combat, player, ghoul = _fight()
    combat.player_current_target[player.participant_id] = ghoul.participant_id
    ghoul.current_dp = 0
    assert combat.living_tracked_target(player.participant_id) is None


def test_a_tracked_target_no_longer_in_the_fight_is_none() -> None:
    combat, player, ghoul = _fight()
    combat.player_current_target[player.participant_id] = ghoul.participant_id
    del combat.participants[ghoul.participant_id]
    assert combat.living_tracked_target(player.participant_id) is None
