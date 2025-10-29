"""
Combat system models for in-memory state management.

This module defines the data structures used to track combat state
in memory during active combat sessions.
"""

from dataclasses import dataclass, field
from datetime import UTC, datetime
from enum import Enum
from uuid import UUID, uuid4

from server.config import get_config


def _get_default_damage() -> int:
    """Get the default damage value from configuration."""
    try:
        config = get_config()
        return config.game.basic_unarmed_damage
    except Exception:
        # Fallback to hardcoded value if config is not available
        return 10


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
    last_action_tick: int | None = None

    def is_alive(self) -> bool:
        """
        Check if participant is alive enough to be in combat.

        For players: alive if HP > -10 (includes mortally wounded state)
        For NPCs: alive if HP > 0
        """
        if self.participant_type == CombatParticipantType.PLAYER:
            # Players remain "in combat" until -10 HP (mortally wounded at 0 HP is still "alive" for combat purposes)
            return self.current_hp > -10 and self.is_active
        else:
            # NPCs die at 0 HP
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
    start_tick: int = 0
    last_activity_tick: int = 0
    last_activity: datetime = field(default_factory=lambda: datetime.now(UTC))
    combat_round: int = 0
    # Auto-progression features
    auto_progression_enabled: bool = True
    turn_interval_ticks: int = 6
    next_turn_tick: int = 0

    def get_current_turn_participant(self) -> CombatParticipant | None:
        """Get the participant whose turn it is."""
        if not self.turn_order or self.current_turn >= len(self.turn_order):
            return None
        participant_id = self.turn_order[self.current_turn]

        # Try direct lookup first
        participant = self.participants.get(participant_id)
        if participant:
            return participant

        # Fallback: try matching by UUID string value if direct lookup fails
        # This handles cases where UUID objects might be different instances
        target_uuid_str = str(participant_id)
        for pid, p in self.participants.items():
            if str(pid) == target_uuid_str:
                return p

        return None

    def advance_turn(self, current_tick: int) -> None:
        """Advance to the next turn."""
        self.current_turn += 1
        if self.current_turn >= len(self.turn_order):
            self.current_turn = 0
            self.combat_round += 1

        # Update next turn tick for auto-progression
        if self.auto_progression_enabled:
            self.next_turn_tick = current_tick + self.turn_interval_ticks

    def is_combat_over(self) -> bool:
        """Check if combat should end."""
        alive_participants = [p for p in self.participants.values() if p.is_alive()]
        return len(alive_participants) <= 1

    def get_alive_participants(self) -> list[CombatParticipant]:
        """Get all alive participants."""
        return [p for p in self.participants.values() if p.is_alive()]

    def update_activity(self, current_tick: int) -> None:
        """Update the last activity tick and datetime."""
        self.last_activity_tick = current_tick
        self.last_activity = datetime.now(UTC)


@dataclass
class CombatAction:
    """Represents a combat action."""

    action_id: UUID = field(default_factory=uuid4)
    combat_id: UUID = field(default_factory=uuid4)
    attacker_id: UUID = field(default_factory=uuid4)
    target_id: UUID = field(default_factory=uuid4)
    action_type: str = "attack"
    damage: int = field(default_factory=_get_default_damage)
    tick: int = 0
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
