"""
Player presence tracking helper for connection manager.

This module provides helper functions for tracking player connections
and disconnections, extracting common logic from ConnectionManager.
"""

import time
import uuid
from typing import Any, cast

from ..exceptions import DatabaseError
from ..structured_logging.enhanced_logging_config import get_logger
from .disconnect_grace_period import start_grace_period
from .player_connection_setup import handle_new_connection_setup
from .player_disconnect_handlers import (
    _cleanup_player_references,
    _collect_disconnect_keys,
    _remove_player_from_online_tracking,
    handle_player_disconnect_broadcast,
)
from .player_presence_utils import extract_player_name, get_player_position

logger = get_logger(__name__)


def _build_player_info(
    player_id: Any,
    player: Any,
    connection_type: str,
    manager: Any,
    is_new_connection: bool,
) -> dict[str, Any]:
    """
    Build or update player info dictionary for connection tracking.

    Args:
        player_id: The player's ID
        player: The player object
        connection_type: Type of connection
        manager: ConnectionManager instance
        is_new_connection: Whether this is a new connection

    Returns:
        Dictionary with player connection info
    """
    position = get_player_position(player, player_id)
    player_name = extract_player_name(player, player_id)

    player_info: dict[str, Any] = {
        "player_id": player_id,
        "player_name": player_name,
        "level": getattr(player, "level", 1),
        "current_room_id": getattr(player, "current_room_id", None),
        "connected_at": time.time(),
        "connection_types": set(),
        "total_connections": 0,
        "position": position,
    }

    if not is_new_connection:
        existing_info = manager.online_players[player_id]
        player_info["connected_at"] = existing_info.get("connected_at", time.time())
        existing_types = existing_info.get("connection_types", set())
        player_info["connection_types"] = existing_types if isinstance(existing_types, set) else set()
        player_info["position"] = existing_info.get("position", player_info["position"])

    connection_types_for_player = player_info["connection_types"]
    if isinstance(connection_types_for_player, set):
        connection_types_for_player.add(connection_type)
    player_info["total_connections"] = len(manager.player_websockets.get(player_id, []))

    return player_info


def _resolve_room_id(player: Any, manager: Any) -> str | None:
    """
    Resolve canonical room ID from player's current_room_id.

    Args:
        player: The player object
        manager: ConnectionManager instance

    Returns:
        Canonical room ID or None
    """
    room_id = getattr(player, "current_room_id", None)
    if not manager.async_persistence or not room_id:
        return room_id

    room = manager.async_persistence.get_room_by_id(room_id)
    if room and getattr(room, "id", None):
        return cast(str, room.id)

    return cast(str | None, room_id)


async def _resolve_room_id_for_tutorial_reconnect(player: Any, manager: Any) -> str | None:
    """
    For players with tutorial_instance_id, ensure instance exists and return first room.

    Per plan: on reconnect, place player at the beginning of the tutorial instance.
    If instance was lost (e.g. server restart), recreate it.

    Returns:
        First room ID if tutorial player, None to fall back to normal resolution
    """
    instance_id = getattr(player, "tutorial_instance_id", None)
    if not instance_id:
        return None

    instance_manager = _get_instance_manager_from_manager(manager)
    if not instance_manager:
        logger.warning("InstanceManager not available for tutorial reconnect", player_id=player.player_id)
        return None

    instance = instance_manager.get_instance(instance_id)
    if not instance:
        logger.info(
            "Tutorial instance missing on reconnect, recreating",
            player_id=player.player_id,
            instance_id=instance_id,
        )
        from ..game.player_creation_service import TUTORIAL_TEMPLATE_ID

        instance = instance_manager.create_instance(
            template_id=TUTORIAL_TEMPLATE_ID,
            owner_player_id=player.player_id,
        )
        instance_id = instance.instance_id
        setattr(player, "tutorial_instance_id", instance_id)  # noqa: B010  # Reason: SQLAlchemy column

    first_room_id = instance_manager.get_first_room_id(instance_id)
    if not first_room_id:
        logger.warning("Tutorial instance has no rooms", instance_id=instance_id)
        return None

    setattr(player, "current_room_id", first_room_id)  # noqa: B010  # Reason: SQLAlchemy column
    if manager.async_persistence:
        await manager.async_persistence.save_player(player)
    return cast(str, first_room_id)


def _get_instance_manager_from_manager(manager: Any) -> Any:
    """Extract InstanceManager from ConnectionManager via app.container."""
    app_state = getattr(manager, "app", None)
    if not app_state:
        return None
    app_state = getattr(app_state, "state", None)
    if not app_state:
        return None
    container = getattr(app_state, "container", None)
    if not container:
        return None
    return getattr(container, "instance_manager", None)


async def track_player_connected_impl(
    player_id: Any,
    player: Any,  # Player
    connection_type: str,
    manager: Any,  # ConnectionManager
) -> None:
    """
    Track when a player connects.

    Args:
        player_id: The player's ID
        player: The player object
        connection_type: Type of connection
        manager: ConnectionManager instance
    """
    try:
        is_new_connection = player_id not in manager.online_players

        player_info = _build_player_info(player_id, player, connection_type, manager, is_new_connection)

        manager.online_players[player_id] = player_info
        manager.mark_player_seen(player_id)

        if is_new_connection:
            room_id = await _resolve_room_id_for_tutorial_reconnect(player, manager)
            if not room_id:
                room_id = _resolve_room_id(player, manager)
            if room_id:
                await handle_new_connection_setup(player_id, player, room_id, manager)
            logger.info("Player presence tracked as connected (new connection)", player_id=player_id)
        else:
            logger.info("Player additional connection tracked", player_id=player_id, connection_type=connection_type)

    except (DatabaseError, AttributeError) as e:
        logger.error("Error tracking player connection", error=str(e), exc_info=True)


async def broadcast_connection_message_impl(
    player_id: Any,
    player: Any,  # Player
    manager: Any,  # ConnectionManager
) -> None:
    """Broadcast a connection message for a player who is already tracked as online."""
    try:
        room_id = getattr(player, "current_room_id", None)
        if manager.async_persistence and room_id:
            room = manager.async_persistence.get_room_by_id(room_id)
            if room and getattr(room, "id", None):
                room_id = room.id

        if room_id:
            logger.debug("Player already tracked as online, skipping duplicate connection message", player_id=player_id)

    except (DatabaseError, AttributeError) as e:
        logger.error("Error broadcasting connection message", player_id=player_id, error=str(e), exc_info=True)


def _should_skip_disconnect(player_id: uuid.UUID, manager: Any, connection_type: str | None) -> bool:
    """
    Check if player disconnection should be skipped.

    Args:
        player_id: The player's ID
        manager: ConnectionManager instance
        connection_type: Type of connection being disconnected

    Returns:
        True if disconnection should be skipped, False otherwise
    """
    has_websocket = manager.has_websocket_connection(player_id)
    if has_websocket and connection_type:
        logger.info(
            "Player still has connections, not fully disconnecting",
            player_id=player_id,
            disconnected_connection_type=connection_type,
        )
        return True
    return False


async def _acquire_disconnect_lock(player_id: uuid.UUID, manager: Any) -> bool:
    """
    Acquire disconnect lock and mark player as disconnecting.

    Args:
        player_id: The player's ID
        manager: ConnectionManager instance

    Returns:
        True if lock acquired successfully, False if already disconnecting
    """
    # Prevent duplicate disconnect events
    if player_id in manager.disconnecting_players:
        logger.warning(
            "Player was stuck in disconnecting_players, force clearing to allow disconnect",
            player_id=player_id,
        )
        async with manager.disconnect_lock:
            manager.disconnecting_players.discard(player_id)

    # Acquire lock and double-check
    async with manager.disconnect_lock:
        if player_id in manager.disconnecting_players:
            logger.debug(
                "DEBUG: Player already being disconnected (post-lock check), skipping duplicate event",
                player_id=player_id,
            )
            return False

        # Mark player as being disconnected
        manager.disconnecting_players.add(player_id)
        logger.debug("DEBUG: Marked player as disconnecting", player_id=player_id)
        return True


async def track_player_disconnected_impl(
    player_id: uuid.UUID,
    manager: Any,  # ConnectionManager
    connection_type: str | None = None,
) -> None:
    """
    Track when a player disconnects.

    For unintentional disconnects (connection loss), starts a 30-second grace period.
    For intentional disconnects (via /rest or /quit), performs immediate cleanup.

    Args:
        player_id: The player's ID
        connection_type: Type of connection being disconnected
        manager: ConnectionManager instance
    """
    try:
        # Check if player has any remaining connections
        if _should_skip_disconnect(player_id, manager, connection_type):
            return

        # Acquire lock and mark as disconnecting
        if not await _acquire_disconnect_lock(player_id, manager):
            return

        # Check if this is an intentional disconnect (no grace period)
        is_intentional = player_id in getattr(manager, "intentional_disconnects", set())

        if is_intentional:
            # Intentional disconnect - perform immediate cleanup (no grace period)
            logger.info("Intentional disconnect detected, skipping grace period", player_id=player_id)

            # Remove from intentional disconnects set
            manager.intentional_disconnects.discard(player_id)

            # Resolve player
            pl = await manager._get_player(player_id)  # pylint: disable=protected-access  # Reason: Accessing protected member _get_player is necessary for player presence tracking implementation, this is part of the internal API
            room_id: str | None = getattr(pl, "current_room_id", None) if pl else None
            player_name: str = extract_player_name(pl, player_id) if pl else "Unknown Player"

            # Collect all keys to remove
            keys_to_remove, keys_to_remove_str = _collect_disconnect_keys(player_id, pl)

            # Handle disconnect broadcast
            await handle_player_disconnect_broadcast(player_id, player_name, room_id, manager)

            # Remove player from online tracking
            _remove_player_from_online_tracking(keys_to_remove, keys_to_remove_str, manager)

            # Clean up ghost players
            manager._cleanup_ghost_players()  # pylint: disable=protected-access  # Reason: Accessing protected member _cleanup_ghost_players is necessary for player presence tracking implementation, this is part of the internal API

            # Clean up remaining references
            _cleanup_player_references(player_id, manager)

            logger.info("Player presence tracked as disconnected (intentional)", player_id=player_id)
        else:
            # Unintentional disconnect - start grace period
            logger.info("Unintentional disconnect detected, starting grace period", player_id=player_id)

            # Start grace period (player will remain in-game for 30 seconds)
            await start_grace_period(player_id, manager)

            logger.info("Grace period started for disconnected player", player_id=player_id)

    except (DatabaseError, AttributeError) as e:
        logger.error("Error tracking player disconnection", error=str(e), exc_info=True)
    finally:
        # Always remove player from disconnecting set
        async with manager.disconnect_lock:
            manager.disconnecting_players.discard(player_id)
