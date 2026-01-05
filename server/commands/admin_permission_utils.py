"""
Admin permission validation utilities for MythosMUD.

This module provides utilities for validating admin permissions.
"""

from typing import Any

from ..structured_logging.admin_actions_logger import get_admin_actions_logger
from ..structured_logging.enhanced_logging_config import get_logger

logger = get_logger(__name__)


async def validate_admin_permission(player: Any, player_name: str) -> bool:
    """
    Validate that a player has admin permissions.

    Args:
        player: Player object to check
        player_name: Player name for logging

    Returns:
        bool: True if player has admin permissions, False otherwise
    """
    try:
        if not player:
            logger.warning("Admin permission check failed - no player object", player_name=player_name)

            # Log the failed permission check
            admin_logger = get_admin_actions_logger()
            admin_logger.log_permission_check(
                player_name=player_name,
                action="admin_teleport",
                has_permission=False,
                additional_data={"error": "No player object"},
            )
            return False

        # Check if player has admin privileges
        if not hasattr(player, "is_admin") or not player.is_admin:
            # Determine the specific reason for failure
            if not hasattr(player, "is_admin"):
                error_msg = "No is_admin attribute"
                logger.warning(
                    "Admin permission check failed - player has no is_admin attribute", player_name=player_name
                )
                additional_data = {"error": error_msg, "player_type": type(player).__name__}
            else:
                error_msg = f"is_admin value: {player.is_admin}"
                logger.info("Admin permission denied", player_name=player_name, error_msg=error_msg)
                additional_data = {"player_type": type(player).__name__, "is_admin_value": player.is_admin}

            # Log the failed permission check
            admin_logger = get_admin_actions_logger()
            admin_logger.log_permission_check(
                player_name=player_name,
                action="admin_teleport",
                has_permission=False,
                additional_data=additional_data,
            )
            return False

        # Log the successful permission check
        admin_logger = get_admin_actions_logger()
        admin_logger.log_permission_check(
            player_name=player_name,
            action="admin_teleport",
            has_permission=True,
            additional_data={"player_type": type(player).__name__, "is_admin_value": player.is_admin},
        )

        logger.info("Admin permission granted", player_name=player_name, is_admin_value=player.is_admin)
        return True

    except (AttributeError, TypeError, OSError) as e:
        logger.error("Error checking admin permissions", player_name=player_name, error=str(e))

        # Log the failed permission check
        try:
            admin_logger = get_admin_actions_logger()
            admin_logger.log_permission_check(
                player_name=player_name,
                action="admin_teleport",
                has_permission=False,
                additional_data={"error": str(e), "player_type": type(player).__name__ if player else "None"},
            )
        except (OSError, AttributeError, TypeError) as log_error:
            logger.error("Failed to log permission check error", error=str(log_error))

        return False


__all__ = ["validate_admin_permission"]
