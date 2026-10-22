"""The catatonia clock: a catatonic player (LCD 0 to -9) loses LCD on a timer until delirium takes them at -10 (#1148).

The mirror of DP bleed-out (``game_tick_death``), with two deliberate differences. It does not pause in combat: combat
costs DP, never LCD, so a pause would leave a catatonic player frozen at 0 while something finishes them. And the
decay is configurable (``GameConfig.catatonia_decay_interval_seconds``) because ``/ground`` is a channel that has to
fit inside the window. Like bleed-out it covers offline players, so logging out is not an escape. Each step goes
through ``LucidityService``, so tiers, events, the catatonia observer and the delirium handler behave as for any other
LCD loss, and it stacks with ``lucidity_drain_over_time`` (both clamp at the floor, so delirium fires once).
"""

from __future__ import annotations

import uuid
from typing import cast

from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession

from ..config import get_config
from ..services.lucidity_service import CatatoniaObserverProtocol, LucidityService
from ..structured_logging.enhanced_logging_config import get_logger
from .game_tick_protocols import _TickContainer

logger = get_logger("server.game_tick")

CATATONIA_DECAY_REASON_CODE = "catatonia_decay"
# Delirium fires when LCD crosses -10 (lucidity_trigger_handlers), so the clock stops there.
DELIRIUM_LCD = -10

_CATATONIC_IDS_SQL = text("SELECT player_id FROM get_catatonic_player_ids()")


def is_catatonia_decay_tick(tick_count: int) -> bool:
    """True on the ticks that land on the configured decay interval, whatever the tick rate."""
    ticks_per_step = round(get_config().game.catatonia_decay_interval_seconds / get_config().game.server_tick_rate)
    return not tick_count % max(1, ticks_per_step)


async def _decay_one(service: LucidityService, player_id: uuid.UUID) -> None:
    """Take one LCD from the player, re-reading it first: a tonic, ``/ground`` or a drain may have moved it."""
    current = (await service.get_player_lucidity(player_id)).current_lcd
    if current > 0 or current <= DELIRIUM_LCD:
        return
    _ = await service.apply_lucidity_adjustment(player_id, -1, reason_code=CATATONIA_DECAY_REASON_CODE)


async def process_catatonia_decay(container: _TickContainer, session: AsyncSession, tick_count: int) -> None:
    """Run one decay step for every catatonic player when the tick is due.

    A database failure rolls the shared tick session back (an aborted transaction would fail every later query this
    tick) and the next due tick retries.
    """
    if not is_catatonia_decay_tick(tick_count):
        return
    try:
        ids = cast("list[uuid.UUID]", (await session.execute(_CATATONIC_IDS_SQL)).scalars().all())
        if not ids:
            return
        observer = cast(CatatoniaObserverProtocol | None, getattr(container, "catatonia_registry", None))
        service = LucidityService(session, catatonia_observer=observer)
        for player_id in ids:
            await _decay_one(service, player_id)
        await session.commit()
    except (SQLAlchemyError, ValueError, RuntimeError, OSError) as e:
        logger.warning("Catatonia decay failed; will retry next interval", tick_count=tick_count, error=str(e))
        await session.rollback()
