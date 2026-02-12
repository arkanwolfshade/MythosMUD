"""
Game mechanics API endpoints for MythosMUD server.

This module handles all game mechanics-related API operations including
game status, broadcasting, and real-time game state management.
"""

import datetime
from typing import TYPE_CHECKING

from fastapi import APIRouter, Depends

from ..auth.dependencies import get_current_superuser
from ..dependencies import ConnectionManagerDep, get_container
from ..models.user import User
from ..schemas.calendar import HolidayEntry
from ..schemas.game import BroadcastMessageResponse, GameStatusResponse, MythosTimeResponse
from ..structured_logging.enhanced_logging_config import get_logger
from ..time.time_service import get_mythos_chronicle

if TYPE_CHECKING:
    from ..container import ApplicationContainer
    from ..realtime.connection_manager import ConnectionManager

logger = get_logger(__name__)

# Create game router
game_router = APIRouter(prefix="/game", tags=["game"])

logger.info("Game API router initialized", prefix="/game")


@game_router.get("/status", response_model=GameStatusResponse)
def get_game_status(connection_manager: "ConnectionManager" = ConnectionManagerDep) -> GameStatusResponse:
    """Get current game status and connection information."""
    logger.debug("Game status requested")

    status_data = GameStatusResponse(
        active_connections=connection_manager.get_active_connection_count(),
        active_players=len(connection_manager.player_websockets),
        room_subscriptions=len(connection_manager.room_manager.room_subscriptions),
        server_time=datetime.datetime.now(datetime.UTC).isoformat(),
    )

    logger.debug(
        "Game status returned",
        active_connections=status_data.active_connections,
        active_players=status_data.active_players,
        room_subscriptions=status_data.room_subscriptions,
    )

    return status_data


@game_router.post("/broadcast", response_model=BroadcastMessageResponse)
async def broadcast_message(
    message: str,
    current_user: User = Depends(get_current_superuser),
    connection_manager: "ConnectionManager" = ConnectionManagerDep,
) -> BroadcastMessageResponse:
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

    # Convert broadcast_stats dict to BroadcastStats model
    from server.schemas.game.game import BroadcastStats

    broadcast_stats_model = BroadcastStats(
        successful_deliveries=broadcast_stats.get("successful_deliveries", 0),
        failed_deliveries=broadcast_stats.get("failed_deliveries", 0),
        total_recipients=broadcast_stats.get("total_recipients", recipients),
    )

    return BroadcastMessageResponse(
        message=message,
        recipients=recipients,
        broadcaster=current_user.username,
        broadcast_stats=broadcast_stats_model,
    )


@game_router.get("/time", response_model=MythosTimeResponse)
def get_mythos_time(container: "ApplicationContainer" = Depends(get_container)) -> MythosTimeResponse:
    """Return the current Mythos calendar metadata for HUD initialization."""

    chronicle = get_mythos_chronicle()
    mythos_dt = chronicle.get_current_mythos_datetime()
    components = chronicle.get_calendar_components(mythos_dt)

    holiday_service = getattr(container, "holiday_service", None) if container else None

    active_holidays: list[HolidayEntry] = []
    upcoming_holidays: list[HolidayEntry] = []

    if holiday_service:
        try:
            # Use service methods that handle serialization internally
            active_holidays = holiday_service.get_serialized_active_holidays(mythos_dt)
            upcoming_holidays = holiday_service.get_serialized_upcoming_holidays(3)
        except Exception as exc:  # noqa: B904  # pragma: no cover - defensive logging  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Holiday service errors unpredictable, optional metadata
            logger.warning("Failed to build holiday payload for /game/time", error=str(exc))

    payload = MythosTimeResponse(
        mythos_datetime=components.mythos_datetime.isoformat(),
        mythos_clock=chronicle.format_clock(components.mythos_datetime),
        month_name=components.month_name,
        day_of_month=components.day_of_month,
        day_name=components.day_name,
        week_of_month=components.week_of_month,
        season=components.season,
        daypart=components.daypart,
        is_daytime=components.is_daytime,
        is_witching_hour=components.is_witching_hour,
        server_timestamp=datetime.datetime.now(datetime.UTC).isoformat(),
        active_holidays=active_holidays,
        upcoming_holidays=upcoming_holidays,
    )

    logger.debug(
        "Mythos time payload generated",
        mythos_clock=payload.mythos_clock,
        daypart=payload.daypart,
        season=payload.season,
    )
    return payload
