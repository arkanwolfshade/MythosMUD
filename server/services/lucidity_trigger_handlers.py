"""Catatonia, delirium, and sanitarium trigger handling for lucidity changes."""

from __future__ import annotations

import uuid
from datetime import UTC, datetime
from threading import Lock

from ..models.lucidity import PlayerLucidity
from ..structured_logging.enhanced_logging_config import get_logger
from .lucidity_event_dispatcher import send_catatonia_event, send_rescue_update_event
from .lucidity_helpers import CatatoniaObserverProtocol, utc_now

logger = get_logger(__name__)

# Delirium respawn debounce: do not log/send delirium event again for the same player within this many seconds.
DELIRIUM_DEBOUNCE_SECONDS = 120
_last_delirium_trigger: dict[str, datetime] = {}
_delirium_debounce_lock = Lock()


async def handle_catatonia_transitions(
    *,
    record: PlayerLucidity,
    player_id: uuid.UUID,
    new_tier: str,
    previous_tier: str,
    new_lcd: int,
    catatonia_observer: CatatoniaObserverProtocol | None,
) -> None:
    """Handle catatonia entry and exit transitions."""
    if new_tier == "catatonic":
        if record.catatonia_entered_at is None:
            entered_at = utc_now()
            record.catatonia_entered_at = entered_at
            logger.warning("Player entered catatonia", player_id=player_id, previous_tier=previous_tier, lcd=new_lcd)
            if catatonia_observer:
                catatonia_observer.on_catatonia_entered(player_id=player_id, entered_at=entered_at, current_lcd=new_lcd)
            await send_catatonia_event(
                player_id=player_id,
                current_lcd=new_lcd,
                message="Your senses collapse into static; only allies can reach you now.",
                status="catatonic",
            )
        return

    if record.catatonia_entered_at is not None:
        resolved_at = utc_now()
        record.catatonia_entered_at = None
        logger.info("Catatonia resolved", player_id=player_id, tier_after=new_tier, lcd=new_lcd)
        if catatonia_observer:
            catatonia_observer.on_catatonia_cleared(player_id=player_id, resolved_at=resolved_at)
        await send_rescue_update_event(
            player_id=player_id,
            status="success",
            current_lcd=new_lcd,
            message="Consciousness steadies; the grounding ritual completes.",
        )


async def handle_delirium_trigger(player_id: uuid.UUID, new_lcd: int, previous_lcd: int) -> None:
    """Handle delirium respawn threshold (LCD crosses -10); debounced."""
    if new_lcd > -10 or previous_lcd <= -10:
        return
    player_id_str = str(player_id)
    with _delirium_debounce_lock:
        last = _last_delirium_trigger.get(player_id_str)
        now = datetime.now(UTC)
        if last is not None:
            elapsed = (now - last).total_seconds()
            if elapsed < DELIRIUM_DEBOUNCE_SECONDS:
                return
        _last_delirium_trigger[player_id_str] = now
    logger.warning("Delirium respawn threshold reached", player_id=player_id, previous_lcd=previous_lcd, lcd=new_lcd)
    await send_rescue_update_event(
        player_id=player_id_str,
        status="delirium",
        current_lcd=new_lcd,
        message="Your mind fractures completely. The sanitarium calls you back from the edge of madness...",
    )


async def handle_sanitarium_trigger(
    player_id: uuid.UUID,
    new_lcd: int,
    previous_lcd: int,
    catatonia_observer: CatatoniaObserverProtocol | None,
) -> None:
    """Handle sanitarium failover (LCD crosses -100); uses observer debounce if available."""
    if new_lcd > -100 or previous_lcd <= -100 or not catatonia_observer:
        return
    if not catatonia_observer.should_trigger_sanitarium_failover(player_id):
        return
    logger.error("Sanitarium failover triggered", player_id=player_id, previous_lcd=previous_lcd, lcd=new_lcd)
    catatonia_observer.on_sanitarium_failover(player_id=player_id, current_lcd=new_lcd)
    await send_rescue_update_event(
        player_id=str(player_id),
        status="sanitarium",
        current_lcd=new_lcd,
        message="Orderlies whisk you to Arkham Sanitarium for observation.",
    )


async def handle_delirium_and_sanitarium_triggers(
    player_id: uuid.UUID,
    new_lcd: int,
    previous_lcd: int,
    catatonia_observer: CatatoniaObserverProtocol | None,
) -> None:
    """Handle delirium respawn and sanitarium failover triggers."""
    await handle_delirium_trigger(player_id, new_lcd, previous_lcd)
    await handle_sanitarium_trigger(player_id, new_lcd, previous_lcd, catatonia_observer)
