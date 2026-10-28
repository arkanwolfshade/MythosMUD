"""NPC behavior control commands (behavior, react, stop)."""

from typing import Any

from ...alias_storage import AliasStorage
from ...services.npc_instance_service import get_npc_instance_service
from ...structured_logging.enhanced_logging_config import get_logger
from ..command_results import command_error

logger = get_logger(__name__)


async def handle_npc_behavior_command(
    command_data: dict[str, Any],
    _current_user: dict[str, Any],
    _request: Any,
    _alias_storage: AliasStorage | None,
    player_name: str,
) -> dict[str, str]:
    """Handle NPC behavior control command."""
    logger.debug("Processing NPC behavior command", player_name=player_name)

    args = command_data.get("args", [])
    if len(args) < 3:
        return command_error("Usage: npc behavior <npc_id> <behavior_type>")

    npc_id = args[1]
    behavior_type = args[2]

    valid_behaviors = ["passive", "aggressive", "defensive", "wander", "patrol", "guard", "idle"]
    if behavior_type.lower() not in valid_behaviors:
        return command_error(f"Invalid behavior type: {behavior_type}. Valid types: {', '.join(valid_behaviors)}")

    try:
        _instance_service = get_npc_instance_service()
        return command_error("NPC behavior modification not yet implemented")

    except Exception as e:  # noqa: B904,BLE001  # pylint: disable=broad-exception-caught
        logger.error("Error setting NPC behavior", npc_id=npc_id, admin_name=player_name, error=str(e))
        return command_error(f"Error setting NPC behavior: {str(e)}")


async def handle_npc_react_command(
    command_data: dict[str, Any],
    _current_user: dict[str, Any],
    _request: Any,
    _alias_storage: AliasStorage | None,
    player_name: str,
) -> dict[str, str]:
    """Handle NPC reaction trigger command."""
    logger.debug("Processing NPC react command", player_name=player_name)

    args = command_data.get("args", [])
    if len(args) < 3:
        return command_error("Usage: npc react <npc_id> <reaction_type>")

    npc_id = args[1]
    reaction_type = args[2]

    valid_reactions = ["greet", "attack", "flee", "investigate", "alert", "calm", "excited", "suspicious"]
    if reaction_type.lower() not in valid_reactions:
        return command_error(f"Invalid reaction type: {reaction_type}. Valid types: {', '.join(valid_reactions)}")

    try:
        _instance_service = get_npc_instance_service()
        return command_error("NPC reaction triggering not yet implemented")

    except Exception as e:  # noqa: B904,BLE001  # pylint: disable=broad-exception-caught
        logger.error("Error triggering NPC reaction", npc_id=npc_id, admin_name=player_name, error=str(e))
        return command_error(f"Error triggering NPC reaction: {str(e)}")


async def handle_npc_stop_command(
    command_data: dict[str, Any],
    _current_user: dict[str, Any],
    _request: Any,
    _alias_storage: AliasStorage | None,
    player_name: str,
) -> dict[str, str]:
    """Handle NPC behavior stop command."""
    logger.debug("Processing NPC stop command", player_name=player_name)

    args = command_data.get("args", [])
    if len(args) < 2:
        return command_error("Usage: npc stop <npc_id>")

    npc_id = args[1]

    try:
        _instance_service = get_npc_instance_service()
        return command_error("NPC behavior stopping not yet implemented")

    except Exception as e:  # noqa: B904,BLE001  # pylint: disable=broad-exception-caught
        logger.error("Error stopping NPC behavior", npc_id=npc_id, admin_name=player_name, error=str(e))
        return command_error(f"Error stopping NPC behavior: {str(e)}")
