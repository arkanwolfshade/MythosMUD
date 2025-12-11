"""
Combat event publishing logic.

Handles publishing of combat-related events (attacks, deaths, XP awards, combat ended).
"""

from datetime import datetime
from uuid import UUID

from server.events.combat_events import (
    CombatEndedEvent,
    NPCAttackedEvent,
    NPCTookDamageEvent,
    PlayerAttackedEvent,
)
from server.logging.enhanced_logging_config import get_logger
from server.models.combat import CombatInstance, CombatParticipant, CombatParticipantType
from server.services.nats_exceptions import NATSError

logger = get_logger(__name__)


class CombatEventHandler:
    """Handles combat event publishing."""

    def __init__(self, combat_service):
        """
        Initialize the event handler.

        Args:
            combat_service: Reference to the parent CombatService
        """
        self._combat_service = combat_service

    async def _publish_attack_events(
        self,
        current_participant: CombatParticipant,
        target: CombatParticipant,
        damage: int,
        combat: CombatInstance,
    ) -> None:
        """Publish combat attack events based on participant types."""
        combat_event_publisher = getattr(self._combat_service, "_combat_event_publisher", None)
        if not combat_event_publisher:
            logger.warning("Combat event publisher not available")
            return

        if current_participant.participant_type == CombatParticipantType.PLAYER:
            attack_event = PlayerAttackedEvent(
                combat_id=combat.combat_id,
                room_id=combat.room_id,
                attacker_id=current_participant.participant_id,
                attacker_name=current_participant.name,
                target_id=target.participant_id,
                target_name=target.name,
                damage=damage,
                action_type="auto_attack",
                target_current_dp=target.current_dp,  # Event field name kept for backward compatibility
                target_max_dp=target.max_dp,  # Event field name kept for backward compatibility
            )
            await combat_event_publisher.publish_player_attacked(attack_event)
        else:
            npc_attack_event = NPCAttackedEvent(
                combat_id=combat.combat_id,
                room_id=combat.room_id,
                attacker_id=current_participant.participant_id,
                attacker_name=current_participant.name,
                npc_id=target.participant_id,
                npc_name=target.name,
                damage=damage,
                action_type="auto_attack",
                target_current_dp=target.current_dp,  # Event field name kept for backward compatibility
                target_max_dp=target.max_dp,  # Event field name kept for backward compatibility
            )
            await combat_event_publisher.publish_npc_attacked(npc_attack_event)

        if target.participant_type == CombatParticipantType.NPC:
            damage_event = NPCTookDamageEvent(
                combat_id=combat.combat_id,
                room_id=combat.room_id,
                npc_id=target.participant_id,
                npc_name=target.name,
                damage=damage,
                current_dp=target.current_dp,  # Event field name kept for backward compatibility
                max_dp=target.max_dp,  # Event field name kept for backward compatibility
            )
            await combat_event_publisher.publish_npc_took_damage(damage_event)

    async def handle_attack_events_and_xp(
        self,
        current_participant: CombatParticipant,
        target: CombatParticipant,
        damage: int,
        combat: CombatInstance,
        target_died: bool,
        target_id: UUID,
    ) -> int | None:
        """
        Publish attack events and calculate XP reward.

        Args:
            current_participant: Attacking participant
            target: Target participant
            damage: Damage amount
            combat: Combat instance
            target_died: Whether target died
            target_id: Target participant ID

        Returns:
            XP reward amount if target died, None otherwise
        """
        try:
            await self._publish_attack_events(current_participant, target, damage, combat)

            if target_died:
                xp_awarded = await self._calculate_xp_reward(target_id)
                if target.participant_type == CombatParticipantType.NPC:
                    death_handler = getattr(self._combat_service, "_death_handler", None)
                    if death_handler:
                        await death_handler.handle_npc_death(target, combat, xp_awarded or 0)
                return xp_awarded

        except (NATSError, ValueError, RuntimeError, AttributeError, ConnectionError, TypeError, KeyError) as e:
            logger.error("Error publishing combat events", error=str(e), exc_info=True)

        return None

    async def _calculate_xp_reward(self, npc_id: UUID) -> int:
        """
        Calculate XP reward for defeating an NPC.

        Args:
            npc_id: ID of the defeated NPC

        Returns:
            XP reward amount
        """
        logger.info(
            "CombatEventHandler._calculate_xp_reward called",
            npc_id=npc_id,
            has_npc_service=bool(getattr(self._combat_service, "_npc_combat_integration_service", None)),
            has_player_service=bool(getattr(self._combat_service, "_player_combat_service", None)),
        )

        # Use PlayerCombatService if available
        player_combat_service = getattr(self._combat_service, "_player_combat_service", None)
        if player_combat_service:
            logger.info("Using PlayerCombatService for XP calculation", npc_id=npc_id)
            return await player_combat_service.calculate_xp_reward(npc_id)
        else:
            # Fallback to default XP value if no player combat service
            logger.info("Using default XP reward", npc_id=npc_id)
            return 0  # Default XP reward changed to 0 to highlight database lookup issues

    async def award_xp_to_player(
        self, current_participant: CombatParticipant, target: CombatParticipant, target_id: UUID, xp_amount: int | None
    ) -> None:
        """
        Award XP to player for defeating an NPC.

        Args:
            current_participant: Attacking participant (player)
            target: Defeated target participant
            target_id: Defeated NPC ID
            xp_amount: XP amount to award
        """
        if (
            current_participant.participant_type == CombatParticipantType.PLAYER
            and target.participant_type == CombatParticipantType.NPC
        ):
            player_combat_service = getattr(self._combat_service, "_player_combat_service", None)
            if player_combat_service and xp_amount is not None:
                logger.debug(
                    "Awarding XP to player for NPC defeat",
                    player_id=current_participant.participant_id,
                    npc_id=target_id,
                    xp_amount=xp_amount,
                )
                try:
                    await player_combat_service.award_xp_on_npc_death(
                        player_id=current_participant.participant_id, npc_id=target_id, xp_amount=xp_amount
                    )
                    logger.debug(
                        "XP award completed successfully",
                        player_id=current_participant.participant_id,
                        xp_amount=xp_amount,
                    )
                except (
                    ValueError,
                    TypeError,
                    AttributeError,
                    RuntimeError,
                    NATSError,
                    ConnectionError,
                    KeyError,
                ) as xp_error:
                    # CRITICAL: Don't let XP award errors disconnect player
                    logger.error(
                        "Error awarding XP to player - preventing disconnect",
                        player_id=current_participant.participant_id,
                        npc_id=target_id,
                        xp_amount=xp_amount,
                        error=str(xp_error),
                        exc_info=True,
                    )

    async def publish_combat_ended_event(self, combat: CombatInstance, reason: str) -> None:
        """Publish combat ended event."""
        combat_event_publisher = getattr(self._combat_service, "_combat_event_publisher", None)
        if not combat_event_publisher:
            logger.warning("Combat event publisher not available for combat ended event")
            return

        try:
            ended_event = CombatEndedEvent(
                combat_id=combat.combat_id,
                room_id=combat.room_id,
                reason=reason,
                duration_seconds=int((datetime.now() - combat.start_time).total_seconds())
                if hasattr(combat, "start_time")
                else 0,
                participants={
                    str(p.participant_id): {"name": p.name, "dp": p.current_dp, "max_dp": p.max_dp}
                    for p in combat.participants.values()
                },
            )
            logger.info(
                "Publishing combat ended event",
                combat_id=combat.combat_id,
                room_id=combat.room_id,
                participant_count=len(combat.participants),
            )
            await combat_event_publisher.publish_combat_ended(ended_event)
            logger.info("Combat ended event published successfully", combat_id=combat.combat_id)
        except (NATSError, ValueError, RuntimeError, AttributeError, ConnectionError, TypeError, KeyError) as e:
            logger.error(
                "Error publishing combat ended event - combat already cleaned up",
                combat_id=combat.combat_id,
                room_id=combat.room_id,
                error=str(e),
                exc_info=True,
            )
