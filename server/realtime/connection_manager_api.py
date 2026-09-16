"""
Public API utility functions for connection manager.

This module provides convenient wrapper functions for sending events
through the connection manager without requiring direct access to the
ConnectionManager instance.
"""

import uuid
from collections.abc import Awaitable, Mapping
from typing import Protocol, cast
from uuid import UUID

from ..exceptions import DatabaseError
from ..structured_logging.enhanced_logging_config import get_logger
from .connection_manager_utils import resolve_connection_manager

logger = get_logger(__name__)


class _ConnectionManagerAPI(Protocol):
    """Structural type for API helpers; avoids importing ConnectionManager."""

    # pylint: disable=missing-function-docstring  # Reason: Protocol stubs; docs live on ConnectionManager

    online_players: dict[UUID, dict[str, object]]

    def send_personal_message(self, player_id: UUID, event: object) -> Awaitable[object]: ...

    def broadcast_global(self, event: object, exclude_player: str | None = None) -> Awaitable[object]: ...

    def broadcast_to_room(
        self, room_id: str, event: object, exclude_player: str | None = None
    ) -> Awaitable[object]: ...


class ConnectionManagerUnavailable(RuntimeError):
    """Raised when no connection manager can be resolved.

    Deliberately a plain RuntimeError and NOT a MythosMUDError: that base class logs at
    ERROR in its constructor (see MythosMUDError._log_error in ../exceptions.py), which
    would defeat the point of handling this at warning level below. Do not reparent it
    into the MythosMUDError tree.
    """


def _require_manager() -> _ConnectionManagerAPI:
    """Resolve manager without importing ConnectionManager (import cycle)."""
    manager = resolve_connection_manager()
    if manager is None:
        raise ConnectionManagerUnavailable("Connection manager not available")
    return cast(_ConnectionManagerAPI, manager)


def remove_online_player(player_id: uuid.UUID) -> None:
    """
    Drop a player from the live online-players roster, best-effort.

    Call this the moment a character is deleted while still connected. Without it, the
    game-tick loop keeps regenerating MP/lucidity for the stale roster entry every tick and
    each attempted save is refused by the soft-delete guard (#777) -- one warning, with a full
    stack trace, per player per tick, forever (or until they happen to disconnect).

    A missing manager is not an error here either (see the send/broadcast helpers below,
    which now also treat it as non-fatal): deletion can run in contexts with no live
    connection manager (unit tests, offline tooling, startup), and it must still succeed.
    """
    manager = resolve_connection_manager()
    if manager is None:
        return
    _ = cast(_ConnectionManagerAPI, manager).online_players.pop(player_id, None)


async def send_game_event(player_id: uuid.UUID | str, event_type: str, data: Mapping[str, object]) -> None:
    """
    Send a game event to a specific player via WebSocket.

    Args:
        player_id: The player's ID (UUID or string)
        event_type: The type of event
        data: The event data
    """
    try:
        from .envelope import build_event

        manager = _require_manager()
        # Convert player_id to UUID if it's a string
        if isinstance(player_id, str):
            try:
                player_id_uuid = uuid.UUID(player_id)
            except (ValueError, AttributeError):
                logger.error("Invalid player_id format", player_id=player_id)
                return
        else:
            player_id_uuid = player_id
        # Pass UUID object directly to build_event (it accepts UUID | str)
        _ = await manager.send_personal_message(player_id_uuid, build_event(event_type, data, player_id=player_id_uuid))

    except ConnectionManagerUnavailable:
        logger.warning(
            "Skipping game event; connection manager unavailable",
            player_id=player_id,
            event_type=event_type,
        )
    except (DatabaseError, AttributeError) as e:
        logger.error("Error sending game event", player_id=player_id, error=str(e))


async def broadcast_game_event(event_type: str, data: Mapping[str, object], exclude_player: str | None = None) -> None:
    """
    Broadcast a game event to all connected players.

    Args:
        event_type: The type of event
        data: The event data
        exclude_player: Player ID to exclude from broadcast
    """
    try:
        from .envelope import build_event

        manager = _require_manager()
        _ = await manager.broadcast_global(build_event(event_type, data), exclude_player)

    except ConnectionManagerUnavailable:
        logger.warning("Skipping game event broadcast; connection manager unavailable", event_type=event_type)
    except (DatabaseError, AttributeError) as e:
        logger.error("Error broadcasting game event", error=str(e))


async def send_room_event(
    room_id: str, event_type: str, data: Mapping[str, object], exclude_player: str | None = None
) -> None:
    """
    Send a room event to all players in a specific room.

    Args:
        room_id: The room's ID
        event_type: The type of event
        data: The event data
        exclude_player: Player ID to exclude from broadcast
    """
    try:
        from .envelope import build_event

        manager = _require_manager()
        _ = await manager.broadcast_to_room(
            room_id,
            build_event(event_type, data, room_id=room_id),
            exclude_player,
        )

    except ConnectionManagerUnavailable:
        logger.warning(
            "Skipping room event; connection manager unavailable",
            room_id=room_id,
            event_type=event_type,
        )
    except (DatabaseError, AttributeError) as e:
        logger.error("Error sending room event", room_id=room_id, error=str(e))


async def send_system_notification(player_id: uuid.UUID | str, message: str, notification_type: str = "info") -> None:
    """
    Send a system notification to a player.

    Args:
        player_id: The player's ID
        message: The notification message
        notification_type: The type of notification (info, warning, error)
    """
    try:
        notification_data = {
            "message": message,
            "notification_type": notification_type,
        }

        await send_game_event(player_id, "system_notification", notification_data)

    except (DatabaseError, AttributeError) as e:
        logger.error("Error sending system notification", player_id=player_id, error=str(e))


async def send_player_status_update(player_id: uuid.UUID | str, status_data: Mapping[str, object]) -> None:
    """
    Send a player status update to a player.

    Args:
        player_id: The player's ID
        status_data: The status data to send
    """
    try:
        await send_game_event(player_id, "player_status", status_data)

    except (DatabaseError, AttributeError) as e:
        logger.error("Error sending status update", player_id=player_id, error=str(e))


async def send_room_description(player_id: uuid.UUID | str, room_data: Mapping[str, object]) -> None:
    """
    Send room description to a player.

    Args:
        player_id: The player's ID
        room_data: The room data to send
    """
    try:
        await send_game_event(player_id, "room_description", room_data)

    except (DatabaseError, AttributeError) as e:
        logger.error("Error sending room description", player_id=player_id, error=str(e))
