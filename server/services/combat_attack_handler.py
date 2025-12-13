"""
Combat attack processing logic.

Handles attack validation, damage application, and attack event publishing.
"""

from uuid import UUID

from server.logging.enhanced_logging_config import get_logger
from server.models.combat import CombatInstance, CombatParticipant, CombatParticipantType, CombatStatus

logger = get_logger(__name__)


class CombatAttackHandler:
    """Handles combat attack processing and damage application."""

    def __init__(self, combat_service):
        """
        Initialize the attack handler.

        Args:
            combat_service: Reference to the parent CombatService
        """
        self._combat_service = combat_service

    def _validate_attack(self, combat: CombatInstance, attacker_id: UUID, is_initial_attack: bool) -> None:
        """Validate that attack is allowed."""
        if combat.status != CombatStatus.ACTIVE:
            raise ValueError("Combat is not active")

        if not is_initial_attack:
            current_participant = combat.get_current_turn_participant()
            if not current_participant or current_participant.participant_id != attacker_id:
                raise ValueError("It is not the attacker's turn")

    def _apply_damage(self, target: CombatParticipant, damage: int) -> tuple[int, bool, bool]:
        """
        Apply damage to target and check death states.

        Returns:
            Tuple of (old_dp, target_died, target_mortally_wounded)
        """
        old_dp = target.current_dp
        if target.participant_type == CombatParticipantType.PLAYER:
            target.current_dp = max(-10, target.current_dp - damage)
            target_died = target.current_dp <= -10
            target_mortally_wounded = old_dp > 0 and target.current_dp == 0
        else:
            target.current_dp = max(0, target.current_dp - damage)
            target_died = target.current_dp <= 0
            target_mortally_wounded = False
        return old_dp, target_died, target_mortally_wounded

    async def apply_attack_damage(
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
        old_dp, target_died, target_mortally_wounded = self._apply_damage(target, damage)

        combat.update_activity(0)
        return old_dp, target_died, target_mortally_wounded

    async def validate_and_get_combat_participants(
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
        combat = await self._combat_service.get_combat_by_participant(attacker_id)
        if not combat:
            raise ValueError("Attacker is not in combat")

        self._validate_attack(combat, attacker_id, is_initial_attack)

        target = combat.participants.get(target_id)
        if not target:
            raise ValueError("Target is not in this combat")

        if not target.is_alive():
            raise ValueError("Target is already dead")

        current_participant = combat.participants.get(attacker_id)
        if not current_participant:
            raise ValueError("Attacker not found in combat")

        return combat, current_participant, target
