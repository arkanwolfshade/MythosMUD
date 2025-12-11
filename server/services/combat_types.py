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
