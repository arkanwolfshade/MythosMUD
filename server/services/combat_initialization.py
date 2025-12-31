"""
Combat initialization logic.

Handles creation and setup of combat instances.
"""

from server.models.combat import CombatInstance, CombatParticipant
from server.services.combat_types import CombatParticipantData
from server.structured_logging.enhanced_logging_config import get_logger

logger = get_logger(__name__)


class CombatInitializer:
    """Handles combat instance initialization and setup."""

    @staticmethod
    def create_combat_instance(
        room_id: str,
        attacker: CombatParticipantData,
        target: CombatParticipantData,
        current_tick: int,
        auto_progression_enabled: bool,
        turn_interval_seconds: int,
    ) -> CombatInstance:
        """
        Create and initialize a combat instance.

        Args:
            room_id: The room where combat is taking place
            attacker: Data for the attacking participant
            target: Data for the target participant
            current_tick: Current game tick
            auto_progression_enabled: Whether auto-progression is enabled
            turn_interval_seconds: Turn interval in seconds

        Returns:
            The initialized CombatInstance
        """
        # Create combat instance with auto-progression configuration
        combat = CombatInstance(
            room_id=room_id,
            auto_progression_enabled=auto_progression_enabled,
            turn_interval_ticks=turn_interval_seconds,  # Convert seconds to ticks (1:1 for now)
            start_tick=current_tick,
            last_activity_tick=current_tick,
            next_turn_tick=current_tick + turn_interval_seconds,
        )

        # Create participant objects
        attacker_participant = CombatParticipant(
            participant_id=attacker.participant_id,
            participant_type=attacker.participant_type,
            name=attacker.name,
            current_dp=attacker.current_dp,
            max_dp=attacker.max_dp,
            dexterity=attacker.dexterity,
        )

        target_participant = CombatParticipant(
            participant_id=target.participant_id,
            participant_type=target.participant_type,
            name=target.name,
            current_dp=target.current_dp,
            max_dp=target.max_dp,
            dexterity=target.dexterity,
        )

        # Add participants to combat
        combat.participants[attacker.participant_id] = attacker_participant
        combat.participants[target.participant_id] = target_participant

        # Calculate turn order: all participants sorted by dexterity (highest first)
        all_participants = [(attacker.participant_id, attacker.dexterity), (target.participant_id, target.dexterity)]
        all_participants.sort(key=lambda x: x[1], reverse=True)

        # Build turn order: highest dexterity first
        combat.turn_order = [pid for pid, _ in all_participants]

        return combat
