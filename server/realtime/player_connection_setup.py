"""
Player connection setup functions.

This module handles the setup tasks when a player connects,
including room management, broadcasting events, and state initialization.
"""

import uuid
from typing import Any

from ..exceptions import DatabaseError
from ..models import Player
from ..structured_logging.enhanced_logging_config import get_logger
from .disconnect_grace_period import cancel_grace_period
from .envelope import build_event
from .login_grace_period import start_login_grace_period
from .player_presence_utils import extract_player_name

logger = get_logger(__name__)


async def _update_player_last_active(player_id: uuid.UUID, manager: Any) -> None:
    """
    Update last_active timestamp in database when player connects.

    Args:
        player_id: The player's ID
        manager: ConnectionManager instance
    """
    if not manager.async_persistence:
        return

    try:
        await manager.async_persistence.update_player_last_active(player_id)
        logger.debug("Updated last_active for player on connection", player_id=player_id)
    except (DatabaseError, AttributeError) as e:
        logger.warning("Failed to update last_active for player", player_id=player_id, error=str(e))


async def _add_player_to_room_silently(player_id: uuid.UUID, room_id: str, manager: Any) -> None:
    """
    Add player to the Room object WITHOUT triggering player_entered event.

    On initial connection, we only send player_entered_game, not player_entered.

    Args:
        player_id: The player's ID
        room_id: The room ID
        manager: ConnectionManager instance
    """
    if not manager.async_persistence:
        return

    room = manager.async_persistence.get_room_by_id(room_id)  # Sync method, uses cache
    if not room:
        logger.warning("Room not found when trying to add player", room_id=room_id, player_id=player_id)
        return

    if not room.has_player(player_id):
        room.add_player_silently(player_id)
        logger.info(
            "Player added to room on initial connection (no player_entered event)",
            player_id=player_id,
            room_id=room_id,
        )


async def _broadcast_player_entered_game(player_id: uuid.UUID, player: Player, room_id: str, manager: Any) -> None:
    """
    Broadcast a structured entry event to other occupants (excluding the newcomer).

    Args:
        player_id: The player's ID
        player: The player object
        room_id: The room ID
        manager: ConnectionManager instance
    """
    try:
        player_name = extract_player_name(player, player_id)
        entered_event = build_event(
            "player_entered_game",
            {
                "player_id": player_id,
                "player_name": player_name,
            },
            room_id=room_id,
        )
        logger.info(
            "Broadcasting player_entered_game event",
            player_id=player_id,
            room_id=room_id,
        )
        await manager.broadcast_to_room(room_id, entered_event, exclude_player=player_id)
    except (DatabaseError, AttributeError) as broadcast_error:
        logger.error(
            "Failed to broadcast player_entered_game event",
            player_id=player_id,
            room_id=room_id,
            error=str(broadcast_error),
        )


async def _send_room_occupants_update_after_connection(player_id: uuid.UUID, room_id: str, manager: Any) -> None:
    """
    Send room_occupants update so other players see the new occupant.

    Args:
        player_id: The player's ID
        room_id: The room ID
        manager: ConnectionManager instance
    """
    try:
        event_handler = None
        if manager.app and hasattr(manager.app, "state"):
            event_handler = getattr(manager.app.state, "event_handler", None)

        if event_handler and hasattr(event_handler, "send_room_occupants_update"):
            logger.debug(
                "Sending room_occupants update after player_entered_game",
                player_id=player_id,
                room_id=room_id,
            )
            await event_handler.send_room_occupants_update(room_id, exclude_player=str(player_id))
        else:
            logger.warning(
                "Event handler not available to send room_occupants update",
                player_id=player_id,
                room_id=room_id,
                has_app=bool(manager.app),
            )
    except (DatabaseError, AttributeError) as occupants_error:
        logger.error(
            "Failed to send room_occupants update after player connection",
            player_id=player_id,
            room_id=room_id,
            error=str(occupants_error),
        )


async def handle_new_connection_setup(
    player_id: uuid.UUID,
    player: Player,
    room_id: str | None,
    manager: Any,  # ConnectionManager - avoiding circular import
) -> None:
    """
    Handle setup tasks for a new player connection.

    Args:
        player_id: The player's ID
        player: The player object
        room_id: The room ID
        manager: ConnectionManager instance
    """
    # Update last_active timestamp in database when player connects
    await _update_player_last_active(player_id, manager)

    # Clear any pending messages to ensure fresh game state
    manager.message_queue.remove_player_messages(str(player_id))

    # Clear processed disconnect flag to allow future disconnect processing
    async with manager.processed_disconnect_lock:
        manager.processed_disconnects.discard(player_id)

    # Cancel grace period if player was in grace period (reconnection)
    if player_id in getattr(manager, "grace_period_players", {}):
        logger.info("Player reconnected during grace period, cancelling grace period", player_id=player_id)
        await cancel_grace_period(player_id, manager)

    # Remove player from combat if they're in combat state on login
    # This ensures players are never in combat when they log in
    try:
        # Lazy import to avoid circular dependency with combat_service
        from ..services.combat_service import get_combat_service  # noqa: E402

        combat_service = get_combat_service()
        if combat_service:
            combat = await combat_service.get_combat_by_participant(player_id)
            if combat:
                try:
                    await combat_service.end_combat(combat.combat_id, "Player logged in - removing from combat")
                    logger.info(
                        "Ended combat for player on login",
                        player_id=player_id,
                        combat_id=combat.combat_id,
                    )
                except Exception as combat_error:  # pylint: disable=broad-exception-caught
                    # Log but don't fail - combat cleanup is best effort
                    logger.warning(
                        "Error ending combat for player on login",
                        player_id=player_id,
                        combat_id=combat.combat_id if combat else None,
                        error=str(combat_error),
                    )
    except (AttributeError, ImportError, TypeError, ValueError) as e:
        # If we can't check combat, log but don't fail - combat cleanup is best effort
        logger.debug("Could not check combat state for player on login", player_id=player_id, error=str(e))

    # Update room occupants using canonical room id
    if not room_id:
        return

    manager.room_manager.add_room_occupant(str(player_id), room_id)

    # Prune any stale occupant ids not currently online
    online_players_str = {str(k): v for k, v in manager.online_players.items()}
    manager.room_manager.reconcile_room_presence(room_id, online_players_str)

    # Add player to the Room object WITHOUT triggering player_entered event
    await _add_player_to_room_silently(player_id, room_id, manager)

    # Start login grace period for the newly connected player
    # This provides 10 seconds of immunity to damage and negative effects
    await start_login_grace_period(player_id, manager)

    # Send initial game_state event to the player
    # Accessing protected method is necessary for modularity
    # pylint: disable=protected-access
    await manager._send_initial_game_state(player_id, player, room_id)

    # Broadcast a structured entry event to other occupants (excluding the newcomer)
    await _broadcast_player_entered_game(player_id, player, room_id, manager)

    # Send room_occupants update so other players see the new occupant
    await _send_room_occupants_update_after_connection(player_id, room_id, manager)
