"""#991: a participant giving Protect cover earns extra damage threat (the tank multiplier)."""

import uuid
from collections.abc import Iterator
from types import SimpleNamespace
from unittest.mock import patch

import pytest

from server.models.combat import CombatInstance, CombatParticipant, CombatParticipantType
from server.services import aggro_threat

_CONFIG = SimpleNamespace(aggro_damage_threat_multiplier=1.0, aggro_guarding_threat_multiplier=1.5)


def _participant(name: str, participant_type: CombatParticipantType) -> CombatParticipant:
    return CombatParticipant(
        participant_id=uuid.uuid4(),
        participant_type=participant_type,
        name=name,
        current_dp=50,
        max_dp=50,
        dexterity=10,
    )


def _fight() -> tuple[CombatInstance, CombatParticipant, CombatParticipant, CombatParticipant]:
    tank = _participant("Tank", CombatParticipantType.PLAYER)
    healer = _participant("Healer", CombatParticipantType.PLAYER)
    ghoul = _participant("Ghoul", CombatParticipantType.NPC)
    ghoul.npc_type = "aggressive_mob"
    combat = CombatInstance(
        room_id="room_1",
        participants={p.participant_id: p for p in (tank, healer, ghoul)},
        combat_round=3,
    )
    return combat, tank, healer, ghoul


def _threat(combat: CombatInstance, ghoul: CombatParticipant, source: CombatParticipant) -> float:
    return combat.npc_hate_lists[ghoul.participant_id][source.participant_id]


@pytest.fixture(autouse=True)
def _config() -> Iterator[None]:
    with patch.object(aggro_threat, "_get_aggro_config", return_value=_CONFIG):
        yield


def test_damage_threat_is_unchanged_without_cover() -> None:
    combat, tank, _healer, ghoul = _fight()
    aggro_threat.add_damage_threat(combat, ghoul.participant_id, tank.participant_id, 10.0, npc_participant=ghoul)
    assert _threat(combat, ghoul, tank) == 10.0


def test_a_protector_earns_the_guarding_multiplier() -> None:
    combat, tank, healer, ghoul = _fight()
    combat.set_guard(healer.participant_id, tank.participant_id, expires_round=4)
    aggro_threat.add_damage_threat(combat, ghoul.participant_id, tank.participant_id, 10.0, npc_participant=ghoul)
    assert _threat(combat, ghoul, tank) == 15.0


def test_only_the_protector_gets_the_multiplier_not_the_ally() -> None:
    combat, tank, healer, ghoul = _fight()
    combat.set_guard(healer.participant_id, tank.participant_id, expires_round=4)
    aggro_threat.add_damage_threat(combat, ghoul.participant_id, healer.participant_id, 10.0, npc_participant=ghoul)
    assert _threat(combat, ghoul, healer) == 10.0


def test_the_multiplier_stacks_with_an_explicit_multiplier() -> None:
    combat, tank, healer, ghoul = _fight()
    combat.set_guard(healer.participant_id, tank.participant_id, expires_round=4)
    aggro_threat.add_damage_threat(
        combat, ghoul.participant_id, tank.participant_id, 10.0, multiplier=2.0, npc_participant=ghoul
    )
    assert _threat(combat, ghoul, tank) == 30.0


def test_the_multiplier_ends_with_the_cover() -> None:
    combat, tank, healer, ghoul = _fight()
    combat.set_guard(healer.participant_id, tank.participant_id, expires_round=3)
    combat.combat_round = 4
    aggro_threat.add_damage_threat(combat, ghoul.participant_id, tank.participant_id, 10.0, npc_participant=ghoul)
    assert _threat(combat, ghoul, tank) == 10.0


def test_the_multiplier_ends_when_the_protector_is_down() -> None:
    combat, tank, healer, ghoul = _fight()
    combat.set_guard(healer.participant_id, tank.participant_id, expires_round=9)
    tank.current_dp = 0
    aggro_threat.add_damage_threat(combat, ghoul.participant_id, tank.participant_id, 10.0, npc_participant=ghoul)
    assert _threat(combat, ghoul, tank) == 10.0
