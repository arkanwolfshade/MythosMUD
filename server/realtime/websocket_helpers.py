"""
WebSocket helper utilities for MythosMUD real-time communication.

This module contains utility functions used by the WebSocket handler.
"""

import json
import uuid
from typing import Any

from fastapi import WebSocket, WebSocketDisconnect

from ..logging.enhanced_logging_config import get_logger

logger = get_logger(__name__)


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
                return name

        return None
    except (ImportError, RuntimeError, AttributeError) as e:
        logger.debug("Error getting NPC name from instance", npc_id=npc_id, error=str(e))
        return None


async def check_shutdown_and_reject(websocket: WebSocket, player_id: uuid.UUID) -> bool:
    """Check if server is shutting down and reject connection if so. Returns True if rejected."""
    from ..commands.admin_shutdown_command import get_shutdown_blocking_message, is_shutdown_pending

    try:
        if hasattr(websocket, "app") and is_shutdown_pending(websocket.app):
            error_message = get_shutdown_blocking_message("motd_progression")
            await websocket.send_json({"type": "error", "message": error_message})
            logger.info("DEBUG: Closing WebSocket due to server shutdown", player_id=player_id)
            await websocket.close(code=1001, reason="Server shutting down")
            logger.info("Rejected WebSocket connection - server shutting down", player_id=player_id)
            return True
    except (WebSocketDisconnect, RuntimeError, AttributeError) as e:
        logger.debug("Could not check shutdown status in WebSocket connection", error=str(e))
    return False


def load_player_mute_data(player_id_str: str) -> None:
    """Load player mute data when they connect."""
    try:
        from ..services.user_manager import user_manager

        user_manager.load_player_mutes(player_id_str)
        logger.info("Loaded mute data", player_id=player_id_str)
    except (ImportError, RuntimeError, AttributeError) as e:
        logger.error("Error loading mute data", player_id=player_id_str, error=str(e))


def validate_occupant_name(name: str) -> bool:
    """Validate that a name is not a UUID string."""
    if not name or not isinstance(name, str):
        return False
    is_uuid = len(name) == 36 and name.count("-") == 4 and all(c in "0123456789abcdefABCDEF-" for c in name)
    return not is_uuid


async def get_occupant_names(room_occupants: list[dict[str, Any]], room_id: str) -> list[str]:
    """Extract and validate occupant names from room occupants list."""
    occupant_names = []
    try:
        for occ in room_occupants or []:
            name = occ.get("player_name") or occ.get("name")
            if name and validate_occupant_name(name):
                occupant_names.append(name)
            elif name:
                logger.warning("Skipping UUID as player name", name=name, room_id=room_id)
    except (ImportError, RuntimeError, AttributeError) as e:
        logger.error("Error transforming occupants", room_id=room_id, error=str(e))
    return occupant_names


def convert_uuids_to_strings(obj: Any) -> Any:
    """Recursively convert UUID objects to strings for JSON serialization."""
    if isinstance(obj, dict):
        return {k: convert_uuids_to_strings(v) for k, v in obj.items()}
    elif isinstance(obj, list):
        return [convert_uuids_to_strings(item) for item in obj]
    elif hasattr(obj, "__class__") and "UUID" in obj.__class__.__name__:
        return str(obj)
    else:
        return obj


def get_player_service_from_connection_manager(connection_manager) -> Any:
    """Extract player service from connection manager."""
    app_state = None
    if hasattr(connection_manager, "app") and connection_manager.app:
        app_state = getattr(connection_manager.app, "state", None)
    return getattr(app_state, "player_service", None) if app_state else None


def convert_schema_to_dict(complete_player_data: Any) -> dict[str, Any]:
    """Convert Pydantic schema to dictionary."""
    if hasattr(complete_player_data, "model_dump"):
        return complete_player_data.model_dump(mode="json")
    return complete_player_data.dict()


def get_player_stats_data(player) -> dict[str, Any]:
    """Get and normalize player stats data."""
    stats_data = player.get_stats() if hasattr(player, "get_stats") else {}
    if isinstance(stats_data, str):
        stats_data = json.loads(stats_data)
    if "health" not in stats_data and "current_db" in stats_data:
        stats_data["health"] = stats_data.get("current_db")
    return stats_data


def build_basic_player_data(player) -> dict[str, Any]:
    """Build basic player data dictionary."""
    stats_data = get_player_stats_data(player)
    return {
        "name": player.name,
        "level": getattr(player, "level", 1),
        "xp": getattr(player, "experience_points", 0),
        "stats": stats_data,
    }


async def prepare_player_data(player, player_id: uuid.UUID, connection_manager) -> dict[str, Any]:
    """Prepare complete player data with profession information for client."""
    try:
        player_service = get_player_service_from_connection_manager(connection_manager)

        if player_service:
            complete_player_data = await player_service.convert_player_to_schema(player)
            player_data_for_client = convert_schema_to_dict(complete_player_data)
            if "experience_points" in player_data_for_client:
                player_data_for_client["xp"] = player_data_for_client["experience_points"]
            return player_data_for_client

        logger.warning("PlayerService not available, using basic player data", player_id=player_id)
        return build_basic_player_data(player)
    except (ImportError, RuntimeError, AttributeError) as e:
        logger.error("Error getting complete player data", error=str(e), player_id=player_id, exc_info=True)
        return build_basic_player_data(player)


async def get_player_and_room(
    player_id: uuid.UUID, player_id_str: str, connection_manager
) -> tuple[Any, Any, str | None]:
    """
    Get and validate player and room for initial game state.

    Returns:
        Tuple of (player, room, canonical_room_id) or (None, None, None) if not found
    """
    player = await connection_manager.get_player(player_id)
    if not player or not hasattr(player, "current_room_id"):
        return None, None, None

    from ..async_persistence import get_async_persistence

    async_persistence = get_async_persistence()
    if not async_persistence:
        return None, None, None

    room = async_persistence.get_room_by_id(str(player.current_room_id))
    if not room:
        return None, None, None

    if not room.has_player(player_id_str):
        logger.info("Adding player to room", player_id=player_id, room_id=str(player.current_room_id))
        room.player_entered(player_id_str)

    canonical_room_id = getattr(room, "id", None) or player.current_room_id
    return player, room, canonical_room_id
