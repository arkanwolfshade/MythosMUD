"""Unit tests for combat_service_end.remove_participant (#833, #1058)."""

import uuid
from unittest.mock import AsyncMock, MagicMock

import pytest

from server.models.combat import CombatInstance, CombatParticipant, CombatParticipantType
from server.services import combat_service_end


def _fighter(name: str, dp: int, ptype: CombatParticipantType = CombatParticipantType.PLAYER) -> CombatParticipant:
    return CombatParticipant(
        participant_id=uuid.uuid4(), participant_type=ptype, name=name, current_dp=dp, max_dp=50, dexterity=10
    )


def _service(combat: CombatInstance, untrack: AsyncMock | None = None) -> MagicMock:
    service = MagicMock()
    service.get_combat = MagicMock(return_value=combat)
    service.untrack_participant = untrack or AsyncMock()
    return service


def _combat(*fighters: CombatParticipant) -> CombatInstance:
    combat = CombatInstance(
        combat_id=uuid.uuid4(), room_id="room_001", participants={f.participant_id: f for f in fighters}
    )
    combat.turn_order = list(combat.participants)
    return combat


@pytest.mark.asyncio
async def test_downed_last_player_ends_the_combat(monkeypatch: pytest.MonkeyPatch) -> None:
    """#1058: the only player going down ends the fight, so the NPC stops and the bleed-out can run."""
    victim = _fighter("Victim", 0)
    combat = _combat(victim, _fighter("Patient", 30, CombatParticipantType.NPC))
    end_combat = AsyncMock()
    monkeypatch.setattr(combat_service_end, "end_combat", end_combat)

    ended = await combat_service_end.remove_participant(_service(combat), combat.combat_id, victim.participant_id)

    assert ended is True
    end_combat.assert_awaited_once()


@pytest.mark.asyncio
async def test_mortally_wounded_ally_does_not_keep_the_combat_alive(monkeypatch: pytest.MonkeyPatch) -> None:
    """#1058: a 0 DP ally cannot act, so the other player going down still ends the fight."""
    victim = _fighter("Victim", 0)
    downed_ally = _fighter("Ally", -4)
    combat = _combat(victim, downed_ally, _fighter("Patient", 30, CombatParticipantType.NPC))
    end_combat = AsyncMock()
    monkeypatch.setattr(combat_service_end, "end_combat", end_combat)

    ended = await combat_service_end.remove_participant(_service(combat), combat.combat_id, victim.participant_id)

    assert ended is True
    end_combat.assert_awaited_once()


@pytest.mark.asyncio
async def test_downed_player_leaves_while_a_standing_ally_keeps_fighting(monkeypatch: pytest.MonkeyPatch) -> None:
    """#1058: with an ally still on their feet the fight continues, minus the downed player."""
    victim = _fighter("Victim", 0)
    ally = _fighter("Ally", 40)
    patient = _fighter("Patient", 30, CombatParticipantType.NPC)
    combat = _combat(victim, ally, patient)
    untrack: AsyncMock = AsyncMock()
    service = _service(combat, untrack)
    end_combat = AsyncMock()
    monkeypatch.setattr(combat_service_end, "end_combat", end_combat)

    ended = await combat_service_end.remove_participant(service, combat.combat_id, victim.participant_id)

    assert ended is False
    end_combat.assert_not_awaited()
    assert victim.participant_id not in combat.participants
    assert victim.participant_id not in combat.turn_order
    assert {ally.participant_id, patient.participant_id} == set(combat.participants)
    untrack.assert_awaited_once_with(victim.participant_id)
