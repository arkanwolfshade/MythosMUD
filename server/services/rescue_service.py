"""
Rescue service encapsulating rescue flows with injectable dependencies.

This isolates the rescue logic from command handlers so tests can exercise the
real behavior by mocking persistence, session providers, and event dispatch.
"""

from __future__ import annotations

import asyncio
import uuid
from collections.abc import Awaitable, Callable
from datetime import UTC, datetime
from typing import Any

from server.models.lucidity import PlayerLucidity
from server.services.lucidity_event_dispatcher import send_rescue_update_event
from server.services.lucidity_service import LucidityService
from server.structured_logging.enhanced_logging_config import get_logger
from server.utils.command_parser import get_username_from_user

logger = get_logger(__name__)

# Type alias for async session factory: produces an async generator of sessions
AsyncSessionFactory = Callable[[], Any]
LucidityServiceFactory = Callable[[Any], LucidityService]
EventDispatcher = Callable[..., Awaitable[None]]


def _ensure_uuid(value: Any) -> uuid.UUID:
    """Convert value to UUID, raising ValueError if invalid."""
    if isinstance(value, uuid.UUID):
        return value
    return uuid.UUID(str(value))


async def _maybe_await(value: Any) -> Any:
    """Await the value if it is awaitable."""
    if asyncio.iscoroutine(value) or isinstance(value, Awaitable):
        return await value
    return value


class RescueService:
    """Service for performing rescue operations."""

    def __init__(
        self,
        persistence: Any,
        session_factory: AsyncSessionFactory,
        *,
        catatonia_registry: Any = None,
        lucidity_service_factory: LucidityServiceFactory | None = None,
        event_dispatcher: EventDispatcher = send_rescue_update_event,
    ) -> None:
        self.persistence = persistence
        self.session_factory = session_factory
        self.catatonia_registry = catatonia_registry
        self.lucidity_service_factory = lucidity_service_factory or (
            lambda session: LucidityService(session, catatonia_observer=catatonia_registry)
        )
        self.event_dispatcher = event_dispatcher

    async def rescue(self, target_name: str, current_user: dict, player_name: str | None = None) -> dict[str, str]:
        """
        Perform a rescue for the given target.

        Returns:
            dict containing a user-facing result message.
        """
        if not self.persistence:
            return {"result": "Rescue service is not available right now."}

        rescuer_name = player_name or get_username_from_user(current_user)
        rescuer = await _maybe_await(self.persistence.get_player_by_name(rescuer_name))
        if rescuer is None:
            return {"result": "Unable to identify rescuer."}

        target = await _maybe_await(self.persistence.get_player_by_name(target_name))
        if target is None:
            return {"result": f"Could not find {target_name} to rescue."}

        if getattr(rescuer, "current_room_id", None) != getattr(target, "current_room_id", None):
            return {"result": f"{target_name} is not within reach to be rescued."}

        target_player_id = _ensure_uuid(target.player_id)
        rescuer_player_id = _ensure_uuid(rescuer.player_id)
        target_player_id_str = str(target_player_id)
        rescuer_player_id_str = str(rescuer_player_id)

        async for session in self.session_factory():
            lucidity_record = await session.get(PlayerLucidity, target_player_id_str)
            if lucidity_record is None:
                return {"result": "The target's lucidity record could not be found."}

            if lucidity_record.current_tier != "catatonic":
                return {"result": f"{target_name} isn't catatonic and needs no rescue."}

            delta = 1 - lucidity_record.current_lcd
            if delta <= 0:
                delta = 1

            lucidity_service = self.lucidity_service_factory(session)
            try:
                result = await lucidity_service.apply_lucidity_adjustment(
                    target_player_id,
                    delta,
                    reason_code="rescue_command",
                    metadata={
                        "rescuer": rescuer_name,
                        "timestamp": datetime.now(UTC).isoformat(),
                        "source": "rescue_command",
                    },
                    location_id=str(getattr(rescuer, "current_room_id", None)),
                )
                await session.commit()
            except Exception as exc:  # pragma: no cover - defensive path
                await session.rollback()
                logger.error("Rescue failed", rescuer=rescuer_name, target=target_name, error=str(exc))
                return {"result": "Rescue failed due to an unexpected error."}

            # Dispatch updates (best-effort)
            try:
                await self.event_dispatcher(
                    target_player_id_str,
                    status="rescued",
                    rescuer_name=rescuer_name,
                    target_name=target_name,
                    message=f"{rescuer_name} steadies {target_name}.",
                    progress=100.0,
                )
                await self.event_dispatcher(
                    rescuer_player_id_str,
                    status="rescued",
                    rescuer_name=rescuer_name,
                    target_name=target_name,
                    message=f"You rescue {target_name}, their lucidity stabilizing.",
                    progress=100.0,
                )
            except Exception:  # pragma: no cover - notifications are best-effort
                logger.warning("Rescue event dispatch failed", rescuer=rescuer_name, target=target_name)

        new_lcd: str | None = getattr(result, "new_lcd", None)
        return {
            "result": f"{rescuer_name} rushes to rescue {target_name}, restoring their lucidity.",
            "new_lcd": str(new_lcd) if new_lcd is not None else "",  # Convert None to empty string for type consistency
        }
