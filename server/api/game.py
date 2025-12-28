"""
Game mechanics API endpoints for MythosMUD server.

This module handles all game mechanics-related API operations including
game status, broadcasting, and real-time game state management.
"""

import datetime
from typing import Any

from fastapi import APIRouter, Depends, Request

from ..auth.dependencies import get_current_superuser
from ..structured_logging.enhanced_logging_config import get_logger
from ..time.time_service import get_mythos_chronicle

logger = get_logger(__name__)

# Create game router
game_router = APIRouter(prefix="/game", tags=["game"])

logger.info("Game API router initialized", prefix="/game")


@game_router.get("/status")
def get_game_status(request: Request) -> dict[str, Any]:
    """Get current game status and connection information."""
    logger.debug("Game status requested")

    # AI Agent: Get connection_manager from container instead of global import
    connection_manager = request.app.state.container.connection_manager

    status_data = {
        "active_connections": connection_manager.get_active_connection_count(),
        "active_players": len(connection_manager.player_websockets),
        "room_subscriptions": len(connection_manager.room_subscriptions),
        "server_time": datetime.datetime.now(datetime.UTC).isoformat(),
    }

    logger.debug(
        "Game status returned",
        active_connections=status_data["active_connections"],
        active_players=status_data["active_players"],
        room_subscriptions=status_data["room_subscriptions"],
    )

    return status_data


@game_router.post("/broadcast")
async def broadcast_message(
    request: Request,
    message: str,
    current_user: Any = Depends(get_current_superuser),
) -> dict[str, str | int | dict[str, Any]]:
    """
    Broadcast a message to all connected players (admin only).

    Requires superuser privileges. Returns 403 for non-admin users.
    """
    logger.info(
        "Admin broadcast message requested",
        admin_username=current_user.username,
        admin_id=str(current_user.id),
        message=message,
    )

    # AI Agent: Get connection_manager from container instead of global import
    connection_manager = request.app.state.container.connection_manager

    # Broadcast to all connected players via connection manager
    # Use broadcast_global_event to send a system broadcast
    broadcast_stats = await connection_manager.broadcast_global_event(
        event_type="system_broadcast",
        data={
            "message": message,
            "broadcaster": current_user.username,
            "broadcaster_id": str(current_user.id),
        },
    )

    recipients = broadcast_stats.get("successful_deliveries", 0)

    logger.info(
        "Admin broadcast completed",
        admin_username=current_user.username,
        recipients=recipients,
        message=message,
        broadcast_stats=broadcast_stats,
    )

    return {
        "message": message,
        "recipients": recipients,
        "broadcaster": current_user.username,
        "broadcast_stats": broadcast_stats,
    }


def _serialize_holiday(entry: Any) -> dict[str, Any]:
    """Convert a holiday entry into a JSON-friendly payload."""

    return {
        "id": getattr(entry, "id", ""),
        "name": getattr(entry, "name", ""),
        "tradition": getattr(entry, "tradition", ""),
        "season": getattr(entry, "season", ""),
        "duration_hours": getattr(entry, "duration_hours", 24),
        "bonus_tags": list(getattr(entry, "bonus_tags", []) or []),
        "notes": getattr(entry, "notes", None),
    }


@game_router.get("/time")
def get_mythos_time(request: Request) -> dict[str, Any]:
    """Return the current Mythos calendar metadata for HUD initialization."""

    chronicle = get_mythos_chronicle()
    mythos_dt = chronicle.get_current_mythos_datetime()
    components = chronicle.get_calendar_components(mythos_dt)

    container = getattr(request.app.state, "container", None)
    holiday_service = getattr(container, "holiday_service", None) if container else None

    active_holidays: list[dict[str, Any]] = []
    upcoming_holidays: list[dict[str, Any]] = []

    if holiday_service:
        try:
            active_entries = holiday_service.refresh_active(mythos_dt)
            active_holidays = [_serialize_holiday(entry) for entry in active_entries]
            upcoming_entries = holiday_service.get_upcoming_holidays(3)
            upcoming_holidays = [_serialize_holiday(entry) for entry in upcoming_entries]
        except Exception as exc:  # pragma: no cover - defensive logging
            logger.warning("Failed to build holiday payload for /game/time", error=str(exc))

    payload = {
        "mythos_datetime": components.mythos_datetime.isoformat(),
        "mythos_clock": chronicle.format_clock(components.mythos_datetime),
        "month_name": components.month_name,
        "day_of_month": components.day_of_month,
        "day_name": components.day_name,
        "week_of_month": components.week_of_month,
        "season": components.season,
        "daypart": components.daypart,
        "is_daytime": components.is_daytime,
        "is_witching_hour": components.is_witching_hour,
        "server_timestamp": datetime.datetime.now(datetime.UTC).isoformat(),
        "active_holidays": active_holidays,
        "upcoming_holidays": upcoming_holidays,
    }

    logger.debug("Mythos time payload generated", **{k: payload[k] for k in ("mythos_clock", "daypart", "season")})
    return payload
