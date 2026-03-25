"""
Combat initialization logic.

Handles creation and setup of combat instances.
"""

# pylint: disable=too-few-public-methods,too-many-arguments,too-many-positional-arguments  # Reason: Initialization class has focused responsibility with minimal public interface, and requires many parameters for combat setup

from uuid import UUID

from server.models.combat import CombatInstance, CombatParticipant
from server.services.combat_types import CombatParticipantData
from server.structured_logging.enhanced_logging_config import get_logger

logger = get_logger(__name__)


def _build_combat_instance(
    room_id: str,
    current_tick: int,
    auto_progression_enabled: bool,
    turn_interval_seconds: int,
) -> CombatInstance:
    """Build CombatInstance with turn interval in ticks (1 tick = 0.1s, so seconds * 10)."""
    turn_interval_ticks = turn_interval_seconds * 10
    return CombatInstance(
        room_id=room_id,
        auto_progression_enabled=auto_progression_enabled,
        turn_interval_ticks=turn_interval_ticks,
        start_tick=current_tick,
        last_activity_tick=current_tick,
        next_turn_tick=current_tick + turn_interval_ticks,
    )


def _build_participant(data: CombatParticipantData) -> CombatParticipant:
    """Build CombatParticipant from CombatParticipantData."""
    return CombatParticipant(
        participant_id=data.participant_id,
        participant_type=data.participant_type,
        name=data.name,
        current_dp=data.current_dp,
        max_dp=data.max_dp,
        dexterity=data.dexterity,
        npc_type=data.npc_type,
        aggression_level=data.aggression_level,
    )


def _compute_turn_order(attacker: CombatParticipantData, target: CombatParticipantData) -> list[UUID]:
    """Return participant IDs sorted by dexterity (highest first)."""
    all_participants = [
        (attacker.participant_id, attacker.dexterity),
        (target.participant_id, target.dexterity),
    ]
    all_participants.sort(key=lambda x: x[1], reverse=True)
    return [pid for pid, _ in all_participants]


class CombatInitializer:  # pylint: disable=too-few-public-methods  # Reason: Initialization class with focused responsibility, minimal public interface
    """Handles combat instance initialization and setup."""

    @staticmethod
    def create_combat_instance(  # pylint: disable=too-many-arguments,too-many-positional-arguments  # Reason: Combat instance creation requires many parameters for complete combat setup
        room_id: str,
        attacker: CombatParticipantData,
        target: CombatParticipantData,
        current_tick: int,
        auto_progression_enabled: bool,
        turn_interval_seconds: int,
    ) -> CombatInstance:
        """Create and initialize a combat instance."""
        combat = _build_combat_instance(room_id, current_tick, auto_progression_enabled, turn_interval_seconds)
        combat.participants[attacker.participant_id] = _build_participant(attacker)
        combat.participants[target.participant_id] = _build_participant(target)
        combat.turn_order = _compute_turn_order(attacker, target)
        return combat
