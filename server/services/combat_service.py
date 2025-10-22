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
from server.logging_config import get_logger
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

    def __init__(self, player_combat_service: PlayerCombatService = None, nats_service=None):
        """Initialize the combat service."""
        self._active_combats: dict[UUID, CombatInstance] = {}
        self._player_combats: dict[UUID, UUID] = {}  # player_id -> combat_id
        self._npc_combats: dict[UUID, UUID] = {}  # npc_id -> combat_id
        self._combat_timeout_minutes = 30  # Configurable timeout
        self._player_combat_service = player_combat_service
        self._nats_service = nats_service
        # Create combat event publisher with proper NATS service
        logger.debug("Creating CombatEventPublisher with NATS service", nats_service_available=bool(nats_service))
        try:
            print("*** COMBAT SERVICE: About to create CombatEventPublisher ***")
            self._combat_event_publisher = CombatEventPublisher(nats_service)
            print("*** COMBAT SERVICE: CombatEventPublisher created successfully ***")
            logger.debug("CombatEventPublisher created successfully")
        except Exception as e:
            print(f"*** CRITICAL ERROR: Failed to create CombatEventPublisher: {e} ***")
            print(f"*** ERROR TYPE: {type(e).__name__} ***")
            print(f"*** ERROR DETAILS: {str(e)} ***")
            logger.error("CRITICAL ERROR: Failed to create CombatEventPublisher", error=str(e), error_type=type(e).__name__, exc_info=True)
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
        logger.info(f"Starting combat between {attacker_name} and {target_name} in room {room_id}")

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

        logger.info(f"Combat {combat.combat_id} started with turn order: {combat.turn_order}")

        # Publish combat started event
        try:
            logger.debug(f"Creating CombatStartedEvent for combat {combat.combat_id}")
            started_event = CombatStartedEvent(
                event_type="combat_started",
                timestamp=datetime.now(),
                combat_id=combat.combat_id,
                room_id=room_id,
                participants={
                    p.participant_id: {"name": p.name, "hp": p.current_hp, "max_hp": p.max_hp}
                    for p in combat.participants.values()
                },
                turn_order=[str(pid) for pid in combat.turn_order],
            )
            logger.debug(f"Calling publish_combat_started for combat {combat.combat_id}")
            await self._combat_event_publisher.publish_combat_started(started_event)
            logger.debug(f"publish_combat_started completed for combat {combat.combat_id}")
        except Exception as e:
            logger.error(f"Error publishing combat started event: {e}", exc_info=True)

        return combat

    async def process_game_tick(self, current_tick: int) -> None:
        """
        Process game tick for combat auto-progression.

        Args:
            current_tick: Current game tick number
        """
        logger.info(
            f"[COMBAT TICK] process_game_tick called for tick {current_tick}, "
            f"_auto_progression_enabled={self._auto_progression_enabled}, "
            f"active_combats={len(self._active_combats)}"
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
                f"Combat {combat_id}: current_tick={current_tick}, next_turn_tick={combat.next_turn_tick}, auto_progression={combat.auto_progression_enabled}"
            )

            # Check if it's time for the next turn
            if current_tick >= combat.next_turn_tick:
                logger.debug(f"Auto-progression triggered for combat {combat_id} at tick {current_tick}")
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
            logger.warning(f"No current participant for combat {combat.combat_id}")
            logger.debug(
                f"Combat state: turn_order={combat.turn_order}, current_turn={combat.current_turn}, participants={list(combat.participants.keys())}"
            )
            # Check if the participant ID exists in turn_order but not in participants
            if combat.turn_order and combat.current_turn < len(combat.turn_order):
                expected_participant_id = combat.turn_order[combat.current_turn]
                logger.debug(
                    f"Expected participant ID: {expected_participant_id}, exists in participants: {expected_participant_id in combat.participants}"
                )

                # If participant is missing, try to fix the combat state
                if expected_participant_id not in combat.participants:
                    logger.error(
                        f"Participant {expected_participant_id} not found in participants dictionary. Combat state is corrupted."
                    )
                    # Remove the corrupted combat
                    self._active_combats.pop(combat.combat_id, None)
                    return

                # Try to find the participant by matching UUID values
                found_participant = None
                for participant_id, participant in combat.participants.items():
                    if str(participant_id) == str(expected_participant_id):
                        found_participant = participant
                        logger.debug(f"Found participant by UUID string match: {participant}")
                        break

                if found_participant:
                    current_participant = found_participant
                else:
                    logger.error(f"Could not find participant {expected_participant_id} even by UUID string match")
                    return
            else:
                return

        # Debug logging to understand participant type
        participant_id = getattr(current_participant, "participant_id", "NO_PARTICIPANT_ID")
        logger.debug(f"Current participant type: {type(current_participant)}, participant_id: {participant_id}")

        # Additional debugging for the combat state
        logger.debug(
            f"Combat state: turn_order={combat.turn_order}, current_turn={combat.current_turn}, participants={list(combat.participants.keys())}"
        )

        # Debug the specific participant lookup
        if combat.turn_order and combat.current_turn < len(combat.turn_order):
            current_participant_id = combat.turn_order[combat.current_turn]
            logger.debug(
                f"Looking for participant_id: {current_participant_id} in participants: {list(combat.participants.keys())}"
            )
            found_participant = combat.participants.get(current_participant_id)
            logger.debug(f"Participant found: {found_participant}")
            logger.debug(f"current_participant (from get_current_turn_participant): {current_participant}")
            logger.debug(f"Are they the same? {found_participant == current_participant}")

        # If it's an NPC's turn, process their action
        if current_participant.participant_type == CombatParticipantType.NPC:
            await self._process_npc_turn(combat, current_participant, current_tick)
        else:
            # Player's turn - perform automatic basic attack
            # Validate that current_participant is a CombatParticipant
            if not isinstance(current_participant, CombatParticipant):
                logger.error(f"Expected CombatParticipant, got {type(current_participant)}: {current_participant}")
                return
            await self._process_player_turn(combat, current_participant, current_tick)

    async def _process_npc_turn(self, combat: CombatInstance, npc: CombatParticipant, current_tick: int) -> None:
        """
        Process NPC turn with passive behavior.

        Args:
            combat: Combat instance
            npc: NPC participant
            current_tick: Current game tick
        """
        # Select NPC passive action
        action = await self._select_npc_non_combat_action(npc)

        # Format NPC health information
        npc_health = f"{npc.current_hp}/{npc.max_hp} HP"

        # Broadcast the action to the room with health information
        if action:
            await self._broadcast_npc_action(combat.room_id, npc.name, action, npc_health)

        # Update NPC's last action tick
        npc.last_action_tick = current_tick

        logger.debug(f"NPC {npc.name} performed passive action: {action} ({npc_health})")

    async def _select_npc_non_combat_action(self, npc: CombatParticipant) -> str | None:
        """
        Select a non-combat action for an NPC.

        Args:
            npc: NPC participant

        Returns:
            Action description or None
        """
        # Simple passive actions for now
        actions = [
            f"{npc.name} shifts uncomfortably.",
            f"{npc.name} glances around nervously.",
            f"{npc.name} mutters something under their breath.",
            f"{npc.name} adjusts their stance.",
            f"{npc.name} looks at you with concern.",
        ]

        import random

        return random.choice(actions)

    async def _broadcast_npc_action(self, room_id: str, npc_name: str, action: str, npc_health: str = "") -> None:
        """
        Broadcast NPC action to room.

        Args:
            room_id: Room ID
            npc_name: NPC name
            action: Action description
            npc_health: Optional NPC health information (e.g., "49/50 HP")
        """
        try:
            # Create a simple message event for NPC actions
            from server.realtime.connection_manager import connection_manager
            from server.realtime.envelope import build_event

            # Add health information to the message if provided
            message = f"{npc_name} {action}"
            if npc_health:
                message = f"{npc_name} {action} ({npc_health})"

            # Create NPC action event
            npc_action_event = build_event(
                "npc_action",
                {
                    "npc_name": npc_name,
                    "action": action,
                    "message": message,
                    "npc_health": npc_health,
                },
                room_id=room_id,
            )

            # Broadcast to all players in the room
            await connection_manager.broadcast_to_room(room_id, npc_action_event)

            logger.info(
                f"NPC {npc_name} in room {room_id}: {action} ({npc_health if npc_health else 'no health info'})"
            )
        except Exception as e:
            logger.error(f"Failed to broadcast NPC action: {e}")
            # Fallback to just logging
            logger.info(f"NPC {npc_name} in room {room_id}: {action}")

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
                logger.error(f"Expected CombatParticipant, got {type(player)}: {player}")
                return

            # Debug logging to understand what we're receiving
            logger.debug(f"_process_player_turn called with player type: {type(player)}, player: {player}")
            if hasattr(player, "participant_id"):
                logger.debug(f"Player participant_id: {player.participant_id} (type: {type(player.participant_id)})")
            else:
                logger.error(f"Player object missing participant_id attribute: {player}")
                return
            # Find the target (other participant in combat)
            target = None
            for participant in combat.participants.values():
                if participant.participant_id != player.participant_id:
                    target = participant
                    break

            if not target:
                logger.warning(f"No target found for player {player.name} in combat {combat.combat_id}")
                return

            # Perform automatic basic attack
            logger.debug(f"Player {player.name} performing automatic attack on {target.name}")

            # Use configured damage for automatic attacks
            config = get_config()
            damage = config.game.basic_unarmed_damage

            # Process the attack
            combat_result = await self.process_attack(
                attacker_id=player.participant_id, target_id=target.participant_id, damage=damage
            )

            if combat_result.success:
                logger.info(f"Player {player.name} automatically attacked {target.name} for {damage} damage")
            else:
                logger.warning(f"Player {player.name} automatic attack failed: {combat_result.message}")

            # Update player's last action tick
            player.last_action_tick = current_tick

        except Exception as e:
            # Handle case where player might not be a CombatParticipant
            player_type = type(player)
            player_name = getattr(player, "name", f"Unknown Player (type: {player_type})")
            logger.error(f"Error processing player turn for {player_name}: {e}")

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

    async def process_attack(self, attacker_id: UUID, target_id: UUID, damage: int = 10) -> CombatResult:
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

        # Check if it's the attacker's turn
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

        logger.info(f"Processing attack: {current_participant.name} attacks {target.name} for {damage} damage")

        # Apply damage
        target.current_hp = max(0, target.current_hp - damage)
        target_died = target.current_hp <= 0

        # Update combat activity
        combat.update_activity(0)  # Will be updated with actual tick in game loop

        # Check if combat should end
        combat_ended = combat.is_combat_over()

        # Create result with health information
        health_info = f" ({target.current_hp}/{target.max_hp} HP)"
        result = CombatResult(
            success=True,
            damage=damage,
            target_died=target_died,
            combat_ended=combat_ended,
            message=f"{current_participant.name} attacks {target.name} for {damage} damage{health_info}",
            combat_id=combat.combat_id,
        )

        # Publish combat events
        try:
            logger.debug(f"Publishing combat events for attack: {current_participant.name} -> {target.name}")
            logger.info(f"About to publish combat events - attacker type: {current_participant.participant_type}")
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
                )
                logger.info(f"Calling publish_player_attacked with event: {attack_event}")
                await self._combat_event_publisher.publish_player_attacked(attack_event)
                logger.info("publish_player_attacked completed")
            else:
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
                )
                await self._combat_event_publisher.publish_npc_attacked(attack_event)

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

            # Publish death event if target died
            if target_died and target.participant_type == CombatParticipantType.NPC:
                death_event = NPCDiedEvent(
                    event_type="npc_died",
                    timestamp=datetime.now(),
                    combat_id=combat.combat_id,
                    room_id=combat.room_id,
                    npc_id=target.participant_id,
                    npc_name=target.name,
                    xp_reward=result.xp_awarded or 0,
                )
                await self._combat_event_publisher.publish_npc_died(death_event)

        except Exception as e:
            logger.error(f"Error publishing combat events: {e}", exc_info=True)

        # Award XP if target died and attacker is a player
        if target_died:
            result.xp_awarded = await self._calculate_xp_reward(target_id)
            # Award XP to player if they defeated an NPC
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
            logger.debug(f"Combat {combat.combat_id} attack processed, auto-progression enabled")

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
            logger.warning(f"Attempted to end non-existent combat {combat_id}")
            return

        logger.info(f"Ending combat {combat_id}: {reason}")

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
                    p.participant_id: {"name": p.name, "hp": p.current_hp, "max_hp": p.max_hp}
                    for p in combat.participants.values()
                },
            )
            await self._combat_event_publisher.publish_combat_ended(ended_event)
        except Exception as e:
            logger.error(f"Error publishing combat ended event: {e}", exc_info=True)

        logger.info(f"Combat {combat_id} ended successfully")

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
            logger.info(f"Cleaned up stale combat {combat_id}")

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
                    logger.warning(f"No current participant in combat {combat.combat_id}")
                    # End combat if no valid participant found
                    await self.end_combat(combat.combat_id, "Combat ended - no valid participant")
                    break

                # If it's a player's turn, stop automatic progression
                if current_participant.participant_type == CombatParticipantType.PLAYER:
                    logger.debug(f"Combat {combat.combat_id} - waiting for player {current_participant.name} to act")
                    break

                # If it's an NPC's turn, process their attack automatically
                if current_participant.participant_type == CombatParticipantType.NPC:
                    await self._process_npc_turn(combat, current_participant, 0)  # Will be updated with actual tick

                    # Check if combat ended after NPC turn
                    if combat.is_combat_over():
                        await self.end_combat(combat.combat_id, "Combat ended - one participant defeated")
                        break

                    # Advance to next turn
                    combat.advance_turn(get_current_tick())
                    logger.debug(f"Combat {combat.combat_id} turn advanced to round {combat.combat_round}")

        except Exception as e:
            logger.error(f"Error in automatic combat progression for combat {combat.combat_id}: {e}")
            # End combat on error to prevent infinite loops
            await self.end_combat(combat.combat_id, f"Combat ended due to error: {str(e)}")

    async def _calculate_xp_reward(self, npc_id: UUID) -> int:
        """
        Calculate XP reward for defeating an NPC.

        Args:
            npc_id: ID of the defeated NPC

        Returns:
            XP reward amount
        """
        if self._player_combat_service:
            return await self._player_combat_service.calculate_xp_reward(npc_id)
        else:
            # Fallback to default XP value if no player combat service
            return 5  # Default XP reward


# Global combat service instance
combat_service = CombatService()
