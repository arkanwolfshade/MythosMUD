"""
Player DP on the player registry (ADR-029 step 6a): the one write path for ``stats.current_dp``.

Each change runs one registry unit and is sync, like corruption: the DP (and any posture it implies) commits before
the call returns, so the readers that still load players from the database see it. ``upsert_player`` keeps an
existing player's stored DP, so a write that bypasses this service is lost. The rules themselves are the pure
functions in ``models/player_dp.py``; callers that already hold a unit (death, respawn) use ``apply_in``.
"""

from __future__ import annotations

import uuid
from collections.abc import Callable, Mapping
from typing import TYPE_CHECKING, Protocol

from ..models.player_dp import DEAD_DP, DpChange, damaged, decayed, dp_of, healed, set_to

if TYPE_CHECKING:
    from ..game.player_registry import PlayerAggregate, PlayerRegistry
    from ..models.player import Player


class HealthPersistence(Protocol):
    """Damage and healing as callers that hold only the persistence layer use them (it runs this service)."""

    async def heal_player(self, player: Player, amount: int) -> None:
        """Heal ``player`` and mirror the new DP onto it."""
        ...  # pylint: disable=unnecessary-ellipsis  # Reason: basedpyright requires an explicit stub body

    async def damage_player(self, player: Player, amount: int, damage_type: str = "physical") -> None:
        """Damage ``player`` and mirror the new DP onto it."""
        ...  # pylint: disable=unnecessary-ellipsis  # Reason: basedpyright requires an explicit stub body


class PlayerHealthService:
    """Damage, healing, decay and absolute DP for one player, each as one sync registry unit."""

    def __init__(self, registry: PlayerRegistry) -> None:
        self._registry: PlayerRegistry = registry

    @staticmethod
    def apply_in(player: PlayerAggregate, change: DpChange) -> DpChange:
        """Write ``change`` inside the caller's unit (sync)."""
        for key, value in change.changes.items():
            player.row.set_stat(key, value, sync=True)
        return change

    async def _run(self, player_id: uuid.UUID, rule: Callable[[Mapping[str, object]], DpChange]) -> DpChange:
        async with self._registry.mutate(player_id) as player:  # pylint: disable=contextmanager-generator-missing-cleanup  # Reason: @asynccontextmanager always drives this generator to completion; pylint cannot see through the wrapper
            return self.apply_in(player, rule(player.row.stats))

    async def damage(self, player_id: uuid.UUID, amount: int, damage_type: str = "physical") -> DpChange:
        """Damage after resistances, never below 0 DP."""
        if amount < 0:
            raise ValueError(f"Damage amount must be positive, got {amount}")
        return await self._run(player_id, lambda stats: damaged(stats, amount, damage_type))

    async def heal(self, player_id: uuid.UUID, amount: int) -> DpChange:
        """Heal, never above max DP (no write when already full)."""
        if amount < 0:
            raise ValueError(f"Healing amount must be positive, got {amount}")
        return await self._run(player_id, lambda stats: healed(stats, amount))

    async def set_dp(self, player_id: uuid.UUID, new_dp: int) -> DpChange:
        """An absolute DP (combat, admin), with its posture."""
        return await self._run(player_id, lambda stats: set_to(stats, new_dp))

    async def decay(self, player_id: uuid.UUID, amount: int = 1) -> DpChange | None:
        """Bleed a mortally wounded player; None (and no write) when they are already dead."""
        async with self._registry.mutate(player_id) as player:  # pylint: disable=contextmanager-generator-missing-cleanup  # Reason: @asynccontextmanager always drives this generator to completion; pylint cannot see through the wrapper
            if dp_of(player.row.stats) <= DEAD_DP:
                return None
            return self.apply_in(player, decayed(player.row.stats, amount))
