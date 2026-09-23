"""
Level service for MythosMUD: grant XP and invoke the level-up hook.

The single XP/level authority for both combat and quest rewards (#879) -- level is
always derived from the SQL-side curve (award_player_xp / level_for_xp), never
computed in Python. Used by the character creation revamp (level/XP) and will be
wired to skill improvement on level-up when skill use tracking is implemented.
"""

import uuid
from collections.abc import Awaitable, Callable
from typing import Any, Protocol, cast

from ..structured_logging.enhanced_logging_config import get_logger

logger = get_logger(__name__)

# Type for level-up hook: (player_id, new_level) -> await None. Stub until skill improvement exists.
LevelUpHook = Callable[[uuid.UUID, int], Awaitable[None]]


class _XpAwardingPersistence(Protocol):
    """Persistence surface LevelService actually calls (narrows the Any-typed constructor arg)."""

    async def award_player_xp(self, player_id: uuid.UUID, amount: int, source: str = "unknown") -> tuple[int, int, int]:
        """Atomically add XP and recompute level. Returns (new_xp, old_level, new_level)."""
        raise NotImplementedError


class LevelService:
    """
    Service for character level and XP: grant XP, recompute level from curve, run level-up hook.

    The level-up hook is a stub that will later run skill improvement for skills
    used during the previous level (see character creation revamp plan 4.5).
    """

    def __init__(
        self,
        async_persistence: Any,
        level_up_hook: LevelUpHook | None = None,
    ) -> None:
        """
        Initialize the level service.

        Args:
            async_persistence: Async persistence for loading/saving players.
            level_up_hook: Optional async hook (player_id, new_level) called on level-up. Stub if None.
        """
        self._persistence = async_persistence
        self._level_up_hook = level_up_hook
        logger.info("LevelService initialized")

    async def grant_xp(self, player_id: uuid.UUID, amount: int) -> None:
        """
        Grant experience points to a character and check for level-up.

        Delegates to persistence.award_player_xp, which atomically adds the XP and
        recomputes level from the SQL-side curve (level_for_xp) in a single row-locked
        update -- no read-modify-write of the player row, so this can't clobber
        concurrent stat changes (e.g. combat damage). If level increased, invokes the
        level-up hook (e.g. for skill improvement).

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

        persistence = cast(_XpAwardingPersistence, self._persistence)
        _new_xp, old_level, new_level = await persistence.award_player_xp(player_id, amount, "grant_xp")

        if new_level > old_level:
            logger.info(
                "Character leveled up",
                player_id=str(player_id),
                old_level=old_level,
                new_level=new_level,
                total_xp=_new_xp,
            )
            if self._level_up_hook:
                await self._level_up_hook(player_id, new_level)
