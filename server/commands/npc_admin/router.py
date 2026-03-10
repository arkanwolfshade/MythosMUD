"""NPC admin command router and permission validation."""

import inspect
from typing import TYPE_CHECKING, Any, cast

from ...alias_storage import AliasStorage
from ...structured_logging.enhanced_logging_config import get_logger

if TYPE_CHECKING:
    from ...models.player import Player

logger = get_logger(__name__)


def validate_npc_admin_permission(player: "Player | Any", player_name: str) -> bool:
    """
    Validate that a player has NPC admin permissions.

    Args:
        player: Player object to check
        player_name: Player name for logging

    Returns:
        bool: True if player has NPC admin permissions, False otherwise
    """
    try:
        if not player:
            logger.warning("NPC admin permission check failed - no player object", player_name=player_name)
            return False

        try:
            is_admin = player.is_admin
            if not is_admin:
                logger.warning("NPC admin permission check failed - player is not an admin", player_name=player_name)
                return False
        except (AttributeError, TypeError) as e:
            logger.error("Error checking NPC admin permission", player_name=player_name, error=str(e))
            return False

        logger.debug("NPC admin permission check passed", player_name=player_name)
        return True

    except (AttributeError, TypeError, ValueError) as e:
        logger.error("Error checking NPC admin permission", player_name=player_name, error=str(e))
        return False


async def _resolve_npc_command_player(request: Any, player_name: str) -> tuple[Any, str | None]:
    """
    Resolve player for NPC command. Returns (player_obj, error).
    If error is set, caller should return {"result": error}.
    """
    app = request.app if request else None
    player_service = app.state.player_service if app else None
    if not player_service:
        logger.warning("NPC command failed - no player service", player_name=player_name)
        return (None, "NPC functionality is not available.")

    _maybe_coro = player_service.resolve_player_name(player_name)
    player_obj = await _maybe_coro if inspect.isawaitable(_maybe_coro) else _maybe_coro
    if not player_obj:
        logger.warning("NPC command failed - player not found", player_name=player_name)
        return (None, "Player not found.")

    if not validate_npc_admin_permission(player_obj, player_name):
        return (None, "You do not have permission to use NPC admin commands.")

    return (player_obj, None)


def _get_npc_help() -> dict[str, str]:
    """Get NPC admin command help text."""
    help_text = """
NPC Admin Commands
==================

Usage: npc <subcommand> [arguments]

Available subcommands:

Definition Management:
  create <name> <type> <sub_zone_id> <room_id>  - Create a new NPC definition
  edit <id> <field> <value>                     - Edit an NPC definition
  delete <id>                                   - Delete an NPC definition
  list                                          - List all NPC definitions

Instance Management:
  spawn <definition_id|name> [quantity] [room_id] - Spawn NPC(s); name supports quantity; room_id defaults to current room
  despawn <npc_id>                              - Despawn an NPC instance
  move <npc_id> <room_id>                       - Move an NPC instance
  stats <npc_id>                                - Get NPC instance stats

Monitoring:
  population                                    - Get NPC population statistics
  zone [zone_key]                               - Get NPC zone statistics
  status                                        - Get NPC system status

Behavior Control:
  behavior <npc_id> <behavior_type>             - Set NPC behavior type
  react <npc_id> <reaction_type>                - Trigger NPC reaction
  stop <npc_id>                                 - Stop NPC current behavior

Testing/Debugging:
  test-occupants [room_id]                      - Test occupant query for a room (uses current room if not specified)

Help:
  help                                          - Show this help message

NPC Types: shopkeeper, passive_mob, aggressive_mob, quest_giver, merchant
"""
    return {"result": help_text.strip()}


def _extract_npc_subcommand(command_data: dict[str, Any]) -> tuple[str | None, list[str], dict[str, str] | None]:
    """
    Extract subcommand and normalize args. Returns (subcommand, args, help_result).
    If help_result is set, caller should return it (no subcommand to run).
    """
    args = command_data.get("args", [])
    subcommand = command_data.get("subcommand")
    if subcommand:
        subcommand = subcommand.lower()
        args = [subcommand] + args
        command_data["args"] = args
    elif args:
        subcommand = args[0].lower()
    else:
        return (None, [], _get_npc_help())
    return (subcommand, args, None)


def _build_subcommand_map() -> dict[str, Any]:
    """Build subcommand to handler mapping. Lazy imports avoid circular dependencies."""
    from .behavior import (
        handle_npc_behavior_command,
        handle_npc_react_command,
        handle_npc_stop_command,
    )
    from .definition import (
        handle_npc_create_command,
        handle_npc_delete_command,
        handle_npc_edit_command,
        handle_npc_list_command,
    )
    from .instance import (
        handle_npc_despawn_command,
        handle_npc_move_command,
        handle_npc_spawn_command,
        handle_npc_stats_command,
    )
    from .monitoring import (
        handle_npc_population_command,
        handle_npc_status_command,
        handle_npc_zone_command,
    )
    from .test_occupants import handle_npc_test_occupants_command

    return {
        "help": _get_npc_help,
        "create": handle_npc_create_command,
        "edit": handle_npc_edit_command,
        "delete": handle_npc_delete_command,
        "list": handle_npc_list_command,
        "spawn": handle_npc_spawn_command,
        "despawn": handle_npc_despawn_command,
        "move": handle_npc_move_command,
        "stats": handle_npc_stats_command,
        "population": handle_npc_population_command,
        "zone": handle_npc_zone_command,
        "status": handle_npc_status_command,
        "behavior": handle_npc_behavior_command,
        "react": handle_npc_react_command,
        "stop": handle_npc_stop_command,
        "test-occupants": handle_npc_test_occupants_command,
    }


async def _invoke_npc_handler(
    handler: Any,
    subcommand: str,
    command_data: dict[str, Any],
    current_user: dict[str, Any],
    request: Any,
    alias_storage: AliasStorage | None,
    player_name: str,
) -> dict[str, str]:
    """Invoke the handler for the given subcommand."""
    if subcommand == "help":
        return cast(dict[str, str], handler())
    return cast(
        dict[str, str],
        await handler(command_data, current_user, request, alias_storage, player_name),
    )


async def handle_npc_command(
    command_data: dict[str, Any],
    current_user: dict[str, Any],
    request: Any,
    alias_storage: AliasStorage | None,
    player_name: str,
) -> dict[str, str]:
    """
    Handle the main NPC admin command with subcommand routing.

    Args:
        command_data: Command data dictionary containing validated command information
        current_user: Current user information
        request: FastAPI request object
        alias_storage: Alias storage instance
        player_name: Player name for logging

    Returns:
        dict: NPC command result
    """
    logger.debug("Processing NPC command", player_name=player_name, command_data=command_data)

    _, player_error = await _resolve_npc_command_player(request, player_name)
    if player_error:
        return {"result": player_error}

    subcommand, _args, help_result = _extract_npc_subcommand(command_data)
    if help_result is not None:
        return help_result
    if subcommand is None:
        return {"result": "Unknown NPC command. Use 'npc help' for available commands."}

    subcommand_map = _build_subcommand_map()
    handler = subcommand_map.get(subcommand)
    if not handler:
        return {"result": f"Unknown NPC command: {subcommand}. Use 'npc help' for available commands."}
    return await _invoke_npc_handler(
        handler, subcommand, command_data, current_user, request, alias_storage, player_name
    )
