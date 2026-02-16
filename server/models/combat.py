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
from server.structured_logging.enhanced_logging_config import get_logger

logger = get_logger(__name__)


def _get_default_damage() -> int:
    """Get the default damage value from configuration."""
    try:
        config = get_config()
        damage = config.game.basic_unarmed_damage
        if not isinstance(damage, int):
            raise TypeError("basic_unarmed_damage must be an int")
        return damage
    except (ImportError, AttributeError, ValueError) as e:
        logger.error("Error getting basic unarmed damage config", error=str(e), error_type=type(e).__name__)
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
class CombatParticipant:  # pylint: disable=too-many-instance-attributes  # Reason: Combat participant requires many fields to capture complete combat state
    """Represents a participant in combat."""

    participant_id: UUID
    participant_type: CombatParticipantType
    name: str
    current_dp: int  # Current determination points (DP)
    max_dp: int  # Maximum determination points (DP)
    dexterity: int
    is_active: bool = True
    last_action_tick: int | None = None

    def is_alive(self) -> bool:
        """
        Check if participant is alive enough to be in combat.

        For players: alive if DP > -10 (includes mortally wounded state)
        For NPCs: alive if DP > 0
        """
        if self.participant_type == CombatParticipantType.PLAYER:
            # Players remain "in combat" until -10 DP (mortally wounded at 0 DP is still "alive" for combat purposes)
            return self.current_dp > -10 and self.is_active
        # NPCs die at 0 DP
        return self.current_dp > 0 and self.is_active

    def is_dead(self) -> bool:
        """
        Check if participant is dead.

        For players: dead if DP <= -10
        For NPCs: dead if DP <= 0
        """
        if self.participant_type == CombatParticipantType.PLAYER:
            return self.current_dp <= -10
        return self.current_dp <= 0

    def is_mortally_wounded(self) -> bool:
        """
        Check if participant is mortally wounded (players only).

        For players: mortally wounded if 0 >= DP > -10
        For NPCs: always False (NPCs die at 0, no mortal wound state)
        """
        if self.participant_type != CombatParticipantType.PLAYER:
            return False
        return 0 >= self.current_dp > -10

    def can_act_in_combat(self) -> bool:
        """
        Check if participant can perform voluntary combat actions.

        Unconscious (DP <= 0) or dead participants cannot act. For both players
        and NPCs, requires current_dp > 0 and is_active.
        """
        return self.current_dp > 0 and self.is_active

    def apply_damage(self, damage: int) -> tuple[int, bool, bool]:
        """
        Apply damage to this participant and determine resulting death states.

        Encapsulates damage application rules: players cap at -10 DP and have
        a mortally wounded band (0 >= DP > -10); NPCs cap at 0 DP and die there.

        Args:
            damage: Amount of damage to apply

        Returns:
            Tuple of (old_dp, target_died, target_mortally_wounded)
            - target_mortally_wounded: True if this hit crossed from positive DP to 0 (players only)
        """
        old_dp = self.current_dp
        if self.participant_type == CombatParticipantType.PLAYER:
            self.current_dp = max(-10, self.current_dp - damage)
            target_died = self.is_dead()
            target_mortally_wounded = old_dp > 0 and not self.current_dp
        else:
            self.current_dp = max(0, self.current_dp - damage)
            target_died = self.is_dead()
            target_mortally_wounded = False
        return old_dp, target_died, target_mortally_wounded


@dataclass
class CombatInstance:  # pylint: disable=too-many-instance-attributes  # Reason: Combat instance requires many fields to capture complete combat state
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
    turn_interval_ticks: int = 100  # 100 ticks = 10 seconds (round interval)
    next_turn_tick: int = 0
    # Action queuing for round-based combat
    queued_actions: dict[UUID, list["CombatAction"]] = field(default_factory=dict)  # Actions queued per participant
    round_actions: dict[UUID, "CombatAction"] = field(default_factory=dict)  # Actions for current round

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
        """
        Advance to the next round - all participants act each round.

        In round-based combat, this increments the combat_round counter.
        All participants act in each round in initiative order (handled by CombatTurnProcessor).
        """
        # Increment combat round (all participants act each round)
        self.combat_round += 1
        # Reset current_turn (may be repurposed for other timing needs)
        self.current_turn = 0

        # Update next turn tick for auto-progression (next round starts in turn_interval_ticks)
        if self.auto_progression_enabled:
            self.next_turn_tick = current_tick + self.turn_interval_ticks

    def is_combat_over(self) -> bool:
        """
        Check if combat should end.

        CRITICAL: Combat should NOT end when a player is mortally wounded (0 DP) but not dead (-10 DP).
        Players at 0 DP are still attackable and should remain in combat until -10 DP.
        """
        # Count participants that are actually dead (not just incapacitated)
        # For players: dead if DP <= -10
        # For NPCs: dead if DP <= 0
        dead_participants = [
            p
            for p in self.participants.values()
            if p.is_dead()  # Use is_dead() instead of is_alive() to check actual death, not incapacitation
        ]
        alive_count = len(self.participants) - len(dead_participants)
        # Combat ends only when <= 1 participant is not dead
        # This allows NPCs to continue attacking mortally wounded players (0 DP) until -10 DP
        return alive_count <= 1

    def get_alive_participants(self) -> list[CombatParticipant]:
        """
        Get all participants that are not dead (includes mortally wounded players at 0 DP).

        CRITICAL: This includes players at 0 DP (mortally wounded) who are still attackable
        until they reach -10 DP. Uses is_dead() instead of is_alive() to ensure mortally
        wounded players remain in combat.
        """
        return [p for p in self.participants.values() if not p.is_dead()]

    def update_activity(self, current_tick: int) -> None:
        """Update the last activity tick and datetime."""
        self.last_activity_tick = current_tick
        self.last_activity = datetime.now(UTC)

    def queue_action(self, participant_id: UUID, action: "CombatAction") -> None:
        """
        Queue an action for a participant to execute in the next round.

        Args:
            participant_id: ID of the participant queuing the action
            action: The combat action to queue
        """
        if participant_id not in self.queued_actions:
            self.queued_actions[participant_id] = []
        action.queued = True
        action.round = self.combat_round + 1  # Execute in next round
        self.queued_actions[participant_id].append(action)
        logger.debug(
            "Action queued",
            combat_id=self.combat_id,
            participant_id=participant_id,
            action_type=action.action_type,
            round=action.round,
        )

    def get_queued_actions(self, participant_id: UUID) -> list["CombatAction"]:
        """
        Get queued actions for a participant.

        Args:
            participant_id: ID of the participant

        Returns:
            List of queued actions for this participant
        """
        return self.queued_actions.get(participant_id, [])

    def clear_queued_actions(self, participant_id: UUID, round_number: int | None = None) -> None:
        """
        Clear queued actions for a participant after execution.

        Args:
            participant_id: ID of the participant
            round_number: Optional round number to clear specific action, or None to clear all
        """
        if participant_id not in self.queued_actions:
            return

        if round_number is None:
            # Clear all queued actions for this participant
            del self.queued_actions[participant_id]
        else:
            # Clear only the action for the specified round
            actions = self.queued_actions[participant_id]
            self.queued_actions[participant_id] = [a for a in actions if a.round != round_number]
            # Clean up empty lists
            if not self.queued_actions[participant_id]:
                del self.queued_actions[participant_id]

    def get_participants_by_initiative(self) -> list[CombatParticipant]:
        """
        Get all alive participants sorted by dexterity (highest first) for initiative order.

        Returns:
            List of participants sorted by dexterity descending
        """
        alive = self.get_alive_participants()
        return sorted(alive, key=lambda p: p.dexterity, reverse=True)


@dataclass
class CombatAction:  # pylint: disable=too-many-instance-attributes  # Reason: Combat action requires many fields to capture complete action state
    """Represents a combat action."""

    action_id: UUID = field(default_factory=uuid4)
    combat_id: UUID = field(default_factory=uuid4)
    attacker_id: UUID = field(default_factory=uuid4)
    target_id: UUID = field(default_factory=uuid4)
    action_type: str = "attack"
    damage: int = field(default_factory=_get_default_damage)
    tick: int = 0
    round: int = 0  # Round number when action executes (for queued actions)
    success: bool = True
    message: str = ""
    # Additional fields for queued actions
    queued: bool = False  # Whether this action was queued
    spell_id: str | None = None  # For spell actions
    spell_name: str | None = None  # For spell actions


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
