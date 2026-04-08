"""
WebSocket helper utilities for MythosMUD real-time communication.

This module contains utility functions used by the WebSocket handler.
"""

import json
import uuid
from collections.abc import Callable, Coroutine
from typing import TYPE_CHECKING, Protocol, cast

from fastapi import WebSocket, WebSocketDisconnect
from structlog.stdlib import BoundLogger

from ..structured_logging.enhanced_logging_config import get_logger

if TYPE_CHECKING:
    from ..models.player import Player


class _PlayerServiceContainer(Protocol):
    player_service: object | None


class _AppStateForPlayerService(Protocol):
    container: _PlayerServiceContainer | None
    player_service: object | None


logger: BoundLogger = get_logger(__name__)


def is_websocket_disconnect_message(error_message: str) -> bool:
    """Check if error message indicates WebSocket disconnection or send-after-close."""
    return (
        "WebSocket is not connected" in error_message
        or 'Need to call "accept" first' in error_message
        or "close message has been sent" in error_message
        or 'Cannot call "send"' in error_message
    )


def is_client_disconnected_exception(exc: BaseException) -> bool:
    """True if the exception indicates the client disconnected (tab close, navigate away, E2E)."""
    if isinstance(exc, WebSocketDisconnect):
        return True
    if isinstance(exc, RuntimeError):
        msg = str(exc)
        return "close message has been sent" in msg or 'Cannot call "send"' in msg
    return False


def get_npc_name_from_instance(npc_id: str) -> str | None:
    """
    Get NPC name from the actual NPC instance, preserving original case from database.

    This is the proper way to get NPC names - directly from the database via the NPC instance.

    Args:
        npc_id: The NPC ID

    Returns:
        NPC name from the database, or None if instance not found
    """
    try:
        # Get the NPC instance from the spawning service
        from ..services.npc_instance_service import get_npc_instance_service

        npc_instance_service = get_npc_instance_service()
        if hasattr(npc_instance_service, "lifecycle_manager"):
            lifecycle_manager = npc_instance_service.lifecycle_manager
            if lifecycle_manager and npc_id in lifecycle_manager.active_npcs:
                npc_instance = lifecycle_manager.active_npcs[npc_id]
                name = getattr(npc_instance, "name", None)
                return name if isinstance(name, str) else None

        return None
    except (ImportError, RuntimeError, AttributeError) as e:
        logger.debug("Error getting NPC name from instance", npc_id=npc_id, error=str(e))
        return None


async def check_shutdown_and_reject(websocket: WebSocket, player_id: uuid.UUID) -> bool:
    """Check if server is shutting down and reject connection if so. Returns True if rejected."""
    from ..commands.admin_shutdown_command import get_shutdown_blocking_message, is_shutdown_pending

    try:
        ws_app = cast(object | None, getattr(websocket, "app", None))
        if ws_app is not None and is_shutdown_pending(ws_app):
            error_message = get_shutdown_blocking_message("motd_progression")
            await websocket.send_json({"type": "error", "message": error_message})
            logger.info("DEBUG: Closing WebSocket due to server shutdown", player_id=player_id)
            await websocket.close(code=1001, reason="Server shutting down")
            logger.info("Rejected WebSocket connection - server shutting down", player_id=player_id)
            return True
    except (WebSocketDisconnect, RuntimeError, AttributeError) as e:
        logger.debug("Could not check shutdown status in WebSocket connection", error=str(e))
    return False


async def load_player_mute_data(player_id_str: str) -> None:
    """Load player mute data when they connect.

    AI: Uses async version to avoid blocking the event loop.
    """
    try:
        from ..services.user_manager import user_manager

        _ = await user_manager.load_player_mutes_async(player_id_str)
        logger.info("Loaded mute data", player_id=player_id_str)
    except (ImportError, RuntimeError, AttributeError) as e:
        logger.error("Error loading mute data", player_id=player_id_str, error=str(e))


def validate_occupant_name(name: object) -> bool:
    """Validate that a name is not a UUID string."""
    if not isinstance(name, str) or not name:
        return False
    is_uuid = len(name) == 36 and name.count("-") == 4 and all(c in "0123456789abcdefABCDEF-" for c in name)
    return not is_uuid


def _accumulate_valid_occupant_name(occ: dict[str, object], room_id: str, occupant_names: list[str]) -> None:
    """Parse one occupant row: append display name or log when it looks like a UUID."""
    raw = occ.get("player_name") or occ.get("name")
    name = raw if isinstance(raw, str) else None
    if not name:
        return
    if validate_occupant_name(name):
        occupant_names.append(name)
        return
    logger.warning("Skipping UUID as player name", name=name, room_id=room_id)


async def get_occupant_names(room_occupants: list[dict[str, object]], room_id: str) -> list[str]:
    """Extract and validate occupant names from room occupants list."""
    occupant_names: list[str] = []
    try:
        for occ in room_occupants or []:
            _accumulate_valid_occupant_name(occ, room_id, occupant_names)
    except (ImportError, RuntimeError, AttributeError) as e:
        logger.error("Error transforming occupants", room_id=room_id, error=str(e))
    return occupant_names


def convert_uuids_to_strings(obj: object) -> object:
    """Recursively convert UUID objects to strings for JSON serialization."""
    if isinstance(obj, dict):
        d = cast(dict[str, object], obj)
        return {k: convert_uuids_to_strings(v) for k, v in d.items()}
    if isinstance(obj, list):
        seq = cast(list[object], obj)
        return [convert_uuids_to_strings(item) for item in seq]
    if isinstance(obj, uuid.UUID):
        return str(obj)
    return obj


def get_player_service_from_connection_manager(connection_manager: object) -> object | None:
    """Extract player service from connection manager using container pattern."""
    app_state: object | None = None
    cm_app = cast(object | None, getattr(connection_manager, "app", None))
    if cm_app is not None and bool(cm_app):
        app_state = cast(object | None, getattr(cm_app, "state", None))

    if not app_state:
        return None

    st = cast(_AppStateForPlayerService, app_state)
    if st.container:
        return st.container.player_service
    return st.player_service


def convert_schema_to_dict(complete_player_data: object) -> dict[str, object]:
    """Convert Pydantic schema to dictionary."""
    model_dump = getattr(complete_player_data, "model_dump", None)
    if callable(model_dump):
        return cast(dict[str, object], model_dump(mode="json"))
    dict_meth = getattr(complete_player_data, "dict", None)
    if callable(dict_meth):
        return cast(dict[str, object], dict_meth())
    if isinstance(complete_player_data, dict):
        return cast(dict[str, object], complete_player_data)
    return {}


def get_player_stats_data(player: "Player | object") -> dict[str, object]:
    """Get and normalize player stats data."""
    stats_raw: object = {}
    if hasattr(player, "get_stats"):
        gs = getattr(player, "get_stats", None)
        if callable(gs):
            stats_raw = gs()
    if isinstance(stats_raw, str):
        stats_data = cast(dict[str, object], json.loads(stats_raw))
    elif isinstance(stats_raw, dict):
        stats_data = cast(dict[str, object], stats_raw)
    else:
        stats_data = {}
    if "health" not in stats_data and "current_dp" in stats_data:
        stats_data["health"] = stats_data.get("current_dp")
    return stats_data


def build_basic_player_data(player: "Player | object") -> dict[str, object]:
    """Build basic player data dictionary."""
    stats_data = get_player_stats_data(player)
    name = cast(str, getattr(player, "name", ""))
    return {
        "name": name,
        "level": cast(object, getattr(player, "level", 1)),
        "xp": cast(object, getattr(player, "experience_points", 0)),
        "stats": stats_data,
    }


async def prepare_player_data(
    player: "Player | object", player_id: uuid.UUID, connection_manager: object
) -> dict[str, object]:
    """Prepare complete player data with profession information for client."""
    try:
        player_service = get_player_service_from_connection_manager(connection_manager)

        if player_service is not None:
            convert_fn = getattr(player_service, "convert_player_to_schema", None)
            if callable(convert_fn):
                complete_player_data = await cast(Coroutine[None, None, object], convert_fn(player))
                player_data_for_client = convert_schema_to_dict(complete_player_data)
                if "experience_points" in player_data_for_client:
                    player_data_for_client["xp"] = player_data_for_client["experience_points"]
                return player_data_for_client

        logger.warning("PlayerService not available, using basic player data", player_id=player_id)
        return build_basic_player_data(player)
    except (ImportError, RuntimeError, AttributeError) as e:
        logger.error("Error getting complete player data", error=str(e), player_id=player_id, exc_info=True)
        return build_basic_player_data(player)


async def _get_tracked_player_from_connection_manager(
    connection_manager: object, player_id: uuid.UUID
) -> object | None:
    """Resolve the live player object from the connection manager (must expose current_room_id)."""
    get_player = getattr(connection_manager, "get_player", None)
    if not callable(get_player):
        return None
    player = await cast(Coroutine[None, None, object], get_player(player_id))
    if not player or not hasattr(player, "current_room_id"):
        return None
    return player


def _fetch_room_for_tracked_player(async_persistence: object, player: object) -> tuple[object, object] | None:
    """
    Load the room instance for the player's current_room_id.

    Returns:
        (room, current_room_id) or None if persistence cannot resolve a room.
    """
    get_room_by_id_raw = getattr(async_persistence, "get_room_by_id", None)
    if not callable(get_room_by_id_raw):
        return None
    fetch_room_by_id: Callable[[str], object] = cast(Callable[[str], object], get_room_by_id_raw)
    current_rid = cast(object | None, getattr(player, "current_room_id", None))
    if current_rid is None:
        return None
    # getattr + cast is opaque to pylint; runtime guarded by callable() above.
    room = fetch_room_by_id(str(current_rid))  # pylint: disable=not-callable
    if not room:
        return None
    return room, current_rid


def _ensure_player_in_room_occupancy(
    room: object,
    *,
    player_id_str: str,
    player_id: uuid.UUID,
    current_rid: object,
) -> None:
    """If the room tracks occupancy, register the player when missing."""
    has_player_raw = getattr(room, "has_player", None)
    if not callable(has_player_raw):
        return
    has_player_fn: Callable[[str], object] = cast(Callable[[str], object], has_player_raw)
    if has_player_fn(player_id_str):  # pylint: disable=not-callable
        return
    logger.info("Adding player to room", player_id=player_id, room_id=str(current_rid))
    player_entered_raw = getattr(room, "player_entered", None)
    if callable(player_entered_raw):
        player_entered_fn: Callable[[str], object] = cast(Callable[[str], object], player_entered_raw)
        _ = player_entered_fn(player_id_str)  # pylint: disable=not-callable


async def get_player_and_room(
    player_id: uuid.UUID, player_id_str: str, connection_manager: object
) -> tuple[object | None, object | None, str | None]:
    """
    Get and validate player and room for initial game state.

    Returns:
        Tuple of (player, room, canonical_room_id) or (None, None, None) if not found
    """
    player = await _get_tracked_player_from_connection_manager(connection_manager, player_id)
    if player is None:
        return None, None, None

    from ..async_persistence import get_async_persistence

    async_persistence = get_async_persistence()
    if not async_persistence:
        return None, None, None

    room_bundle = _fetch_room_for_tracked_player(async_persistence, player)
    if room_bundle is None:
        return None, None, None
    room, current_rid = room_bundle

    _ensure_player_in_room_occupancy(room, player_id_str=player_id_str, player_id=player_id, current_rid=current_rid)

    canonical_raw = cast(object | None, getattr(room, "id", None)) or current_rid
    canonical_room_id = str(canonical_raw) if canonical_raw is not None else None
    return player, room, canonical_room_id
