"""Helpers for broadcasting sanity-related SSE events."""

from __future__ import annotations

from collections.abc import Iterable
from typing import Any

from ..logging.enhanced_logging_config import get_logger

logger = get_logger(__name__)


async def _dispatch_player_event(player_id: str, event_type: str, payload: dict[str, Any]) -> None:
    """Send an event to a specific player, swallowing transport errors in headless tests."""
    try:
        from ..realtime.sse_handler import send_game_event
    except Exception as exc:  # pragma: no cover - import side effects in tests
        logger.debug(
            "Sanity event dispatch unavailable",
            event_type=event_type,
            player_id=player_id,
            error=str(exc),
        )
        return

    try:
        await send_game_event(str(player_id), event_type, payload)
    except Exception as exc:  # pragma: no cover - connection manager may be absent in tests
        logger.debug(
            "Failed to deliver sanity event",
            event_type=event_type,
            player_id=str(player_id),
            error=str(exc),
        )


def _format_liabilities(liabilities: Iterable[dict[str, Any]] | None) -> list[str]:
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


async def send_sanity_change_event(
    player_id: str,
    *,
    current_san: int,
    delta: int,
    tier: str,
    liabilities: Iterable[dict[str, Any]] | None = None,
    reason: str | None = None,
    source: str | None = None,
    metadata: dict[str, Any] | None = None,
) -> None:
    """Notify a player that their SAN changed."""
    payload: dict[str, Any] = {
        "player_id": str(player_id),
        "current_san": current_san,
        "max_san": 100,
        "delta": delta,
        "tier": tier,
    }

    liability_strings = _format_liabilities(liabilities)
    if liability_strings:
        payload["liabilities"] = liability_strings
    if reason:
        payload["reason"] = reason
    if source:
        payload["source"] = source
    if metadata:
        payload["metadata"] = metadata

    await _dispatch_player_event(str(player_id), "sanity_change", payload)


async def send_catatonia_event(
    player_id: str,
    *,
    current_san: int | None = None,
    message: str | None = None,
    status: str = "catatonic",
    rescuer_name: str | None = None,
    target_name: str | None = None,
) -> None:
    """Emit a catatonia state event to the affected player."""
    payload: dict[str, Any] = {
        "status": status,
        "rescuer_name": rescuer_name,
        "target_name": target_name,
    }
    if current_san is not None:
        payload["current_san"] = current_san
    if message:
        payload["message"] = message

    await _dispatch_player_event(str(player_id), "catatonia", payload)


async def send_rescue_update_event(
    player_id: str,
    *,
    status: str,
    current_san: int | None = None,
    message: str | None = None,
    rescuer_name: str | None = None,
    target_name: str | None = None,
    progress: float | None = None,
    eta_seconds: float | None = None,
) -> None:
    """Send rescue progress/status updates to either participant."""
    payload: dict[str, Any] = {
        "status": status,
        "rescuer_name": rescuer_name,
        "target_name": target_name,
    }
    if current_san is not None:
        payload["current_san"] = current_san
    if message:
        payload["message"] = message
    if progress is not None:
        payload["progress"] = progress
    if eta_seconds is not None:
        payload["eta_seconds"] = eta_seconds

    await _dispatch_player_event(str(player_id), "rescue_update", payload)


__all__ = [
    "send_catatonia_event",
    "send_rescue_update_event",
    "send_sanity_change_event",
]
