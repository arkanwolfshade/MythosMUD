"""
Rescue service encapsulating rescue flows with injectable dependencies.

This isolates the rescue logic from command handlers so tests can exercise the
real behavior by mocking persistence, session providers, and event dispatch.
"""

# pylint: disable=too-few-public-methods,too-many-arguments,too-many-positional-arguments,too-many-locals,too-many-return-statements  # Reason: Rescue service has focused responsibility with minimal public interface, and requires many parameters and intermediate variables for complex rescue logic and multiple return statements for early validation returns

from __future__ import annotations

import asyncio
import uuid
from collections.abc import Awaitable, Callable
from datetime import UTC, datetime
from typing import TYPE_CHECKING, Any, cast

from server.services.lucidity_event_dispatcher import send_rescue_update_event
from server.services.lucidity_repository import PlayerGoneError
from server.services.lucidity_service import LucidityService, LucidityUpdateResult
from server.structured_logging.enhanced_logging_config import get_logger
from server.utils.command_parser import get_username_from_user

if TYPE_CHECKING:
    from server.game.player_registry import PlayerRegistry

logger = get_logger(__name__)

EventDispatcher = Callable[..., Awaitable[None]]


def rescue_lift(current_lcd: int) -> int:  # lizard: allow - the computed delta of both rescue paths (rescue, ground)
    """The delta that brings a catatonic player back to 1 LCD (at least +1), from their live LCD."""
    return max(1 - current_lcd, 1)


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


async def _load_rescue_participants(
    persistence: Any, target_name: str, current_user: dict[str, Any], player_name: str | None
) -> tuple[Any, Any, str] | dict[str, str]:
    """Load rescuer and target or return an error payload."""
    rescuer_name = player_name or get_username_from_user(current_user)
    rescuer = await _maybe_await(persistence.get_player_by_name(rescuer_name))
    if rescuer is None:
        return {"result": "Unable to identify rescuer."}

    target = await _maybe_await(persistence.get_player_by_name(target_name))
    if target is None:
        return {"result": f"Could not find {target_name} to rescue."}

    if getattr(rescuer, "current_room_id", None) != getattr(target, "current_room_id", None):
        return {"result": f"{target_name} is not within reach to be rescued."}

    return rescuer, target, rescuer_name


async def _dispatch_rescue_events(
    event_dispatcher: EventDispatcher,
    target_player_id_str: str,
    rescuer_player_id_str: str,
    rescuer_name: str,
    target_name: str,
) -> None:
    """Dispatch rescue notifications (best-effort)."""
    try:
        await event_dispatcher(
            target_player_id_str,
            status="rescued",
            role="target",
            rescuer_name=rescuer_name,
            target_name=target_name,
            message=f"{rescuer_name} steadies {target_name}.",
            progress=100.0,
        )
        await event_dispatcher(
            rescuer_player_id_str,
            status="rescued",
            role="rescuer",
            rescuer_name=rescuer_name,
            target_name=target_name,
            message=f"You rescue {target_name}, their lucidity stabilizing.",
            progress=100.0,
        )
    except Exception:  # noqa: B904  # pragma: no cover - notifications are best-effort  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Event dispatch errors unpredictable, must log but continue
        logger.warning("Rescue event dispatch failed", rescuer=rescuer_name, target=target_name)


def _rescue_success_payload(rescuer_name: str, target_name: str, result: Any) -> dict[str, str]:
    new_lcd = getattr(result, "new_lcd", None)
    return {
        "result": f"{rescuer_name} rushes to rescue {target_name}, restoring their lucidity.",
        "new_lcd": str(new_lcd) if new_lcd is not None else "",
    }


class RescueService:  # pylint: disable=too-few-public-methods  # Reason: Rescue service class with focused responsibility, minimal public interface
    """Service for performing rescue operations."""

    def __init__(
        self,
        persistence: Any,
        player_registry: PlayerRegistry,
        *,
        catatonia_registry: Any | None = None,
        lucidity_service: LucidityService | None = None,
        event_dispatcher: EventDispatcher = send_rescue_update_event,
    ) -> None:
        self.persistence = persistence
        self.catatonia_registry = catatonia_registry
        self.lucidity_service = lucidity_service or LucidityService(
            player_registry, catatonia_observer=catatonia_registry
        )
        self.event_dispatcher: EventDispatcher = event_dispatcher

    async def _apply_rescue_adjustment(
        self,
        target_player_id: uuid.UUID,
        rescuer_name: str,
        rescuer_room: str | None,
    ) -> LucidityUpdateResult:
        return await self.lucidity_service.apply_lucidity_adjustment(
            target_player_id,
            rescue_lift,
            reason_code="rescue_command",
            metadata={
                "rescuer": rescuer_name,
                "timestamp": datetime.now(UTC).isoformat(),
                "source": "rescue_command",
            },
            location_id=str(rescuer_room),
        )

    async def rescue(
        self, target_name: str, current_user: dict[str, Any], player_name: str | None = None
    ) -> dict[str, str]:  # pylint: disable=too-many-arguments,too-many-positional-arguments,too-many-locals  # Reason: Rescue operation requires many parameters and intermediate variables for complex rescue logic
        """
        Perform a rescue for the given target.

        Returns:
            dict containing a user-facing result message.
        """
        if not self.persistence:
            return {"result": "Rescue service is not available right now."}

        participants = await _load_rescue_participants(self.persistence, target_name, current_user, player_name)
        if isinstance(participants, dict):
            return participants

        rescuer, target, rescuer_name = participants
        target_player_id = _ensure_uuid(target.player_id)
        rescuer_player_id = _ensure_uuid(rescuer.player_id)
        target_player_id_str = str(target_player_id)
        rescuer_player_id_str = str(rescuer_player_id)

        try:
            lucidity = await self.lucidity_service.get_lucidity(target_player_id)
        except PlayerGoneError:
            return {"result": "The target's lucidity record could not be found."}
        if lucidity.tier != "catatonic":
            return {"result": f"{target_name} isn't catatonic and needs no rescue."}

        rescuer_room = cast(str | None, getattr(cast(object, rescuer), "current_room_id", None))
        try:
            result = await self._apply_rescue_adjustment(target_player_id, rescuer_name, rescuer_room)
        except Exception as exc:  # noqa: B904  # pragma: no cover - defensive path  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Rescue operation errors unpredictable, must return error
            logger.error("Rescue failed", rescuer=rescuer_name, target=target_name, error=str(exc))
            return {"result": "Rescue failed due to an unexpected error."}

        await _dispatch_rescue_events(
            self.event_dispatcher,
            target_player_id_str,
            rescuer_player_id_str,
            rescuer_name,
            target_name,
        )

        return _rescue_success_payload(rescuer_name, target_name, result)
