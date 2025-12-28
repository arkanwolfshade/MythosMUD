"""
Core combat service for managing combat state and logic.

This service handles all combat-related operations including state management,
turn order calculation, and combat resolution.
"""

from uuid import UUID

from server.app.lifespan import get_current_tick
from server.events.combat_events import CombatStartedEvent
from server.structured_logging.enhanced_logging_config import get_logger
from server.models.combat import (
    CombatInstance,
    CombatParticipant,
    CombatParticipantType,
    CombatResult,
    CombatStatus,
)
from server.services.combat_attack_handler import CombatAttackHandler
from server.services.combat_cleanup_handler import CombatCleanupHandler
from server.services.combat_death_handler import CombatDeathHandler
from server.services.combat_event_handler import CombatEventHandler
from server.services.combat_event_publisher import CombatEventPublisher
from server.services.combat_initialization import CombatInitializer
from server.services.combat_persistence_handler import CombatPersistenceHandler
from server.services.combat_turn_processor import CombatTurnProcessor
from server.services.combat_types import CombatParticipantData
from server.services.nats_exceptions import NATSError
from server.services.player_combat_service import PlayerCombatService

logger = get_logger(__name__)


class CombatService:
    """
    Service for managing combat instances and state.

    This service maintains in-memory combat state and provides methods
    for initiating combat, processing actions, and managing turn order.
    """

    def __init__(
        self,
        player_combat_service: PlayerCombatService | None = None,
        nats_service=None,
        npc_combat_integration_service=None,
        subject_manager=None,
        player_death_service=None,
        player_respawn_service=None,
        event_bus=None,
        magic_service=None,
    ):
        """Initialize the combat service."""
        from server.config import get_config
        from server.events.event_bus import EventBus

        self._active_combats: dict[UUID, CombatInstance] = {}
        self._player_combats: dict[UUID, UUID] = {}  # player_id -> combat_id
        self._npc_combats: dict[UUID, UUID] = {}  # npc_id -> combat_id
        self._combat_timeout_minutes = 30  # Configurable timeout
        self._player_combat_service = player_combat_service
        self._nats_service = nats_service
        self._npc_combat_integration_service = npc_combat_integration_service
        self._player_death_service = player_death_service
        self._player_respawn_service = player_respawn_service
        self.magic_service = magic_service  # For casting state checks
        # CRITICAL: Use shared EventBus instance, not a new one
        self._event_bus = event_bus or EventBus()
        # Create combat event publisher with proper NATS service and subject_manager
        logger.debug("Creating CombatEventPublisher with NATS service", nats_service_available=bool(nats_service))
        try:
            logger.debug("Creating CombatEventPublisher")
            # If no subject_manager provided, create one with default settings
            if subject_manager is None and nats_service is not None:
                from .nats_subject_manager import NATSSubjectManager

                subject_manager = NATSSubjectManager()
                logger.debug("Created NATSSubjectManager with default settings")
            self._combat_event_publisher = CombatEventPublisher(nats_service, subject_manager)
            logger.debug("CombatEventPublisher created successfully")
        except Exception as e:
            logger.error(
                "CRITICAL ERROR: Failed to create CombatEventPublisher",
                error=str(e),
                error_type=type(e).__name__,
                exc_info=True,
            )
            raise
        # Auto-progression configuration
        self._auto_progression_enabled = True
        # Get combat tick interval from config (defaults to 6 seconds = 1 Mythos minute)
        config = get_config()
        self._turn_interval_seconds = config.game.combat_tick_interval

        # Initialize helper handlers
        self._turn_processor = CombatTurnProcessor(self)
        self._attack_handler = CombatAttackHandler(self)
        self._death_handler = CombatDeathHandler(self)
        self._event_handler = CombatEventHandler(self)
        self._persistence_handler = CombatPersistenceHandler(self)
        self._cleanup_handler = CombatCleanupHandler(self)

    @property
    def auto_progression_enabled(self) -> bool:
        """Get auto-progression enabled status."""
        return self._auto_progression_enabled

    @auto_progression_enabled.setter
    def auto_progression_enabled(self, value: bool) -> None:
        """Set auto-progression enabled status."""
        self._auto_progression_enabled = value

    @property
    def turn_interval_seconds(self) -> int:
        """Get turn interval in seconds."""
        return self._turn_interval_seconds

    @turn_interval_seconds.setter
    def turn_interval_seconds(self, value: int) -> None:
        """Set turn interval in seconds."""
        self._turn_interval_seconds = value

    async def start_combat(
        self,
        room_id: str,
        attacker: CombatParticipantData,
        target: CombatParticipantData,
        current_tick: int,
    ) -> CombatInstance:
        """
        Start a new combat instance between two participants.

        Args:
            room_id: The room where combat is taking place
            attacker: Data for the attacking participant
            target: Data for the target participant
            current_tick: Current game tick

        Returns:
            The created CombatInstance

        Raises:
            ValueError: If combat cannot be started (invalid participants, etc.)
        """
        logger.info("Starting combat", attacker=attacker.name, target=target.name, room_id=room_id)
        # Check if either participant is already in combat
        if attacker.participant_id in self._player_combats or target.participant_id in self._npc_combats:
            raise ValueError("One or both participants are already in combat")

        # Create and initialize combat instance
        combat = CombatInitializer.create_combat_instance(
            room_id=room_id,
            attacker=attacker,
            target=target,
            current_tick=current_tick,
            auto_progression_enabled=self._auto_progression_enabled,
            turn_interval_seconds=self._turn_interval_seconds,
        )

        # Store combat and track state
        await self._register_combat(combat, attacker, room_id)

        logger.info("Combat started", combat_id=combat.combat_id, turn_order=combat.turn_order)

        # Publish combat started event
        await self._publish_combat_started_event(combat, room_id)

        return combat

    async def _register_combat(
        self,
        combat: CombatInstance,
        attacker: CombatParticipantData,
        room_id: str,
    ) -> None:
        """Register combat instance and track player combat state."""
        # Store combat instance
        self._active_combats[combat.combat_id] = combat
        self._player_combats[attacker.participant_id] = combat.combat_id

        # Get target participant ID from combat
        target_id = next(
            (p.participant_id for p in combat.participants.values() if p.participant_id != attacker.participant_id),
            None,
        )
        if target_id:
            self._npc_combats[target_id] = combat.combat_id

        # Track player combat state if player combat service is available
        if self._player_combat_service:
            await self._player_combat_service.track_player_combat_state(
                player_id=attacker.participant_id,
                player_name=attacker.name,
                combat_id=combat.combat_id,
                room_id=room_id,
            )

    async def _publish_combat_started_event(self, combat: CombatInstance, room_id: str) -> None:
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
            await self._combat_event_publisher.publish_combat_started(started_event)
            logger.debug("publish_combat_started completed", combat_id=combat.combat_id)
        except (NATSError, ValueError, RuntimeError, AttributeError, ConnectionError) as e:
            logger.error("Error publishing combat started event", error=str(e), exc_info=True)

    async def process_game_tick(self, current_tick: int) -> None:
        """
        Process game tick for combat auto-progression.

        Args:
            current_tick: Current game tick number
        """
        await self._turn_processor.process_game_tick(current_tick, self._active_combats, self._auto_progression_enabled)

    async def get_combat_by_participant(self, participant_id: UUID) -> CombatInstance | None:
        """
        Get combat instance for a specific participant.

        Args:
            participant_id: ID of the participant

        Returns:
            CombatInstance if found, None otherwise
        """
        combat_id = self._player_combats.get(participant_id) or self._npc_combats.get(participant_id)
        if combat_id:
            return self._active_combats.get(combat_id)
        return None

    async def _handle_player_dp_update(self, target: CombatParticipant, old_dp: int, combat: CombatInstance) -> None:
        """Handle player DP update, persistence, and event publishing."""
        await self._persistence_handler.publish_player_dp_update_event(
            target.participant_id,
            old_dp,
            target.current_dp,
            target.max_dp,
            combat_id=str(combat.combat_id),
            room_id=combat.room_id,
        )
        self._persistence_handler.persist_player_dp_background(
            target.participant_id,
            target.current_dp,
            old_dp,
            target.max_dp,
            combat.room_id,
            str(combat.combat_id),
        )

    async def _validate_and_get_combat_participants(
        self, attacker_id: UUID, target_id: UUID, is_initial_attack: bool
    ) -> tuple[CombatInstance, CombatParticipant, CombatParticipant]:
        """
        Validate attack and retrieve combat participants.

        Args:
            attacker_id: ID of the attacker
            target_id: ID of the target
            is_initial_attack: Whether this is the initial attack

        Returns:
            Tuple of (combat, attacker, target)

        Raises:
            ValueError: If attack is invalid
        """
        return await self._attack_handler.validate_and_get_combat_participants(
            attacker_id, target_id, is_initial_attack
        )

    async def _apply_attack_damage(
        self, combat: CombatInstance, target: CombatParticipant, damage: int
    ) -> tuple[int, bool, bool]:
        """
        Apply damage to target and update combat state.

        Args:
            combat: Combat instance
            target: Target participant
            damage: Damage amount

        Returns:
            Tuple of (old_dp, target_died, target_mortally_wounded)
        """
        old_dp, target_died, target_mortally_wounded = await self._attack_handler.apply_attack_damage(
            combat, target, damage
        )
        if target.participant_type == CombatParticipantType.PLAYER:
            await self._handle_player_dp_update(target, old_dp, combat)
        return old_dp, target_died, target_mortally_wounded

    async def _handle_target_state_changes(
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
        await self._death_handler.handle_target_state_changes(
            target, current_participant, target_mortally_wounded, target_died, combat
        )

    async def _handle_attack_events_and_xp(
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
        return await self._event_handler.handle_attack_events_and_xp(
            current_participant, target, damage, combat, target_died, target_id
        )

    async def _award_xp_to_player(
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
        await self._event_handler.award_xp_to_player(current_participant, target, target_id, xp_amount)

    async def _handle_combat_completion(self, combat: CombatInstance, combat_ended: bool) -> None:
        """
        Handle combat completion or continuation.

        Args:
            combat: Combat instance
            combat_ended: Whether combat has ended
        """
        if combat_ended:
            logger.info(
                "Combat ending - starting end combat process",
                combat_id=combat.combat_id,
                room_id=combat.room_id,
            )
            try:
                await self.end_combat(combat.combat_id, "Combat ended - one participant defeated")
                logger.info(
                    "Combat end process completed successfully",
                    combat_id=combat.combat_id,
                )
            except (
                NATSError,
                ValueError,
                RuntimeError,
                AttributeError,
                ConnectionError,
                TypeError,
                KeyError,
            ) as end_combat_error:
                # CRITICAL: Prevent combat end errors from disconnecting players
                logger.error(
                    "Error ending combat - preventing disconnect",
                    combat_id=combat.combat_id,
                    room_id=combat.room_id,
                    error=str(end_combat_error),
                    exc_info=True,
                )
        else:
            # Set up next turn tick for auto-progression
            combat.next_turn_tick = get_current_tick() + combat.turn_interval_ticks
            logger.debug("Combat attack processed, auto-progression enabled", combat_id=combat.combat_id)

    async def process_attack(
        self, attacker_id: UUID, target_id: UUID, damage: int = 10, is_initial_attack: bool = False
    ) -> CombatResult:
        """
        Process an attack action in combat.

        Args:
            attacker_id: ID of the attacker
            target_id: ID of the target
            damage: Amount of damage to deal
            is_initial_attack: Whether this is the initial attack

        Returns:
            CombatResult containing the outcome

        Raises:
            ValueError: If attack is invalid (not in combat, wrong turn, etc.)
        """
        # Validate and get participants
        combat, current_participant, target = await self._validate_and_get_combat_participants(
            attacker_id, target_id, is_initial_attack
        )

        logger.info("Processing attack", attacker_name=current_participant.name, target_name=target.name, damage=damage)

        # Apply damage
        # old_dp is handled inside _apply_attack_damage via _handle_player_dp_update
        _, target_died, target_mortally_wounded = await self._apply_attack_damage(combat, target, damage)

        # Check if combat ended
        combat_ended = combat.is_combat_over()

        # Create result
        health_info = f" ({target.current_dp}/{target.max_dp} DP)"
        attack_message = f"{current_participant.name} attacks {target.name} for {damage} damage{health_info}"
        result = CombatResult(
            success=True,
            damage=damage,
            target_died=target_died,
            combat_ended=combat_ended,
            message=attack_message,
            combat_id=combat.combat_id,
        )

        # Handle state changes (mortally wounded, death)
        await self._handle_target_state_changes(
            target, current_participant, target_mortally_wounded, target_died, combat
        )

        # Publish events and calculate XP
        xp_awarded = await self._handle_attack_events_and_xp(
            current_participant, target, damage, combat, target_died, target_id
        )
        # Handle None case: default to 0 if no XP awarded
        result.xp_awarded = xp_awarded if xp_awarded is not None else 0

        # Award XP to player if they defeated an NPC
        if target_died:
            await self._award_xp_to_player(current_participant, target, target_id, result.xp_awarded)

        # Handle combat completion
        await self._handle_combat_completion(combat, combat_ended)

        return result

    def _cleanup_combat_tracking(self, combat: CombatInstance) -> None:
        """Remove combat from tracking dictionaries."""
        self._cleanup_handler.cleanup_combat_tracking(combat)

    def _check_connection_state(self, room_id: str) -> None:
        """Check connection state before publishing combat ended event."""
        self._cleanup_handler.check_connection_state(room_id)

    async def end_combat(self, combat_id: UUID, reason: str = "Combat ended") -> None:
        """
        End a combat instance.

        Args:
            combat_id: ID of the combat to end
            reason: Reason for ending combat
        """
        combat = self._active_combats.get(combat_id)
        if not combat:
            logger.warning("Attempted to end non-existent combat", combat_id=combat_id)
            return

        logger.info("Ending combat", combat_id=combat_id, reason=reason)

        combat.status = CombatStatus.ENDED
        self._cleanup_combat_tracking(combat)

        if self._player_combat_service:
            await self._player_combat_service.handle_combat_end(combat_id)

        logger.debug(
            "Preparing combat ended event",
            combat_id=combat_id,
            room_id=combat.room_id,
            participant_count=len(combat.participants),
        )

        self._check_connection_state(combat.room_id)
        await self._event_handler.publish_combat_ended_event(combat, reason)

        logger.info("Combat ended successfully", combat_id=combat_id)

    async def cleanup_stale_combats(self) -> int:
        """
        Clean up combats that have been inactive for too long.

        Returns:
            Number of combats cleaned up
        """
        return await self._cleanup_handler.cleanup_stale_combats(self._combat_timeout_minutes)

    async def get_combat_stats(self) -> dict[str, int]:
        """
        Get statistics about active combats.

        Returns:
            Dictionary with combat statistics
        """
        return {
            "active_combats": len(self._active_combats),
            "player_combats": len(self._player_combats),
            "npc_combats": len(self._npc_combats),
        }


# Global combat service instance - will be properly initialized by lifespan
# Using a dict container to avoid global statement warnings
_combat_service_state: dict[str, CombatService | None] = {"service": None}


def get_combat_service() -> CombatService | None:
    """Get the global combat service instance."""
    return _combat_service_state["service"]


def set_combat_service(service: CombatService | None) -> None:
    """Set the global combat service instance."""
    _combat_service_state["service"] = service


# For backward compatibility
combat_service = None
