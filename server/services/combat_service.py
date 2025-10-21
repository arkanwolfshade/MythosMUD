"""
Core combat service for managing combat state and logic.

This service handles all combat-related operations including state management,
turn order calculation, and combat resolution.
"""

from datetime import datetime, timedelta
from uuid import UUID

from server.logging_config import get_logger
from server.models.combat import (
    CombatInstance,
    CombatParticipant,
    CombatParticipantType,
    CombatResult,
    CombatStatus,
)
from server.services.player_combat_service import PlayerCombatService

logger = get_logger(__name__)


class CombatService:
    """
    Service for managing combat instances and state.

    This service maintains in-memory combat state and provides methods
    for initiating combat, processing actions, and managing turn order.
    """

    def __init__(self, player_combat_service: PlayerCombatService = None):
        """Initialize the combat service."""
        self._active_combats: dict[UUID, CombatInstance] = {}
        self._player_combats: dict[UUID, UUID] = {}  # player_id -> combat_id
        self._npc_combats: dict[UUID, UUID] = {}  # npc_id -> combat_id
        self._combat_timeout_minutes = 30  # Configurable timeout
        self._player_combat_service = player_combat_service
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
            turn_interval_seconds=self._turn_interval_seconds,
            next_turn_time=datetime.utcnow() + timedelta(seconds=self._turn_interval_seconds),
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

        return combat

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

    async def process_attack(self, attacker_id: UUID, target_id: UUID, damage: int = 1) -> CombatResult:
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

        logger.info(f"Processing attack: {current_participant.name} attacks {target.name} for {damage} damage")

        # Apply damage
        target.current_hp = max(0, target.current_hp - damage)
        target_died = target.current_hp <= 0

        # Update combat activity
        combat.update_activity()

        # Check if combat should end
        combat_ended = combat.is_combat_over()

        # Create result
        result = CombatResult(
            success=True,
            damage=damage,
            target_died=target_died,
            combat_ended=combat_ended,
            message=f"{current_participant.name} attacks {target.name} for {damage} damage",
            combat_id=combat.combat_id,
        )

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
            # Advance turn
            combat.advance_turn()
            logger.debug(f"Combat {combat.combat_id} turn advanced to round {combat.combat_round}")

            # Automatically process next participant's turn if it's an NPC
            await self._process_automatic_combat_progression(combat)

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

    async def _advance_turn_automatically(self, combat: CombatInstance) -> None:
        """
        Advance turn automatically for auto-progression system.

        Args:
            combat: The combat instance to advance
        """
        combat.advance_turn()
        logger.debug(f"Combat {combat.combat_id} turn advanced to round {combat.combat_round}")

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
                    await self._process_npc_turn(combat, current_participant)

                    # Check if combat ended after NPC turn
                    if combat.is_combat_over():
                        await self.end_combat(combat.combat_id, "Combat ended - one participant defeated")
                        break

                    # Advance to next turn
                    combat.advance_turn()
                    logger.debug(f"Combat {combat.combat_id} turn advanced to round {combat.combat_round}")

        except Exception as e:
            logger.error(f"Error in automatic combat progression for combat {combat.combat_id}: {e}")
            # End combat on error to prevent infinite loops
            await self.end_combat(combat.combat_id, f"Combat ended due to error: {str(e)}")

    async def _process_npc_turn(self, combat: CombatInstance, npc_participant: CombatParticipant) -> None:
        """
        Process an NPC's turn in combat with passive behavior (non-combat actions).

        Args:
            combat: The combat instance
            npc_participant: The NPC participant whose turn it is
        """
        try:
            # Find a valid target for the NPC (preferably a player)
            target = None
            for participant in combat.participants.values():
                if (
                    participant.participant_type == CombatParticipantType.PLAYER
                    and participant.is_alive()
                    and participant.participant_id != npc_participant.participant_id
                ):
                    target = participant
                    break

            if not target:
                logger.warning(f"No valid target found for NPC {npc_participant.name} in combat {combat.combat_id}")
                return

            # NPC performs non-combat action (passive behavior for MVP)
            action_message = await self._select_npc_non_combat_action(npc_participant, target)
            logger.info(f"NPC {npc_participant.name} performs non-combat action: {action_message}")

            # Update combat activity
            combat.update_activity()

        except Exception as e:
            logger.error(f"Error processing NPC turn for {npc_participant.name}: {e}")

    async def _select_npc_non_combat_action(self, npc_participant: CombatParticipant, target: CombatParticipant) -> str:
        """
        Select a non-combat action for the NPC to perform.

        Args:
            npc_participant: The NPC performing the action
            target: The target participant

        Returns:
            Action message describing what the NPC did
        """
        import random

        # Non-combat actions for debugging and thematic behavior
        actions = [
            f"{npc_participant.name} takes a defensive stance, watching {target.name} carefully.",
            f"{npc_participant.name} mutters something in an unknown language, "
            f"eyes gleaming with otherworldly intelligence.",
            f"{npc_participant.name} shifts position, creating an eerie silhouette against the shadows.",
            f"{npc_participant.name} seems to be studying {target.name} with unnerving intensity.",
            f"{npc_participant.name} makes a gesture that sends chills down your spine.",
            f"{npc_participant.name} appears to be gathering some form of energy around them.",
            f"{npc_participant.name} whispers words that seem to echo from beyond the veil of reality.",
            f"{npc_participant.name} moves with an unnatural grace, their form seeming to shift at the edges.",
            f"{npc_participant.name} fixes {target.name} with a gaze that speaks of ancient knowledge.",
            f"{npc_participant.name} gestures menacingly, though no immediate threat manifests.",
        ]

        return random.choice(actions)

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
