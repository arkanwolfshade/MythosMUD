"""
Status command handlers for MythosMUD.

This module contains handlers for status and whoami commands.
"""

from typing import Any

from ..alias_storage import AliasStorage
from ..logging.enhanced_logging_config import get_logger
from ..utils.command_parser import get_username_from_user

logger = get_logger(__name__)


async def _get_profession_info(player: Any, persistence: Any) -> dict[str, Any]:
    """
    Get profession information for a player.

    Args:
        player: Player object
        persistence: Persistence layer instance

    Returns:
        dict: Profession information with name, description, and flavor_text
    """
    profession_id: int | None = 0
    if hasattr(player, "profession_id"):
        attr_value = getattr(player, "profession_id", None)
        profession_id = attr_value if attr_value is not None else 0
    elif isinstance(player, dict):
        profession_id = player.get("profession_id", 0)

    # Mypy: profession_id can be 0 but not None at this point
    if profession_id == 0:
        return {"name": None, "description": None, "flavor_text": None}

    try:
        profession = await persistence.get_profession_by_id(profession_id)
        if profession:
            return {
                "name": profession.name,
                "description": profession.description,
                "flavor_text": profession.flavor_text,
            }
    except (AttributeError, TypeError) as e:
        logger.warning("Failed to fetch profession", profession_id=profession_id, error=str(e))

    return {"name": None, "description": None, "flavor_text": None}


async def _get_combat_status(app: Any, player: Any) -> bool:
    """
    Check if player is in combat.

    Args:
        app: FastAPI app instance
        player: Player object

    Returns:
        bool: True if player is in combat, False otherwise
    """
    combat_service = app.state.combat_service if app else None
    if not combat_service:
        logger.debug("No combat service available")
        return False

    logger.debug("Checking combat status for player", player_id=player.player_id)
    combat = await combat_service.get_combat_by_participant(player.player_id)
    logger.debug("Combat result for player", player_id=player.player_id, combat=combat)
    in_combat = combat is not None
    logger.debug("Player combat status", player_id=player.player_id, in_combat=in_combat)
    return in_combat


def _build_base_status_lines(player: Any, room_name: str, stats: dict, in_combat: bool) -> list[str]:
    """
    Build base status lines for the status command.

    Args:
        player: Player object
        room_name: Room name string
        stats: Player stats dictionary
        in_combat: Whether player is in combat

    Returns:
        list: Base status lines
    """
    position_value = str(stats.get("position", "standing")).lower()
    position_label = position_value.replace("_", " ").capitalize()

    return [
        f"Name: {player.name}",
        f"Location: {room_name}",
        f"Position: {position_label}",
        f"Health: {stats.get('current_dp', 100)}/{stats.get('max_dp', 100)}",
        f"lucidity: {stats.get('lucidity', 100)}/{stats.get('max_lucidity', 100)}",
        f"XP: {player.experience_points}",
        f"In Combat: {'Yes' if in_combat else 'No'}",
    ]


def _add_profession_lines(status_lines: list[str], profession_info: dict[str, Any]) -> None:
    """
    Add profession information lines to status lines.

    Args:
        status_lines: List of status lines to append to
        profession_info: Dictionary with profession name, description, and flavor_text
    """
    profession_name = profession_info.get("name")
    if not profession_name:
        return

    status_lines.append(f"Profession: {profession_name}")

    profession_description = profession_info.get("description")
    if profession_description:
        status_lines.append(f"Description: {profession_description}")

    profession_flavor_text = profession_info.get("flavor_text")
    if profession_flavor_text:
        status_lines.append(f"Background: {profession_flavor_text}")


def _add_additional_stats_lines(status_lines: list[str], stats: dict) -> None:
    """
    Add additional stats lines to status lines if they have non-zero values.

    Args:
        status_lines: List of status lines to append to
        stats: Player stats dictionary
    """
    if stats.get("fear", 0) > 0:
        status_lines.append(f"Fear: {stats.get('fear', 0)}")

    if stats.get("corruption", 0) > 0:
        status_lines.append(f"Corruption: {stats.get('corruption', 0)}")

    if stats.get("occult_knowledge", 0) > 0:
        status_lines.append(f"Occult Knowledge: {stats.get('occult_knowledge', 0)}")


async def handle_status_command(
    command_data: dict, current_user: dict, request: Any, _alias_storage: AliasStorage | None, player_name: str
) -> dict[str, str]:
    """
    Handle the status command for showing player status.

    Args:
        command_data: Command data dictionary containing args and other info
        current_user: Current user information
        request: FastAPI request object
        _alias_storage: Alias storage instance (unused, required by interface)
        player_name: Player name for logging

    Returns:
        dict: Status command result
    """
    # Extract args from command_data (not used in this command)
    _args: list = command_data.get("args", [])

    logger.debug("Processing status command", player=player_name)

    app = request.app if request else None
    persistence = app.state.persistence if app else None

    if not persistence:
        logger.warning("Status command failed - no persistence layer", player=player_name)
        return {"result": "Status information is not available."}

    try:
        player = await persistence.get_player_by_name(get_username_from_user(current_user))
        if not player:
            logger.warning("Status command failed - player not found", player=player_name)
            return {"result": "Player information not found."}

        room = persistence.get_room_by_id(player.current_room_id) if player.current_room_id else None
        room_name = room.name if room else "Unknown location"
        stats = player.get_stats()

        profession_info = await _get_profession_info(player, persistence)
        in_combat = await _get_combat_status(app, player)

        status_lines = _build_base_status_lines(player, room_name, stats, in_combat)
        _add_profession_lines(status_lines, profession_info)
        _add_additional_stats_lines(status_lines, stats)

        result = "\n".join(status_lines)
        logger.debug("Status command successful", player=player_name)
        return {"result": result}
    except (AttributeError, TypeError) as e:
        logger.error("Status command error", player=player_name, error=str(e))
        return {"result": f"Error retrieving status information: {str(e)}"}


async def handle_whoami_command(
    command_data: dict, current_user: dict, request: Any, alias_storage: AliasStorage | None, player_name: str
) -> dict[str, str]:
    """
    Handle the whoami command as an alias for status.

    Mirrors handle_status_command while providing additional logging context.
    """
    logger.debug("Processing whoami command as status alias", player=player_name)

    result = await handle_status_command(command_data, current_user, request, alias_storage, player_name)
    # Annotate response to clarify alias usage
    if "result" in result and isinstance(result["result"], str):
        result["result"] = result["result"]
    logger.debug("Whoami command completed", player=player_name)
    return result
