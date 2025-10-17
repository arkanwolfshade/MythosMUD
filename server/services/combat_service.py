"""
Core combat service for managing combat state and logic.

This service handles all combat-related operations including state management,
turn order calculation, and combat resolution.
"""

from datetime import datetime, timedelta
from uuid import UUID

from server.logging_config import get_logger
from server.models.combat import CombatInstance, CombatParticipant, CombatParticipantType, CombatResult, CombatStatus

logger = get_logger(__name__)


class CombatService:
    """
    Service for managing combat instances and state.

    This service maintains in-memory combat state and provides methods
    for initiating combat, processing actions, and managing turn order.
    """

    def __init__(self):
        """Initialize the combat service."""
        self._active_combats: dict[UUID, CombatInstance] = {}
        self._player_combats: dict[UUID, UUID] = {}  # player_id -> combat_id
        self._npc_combats: dict[UUID, UUID] = {}  # npc_id -> combat_id
        self._combat_timeout_minutes = 30  # Configurable timeout

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

        # Create combat instance
        combat = CombatInstance(room_id=room_id)

        # Create participants
        attacker = CombatParticipant(
            participant_id=attacker_id,
            participant_type=CombatParticipantType.PLAYER,
            name=attacker_name,
            current_hp=attacker_hp,
            max_hp=attacker_max_hp,
            dexterity=attacker_dex,
        )

        target = CombatParticipant(
            participant_id=target_id,
            participant_type=CombatParticipantType.NPC,
            name=target_name,
            current_hp=target_hp,
            max_hp=target_max_hp,
            dexterity=target_dex,
        )

        # Add participants to combat
        combat.participants[attacker_id] = attacker
        combat.participants[target_id] = target

        # Calculate turn order based on dexterity (higher dexterity goes first)
        participants_with_dex = [(attacker_id, attacker_dex), (target_id, target_dex)]
        participants_with_dex.sort(key=lambda x: x[1], reverse=True)
        combat.turn_order = [pid for pid, _ in participants_with_dex]

        # Store combat instance
        self._active_combats[combat.combat_id] = combat
        self._player_combats[attacker_id] = combat.combat_id
        self._npc_combats[target_id] = combat.combat_id

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

        # Award XP if target died
        if target_died:
            result.xp_awarded = await self._calculate_xp_reward(target_id)

        # End combat if necessary
        if combat_ended:
            await self.end_combat(combat.combat_id, "Combat ended - one participant defeated")
        else:
            # Advance turn
            combat.advance_turn()
            logger.debug(f"Combat {combat.combat_id} turn advanced to round {combat.combat_round}")

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

    async def _calculate_xp_reward(self, npc_id: UUID) -> int:
        """
        Calculate XP reward for defeating an NPC.

        Args:
            npc_id: ID of the defeated NPC

        Returns:
            XP reward amount
        """
        # For now, return a default XP value
        # In the future, this will query the NPC database for XP value
        return 5  # Default XP reward


# Global combat service instance
combat_service = CombatService()
