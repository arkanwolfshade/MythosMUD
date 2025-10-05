"""
Broadcast utilities for MythosMUD real-time communication.

This module contains functions for broadcasting updates to players and rooms.
"""

from ..logging_config import get_logger
from .connection_manager import connection_manager
from .envelope import build_event

logger = get_logger(__name__)


def _get_npc_name_from_instance(npc_id: str) -> str | None:
    """
    Get NPC name from the actual NPC instance, preserving original case from database.

    Args:
        npc_id: The NPC instance ID

    Returns:
        The NPC name or None if not found
    """
    try:
        from ..services.npc_instance_service import get_npc_instance_service

        npc_service = get_npc_instance_service()
        if npc_service:
            npc = npc_service.get_npc_by_id(npc_id)
            if npc:
                return npc.name
    except Exception as e:
        logger.error(f"Error getting NPC name for ID {npc_id}: {e}")

    return None


async def broadcast_room_update(player_id: str, room_id: str):
    """
    Broadcast a room update to all players in the room.

    Args:
        player_id: The player who triggered the update
        room_id: The room's ID
    """
    logger.debug(f"broadcast_room_update called with player_id: {player_id}, room_id: {room_id}")
    try:
        # Get room data
        persistence = connection_manager.persistence
        if not persistence:
            logger.warning("Persistence layer not available for room update")
            return

        room = persistence.get_room(room_id)
        if not room:
            logger.warning(f"Room not found for update: {room_id}")
            return

        logger.debug(f"🔍 DEBUG: broadcast_room_update - Room object ID: {id(room)}")
        logger.debug(f"🔍 DEBUG: broadcast_room_update - Room players before any processing: {room.get_players()}")

        # Get room occupants (players and NPCs)
        occupant_names = []

        # Get player occupants
        room_occupants = connection_manager.get_room_occupants(room_id)
        try:
            for occ in room_occupants or []:
                if isinstance(occ, dict):
                    name = occ.get("player_name") or occ.get("name")
                    if name:
                        occupant_names.append(name)
                elif isinstance(occ, str):
                    occupant_names.append(occ)
        except Exception as e:
            logger.error(f"Error transforming room occupants for room {room_id}: {e}")

        # Get NPC occupants
        if persistence:
            npc_ids = room.get_npcs()
            logger.debug(f"DEBUG: Room {room_id} has NPCs: {npc_ids}")
            for npc_id in npc_ids:
                # Get NPC name from the actual NPC instance, preserving original case from database
                npc_name = _get_npc_name_from_instance(npc_id)
                if npc_name:
                    logger.debug(f"DEBUG: Got NPC name '{npc_name}' from database for ID '{npc_id}'")
                    occupant_names.append(npc_name)
                else:
                    # Log warning if NPC instance not found - this should not happen in normal operation
                    logger.warning(f"NPC instance not found for ID: {npc_id} - skipping from room display")

        # Create room update event
        room_data = room.to_dict() if hasattr(room, "to_dict") else room

        # Debug: Log the room's actual occupants
        logger.debug(f"🔍 DEBUG: Room {room_id} occupants breakdown:")
        logger.debug(f"  - Room object ID: {id(room)}")
        logger.debug(f"  - Players: {room.get_players()}")
        logger.debug(f"  - Objects: {room.get_objects()}")
        logger.debug(f"  - NPCs: {room.get_npcs()}")
        logger.debug(f"  - Total occupant_count: {room.get_occupant_count()}")

        # Ensure all UUID objects are converted to strings for JSON serialization
        def convert_uuids_to_strings(obj):
            if isinstance(obj, dict):
                return {k: convert_uuids_to_strings(v) for k, v in obj.items()}
            elif isinstance(obj, list):
                return [convert_uuids_to_strings(item) for item in obj]
            elif hasattr(obj, "__class__") and "UUID" in obj.__class__.__name__:
                return str(obj)
            else:
                return obj

        room_data = convert_uuids_to_strings(room_data)

        update_event = build_event(
            "room_update",
            {
                "room": room_data,
                "entities": [],
                "occupants": occupant_names,
                "occupant_count": len(occupant_names),
            },
            player_id=player_id,
            room_id=room_id,
        )

        logger.debug(f"Room update event created: {update_event}")

        # Update player's room subscription
        player = connection_manager._get_player(player_id)
        if player:
            # Unsubscribe from old room
            if hasattr(player, "current_room_id") and player.current_room_id and player.current_room_id != room_id:
                await connection_manager.unsubscribe_from_room(player_id, player.current_room_id)
                logger.debug(f"Player {player_id} unsubscribed from old room {player.current_room_id}")

            # Subscribe to new room
            await connection_manager.subscribe_to_room(player_id, room_id)
            logger.debug(f"Player {player_id} subscribed to new room {room_id}")

            # Update player's current room
            player.current_room_id = room_id

        # Broadcast to room
        logger.debug(f"Broadcasting room update to room: {room_id}")
        await connection_manager.broadcast_to_room(room_id, update_event)
        logger.debug(f"Room update broadcast completed for room: {room_id}")

    except Exception as e:
        logger.error(f"Error broadcasting room update for room {room_id}: {e}")
