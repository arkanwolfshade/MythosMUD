"""
Teleport utility functions for admin commands in MythosMUD.

This module provides utility functions for teleport-related admin commands,
including player lookup, teleport effect messages, and broadcasting.
"""

# pylint: disable=too-many-arguments,too-many-return-statements  # Reason: Teleport utilities require many parameters for context and validation and multiple return statements for early validation returns

from typing import Any, cast
from uuid import UUID

from ..realtime.envelope import build_event
from ..structured_logging.admin_actions_logger import get_admin_actions_logger
from ..structured_logging.enhanced_logging_config import get_logger

logger = get_logger(__name__)


def log_failed_admin_move(
    *,
    admin_name: str,
    target_player_name: str,
    action_type: str,
    from_room: str,
    to_room: str,
    error: Exception,
    direction: str | None = None,
) -> None:
    """Best-effort audit log for a failed teleport/goto action; never raises.

    Shared by handle_teleport_command, handle_confirm_teleport_command, and
    handle_confirm_goto_command (issue #787): each had a near-identical
    try/except-around-log_teleport_action block in its exception handler.
    Takes room ids rather than player objects so it doesn't need an explicit
    Any (the module's player-lookup helpers all return Any today).

    A "goto" moves the admin (from_room=admin's room); a "teleport" moves the
    target (from_room=target's room) -- admin_room_id/target_room_id are
    derived from that instead of taking two more redundant params.
    """
    admin_logger = get_admin_actions_logger()
    admin_room_id, target_room_id = (from_room, to_room) if action_type == "goto" else (to_room, from_room)
    additional_data: dict[str, str] = {
        "admin_room_id": admin_room_id,
        "target_room_id": target_room_id,
    }
    if direction is not None:
        additional_data["direction"] = direction
    try:
        admin_logger.log_teleport_action(
            admin_name=admin_name,
            target_player=target_player_name,
            action_type=action_type,
            from_room=from_room,
            to_room=to_room,
            success=False,
            error_message=str(error),
            additional_data=additional_data,
        )
    except (OSError, AttributeError, TypeError):
        pass  # Ignore logging errors if command itself failed


async def get_online_player_by_display_name(display_name: str, connection_manager: Any) -> dict[str, Any] | None:
    """
    Get online player information by display name.

    Args:
        display_name: Display name to search for
        connection_manager: Connection manager instance

    Returns:
        dict: Player information if found, None otherwise
    """
    if not connection_manager:
        logger.warning("Connection manager not available for online player lookup")
        return None

    result: dict[str, Any] | None = cast(
        dict[str, Any] | None, connection_manager.get_online_player_by_display_name(display_name)
    )
    return result


def create_teleport_effect_message(
    player_name: str,
    effect_type: str,
    *,
    teleport_type: str,
    direction: str | None = None,
    arrival_direction: str | None = None,
) -> str:
    """
    Create teleport effect message for visual display.

    Args:
        player_name: Name of the player being teleported
        effect_type: Type of effect ('arrival' or 'departure')
        teleport_type: Type of teleport ('teleport' or 'goto')
        direction: Optional direction text for departure messages
        arrival_direction: Optional direction text for arrival messages

    Returns:
        str: Formatted teleport effect message
    """
    if teleport_type == "teleport":
        if effect_type == "departure":
            if direction:
                return f"{player_name} leaves the room heading {direction}."
            return f"{player_name} disappears in a ripple of distorted air."
        if effect_type == "arrival":
            if arrival_direction:
                return f"{player_name} arrives from the {arrival_direction}."
            return f"{player_name} arrives in a shimmer of eldritch energy."
    elif teleport_type == "goto":
        if effect_type == "departure":
            return f"{player_name} vanishes in a flash of pale light."
        if effect_type == "arrival":
            if arrival_direction:
                return f"{player_name} arrives from the {arrival_direction}."
            return f"{player_name} appears beside you in a rush of displaced air."

    return f"{player_name} is affected by mysterious forces."


async def broadcast_teleport_effects(  # pylint: disable=too-many-arguments  # Reason: Teleport utilities require many parameters for context and broadcasting
    connection_manager: Any,
    player_name: str,
    from_room_id: str,
    to_room_id: str,
    teleport_type: str,
    *,
    direction: str | None = None,
    arrival_direction: str | None = None,
    target_player_id: str | None = None,
) -> None:
    """
    Broadcast teleport visual effects to players in affected rooms.

    Args:
        connection_manager: Connection manager instance
        player_name: Name of the player being teleported
        from_room_id: Room ID the player is leaving
        to_room_id: Room ID the player is arriving at
        teleport_type: Type of teleport ('teleport' or 'goto')
        direction: Optional direction for departure messaging
        arrival_direction: Optional reverse direction for arrival messaging
        target_player_id: Optional player ID to exclude from broadcasts
    """
    try:
        departure_message = create_teleport_effect_message(
            player_name,
            "departure",
            teleport_type=teleport_type,
            direction=direction,
            arrival_direction=arrival_direction,
        )

        arrival_message = create_teleport_effect_message(
            player_name,
            "arrival",
            teleport_type=teleport_type,
            direction=direction,
            arrival_direction=arrival_direction,
        )

        if hasattr(connection_manager, "broadcast_to_room"):
            departure_event = build_event(
                "system",
                {"message": departure_message, "message_type": "info"},
                room_id=from_room_id,
                connection_manager=connection_manager,
            )
            arrival_event = build_event(
                "system",
                {"message": arrival_message, "message_type": "info"},
                room_id=to_room_id,
                connection_manager=connection_manager,
            )
            await connection_manager.broadcast_to_room(
                from_room_id, departure_event, exclude_player=str(target_player_id) if target_player_id else None
            )
            await connection_manager.broadcast_to_room(
                to_room_id, arrival_event, exclude_player=str(target_player_id) if target_player_id else None
            )

        logger.debug(
            "Teleport effects broadcast", player_name=player_name, from_room_id=from_room_id, to_room_id=to_room_id
        )

    except (ValueError, TypeError, AttributeError, KeyError, OSError) as e:
        logger.error("Failed to broadcast teleport effects", player_name=player_name, error=str(e))


async def notify_player_of_teleport(
    connection_manager: Any,
    target_player_name: str,
    admin_name: str,
    notification_type: str,
    *,
    message: str | None = None,
) -> None:
    """
    Notify a player that they are being teleported by an admin.

    Args:
        connection_manager: Connection manager instance
        target_player_name: Name of the player being teleported
        admin_name: Name of the admin performing the teleport
        notification_type: Type of notification ('teleported_to' or 'teleported_from')
        message: Optional preformatted message to deliver
    """
    try:
        if message is None:
            if notification_type == "teleported_to":
                message = f"You have been teleported to {admin_name}'s location by an administrator."
            else:
                message = f"You have been teleported away from {admin_name} by an administrator."

        target_player_info = connection_manager.get_online_player_by_display_name(target_player_name)
        if target_player_info:
            raw_player_id = target_player_info.get("player_id")
            if raw_player_id and hasattr(connection_manager, "send_personal_message"):
                player_id = UUID(str(raw_player_id)) if not isinstance(raw_player_id, UUID) else raw_player_id
                event = build_event(
                    "system",
                    {"message": message, "message_type": "info"},
                    player_id=str(player_id),
                    connection_manager=connection_manager,
                )
                await connection_manager.send_personal_message(player_id, event)

        logger.debug("Teleport notification sent", target_player_name=target_player_name, admin_name=admin_name)

    except (ValueError, TypeError, AttributeError, KeyError, OSError) as e:
        logger.error("Failed to notify player of teleport", target_player_name=target_player_name, error=str(e))


__all__ = [
    "get_online_player_by_display_name",
    "create_teleport_effect_message",
    "broadcast_teleport_effects",
    "notify_player_of_teleport",
]
