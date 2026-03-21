"""
Combat start validation, registration, and event publishing for CombatService.

Extracted from combat_service.py to keep module line count under limit.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from server.commands.rest_command import cancel_rest_countdown, is_player_resting
from server.config import get_config
from server.events.combat_events import CombatStartedEvent
from server.models.combat import CombatInstance
from server.realtime.login_grace_period import is_player_in_login_grace_period
from server.services.combat_types import CombatParticipantData
from server.services.nats_exceptions import NATSError
from server.structured_logging.enhanced_logging_config import get_logger

logger = get_logger(__name__)


def get_connection_manager_for_combat_check(_service: CombatService) -> Any | None:
    """Resolve connection_manager from config app instance for rest/grace checks."""
    config = get_config()
    app = getattr(config, "_app_instance", None)
    if not app:
        return None
    return getattr(app.state, "connection_manager", None)


async def apply_target_rest_and_grace_checks(
    _service: CombatService,
    connection_manager: Any,
    target: CombatParticipantData,
    attacker: CombatParticipantData,
) -> None:
    """Check target login grace period (raises) and resting (cancel + log)."""
    target_id = target.participant_id
    if is_player_in_login_grace_period(target_id, connection_manager):
        logger.info(
            "Combat prevented - target in login grace period",
            target_id=target_id,
            target_name=target.name,
            attacker_name=attacker.name,
        )
        raise ValueError("Target is protected by login grace period and cannot be attacked")
    if is_player_resting(target_id, connection_manager):
        await cancel_rest_countdown(target_id, connection_manager)
        logger.info(
            "Rest interrupted by combat start (player attacked)",
            target_id=target_id,
            target_name=target.name,
        )


async def check_target_rest_and_grace_period(
    service: CombatService, target: CombatParticipantData, attacker: CombatParticipantData
) -> None:
    """Check if target is resting or in grace period and handle accordingly."""
    from server.models.combat import CombatParticipantType  # noqa: PLC0415  # Avoid circular import

    if target.participant_type != CombatParticipantType.PLAYER:
        return
    try:
        connection_manager = get_connection_manager_for_combat_check(service)
        if not connection_manager:
            return
        await apply_target_rest_and_grace_checks(service, connection_manager, target, attacker)
    except (AttributeError, ImportError, TypeError) as e:
        logger.debug("Could not check rest state for combat start", target_id=target.participant_id, error=str(e))
    except ValueError as e:
        if "login grace period" in str(e):
            raise
        logger.debug("Could not check rest state for combat start", target_id=target.participant_id, error=str(e))


async def check_attacker_grace_period(
    _service: CombatService, attacker: CombatParticipantData, target: CombatParticipantData
) -> None:
    """Check if attacker is in login grace period."""
    from server.models.combat import CombatParticipantType  # noqa: PLC0415  # Avoid circular import

    if attacker.participant_type != CombatParticipantType.PLAYER:
        return
    try:
        config = get_config()
        app = getattr(config, "_app_instance", None)
        if not app:
            return
        connection_manager = getattr(app.state, "connection_manager", None)
        if not connection_manager:
            return
        attacker_id = attacker.participant_id
        if is_player_in_login_grace_period(attacker_id, connection_manager):
            logger.info(
                "Combat prevented - attacker in login grace period",
                attacker_id=attacker_id,
                attacker_name=attacker.name,
                target_name=target.name,
            )
            raise ValueError("You are protected by login grace period and cannot initiate combat")
    except (AttributeError, ImportError, TypeError) as e:
        logger.debug(
            "Could not check login grace period for attacker",
            attacker_id=attacker.participant_id,
            error=str(e),
        )
    except ValueError as e:
        if "login grace period" in str(e):
            raise
        logger.debug(
            "Could not check login grace period for attacker",
            attacker_id=attacker.participant_id,
            error=str(e),
        )


async def validate_combat_can_start(
    service: CombatService, attacker: CombatParticipantData, target: CombatParticipantData
) -> None:
    """Validate that combat can start (participants not already in combat)."""
    attacker_combat = await service.get_combat_by_participant(attacker.participant_id)
    target_combat = await service.get_combat_by_participant(target.participant_id)
    if attacker_combat or target_combat:
        raise ValueError("One or both participants are already in combat")


async def register_combat(
    service: CombatService,
    combat: CombatInstance,
    attacker: CombatParticipantData,
    room_id: str,
) -> None:
    """Register combat instance and track player combat state."""
    await service.register_combat_state(combat, attacker.participant_id, attacker.name, room_id)


async def publish_combat_started_event(service: CombatService, combat: CombatInstance, room_id: str) -> None:
    """Publish combat started event."""
    try:
        logger.debug("Creating CombatStartedEvent", combat_id=combat.combat_id)
        started_event = CombatStartedEvent(
            combat_id=combat.combat_id,
            room_id=room_id,
            participants={
                str(p.participant_id): {"name": p.name, "dp": p.current_dp, "max_dp": p.max_dp}
                for p in combat.participants.values()
            },
            turn_order=[str(pid) for pid in combat.turn_order],
        )
        logger.debug("Calling publish_combat_started", combat_id=combat.combat_id)
        await service.publish_combat_started_event(started_event)
        logger.debug("publish_combat_started completed", combat_id=combat.combat_id)
    except (NATSError, ValueError, RuntimeError, AttributeError, ConnectionError) as e:
        logger.error("Error publishing combat started event", error=str(e), exc_info=True)


if TYPE_CHECKING:
    from server.services.combat_service import CombatService
