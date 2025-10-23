"""
Combat event publisher for MythosMUD.

This module provides a service for publishing combat events to NATS
for real-time distribution to clients and other systems.
"""

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
from ..logging.enhanced_logging_config import get_logger

logger = get_logger("services.combat_event_publisher")


class CombatEventPublisher:
    """
    Service for publishing combat events to NATS for real-time distribution.

    This service integrates combat events with the existing NATS messaging
    system to provide real-time combat updates to clients and other systems.
    """

    def __init__(self, nats_service=None):
        """
        Initialize combat event publisher.

        Args:
            nats_service: NATS service instance (optional, defaults to global)
        """
        logger.debug("CombatEventPublisher __init__ method entered")
        # Import here to avoid circular dependencies
        from ..services.nats_service import nats_service as global_nats_service

        self.nats_service = nats_service or global_nats_service
        logger.info(
            "CombatEventPublisher initialized",
            nats_service_available=bool(self.nats_service),
            nats_service_type=(type(self.nats_service).__name__ if self.nats_service else "None"),
        )

    async def publish_combat_started(self, event: CombatStartedEvent) -> bool:
        """
        Publish combat started event to NATS.

        Args:
            event: CombatStartedEvent to publish

        Returns:
            True if published successfully, False otherwise
        """
        # Extract structured data for consistent logging
        combat_id = str(event.combat_id)
        room_id = event.room_id
        participant_count = len(event.participants)
        turn_order_count = len(event.turn_order)
        try:
            logger.info(
                "Starting combat event publishing",
                combat_id=combat_id,
                room_id=room_id,
                participant_count=participant_count,
                turn_order_count=turn_order_count,
                event_type="combat_started",
            )

            if not self.nats_service:
                logger.error(
                    "NATS service not available for combat event publishing - event will not be broadcasted",
                    combat_id=combat_id,
                    room_id=room_id,
                    event_type="combat_started",
                    participant_count=participant_count,
                    nats_service_available=False,
                )
                return False

            if not self.nats_service.is_connected():
                logger.error(
                    "NATS service not connected for combat event publishing - event will not be broadcasted",
                    combat_id=combat_id,
                    room_id=room_id,
                    event_type="combat_started",
                    participant_count=participant_count,
                    nats_connected=False,
                )
                return False

            # Create message data for NATS
            message_data = {
                "event_type": "combat_started",
                "data": {
                    "combat_id": combat_id,
                    "room_id": room_id,
                    "participants": event.participants,
                    "turn_order": event.turn_order,
                    "timestamp": event.timestamp.isoformat(),
                },
            }

            # Publish to NATS using room-specific subject
            subject = f"combat.started.{room_id}"
            logger.debug(
                "Publishing combat started event to NATS",
                combat_id=combat_id,
                room_id=room_id,
                subject=subject,
                participant_count=participant_count,
            )
            success = await self.nats_service.publish(subject, message_data)

            if success:
                logger.info(
                    "Combat started event published to NATS",
                    combat_id=combat_id,
                    room_id=room_id,
                    subject=subject,
                    participant_count=participant_count,
                )
            else:
                logger.error(
                    "Failed to publish combat started event to NATS",
                    combat_id=combat_id,
                    room_id=room_id,
                    subject=subject,
                    participant_count=participant_count,
                )

            return success

        except Exception as e:
            logger.error(
                "Error publishing combat started event",
                combat_id=combat_id,
                room_id=room_id,
                error=str(e),
                error_type=type(e).__name__,
                exc_info=True,
            )
            return False

    async def publish_combat_ended(self, event: CombatEndedEvent) -> bool:
        """
        Publish combat ended event to NATS.

        Args:
            event: CombatEndedEvent to publish

        Returns:
            True if published successfully, False otherwise
        """
        try:
            if not self.nats_service:
                logger.error(
                    "NATS service not available for combat event publishing - event will not be broadcasted",
                    combat_id=str(event.combat_id),
                    room_id=event.room_id,
                    event_type="combat_ended",
                    reason=event.reason,
                    duration_seconds=event.duration_seconds,
                    participants=event.participants,
                )
                return False

            if not self.nats_service.is_connected():
                logger.error(
                    "NATS service not connected for combat event publishing - event will not be broadcasted",
                    combat_id=str(event.combat_id),
                    room_id=event.room_id,
                    event_type="combat_ended",
                    nats_connected=False,
                    reason=event.reason,
                    duration_seconds=event.duration_seconds,
                    participants=event.participants,
                )
                return False

            # Create message data for NATS
            message_data = {
                "event_type": "combat_ended",
                "data": {
                    "combat_id": str(event.combat_id),
                    "room_id": event.room_id,
                    "reason": event.reason,
                    "duration_seconds": event.duration_seconds,
                    "participants": event.participants,
                    "timestamp": event.timestamp.isoformat(),
                },
            }

            # Publish to NATS using room-specific subject
            subject = f"combat.ended.{event.room_id}"
            success = await self.nats_service.publish(subject, message_data)

            if success:
                logger.info(
                    "Combat ended event published to NATS",
                    combat_id=str(event.combat_id),
                    room_id=event.room_id,
                    subject=subject,
                )
            else:
                logger.error(
                    "Failed to publish combat ended event to NATS",
                    combat_id=str(event.combat_id),
                    room_id=event.room_id,
                )

            return success

        except Exception as e:
            logger.error(
                "Error publishing combat ended event",
                combat_id=str(event.combat_id),
                error=str(e),
                exc_info=True,
            )
            return False

    async def publish_player_attacked(self, event: PlayerAttackedEvent) -> bool:
        """
        Publish player attacked event to NATS.

        Args:
            event: PlayerAttackedEvent to publish

        Returns:
            True if published successfully, False otherwise
        """
        try:
            if not self.nats_service:
                logger.error(
                    "NATS service not available for combat event publishing - event will not be broadcasted",
                    combat_id=str(event.combat_id),
                    room_id=event.room_id,
                    event_type="player_attacked",
                    attacker_id=str(event.attacker_id),
                    attacker_name=event.attacker_name,
                    target_id=str(event.target_id),
                    target_name=event.target_name,
                    damage=event.damage,
                    action_type=event.action_type,
                )
                return False

            if not self.nats_service.is_connected():
                logger.error(
                    "NATS service not connected for combat event publishing - event will not be broadcasted",
                    combat_id=str(event.combat_id),
                    room_id=event.room_id,
                    event_type="player_attacked",
                    nats_connected=False,
                    attacker_id=str(event.attacker_id),
                    attacker_name=event.attacker_name,
                    target_id=str(event.target_id),
                    target_name=event.target_name,
                    damage=event.damage,
                    action_type=event.action_type,
                )
                return False

            # Create message data for NATS
            message_data = {
                "event_type": "player_attacked",
                "data": {
                    "combat_id": str(event.combat_id),
                    "room_id": event.room_id,
                    "attacker_id": str(event.attacker_id),
                    "attacker_name": event.attacker_name,
                    "target_id": str(event.target_id),
                    "target_name": event.target_name,
                    "damage": event.damage,
                    "action_type": event.action_type,
                    "target_current_hp": event.target_current_hp,
                    "target_max_hp": event.target_max_hp,
                    "timestamp": event.timestamp.isoformat(),
                },
            }

            # Publish to NATS using room-specific subject
            subject = f"combat.attack.{event.room_id}"
            success = await self.nats_service.publish(subject, message_data)

            if success:
                logger.info(
                    "Player attacked event published to NATS",
                    combat_id=str(event.combat_id),
                    attacker_name=event.attacker_name,
                    target_name=event.target_name,
                    damage=event.damage,
                )
            else:
                logger.error(
                    "Failed to publish player attacked event to NATS",
                    combat_id=str(event.combat_id),
                    attacker_name=event.attacker_name,
                )

            return success

        except Exception as e:
            logger.error(
                "Error publishing player attacked event",
                combat_id=str(event.combat_id),
                error=str(e),
                exc_info=True,
            )
            return False

    async def publish_npc_attacked(self, event: NPCAttackedEvent) -> bool:
        """
        Publish NPC attacked event to NATS.

        Args:
            event: NPCAttackedEvent to publish

        Returns:
            True if published successfully, False otherwise
        """
        try:
            if not self.nats_service:
                logger.error(
                    "NATS service not available for combat event publishing - event will not be broadcasted",
                    combat_id=str(event.combat_id),
                    room_id=event.room_id,
                    event_type="npc_attacked",
                    attacker_id=str(event.attacker_id),
                    attacker_name=event.attacker_name,
                    npc_id=str(event.npc_id),
                    npc_name=event.npc_name,
                    damage=event.damage,
                    action_type=event.action_type,
                )
                return False

            if not self.nats_service.is_connected():
                logger.error(
                    "NATS service not connected for combat event publishing - event will not be broadcasted",
                    combat_id=str(event.combat_id),
                    room_id=event.room_id,
                    event_type="npc_attacked",
                    nats_connected=False,
                    attacker_id=str(event.attacker_id),
                    attacker_name=event.attacker_name,
                    npc_id=str(event.npc_id),
                    npc_name=event.npc_name,
                    damage=event.damage,
                    action_type=event.action_type,
                )
                return False

            # Create message data for NATS
            message_data = {
                "event_type": "npc_attacked",
                "data": {
                    "combat_id": str(event.combat_id),
                    "attacker_id": str(event.attacker_id),
                    "attacker_name": event.attacker_name,
                    "npc_id": str(event.npc_id),
                    "npc_name": event.npc_name,
                    "damage": event.damage,
                    "action_type": event.action_type,
                    "target_current_hp": event.target_current_hp,
                    "target_max_hp": event.target_max_hp,
                    "timestamp": event.timestamp.isoformat(),
                },
            }

            # Publish to NATS using room-specific subject
            subject = f"combat.npc_attacked.{event.room_id}"
            success = await self.nats_service.publish(subject, message_data)

            if success:
                logger.info(
                    "NPC attacked event published to NATS",
                    combat_id=str(event.combat_id),
                    attacker_name=event.attacker_name,
                    npc_name=event.npc_name,
                    damage=event.damage,
                )
            else:
                logger.error(
                    "Failed to publish NPC attacked event to NATS",
                    combat_id=str(event.combat_id),
                    attacker_name=event.attacker_name,
                )

            return success

        except Exception as e:
            logger.error(
                "Error publishing NPC attacked event",
                combat_id=str(event.combat_id),
                error=str(e),
                exc_info=True,
            )
            return False

    async def publish_npc_took_damage(self, event: NPCTookDamageEvent) -> bool:
        """
        Publish NPC took damage event to NATS.

        Args:
            event: NPCTookDamageEvent to publish

        Returns:
            True if published successfully, False otherwise
        """
        try:
            if not self.nats_service:
                logger.error(
                    "NATS service not available for combat event publishing - event will not be broadcasted",
                    combat_id=str(event.combat_id),
                    room_id=event.room_id,
                    event_type="npc_took_damage",
                    npc_id=str(event.npc_id),
                    npc_name=event.npc_name,
                    damage=event.damage,
                    current_hp=event.current_hp,
                    max_hp=event.max_hp,
                )
                return False

            if not self.nats_service.is_connected():
                logger.error(
                    "NATS service not connected for combat event publishing - event will not be broadcasted",
                    combat_id=str(event.combat_id),
                    room_id=event.room_id,
                    event_type="npc_took_damage",
                    nats_connected=False,
                    npc_id=str(event.npc_id),
                    npc_name=event.npc_name,
                    damage=event.damage,
                    current_hp=event.current_hp,
                    max_hp=event.max_hp,
                )
                return False

            # Create message data for NATS
            message_data = {
                "event_type": "npc_took_damage",
                "data": {
                    "combat_id": str(event.combat_id),
                    "npc_id": str(event.npc_id),
                    "npc_name": event.npc_name,
                    "damage": event.damage,
                    "current_hp": event.current_hp,
                    "max_hp": event.max_hp,
                    "timestamp": event.timestamp.isoformat(),
                },
            }

            # Publish to NATS using room-specific subject
            subject = f"combat.damage.{event.room_id}"
            success = await self.nats_service.publish(subject, message_data)

            if success:
                logger.info(
                    "NPC took damage event published to NATS",
                    combat_id=str(event.combat_id),
                    npc_name=event.npc_name,
                    damage=event.damage,
                    current_hp=event.current_hp,
                )
            else:
                logger.error(
                    "Failed to publish NPC took damage event to NATS",
                    combat_id=str(event.combat_id),
                    npc_name=event.npc_name,
                )

            return success

        except Exception as e:
            logger.error(
                "Error publishing NPC took damage event",
                combat_id=str(event.combat_id),
                error=str(e),
                exc_info=True,
            )
            return False

    async def publish_npc_died(self, event: NPCDiedEvent) -> bool:
        """
        Publish NPC died event to NATS.

        Args:
            event: NPCDiedEvent to publish

        Returns:
            True if published successfully, False otherwise
        """
        try:
            if not self.nats_service:
                logger.error(
                    "NATS service not available for combat event publishing - event will not be broadcasted",
                    combat_id=str(event.combat_id),
                    room_id=event.room_id,
                    event_type="npc_died",
                    npc_id=str(event.npc_id),
                    npc_name=event.npc_name,
                    xp_reward=event.xp_reward,
                )
                return False

            if not self.nats_service.is_connected():
                logger.error(
                    "NATS service not connected for combat event publishing - event will not be broadcasted",
                    combat_id=str(event.combat_id),
                    room_id=event.room_id,
                    event_type="npc_died",
                    nats_connected=False,
                    npc_id=str(event.npc_id),
                    npc_name=event.npc_name,
                    xp_reward=event.xp_reward,
                )
                return False

            # Create message data for NATS
            message_data = {
                "event_type": "npc_died",
                "data": {
                    "combat_id": str(event.combat_id),
                    "npc_id": str(event.npc_id),
                    "npc_name": event.npc_name,
                    "xp_reward": event.xp_reward,
                    "timestamp": event.timestamp.isoformat(),
                },
            }

            # Publish to NATS using room-specific subject
            subject = f"combat.death.{event.room_id}"
            success = await self.nats_service.publish(subject, message_data)

            if success:
                logger.info(
                    "NPC died event published to NATS",
                    combat_id=str(event.combat_id),
                    npc_name=event.npc_name,
                    xp_reward=event.xp_reward,
                )
            else:
                logger.error(
                    "Failed to publish NPC died event to NATS",
                    combat_id=str(event.combat_id),
                    npc_name=event.npc_name,
                )

            return success

        except Exception as e:
            logger.error(
                "Error publishing NPC died event",
                combat_id=str(event.combat_id),
                error=str(e),
                exc_info=True,
            )
            return False

    async def publish_combat_turn_advanced(self, event: CombatTurnAdvancedEvent) -> bool:
        """
        Publish combat turn advanced event to NATS.

        Args:
            event: CombatTurnAdvancedEvent to publish

        Returns:
            True if published successfully, False otherwise
        """
        try:
            if not self.nats_service:
                logger.error(
                    "NATS service not available for combat event publishing - event will not be broadcasted",
                    combat_id=str(event.combat_id),
                    room_id=event.room_id,
                    event_type="combat_turn_advanced",
                    current_turn=event.current_turn,
                    combat_round=event.combat_round,
                    next_participant=event.next_participant,
                )
                return False

            if not self.nats_service.is_connected():
                logger.error(
                    "NATS service not connected for combat event publishing - event will not be broadcasted",
                    combat_id=str(event.combat_id),
                    room_id=event.room_id,
                    event_type="combat_turn_advanced",
                    nats_connected=False,
                    current_turn=event.current_turn,
                    combat_round=event.combat_round,
                    next_participant=event.next_participant,
                )
                return False

            # Create message data for NATS
            message_data = {
                "event_type": "combat_turn_advanced",
                "data": {
                    "combat_id": str(event.combat_id),
                    "room_id": event.room_id,
                    "current_turn": event.current_turn,
                    "combat_round": event.combat_round,
                    "next_participant": event.next_participant,
                    "timestamp": event.timestamp.isoformat(),
                },
            }

            # Publish to NATS using room-specific subject
            subject = f"combat.turn.{event.room_id}"
            success = await self.nats_service.publish(subject, message_data)

            if success:
                logger.info(
                    "Combat turn advanced event published to NATS",
                    combat_id=str(event.combat_id),
                    room_id=event.room_id,
                    current_turn=event.current_turn,
                )
            else:
                logger.error(
                    "Failed to publish combat turn advanced event to NATS",
                    combat_id=str(event.combat_id),
                    room_id=event.room_id,
                )

            return success

        except Exception as e:
            logger.error(
                "Error publishing combat turn advanced event",
                combat_id=str(event.combat_id),
                error=str(e),
                exc_info=True,
            )
            return False

    async def publish_combat_timeout(self, event: CombatTimeoutEvent) -> bool:
        """
        Publish combat timeout event to NATS.

        Args:
            event: CombatTimeoutEvent to publish

        Returns:
            True if published successfully, False otherwise
        """
        try:
            if not self.nats_service:
                logger.error(
                    "NATS service not available for combat event publishing - event will not be broadcasted",
                    combat_id=str(event.combat_id),
                    room_id=event.room_id,
                    event_type="combat_timeout",
                    timeout_minutes=event.timeout_minutes,
                    last_activity=event.last_activity.isoformat() if event.last_activity else None,
                )
                return False

            if not self.nats_service.is_connected():
                logger.error(
                    "NATS service not connected for combat event publishing - event will not be broadcasted",
                    combat_id=str(event.combat_id),
                    room_id=event.room_id,
                    event_type="combat_timeout",
                    nats_connected=False,
                    timeout_minutes=event.timeout_minutes,
                    last_activity=event.last_activity.isoformat() if event.last_activity else None,
                )
                return False

            # Create message data for NATS
            message_data = {
                "event_type": "combat_timeout",
                "data": {
                    "combat_id": str(event.combat_id),
                    "room_id": event.room_id,
                    "timeout_minutes": event.timeout_minutes,
                    "last_activity": event.last_activity.isoformat() if event.last_activity else None,
                    "timestamp": event.timestamp.isoformat(),
                },
            }

            # Publish to NATS using room-specific subject
            subject = f"combat.timeout.{event.room_id}"
            success = await self.nats_service.publish(subject, message_data)

            if success:
                logger.info(
                    "Combat timeout event published to NATS",
                    combat_id=str(event.combat_id),
                    room_id=event.room_id,
                    timeout_minutes=event.timeout_minutes,
                )
            else:
                logger.error(
                    "Failed to publish combat timeout event to NATS",
                    combat_id=str(event.combat_id),
                    room_id=event.room_id,
                )

            return success

        except Exception as e:
            logger.error(
                "Error publishing combat timeout event",
                combat_id=str(event.combat_id),
                error=str(e),
                exc_info=True,
            )
            return False


# Global instance
combat_event_publisher = CombatEventPublisher()
