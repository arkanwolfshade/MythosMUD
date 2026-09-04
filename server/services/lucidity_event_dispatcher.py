"""Helpers for broadcasting lucidity-related SSE events."""

# pylint: disable=too-many-arguments,too-many-positional-arguments  # Reason: Event dispatching requires many parameters for context and event routing

from __future__ import annotations

import uuid
from collections.abc import Iterable, Mapping
from dataclasses import dataclass

from ..structured_logging.enhanced_logging_config import get_logger
from ..utils.liability_types import LiabilityStackEntry

logger = get_logger(__name__)


async def _dispatch_player_event(player_id: uuid.UUID | str, event_type: str, payload: Mapping[str, object]) -> None:
    """Send an event to a specific player, swallowing transport errors in headless tests."""
    # Convert UUID to string for send_game_event (which expects str for JSON serialization)
    player_id_str = str(player_id) if isinstance(player_id, uuid.UUID) else player_id

    try:
        from ..realtime.connection_manager_api import send_game_event
    except ImportError as exc:  # pragma: no cover - import side effects in tests
        logger.debug(
            "Lucidity event dispatch unavailable",
            event_type=event_type,
            # Structlog handles UUID objects automatically, no need to convert to string
            player_id=player_id,
            error=str(exc),
        )
        return

    try:
        await send_game_event(player_id_str, event_type, payload)
    except (
        AttributeError,
        TypeError,
        ValueError,
        RuntimeError,
        ConnectionError,
        OSError,
    ) as exc:  # pragma: no cover - connection manager may be absent in tests
        logger.debug(
            "Failed to deliver lucidity event",
            event_type=event_type,
            # Structlog handles UUID objects automatically, no need to convert to string
            player_id=player_id,
            error=str(exc),
        )


def _format_liabilities(liabilities: Iterable[LiabilityStackEntry] | None) -> list[str]:
    """Flatten liability entries into human-readable strings for the client."""
    formatted: list[str] = []
    if not liabilities:
        return formatted

    for entry in liabilities:
        code = str(entry.get("code", "")).strip()
        if not code:
            continue
        stacks = entry.get("stacks", 1)
        try:
            stacks_int = int(stacks)
        except (TypeError, ValueError):
            stacks_int = 1

        if stacks_int > 1:
            formatted.append(f"{code} (x{stacks_int})")
        else:
            formatted.append(code)
    return formatted


@dataclass(frozen=True)
class LucidityChangeEventExtras:
    """Optional lucidity change event fields (reduces send_lucidity_change_event parameter count)."""

    max_lcd: int | None = None
    liabilities: Iterable[LiabilityStackEntry] | None = None
    reason: str | None = None
    source: str | None = None
    metadata: Mapping[str, object] | None = None


async def send_lucidity_change_event(
    player_id: uuid.UUID | str,
    *,
    current_lcd: int,
    delta: int,
    tier: str,
    extras: LucidityChangeEventExtras | None = None,
) -> None:
    """Notify a player that their LCD changed."""
    event_extras = extras or LucidityChangeEventExtras()
    # Convert UUID to string for JSON payload (client expects string)
    player_id_str = str(player_id) if isinstance(player_id, uuid.UUID) else player_id
    # Use provided max_lcd or default to 100 for backward compatibility
    # Note: max_lcd should be calculated from player's education stat (max_lucidity = education)
    payload: dict[str, object] = {
        "player_id": player_id_str,
        "current_lcd": current_lcd,
        "max_lcd": event_extras.max_lcd if event_extras.max_lcd is not None else 100,
        "delta": delta,
        "tier": tier,
    }

    liability_strings = _format_liabilities(event_extras.liabilities)
    if liability_strings:
        payload["liabilities"] = liability_strings
    if event_extras.reason:
        payload["reason"] = event_extras.reason
    if event_extras.source:
        payload["source"] = event_extras.source
    if event_extras.metadata:
        payload["metadata"] = event_extras.metadata

    await _dispatch_player_event(player_id, "lucidity_change", payload)


async def send_catatonia_event(  # pylint: disable=too-many-arguments,too-many-positional-arguments  # Reason: Event dispatching requires many parameters for context and event routing
    player_id: uuid.UUID | str,
    *,
    current_lcd: int | None = None,
    message: str | None = None,
    status: str = "catatonic",
    rescuer_name: str | None = None,
    target_name: str | None = None,
) -> None:
    """Emit a catatonia state event to the affected player."""
    payload: dict[str, object] = {
        "status": status,
        "rescuer_name": rescuer_name,
        "target_name": target_name,
    }
    if current_lcd is not None:
        payload["current_lcd"] = current_lcd
    if message:
        payload["message"] = message

    await _dispatch_player_event(player_id, "catatonia", payload)


async def send_rescue_update_event(
    player_id: uuid.UUID | str,
    *,
    status: str,
    current_lcd: int | None = None,
    message: str | None = None,
    rescuer_name: str | None = None,
    target_name: str | None = None,
    progress: float | None = None,
    eta_seconds: float | None = None,
) -> None:
    """Send rescue progress/status updates to either participant."""
    payload: dict[str, object] = {
        "status": status,
        "rescuer_name": rescuer_name,
        "target_name": target_name,
    }
    if current_lcd is not None:
        payload["current_lcd"] = current_lcd
    if message:
        payload["message"] = message
    if progress is not None:
        payload["progress"] = progress
    if eta_seconds is not None:
        payload["eta_seconds"] = eta_seconds

    await _dispatch_player_event(player_id, "rescue_update", payload)


async def send_hallucination_event(
    player_id: uuid.UUID | str,
    *,
    hallucination_type: str,
    message: str,
    metadata: Mapping[str, object] | None = None,
) -> None:
    """Send a hallucination event to a player."""
    payload: dict[str, object] = {
        "hallucination_type": hallucination_type,
        "message": message,
    }
    if metadata:
        payload["metadata"] = metadata

    await _dispatch_player_event(player_id, "hallucination", payload)


__all__ = [
    "LucidityChangeEventExtras",
    "send_catatonia_event",
    "send_rescue_update_event",
    "send_lucidity_change_event",
    "send_hallucination_event",
]
