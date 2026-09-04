"""
Level service for MythosMUD: grant XP, check level-up, and invoke level-up hook.

Used by the character creation revamp (level/XP) and will be wired to skill
improvement on level-up when skill use tracking is implemented.
"""

import uuid
from collections.abc import Awaitable, Callable
from typing import Any

from ..structured_logging.enhanced_logging_config import get_logger
from .level_curve import level_from_total_xp

logger = get_logger(__name__)

# Type for level-up hook: (player_id, new_level) -> await None. Stub until skill improvement exists.
LevelUpHook = Callable[[uuid.UUID, int], Awaitable[None]]


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

        Adds amount to the character's experience_points, recomputes level from
        the XP curve, and if level increased persists the new level and invokes
        the level-up hook (e.g. for skill improvement).

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

        player = await self._persistence.get_player_by_id(player_id)
        if not player:
            raise ValueError(f"Player {player_id} not found")

        player.experience_points += amount
        new_level = level_from_total_xp(player.experience_points)

        if new_level > player.level:
            old_level = player.level
            player.level = new_level
            await self._persistence.save_player(player)
            logger.info(
                "Character leveled up",
                player_id=str(player_id),
                old_level=old_level,
                new_level=new_level,
                total_xp=player.experience_points,
            )
            if self._level_up_hook:
                await self._level_up_hook(player_id, new_level)
        else:
            # Persist XP increase (level unchanged)
            await self._persistence.save_player(player)

    async def check_level_up(self, player_id: uuid.UUID) -> bool:
        """
        Recompute level from current total XP and persist if level increased.

        Use when XP may have been changed elsewhere (e.g. direct DB update) or
        to sync level with the curve. If level increases, the level-up hook is
        invoked.

        Args:
            player_id: Character to check.

        Returns:
            True if level increased and was persisted, False otherwise.

        Raises:
            ValueError: If player not found.
        """
        player = await self._persistence.get_player_by_id(player_id)
        if not player:
            raise ValueError(f"Player {player_id} not found")

        new_level = level_from_total_xp(player.experience_points)
        if new_level <= player.level:
            return False

        old_level = player.level
        player.level = new_level
        await self._persistence.save_player(player)
        logger.info(
            "Character level synced (level-up)",
            player_id=str(player_id),
            old_level=old_level,
            new_level=new_level,
        )
        if self._level_up_hook:
            await self._level_up_hook(player_id, new_level)
        return True
