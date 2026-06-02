"""
WebSocket initial state preparation for MythosMUD real-time communication.

This module handles sending initial game state to connecting players.
"""

# pylint: disable=too-many-arguments,too-many-positional-arguments  # Reason: Initial state preparation requires many parameters for complete game state context

import uuid
from collections.abc import Mapping
from typing import TYPE_CHECKING, Protocol, cast

from fastapi import WebSocket
from starlette.websockets import WebSocketDisconnect

from ..models.room import Room
from ..structured_logging.enhanced_logging_config import get_logger
from ..utils.int_coercion import coerce_int
from .envelope import build_event
from .websocket_helpers import (
    convert_uuids_to_strings,
    get_occupant_names,
    get_player_and_room,
    prepare_player_data,
)

if TYPE_CHECKING:
    from ..models.player import Player
    from .connection_manager import ConnectionManager
    from .event_handler import RealTimeEventHandler

logger = get_logger(__name__)


class _RealTimeHandlerContainer(Protocol):
    """Minimal app.state.container shape for resolving the real-time event handler."""

    real_time_event_handler: "RealTimeEventHandler | None"


class _AppWithState(Protocol):
    """Minimal FastAPI/Starlette app shape for reading ``state``."""

    state: object


class _AppStateForEventHandler(Protocol):
    """Minimal app.state shape for resolving the real-time event handler."""

    container: _RealTimeHandlerContainer | None
    event_handler: "RealTimeEventHandler | None"


class _NpcOccupantDisplay(Protocol):
    """Minimal NPC instance shape for room occupant name display."""

    name: str


class _NpcLifecycleManagerForOccupants(Protocol):
    """Minimal lifecycle manager shape for listing NPC names in a room."""

    active_npcs: Mapping[str, _NpcOccupantDisplay]


class _ContainerWithNpcLifecycle(Protocol):
    """Minimal app.state.container shape for resolving the NPC lifecycle manager."""

    npc_lifecycle_manager: _NpcLifecycleManagerForOccupants | None


class _AppStateWithNpcLifecycle(Protocol):
    """Minimal app.state shape for resolving the NPC lifecycle manager."""

    container: _ContainerWithNpcLifecycle | None
    npc_lifecycle_manager: _NpcLifecycleManagerForOccupants | None


async def prepare_room_data_with_occupants(
    room: "Room | dict[str, object]", canonical_room_id: str, connection_manager: "ConnectionManager"
) -> tuple[dict[str, object], list[str]]:
    """Prepare room data and get occupant names."""
    room_occupants = await connection_manager.get_room_occupants(str(canonical_room_id))
    occupant_names = await get_occupant_names(room_occupants, str(canonical_room_id))

    room_data = room if isinstance(room, dict) else room.to_dict()
    room_data = await connection_manager.convert_room_players_uuids_to_names(room_data)
    room_data = cast(dict[str, object], convert_uuids_to_strings(room_data))

    return room_data, occupant_names


async def send_game_state_event_safely(
    websocket: WebSocket, game_state_event: dict[str, object], player_id_str: str
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

        room_typed = cast("Room | dict[str, object]", room)
        room_data, occupant_names = await prepare_room_data_with_occupants(
            room_typed, canonical_room_id, connection_manager
        )
        # Ensure the connecting player is always in occupants (they may not be in room_occupants yet)
        from .websocket_helpers import validate_occupant_name

        player_name = getattr(player, "name", None)
        if isinstance(player_name, str) and validate_occupant_name(player_name) and player_name not in occupant_names:
            occupant_names.append(player_name)

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


def _get_death_location_name(room: Room | dict[str, object]) -> str:
    """Extract death location name from room object or dict."""
    if isinstance(room, dict):
        name = room.get("name")
        return str(name) if name is not None else "Unknown Location"
    room_name = cast(object, room.name)
    if isinstance(room_name, str):
        return room_name
    return "Unknown Location"


async def _get_player_for_death_check(
    player_id: uuid.UUID, connection_manager: "ConnectionManager"
) -> tuple["Player", str | None] | None:
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
    room: "Room | dict[str, object]",
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
    current_dp = coerce_int(stats.get("current_dp"), default=20)

    # Only send death notification when player is actually dead (DP <= -10).
    # Do not send based on limbo alone: player must only be in limbo at -10 DP, so if they are
    # in limbo with DP > -10 that is an invalid state; avoid showing respawn modal at 0 DP.
    if current_dp <= -10:
        death_location_name = _get_death_location_name(room)
        death_event = build_event(
            "player_died",
            {
                "player_id": player_id_str,
                "player_name": player.name,
                "death_location": death_location_name,
                "message": "You have died. The darkness claims you utterly.",
                "current_dp": current_dp,
            },
            player_id=player_id_str,
        )
        if await send_game_state_event_safely(websocket, death_event, player_id_str):
            return
        logger.info(
            "Sent death notification to player on login",
            player_id=player_id_str,
            current_dp=current_dp,
            in_limbo=str(canonical_room_id) == LIMBO_ROOM_ID,
        )


def _get_npc_lifecycle_manager_from_connection_manager(
    connection_manager: "ConnectionManager",
) -> _NpcLifecycleManagerForOccupants | None:
    """Resolve NPC lifecycle manager from connection manager app state."""
    app = cast(object | None, getattr(connection_manager, "app", None))
    if app is None:
        return None
    app_state = cast(_AppStateWithNpcLifecycle, cast(_AppWithState, app).state)
    # Prefer container, fallback to app.state for backward compatibility
    if app_state.container is not None:
        return app_state.container.npc_lifecycle_manager
    return app_state.npc_lifecycle_manager


async def add_npc_occupants_to_list(
    room: "Room", occupant_names: list[str], canonical_room_id: str, connection_manager: "ConnectionManager"
) -> None:
    """Add NPC occupants to the occupant names list."""
    npc_lifecycle_manager = _get_npc_lifecycle_manager_from_connection_manager(connection_manager)
    if not npc_lifecycle_manager:
        return
    for npc_id in room.get_npcs():
        npc = npc_lifecycle_manager.active_npcs.get(npc_id)
        if npc is None:
            continue
        occupant_names.append(npc.name)
        logger.info(
            "Added NPC to room occupants display",
            npc_name=npc.name,
            npc_id=npc_id,
            room_id=canonical_room_id,
        )


async def prepare_initial_room_data(
    room: "Room | dict[str, object]", connection_manager: "ConnectionManager"
) -> dict[str, object]:
    """Prepare room data for initial state event."""
    room_data_for_update = room if isinstance(room, dict) else room.to_dict()
    room_data_for_update = await connection_manager.convert_room_players_uuids_to_names(room_data_for_update)
    return cast(dict[str, object], room_data_for_update)


def _get_event_handler_from_app_host(
    host: "ConnectionManager | WebSocket",
) -> "RealTimeEventHandler | None":
    """Resolve real-time event handler from a connection manager or websocket app."""
    app = cast(object | None, host.app)
    if app is None:
        return None
    app_state = cast(_AppStateForEventHandler, cast(_AppWithState, app).state)
    # Prefer container, fallback to app.state for backward compatibility
    if app_state.container is not None:
        return app_state.container.real_time_event_handler
    return app_state.event_handler


def get_event_handler_for_initial_state(
    connection_manager: "ConnectionManager", websocket: WebSocket
) -> "RealTimeEventHandler | None":
    """Get event handler from connection manager or websocket app state."""
    event_handler = _get_event_handler_from_app_host(connection_manager)
    if event_handler:
        return event_handler
    return _get_event_handler_from_app_host(websocket)


async def send_occupants_snapshot_if_needed(
    event_handler: "RealTimeEventHandler | None",
    room: "Room",
    player_id: uuid.UUID,
    player_id_str: str,
    canonical_room_id: str,
) -> None:
    """Send occupants snapshot if event handler is available (include connecting player via ensure_player_included)."""
    if not event_handler or not room:
        return
    # Always send snapshot so connecting player is included (they may not be in room._players yet)
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
        # Ensure the connecting player is in occupants (they may not be in room_occupants yet)
        from .websocket_helpers import validate_occupant_name

        connecting_player = await connection_manager.get_player(player_id)
        if connecting_player:
            player_name = connecting_player.name
            if validate_occupant_name(player_name) and player_name not in occupant_names:
                occupant_names.append(player_name)

        room_data_for_update = await prepare_initial_room_data(room, connection_manager)

        initial_state = build_event(
            "room_update",
            {"room": room_data_for_update, "entities": [], "occupants": occupant_names},
            player_id=player_id_str,
        )
        if await send_game_state_event_safely(websocket, initial_state, player_id_str):
            return
        logger.debug(
            "Sent initial room state to connecting player", player_id=player_id_str, occupants_sent=occupant_names
        )

        event_handler = get_event_handler_for_initial_state(connection_manager, websocket)
        await send_occupants_snapshot_if_needed(event_handler, room, player_id, player_id_str, canonical_room_id)

    except (AttributeError, KeyError, ValueError, TypeError, RuntimeError) as e:
        logger.error("Error sending initial room state", player_id=player_id, error=str(e), exc_info=True)
