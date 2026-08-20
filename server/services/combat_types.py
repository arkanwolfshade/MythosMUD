"""
Combat-related type definitions.

This module contains data classes and types used across combat services
to avoid circular import issues.
"""

from dataclasses import dataclass
from uuid import UUID

from server.models.combat import CombatParticipantType


@dataclass
class CombatParticipantData:
    """Data for a combat participant."""

    participant_id: UUID
    name: str
    current_dp: int  # Current determination points (DP)
    max_dp: int  # Maximum determination points (DP)
    dexterity: int
    participant_type: CombatParticipantType = CombatParticipantType.PLAYER
    # ADR-016 + behavior_config: per-NPC aggro; only set for NPCs
    npc_type: str | None = None
    aggression_level: int | None = None  # 0-10; None = full threat
    is_non_damaging: bool = False  # #625: only set for PHANTOM participants
    phantom_id: str | None = None  # #625: PhantomHostileService's own id, not the synthetic UUID above
