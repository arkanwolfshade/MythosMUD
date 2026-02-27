"""Unit tests for CombatService process_attack flow and private helper methods."""

import uuid
from unittest.mock import AsyncMock, MagicMock

import pytest

from server.models.combat import CombatInstance, CombatParticipant, CombatParticipantType, CombatResult
from server.services.combat_service import CombatService

# pylint: disable=protected-access  # Reason: Test file - accessing protected members is standard practice for unit testing
# pylint: disable=redefined-outer-name  # Reason: Test file - pytest fixture parameter names must match fixture names, causing intentional redefinitions


def _make_combat_instance() -> CombatInstance:
    combat = CombatInstance(
        combat_id=uuid.uuid4(),
        room_id="room_001",
        participants={},
    )
    return combat


def _make_participant(
    name: str, participant_type: CombatParticipantType = CombatParticipantType.PLAYER
) -> CombatParticipant:
    return CombatParticipant(
        participant_id=uuid.uuid4(),
        participant_type=participant_type,
        name=name,
        current_dp=10,
        max_dp=20,
        dexterity=10,
    )


def _make_service() -> CombatService:
    # Use MagicMocks for constructor dependencies to avoid external side effects.
    player_combat_service = MagicMock()
    nats_service = MagicMock()
    npc_integration = MagicMock()
    subject_manager = MagicMock()
    event_bus = MagicMock()
    return CombatService(
        player_combat_service=player_combat_service,
        nats_service=nats_service,
        npc_combat_integration_service=npc_integration,
        subject_manager=subject_manager,
        event_bus=event_bus,
    )


@pytest.mark.asyncio
async def test_validate_melee_or_end_combat_returns_none_on_valid() -> None:
    """When melee validation passes, helper returns None and does not end combat."""
    service = _make_service()
    combat = _make_combat_instance()
    attacker = _make_participant("Attacker")
    target = _make_participant("Target")

    # Patch _validate_melee_location to return valid
    service._validate_melee_location = AsyncMock(return_value=(True, None))  # type: ignore[assignment]
    service.end_combat = AsyncMock()  # type: ignore[assignment]

    result = await service._validate_melee_or_end_combat(  # type: ignore[attr-defined]
        combat, attacker, target, attacker.participant_id, target.participant_id
    )

    assert result is None
    service.end_combat.assert_not_awaited()  # type: ignore[attr-defined]


@pytest.mark.asyncio
async def test_validate_melee_or_end_combat_ends_combat_on_invalid() -> None:
    """When melee validation fails, combat is ended and a failure CombatResult is returned."""
    service = _make_service()
    combat = _make_combat_instance()
    attacker = _make_participant("Attacker")
    target = _make_participant("Target")
    reason = "rooms do not match"

    service._validate_melee_location = AsyncMock(return_value=(False, reason))  # type: ignore[assignment]
    service.end_combat = AsyncMock()  # type: ignore[assignment]

    result = await service._validate_melee_or_end_combat(  # type: ignore[attr-defined]
        combat, attacker, target, attacker.participant_id, target.participant_id
    )

    assert isinstance(result, CombatResult)
    assert result.success is False
    assert result.combat_ended is True
    assert result.damage == 0
    assert result.message == reason
    service.end_combat.assert_awaited_once_with(combat.combat_id, reason)  # type: ignore[attr-defined]


@pytest.mark.asyncio
async def test_apply_damage_and_check_involuntary_flee_no_flee_for_npc() -> None:
    """NPC targets never trigger involuntary flee logic."""
    service = _make_service()
    combat = _make_combat_instance()
    attacker = _make_participant("Attacker")
    target = _make_participant("NPC", participant_type=CombatParticipantType.NPC)

    service._apply_attack_damage = AsyncMock(return_value=(5, False, False))  # type: ignore[assignment]
    service._check_involuntary_flee = AsyncMock()  # type: ignore[assignment]

    target_died, mortally_wounded, early = await service._apply_damage_and_check_involuntary_flee(  # type: ignore[attr-defined]
        combat, attacker, target, damage=7
    )

    assert target_died is False
    assert mortally_wounded is False
    assert early is None
    service._check_involuntary_flee.assert_not_awaited()  # type: ignore[attr-defined]


@pytest.mark.asyncio
async def test_apply_damage_and_check_involuntary_flee_returns_early_result_on_flee() -> None:
    """When involuntary flee triggers, combat ends and an early CombatResult is returned."""
    service = _make_service()
    combat = _make_combat_instance()
    attacker = _make_participant("Attacker")
    target = _make_participant("Victim", participant_type=CombatParticipantType.PLAYER)

    service._apply_attack_damage = AsyncMock(return_value=(5, False, False))  # type: ignore[assignment]
    service._check_involuntary_flee = AsyncMock(return_value=True)  # type: ignore[assignment]
    service.end_combat = AsyncMock()  # type: ignore[assignment]

    target_died, mortally_wounded, early = await service._apply_damage_and_check_involuntary_flee(  # type: ignore[attr-defined]
        combat, attacker, target, damage=7
    )

    assert target_died is False
    assert mortally_wounded is False
    assert isinstance(early, CombatResult)
    assert early.success is True
    assert early.combat_ended is True
    assert "flee" in (early.message or "").lower()
    service.end_combat.assert_awaited_once()  # type: ignore[attr-defined]


@pytest.mark.asyncio
async def test_finalize_attack_result_awards_xp_and_completes_combat() -> None:
    """_finalize_attack_result wires target state, events, XP, and completion correctly."""
    service = _make_service()
    combat = _make_combat_instance()
    attacker = _make_participant("Attacker")
    target = _make_participant("Target")
    damage = 7
    target_died = True
    target_mortally_wounded = False
    target_id = uuid.uuid4()

    combat.is_combat_over = MagicMock(return_value=True)  # type: ignore[assignment]
    service._handle_target_state_changes = AsyncMock()  # type: ignore[assignment]
    service._handle_attack_events_and_xp = AsyncMock(return_value=42)  # type: ignore[assignment]
    service._award_xp_to_player = AsyncMock()  # type: ignore[assignment]
    service._handle_combat_completion = AsyncMock()  # type: ignore[assignment]

    result = await service._finalize_attack_result(  # type: ignore[attr-defined]
        combat,
        attacker,
        target,
        damage,
        target_died,
        target_mortally_wounded,
        target_id,
    )

    assert isinstance(result, CombatResult)
    assert result.success is True
    assert result.damage == damage
    assert result.target_died is True
    assert result.combat_ended is True
    assert result.xp_awarded == 42
    service._handle_target_state_changes.assert_awaited_once()  # type: ignore[attr-defined]
    service._handle_attack_events_and_xp.assert_awaited_once()  # type: ignore[attr-defined]
    service._award_xp_to_player.assert_awaited_once_with(attacker, target, target_id, 42)  # type: ignore[attr-defined]
    service._handle_combat_completion.assert_awaited_once_with(combat, True)  # type: ignore[attr-defined]


@pytest.mark.asyncio
async def test_process_attack_returns_melee_validation_early_result() -> None:
    """process_attack returns early CombatResult when melee validation ends combat."""
    service = _make_service()
    attacker_id = uuid.uuid4()
    target_id = uuid.uuid4()

    combat = _make_combat_instance()
    attacker = _make_participant("Attacker")
    target = _make_participant("Target")

    early_result = CombatResult(
        success=False,
        damage=0,
        target_died=False,
        combat_ended=True,
        message="melee invalid",
        combat_id=combat.combat_id,
    )

    service._validate_and_get_combat_participants = AsyncMock(  # type: ignore[assignment]
        return_value=(combat, attacker, target),
    )
    service._validate_melee_or_end_combat = AsyncMock(return_value=early_result)  # type: ignore[assignment]

    result = await service.process_attack(attacker_id, target_id, damage=5)

    assert result is early_result


@pytest.mark.asyncio
async def test_process_attack_happy_path_calls_helpers_and_returns_final_result() -> None:
    """process_attack orchestrates helper calls and returns the final CombatResult."""
    service = _make_service()
    attacker_id = uuid.uuid4()
    target_id = uuid.uuid4()

    combat = _make_combat_instance()
    attacker = _make_participant("Attacker")
    target = _make_participant("Target")

    final_result = CombatResult(
        success=True,
        damage=5,
        target_died=False,
        combat_ended=False,
        message="ok",
        combat_id=combat.combat_id,
    )

    service._validate_and_get_combat_participants = AsyncMock(  # type: ignore[assignment]
        return_value=(combat, attacker, target),
    )
    service._validate_melee_or_end_combat = AsyncMock(return_value=None)  # type: ignore[assignment]
    service._apply_damage_and_check_involuntary_flee = AsyncMock(  # type: ignore[assignment]
        return_value=(False, False, None),
    )
    service._finalize_attack_result = AsyncMock(return_value=final_result)  # type: ignore[assignment]

    result = await service.process_attack(attacker_id, target_id, damage=5)

    assert result is final_result
    service._validate_and_get_combat_participants.assert_awaited_once()  # type: ignore[attr-defined]
    service._validate_melee_or_end_combat.assert_awaited_once()  # type: ignore[attr-defined]
    service._apply_damage_and_check_involuntary_flee.assert_awaited_once()  # type: ignore[attr-defined]
    service._finalize_attack_result.assert_awaited_once()  # type: ignore[attr-defined]
