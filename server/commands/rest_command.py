"""
Rest command handler for MP and health recovery.

This module handles the /rest command for accelerated MP regeneration
while in a resting position (sitting or lying).
"""

from typing import Any

from server.alias_storage import AliasStorage
from server.logging.enhanced_logging_config import get_logger
from server.utils.command_parser import get_username_from_user

logger = get_logger(__name__)


async def handle_rest_command(
    command_data: dict,
    current_user: dict,
    request: Any,
    _alias_storage: AliasStorage | None,
    player_name: str,
) -> dict[str, str]:
    """
    Handle /rest command for MP regeneration.

    Usage: /rest [duration]
    Duration defaults to 60 seconds if not specified.

    Args:
        command_data: Command data dictionary
        current_user: Current user information
        request: FastAPI request object
        alias_storage: Alias storage instance
        player_name: Player name

    Returns:
        dict: Command result
    """
    logger.debug("Handling rest command", player_name=player_name, command_data=command_data)

    # Get services from app state
    app = request.app if request else None
    if not app:
        return {"result": "System error: application not available."}

    persistence = getattr(app.state, "persistence", None)
    mp_regeneration_service = getattr(app.state, "mp_regeneration_service", None)

    if not persistence:
        return {"result": "System error: persistence layer not available."}

    if not mp_regeneration_service:
        return {"result": "MP regeneration system not initialized."}

    # Get player
    player = await persistence.get_player_by_name(get_username_from_user(current_user))
    if not player:
        return {"result": "You are not recognized by the cosmic forces."}

    # Check player position (must be sitting or lying to rest effectively)
    stats = player.get_stats()
    position = stats.get("position", "standing")

    if position not in ("sitting", "lying"):
        return {"result": "You must be sitting or lying down to rest effectively. Use /sit or /lie first."}

    # Get duration (default 60 seconds)
    duration = command_data.get("duration", 60)
    try:
        duration = int(duration)
        if duration < 1:
            duration = 60
        if duration > 300:  # Cap at 5 minutes
            duration = 300
    except (ValueError, TypeError):
        duration = 60

    # Restore MP
    result = await mp_regeneration_service.restore_mp_from_rest(player.player_id, duration)

    if not result.get("success"):
        return {"result": result.get("message", "Rest failed.")}

    return {"result": result.get("message", "You rest and recover.")}
