"""#991: Protect cover is checked on read, so it lapses on its own and needs no cleanup."""

import uuid

from server.models.combat import CombatInstance, CombatParticipant, CombatParticipantType


def _player(name: str, current_dp: int = 50) -> CombatParticipant:
    return CombatParticipant(
        participant_id=uuid.uuid4(),
        participant_type=CombatParticipantType.PLAYER,
        name=name,
        current_dp=current_dp,
        max_dp=50,
        dexterity=10,
    )


def _fight(*players: CombatParticipant, combat_round: int = 3) -> CombatInstance:
    return CombatInstance(
        room_id="room_1",
        participants={p.participant_id: p for p in players},
        combat_round=combat_round,
    )


def test_no_guard_by_default() -> None:
    tank, healer = _player("Tank"), _player("Healer")
    combat = _fight(tank, healer)
    assert combat.active_guard(healer.participant_id) is None
    assert not combat.is_guarding(tank.participant_id)


def test_set_guard_covers_the_ally_and_marks_the_protector() -> None:
    tank, healer = _player("Tank"), _player("Healer")
    combat = _fight(tank, healer)
    combat.set_guard(healer.participant_id, tank.participant_id, expires_round=4)
    guard = combat.active_guard(healer.participant_id)
    assert guard is not None
    assert guard.protector_id == tank.participant_id
    assert combat.is_guarding(tank.participant_id)
    assert not combat.is_guarding(healer.participant_id)
    assert combat.active_guard(tank.participant_id) is None


def test_cover_holds_through_its_last_round_then_lapses() -> None:
    tank, healer = _player("Tank"), _player("Healer")
    combat = _fight(tank, healer, combat_round=4)
    combat.set_guard(healer.participant_id, tank.participant_id, expires_round=4)
    assert combat.active_guard(healer.participant_id) is not None
    combat.combat_round = 5
    assert combat.active_guard(healer.participant_id) is None
    assert not combat.is_guarding(tank.participant_id)


def test_cover_ends_when_the_protector_drops_to_zero_dp() -> None:
    tank, healer = _player("Tank"), _player("Healer")
    combat = _fight(tank, healer)
    combat.set_guard(healer.participant_id, tank.participant_id, expires_round=9)
    tank.current_dp = 0
    assert combat.active_guard(healer.participant_id) is None
    assert not combat.is_guarding(tank.participant_id)


def test_cover_ends_when_the_protector_leaves_the_fight() -> None:
    tank, healer = _player("Tank"), _player("Healer")
    combat = _fight(tank, healer)
    combat.set_guard(healer.participant_id, tank.participant_id, expires_round=9)
    del combat.participants[tank.participant_id]
    assert combat.active_guard(healer.participant_id) is None


def test_cover_ends_when_the_ally_leaves_the_fight() -> None:
    tank, healer = _player("Tank"), _player("Healer")
    combat = _fight(tank, healer)
    combat.set_guard(healer.participant_id, tank.participant_id, expires_round=9)
    del combat.participants[healer.participant_id]
    assert combat.active_guard(healer.participant_id) is None
    assert not combat.is_guarding(tank.participant_id)


def test_an_ally_has_one_protector_and_the_latest_wins() -> None:
    first, second, healer = _player("First"), _player("Second"), _player("Healer")
    combat = _fight(first, second, healer)
    combat.set_guard(healer.participant_id, first.participant_id, expires_round=9)
    combat.set_guard(healer.participant_id, second.participant_id, expires_round=9)
    guard = combat.active_guard(healer.participant_id)
    assert guard is not None
    assert guard.protector_id == second.participant_id
    assert not combat.is_guarding(first.participant_id)


def test_a_protector_covers_one_ally_and_the_latest_wins() -> None:
    tank, healer, mage = _player("Tank"), _player("Healer"), _player("Mage")
    combat = _fight(tank, healer, mage)
    combat.set_guard(healer.participant_id, tank.participant_id, expires_round=9)
    combat.set_guard(mage.participant_id, tank.participant_id, expires_round=9)
    assert combat.active_guard(healer.participant_id) is None
    assert combat.active_guard(mage.participant_id) is not None
