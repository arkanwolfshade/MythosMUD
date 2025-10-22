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
        print("COMBAT EVENT PUBLISHER __init__ CALLED!")
        logger.debug("CombatEventPublisher __init__ method entered")
        # Import here to avoid circular dependencies
        from ..services.nats_service import nats_service as global_nats_service

        print("COMBAT EVENT PUBLISHER: After global_nats_service import")

        self.nats_service = nats_service or global_nats_service
        print(f"DEBUG: CombatEventPublisher initialized with NATS service: {bool(self.nats_service)}")
        logger.info("CombatEventPublisher initialized", nats_service_available=bool(self.nats_service))

    async def publish_combat_started(self, event: CombatStartedEvent) -> bool:
        """
        Publish combat started event to NATS.

        Args:
            event: CombatStartedEvent to publish

        Returns:
            True if published successfully, False otherwise
        """
        try:
            print(f"COMBAT EVENT PUBLISHER: Starting combat event publishing for combat {event.combat_id}")
            logger.debug("Starting combat event publishing", combat_id=str(event.combat_id), room_id=event.room_id)

            if not self.nats_service:
                logger.error("NATS service not available for combat event publishing")
                return False

            if not self.nats_service.is_connected():
                logger.error(
                    "NATS service not connected for combat event publishing",
                    nats_connected=self.nats_service.is_connected(),
                )
                return False

            # Create message data for NATS
            message_data = {
                "event_type": "combat_started",
                "combat_id": str(event.combat_id),
                "room_id": event.room_id,
                "participants": event.participants,
                "turn_order": event.turn_order,
                "timestamp": event.timestamp.isoformat(),
            }

            # Publish to NATS using room-specific subject
            subject = f"combat.started.{event.room_id}"
            logger.debug("Publishing combat started event to NATS", subject=subject, message_data=message_data)
            success = await self.nats_service.publish(subject, message_data)

            if success:
                logger.info(
                    "Combat started event published to NATS",
                    combat_id=str(event.combat_id),
                    room_id=event.room_id,
                    subject=subject,
                )
            else:
                logger.error(
                    "Failed to publish combat started event to NATS",
                    combat_id=str(event.combat_id),
                    room_id=event.room_id,
                )

            return success

        except Exception as e:
            logger.error(
                "Error publishing combat started event",
                combat_id=str(event.combat_id),
                error=str(e),
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
            if not self.nats_service or not self.nats_service.is_connected():
                logger.error("NATS service not available for combat event publishing")
                return False

            # Create message data for NATS
            message_data = {
                "event_type": "combat_ended",
                "combat_id": str(event.combat_id),
                "room_id": event.room_id,
                "reason": event.reason,
                "duration_seconds": event.duration_seconds,
                "participants": event.participants,
                "timestamp": event.timestamp.isoformat(),
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
            if not self.nats_service or not self.nats_service.is_connected():
                logger.error("NATS service not available for combat event publishing")
                return False

            # Create message data for NATS
            message_data = {
                "event_type": "player_attacked",
                "combat_id": str(event.combat_id),
                "attacker_id": str(event.attacker_id),
                "attacker_name": event.attacker_name,
                "target_id": str(event.target_id),
                "target_name": event.target_name,
                "damage": event.damage,
                "action_type": event.action_type,
                "timestamp": event.timestamp.isoformat(),
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
            if not self.nats_service or not self.nats_service.is_connected():
                logger.error("NATS service not available for combat event publishing")
                return False

            # Create message data for NATS
            message_data = {
                "event_type": "npc_attacked",
                "combat_id": str(event.combat_id),
                "attacker_id": str(event.attacker_id),
                "attacker_name": event.attacker_name,
                "npc_id": str(event.npc_id),
                "npc_name": event.npc_name,
                "damage": event.damage,
                "action_type": event.action_type,
                "timestamp": event.timestamp.isoformat(),
            }

            # Publish to NATS using room-specific subject
            subject = f"combat.attack.{event.room_id}"
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
            if not self.nats_service or not self.nats_service.is_connected():
                logger.error("NATS service not available for combat event publishing")
                return False

            # Create message data for NATS
            message_data = {
                "event_type": "npc_took_damage",
                "combat_id": str(event.combat_id),
                "npc_id": str(event.npc_id),
                "npc_name": event.npc_name,
                "damage": event.damage,
                "current_hp": event.current_hp,
                "max_hp": event.max_hp,
                "timestamp": event.timestamp.isoformat(),
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
            if not self.nats_service or not self.nats_service.is_connected():
                logger.error("NATS service not available for combat event publishing")
                return False

            # Create message data for NATS
            message_data = {
                "event_type": "npc_died",
                "combat_id": str(event.combat_id),
                "npc_id": str(event.npc_id),
                "npc_name": event.npc_name,
                "xp_reward": event.xp_reward,
                "timestamp": event.timestamp.isoformat(),
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
            if not self.nats_service or not self.nats_service.is_connected():
                logger.error("NATS service not available for combat event publishing")
                return False

            # Create message data for NATS
            message_data = {
                "event_type": "combat_turn_advanced",
                "combat_id": str(event.combat_id),
                "room_id": event.room_id,
                "current_turn": event.current_turn,
                "combat_round": event.combat_round,
                "next_participant": event.next_participant,
                "timestamp": event.timestamp.isoformat(),
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
            if not self.nats_service or not self.nats_service.is_connected():
                logger.error("NATS service not available for combat event publishing")
                return False

            # Create message data for NATS
            message_data = {
                "event_type": "combat_timeout",
                "combat_id": str(event.combat_id),
                "room_id": event.room_id,
                "timeout_minutes": event.timeout_minutes,
                "last_activity": event.last_activity.isoformat() if event.last_activity else None,
                "timestamp": event.timestamp.isoformat(),
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
