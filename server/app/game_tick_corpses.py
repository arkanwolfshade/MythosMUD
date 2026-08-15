"""Decayed corpse cleanup for the game tick loop."""

from typing import TYPE_CHECKING, Protocol, cast
from uuid import UUID

from fastapi import FastAPI

from ..services.corpse_lifecycle_service import CorpseLifecycleService
from ..structured_logging.enhanced_logging_config import get_logger
from ..time.time_service import get_mythos_chronicle

if TYPE_CHECKING:
    from ..async_persistence import AsyncPersistenceLayer
    from ..container.main import ApplicationContainer

logger = get_logger("server.game_tick")


def _create_corpse_lifecycle_service(app: FastAPI) -> CorpseLifecycleService | None:
    """Create CorpseLifecycleService or None if persistence is unavailable."""
    container = cast("ApplicationContainer", app.state.container)
    persistence = cast("AsyncPersistenceLayer | None", container.persistence)
    if persistence is None:
        return None

    connection_manager = cast(object | None, container.connection_manager)
    time_service = get_mythos_chronicle()

    return CorpseLifecycleService(
        persistence=persistence,
        connection_manager=connection_manager,
        time_service=time_service,
    )


class _CorpseLike(Protocol):
    room_id: str | None
    container_id: UUID


async def _cleanup_single_decayed_corpse(
    corpse_service: CorpseLifecycleService,
    connection_manager: object | None,
    corpse: _CorpseLike,
    tick_count: int,
) -> bool:
    """Cleanup a single decayed corpse. Returns True on success."""
    try:
        if connection_manager and corpse.room_id:
            # Inline import: module-level import cycles through container_websocket_events
            # back to game_tick_processing (basedpyright reportImportCycles).
            from ..services.container_websocket_events import emit_container_decayed

            _ = await emit_container_decayed(
                connection_manager=connection_manager,
                container_id=corpse.container_id,
                room_id=corpse.room_id,
            )

        await corpse_service.cleanup_decayed_corpse(corpse.container_id)
        logger.debug(
            "Cleaned up decayed corpse",
            tick_count=tick_count,
            container_id=str(corpse.container_id),
            room_id=corpse.room_id,
        )
        return True
    except (AttributeError, KeyError, TypeError, ValueError, RuntimeError) as cleanup_error:
        logger.error(
            "Error cleaning up individual decayed corpse",
            error=str(cleanup_error),
            container_id=str(corpse.container_id),
            tick_count=tick_count,
            exc_info=True,
        )
        return False


def _log_cleanup_results(tick_count: int, cleaned_count: int, total_decayed: int) -> None:
    """Log the results of corpse cleanup."""
    if cleaned_count > 0:
        logger.info(
            "Decayed corpses cleaned up",
            tick_count=tick_count,
            cleaned_count=cleaned_count,
            total_decayed=total_decayed,
        )
    elif total_decayed > 0:
        logger.warning(
            "Found decayed corpses but none were cleaned",
            tick_count=tick_count,
            total_decayed=total_decayed,
            cleaned_count=cleaned_count,
        )


async def cleanup_decayed_corpses(app: FastAPI, tick_count: int) -> None:
    """Cleanup decayed corpse containers (every 60 ticks = 1 minute)."""
    if tick_count % 60:
        return

    logger.debug("Running decayed corpse cleanup check", tick_count=tick_count)

    try:
        corpse_service = _create_corpse_lifecycle_service(app)
        if corpse_service is None:
            logger.warning("Persistence layer not available for corpse cleanup", tick_count=tick_count)
            return

        decayed = await corpse_service.get_all_decayed_corpses()
        logger.debug(
            "Decayed corpses check completed",
            tick_count=tick_count,
            decayed_count=len(decayed),
        )

        cleaned_count = 0
        container = cast("ApplicationContainer", app.state.container)
        connection_manager = cast(object | None, container.connection_manager)

        for corpse in decayed:
            if await _cleanup_single_decayed_corpse(corpse_service, connection_manager, corpse, tick_count):
                cleaned_count += 1

        _log_cleanup_results(tick_count, cleaned_count, len(decayed))
    except (AttributeError, KeyError, TypeError, ValueError, RuntimeError) as corpse_cleanup_error:
        logger.error(
            "Error during decayed corpse cleanup",
            error=str(corpse_cleanup_error),
            tick_count=tick_count,
            exc_info=True,
        )
