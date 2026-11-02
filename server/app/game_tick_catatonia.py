"""The catatonia clock: a catatonic player (LCD 0 to -9) loses LCD on a timer until delirium takes them at -10 (#1148).

The mirror of DP bleed-out (``game_tick_death``), with two deliberate differences. It does not pause in combat: combat
costs DP, never LCD, so a pause would leave a catatonic player frozen at 0 while something finishes them. And the
decay is configurable (``GameConfig.catatonia_decay_interval_seconds``) because ``/ground`` is a channel that has to
fit inside the window. Like bleed-out it covers offline players, so logging out is not an escape. Each step goes
through ``LucidityService``, so tiers, events, the catatonia observer and the delirium handler behave as for any other
LCD loss, and it stacks with ``lucidity_drain_over_time`` (both clamp at the floor, so delirium fires once).
"""

from __future__ import annotations

from typing import TYPE_CHECKING, cast

from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession

from ..config import get_config
from ..services.lucidity_repository import PlayerGoneError
from ..services.lucidity_service import CatatoniaObserverProtocol, LucidityService
from ..structured_logging.enhanced_logging_config import get_logger
from .game_tick_protocols import _TickContainer

if TYPE_CHECKING:
    import uuid

    from ..game.player_registry import PlayerRegistry

logger = get_logger("server.game_tick")

CATATONIA_DECAY_REASON_CODE = "catatonia_decay"
# Delirium fires when LCD crosses -10 (lucidity_trigger_handlers), so the clock stops there.
DELIRIUM_LCD = -10

_CATATONIC_IDS_SQL = text("SELECT player_id FROM get_catatonic_player_ids()")


def is_catatonia_decay_tick(tick_count: int) -> bool:
    """True on the ticks that land on the configured decay interval, whatever the tick rate."""
    ticks_per_step = round(get_config().game.catatonia_decay_interval_seconds / get_config().game.server_tick_rate)
    return not tick_count % max(1, ticks_per_step)


def catatonia_step(current_lcd: int) -> int:
    """One LCD while the player is inside the countdown, else nothing: a tonic, ``/ground`` or a drain may have moved
    them since the catatonic ids were read. Evaluated inside the adjustment's unit, so it sees the live value."""
    return -1 if DELIRIUM_LCD < current_lcd <= 0 else 0


async def process_catatonia_decay(container: _TickContainer, session: AsyncSession, tick_count: int) -> None:
    """Run one decay step for every catatonic player when the tick is due.

    The ids come from the database, so a change the sweep has not written yet shows up a sweep late; the step itself
    reads the registry's live value. A failure of the id query rolls the shared tick session back (an aborted
    transaction would fail every later query this tick) and the next due tick retries.
    """
    if not is_catatonia_decay_tick(tick_count):
        return
    registry = cast("PlayerRegistry | None", container.player_registry)
    if registry is None:
        return
    try:
        ids = cast("list[uuid.UUID]", (await session.execute(_CATATONIC_IDS_SQL)).scalars().all())
        if not ids:
            return
        observer = cast(CatatoniaObserverProtocol | None, getattr(container, "catatonia_registry", None))
        service = LucidityService(registry, catatonia_observer=observer)
        for player_id in ids:
            try:
                _ = await service.apply_lucidity_adjustment(
                    player_id, catatonia_step, reason_code=CATATONIA_DECAY_REASON_CODE
                )
            except PlayerGoneError:
                logger.debug("Catatonia decay skipped: player no longer exists", player_id=str(player_id))
    except (SQLAlchemyError, ValueError, RuntimeError, OSError) as e:
        logger.warning("Catatonia decay failed; will retry next interval", tick_count=tick_count, error=str(e))
        await session.rollback()
