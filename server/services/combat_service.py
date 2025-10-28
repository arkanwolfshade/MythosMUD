"""
Core combat service for managing combat state and logic.

This service handles all combat-related operations including state management,
turn order calculation, and combat resolution.
"""

from datetime import datetime, timedelta
from uuid import UUID

from server.app.lifespan import get_current_tick
from server.config import get_config
from server.events.combat_events import (
    CombatEndedEvent,
    CombatStartedEvent,
    NPCAttackedEvent,
    NPCDiedEvent,
    NPCTookDamageEvent,
    PlayerAttackedEvent,
)
from server.logging.enhanced_logging_config import get_logger
from server.models.combat import (
    CombatInstance,
    CombatParticipant,
    CombatParticipantType,
    CombatResult,
    CombatStatus,
)
from server.services.combat_event_publisher import CombatEventPublisher
from server.services.player_combat_service import PlayerCombatService

logger = get_logger(__name__)


class CombatService:
    """
    Service for managing combat instances and state.

    This service maintains in-memory combat state and provides methods
    for initiating combat, processing actions, and managing turn order.
    """

    def __init__(
        self, player_combat_service: PlayerCombatService = None, nats_service=None, npc_combat_integration_service=None
    ):
        """Initialize the combat service."""
        self._active_combats: dict[UUID, CombatInstance] = {}
        self._player_combats: dict[UUID, UUID] = {}  # player_id -> combat_id
        self._npc_combats: dict[UUID, UUID] = {}  # npc_id -> combat_id
        self._combat_timeout_minutes = 30  # Configurable timeout
        self._player_combat_service = player_combat_service
        self._nats_service = nats_service
        self._npc_combat_integration_service = npc_combat_integration_service
        # Create combat event publisher with proper NATS service
        logger.debug("Creating CombatEventPublisher with NATS service", nats_service_available=bool(nats_service))
        try:
            logger.debug("Creating CombatEventPublisher")
            self._combat_event_publisher = CombatEventPublisher(nats_service)
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
        self._turn_interval_seconds = 6

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
        attacker_id: UUID,
        target_id: UUID,
        attacker_name: str,
        target_name: str,
        attacker_hp: int,
        attacker_max_hp: int,
        attacker_dex: int,
        target_hp: int,
        target_max_hp: int,
        target_dex: int,
        current_tick: int,
        attacker_type: CombatParticipantType = CombatParticipantType.PLAYER,
        target_type: CombatParticipantType = CombatParticipantType.NPC,
    ) -> CombatInstance:
        """
        Start a new combat instance between two participants.

        Args:
            room_id: The room where combat is taking place
            attacker_id: ID of the participant initiating combat
            target_id: ID of the target participant
            attacker_name: Name of the attacker
            target_name: Name of the target
            attacker_hp: Current HP of attacker
            attacker_max_hp: Max HP of attacker
            attacker_dex: Dexterity of attacker
            target_hp: Current HP of target
            target_max_hp: Max HP of target
            target_dex: Dexterity of target

        Returns:
            The created CombatInstance

        Raises:
            ValueError: If combat cannot be started (invalid participants, etc.)
        """
        logger.info("Starting combat", attacker=attacker_name, target=target_name, room_id=room_id)

        # Check if either participant is already in combat
        if attacker_id in self._player_combats or target_id in self._npc_combats:
            raise ValueError("One or both participants are already in combat")

        # Create combat instance with auto-progression configuration
        combat = CombatInstance(
            room_id=room_id,
            auto_progression_enabled=self._auto_progression_enabled,
            turn_interval_ticks=self._turn_interval_seconds,  # Convert seconds to ticks (1:1 for now)
            start_tick=current_tick,
            last_activity_tick=current_tick,
            next_turn_tick=current_tick + self._turn_interval_seconds,
        )

        # Create participants
        attacker = CombatParticipant(
            participant_id=attacker_id,
            participant_type=attacker_type,
            name=attacker_name,
            current_hp=attacker_hp,
            max_hp=attacker_max_hp,
            dexterity=attacker_dex,
        )

        target = CombatParticipant(
            participant_id=target_id,
            participant_type=target_type,
            name=target_name,
            current_hp=target_hp,
            max_hp=target_max_hp,
            dexterity=target_dex,
        )

        # Add participants to combat
        combat.participants[attacker_id] = attacker
        combat.participants[target_id] = target

        # Calculate turn order: all participants sorted by dexterity (highest first)
        all_participants = [(attacker_id, attacker_dex), (target_id, target_dex)]
        all_participants.sort(key=lambda x: x[1], reverse=True)

        # Build turn order: highest dexterity first
        combat.turn_order = [pid for pid, _ in all_participants]

        # Store combat instance
        self._active_combats[combat.combat_id] = combat
        self._player_combats[attacker_id] = combat.combat_id
        self._npc_combats[target_id] = combat.combat_id

        # Track player combat state if player combat service is available
        if self._player_combat_service:
            await self._player_combat_service.track_player_combat_state(
                player_id=attacker_id, player_name=attacker_name, combat_id=combat.combat_id, room_id=room_id
            )

        logger.info("Combat started", combat_id=combat.combat_id, turn_order=combat.turn_order)

        # Publish combat started event
        try:
            logger.debug("Creating CombatStartedEvent", combat_id=combat.combat_id)
            started_event = CombatStartedEvent(
                event_type="combat_started",
                timestamp=datetime.now(),
                combat_id=combat.combat_id,
                room_id=room_id,
                participants={
                    str(p.participant_id): {"name": p.name, "hp": p.current_hp, "max_hp": p.max_hp}
                    for p in combat.participants.values()
                },
                turn_order=[str(pid) for pid in combat.turn_order],
            )
            logger.debug("Calling publish_combat_started", combat_id=combat.combat_id)
            await self._combat_event_publisher.publish_combat_started(started_event)
            logger.debug("publish_combat_started completed", combat_id=combat.combat_id)
        except Exception as e:
            logger.error("Error publishing combat started event", error=str(e), exc_info=True)

        return combat

    async def process_game_tick(self, current_tick: int) -> None:
        """
        Process game tick for combat auto-progression.

        Args:
            current_tick: Current game tick number
        """
        logger.info(
            "Combat tick processing",
            tick=current_tick,
            auto_progression_enabled=self._auto_progression_enabled,
            active_combats_count=len(self._active_combats),
        )
        if not self._auto_progression_enabled:
            logger.info("[COMBAT TICK] Auto-progression is disabled, returning early")
            return

        # Check all active combats for auto-progression
        for combat_id, combat in list(self._active_combats.items()):
            if combat.status != CombatStatus.ACTIVE:
                continue

            if not combat.auto_progression_enabled:
                continue

            logger.debug(
                "Combat auto-progression check",
                combat_id=combat_id,
                current_tick=current_tick,
                next_turn_tick=combat.next_turn_tick,
                auto_progression_enabled=combat.auto_progression_enabled,
            )

            # Check if it's time for the next turn
            if current_tick >= combat.next_turn_tick:
                logger.debug("Auto-progression triggered", combat_id=combat_id, tick=current_tick)
                await self._advance_turn_automatically(combat, current_tick)

    async def _advance_turn_automatically(self, combat: CombatInstance, current_tick: int) -> None:
        """
        Automatically advance combat turn and process NPC actions.

        Args:
            combat: Combat instance to advance
            current_tick: Current game tick
        """
        # Update activity
        combat.update_activity(current_tick)

        # Advance turn
        combat.advance_turn(current_tick)

        # Get current participant
        current_participant = combat.get_current_turn_participant()
        if not current_participant:
            logger.warning("No current participant for combat", combat_id=combat.combat_id)
            logger.debug(
                "Combat state debug",
                turn_order=combat.turn_order,
                current_turn=combat.current_turn,
                participants=list(combat.participants.keys()),
            )
            # Check if the participant ID exists in turn_order but not in participants
            if combat.turn_order and combat.current_turn < len(combat.turn_order):
                expected_participant_id = combat.turn_order[combat.current_turn]
                logger.debug(
                    "Expected participant lookup",
                    expected_participant_id=expected_participant_id,
                    exists_in_participants=expected_participant_id in combat.participants,
                )

                # If participant is missing, try to fix the combat state
                if expected_participant_id not in combat.participants:
                    logger.error(
                        "Participant not found in participants dictionary - combat state corrupted",
                        participant_id=expected_participant_id,
                    )
                    # Remove the corrupted combat
                    self._active_combats.pop(combat.combat_id, None)
                    return

                # Try to find the participant by matching UUID values
                found_participant = None
                for participant_id, participant in combat.participants.items():
                    if str(participant_id) == str(expected_participant_id):
                        found_participant = participant
                        logger.debug("Found participant by UUID string match", participant=participant)
                        break

                if found_participant:
                    current_participant = found_participant
                else:
                    logger.error(
                        "Could not find participant even by UUID string match",
                        participant_id=expected_participant_id,
                    )
                    return
            else:
                return

        # Debug logging to understand participant type
        participant_id = getattr(current_participant, "participant_id", "NO_PARTICIPANT_ID")
        logger.debug(
            "Current participant type",
            participant_type=type(current_participant).__name__,
            participant_id=participant_id,
        )

        # Additional debugging for the combat state
        logger.debug(
            "Combat state debug",
            turn_order=combat.turn_order,
            current_turn=combat.current_turn,
            participants=list(combat.participants.keys()),
        )

        # Debug the specific participant lookup
        if combat.turn_order and combat.current_turn < len(combat.turn_order):
            current_participant_id = combat.turn_order[combat.current_turn]
            logger.debug(
                "Participant lookup",
                looking_for=current_participant_id,
                available_participants=list(combat.participants.keys()),
            )
            found_participant = combat.participants.get(current_participant_id)
            logger.debug("Participant found", participant=found_participant)
            logger.debug("current_participant (from get_current_turn_participant)", participant=current_participant)
            logger.debug("Participant comparison", same=found_participant == current_participant)

        # If it's an NPC's turn, process their action
        if current_participant.participant_type == CombatParticipantType.NPC:
            await self._process_npc_turn(combat, current_participant, current_tick)
        else:
            # Player's turn - perform automatic basic attack
            # Validate that current_participant is a CombatParticipant
            if not isinstance(current_participant, CombatParticipant):
                logger.error(
                    "Expected CombatParticipant",
                    got_type=type(current_participant).__name__,
                    participant=current_participant,
                )
                return
            await self._process_player_turn(combat, current_participant, current_tick)

    async def _process_npc_turn(self, combat: CombatInstance, npc: CombatParticipant, current_tick: int) -> None:
        """
        Process NPC turn with actual combat attack.

        Args:
            combat: Combat instance
            npc: NPC participant
            current_tick: Current game tick
        """
        try:
            # Validate that we received a proper CombatParticipant object
            if not isinstance(npc, CombatParticipant):
                logger.error("Expected CombatParticipant", got_type=type(npc).__name__, npc=npc)
                return

            # Debug logging to understand what we're receiving
            logger.debug("_process_npc_turn called", npc_type=type(npc).__name__, npc=npc)
            if hasattr(npc, "participant_id"):
                logger.debug(
                    "NPC participant_id", participant_id=npc.participant_id, id_type=type(npc.participant_id).__name__
                )
            else:
                logger.error("NPC object missing participant_id attribute", npc=npc)
                return

            # Find the target (other participant in combat)
            target = None
            for participant in combat.participants.values():
                if participant.participant_id != npc.participant_id:
                    target = participant
                    break

            if not target:
                logger.warning("No target found for NPC", npc_name=npc.name, combat_id=combat.combat_id)
                return

            # Perform automatic basic attack
            logger.debug("NPC performing automatic attack", npc_name=npc.name, target_name=target.name)

            # Use configured damage for automatic attacks
            config = get_config()
            damage = config.game.basic_unarmed_damage

            # Process the attack
            combat_result = await self.process_attack(
                attacker_id=npc.participant_id, target_id=target.participant_id, damage=damage
            )

            if combat_result.success:
                logger.info("NPC automatically attacked", npc_name=npc.name, target_name=target.name, damage=damage)
            else:
                logger.warning("NPC automatic attack failed", npc_name=npc.name, message=combat_result.message)

            # Update NPC's last action tick
            npc.last_action_tick = current_tick

        except Exception as e:
            logger.error("Error processing NPC turn", npc_name=npc.name, error=str(e), exc_info=True)

    async def _process_player_turn(self, combat: CombatInstance, player: CombatParticipant, current_tick: int) -> None:
        """
        Process player turn with automatic basic attack.

        Args:
            combat: Combat instance
            player: Player participant
            current_tick: Current game tick
        """
        try:
            # Validate that we received a proper CombatParticipant object
            if not isinstance(player, CombatParticipant):
                logger.error("Expected CombatParticipant", got_type=type(player), player=player)
                return

            # Debug logging to understand what we're receiving
            logger.debug("_process_player_turn called", player_type=type(player), player=player)
            if hasattr(player, "participant_id"):
                logger.debug(
                    "Player participant_id",
                    participant_id=player.participant_id,
                    participant_id_type=type(player.participant_id),
                )
            else:
                logger.error("Player object missing participant_id attribute", player=player)
                return
            # Find the target (other participant in combat)
            target = None
            for participant in combat.participants.values():
                if participant.participant_id != player.participant_id:
                    target = participant
                    break

            if not target:
                logger.warning("No target found for player", player_name=player.name, combat_id=combat.combat_id)
                return

            # Perform automatic basic attack
            logger.debug("Player performing automatic attack", player_name=player.name, target_name=target.name)

            # Use configured damage for automatic attacks
            config = get_config()
            damage = config.game.basic_unarmed_damage

            # Process the attack
            combat_result = await self.process_attack(
                attacker_id=player.participant_id, target_id=target.participant_id, damage=damage
            )

            if combat_result.success:
                logger.info(
                    "Player automatically attacked", player_name=player.name, target_name=target.name, damage=damage
                )
            else:
                logger.warning("Player automatic attack failed", player_name=player.name, message=combat_result.message)

            # Update player's last action tick
            player.last_action_tick = current_tick

        except Exception as e:
            # Handle case where player might not be a CombatParticipant
            player_type = type(player)
            player_name = getattr(player, "name", f"Unknown Player (type: {player_type})")
            logger.error("Error processing player turn", player_name=player_name, error=str(e))

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

    async def process_attack(
        self, attacker_id: UUID, target_id: UUID, damage: int = 10, is_initial_attack: bool = False
    ) -> CombatResult:
        """
        Process an attack action in combat.

        Args:
            attacker_id: ID of the attacker
            target_id: ID of the target
            damage: Amount of damage to deal

        Returns:
            CombatResult containing the outcome

        Raises:
            ValueError: If attack is invalid (not in combat, wrong turn, etc.)
        """
        combat = await self.get_combat_by_participant(attacker_id)
        if not combat:
            raise ValueError("Attacker is not in combat")

        if combat.status != CombatStatus.ACTIVE:
            raise ValueError("Combat is not active")

        # Check if it's the attacker's turn (skip for initial attack)
        if not is_initial_attack:
            current_participant = combat.get_current_turn_participant()
            if not current_participant or current_participant.participant_id != attacker_id:
                raise ValueError("It is not the attacker's turn")

        # Validate target
        target = combat.participants.get(target_id)
        if not target:
            raise ValueError("Target is not in this combat")

        if not target.is_alive():
            raise ValueError("Target is already dead")

        # Get current participant for logging
        current_participant = combat.participants.get(attacker_id)
        if not current_participant:
            raise ValueError("Attacker not found in combat")

        logger.info("Processing attack", attacker_name=current_participant.name, target_name=target.name, damage=damage)

        # Apply damage with different caps for players vs NPCs
        # Players: cap at -10 (death threshold), NPCs: cap at 0
        old_hp = target.current_hp
        if target.participant_type == CombatParticipantType.PLAYER:
            # Players can go to -10 HP before death
            target.current_hp = max(-10, target.current_hp - damage)
        else:
            # NPCs die at 0 HP
            target.current_hp = max(0, target.current_hp - damage)

        # Check for death states (different for players vs NPCs)
        if target.participant_type == CombatParticipantType.PLAYER:
            # Players die at -10 HP
            target_died = target.current_hp <= -10
            target_mortally_wounded = old_hp > 0 and target.current_hp == 0
        else:
            # NPCs die at 0 HP
            target_died = target.current_hp <= 0
            target_mortally_wounded = False

        # Persist player HP to database if target is a player
        if target.participant_type == CombatParticipantType.PLAYER:
            await self._persist_player_hp(target.participant_id, target.current_hp)

        # Update combat activity
        combat.update_activity(0)  # Will be updated with actual tick in game loop

        # Check if combat should end
        combat_ended = combat.is_combat_over()

        # Create result with health information
        health_info = f" ({target.current_hp}/{target.max_hp} HP)"
        attack_message = f"{current_participant.name} attacks {target.name} for {damage} damage{health_info}"
        result = CombatResult(
            success=True,
            damage=damage,
            target_died=target_died,
            combat_ended=combat_ended,
            message=attack_message,
            combat_id=combat.combat_id,
        )

        # Publish player mortally wounded event if applicable
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
            except Exception as e:
                logger.error("Error publishing player mortally wounded event", error=str(e), exc_info=True)

        # Publish player death event if applicable
        if target_died and target.participant_type == CombatParticipantType.PLAYER:
            try:
                from ..services.combat_messaging_integration import combat_messaging_integration

                await combat_messaging_integration.broadcast_player_death(
                    player_id=str(target.participant_id),
                    player_name=target.name,
                    room_id=combat.room_id,
                    death_location=combat.room_id,
                )
                logger.info("Player death event published", player_id=target.participant_id, player_name=target.name)
            except Exception as e:
                logger.error("Error publishing player death event", error=str(e), exc_info=True)

        # Publish combat events
        try:
            logger.debug(
                "Publishing combat events for attack", attacker_name=current_participant.name, target_name=target.name
            )
            logger.info("About to publish combat events", attacker_type=current_participant.participant_type)
            # Publish attack event based on attacker type
            if current_participant.participant_type == CombatParticipantType.PLAYER:
                logger.info("Creating PlayerAttackedEvent")
                attack_event = PlayerAttackedEvent(
                    event_type="player_attacked",
                    timestamp=datetime.now(),
                    combat_id=combat.combat_id,
                    room_id=combat.room_id,
                    attacker_id=current_participant.participant_id,
                    attacker_name=current_participant.name,
                    target_id=target.participant_id,
                    target_name=target.name,
                    damage=damage,
                    action_type="auto_attack",
                    target_current_hp=target.current_hp,
                    target_max_hp=target.max_hp,
                )
                logger.info("Calling publish_player_attacked", attack_event=attack_event)
                await self._combat_event_publisher.publish_player_attacked(attack_event)
                logger.info("publish_player_attacked completed")
            else:
                logger.info("Creating NPCAttackedEvent")
                attack_event = NPCAttackedEvent(
                    event_type="npc_attacked",
                    timestamp=datetime.now(),
                    combat_id=combat.combat_id,
                    room_id=combat.room_id,
                    attacker_id=current_participant.participant_id,
                    attacker_name=current_participant.name,
                    npc_id=target.participant_id,
                    npc_name=target.name,
                    damage=damage,
                    action_type="auto_attack",
                    target_current_hp=target.current_hp,
                    target_max_hp=target.max_hp,
                )
                logger.info("Calling publish_npc_attacked", attack_event=attack_event)
                await self._combat_event_publisher.publish_npc_attacked(attack_event)
                logger.info("publish_npc_attacked completed")

            # Publish damage event if target is NPC
            if target.participant_type == CombatParticipantType.NPC:
                damage_event = NPCTookDamageEvent(
                    event_type="npc_took_damage",
                    timestamp=datetime.now(),
                    combat_id=combat.combat_id,
                    room_id=combat.room_id,
                    npc_id=target.participant_id,
                    npc_name=target.name,
                    damage=damage,
                    current_hp=target.current_hp,
                    max_hp=target.max_hp,
                )
                await self._combat_event_publisher.publish_npc_took_damage(damage_event)

            # Award XP if target died and attacker is a player
            if target_died:
                result.xp_awarded = await self._calculate_xp_reward(target_id)

            # Publish death event if target died
            if target_died and target.participant_type == CombatParticipantType.NPC:
                logger.info("Creating NPCDiedEvent", target_name=target.name)
                death_event = NPCDiedEvent(
                    event_type="npc_died",
                    timestamp=datetime.now(),
                    combat_id=combat.combat_id,
                    room_id=combat.room_id,
                    npc_id=target.participant_id,
                    npc_name=target.name,
                    xp_reward=result.xp_awarded or 0,
                )
                logger.info("Publishing NPCDiedEvent", death_event=death_event)
                await self._combat_event_publisher.publish_npc_died(death_event)
                logger.info("NPCDiedEvent published successfully")

        except Exception as e:
            logger.error("Error publishing combat events", error=str(e), exc_info=True)

        # Award XP to player if they defeated an NPC
        if target_died:
            if (
                current_participant.participant_type == CombatParticipantType.PLAYER
                and target.participant_type == CombatParticipantType.NPC
                and self._player_combat_service
            ):
                await self._player_combat_service.award_xp_on_npc_death(
                    player_id=current_participant.participant_id, npc_id=target_id, xp_amount=result.xp_awarded
                )

        # End combat if necessary
        if combat_ended:
            await self.end_combat(combat.combat_id, "Combat ended - one participant defeated")
        else:
            # Set up next turn tick for auto-progression
            combat.next_turn_tick = get_current_tick() + combat.turn_interval_ticks
            logger.debug("Combat attack processed, auto-progression enabled", combat_id=combat.combat_id)

        return result

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

        # Update combat status
        combat.status = CombatStatus.ENDED

        # Remove from tracking dictionaries
        for participant_id in combat.participants.keys():
            self._player_combats.pop(participant_id, None)
            self._npc_combats.pop(participant_id, None)

        # Remove from active combats
        self._active_combats.pop(combat_id, None)

        # Clear player combat states if player combat service is available
        if self._player_combat_service:
            await self._player_combat_service.handle_combat_end(combat_id)

        # Publish combat ended event
        try:
            ended_event = CombatEndedEvent(
                event_type="combat_ended",
                timestamp=datetime.now(),
                combat_id=combat_id,
                room_id=combat.room_id,
                reason=reason,
                duration_seconds=int((datetime.now() - combat.start_time).total_seconds())
                if hasattr(combat, "start_time")
                else 0,
                participants={
                    str(p.participant_id): {"name": p.name, "hp": p.current_hp, "max_hp": p.max_hp}
                    for p in combat.participants.values()
                },
            )
            await self._combat_event_publisher.publish_combat_ended(ended_event)
        except Exception as e:
            logger.error("Error publishing combat ended event", error=str(e), exc_info=True)

        logger.info("Combat ended successfully", combat_id=combat_id)

    async def cleanup_stale_combats(self) -> int:
        """
        Clean up combats that have been inactive for too long.

        Returns:
            Number of combats cleaned up
        """
        cutoff_time = datetime.utcnow() - timedelta(minutes=self._combat_timeout_minutes)
        stale_combats = []

        for combat_id, combat in self._active_combats.items():
            if combat.last_activity < cutoff_time:
                stale_combats.append(combat_id)

        for combat_id in stale_combats:
            await self.end_combat(combat_id, "Combat timeout - no activity")
            logger.info("Cleaned up stale combat", combat_id=combat_id)

        return len(stale_combats)

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

    async def _process_automatic_combat_progression(self, combat: CombatInstance) -> None:
        """
        Process automatic combat progression for NPCs.

        This method automatically handles NPC turns in combat, continuing
        the combat loop until it's a player's turn or combat ends.

        Args:
            combat: The combat instance to process
        """
        try:
            # Only process if auto-progression is enabled
            if not combat.auto_progression_enabled:
                return

            # Continue processing turns until it's a player's turn or combat ends
            while combat.status == CombatStatus.ACTIVE:
                current_participant = combat.get_current_turn_participant()
                if not current_participant:
                    logger.warning("No current participant in combat", combat_id=combat.combat_id)
                    # End combat if no valid participant found
                    await self.end_combat(combat.combat_id, "Combat ended - no valid participant")
                    break

                # If it's a player's turn, stop automatic progression
                if current_participant.participant_type == CombatParticipantType.PLAYER:
                    logger.debug(
                        "Combat waiting for player to act",
                        combat_id=combat.combat_id,
                        player_name=current_participant.name,
                    )
                    break

                # If it's an NPC's turn, process their attack automatically
                if current_participant.participant_type == CombatParticipantType.NPC:
                    await self._process_npc_turn(combat, current_participant, 0)  # Will be updated with actual tick

                    # Check if combat ended after NPC turn
                    if combat.is_combat_over():
                        # Only end combat if it hasn't been ended already
                        if combat.combat_id in self._active_combats:
                            await self.end_combat(combat.combat_id, "Combat ended - one participant defeated")
                        break

                    # Advance to next turn
                    combat.advance_turn(get_current_tick())
                    logger.debug("Combat turn advanced", combat_id=combat.combat_id, round=combat.combat_round)

        except Exception as e:
            logger.error("Error in automatic combat progression", combat_id=combat.combat_id, error=str(e))
            # End combat on error to prevent infinite loops
            await self.end_combat(combat.combat_id, f"Combat ended due to error: {str(e)}")

    async def _persist_player_hp(self, player_id: UUID, current_hp: int) -> None:
        """
        Persist player HP to database after taking damage.

        Args:
            player_id: ID of the player whose HP changed
            current_hp: New current HP value
        """
        try:
            if not self._player_combat_service:
                logger.warning("No player combat service available for HP persistence", player_id=player_id)
                return

            # Get persistence layer from player combat service
            persistence = self._player_combat_service._persistence
            if not persistence:
                logger.warning("No persistence layer available for HP persistence", player_id=player_id)
                return

            # Get player from database
            player = persistence.get_player(str(player_id))
            if not player:
                logger.warning("Player not found for HP persistence", player_id=player_id)
                return

            # Update player HP using proper methods
            stats = player.get_stats()
            old_hp = stats.get("current_health", 100)
            stats["current_health"] = current_hp
            player.set_stats(stats)

            # Save player to database
            persistence.save_player(player)

            logger.info(
                "Player HP persisted to database",
                player_id=player_id,
                player_name=player.name,
                old_hp=old_hp,
                new_hp=current_hp,
            )

            # Publish HP update event for real-time UI updates
            await self._publish_player_hp_update_event(player_id, old_hp, current_hp, stats.get("max_health", 100))

        except Exception as e:
            logger.error(
                "Error persisting player HP to database",
                player_id=player_id,
                current_hp=current_hp,
                error=str(e),
                exc_info=True,
            )

    async def _publish_player_hp_update_event(self, player_id: UUID, old_hp: int, new_hp: int, max_hp: int) -> None:
        """
        Publish a PlayerHPUpdated event for real-time UI updates.

        Args:
            player_id: ID of the player whose HP changed
            old_hp: Previous HP value
            new_hp: New HP value
            max_hp: Maximum HP value
        """
        try:
            if not self._player_combat_service or not self._player_combat_service._event_bus:
                logger.warning("No event bus available for HP update event", player_id=player_id)
                return

            from server.events.event_types import PlayerHPUpdated

            # Calculate damage taken (negative for healing)
            damage_taken = old_hp - new_hp

            # Create and publish the event
            hp_update_event = PlayerHPUpdated(
                timestamp=None,  # Will be set by BaseEvent.__post_init__
                event_type="PlayerHPUpdated",  # Will be set by BaseEvent.__post_init__
                player_id=str(player_id),
                old_hp=old_hp,
                new_hp=new_hp,
                max_hp=max_hp,
                damage_taken=damage_taken,
                source_id=None,  # Could be enhanced to track damage source
                combat_id=None,  # Could be enhanced to track combat context
                room_id=None,  # Could be enhanced to track room context
            )

            # Use the NATS service directly to publish the event
            if self._nats_service:
                await self._nats_service.publish_event(hp_update_event)
            else:
                logger.warning("No NATS service available for HP update event", player_id=player_id)

            logger.info(
                "Published PlayerHPUpdated event",
                player_id=player_id,
                old_hp=old_hp,
                new_hp=new_hp,
                damage_taken=damage_taken,
            )

        except Exception as e:
            logger.error(
                "Error publishing PlayerHPUpdated event",
                player_id=player_id,
                old_hp=old_hp,
                new_hp=new_hp,
                error=str(e),
                exc_info=True,
            )

    async def _calculate_xp_reward(self, npc_id: UUID) -> int:
        """
        Calculate XP reward for defeating an NPC.

        Args:
            npc_id: ID of the defeated NPC

        Returns:
            XP reward amount
        """
        logger.info(
            "CombatService._calculate_xp_reward called",
            npc_id=npc_id,
            has_npc_service=bool(self._npc_combat_integration_service),
            has_player_service=bool(self._player_combat_service),
        )

        # Use the PlayerCombatService from NPCCombatIntegrationService if available
        # This ensures we have access to the UUID-to-string ID mapping
        if self._npc_combat_integration_service and self._npc_combat_integration_service._player_combat_service:
            logger.info("Using PlayerCombatService from NPCCombatIntegrationService", npc_id=npc_id)
            return await self._npc_combat_integration_service._player_combat_service.calculate_xp_reward(npc_id)
        elif self._player_combat_service:
            logger.info("Using PlayerCombatService from CombatService", npc_id=npc_id)
            return await self._player_combat_service.calculate_xp_reward(npc_id)
        else:
            # Fallback to default XP value if no player combat service
            logger.info("Using default XP reward", npc_id=npc_id)
            return 0  # Default XP reward changed to 0 to highlight database lookup issues


# Global combat service instance - will be properly initialized by lifespan
_global_combat_service = None


def get_combat_service():
    """Get the global combat service instance."""
    return _global_combat_service


def set_combat_service(service):
    """Set the global combat service instance."""
    global _global_combat_service
    _global_combat_service = service


# For backward compatibility
combat_service = None
