"""Best-effort async scheduling for NPC combat cleanup (extracted to limit npc_base.py size)."""

from __future__ import annotations

from typing import cast

from structlog.stdlib import BoundLogger

from ..structured_logging.enhanced_logging_config import get_logger

logger: BoundLogger = cast(BoundLogger, get_logger(__name__))


def schedule_end_combat_if_npc_died_best_effort(npc_id: str) -> None:
    """Schedule end_combat_if_npc_died so the slain NPC no longer gets combat turns (best-effort)."""
    try:
        import asyncio

        from ..services.combat_service_state import get_combat_service

        combat_service = get_combat_service()
        if not combat_service or not hasattr(combat_service, "end_combat_if_npc_died"):
            return
        try:
            loop = asyncio.get_running_loop()
            _ = loop.create_task(combat_service.end_combat_if_npc_died(npc_id))
        except RuntimeError:
            logger.debug(
                "Skipping async end_combat_if_npc_died schedule (no running event loop)",
                npc_id=npc_id,
            )
    except Exception as exc:  # pylint: disable=broad-exception-caught  # Best-effort; must not fail death handling
        logger.debug(
            "Best-effort end_combat_if_npc_died scheduling failed",
            npc_id=npc_id,
            error=str(exc),
            error_type=type(exc).__name__,
        )
