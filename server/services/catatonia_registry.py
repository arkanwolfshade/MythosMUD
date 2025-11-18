"""In-memory registry tracking catatonic investigators."""

from __future__ import annotations

import asyncio
from collections.abc import Awaitable, Callable
from datetime import UTC, datetime
from threading import RLock

from ..logging.enhanced_logging_config import get_logger
from .sanity_service import CatatoniaObserverProtocol

logger = get_logger(__name__)


class CatatoniaRegistry(CatatoniaObserverProtocol):
    """Track players who have entered catatonia and coordinate failover hooks."""

    def __init__(
        self,
        *,
        failover_callback: Callable[[str, int], Awaitable[None] | None] | None = None,
    ) -> None:
        self._lock = RLock()
        self._catatonic: dict[str, datetime] = {}
        self._failover_callback = failover_callback

    # Observer protocol implementations -------------------------------------------------

    def on_catatonia_entered(self, *, player_id: str, entered_at: datetime, current_san: int) -> None:
        with self._lock:
            self._catatonic[player_id] = entered_at

        logger.debug(
            "Catatonia registry marked player",
            player_id=player_id,
            entered_at=entered_at.isoformat(),
            current_san=current_san,
        )

    def on_catatonia_cleared(self, *, player_id: str, resolved_at: datetime) -> None:
        with self._lock:
            self._catatonic.pop(player_id, None)

        logger.debug("Catatonia cleared for player", player_id=player_id, resolved_at=resolved_at.isoformat())

    def on_sanitarium_failover(self, *, player_id: str, current_san: int) -> None:
        with self._lock:
            self._catatonic[player_id] = datetime.now(UTC)

        logger.warning(
            "Catatonia failover triggered",
            player_id=player_id,
            current_san=current_san,
        )

        callback = self._failover_callback
        if callback is None:
            return

        try:
            result = callback(player_id, current_san)
            if asyncio.iscoroutine(result):
                # Fire-and-forget failover task
                # AnyIO Pattern: For fire-and-forget tasks, we create them but don't track
                # since they're intentionally decoupled from the main flow.
                # The callback is responsible for its own error handling.
                try:
                    task = asyncio.create_task(result)

                    # Add a callback to log if it fails (defensive logging)
                    def log_failover_error(t: asyncio.Task) -> None:
                        try:
                            t.result()  # This will raise if task failed
                        except Exception as e:
                            logger.error("Failover callback task failed", player_id=player_id, error=str(e))

                    task.add_done_callback(log_failover_error)
                except RuntimeError:
                    # No event loop available - log and continue
                    logger.warning("Failover callback requires event loop", player_id=player_id)
        except Exception as exc:  # pragma: no cover - defensive logging
            logger.error("Failover callback failed", player_id=player_id, error=str(exc))

    # Registry helpers ------------------------------------------------------------------

    def is_catatonic(self, player_id: str) -> bool:
        """Return True if the player is currently registered as catatonic."""

        with self._lock:
            return player_id in self._catatonic

    def get_snapshot(self) -> dict[str, datetime]:
        """Return a shallow copy of the current registry for diagnostics."""

        with self._lock:
            return dict(self._catatonic)
