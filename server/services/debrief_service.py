"""Debrief: the post-crisis session that recaps what happened and can run an immediate therapy session.

Delirium and sanitarium respawns leave a ``DEBRIEF_PENDING`` flag on the player. ``perform_debrief`` is the one place
that spends it: it recaps recent lucidity events, optionally runs therapy, and clears the flag. It is driven by the
``debrief`` scripted action (Dr. Morgan's dialogue, ADR-028) and by the parked debrief command (#872).
"""

from __future__ import annotations

import uuid
from dataclasses import dataclass
from typing import cast

from sqlalchemy import desc, select
from sqlalchemy.ext.asyncio import AsyncSession

from ..database import get_async_session
from ..models.lucidity import LucidityActionCode, LucidityAdjustmentLog
from ..models.player import Player
from ..structured_logging.enhanced_logging_config import get_logger
from .active_lucidity_service import ActiveLucidityService, LucidityActionOnCooldownError
from .lucidity_helpers import LucidityUpdateResult
from .lucidity_service import CatatoniaObserverProtocol, LucidityService

logger = get_logger(__name__)

NOT_AVAILABLE_MESSAGE = (
    "No debrief session is available. This interaction is only available after sanitarium intervention."
)
COMPLICATIONS_MESSAGE = "The debrief session encountered complications. Please try again."
NO_SESSION_MESSAGE = "The sanitarium records could not be accessed. Please try again."

_NO_RECORDS_RECAP = (
    "The sanitarium staff notes your arrival but records are incomplete. "
    "They recommend rest and observation. Your mind has been through a trial, "
    "though the specifics remain clouded."
)
_FALLBACK_RECAP = (
    "The sanitarium staff provides a general overview: you experienced a severe "
    "lucidity crisis requiring immediate intervention. Your mind has been stabilized, "
    "but recovery will require time and care."
)
_RECAP_CLOSING = (
    "The staff explains that you experienced a significant lucidity crisis, "
    "requiring immediate intervention. Your mind has been stabilized, but "
    "the effects of your ordeal remain. Recovery will take time and care."
)
_CONCLUSION = (
    "The debrief session concludes. You are free to leave the sanitarium "
    "when you are ready, though the staff recommends rest and reflection."
)


@dataclass(frozen=True)
class DebriefOutcome:
    """What the player is told, and whether the debrief actually ran (and so spent DEBRIEF_PENDING)."""

    message: str
    completed: bool


def _summarize(adjustments: list[LucidityAdjustmentLog]) -> str:
    """Narrative recap of the latest adjustments, grouped by reason."""
    recent_events: dict[str, list[int]] = {}
    for adj in adjustments[:5]:
        recent_events.setdefault(adj.reason_code.replace("_", " ").title(), []).append(adj.delta)
    lines = ["The sanitarium staff provides you with a brief recap of recent events:", ""]
    for reason, deltas in recent_events.items():
        total = sum(deltas)
        sign = "+" if total >= 0 else ""
        plural = "s" if len(deltas) > 1 else ""
        lines.append(f"- {reason}: {len(deltas)} occurrence{plural}, net change {sign}{total} LCD")
    return "\n".join([*lines, "", _RECAP_CLOSING])


async def generate_narrative_recap(player_id: uuid.UUID, session: AsyncSession) -> str:
    """Narrative recap of the player's recent lucidity events; a generic overview if the records cannot be read."""
    try:
        statement = (
            select(LucidityAdjustmentLog)
            .where(LucidityAdjustmentLog.player_id == player_id)
            .order_by(desc(LucidityAdjustmentLog.created_at))
            .limit(10)
        )
        adjustments = list((await session.execute(statement)).scalars().all())
    except Exception as e:  # pylint: disable=broad-exception-caught  # Reason: recap errors are unpredictable and must fall back, not fail the debrief
        logger.warning("Failed to generate narrative recap", player_id=player_id, error=str(e))
        return _FALLBACK_RECAP
    return _summarize(adjustments) if adjustments else _NO_RECORDS_RECAP


async def _therapy_note(
    player: Player, session: AsyncSession, observer: CatatoniaObserverProtocol | None, player_id: uuid.UUID
) -> str:
    """The paragraph describing the optional immediate therapy session (run it, or say why it did not happen)."""
    active_service = ActiveLucidityService(session, catatonia_observer=observer)
    room_id = cast(str | None, player.current_room_id)
    try:
        result = cast(
            LucidityUpdateResult,
            await active_service.perform_recovery_action(
                player_id=player_id, action_code="therapy", location_id=str(room_id) if room_id else None
            ),
        )
    except LucidityActionOnCooldownError:
        return "Therapy is currently unavailable due to recent sessions. You may return later for additional support."
    except Exception as e:  # pylint: disable=broad-exception-caught  # Reason: therapy errors are unpredictable and must not fail the debrief
        logger.warning("Therapy failed during debrief", player_id=player_id, error=str(e))
        return "Therapy session could not be initiated at this time."
    sign = "+" if result.delta >= 0 else ""
    return (
        "You opt for immediate therapy. The sanitarium staff guides you through a structured session. "
        f"Stability shifts {sign}{result.delta}, settling at {result.new_lcd}/100."
    )


async def _run_debrief(
    player: Player,
    session: AsyncSession,
    lucidity_service: LucidityService,
    wants_therapy: bool,
    observer: CatatoniaObserverProtocol | None,
) -> DebriefOutcome:
    player_id = uuid.UUID(str(player.player_id))
    if await lucidity_service.get_cooldown(player_id, LucidityActionCode.DEBRIEF_PENDING) is None:
        return DebriefOutcome(NOT_AVAILABLE_MESSAGE, completed=False)
    parts = [await generate_narrative_recap(player_id, session)]
    if wants_therapy:
        parts.append(await _therapy_note(player, session, observer, player_id))
    _ = await lucidity_service.clear_cooldown(player_id, LucidityActionCode.DEBRIEF_PENDING)
    await session.commit()
    parts.append(_CONCLUSION)
    logger.info("Debrief completed", player_id=player_id, therapy_requested=wants_therapy)
    return DebriefOutcome("\n\n".join(parts), completed=True)


async def perform_debrief(
    player: Player, *, wants_therapy: bool = False, catatonia_observer: CatatoniaObserverProtocol | None = None
) -> DebriefOutcome:
    """Run the debrief for ``player``: recap, optional therapy, then clear DEBRIEF_PENDING.

    Reports "not available" (without touching anything) when no debrief is pending. A failure rolls back, so the flag
    survives and the player can try again.
    """
    async for session in get_async_session():
        try:
            return await _run_debrief(player, session, LucidityService(session), wants_therapy, catatonia_observer)
        except Exception as e:  # pylint: disable=broad-exception-caught  # Reason: debrief errors are unpredictable and must be handled gracefully
            logger.error("Debrief failed", player_id=str(player.player_id), error=str(e), exc_info=True)
            await session.rollback()
            return DebriefOutcome(COMPLICATIONS_MESSAGE, completed=False)
    return DebriefOutcome(NO_SESSION_MESSAGE, completed=False)
