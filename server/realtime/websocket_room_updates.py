"""
WebSocket room update and broadcast functions for MythosMUD real-time communication.

This module handles room updates and broadcasting to players.
"""

import uuid
from typing import TYPE_CHECKING, Any

from ..async_persistence import get_async_persistence
from ..services.npc_instance_service import get_npc_instance_service
from ..structured_logging.enhanced_logging_config import get_logger
from ..utils.room_renderer import build_room_drop_summary, clone_room_drops
from .disconnect_grace_period import is_player_in_grace_period
from .envelope import build_event
from .login_grace_period import is_player_in_login_grace_period
from .websocket_helpers import convert_uuids_to_strings, get_npc_name_from_instance

if TYPE_CHECKING:
    from ..models.room import Room
    from .connection_manager import ConnectionManager

logger = get_logger(__name__)


async def get_player_occupants(connection_manager: "ConnectionManager | Any", room_id: str) -> list[str]:
    """
    Get player occupant names from room.

    Includes "(linkdead)" indicator for players in grace period.
    """
    occupant_names = []
    try:  # pylint: disable=too-many-nested-blocks  # Reason: Room occupant processing requires complex nested logic for name extraction, grace period checks, and formatting
        room_occupants = await connection_manager.get_room_occupants(room_id)
        for occ in room_occupants or []:
            name = occ.get("player_name") or occ.get("name")
            if name:
                # Check if player is in disconnect grace period (name may already include "(linkdead)" from occupant processor)
                # Also check if player is in login grace period and add "(warded)" indicator
                # But we check here as well for safety
                player_id_str = occ.get("player_id")
                if player_id_str and connection_manager:
                    try:
                        player_id = uuid.UUID(player_id_str) if isinstance(player_id_str, str) else player_id_str

                        if is_player_in_grace_period(player_id, connection_manager) and "(linkdead)" not in name:
                            name = f"{name} (linkdead)"
                        # Check login grace period (can have both indicators)
                        if is_player_in_login_grace_period(player_id, connection_manager) and "(warded)" not in name:
                            name = f"{name} (warded)"
                    except (ValueError, AttributeError, ImportError, TypeError):
                        # If we can't check grace period, use name as-is
                        pass
                occupant_names.append(name)
    except (AttributeError, KeyError, TypeError, ValueError) as e:
        logger.error("Error transforming room occupants", room_id=room_id, error=str(e))
    return occupant_names


async def get_npc_occupants_from_lifecycle_manager(room_id: str) -> list[str]:
    """Get NPC occupant names from lifecycle manager."""
    occupant_names = []
    npc_ids: list[str] = []
    try:
        npc_instance_service = get_npc_instance_service()
        if npc_instance_service and hasattr(npc_instance_service, "lifecycle_manager"):
            lifecycle_manager = npc_instance_service.lifecycle_manager
            if lifecycle_manager and hasattr(lifecycle_manager, "active_npcs"):
                active_npcs_dict = lifecycle_manager.active_npcs
                for npc_id, npc_instance in active_npcs_dict.items():
                    if not npc_instance.is_alive:
                        logger.debug(
                            "Skipping dead NPC from occupants",
                            npc_id=npc_id,
                            npc_name=getattr(npc_instance, "name", "unknown"),
                            room_id=room_id,
                        )
                        continue

                    current_room = getattr(npc_instance, "current_room", None)
                    current_room_id = getattr(npc_instance, "current_room_id", None)
                    npc_room_id = current_room or current_room_id
                    if npc_room_id == room_id:
                        npc_ids.append(npc_id)

        logger.debug("DEBUG: Room has NPCs from lifecycle manager", room_id=room_id, npc_ids=npc_ids)
        for npc_id in npc_ids:
            npc_name = get_npc_name_from_instance(npc_id)
            if npc_name:
                logger.debug("DEBUG: Got NPC name from database", npc_name=npc_name, npc_id=npc_id)
                occupant_names.append(npc_name)
            else:
                logger.warning("NPC instance not found for ID - skipping from room display", npc_id=npc_id)
    except (AttributeError, KeyError, TypeError, ValueError) as npc_query_error:
        logger.warning(
            "Error querying NPCs from lifecycle manager, falling back to room.get_npcs()",
            room_id=room_id,
            error=str(npc_query_error),
        )
        raise
    return occupant_names


async def get_npc_occupants_fallback(room: "Room | Any", room_id: str) -> list[str]:
    """Get NPC occupant names using fallback method (room.get_npcs())."""
    occupant_names = []
    room_npc_ids = room.get_npcs()
    logger.debug("DEBUG: Room has NPCs from fallback", room_id=room_id, npc_ids=room_npc_ids)

    filtered_npc_ids = []
    try:  # pylint: disable=too-many-nested-blocks  # Reason: NPC filtering requires complex nested logic for service lookup, lifecycle validation, and NPC ID filtering
        npc_instance_service = get_npc_instance_service()
        if npc_instance_service and hasattr(npc_instance_service, "lifecycle_manager"):
            lifecycle_manager = npc_instance_service.lifecycle_manager
            if lifecycle_manager and hasattr(lifecycle_manager, "active_npcs"):
                for npc_id in room_npc_ids:
                    if npc_id in lifecycle_manager.active_npcs:
                        npc_instance = lifecycle_manager.active_npcs[npc_id]
                        if npc_instance.is_alive:
                            filtered_npc_ids.append(npc_id)
                        else:
                            logger.debug("Filtered dead NPC from fallback occupants", npc_id=npc_id, room_id=room_id)
    except (AttributeError, KeyError, TypeError, ValueError) as filter_error:
        logger.warning("Error filtering fallback NPCs, using all room NPCs", room_id=room_id, error=str(filter_error))
        filtered_npc_ids = room_npc_ids

    for npc_id in filtered_npc_ids:
        npc_name = get_npc_name_from_instance(npc_id)
        if npc_name:
            occupant_names.append(npc_name)

    return occupant_names


async def build_room_update_event(
    room: "Room | Any",
    room_id: str,
    player_id: str,
    occupant_names: list[str],
    connection_manager: "ConnectionManager | Any",
) -> dict[str, Any]:
    """Build room update event with room data and occupants."""
    room_data = room.to_dict() if hasattr(room, "to_dict") else room
    if isinstance(room_data, dict):
        room_data = await connection_manager.convert_room_players_uuids_to_names(room_data)

    logger.debug("DEBUG: Room occupants breakdown", room_id=room_id)
    logger.debug("  - Room object ID", room_id=id(room))
    logger.debug("  - Players", players=room.get_players())
    logger.debug("  - Objects", objects=room.get_objects())
    logger.debug("  - NPCs", npcs=room.get_npcs())
    logger.debug("  - Total occupant_count", count=room.get_occupant_count())

    room_data = convert_uuids_to_strings(room_data)

    room_drops: list[dict[str, Any]] = []
    room_manager = getattr(connection_manager, "room_manager", None)
    if room_manager and hasattr(room_manager, "list_room_drops"):
        try:
            room_drops = clone_room_drops(room_manager.list_room_drops(room_id))
        except (AttributeError, KeyError, TypeError, ValueError) as exc:
            logger.debug("Failed to collect room drops for broadcast", room_id=room_id, error=str(exc))

    drop_summary = build_room_drop_summary(room_drops)

    return build_event(
        "room_update",
        {
            "room": room_data,
            "entities": [],
            "occupants": occupant_names,
            "occupant_count": len(occupant_names),
            "room_drops": room_drops,
            "drop_summary": drop_summary,
        },
        player_id=player_id,
        room_id=room_id,
    )


async def update_player_room_subscription(
    connection_manager: "ConnectionManager | Any", player_id: str, room_id: str
) -> None:
    """Update player's room subscription and current room."""
    player_id_uuid = uuid.UUID(player_id) if isinstance(player_id, str) else player_id
    player = await connection_manager.get_player(player_id_uuid)
    if not player:
        return

    if hasattr(player, "current_room_id") and player.current_room_id and player.current_room_id != room_id:
        await connection_manager.unsubscribe_from_room(player_id_uuid, str(player.current_room_id))
        logger.debug("Player unsubscribed from old room", player_id=player_id, old_room_id=player.current_room_id)

    await connection_manager.subscribe_to_room(player_id_uuid, room_id)
    logger.debug("Player subscribed to new room", player_id=player_id, new_room_id=room_id)

    player.current_room_id = room_id


async def broadcast_room_update(
    player_id: str, room_id: str, connection_manager: "ConnectionManager | None" = None
) -> None:
    """
    Broadcast a room update to all players in the room.

    Args:
        player_id: The player who triggered the update
        room_id: The room's ID
        connection_manager: ConnectionManager instance (optional, will resolve from app.state if not provided)
    """
    logger.debug("broadcast_room_update called", player_id=player_id, room_id=room_id)
    try:
        if connection_manager is None:
            # Import inside function to avoid circular import (main.py imports websocket_room_updates indirectly)
            from ..main import (
                app,  # pylint: disable=import-outside-toplevel  # Reason: Import inside function to avoid circular import, main.py imports websocket_room_updates indirectly
            )

            connection_manager = app.state.container.connection_manager

        async_persistence = get_async_persistence()
        if not async_persistence:
            logger.warning("Async persistence layer not available for room update")
            return

        room = async_persistence.get_room_by_id(room_id)
        if not room:
            logger.warning("Room not found for update", room_id=room_id)
            return

        logger.debug("DEBUG: broadcast_room_update - Room object ID", room_id=id(room))
        logger.debug("DEBUG: broadcast_room_update - Room players before any processing", players=room.get_players())

        occupant_names = await get_player_occupants(connection_manager, room_id)

        try:
            npc_occupants = await get_npc_occupants_from_lifecycle_manager(room_id)
            occupant_names.extend(npc_occupants)
        except (AttributeError, KeyError, TypeError, ValueError):
            npc_occupants = await get_npc_occupants_fallback(room, room_id)
            occupant_names.extend(npc_occupants)

        update_event = await build_room_update_event(room, room_id, player_id, occupant_names, connection_manager)

        logger.debug("Room update event created", update_event=update_event)

        await update_player_room_subscription(connection_manager, player_id, room_id)

        logger.debug("Broadcasting room update to room", room_id=room_id)
        await connection_manager.broadcast_to_room(room_id, update_event)
        logger.debug("Room update broadcast completed for room", room_id=room_id)

    except (AttributeError, KeyError, TypeError, ValueError, RuntimeError) as e:
        logger.error("Error broadcasting room update for room", room_id=room_id, error=str(e))
