"""
Level service for MythosMUD: grant XP and invoke the level-up hook.

The single XP/level authority for both combat and quest rewards (#879). The registry is the only writer (ADR-029
step 7b): an award is one unit of work on the player, whose level comes from the curve in ``models.player_xp`` (the
same curve as the SQL function ``level_for_xp``, which an integration test checks it against). Used by the character
creation revamp (level/XP) and will be wired to skill improvement on level-up when skill use tracking is implemented.
"""

from __future__ import annotations

import uuid
from collections.abc import Awaitable, Callable
from typing import TYPE_CHECKING

from ..events.event_types import PlayerXPAwardEvent
from ..models.player_xp import awarded
from ..structured_logging.enhanced_logging_config import get_logger
from .player_registry import PlayerNotFoundError

if TYPE_CHECKING:
    from .player_registry import PlayerRegistry

logger = get_logger(__name__)

# Type for level-up hook: (player_id, new_level) -> await None. Stub until skill improvement exists.
LevelUpHook = Callable[[uuid.UUID, int], Awaitable[None]]


class LevelService:  # pylint: disable=too-few-public-methods  # Reason: Focused service, minimal public interface
    """
    Service for character level and XP: grant XP, recompute level from curve, run level-up hook.

    The level-up hook is a stub that will later run skill improvement for skills
    used during the previous level (see character creation revamp plan 4.5).
    """

    def __init__(self, player_registry: PlayerRegistry, level_up_hook: LevelUpHook | None = None) -> None:
        """
        Initialize the level service.

        Args:
            player_registry: The player registry, which owns the XP and level.
            level_up_hook: Optional async hook (player_id, new_level) called on level-up. Stub if None.
        """
        self._registry: PlayerRegistry = player_registry
        self._level_up_hook = level_up_hook
        logger.info("LevelService initialized")

    async def grant_xp(self, player_id: uuid.UUID, amount: int) -> None:
        """
        Grant experience points to a character and check for level-up.

        One registry unit: the XP is added to the player's live total and the level follows the curve (it never
        falls), both committed before this returns, so the award cannot clobber a concurrent change to the player
        (combat damage, a move). The client's XP event is sent after the commit. If the level rose, the level-up hook
        runs (e.g. for skill improvement).

        Args:
            player_id: Character to award XP to.
            amount: Non-negative XP amount.

        Raises:
            ValueError: If amount < 0 or player not found.
        """
        if amount < 0:
            raise ValueError("XP amount must be non-negative")
        if not amount:
            return

        try:
            async with self._registry.mutate(player_id) as player:  # pylint: disable=contextmanager-generator-missing-cleanup  # Reason: @asynccontextmanager always drives this generator to completion; pylint cannot see through the wrapper
                change = awarded(player.row.experience_points, player.row.level, amount)
                player.row.set_experience(change.new_xp, change.new_level, sync=True)
                player.emit(PlayerXPAwardEvent(player_id=player_id, xp_amount=amount, new_level=change.new_level))
        except PlayerNotFoundError as e:
            raise ValueError(f"Player {player_id} not found") from e

        logger.info(
            "Player XP awarded",
            player_id=str(player_id),
            delta=amount,
            new_xp=change.new_xp,
            old_level=change.old_level,
            new_level=change.new_level,
        )
        if change.leveled_up:
            logger.info(
                "Character leveled up",
                player_id=str(player_id),
                old_level=change.old_level,
                new_level=change.new_level,
                total_xp=change.new_xp,
            )
            if self._level_up_hook:
                await self._level_up_hook(player_id, change.new_level)
