"""
Player MP on the player registry (ADR-029 step 6b): the one write path for ``stats.magic_points``.

Each change runs one registry unit and is sync, like DP: it commits before the call returns, so the readers that still
load players from the database see it. ``upsert_player`` keeps an existing player's stored MP, so a write that bypasses
this service is lost. The rules themselves are the pure functions in ``models/player_mp.py``.
"""

from __future__ import annotations

import uuid
from collections.abc import Callable, Mapping
from typing import TYPE_CHECKING

from sqlalchemy.exc import SQLAlchemyError

from ..models.player_mp import MpChange, after_gaining, after_spending, set_to
from ..structured_logging.enhanced_logging_config import get_logger

if TYPE_CHECKING:
    from ..game.player_registry import PlayerAggregate, PlayerRegistry

logger = get_logger(__name__)


async def announce_mp(player_id: uuid.UUID, change: MpChange) -> None:
    """Tell the player's client their new MP; a failed send never fails the change that already committed."""
    try:
        from ..realtime.connection_manager_api import send_game_event

        await send_game_event(
            player_id,
            "player_update",
            {"stats": {"magic_points": change.new_mp, "max_magic_points": change.max_mp}},
        )
    except (ValueError, AttributeError, SQLAlchemyError, OSError, TypeError, RuntimeError) as e:
        logger.warning("Failed to send MP update event", player_id=player_id, error=str(e))


def _write(player: PlayerAggregate, change: MpChange) -> MpChange:
    player.row.set_stat("magic_points", change.new_mp, sync=True)
    # Regeneration's fraction used to be saved here; it now lives on MPRegenerationService.
    player.row.remove_stat("_mp_fractional", sync=True)
    return change


class PlayerMpService:
    """Spending, restoring and setting MP for one player, each as one sync registry unit."""

    def __init__(self, registry: PlayerRegistry) -> None:
        self._registry: PlayerRegistry = registry

    async def _run(self, player_id: uuid.UUID, rule: Callable[[Mapping[str, object]], MpChange]) -> MpChange:
        async with self._registry.mutate(player_id) as player:  # pylint: disable=contextmanager-generator-missing-cleanup  # Reason: @asynccontextmanager always drives this generator to completion; pylint cannot see through the wrapper
            return _write(player, rule(player.row.stats))

    async def spend(self, player_id: uuid.UUID, cost: int) -> MpChange:
        """Pay ``cost``, never below 0 MP."""
        return await self._run(player_id, lambda stats: after_spending(stats, cost))

    async def restore(self, player_id: uuid.UUID, amount: float) -> MpChange:
        """Gain ``amount`` (whole MP are kept), capped at max MP."""
        return await self._run(player_id, lambda stats: after_gaining(stats, amount))

    async def drain(self, target_id: uuid.UUID, into_id: uuid.UUID, amount: int) -> tuple[MpChange, MpChange]:
        """Move up to ``amount`` MP from one player to another, in one transaction; returns (target's, receiver's)."""
        async with self._registry.mutate_many([target_id, into_id]) as (target, receiver):  # pylint: disable=contextmanager-generator-missing-cleanup  # Reason: @asynccontextmanager always drives this generator to completion; pylint cannot see through the wrapper
            lost = _write(target, after_spending(target.row.stats, amount))
            return lost, _write(receiver, after_gaining(receiver.row.stats, -lost.gained))

    async def set_mp(self, player_id: uuid.UUID, new_mp: int) -> MpChange:
        """An absolute MP (admin set)."""
        return await self._run(player_id, lambda stats: set_to(stats, new_mp))
