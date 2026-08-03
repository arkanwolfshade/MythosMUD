"""Unit tests for CombatService process_attack flow and private helper methods."""

import uuid
from unittest.mock import AsyncMock, MagicMock, patch

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

    # Patch validate_melee_location to return valid
    service.validate_melee_location = AsyncMock(return_value=(True, None))  # type: ignore[assignment]
    service.end_combat = AsyncMock()  # type: ignore[assignment]

    result = await service.validate_melee_or_end_combat(
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

    service.validate_melee_location = AsyncMock(return_value=(False, reason))  # type: ignore[assignment]
    service.end_combat = AsyncMock()  # type: ignore[assignment]

    result = await service.validate_melee_or_end_combat(
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

    service.apply_attack_damage = AsyncMock(return_value=(5, False, False))  # type: ignore[assignment]
    service.check_involuntary_flee = AsyncMock()  # type: ignore[assignment]

    target_died, mortally_wounded, early = await service.apply_damage_and_check_involuntary_flee(
        combat, attacker, target, damage=7
    )

    assert target_died is False
    assert mortally_wounded is False
    assert early is None
    service.check_involuntary_flee.assert_not_awaited()  # type: ignore[attr-defined]


@pytest.mark.asyncio
async def test_apply_damage_and_check_involuntary_flee_returns_early_result_on_flee() -> None:
    """When involuntary flee triggers, combat ends and an early CombatResult is returned."""
    service = _make_service()
    combat = _make_combat_instance()
    attacker = _make_participant("Attacker")
    target = _make_participant("Victim", participant_type=CombatParticipantType.PLAYER)

    service.apply_attack_damage = AsyncMock(return_value=(5, False, False))  # type: ignore[assignment]
    service.check_involuntary_flee = AsyncMock(return_value=True)  # type: ignore[assignment]
    service.end_combat = AsyncMock()  # type: ignore[assignment]

    target_died, mortally_wounded, early = await service.apply_damage_and_check_involuntary_flee(
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
    """finalize_attack_result wires target state, events, XP, and completion correctly."""
    service = _make_service()
    combat = _make_combat_instance()
    attacker = _make_participant("Attacker")
    target = _make_participant("Target")
    damage = 7
    target_died = True
    target_mortally_wounded = False
    target_id = uuid.uuid4()

    combat.is_combat_over = MagicMock(return_value=True)  # type: ignore[assignment]
    service.handle_target_state_changes = AsyncMock()  # type: ignore[assignment]
    service.handle_attack_events_and_xp = AsyncMock(return_value=42)  # type: ignore[assignment]
    service.award_xp_to_player = AsyncMock()  # type: ignore[assignment]
    service.handle_combat_completion = AsyncMock()  # type: ignore[assignment]

    result = await service.finalize_attack_result(
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
    service.handle_target_state_changes.assert_awaited_once()  # type: ignore[attr-defined]
    service.handle_attack_events_and_xp.assert_awaited_once()  # type: ignore[attr-defined]
    service.award_xp_to_player.assert_awaited_once_with(attacker, target, target_id, 42)  # type: ignore[attr-defined]
    service.handle_combat_completion.assert_awaited_once_with(combat, True)  # type: ignore[attr-defined]


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

    service.validate_and_get_combat_participants = AsyncMock(  # type: ignore[assignment]
        return_value=(combat, attacker, target),
    )
    service.validate_melee_or_end_combat = AsyncMock(return_value=early_result)  # type: ignore[assignment]

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

    service.validate_and_get_combat_participants = AsyncMock(  # type: ignore[assignment]
        return_value=(combat, attacker, target),
    )
    service.validate_melee_or_end_combat = AsyncMock(return_value=None)  # type: ignore[assignment]
    service.apply_damage_and_check_involuntary_flee = AsyncMock(  # type: ignore[assignment]
        return_value=(False, False, None),
    )
    service.finalize_attack_result = AsyncMock(return_value=final_result)  # type: ignore[assignment]

    result = await service.process_attack(attacker_id, target_id, damage=5)

    assert result is final_result
    service.validate_and_get_combat_participants.assert_awaited_once()  # type: ignore[attr-defined]
    service.validate_melee_or_end_combat.assert_awaited_once()  # type: ignore[attr-defined]
    service.apply_damage_and_check_involuntary_flee.assert_awaited_once()  # type: ignore[attr-defined]
    service.finalize_attack_result.assert_awaited_once()  # type: ignore[attr-defined]


def test_combat_service_property_getters_setters() -> None:
    """Auto-progression and turn interval properties round-trip."""
    service = _make_service()
    service.auto_progression_enabled = False
    service.turn_interval_seconds = 45
    assert service.auto_progression_enabled is False
    assert service.turn_interval_seconds == 45


def test_get_combat_returns_active_instance() -> None:
    """get_combat returns combat stored in active combats."""
    service = _make_service()
    combat = _make_combat_instance()
    service._active_combats[combat.combat_id] = combat
    assert service.get_combat(combat.combat_id) is combat
    assert service.get_combat(uuid.uuid4()) is None


def test_get_combat_id_for_participant() -> None:
    """Participant lookup returns combat id when registered."""
    service = _make_service()
    combat_id = uuid.uuid4()
    participant_id = uuid.uuid4()
    service._player_combats[participant_id] = combat_id
    assert service.get_combat_id_for_participant(participant_id) == combat_id
    assert service.get_combat_id_for_participant(uuid.uuid4()) is None


def test_is_npc_in_combat_sync() -> None:
    """NPC string id resolves via UUID mapping."""
    service = _make_service()
    npc_uuid = uuid.uuid4()
    combat_id = uuid.uuid4()
    service._npc_combats[npc_uuid] = combat_id
    assert service.is_npc_in_combat_sync(str(npc_uuid)) is True
    assert service.is_npc_in_combat_sync("not-in-combat") is False


def test_sync_npc_participant_dp_after_spell_damage() -> None:
    """Spell damage sync updates NPC participant DP in active combat."""
    service = _make_service()
    combat = _make_combat_instance()
    npc_id = uuid.uuid4()
    npc = _make_participant("NPC", participant_type=CombatParticipantType.NPC)
    npc.participant_id = npc_id
    combat.participants[npc_id] = npc
    service._active_combats[combat.combat_id] = combat
    service._npc_combats[npc_id] = combat.combat_id
    service.sync_npc_participant_dp_after_spell_damage(str(npc_id), 3)
    assert npc.current_dp == 3


def test_get_npc_combat_integration_service_round_trip() -> None:
    """Getter/setter for NPC combat integration service."""
    service = _make_service()
    integration = MagicMock()
    service.set_npc_combat_integration_service(integration)
    assert service.get_npc_combat_integration_service() is integration


@pytest.mark.asyncio
async def test_publish_npc_damage_event_delegates() -> None:
    """publish_npc_damage_event forwards to events module."""
    service = _make_service()
    with patch(
        "server.services.combat_service_events.publish_npc_damage_event",
        new=AsyncMock(return_value=True),
    ) as mock_impl:
        result = await service.publish_npc_damage_event("room_1", "npc_1", "Goblin", 5, 10, 20)
    assert result is True
    mock_impl.assert_awaited_once()


@pytest.mark.asyncio
async def test_publish_npc_died_event_delegates() -> None:
    """publish_npc_died_event forwards to events module."""
    service = _make_service()
    with patch(
        "server.services.combat_service_events.publish_npc_died_event",
        new=AsyncMock(return_value=True),
    ) as mock_impl:
        result = await service.publish_npc_died_event("room_1", "npc_1", "Goblin", xp_reward=10)
    assert result is True
    mock_impl.assert_awaited_once()


@pytest.mark.asyncio
async def test_end_combat_if_npc_died() -> None:
    """end_combat_if_npc_died ends combat when NPC is tracked."""
    service = _make_service()
    npc_uuid = uuid.uuid4()
    combat_id = uuid.uuid4()
    service._npc_combats[npc_uuid] = combat_id
    service.end_combat = AsyncMock()  # type: ignore[method-assign]
    ended = await service.end_combat_if_npc_died(npc_uuid)
    assert ended is True
    service.end_combat.assert_awaited_once_with(combat_id, "Combat ended - NPC slain")  # type: ignore[attr-defined]


@pytest.mark.asyncio
async def test_end_combat_if_npc_died_not_in_combat() -> None:
    """end_combat_if_npc_died returns False when NPC not in combat."""
    service = _make_service()
    assert await service.end_combat_if_npc_died("unknown") is False


@pytest.mark.asyncio
async def test_process_game_tick_delegates() -> None:
    """process_game_tick forwards to turn processor."""
    service = _make_service()
    service._turn_processor.process_game_tick = AsyncMock()  # type: ignore[method-assign]
    await service.process_game_tick(42)
    service._turn_processor.process_game_tick.assert_awaited_once()  # type: ignore[attr-defined]


def test_set_player_combat_service() -> None:
    """Player combat service can be replaced after init."""
    service = _make_service()
    pcs = MagicMock()
    service.set_player_combat_service(pcs)
    assert service._player_combat_service is pcs


def test_get_combat_id_for_npc_uuid() -> None:
    """UUID npc lookup returns combat id."""
    service = _make_service()
    npc_uuid = uuid.uuid4()
    combat_id = uuid.uuid4()
    service._npc_combats[npc_uuid] = combat_id
    assert service.get_combat_id_for_npc_uuid(npc_uuid) == combat_id


@pytest.mark.asyncio
async def test_get_combat_by_participant_returns_active_combat() -> None:
    """get_combat_by_participant resolves combat via participant mapping."""
    service = _make_service()
    combat = _make_combat_instance()
    participant_id = uuid.uuid4()
    service._active_combats[combat.combat_id] = combat
    service._player_combats[participant_id] = combat.combat_id
    result = await service.get_combat_by_participant(participant_id)
    assert result is combat


@pytest.mark.asyncio
async def test_broadcast_aggro_target_switches_delegates() -> None:
    """Aggro switch broadcast delegates to events module."""
    service = _make_service()
    combat_id = uuid.uuid4()
    switches = [(uuid.uuid4(), "Wolf", "Alice")]
    with patch(
        "server.services.combat_service_events.broadcast_aggro_target_switches",
        new=AsyncMock(),
    ) as mock_impl:
        await service.broadcast_aggro_target_switches("room_1", combat_id, switches)
    mock_impl.assert_awaited_once()


@pytest.mark.asyncio
async def test_register_combat_state_tracks_participants() -> None:
    """register_combat_state stores combat and notifies player combat service."""
    service = _make_service()
    pcs = MagicMock()
    pcs.track_player_combat_state = AsyncMock()
    service.set_player_combat_service(pcs)
    combat = _make_combat_instance()
    attacker = _make_participant("Attacker")
    target = _make_participant("Target", participant_type=CombatParticipantType.NPC)
    combat.participants = {attacker.participant_id: attacker, target.participant_id: target}
    await service.register_combat_state(combat, attacker.participant_id, attacker.name, "room_001")
    assert service.get_combat(combat.combat_id) is combat
    pcs.track_player_combat_state.assert_awaited_once()


@pytest.mark.asyncio
async def test_notify_player_combat_ended() -> None:
    """notify_player_combat_ended calls player combat service."""
    service = _make_service()
    pcs = MagicMock()
    pcs.handle_combat_end = AsyncMock()
    service.set_player_combat_service(pcs)
    combat_id = uuid.uuid4()
    await service.notify_player_combat_ended(combat_id)
    pcs.handle_combat_end.assert_awaited_once_with(combat_id)


def test_cleanup_combat_tracking_and_connection_state() -> None:
    """Cleanup handler methods are invoked."""
    service = _make_service()
    combat = _make_combat_instance()
    service._cleanup_handler.cleanup_combat_tracking = MagicMock()  # type: ignore[method-assign]
    service._cleanup_handler.check_connection_state = MagicMock()  # type: ignore[method-assign]
    service.cleanup_combat_tracking(combat)
    service.check_connection_state("room_001")
    service._cleanup_handler.cleanup_combat_tracking.assert_called_once_with(combat)  # type: ignore[attr-defined]
    service._cleanup_handler.check_connection_state.assert_called_once_with("room_001")  # type: ignore[attr-defined]


@pytest.mark.asyncio
async def test_start_combat_happy_path() -> None:
    """start_combat wires validation, registration, and publish."""
    service = _make_service()
    attacker_data = MagicMock()
    attacker_data.name = "Attacker"
    target_data = MagicMock()
    target_data.name = "Target"
    combat = _make_combat_instance()
    with (
        patch(
            "server.services.combat_service_start.check_target_rest_and_grace_period",
            new=AsyncMock(),
        ),
        patch(
            "server.services.combat_service_start.check_attacker_grace_period",
            new=AsyncMock(),
        ),
        patch(
            "server.services.combat_service_start.validate_combat_can_start",
            new=AsyncMock(),
        ),
        patch(
            "server.services.combat_service.CombatInitializer.create_combat_instance",
            return_value=combat,
        ),
        patch(
            "server.services.combat_service_start.register_combat",
            new=AsyncMock(),
        ),
        patch(
            "server.services.combat_service_start.publish_combat_started_event",
            new=AsyncMock(),
        ),
    ):
        result = await service.start_combat("room_001", attacker_data, target_data, current_tick=1)
    assert result is combat
