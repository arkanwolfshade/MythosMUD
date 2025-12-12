"""
Combat death handling logic.

Handles player death, NPC death, mortally wounded states, and related events.
"""

from server.logging.enhanced_logging_config import get_logger
from server.models.combat import CombatInstance, CombatParticipant, CombatParticipantType
from server.services.nats_exceptions import NATSError

logger = get_logger(__name__)


class CombatDeathHandler:
    """Handles combat death events and state changes."""

    def __init__(self, combat_service):
        """
        Initialize the death handler.

        Args:
            combat_service: Reference to the parent CombatService
        """
        self._combat_service = combat_service

    async def _handle_player_death_events(self, target: CombatParticipant, combat: CombatInstance) -> None:
        """Handle player death events including mortally wounded, death, and corpse creation."""
        try:
            from ..services.combat_messaging_integration import combat_messaging_integration

            await combat_messaging_integration.broadcast_player_death(
                player_id=str(target.participant_id),
                player_name=target.name,
                room_id=combat.room_id,
                death_location=combat.room_id,
            )
            logger.info("Player death event published", player_id=target.participant_id, player_name=target.name)

            # Create corpse container on death
            await self._create_corpse_on_death(target, combat)
        except (NATSError, ValueError, RuntimeError, AttributeError, ConnectionError, TypeError, KeyError) as e:
            logger.error("Error publishing player death event", error=str(e), exc_info=True)

    async def _create_corpse_on_death(self, target: CombatParticipant, combat: CombatInstance) -> None:
        """Create corpse container when player dies."""
        try:
            from ..container import ApplicationContainer
            from ..services.corpse_lifecycle_service import CorpseLifecycleService

            connection_manager = getattr(self._combat_service, "_connection_manager", None)
            persistence = None

            if connection_manager is None:
                try:
                    container = ApplicationContainer.get_instance()
                    connection_manager = getattr(container, "connection_manager", None)
                    persistence = getattr(container, "async_persistence", None) if container else None
                except (ImportError, AttributeError, RuntimeError, ValueError):
                    pass

            if persistence is None:
                logger.warning("Could not get persistence for corpse creation, skipping")
                return

            corpse_service = CorpseLifecycleService(persistence=persistence, connection_manager=connection_manager)
            corpse = await corpse_service.create_corpse_on_death(
                player_id=target.participant_id,
                room_id=combat.room_id,
                grace_period_seconds=300,
                decay_hours=1,
            )
            logger.info(
                "Corpse container created on death",
                container_id=str(corpse.container_id),
                player_id=target.participant_id,
                room_id=combat.room_id,
            )
        except (ImportError, AttributeError, RuntimeError, ValueError, ConnectionError, OSError) as corpse_error:
            logger.error(
                "Error creating corpse container on death",
                error=str(corpse_error),
                player_id=target.participant_id,
                room_id=combat.room_id,
                exc_info=True,
            )

    async def _handle_npc_death(self, target: CombatParticipant, combat: CombatInstance, xp_reward: int) -> None:
        """Handle NPC death event publishing and ID resolution."""
        try:
            from ..container import ApplicationContainer

            container = ApplicationContainer.get_instance()
            connection_manager = getattr(container, "connection_manager", None) if container else None
            if connection_manager is not None:
                canonical_room_id = connection_manager.canonical_room_id(combat.room_id) or combat.room_id
                room_subscribers = connection_manager.room_subscriptions.get(canonical_room_id, set())
                logger.debug(
                    "Connection state check before NPC death event",
                    room_id=combat.room_id,
                    canonical_room_id=canonical_room_id,
                    connected_players_count=len(room_subscribers),
                    connected_player_ids=list(room_subscribers),
                )
        except (
            AttributeError,
            ValueError,
            TypeError,
            RuntimeError,
            NATSError,
            ConnectionError,
            KeyError,
        ) as conn_check_error:
            logger.warning(
                "Could not check connection state before NPC death event",
                error=str(conn_check_error),
                room_id=combat.room_id,
            )

        try:
            original_npc_id = str(target.participant_id)
            npc_combat_integration_service = getattr(self._combat_service, "_npc_combat_integration_service", None)
            if npc_combat_integration_service:
                resolved_id = npc_combat_integration_service.get_original_string_id(target.participant_id)
                if resolved_id:
                    original_npc_id = resolved_id
                    logger.info(
                        "Resolved UUID to original NPC ID for death event",
                        uuid=target.participant_id,
                        original_id=original_npc_id,
                    )
                else:
                    logger.error(
                        "UUID not found in mapping - NPC WILL NOT RESPAWN!",
                        uuid=target.participant_id,
                        npc_name=target.name,
                        combat_id=combat.combat_id,
                    )
            else:
                logger.error(
                    "NPC combat integration service not available - NPC WILL NOT RESPAWN!",
                    uuid=target.participant_id,
                    npc_name=target.name,
                    combat_id=combat.combat_id,
                )

            combat_event_publisher = getattr(self._combat_service, "_combat_event_publisher", None)
            if combat_event_publisher:
                from server.events.combat_events import NPCDiedEvent

                death_event = NPCDiedEvent(
                    combat_id=combat.combat_id,
                    room_id=combat.room_id,
                    npc_id=original_npc_id,
                    npc_name=target.name,
                    xp_reward=xp_reward,
                )
                await combat_event_publisher.publish_npc_died(death_event)
                logger.info("NPCDiedEvent published successfully", npc_id=original_npc_id, combat_id=combat.combat_id)
            else:
                logger.error("Combat event publisher not available for NPC death event")

        except (NATSError, ValueError, RuntimeError, AttributeError, ConnectionError, TypeError) as death_event_error:
            logger.error(
                "Error publishing NPC death event - preventing disconnect",
                target_name=target.name,
                target_id=target.participant_id,
                combat_id=combat.combat_id,
                room_id=combat.room_id,
                error=str(death_event_error),
                exc_info=True,
            )

    async def handle_target_state_changes(
        self,
        target: CombatParticipant,
        current_participant: CombatParticipant,
        target_mortally_wounded: bool,
        target_died: bool,
        combat: CombatInstance,
    ) -> None:
        """
        Handle mortally wounded and death state changes for target.

        Args:
            target: Target participant
            current_participant: Attacking participant
            target_mortally_wounded: Whether target became mortally wounded
            target_died: Whether target died
            combat: Combat instance
        """
        if target_mortally_wounded and target.participant_type == CombatParticipantType.PLAYER:
            try:
                from ..services.combat_messaging_integration import combat_messaging_integration

                attacker_name = current_participant.name if current_participant else None
                await combat_messaging_integration.broadcast_player_mortally_wounded(
                    player_id=str(target.participant_id),
                    player_name=target.name,
                    attacker_name=attacker_name,
                    room_id=combat.room_id,
                )
                logger.info(
                    "Player mortally wounded event published",
                    player_id=target.participant_id,
                    player_name=target.name,
                )
            except (NATSError, ValueError, RuntimeError, AttributeError, ConnectionError, TypeError, KeyError) as e:
                logger.error("Error publishing player mortally wounded event", error=str(e), exc_info=True)

        if target_died and target.participant_type == CombatParticipantType.PLAYER:
            await self._handle_player_death_events(target, combat)

    async def handle_npc_death(self, target: CombatParticipant, combat: CombatInstance, xp_reward: int) -> None:
        """
        Handle NPC death event publishing and ID resolution.

        Args:
            target: NPC participant that died
            combat: Combat instance
            xp_reward: XP reward amount for defeating the NPC
        """
        await self._handle_npc_death(target, combat, xp_reward)
