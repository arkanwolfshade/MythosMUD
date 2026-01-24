"""
WebSocket initial state preparation for MythosMUD real-time communication.

This module handles sending initial game state to connecting players.
"""

# pylint: disable=too-many-arguments,too-many-positional-arguments  # Reason: Initial state preparation requires many parameters for complete game state context

import uuid
from typing import TYPE_CHECKING, Any, cast

from fastapi import WebSocket
from starlette.websockets import WebSocketDisconnect

from ..structured_logging.enhanced_logging_config import get_logger
from .envelope import build_event
from .websocket_helpers import (
    convert_uuids_to_strings,
    get_occupant_names,
    get_player_and_room,
    prepare_player_data,
)

if TYPE_CHECKING:
    from ..models.room import Room
    from .connection_manager import ConnectionManager

logger = get_logger(__name__)


async def prepare_room_data_with_occupants(
    room: "Room | dict[str, Any]", canonical_room_id: str, connection_manager: "ConnectionManager"
) -> tuple[dict[str, Any], list[str]]:
    """Prepare room data and get occupant names."""
    room_occupants = await connection_manager.get_room_occupants(str(canonical_room_id))
    occupant_names = await get_occupant_names(room_occupants, str(canonical_room_id))

    room_data = room.to_dict() if hasattr(room, "to_dict") else room
    if isinstance(room_data, dict):
        room_data = await connection_manager.convert_room_players_uuids_to_names(room_data)
    room_data = convert_uuids_to_strings(room_data)

    return room_data, occupant_names


async def send_game_state_event_safely(
    websocket: WebSocket, game_state_event: dict[str, Any], player_id_str: str
) -> bool:
    """
    Send game state event with proper error handling.

    Returns:
        True if should exit (WebSocket disconnected), False otherwise
    """
    from starlette.websockets import WebSocketState

    ws_state = getattr(websocket, "application_state", None)
    if ws_state == WebSocketState.DISCONNECTED:
        # WebSocket already disconnected - this is expected during cleanup, no need to warn
        logger.debug("WebSocket already disconnected, skipping game_state send", player_id=player_id_str)
        return True

    try:
        await websocket.send_json(game_state_event)
        return False
    except (RuntimeError, WebSocketDisconnect) as send_err:
        error_message = str(send_err)
        if "close message has been sent" in error_message or "Cannot call" in error_message:
            logger.warning(
                "WebSocket closed during send, exiting connection handler",
                player_id=player_id_str,
                error=error_message,
            )
            return True
        # WebSocketDisconnect means connection is closed
        if isinstance(send_err, WebSocketDisconnect):
            logger.debug("WebSocket disconnected during game state send", player_id=player_id_str)
            return True
        raise


async def send_initial_game_state(
    websocket: WebSocket, player_id: uuid.UUID, player_id_str: str, connection_manager: "ConnectionManager"
) -> tuple[str | None, bool]:
    """
    Send initial game state to connecting player.
    Returns tuple of (canonical_room_id, should_exit).
    """
    try:
        player, room, canonical_room_id = await get_player_and_room(player_id, player_id_str, connection_manager)
        if not player or not room or not canonical_room_id:
            return None, False

        room_data, occupant_names = await prepare_room_data_with_occupants(room, canonical_room_id, connection_manager)

        player_data_for_client = await prepare_player_data(player, player_id, connection_manager)

        game_state_event = build_event(
            "game_state",
            {
                "player": player_data_for_client,
                "room": room_data,
                "occupants": occupant_names,
                "occupant_count": len(occupant_names),
            },
            player_id=player_id_str,
            room_id=str(canonical_room_id),
        )

        should_exit = await send_game_state_event_safely(websocket, game_state_event, player_id_str)
        return canonical_room_id, should_exit

    except (AttributeError, KeyError, ValueError, TypeError, RuntimeError) as e:
        logger.error("Error sending initial game state", player_id=player_id, error=str(e), exc_info=True)
        return None, False


def _get_death_location_name(room: "Room | dict[str, Any]") -> str:
    """Extract death location name from room object or dict."""
    if isinstance(room, dict):
        name = room.get("name")
        return str(name) if name is not None else "Unknown Location"
    if hasattr(room, "name"):
        name = getattr(room, "name", None)
        return str(name) if name is not None else "Unknown Location"
    return "Unknown Location"


async def _get_player_for_death_check(
    player_id: uuid.UUID, connection_manager: "ConnectionManager"
) -> tuple[Any, str | None] | None:
    """Get player and updated room ID for death check."""
    from ..async_persistence import get_async_persistence

    async_persistence = get_async_persistence()
    fresh_player = await async_persistence.get_player_by_id(player_id)
    if fresh_player:
        canonical_room_id = str(fresh_player.current_room_id) if hasattr(fresh_player, "current_room_id") else None
        return fresh_player, canonical_room_id

    player_result = await connection_manager.get_player(player_id)
    if not player_result:
        return None
    return player_result, None


async def check_and_send_death_notification(  # pylint: disable=too-many-arguments,too-many-positional-arguments  # Reason: Death notification requires many parameters for context and notification logic
    websocket: WebSocket,
    player_id: uuid.UUID,
    player_id_str: str,
    canonical_room_id: str,
    room: "Room | dict[str, Any]",
    connection_manager: "ConnectionManager",
) -> None:
    """Check if player is dead and send death notification if needed."""
    from ..services.player_respawn_service import LIMBO_ROOM_ID

    player_result = await _get_player_for_death_check(player_id, connection_manager)
    if not player_result:
        return
    player, updated_room_id = player_result
    if updated_room_id:
        canonical_room_id = updated_room_id

    stats = player.get_stats() if hasattr(player, "get_stats") else {}
    current_dp = stats.get("current_dp", 20) if isinstance(stats.get("current_dp"), int) else 20

    if current_dp <= -10 or str(canonical_room_id) == LIMBO_ROOM_ID:
        death_location_name = _get_death_location_name(room)
        death_event = build_event(
            "player_died",
            {
                "player_id": player_id_str,
                "player_name": player.name,
                "death_location": death_location_name,
                "message": "You have died. The darkness claims you utterly.",
            },
            player_id=player_id_str,
        )
        await websocket.send_json(death_event)
        logger.info(
            "Sent death notification to player on login",
            player_id=player_id_str,
            current_dp=current_dp,
            in_limbo=str(canonical_room_id) == LIMBO_ROOM_ID,
        )


async def add_npc_occupants_to_list(
    room: "Room", occupant_names: list[str], canonical_room_id: str, connection_manager: "ConnectionManager"
) -> None:
    """Add NPC occupants to the occupant names list."""
    if not hasattr(connection_manager, "app"):
        return

    # Prefer container, fallback to app.state for backward compatibility
    npc_lifecycle_manager = None
    if hasattr(connection_manager.app.state, "container") and connection_manager.app.state.container:
        npc_lifecycle_manager = connection_manager.app.state.container.npc_lifecycle_manager
    elif hasattr(connection_manager.app.state, "npc_lifecycle_manager"):
        npc_lifecycle_manager = connection_manager.app.state.npc_lifecycle_manager

    if not npc_lifecycle_manager:
        return
    npc_ids = room.get_npcs()
    for npc_id in npc_ids:
        npc = npc_lifecycle_manager.active_npcs.get(npc_id)
        if npc and hasattr(npc, "name"):
            occupant_names.append(npc.name)
            logger.info(
                "Added NPC to room occupants display",
                npc_name=npc.name,
                npc_id=npc_id,
                room_id=canonical_room_id,
            )


async def prepare_initial_room_data(
    room: "Room | dict[str, Any]", connection_manager: "ConnectionManager"
) -> dict[str, Any]:
    """Prepare room data for initial state event."""
    room_data_for_update = room.to_dict() if hasattr(room, "to_dict") else room
    if isinstance(room_data_for_update, dict):
        room_data_for_update = await connection_manager.convert_room_players_uuids_to_names(room_data_for_update)
    return cast(dict[str, Any], room_data_for_update)


def get_event_handler_for_initial_state(connection_manager: "ConnectionManager", websocket: WebSocket) -> Any:
    """Get event handler from connection manager or websocket app state."""
    # Prefer container, fallback to app.state for backward compatibility
    event_handler = None
    if hasattr(connection_manager, "app") and connection_manager.app:
        if hasattr(connection_manager.app.state, "container") and connection_manager.app.state.container:
            event_handler = connection_manager.app.state.container.real_time_event_handler
        else:
            event_handler = getattr(connection_manager.app.state, "event_handler", None)
    if not event_handler and hasattr(websocket, "app") and websocket.app:
        if hasattr(websocket.app.state, "container") and websocket.app.state.container:
            event_handler = websocket.app.state.container.real_time_event_handler
        else:
            event_handler = getattr(websocket.app.state, "event_handler", None)
    return event_handler


async def send_occupants_snapshot_if_needed(
    event_handler: Any, room: "Room", player_id: uuid.UUID, player_id_str: str, canonical_room_id: str
) -> None:
    """Send occupants snapshot if event handler is available and player is in room."""
    if not event_handler:
        return
    if not hasattr(event_handler, "player_handler"):
        return
    if not hasattr(event_handler.player_handler, "send_occupants_snapshot_to_player"):
        return
    if not room or not room.has_player(player_id_str):
        return

    await event_handler.player_handler.send_occupants_snapshot_to_player(player_id, str(canonical_room_id))
    logger.debug(
        "Sent room_occupants event to connecting player",
        player_id=player_id_str,
        room_id=str(canonical_room_id),
    )


async def send_initial_room_state(
    websocket: WebSocket,
    player_id: uuid.UUID,
    player_id_str: str,
    canonical_room_id: str,
    connection_manager: "ConnectionManager",
) -> None:
    """Send initial room state and occupants snapshot to connecting player."""
    try:
        from ..async_persistence import get_async_persistence

        async_persistence = get_async_persistence()
        room = async_persistence.get_room_by_id(canonical_room_id)
        if not room:
            return

        room_occupants = await connection_manager.get_room_occupants(str(canonical_room_id))
        occupant_names = await get_occupant_names(room_occupants, canonical_room_id)

        await add_npc_occupants_to_list(room, occupant_names, canonical_room_id, connection_manager)

        room_data_for_update = await prepare_initial_room_data(room, connection_manager)

        initial_state = build_event(
            "room_update",
            {"room": room_data_for_update, "entities": [], "occupants": occupant_names},
            player_id=player_id_str,
        )
        await websocket.send_json(initial_state)
        logger.debug(
            "Sent initial room state to connecting player", player_id=player_id_str, occupants_sent=occupant_names
        )

        event_handler = get_event_handler_for_initial_state(connection_manager, websocket)
        await send_occupants_snapshot_if_needed(event_handler, room, player_id, player_id_str, canonical_room_id)

    except (AttributeError, KeyError, ValueError, TypeError, RuntimeError) as e:
        logger.error("Error sending initial room state", player_id=player_id, error=str(e), exc_info=True)
