"""
Combat event publisher for MythosMUD.

This module provides a service for publishing combat events to NATS
for real-time distribution to clients and other systems.
"""

# pylint: disable=too-many-arguments,too-many-positional-arguments,too-many-return-statements,too-many-lines  # Reason: Event publishing requires many parameters for complete event context and multiple return statements for early validation returns. Combat event publisher requires extensive event publishing logic for comprehensive combat event distribution.

import uuid
from dataclasses import dataclass
from datetime import UTC, datetime
from typing import TYPE_CHECKING, Any

from ..events.combat_events import (
    CombatEndedEvent,
    CombatStartedEvent,
    CombatTimeoutEvent,
    CombatTurnAdvancedEvent,
    NPCAttackedEvent,
    NPCDiedEvent,
    NPCTookDamageEvent,
    PlayerAttackedEvent,
)
from ..structured_logging.enhanced_logging_config import get_logger
from .nats_exceptions import NATSPublishError
from .nats_subject_manager import NATSSubjectManager

if TYPE_CHECKING:
    from .nats_service import NATSService

logger = get_logger("services.combat_event_publisher")


@dataclass
class _CombatPublishJob:
    """Bundled NATS publish inputs (keeps helper parameter count under gate)."""

    event_type: str
    subject_key: str
    room_id: str
    event_data: dict[str, Any]
    timestamp: datetime
    log_context: dict[str, Any]
    success_fields: dict[str, Any]
    error_label: str


class CombatEventPublisher:
    """
    Service for publishing combat events to NATS for real-time distribution.

    This service integrates combat events with the existing NATS messaging
    system to provide real-time combat updates to clients and other systems.
    """

    def __init__(
        self, nats_service: "NATSService | None" = None, subject_manager: NATSSubjectManager | None = None
    ) -> None:
        """
        Initialize combat event publisher.

        Args:
            nats_service: NATS service instance (optional, defaults to global)
            subject_manager: Subject manager for standardized NATS subjects (optional for backward compatibility)

        AI: subject_manager is optional for backward compatibility but recommended for standardized patterns.
        AI: Falls back to legacy subject construction if subject_manager is None.
        """
        logger.debug("CombatEventPublisher __init__ method entered")
        # Import here to avoid circular dependencies
        from ..services.nats_service import nats_service as global_nats_service

        self.nats_service = nats_service or global_nats_service
        self.subject_manager = subject_manager
        logger.info(
            "CombatEventPublisher initialized",
            nats_service_available=bool(self.nats_service),
            nats_service_type=(type(self.nats_service).__name__ if self.nats_service else "None"),
            subject_manager_enabled=subject_manager is not None,
        )

    def _create_event_message(  # pylint: disable=too-many-arguments,too-many-positional-arguments  # Reason: Event message creation requires many parameters for complete event context
        self,
        event_type: str,
        event_data: dict[str, Any],
        room_id: str | None = None,
        player_id: str | None = None,
        timestamp: str | None = None,
    ) -> dict[str, Any]:
        """
        Create a standardized event message structure matching EventMessageSchema.

        Args:
            event_type: Type of event (combat_started, player_attacked, etc.)
            event_data: Event-specific data dictionary
            room_id: Optional room ID for room-scoped events
            player_id: Optional player ID for player-scoped events
            timestamp: Optional custom timestamp (ISO format)

        Returns:
            Event message dictionary matching EventMessageSchema
        """
        # Generate message_id
        message_id = str(uuid.uuid4())

        # Generate timestamp if not provided
        if timestamp is None:
            timestamp = datetime.now(UTC).isoformat().replace("+00:00", "Z")

        # Create base message structure matching EventMessageSchema
        message = {
            "message_id": message_id,
            "timestamp": timestamp,
            "event_type": event_type,
            "event_data": event_data,
        }

        # Add optional fields
        if room_id is not None:
            message["room_id"] = room_id
        if player_id is not None:
            message["player_id"] = player_id

        return message

    _LEGACY_SUBJECT_PREFIX = {
        "combat_started": "combat.started",
        "combat_ended": "combat.ended",
        "combat_attack": "combat.attack",
        "combat_npc_attacked": "combat.npc_attacked",
        "combat_damage": "combat.damage",
        "combat_npc_died": "combat.npc_died",
        "combat_turn": "combat.turn",
        "combat_timeout": "combat.timeout",
    }

    def _build_combat_subject(self, subject_key: str, room_id: str) -> str:
        if self.subject_manager:
            return self.subject_manager.build_subject(subject_key, room_id=room_id)
        prefix = self._LEGACY_SUBJECT_PREFIX.get(subject_key, subject_key)
        logger.warning(
            "Using legacy subject construction - subject_manager not configured",
            event_type=subject_key,
            room_id=room_id,
        )
        return f"{prefix}.{room_id}"

    def _nats_ready(self, log_context: dict[str, Any]) -> bool:
        if not self.nats_service:
            logger.error(
                "NATS service not available for combat event publishing - event will not be broadcasted",
                nats_service_available=False,
                **log_context,
            )
            return False
        if not self.nats_service.is_connected():
            logger.error(
                "NATS service not connected for combat event publishing - event will not be broadcasted",
                nats_connected=False,
                **log_context,
            )
            return False
        return True

    async def _publish_combat_payload(self, job: _CombatPublishJob) -> bool:
        """Shared NATS publish path for combat events."""
        try:
            if not self._nats_ready(job.log_context):
                return False
            message_data = self._create_event_message(
                event_type=job.event_type,
                event_data=job.event_data,
                room_id=job.room_id,
                timestamp=job.timestamp.isoformat().replace("+00:00", "Z"),
            )
            subject = self._build_combat_subject(job.subject_key, job.room_id)
            try:
                await self.nats_service.publish(subject, message_data)
                logger.info(f"{job.error_label} published to NATS", subject=subject, **job.success_fields)
                return True
            except NATSPublishError as exc:
                logger.error(f"Failed to publish {job.error_label} to NATS", error=str(exc), **job.success_fields)
                return False
            except (RuntimeError, ConnectionError, TimeoutError, OSError) as exc:
                logger.error(
                    f"Unexpected error publishing {job.error_label} to NATS", error=str(exc), **job.success_fields
                )
                return False
            except Exception as exc:  # pylint: disable=broad-exception-caught  # noqa: B904
                # Catch generic exceptions from mocks in tests
                logger.error(
                    f"Unexpected error publishing {job.error_label} to NATS", error=str(exc), **job.success_fields
                )
                return False
        except (AttributeError, TypeError, ValueError, KeyError) as exc:
            logger.error(f"Error publishing {job.error_label}", error=str(exc), exc_info=True, **job.log_context)
            return False

    async def publish_combat_started(self, event: CombatStartedEvent) -> bool:
        """Publish combat started event to NATS."""
        combat_id = str(event.combat_id)
        room_id = event.room_id
        log_context = {
            "combat_id": combat_id,
            "room_id": room_id,
            "event_type": "combat_started",
            "participant_count": len(event.participants),
            "turn_order_count": len(event.turn_order),
        }
        logger.info("Starting combat event publishing", **log_context)
        if event.timestamp is None:
            raise ValueError("Event timestamp should be set by BaseEvent.__post_init__")
        event_data = {
            "combat_id": combat_id,
            "room_id": room_id,
            "participants": event.participants,
            "turn_order": event.turn_order,
            "timestamp": event.timestamp.isoformat(),
        }
        return await self._publish_combat_payload(
            _CombatPublishJob(
                "combat_started",
                "combat_started",
                room_id,
                event_data,
                event.timestamp,
                log_context,
                {"combat_id": combat_id, "room_id": room_id, "participant_count": len(event.participants)},
                "Combat started event",
            )
        )

    async def publish_combat_ended(self, event: CombatEndedEvent) -> bool:
        """Publish combat ended event to NATS."""
        combat_id = str(event.combat_id)
        log_context = {
            "combat_id": combat_id,
            "room_id": event.room_id,
            "event_type": "combat_ended",
            "reason": event.reason,
            "duration_seconds": event.duration_seconds,
            "participants": event.participants,
        }
        event_data = {
            "combat_id": combat_id,
            "room_id": event.room_id,
            "reason": event.reason,
            "duration_seconds": event.duration_seconds,
            "participants": event.participants,
            "timestamp": event.timestamp.isoformat(),
        }
        return await self._publish_combat_payload(
            _CombatPublishJob(
                "combat_ended",
                "combat_ended",
                event.room_id,
                event_data,
                event.timestamp,
                log_context,
                {"combat_id": combat_id, "room_id": event.room_id},
                "Combat ended event",
            )
        )

    async def publish_player_attacked(self, event: PlayerAttackedEvent) -> bool:
        """Publish player attacked event to NATS."""
        combat_id = str(event.combat_id)
        log_context = {
            "combat_id": combat_id,
            "room_id": event.room_id,
            "event_type": "player_attacked",
            "attacker_id": str(event.attacker_id),
            "attacker_name": event.attacker_name,
            "target_id": str(event.target_id),
            "target_name": event.target_name,
            "damage": event.damage,
            "action_type": event.action_type,
        }
        event_data = {
            "combat_id": combat_id,
            "room_id": event.room_id,
            "attacker_id": str(event.attacker_id),
            "attacker_name": event.attacker_name,
            "target_id": str(event.target_id),
            "target_name": event.target_name,
            "damage": event.damage,
            "action_type": event.action_type,
            "target_current_dp": event.target_current_dp,
            "target_max_dp": event.target_max_dp,
            "timestamp": event.timestamp.isoformat(),
        }
        return await self._publish_combat_payload(
            _CombatPublishJob(
                "player_attacked",
                "combat_attack",
                event.room_id,
                event_data,
                event.timestamp,
                log_context,
                {
                    "combat_id": combat_id,
                    "attacker_name": event.attacker_name,
                    "target_name": event.target_name,
                    "damage": event.damage,
                },
                "Player attacked event",
            )
        )

    async def publish_npc_attacked(self, event: NPCAttackedEvent) -> bool:
        """Publish NPC attacked event to NATS."""
        combat_id = str(event.combat_id)
        log_context = {
            "combat_id": combat_id,
            "room_id": event.room_id,
            "event_type": "npc_attacked",
            "attacker_id": str(event.attacker_id),
            "attacker_name": event.attacker_name,
            "npc_id": str(event.npc_id),
            "npc_name": event.npc_name,
            "damage": event.damage,
            "action_type": event.action_type,
        }
        event_data = {
            "combat_id": combat_id,
            "room_id": event.room_id,
            "attacker_id": str(event.attacker_id),
            "attacker_name": event.attacker_name,
            "npc_id": str(event.npc_id),
            "npc_name": event.npc_name,
            "damage": event.damage,
            "action_type": event.action_type,
            "target_current_dp": event.target_current_dp,
            "target_max_dp": event.target_max_dp,
            "timestamp": event.timestamp.isoformat(),
        }
        return await self._publish_combat_payload(
            _CombatPublishJob(
                "npc_attacked",
                "combat_npc_attacked",
                event.room_id,
                event_data,
                event.timestamp,
                log_context,
                {
                    "combat_id": combat_id,
                    "attacker_name": event.attacker_name,
                    "npc_name": event.npc_name,
                    "damage": event.damage,
                },
                "NPC attacked event",
            )
        )

    async def publish_npc_took_damage(self, event: NPCTookDamageEvent) -> bool:
        """Publish NPC took damage event to NATS."""
        combat_id = str(event.combat_id)
        log_context = {
            "combat_id": combat_id,
            "room_id": event.room_id,
            "event_type": "npc_took_damage",
            "npc_id": str(event.npc_id),
            "npc_name": event.npc_name,
            "damage": event.damage,
            "current_dp": event.current_dp,
            "max_dp": event.max_dp,
        }
        event_data = {
            "combat_id": combat_id,
            "room_id": event.room_id,
            "npc_id": str(event.npc_id),
            "npc_name": event.npc_name,
            "damage": event.damage,
            "current_dp": event.current_dp,
            "max_dp": event.max_dp,
            "timestamp": event.timestamp.isoformat(),
        }
        return await self._publish_combat_payload(
            _CombatPublishJob(
                "npc_took_damage",
                "combat_damage",
                event.room_id,
                event_data,
                event.timestamp,
                log_context,
                {
                    "combat_id": combat_id,
                    "npc_name": event.npc_name,
                    "damage": event.damage,
                    "current_dp": event.current_dp,
                },
                "NPC took damage event",
            )
        )

    async def publish_npc_died(self, event: NPCDiedEvent) -> bool:
        """Publish NPC died event to NATS."""
        combat_id = str(event.combat_id)
        log_context = {
            "combat_id": combat_id,
            "room_id": event.room_id,
            "event_type": "npc_died",
            "npc_id": str(event.npc_id),
            "npc_name": event.npc_name,
            "xp_reward": event.xp_reward,
        }
        event_data = {
            "combat_id": combat_id,
            "room_id": event.room_id,
            "npc_id": str(event.npc_id),
            "npc_name": event.npc_name,
            "xp_reward": event.xp_reward,
            "timestamp": event.timestamp.isoformat(),
        }
        if getattr(event, "killer_id", None):
            event_data["killer_id"] = event.killer_id
        return await self._publish_combat_payload(
            _CombatPublishJob(
                "npc_died",
                "combat_npc_died",
                event.room_id,
                event_data,
                event.timestamp,
                log_context,
                {"combat_id": combat_id, "npc_name": event.npc_name, "xp_reward": event.xp_reward},
                "NPC died event",
            )
        )

    async def publish_combat_turn_advanced(self, event: CombatTurnAdvancedEvent) -> bool:
        """Publish combat turn advanced event to NATS."""
        combat_id = str(event.combat_id)
        log_context = {
            "combat_id": combat_id,
            "room_id": event.room_id,
            "event_type": "combat_turn_advanced",
            "current_turn": event.current_turn,
            "combat_round": event.combat_round,
            "next_participant": event.next_participant,
        }
        event_data = {
            "combat_id": combat_id,
            "room_id": event.room_id,
            "current_turn": event.current_turn,
            "combat_round": event.combat_round,
            "next_participant": event.next_participant,
            "timestamp": event.timestamp.isoformat(),
        }
        return await self._publish_combat_payload(
            _CombatPublishJob(
                "combat_turn_advanced",
                "combat_turn",
                event.room_id,
                event_data,
                event.timestamp,
                log_context,
                {"combat_id": combat_id, "room_id": event.room_id, "current_turn": event.current_turn},
                "Combat turn advanced event",
            )
        )

    async def publish_combat_timeout(self, event: CombatTimeoutEvent) -> bool:
        """Publish combat timeout event to NATS."""
        combat_id = str(event.combat_id)
        last_activity = event.last_activity.isoformat() if event.last_activity else None
        log_context = {
            "combat_id": combat_id,
            "room_id": event.room_id,
            "event_type": "combat_timeout",
            "timeout_minutes": event.timeout_minutes,
            "last_activity": last_activity,
        }
        event_data = {
            "combat_id": combat_id,
            "room_id": event.room_id,
            "timeout_minutes": event.timeout_minutes,
            "last_activity": last_activity,
            "timestamp": event.timestamp.isoformat(),
        }
        return await self._publish_combat_payload(
            _CombatPublishJob(
                "combat_timeout",
                "combat_timeout",
                event.room_id,
                event_data,
                event.timestamp,
                log_context,
                {"combat_id": combat_id, "room_id": event.room_id, "timeout_minutes": event.timeout_minutes},
                "Combat timeout event",
            )
        )


# Global instance
combat_event_publisher = CombatEventPublisher()
