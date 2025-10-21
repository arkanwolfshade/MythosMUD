"""
Combat system models for in-memory state management.

This module defines the data structures used to track combat state
in memory during active combat sessions.
"""

from dataclasses import dataclass, field
from datetime import datetime, timedelta
from enum import Enum
from uuid import UUID, uuid4


class CombatStatus(Enum):
    """Status of a combat instance."""

    ACTIVE = "active"
    ENDED = "ended"
    TIMEOUT = "timeout"


class CombatParticipantType(Enum):
    """Type of combat participant."""

    PLAYER = "player"
    NPC = "npc"


@dataclass
class CombatParticipant:
    """Represents a participant in combat."""

    participant_id: UUID
    participant_type: CombatParticipantType
    name: str
    current_hp: int
    max_hp: int
    dexterity: int
    is_active: bool = True
    last_action_time: datetime | None = None

    def is_alive(self) -> bool:
        """Check if participant is alive."""
        return self.current_hp > 0 and self.is_active


@dataclass
class CombatInstance:
    """Represents an active combat instance."""

    combat_id: UUID = field(default_factory=uuid4)
    room_id: str = ""
    participants: dict[UUID, CombatParticipant] = field(default_factory=dict)
    turn_order: list[UUID] = field(default_factory=list)
    current_turn: int = 0
    status: CombatStatus = CombatStatus.ACTIVE
    start_time: datetime = field(default_factory=datetime.utcnow)
    last_activity: datetime = field(default_factory=datetime.utcnow)
    combat_round: int = 0
    # Auto-progression features
    auto_progression_enabled: bool = True
    turn_interval_seconds: int = 6
    next_turn_time: datetime = field(default_factory=lambda: datetime.utcnow() + timedelta(seconds=6))

    def get_current_turn_participant(self) -> CombatParticipant | None:
        """Get the participant whose turn it is."""
        if not self.turn_order or self.current_turn >= len(self.turn_order):
            return None
        participant_id = self.turn_order[self.current_turn]
        return self.participants.get(participant_id)

    def advance_turn(self) -> None:
        """Advance to the next turn."""
        self.current_turn += 1
        if self.current_turn >= len(self.turn_order):
            self.current_turn = 0
            self.combat_round += 1

        # Update next turn time for auto-progression
        if self.auto_progression_enabled:
            self.next_turn_time = datetime.utcnow() + timedelta(seconds=self.turn_interval_seconds)

    def is_combat_over(self) -> bool:
        """Check if combat should end."""
        alive_participants = [p for p in self.participants.values() if p.is_alive()]
        return len(alive_participants) <= 1

    def get_alive_participants(self) -> list[CombatParticipant]:
        """Get all alive participants."""
        return [p for p in self.participants.values() if p.is_alive()]

    def update_activity(self) -> None:
        """Update the last activity timestamp."""
        self.last_activity = datetime.utcnow()


@dataclass
class CombatAction:
    """Represents a combat action."""

    action_id: UUID = field(default_factory=uuid4)
    combat_id: UUID = field(default_factory=uuid4)
    attacker_id: UUID = field(default_factory=uuid4)
    target_id: UUID = field(default_factory=uuid4)
    action_type: str = "attack"
    damage: int = 1
    timestamp: datetime = field(default_factory=datetime.utcnow)
    success: bool = True
    message: str = ""


@dataclass
class CombatResult:
    """Result of a combat action."""

    success: bool
    damage: int
    target_died: bool
    combat_ended: bool
    message: str
    xp_awarded: int = 0
    combat_id: UUID | None = None
