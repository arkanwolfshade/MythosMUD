"""
Chat pose management utilities.

This module provides pose management functionality for players,
handling in-memory storage of player poses.
"""

# pylint: disable=wrong-import-position  # Reason: Import after TYPE_CHECKING block is intentional to avoid circular dependencies

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from uuid import UUID

from ..structured_logging.enhanced_logging_config import get_logger

logger = get_logger("communications.chat_pose_manager")


class ChatPoseManager:
    """Manages in-memory storage of player poses."""

    def __init__(self) -> None:
        """Initialize the pose manager."""
        self._poses: dict[str, str] = {}

    def normalize_player_id(self, player_id: "UUID | str") -> str:
        """Normalize player identifiers to string form."""
        return str(player_id)

    def set_pose(self, player_id: "UUID | str", pose: str) -> None:
        """
        Set a player's pose in memory.

        Args:
            player_id: ID of the player
            pose: Pose description
        """
        player_id_str = self.normalize_player_id(player_id)
        self._poses[player_id_str] = pose.strip()
        logger.debug("Player pose set", player_id=player_id_str, pose=pose.strip())

    def get_pose(self, player_id: "UUID | str") -> str | None:
        """
        Get a player's current pose.

        Args:
            player_id: ID of the player

        Returns:
            Current pose description or None if no pose set
        """
        player_id_str = self.normalize_player_id(player_id)
        return self._poses.get(player_id_str)

    def clear_pose(self, player_id: "UUID | str") -> bool:
        """
        Clear a player's pose.

        Args:
            player_id: ID of the player

        Returns:
            True if pose was cleared, False if no pose was set
        """
        player_id_str = self.normalize_player_id(player_id)
        if player_id_str in self._poses:
            del self._poses[player_id_str]
            logger.debug("Player pose cleared", player_id=player_id_str)
            return True
        return False

    def get_all_poses(self) -> dict[str, str]:
        """
        Get all poses (for testing/debugging).

        Returns:
            Dictionary mapping player IDs to poses
        """
        return self._poses.copy()
