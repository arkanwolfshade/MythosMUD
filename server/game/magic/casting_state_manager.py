"""
Casting state manager for tracking active spell castings.

This module manages the state of ongoing spell castings, tracking casting time,
combat integration, and interruption handling.
"""

import uuid
from dataclasses import dataclass
from typing import Any

from server.logging.enhanced_logging_config import get_logger

logger = get_logger(__name__)


@dataclass
class CastingState:
    """Represents an active spell casting state."""

    player_id: uuid.UUID
    spell_id: str
    spell_name: str
    start_tick: int
    casting_time_seconds: int
    remaining_seconds: float
    combat_id: uuid.UUID | None
    next_initiative_tick: int | None
    mp_cost: int
    target_name: str | None
    target_id: str | None
    target_type: str | None
    mastery: int
    spell: Any  # Spell object


class CastingStateManager:
    """
    Manages casting state for all active spell castings.

    Tracks which players are currently casting spells, their progress,
    and handles state transitions.
    """

    def __init__(self) -> None:
        """Initialize the casting state manager."""
        self._casting_states: dict[uuid.UUID, CastingState] = {}
        logger.info("CastingStateManager initialized")

    def start_casting(
        self,
        player_id: uuid.UUID,
        spell: Any,
        start_tick: int,
        combat_id: uuid.UUID | None = None,
        next_initiative_tick: int | None = None,
        target_name: str | None = None,
        target_id: str | None = None,
        target_type: str | None = None,
        mastery: int = 0,
    ) -> CastingState:
        """
        Start a new casting state.

        Args:
            player_id: ID of the player casting
            spell: Spell object being cast
            start_tick: Current game tick when casting starts
            combat_id: Optional combat ID if in combat
            next_initiative_tick: Optional next initiative tick if waiting for turn
            target_name: Optional target name
            target_id: Optional target ID
            target_type: Optional target type
            mastery: Mastery level for the spell

        Returns:
            CastingState: The created casting state

        Raises:
            ValueError: If player is already casting
        """
        if player_id in self._casting_states:
            raise ValueError(f"Player {player_id} is already casting a spell")

        casting_state = CastingState(
            player_id=player_id,
            spell_id=spell.spell_id,
            spell_name=spell.name,
            start_tick=start_tick,
            casting_time_seconds=spell.casting_time_seconds,
            remaining_seconds=spell.casting_time_seconds,
            combat_id=combat_id,
            next_initiative_tick=next_initiative_tick,
            mp_cost=spell.mp_cost,
            target_name=target_name,
            target_id=target_id,
            target_type=target_type,
            mastery=mastery,
            spell=spell,
        )

        self._casting_states[player_id] = casting_state
        logger.info(
            "Started casting",
            player_id=player_id,
            spell_id=spell.spell_id,
            casting_time=spell.casting_time_seconds,
            combat_id=combat_id,
        )

        return casting_state

    def is_casting(self, player_id: uuid.UUID) -> bool:
        """
        Check if a player is currently casting.

        Args:
            player_id: Player ID to check

        Returns:
            bool: True if player is casting, False otherwise
        """
        return player_id in self._casting_states

    def get_casting_state(self, player_id: uuid.UUID) -> CastingState | None:
        """
        Get the casting state for a player.

        Args:
            player_id: Player ID

        Returns:
            CastingState | None: The casting state if found, None otherwise
        """
        return self._casting_states.get(player_id)

    def complete_casting(self, player_id: uuid.UUID) -> CastingState | None:
        """
        Complete and remove a casting state.

        Args:
            player_id: Player ID

        Returns:
            CastingState | None: The completed casting state if found, None otherwise
        """
        casting_state = self._casting_states.pop(player_id, None)
        if casting_state:
            logger.info("Completed casting", player_id=player_id, spell_id=casting_state.spell_id)
        return casting_state

    def interrupt_casting(self, player_id: uuid.UUID) -> CastingState | None:
        """
        Interrupt and remove a casting state.

        Args:
            player_id: Player ID

        Returns:
            CastingState | None: The interrupted casting state if found, None otherwise
        """
        casting_state = self._casting_states.pop(player_id, None)
        if casting_state:
            logger.info("Interrupted casting", player_id=player_id, spell_id=casting_state.spell_id)
        return casting_state

    def update_casting_progress(self, player_id: uuid.UUID, current_tick: int) -> bool:
        """
        Update casting progress for a player.

        Args:
            player_id: Player ID
            current_tick: Current game tick

        Returns:
            bool: True if casting is complete, False otherwise
        """
        casting_state = self._casting_states.get(player_id)
        if not casting_state:
            return False

        # If waiting for initiative, don't progress yet
        if casting_state.next_initiative_tick is not None:
            if current_tick < casting_state.next_initiative_tick:
                return False
            # Initiative has arrived, start/continue casting
            casting_state.next_initiative_tick = None
            casting_state.start_tick = current_tick

        # Calculate elapsed time
        # Convert tick difference to seconds (tick rate is 0.1s per tick)
        elapsed_ticks = current_tick - casting_state.start_tick
        elapsed_seconds = elapsed_ticks * 0.1
        casting_state.remaining_seconds = max(0, casting_state.casting_time_seconds - elapsed_seconds)

        # Check if complete
        if casting_state.remaining_seconds <= 0:
            return True

        return False

    def get_all_casting_players(self) -> list[uuid.UUID]:
        """
        Get all players currently casting.

        Returns:
            list[uuid.UUID]: List of player IDs who are casting
        """
        return list(self._casting_states.keys())

    def clear_all(self) -> None:
        """Clear all casting states (for testing/reset)."""
        self._casting_states.clear()
        logger.info("Cleared all casting states")
