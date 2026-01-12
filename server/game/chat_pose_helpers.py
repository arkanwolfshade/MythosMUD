"""Pose management helpers for chat service."""

import uuid
from typing import Any

from ..structured_logging.enhanced_logging_config import get_logger
from .chat_message import ChatMessage
from .chat_nats_publisher import publish_chat_message_to_nats

logger = get_logger("communications.chat_pose_helpers")


def normalize_player_id(player_id: Any) -> str:
    """Normalize player identifiers to string form."""
    return str(player_id)


async def set_player_pose(  # pylint: disable=too-many-arguments,too-many-positional-arguments  # Reason: Pose setting requires many parameters for context and validation
    player_id: uuid.UUID | str,
    pose: str,
    player_service: Any,
    pose_manager: Any,
    nats_service: Any,
    subject_manager: Any | None,
) -> dict[str, Any]:
    """
    Set a player's pose (temporary, in-memory only).

    Args:
        player_id: ID of the player setting the pose
        pose: Pose description
        player_service: Player service instance
        pose_manager: Pose manager instance
        nats_service: NATS service instance
        subject_manager: NATS subject manager instance (optional)

    Returns:
        Dictionary with success status and message details
    """
    player_id = normalize_player_id(player_id)
    logger.debug("=== CHAT SERVICE DEBUG: set_player_pose called ===", player_id=player_id, pose=pose)

    # Validate input
    if not pose or not pose.strip():
        logger.debug("=== CHAT SERVICE DEBUG: Empty pose ===")
        return {"success": False, "error": "Pose cannot be empty"}

    if len(pose.strip()) > 100:  # Limit for poses
        logger.debug("=== CHAT SERVICE DEBUG: Pose too long ===")
        return {"success": False, "error": "Pose too long (max 100 characters)"}

    # Get player information
    player = await player_service.get_player_by_id(player_id)
    if not player:
        logger.warning("Player not found for pose")
        return {"success": False, "error": "Player not found"}

    # Get player's current room
    room_id = player.current_room_id
    if not room_id:
        logger.warning("Player not in a room")
        return {"success": False, "error": "Player not in a room"}

    # Set the pose in memory
    pose_manager.set_pose(player_id, pose)

    # Create a chat message to notify room of pose change
    # ChatMessage accepts UUID | str and converts internally
    chat_message = ChatMessage(sender_id=player_id, sender_name=player.name, channel="pose", content=pose.strip())

    logger.info(
        "Player pose set successfully",
        player_id=player_id,
        player_name=player.name,
        room_id=room_id,
        pose=pose.strip(),
    )

    # Publish pose change to NATS for real-time distribution
    logger.debug("=== CHAT SERVICE DEBUG: About to publish pose message to NATS ===")
    success = await publish_chat_message_to_nats(chat_message, room_id, nats_service, subject_manager)
    if not success:
        # NATS publishing failed - detailed error already logged in _publish_chat_message_to_nats
        logger.error(
            "NATS publishing failed - NATS is mandatory for chat functionality",
            player_id=player_id,
            player_name=player.name,
            room_id=room_id,
            message_id=chat_message.id,
        )
        return {"success": False, "error": "Chat system temporarily unavailable. Please try again in a moment."}
    logger.debug("=== CHAT SERVICE DEBUG: NATS publishing completed ===")

    return {"success": True, "pose": pose.strip(), "room_id": room_id}


def get_player_pose(player_id: uuid.UUID | str, pose_manager: Any) -> str | None:
    """
    Get a player's current pose.

    Args:
        player_id: ID of the player
        pose_manager: Pose manager instance

    Returns:
        Current pose description or None if no pose set
    """
    return pose_manager.get_pose(player_id)


def clear_player_pose(player_id: uuid.UUID | str, pose_manager: Any) -> bool:
    """
    Clear a player's pose.

    Args:
        player_id: ID of the player
        pose_manager: Pose manager instance

    Returns:
        True if pose was cleared, False if no pose was set
    """
    return pose_manager.clear_pose(player_id)


async def get_room_poses(room_id: str, room_service: Any, player_service: Any, pose_manager: Any) -> dict[str, str]:
    """
    Get all poses for players in a room.

    Args:
        room_id: ID of the room
        room_service: Room service instance
        player_service: Player service instance
        pose_manager: Pose manager instance

    Returns:
        Dictionary mapping player names to their poses
    """
    poses = {}
    room_players = await room_service.get_room_occupants(room_id)

    for player_id in room_players:
        pose = pose_manager.get_pose(player_id)
        if pose:
            player = await player_service.get_player_by_id(player_id)
            if player:
                poses[player.name] = pose

    return poses
