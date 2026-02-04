"""
Combat attack processing logic.

Handles attack validation, damage application, and attack event publishing.
"""

from typing import Any
from uuid import UUID

from server.config import get_config
from server.models.combat import CombatInstance, CombatParticipant, CombatParticipantType, CombatStatus
from server.realtime.login_grace_period import is_player_in_login_grace_period
from server.structured_logging.enhanced_logging_config import get_logger

logger = get_logger(__name__)


class CombatAttackHandler:
    """Handles combat attack processing and damage application."""

    def __init__(self, combat_service: Any) -> None:
        """
        Initialize the attack handler.

        Args:
            combat_service: Reference to the parent CombatService
        """
        self._combat_service = combat_service

    def _validate_attack(self, combat: CombatInstance, is_initial_attack: bool) -> None:  # pylint: disable=unused-argument  # Reason: is_initial_attack kept for backward compatibility
        """Validate that attack is allowed."""
        if combat.status != CombatStatus.ACTIVE:
            raise ValueError("Combat is not active")

        # In round-based combat, all participants act each round, so turn validation
        # is not needed. Attacks can happen anytime during a round.
        # Note: is_initial_attack flag is kept for backward compatibility but not used for validation

    def _apply_damage(self, target: CombatParticipant, damage: int) -> tuple[int, bool, bool]:
        """
        Apply damage to target and check death states.

        Delegates domain logic to CombatParticipant.apply_damage; handles
        infrastructure concerns (login grace period) here.

        Returns:
            Tuple of (old_dp, target_died, target_mortally_wounded)
        """
        # Check if target is in login grace period - block damage if so (infrastructure concern)
        if target.participant_type == CombatParticipantType.PLAYER:
            try:
                config = get_config()
                app = getattr(config, "_app_instance", None)
                if app:
                    connection_manager = getattr(app.state, "connection_manager", None)
                    if connection_manager:
                        if is_player_in_login_grace_period(target.participant_id, connection_manager):
                            logger.info(
                                "Damage blocked - target in login grace period",
                                target_id=target.participant_id,
                                target_name=target.name,
                                damage=damage,
                            )
                            # Return original DP, no death, no mortal wound
                            return target.current_dp, False, False
            except (AttributeError, ImportError, TypeError, ValueError, Exception) as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Fail-open behavior requires catching all exceptions
                # If we can't check grace period, proceed with damage (fail open)
                logger.debug(
                    "Could not check login grace period for damage", target_id=target.participant_id, error=str(e)
                )

        # Delegate damage application and death-state logic to domain model
        return target.apply_damage(damage)

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

        self._validate_attack(combat, is_initial_attack)

        target = combat.participants.get(target_id)
        if not target:
            # Fallback: lookup by string comparison in case of UUID representation mismatch
            target_id_str = str(target_id)
            target = next(
                (p for p in combat.participants.values() if str(p.participant_id) == target_id_str),
                None,
            )
        if not target:
            logger.warning(
                "Target not found in combat participants",
                target_id=target_id,
                participant_ids=[str(pid) for pid in combat.participants.keys()],
            )
            raise ValueError("Target is not in this combat")

        if not target.is_alive():
            raise ValueError("Target is already dead")

        current_participant = combat.participants.get(attacker_id)
        if not current_participant:
            raise ValueError("Attacker not found in combat")

        return combat, current_participant, target
