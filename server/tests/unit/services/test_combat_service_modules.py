"""Unit tests for combat_service_start, combat_service_end, and combat_service_events."""

import asyncio
import uuid
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from server.exceptions import DatabaseError
from server.models.combat import CombatInstance, CombatParticipant, CombatParticipantType, CombatStatus
from server.services import (
    combat_service_attack,
    combat_service_end,
    combat_service_events,
    combat_service_start,
)
from server.services.combat_hp_sync import CombatDPSync
from server.services.combat_types import CombatParticipantData
from server.services.nats_exceptions import NATSError


def _participant(
    name: str = "Attacker", ptype: CombatParticipantType = CombatParticipantType.PLAYER
) -> CombatParticipantData:
    return CombatParticipantData(
        participant_id=uuid.uuid4(),
        name=name,
        current_dp=10,
        max_dp=20,
        dexterity=10,
        participant_type=ptype,
    )


def _combat_instance() -> CombatInstance:
    combat_id = uuid.uuid4()
    participant = CombatParticipant(
        participant_id=uuid.uuid4(),
        participant_type=CombatParticipantType.PLAYER,
        name="Fighter",
        current_dp=10,
        max_dp=20,
        dexterity=10,
    )
    combat = CombatInstance(
        combat_id=combat_id, room_id="room_001", participants={participant.participant_id: participant}
    )
    combat.turn_order = [participant.participant_id]
    return combat


@pytest.mark.asyncio
async def test_validate_combat_can_start_raises_when_in_combat() -> None:
    """Cannot start combat when either participant is already fighting."""
    service = MagicMock()
    attacker = _participant("Attacker")
    target = _participant("Target")
    service.get_combat_by_participant = AsyncMock(side_effect=[MagicMock(), None])

    with pytest.raises(ValueError, match="already in combat"):
        await combat_service_start.validate_combat_can_start(service, attacker, target)


@pytest.mark.asyncio
async def test_validate_combat_can_start_ok() -> None:
    """Validation passes when neither participant is in combat."""
    service = MagicMock()
    service.get_combat_by_participant = AsyncMock(return_value=None)
    await combat_service_start.validate_combat_can_start(service, _participant(), _participant("Target"))


@pytest.mark.asyncio
async def test_register_combat_delegates_to_service() -> None:
    """register_combat forwards to register_combat_state."""
    service = MagicMock()
    service.register_combat_state = AsyncMock()
    combat = _combat_instance()
    attacker = _participant()
    await combat_service_start.register_combat(service, combat, attacker, "room_001")
    service.register_combat_state.assert_awaited_once_with(combat, attacker.participant_id, attacker.name, "room_001")


@pytest.mark.asyncio
async def test_publish_combat_started_event_success() -> None:
    """Combat started event is built and published."""
    service = MagicMock()
    service.publish_combat_started_event = AsyncMock()
    combat = _combat_instance()
    await combat_service_start.publish_combat_started_event(service, combat, "room_001")
    service.publish_combat_started_event.assert_awaited_once()


@pytest.mark.asyncio
async def test_publish_combat_started_event_handles_errors() -> None:
    """Publish errors are logged, not raised."""
    service = MagicMock()
    service.publish_combat_started_event = AsyncMock(side_effect=RuntimeError("nats down"))
    await combat_service_start.publish_combat_started_event(service, _combat_instance(), "room_001")


@pytest.mark.asyncio
async def test_check_target_rest_skips_non_player() -> None:
    """NPC targets skip rest/grace checks."""
    service = MagicMock()
    target = _participant("NPC", CombatParticipantType.NPC)
    await combat_service_start.check_target_rest_and_grace_period(service, target, _participant())


@pytest.mark.asyncio
async def test_apply_target_rest_grace_raises_on_grace_period() -> None:
    """Target in login grace period blocks combat."""
    target = _participant("Target")
    attacker = _participant("Attacker")
    connection_manager = MagicMock()
    with (
        patch("server.services.combat_service_start.is_player_in_login_grace_period", return_value=True),
        patch("server.services.combat_service_start.is_player_resting", return_value=False),
    ):
        with pytest.raises(ValueError, match="login grace period"):
            await combat_service_start.apply_target_rest_and_grace_checks(
                MagicMock(), connection_manager, target, attacker
            )


@pytest.mark.asyncio
async def test_apply_target_rest_cancels_rest() -> None:
    """Resting target has rest countdown cancelled."""
    target = _participant("Target")
    connection_manager = MagicMock()
    with (
        patch("server.services.combat_service_start.is_player_in_login_grace_period", return_value=False),
        patch("server.services.combat_service_start.is_player_resting", return_value=True),
        patch("server.services.combat_service_start.cancel_rest_countdown", AsyncMock()) as mock_cancel,
    ):
        await combat_service_start.apply_target_rest_and_grace_checks(
            MagicMock(), connection_manager, target, _participant("Attacker")
        )
    mock_cancel.assert_awaited_once()


@pytest.mark.asyncio
async def test_check_attacker_grace_period_raises() -> None:
    """Attacker in grace period cannot initiate combat."""
    attacker = _participant("Attacker")
    mock_app = MagicMock()
    mock_app.state.connection_manager = MagicMock()
    with (
        patch("server.services.combat_service_start.get_config") as mock_config,
        patch("server.services.combat_service_start.is_player_in_login_grace_period", return_value=True),
    ):
        mock_config.return_value._app_instance = mock_app
        with pytest.raises(ValueError, match="cannot initiate combat"):
            await combat_service_start.check_attacker_grace_period(MagicMock(), attacker, _participant("Target"))


@pytest.mark.asyncio
async def test_end_combat_missing_combat_returns_early() -> None:
    """Ending unknown combat is a no-op."""
    service = MagicMock()
    service.get_combat = MagicMock(return_value=None)
    await combat_service_end.end_combat(service, uuid.uuid4())
    service.cleanup_combat_tracking.assert_not_called()


@pytest.mark.asyncio
async def test_end_combat_full_flow() -> None:
    """End combat clears aggro, updates status, and publishes event."""
    service = MagicMock()
    combat = _combat_instance()
    service.get_combat = MagicMock(return_value=combat)
    service.cleanup_combat_tracking = MagicMock()
    service.notify_player_combat_ended = AsyncMock()
    service.check_connection_state = MagicMock()
    service.publish_combat_ended_event = AsyncMock()

    with patch("server.services.combat_service_end.clear_aggro_for_combat") as mock_clear:
        await combat_service_end.end_combat(service, combat.combat_id, reason="Victory")

    mock_clear.assert_called_once_with(combat)
    assert combat.status == CombatStatus.ENDED
    service.cleanup_combat_tracking.assert_called_once_with(combat)
    service.notify_player_combat_ended.assert_awaited_once_with(combat.combat_id)
    service.publish_combat_ended_event.assert_awaited_once()


@pytest.mark.asyncio
async def test_publish_npc_damage_event_success() -> None:
    """NPC damage event delegates to service NATS publisher."""
    service = MagicMock()
    service.publish_npc_took_damage_event_to_nats = AsyncMock(return_value=True)
    npc_id = uuid.uuid4()
    result = await combat_service_events.publish_npc_damage_event(
        service, "room_001", npc_id, "Deep One", 5, 15, 20, combat_id=uuid.uuid4()
    )
    assert result is True
    service.publish_npc_took_damage_event_to_nats.assert_awaited_once()


@pytest.mark.asyncio
async def test_publish_npc_damage_event_handles_errors() -> None:
    """NPC damage publish errors return False."""
    service = MagicMock()
    service.publish_npc_took_damage_event_to_nats = AsyncMock(side_effect=RuntimeError("fail"))
    result = await combat_service_events.publish_npc_damage_event(
        service, "room_001", uuid.uuid4(), "Deep One", 5, 15, 20
    )
    assert result is False


@pytest.mark.asyncio
async def test_publish_npc_died_event_success() -> None:
    """NPC died event delegates to service NATS publisher."""
    service = MagicMock()
    service.publish_npc_died_event_to_nats = AsyncMock(return_value=True)
    result = await combat_service_events.publish_npc_died_event(
        service, "room_001", uuid.uuid4(), "Deep One", xp_reward=10, killer_id="player-1"
    )
    assert result is True


@pytest.mark.asyncio
async def test_broadcast_aggro_target_switches_noop_cases() -> None:
    """Empty switches or missing NPC service skips broadcast."""
    service = MagicMock()
    service.get_npc_combat_integration_service.return_value = None
    await combat_service_events.broadcast_aggro_target_switches(service, "room_001", uuid.uuid4(), [])
    service.get_npc_combat_integration_service.assert_not_called()


@pytest.mark.asyncio
async def test_broadcast_aggro_target_switches_sends_messages() -> None:
    """Each switch triggers a combat target switch broadcast."""
    service = MagicMock()
    npc_id = uuid.uuid4()
    mi = MagicMock()
    mi.broadcast_combat_target_switch = AsyncMock()
    npc_svc = MagicMock()
    npc_svc.get_messaging_integration.return_value = mi
    service.get_npc_combat_integration_service.return_value = npc_svc

    switches = [(npc_id, "Horror", "Investigator")]
    await combat_service_events.broadcast_aggro_target_switches(service, "room_001", uuid.uuid4(), switches)
    mi.broadcast_combat_target_switch.assert_awaited_once()


# --- CombatDPSync ---


def _dp_sync(**combat_attrs: object) -> CombatDPSync:
    combat_service = MagicMock(**combat_attrs)
    return CombatDPSync(combat_service)


def test_combat_dp_sync_get_persistence_missing() -> None:
    sync = _dp_sync()
    with patch("server.container.ApplicationContainer.get_instance", side_effect=RuntimeError("no container")):
        assert sync._get_persistence(uuid.uuid4()) is None


@pytest.mark.asyncio
async def test_combat_dp_sync_update_and_save_player_not_found() -> None:
    sync = _dp_sync()
    persistence = AsyncMock()
    persistence.get_player_by_id = AsyncMock(return_value=None)
    result = await sync._update_and_save_player_dp(persistence, uuid.uuid4(), 5)
    assert result is None


@pytest.mark.asyncio
async def test_combat_dp_sync_update_and_save_success() -> None:
    sync = _dp_sync()
    player = MagicMock(name="Investigator")
    player.apply_dp_change.return_value = (10, False, False)
    persistence = AsyncMock()
    persistence.get_player_by_id = AsyncMock(return_value=player)
    persistence.save_player = AsyncMock()
    result = await sync._update_and_save_player_dp(persistence, uuid.uuid4(), 8)
    assert result is not None
    persistence.save_player.assert_awaited_once()


def test_combat_dp_sync_log_death_threshold() -> None:
    sync = _dp_sync()
    player_id = uuid.uuid4()
    sync._log_death_threshold_events(-10, 5, player_id, "Investigator")
    sync._log_death_threshold_events(-1, 5, player_id, "Investigator")


@pytest.mark.asyncio
async def test_combat_dp_sync_persist_player_dp_sync_no_persistence() -> None:
    sync = _dp_sync()
    with patch.object(sync, "_get_persistence", return_value=None):
        await sync._persist_player_dp_sync(uuid.uuid4(), 5)


@pytest.mark.asyncio
async def test_combat_dp_sync_publish_player_dp_update_event() -> None:
    sync = _dp_sync(_nats_service=None)
    with patch("server.services.combat_hp_sync.EventBus") as bus_cls:
        bus_cls.return_value.publish = MagicMock()
        await sync._publish_player_dp_update_event(uuid.uuid4(), 10, 8, 20, room_id="room-a")
        bus_cls.return_value.publish.assert_called_once()


@pytest.mark.asyncio
async def test_combat_dp_sync_publish_correction_event() -> None:
    sync = _dp_sync()
    with patch("server.services.combat_hp_sync.EventBus") as bus_cls:
        bus_cls.return_value.publish = MagicMock()
        await sync._publish_player_dp_correction_event(uuid.uuid4(), 10, 20, error_message="db fail")
        bus_cls.return_value.publish.assert_called_once()


@pytest.mark.asyncio
async def test_combat_dp_sync_verify_player_save_mismatch() -> None:
    sync = _dp_sync()
    persistence = AsyncMock()
    player = MagicMock()
    player.get_stats.return_value = {"current_dp": 99}
    persistence.get_player_by_id = AsyncMock(return_value=player)
    await sync._verify_player_save(persistence, uuid.uuid4(), "Investigator", 10, 8)


@pytest.mark.asyncio
async def test_combat_dp_sync_persist_player_dp_sync_success() -> None:
    sync = _dp_sync()
    player = MagicMock(name="Investigator")
    player.apply_dp_change.return_value = (10, True, False)
    persistence = AsyncMock()
    persistence.get_player_by_id = AsyncMock(return_value=player)
    persistence.save_player = AsyncMock()
    with patch.object(sync, "_get_persistence", return_value=persistence):
        await sync._persist_player_dp_sync(uuid.uuid4(), 5)
    persistence.save_player.assert_awaited_once()


@pytest.mark.asyncio
async def test_combat_dp_sync_persist_player_dp_sync_database_error() -> None:
    sync = _dp_sync()
    persistence = AsyncMock()
    persistence.get_player_by_id = AsyncMock(side_effect=DatabaseError("db down"))
    with patch.object(sync, "_get_persistence", return_value=persistence):
        await sync._persist_player_dp_sync(uuid.uuid4(), 5)


@pytest.mark.asyncio
async def test_combat_dp_sync_publish_with_nats_legacy_subject() -> None:
    nats_service = AsyncMock()
    sync = _dp_sync(_nats_service=nats_service, _combat_event_publisher=None)
    with patch("server.services.combat_hp_sync.EventBus") as bus_cls:
        bus_cls.return_value.publish = MagicMock()
        await sync._publish_player_dp_update_event(uuid.uuid4(), 10, 8, 20)
    nats_service.publish.assert_awaited_once()


@pytest.mark.asyncio
async def test_combat_dp_sync_publish_with_nats_subject_manager() -> None:
    nats_service = AsyncMock()
    subject_manager = MagicMock()
    subject_manager.build_subject.return_value = "combat.dp_update.player-1"
    publisher = MagicMock(subject_manager=subject_manager)
    sync = _dp_sync(_nats_service=nats_service, _combat_event_publisher=publisher)
    with patch("server.services.combat_hp_sync.EventBus") as bus_cls:
        bus_cls.return_value.publish = MagicMock()
        await sync._publish_player_dp_update_event(uuid.uuid4(), 10, 8, 20)
    nats_service.publish.assert_awaited_once()


@pytest.mark.asyncio
async def test_combat_dp_sync_persist_background_runs_task() -> None:
    sync = _dp_sync()
    player_id = uuid.uuid4()
    with patch.object(sync, "_persist_player_dp_sync", AsyncMock()) as persist:
        with patch("asyncio.create_task", new=lambda coro: asyncio.ensure_future(coro)):
            sync._persist_player_dp_background(player_id, 8, 10, 20, room_id="room-a")
            await asyncio.sleep(0)
    persist.assert_awaited_once_with(player_id, 8)


def test_combat_dp_sync_persist_background_no_event_loop() -> None:
    sync = _dp_sync()
    with patch("asyncio.create_task", side_effect=RuntimeError("no loop")):
        sync._persist_player_dp_background(uuid.uuid4(), 8, 10, 20)


@pytest.mark.asyncio
async def test_combat_dp_sync_persist_background_persistence_failure_sends_correction() -> None:
    sync = _dp_sync()

    async def fail_persist(_player_id: uuid.UUID, _dp: int) -> None:
        raise DatabaseError("write failed")

    with patch.object(sync, "_persist_player_dp_sync", fail_persist):
        with patch.object(sync, "_publish_player_dp_correction_event", AsyncMock()) as correction:
            with patch("asyncio.create_task", new=lambda coro: asyncio.ensure_future(coro)):
                sync._persist_player_dp_background(uuid.uuid4(), 8, 10, 20, room_id="room-a")
                await asyncio.sleep(0)
            correction.assert_awaited_once()


# --- combat_service_attack ---


def _attack_participant(
    name: str = "Fighter",
    ptype: CombatParticipantType = CombatParticipantType.PLAYER,
) -> CombatParticipant:
    return CombatParticipant(
        participant_id=uuid.uuid4(),
        participant_type=ptype,
        name=name,
        current_dp=10,
        max_dp=20,
        dexterity=10,
    )


@pytest.mark.asyncio
async def test_handle_combat_completion_ends_combat() -> None:
    service = MagicMock()
    service.end_combat = AsyncMock()
    combat = _combat_instance()
    await combat_service_attack.handle_combat_completion(service, combat, True)
    service.end_combat.assert_awaited_once()


@pytest.mark.asyncio
async def test_handle_combat_completion_end_error_swallowed() -> None:
    service = MagicMock()
    service.end_combat = AsyncMock(side_effect=NATSError("down"))
    await combat_service_attack.handle_combat_completion(service, _combat_instance(), True)


@pytest.mark.asyncio
async def test_handle_combat_completion_schedules_next_turn() -> None:
    service = MagicMock()
    combat = _combat_instance()
    combat.turn_interval_ticks = 3
    with patch("server.app.game_tick_processing.get_current_tick", return_value=10):
        await combat_service_attack.handle_combat_completion(service, combat, False)
    assert combat.next_turn_tick == 13


@pytest.mark.asyncio
async def test_queue_combat_action_success_and_failures() -> None:
    combat = _combat_instance()
    pid = next(iter(combat.participants))
    service = MagicMock()
    service.get_combat = MagicMock(return_value=combat)
    assert await combat_service_attack.queue_combat_action(service, combat.combat_id, pid, "attack") is True

    service.get_combat = MagicMock(return_value=None)
    assert await combat_service_attack.queue_combat_action(service, combat.combat_id, pid, "attack") is False

    service.get_combat = MagicMock(return_value=combat)
    assert await combat_service_attack.queue_combat_action(service, combat.combat_id, uuid.uuid4(), "attack") is False


def test_effective_room_for_melee_helpers() -> None:
    pid = uuid.uuid4()
    parts = {pid: _attack_participant()}
    assert combat_service_attack._effective_room_for_melee("r1", pid, "combat_r", parts) == "r1"
    assert combat_service_attack._effective_room_for_melee(None, pid, "combat_r", parts) == "combat_r"
    assert combat_service_attack._effective_room_for_melee(None, uuid.uuid4(), "combat_r", parts) is None
    reason = combat_service_attack._melee_location_fail_reason(
        _attack_participant("A"), _attack_participant("B"), "r1", "r2", "r0"
    )
    assert "Combat ended" in reason


@pytest.mark.asyncio
async def test_validate_melee_location_paths() -> None:
    attacker = _attack_participant("A")
    target = _attack_participant("B")
    combat = CombatInstance(
        combat_id=uuid.uuid4(),
        room_id="room_a",
        participants={attacker.participant_id: attacker, target.participant_id: target},
    )
    service = MagicMock()
    service.get_participant_current_room = AsyncMock(side_effect=["room_a", "room_a"])
    ok, reason = await combat_service_attack.validate_melee_location(service, combat, attacker, target)
    assert ok is True
    assert reason is None

    service.get_participant_current_room = AsyncMock(side_effect=[None, None])
    ok, reason = await combat_service_attack.validate_melee_location(service, combat, attacker, target)
    assert ok is True

    service.get_participant_current_room = AsyncMock(side_effect=["elsewhere", "room_a"])
    ok, reason = await combat_service_attack.validate_melee_location(service, combat, attacker, target)
    assert ok is False
    assert reason is not None


@pytest.mark.asyncio
async def test_validate_melee_or_end_combat_ends() -> None:
    service = MagicMock()
    service.validate_melee_location = AsyncMock(return_value=(False, "bad rooms"))
    service.end_combat = AsyncMock()
    attacker = _attack_participant()
    target = _attack_participant("T")
    combat = _combat_instance()
    early = await combat_service_attack.validate_melee_or_end_combat(
        service, combat, attacker, target, attacker.participant_id, target.participant_id
    )
    assert early is not None
    assert early.combat_ended is True


@pytest.mark.asyncio
async def test_apply_damage_and_check_involuntary_flee() -> None:
    service = MagicMock()
    service.apply_attack_damage = AsyncMock(return_value=(8, False, False))
    service.check_involuntary_flee = AsyncMock(return_value=False)
    attacker = _attack_participant()
    npc = _attack_participant("Mob", CombatParticipantType.NPC)
    combat = _combat_instance()
    died, mw, early = await combat_service_attack.apply_damage_and_check_involuntary_flee(
        service, combat, attacker, npc, 5
    )
    assert died is False and mw is False and early is None

    player = _attack_participant("Player")
    service.check_involuntary_flee = AsyncMock(return_value=True)
    service.end_combat = AsyncMock()
    died, mw, early = await combat_service_attack.apply_damage_and_check_involuntary_flee(
        service, combat, attacker, player, 5
    )
    assert early is not None
    assert early.combat_ended is True


@pytest.mark.asyncio
async def test_finalize_attack_result_and_process_attack() -> None:
    service = MagicMock()
    attacker = _attack_participant()
    target = _attack_participant("Mob", CombatParticipantType.NPC)
    combat = CombatInstance(
        combat_id=uuid.uuid4(),
        room_id="room_a",
        participants={attacker.participant_id: attacker, target.participant_id: target},
    )
    combat.is_combat_over = MagicMock(return_value=False)
    service.handle_target_state_changes = AsyncMock()
    service.handle_attack_events_and_xp = AsyncMock(return_value=0)
    service.award_xp_to_player = AsyncMock()
    service.handle_combat_completion = AsyncMock()
    with patch("server.services.combat_service_attack.add_damage_threat") as threat:
        result = await combat_service_attack.finalize_attack_result(
            service, combat, attacker, target, 4, False, False, target.participant_id
        )
    threat.assert_called_once()
    assert result.success is True
    assert result.damage == 4

    service.validate_and_get_combat_participants = AsyncMock(return_value=(combat, attacker, target))
    service.validate_melee_or_end_combat = AsyncMock(return_value=None)
    service.apply_damage_and_check_involuntary_flee = AsyncMock(return_value=(False, False, None))
    service.finalize_attack_result = AsyncMock(return_value=result)
    out = await combat_service_attack.process_attack(service, attacker.participant_id, target.participant_id, 4)
    assert out is result

    early = MagicMock()
    service.validate_melee_or_end_combat = AsyncMock(return_value=early)
    assert (
        await combat_service_attack.process_attack(service, attacker.participant_id, target.participant_id, 4) is early
    )
