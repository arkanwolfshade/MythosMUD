"""
NPC Admin Commands for MythosMUD.

This module provides administrative slash commands for managing NPCs,
including CRUD operations for NPC definitions, instance management,
population monitoring, and relationship management.

As documented in the Cultes des Goules, proper administrative protocols
are essential for maintaining control over the eldritch entities that
lurk in the shadows of our world.
"""

# pylint: disable=too-many-return-statements,too-many-lines  # Reason: Command handlers require multiple return statements for early validation returns (input validation, permission checks, error handling). NPC admin commands require extensive handlers for comprehensive NPC management operations.

import inspect
from typing import TYPE_CHECKING, Any, cast

from ..alias_storage import AliasStorage
from ..models.npc import NPCDefinitionType
from ..services.npc_instance_service import get_npc_instance_service
from ..services.npc_service import npc_service
from ..structured_logging.enhanced_logging_config import get_logger

if TYPE_CHECKING:
    from ..models.player import Player
logger = get_logger(__name__)


# --- Permission Validation ---


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

        # Check if player has admin privileges
        # Use try-except to catch exceptions when accessing is_admin (e.g., if it's a property that raises)
        try:
            # Access is_admin directly to catch any exceptions
            is_admin = player.is_admin
            if not is_admin:
                logger.warning("NPC admin permission check failed - player is not an admin", player_name=player_name)
                return False
        except (AttributeError, TypeError) as e:
            # If accessing is_admin raises AttributeError or TypeError, log it as an error and return False
            # Catching specific exceptions here since is_admin might be a property that raises
            logger.error("Error checking NPC admin permission", player_name=player_name, error=str(e))
            return False

        logger.debug("NPC admin permission check passed", player_name=player_name)
        return True

    except (AttributeError, TypeError, ValueError) as e:
        # Catching specific exceptions for player object access issues
        logger.error("Error checking NPC admin permission", player_name=player_name, error=str(e))
        return False


# --- Main NPC Command Handler ---


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

    # Get player object for permission check
    app = request.app if request else None
    player_service = app.state.player_service if app else None

    if not player_service:
        logger.warning("NPC command failed - no player service", player_name=player_name)
        return {"result": "NPC functionality is not available."}

    # Get player object (supports sync or async implementations)
    _maybe_coro = player_service.resolve_player_name(player_name)
    player_obj = await _maybe_coro if inspect.isawaitable(_maybe_coro) else _maybe_coro
    if not player_obj:
        logger.warning("NPC command failed - player not found", player_name=player_name)
        return {"result": "Player not found."}

    # Check admin permission
    if not validate_npc_admin_permission(player_obj, player_name):
        return {"result": "You do not have permission to use NPC admin commands."}

    # Extract subcommand - command_service reconstructs args to include subcommand as first element
    # So we can extract from either args[0] or command_data.subcommand
    args = command_data.get("args", [])
    if not args:
        # No args - show help
        return _get_npc_help()

    # Subcommand is first arg (command_service ensures this)
    subcommand = args[0].lower()
    # Keep args as-is for subcommand handlers (they expect args[0] = subcommand, args[1] = first arg, etc.)
    # This maintains backward compatibility with existing subcommand handlers

    # Route to appropriate subcommand handler
    async def _route_npc_subcommand() -> dict[str, str]:
        """Route to the appropriate NPC subcommand handler."""
        subcommand_map = {
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

        handler = subcommand_map.get(subcommand)
        if handler:
            if subcommand == "help":
                return cast(dict[str, str], handler())  # type: ignore[operator]  # Handler is a callable from the map with unknown signature
            return cast(dict[str, str], await handler(command_data, current_user, request, alias_storage, player_name))  # type: ignore[operator]  # Handler is a callable from the map with unknown signature
        return {"result": f"Unknown NPC command: {subcommand}. Use 'npc help' for available commands."}

    return await _route_npc_subcommand()


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
  spawn <definition_id> <room_id>               - Spawn an NPC instance
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


# --- NPC Definition Management Commands ---


async def handle_npc_create_command(
    command_data: dict[str, Any],
    _current_user: dict[str, Any],
    request: Any,
    _alias_storage: AliasStorage | None,
    player_name: str,
) -> dict[str, str]:
    """Handle NPC creation command."""
    logger.debug("Processing NPC create command", player_name=player_name)

    args = command_data.get("args", [])
    if len(args) < 5:
        return {"result": "Usage: npc create <name> <type> <sub_zone_id> <room_id>"}

    name = args[1]
    npc_type_str = args[2]
    sub_zone_id = args[3]
    room_id = args[4]

    # Validate NPC type
    try:
        npc_type = NPCDefinitionType(npc_type_str)
    except ValueError:
        valid_types = [t.value for t in NPCDefinitionType]
        return {"result": f"Invalid NPC type: {npc_type_str}. Valid types: {', '.join(valid_types)}"}

    try:
        # Get database session
        app = request.app if request else None
        if not app or not hasattr(app.state, "db_session_maker"):
            return {"result": "Database not available."}

        async with app.state.db_session_maker() as session:
            # Create NPC definition
            definition = await npc_service.create_npc_definition(
                session=session,
                name=name,
                description=None,  # Description can be set later via npc modify
                npc_type=npc_type,
                sub_zone_id=sub_zone_id,
                room_id=room_id,
                base_stats={},
                behavior_config={},
                ai_integration_stub={},
            )

            logger.info("NPC created successfully", npc_name=name, admin_name=player_name, npc_id=definition.id)
            return {"result": f"NPC '{name}' created successfully with ID {definition.id}"}

    except Exception as e:  # noqa: B904,BLE001  # pylint: disable=broad-exception-caught  # Reason: NPC creation errors unpredictable, must return user-friendly error
        # Catching broad Exception to handle database errors, validation errors, and service errors
        # and return user-friendly error messages
        logger.error("Error creating NPC", admin_name=player_name, error=str(e))
        return {"result": f"Error creating NPC: {str(e)}"}


async def handle_npc_edit_command(
    command_data: dict[str, Any],
    _current_user: dict[str, Any],
    request: Any,
    _alias_storage: AliasStorage | None,
    player_name: str,
) -> dict[str, str]:
    """Handle NPC editing command."""
    logger.debug("Processing NPC edit command", player_name=player_name)

    args = command_data.get("args", [])
    if len(args) < 4:
        return {"result": "Usage: npc edit <id> <field> <value>"}

    try:
        npc_id = int(args[1])
    except ValueError:
        return {"result": f"Invalid NPC ID: {args[1]}"}

    field = args[2]
    value = args[3]

    # Validate field
    valid_fields = ["name", "npc_type", "sub_zone_id", "room_id"]
    if field not in valid_fields:
        return {"result": f"Invalid field: {field}. Valid fields: {', '.join(valid_fields)}"}

    # Validate npc_type if field is npc_type
    if field == "npc_type":
        try:
            value = NPCDefinitionType(value)
        except ValueError:
            valid_types = [t.value for t in NPCDefinitionType]
            return {"result": f"Invalid NPC type: {value}. Valid types: {', '.join(valid_types)}"}

    try:
        # Get database session
        app = request.app if request else None
        if not app or not hasattr(app.state, "db_session_maker"):
            return {"result": "Database not available."}

        async with app.state.db_session_maker() as session:
            # Update NPC definition
            definition = await npc_service.update_npc_definition(
                session=session, definition_id=npc_id, **{field: value}
            )

            if not definition:
                return {"result": f"NPC definition {npc_id} not found"}

            logger.info("NPC definition updated", npc_id=npc_id, admin_name=player_name, field=field, value=value)
            return {"result": f"NPC definition {npc_id} updated successfully"}

    except Exception as e:  # noqa: B904,BLE001  # pylint: disable=broad-exception-caught  # Reason: NPC creation errors unpredictable, must return user-friendly error
        # Catching broad Exception to handle database errors, validation errors, and service errors
        # and return user-friendly error messages
        logger.error("Error editing NPC", npc_id=npc_id, admin_name=player_name, error=str(e))
        return {"result": f"Error editing NPC: {str(e)}"}


async def handle_npc_delete_command(
    command_data: dict[str, Any],
    _current_user: dict[str, Any],
    request: Any,
    _alias_storage: AliasStorage | None,
    player_name: str,
) -> dict[str, str]:
    """Handle NPC deletion command."""
    logger.debug("Processing NPC delete command", player_name=player_name)

    args = command_data.get("args", [])
    if len(args) < 2:
        return {"result": "Usage: npc delete <id>"}

    try:
        npc_id = int(args[1])
    except ValueError:
        return {"result": f"Invalid NPC ID: {args[1]}"}

    try:
        # Get database session
        app = request.app if request else None
        if not app or not hasattr(app.state, "db_session_maker"):
            return {"result": "Database not available."}

        async with app.state.db_session_maker() as session:
            # Delete NPC definition
            deleted = await npc_service.delete_npc_definition(session, npc_id)

            if not deleted:
                return {"result": f"NPC definition {npc_id} not found"}

            logger.info("NPC definition deleted", npc_id=npc_id, admin_name=player_name)
            return {"result": f"NPC definition {npc_id} deleted successfully"}

    except Exception as e:  # noqa: B904,BLE001  # pylint: disable=broad-exception-caught  # Reason: NPC creation errors unpredictable, must return user-friendly error
        # Catching broad Exception to handle database errors, validation errors, and service errors
        # and return user-friendly error messages
        logger.error("Error deleting NPC", npc_id=npc_id, admin_name=player_name, error=str(e))
        return {"result": f"Error deleting NPC: {str(e)}"}


async def handle_npc_list_command(
    _command_data: dict[str, Any],
    _current_user: dict[str, Any],
    request: Any,
    _alias_storage: AliasStorage | None,
    player_name: str,
) -> dict[str, str]:
    """Handle NPC listing command."""
    logger.debug("Processing NPC list command", player_name=player_name)

    try:
        # Get database session
        app = request.app if request else None
        if not app or not hasattr(app.state, "db_session_maker"):
            return {"result": "Database not available."}

        async with app.state.db_session_maker() as session:
            # Get NPC definitions
            definitions = await npc_service.get_npc_definitions(session)

            if not definitions:
                return {"result": "No NPC definitions found"}

            # Format output
            result_lines = ["NPC Definitions:"]
            for definition in definitions:
                result_lines.append(f"  ID {definition.id}: {definition.name} ({definition.npc_type})")
                result_lines.append(f"    Zone: {definition.sub_zone_id}, Room: {definition.room_id}")

            logger.info("NPC definitions listed", admin_name=player_name, count=len(definitions))
            return {"result": "\n".join(result_lines)}

    except Exception as e:  # noqa: B904,BLE001  # pylint: disable=broad-exception-caught  # Reason: NPC listing errors unpredictable (database, service, validation), must return user-friendly error messages
        # Catching broad Exception to handle database errors and service errors
        # and return user-friendly error messages
        logger.error("Error listing NPCs", admin_name=player_name, error=str(e))
        return {"result": f"Error listing NPCs: {str(e)}"}


# --- NPC Instance Management Commands ---


async def handle_npc_spawn_command(
    command_data: dict[str, Any],
    _current_user: dict[str, Any],
    _request: Any,
    _alias_storage: AliasStorage | None,
    player_name: str,
) -> dict[str, str]:
    """Handle NPC spawning command."""
    logger.debug("Processing NPC spawn command", player_name=player_name)

    args = command_data.get("args", [])
    if len(args) < 3:
        return {"result": "Usage: npc spawn <definition_id> <room_id>"}

    try:
        definition_id = int(args[1])
    except ValueError:
        return {"result": f"Invalid definition ID: {args[1]}"}

    room_id = args[2]

    try:
        # Get NPC instance service
        instance_service = get_npc_instance_service()

        # Spawn NPC instance
        await instance_service.spawn_npc_instance(definition_id, room_id)

        logger.info("NPC spawned", admin_name=player_name, definition_id=definition_id, room_id=room_id)
        return {"result": f"NPC spawned successfully in {room_id}"}

    except Exception as e:  # noqa: B904,BLE001  # pylint: disable=broad-exception-caught  # Reason: NPC spawning errors unpredictable (service, validation, instance management), must return user-friendly error messages
        # Catching broad Exception to handle service errors, validation errors, and instance management errors
        # and return user-friendly error messages
        logger.error("Error spawning NPC", admin_name=player_name, error=str(e))
        return {"result": f"Error spawning NPC: {str(e)}"}


async def handle_npc_despawn_command(
    command_data: dict[str, Any],
    _current_user: dict[str, Any],
    _request: Any,
    _alias_storage: AliasStorage | None,
    player_name: str,
) -> dict[str, str]:
    """Handle NPC despawning command."""
    logger.debug("Processing NPC despawn command", player_name=player_name)

    args = command_data.get("args", [])
    if len(args) < 2:
        return {"result": "Usage: npc despawn <npc_id>"}

    npc_id = args[1]

    try:
        # Get NPC instance service
        instance_service = get_npc_instance_service()

        # Despawn NPC instance
        result = await instance_service.despawn_npc_instance(npc_id)

        if not result:
            return {"result": f"NPC {npc_id} not found or already despawned"}

        logger.info("NPC despawned", npc_id=npc_id, admin_name=player_name)
        return {"result": f"NPC {npc_id} despawned successfully"}

    except Exception as e:  # noqa: B904,BLE001  # pylint: disable=broad-exception-caught  # Reason: NPC despawning errors unpredictable (service, instance management), must return user-friendly error messages
        # Catching broad Exception to handle service errors and instance management errors
        # and return user-friendly error messages
        logger.error("Error despawning NPC", npc_id=npc_id, admin_name=player_name, error=str(e))
        return {"result": f"Error despawning NPC: {str(e)}"}


async def handle_npc_move_command(
    command_data: dict[str, Any],
    _current_user: dict[str, Any],
    _request: Any,
    _alias_storage: AliasStorage | None,
    player_name: str,
) -> dict[str, str]:
    """Handle NPC movement command."""
    logger.debug("Processing NPC move command", player_name=player_name)

    args = command_data.get("args", [])
    if len(args) < 3:
        return {"result": "Usage: npc move <npc_id> <room_id>"}

    npc_id = args[1]
    room_id = args[2]

    try:
        # Get NPC instance service
        instance_service = get_npc_instance_service()

        # Move NPC instance
        result = await instance_service.move_npc_instance(npc_id, room_id)

        if not result:
            return {"result": f"NPC {npc_id} not found or could not be moved"}

        logger.info("NPC moved", npc_id=npc_id, admin_name=player_name, room_id=room_id)
        return {"result": f"NPC {npc_id} moved to {room_id}"}

    except Exception as e:  # noqa: B904,BLE001  # pylint: disable=broad-exception-caught  # Reason: NPC movement errors unpredictable (service, validation, instance management), must return user-friendly error messages
        # Catching broad Exception to handle service errors, validation errors, and instance management errors
        # and return user-friendly error messages
        logger.error("Error moving NPC", npc_id=npc_id, admin_name=player_name, error=str(e))
        return {"result": f"Error moving NPC: {str(e)}"}


async def handle_npc_stats_command(
    command_data: dict[str, Any],
    _current_user: dict[str, Any],
    _request: Any,
    _alias_storage: AliasStorage | None,
    player_name: str,
) -> dict[str, str]:
    """Handle NPC stats command."""
    logger.debug("Processing NPC stats command", player_name=player_name)

    args = command_data.get("args", [])
    if len(args) < 2:
        return {"result": "Usage: npc stats <npc_id>"}

    npc_id = args[1]

    try:
        # Get NPC instance service
        instance_service = get_npc_instance_service()

        # Get NPC stats
        stats = await instance_service.get_npc_stats(npc_id)

        if not stats:
            return {"result": f"NPC {npc_id} not found"}

        # Format stats output
        result_lines = [f"NPC {npc_id} stats:"]
        for key, value in stats.items():
            result_lines.append(f"  {key}: {value}")

        logger.info("NPC stats retrieved", npc_id=npc_id, admin_name=player_name)
        return {"result": "\n".join(result_lines)}

    except Exception as e:  # noqa: B904,BLE001  # pylint: disable=broad-exception-caught  # Reason: NPC stats retrieval errors unpredictable (service, instance management), must return user-friendly error messages
        # Catching broad Exception to handle service errors and instance management errors
        # and return user-friendly error messages
        logger.error("Error getting NPC stats", admin_name=player_name, error=str(e))
        return {"result": f"Error getting NPC stats: {str(e)}"}


# --- NPC Monitoring Commands ---


async def handle_npc_population_command(
    _command_data: dict[str, Any],
    _current_user: dict[str, Any],
    _request: Any,
    _alias_storage: AliasStorage | None,
    player_name: str,
) -> dict[str, str]:
    """Handle NPC population stats command."""
    logger.debug("Processing NPC population command", player_name=player_name)

    try:
        # Get NPC instance service
        instance_service = get_npc_instance_service()

        # Get population stats
        stats = await instance_service.get_population_stats()

        # Format population stats output
        result_lines = ["NPC Population Statistics:"]
        result_lines.append(f"  Total NPCs: {stats.get('total_npcs', 0)}")

        if stats.get("by_type"):
            result_lines.append("  By Type:")
            for npc_type, count in stats["by_type"].items():
                result_lines.append(f"    {npc_type}: {count}")

        if stats.get("by_zone"):
            result_lines.append("  By Zone:")
            for zone, count in stats["by_zone"].items():
                result_lines.append(f"    {zone}: {count}")

        logger.info("NPC population stats retrieved", admin_name=player_name)
        return {"result": "\n".join(result_lines)}

    except Exception as e:  # noqa: B904,BLE001  # pylint: disable=broad-exception-caught  # Reason: NPC population stats errors unpredictable (service, instance management), must return user-friendly error messages
        # Catching broad Exception to handle service errors and instance management errors
        # and return user-friendly error messages
        logger.error("Error getting NPC population stats", admin_name=player_name, error=str(e))
        return {"result": f"Error getting NPC population stats: {str(e)}"}


async def handle_npc_zone_command(
    command_data: dict[str, Any],
    _current_user: dict[str, Any],
    _request: Any,
    _alias_storage: AliasStorage | None,
    player_name: str,
) -> dict[str, str]:
    """Handle NPC zone stats command."""
    logger.debug("Processing NPC zone command", player_name=player_name)

    args = command_data.get("args", [])
    zone_key = args[1] if len(args) > 1 else None

    try:
        # Get NPC instance service
        instance_service = get_npc_instance_service()

        # Get zone stats
        stats = await instance_service.get_zone_stats()

        # Format zone stats output
        result_lines = ["NPC Zone Statistics:"]
        result_lines.append(f"  Total Zones: {stats.get('total_zones', 0)}")
        result_lines.append(f"  Total NPCs: {stats.get('total_npcs', 0)}")

        if stats.get("zones"):
            result_lines.append("  Zone Details:")
            for zone in stats["zones"]:
                zone_key_display = zone.get("zone_key", "unknown")
                npc_count = zone.get("npc_count", 0)
                result_lines.append(f"    {zone_key_display}: {npc_count} NPCs")

                if zone_key and zone_key_display == zone_key and zone.get("active_npcs"):
                    result_lines.append(f"      Active NPCs: {', '.join(zone['active_npcs'])}")

        logger.info("NPC zone stats retrieved", admin_name=player_name, zone_key=zone_key)
        return {"result": "\n".join(result_lines)}

    except Exception as e:  # noqa: B904,BLE001  # pylint: disable=broad-exception-caught  # Reason: NPC zone stats errors unpredictable (service, instance management), must return user-friendly error messages
        # Catching broad Exception to handle service errors and instance management errors
        # and return user-friendly error messages
        logger.error("Error getting NPC zone stats", admin_name=player_name, error=str(e))
        return {"result": f"Error getting NPC zone stats: {str(e)}"}


async def handle_npc_status_command(
    _command_data: dict[str, Any],
    _current_user: dict[str, Any],
    _request: Any,
    _alias_storage: AliasStorage | None,
    player_name: str,
) -> dict[str, str]:
    """Handle NPC system status command."""
    logger.debug("Processing NPC status command", player_name=player_name)

    try:
        # Get NPC instance service
        instance_service = get_npc_instance_service()

        # Get system stats
        stats = await instance_service.get_system_stats()

        # Format system status output
        result_lines = ["NPC System Status:"]
        result_lines.append(f"  Status: {stats.get('system_status', 'unknown')}")
        result_lines.append(f"  Active NPCs: {stats.get('active_npcs', 0)}")
        result_lines.append(f"  Lifecycle Manager: {stats.get('lifecycle_manager_status', 'unknown')}")
        result_lines.append(f"  Population Controller: {stats.get('population_controller_status', 'unknown')}")
        result_lines.append(f"  Spawn Queue Size: {stats.get('spawn_queue_size', 0)}")

        logger.info("NPC system status retrieved", admin_name=player_name)
        return {"result": "\n".join(result_lines)}

    except Exception as e:  # noqa: B904,BLE001  # pylint: disable=broad-exception-caught  # Reason: NPC system status errors unpredictable (service, instance management), must return user-friendly error messages
        # Catching broad Exception to handle service errors and instance management errors
        # and return user-friendly error messages
        logger.error("Error getting NPC system status", admin_name=player_name, error=str(e))
        return {"result": f"Error getting NPC system status: {str(e)}"}


# --- NPC Behavior Control Commands ---


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
        return {"result": "Usage: npc behavior <npc_id> <behavior_type>"}

    npc_id = args[1]
    behavior_type = args[2]

    # Validate behavior type
    valid_behaviors = ["passive", "aggressive", "defensive", "wander", "patrol", "guard", "idle"]
    if behavior_type.lower() not in valid_behaviors:
        return {"result": f"Invalid behavior type: {behavior_type}. Valid types: {', '.join(valid_behaviors)}"}

    try:
        # Get NPC instance service
        _instance_service = get_npc_instance_service()

        # TODO: Implement set_npc_behavior method in NPCInstanceService  # pylint: disable=fixme  # Reason: Feature placeholder for NPC behavior system
        # For now, return not implemented message
        return {"result": "NPC behavior modification not yet implemented"}

    except Exception as e:  # noqa: B904,BLE001  # pylint: disable=broad-exception-caught  # Reason: NPC behavior setting errors unpredictable (service, validation), must return user-friendly error messages
        # Catching broad Exception to handle service errors and validation errors
        # and return user-friendly error messages
        logger.error("Error setting NPC behavior", npc_id=npc_id, admin_name=player_name, error=str(e))
        return {"result": f"Error setting NPC behavior: {str(e)}"}


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
        return {"result": "Usage: npc react <npc_id> <reaction_type>"}

    npc_id = args[1]
    reaction_type = args[2]

    # Validate reaction type
    valid_reactions = ["greet", "attack", "flee", "investigate", "alert", "calm", "excited", "suspicious"]
    if reaction_type.lower() not in valid_reactions:
        return {"result": f"Invalid reaction type: {reaction_type}. Valid types: {', '.join(valid_reactions)}"}

    try:
        # Get NPC instance service
        _instance_service = get_npc_instance_service()

        # TODO: Implement trigger_npc_reaction method in NPCInstanceService  # pylint: disable=fixme  # Reason: Feature placeholder for NPC reaction system
        # For now, return not implemented message
        return {"result": "NPC reaction triggering not yet implemented"}

    except Exception as e:  # noqa: B904,BLE001  # pylint: disable=broad-exception-caught  # Reason: NPC reaction triggering errors unpredictable (service, validation), must return user-friendly error messages
        # Catching broad Exception to handle service errors and validation errors
        # and return user-friendly error messages
        logger.error("Error triggering NPC reaction", npc_id=npc_id, admin_name=player_name, error=str(e))
        return {"result": f"Error triggering NPC reaction: {str(e)}"}


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
        return {"result": "Usage: npc stop <npc_id>"}

    npc_id = args[1]

    try:
        # Get NPC instance service
        _instance_service = get_npc_instance_service()

        # TODO: Implement stop_npc_behavior method in NPCInstanceService  # pylint: disable=fixme  # Reason: Feature placeholder for NPC behavior control
        # For now, return not implemented message
        return {"result": "NPC behavior stopping not yet implemented"}

    except Exception as e:  # noqa: B904,BLE001  # pylint: disable=broad-exception-caught  # Reason: NPC behavior stopping errors unpredictable (service, validation), must return user-friendly error messages
        # Catching broad Exception to handle service errors and validation errors
        # and return user-friendly error messages
        logger.error("Error stopping NPC behavior", npc_id=npc_id, admin_name=player_name, error=str(e))
        return {"result": f"Error stopping NPC behavior: {str(e)}"}


async def _get_room_id_for_test_occupants(
    command_data: dict[str, Any], player_obj: Any
) -> tuple[str | None, dict[str, str] | None]:
    """Get room_id from args or current room. Returns (room_id, error_result)."""
    args = command_data.get("args", [])
    room_id = args[1] if len(args) > 1 else None

    if not room_id:
        room_id = getattr(player_obj, "current_room_id", None)
        if not room_id:
            return None, {"result": "No room ID provided and player has no current room."}

    return room_id, None


def _get_event_handler_for_test_occupants(app: Any) -> tuple[Any | None, dict[str, str] | None]:
    """Get event handler from app.state. Returns (event_handler, error_result)."""
    event_handler = getattr(app.state, "event_handler", None)
    if not event_handler:
        event_handler = getattr(app.state.container, "real_time_event_handler", None)

    if not event_handler:
        return None, {"result": "Event handler not available. Cannot test occupants directly."}

    return event_handler, None


def _separate_occupants(occupants_info: list[dict[str, Any]] | None) -> tuple[list[str], list[str]]:
    """Separate occupants into players and NPCs."""
    players: list[str] = []
    npcs: list[str] = []

    for occ in occupants_info or []:
        if isinstance(occ, dict):
            if "player_name" in occ:
                players.append(occ.get("player_name", "Unknown"))
            elif "npc_name" in occ:
                npcs.append(occ.get("npc_name", "Unknown"))

    return players, npcs


def _format_occupants_result(room_id: str, players: list[str], npcs: list[str]) -> str:
    """Format occupants result as a string."""
    result_lines = [f"Occupants in room: {room_id}", ""]
    result_lines.append(f"Players ({len(players)}):")
    if players:
        for player in players:
            result_lines.append(f"  - {player}")
    else:
        result_lines.append("  (none)")

    result_lines.append(f"\nNPCs ({len(npcs)}):")
    if npcs:
        for npc in npcs:
            result_lines.append(f"  - {npc}")
    else:
        result_lines.append("  (none)")

    result_lines.append("\n✅ Occupant update broadcast triggered. Check logs for detailed NPC query information.")
    return "\n".join(result_lines)


async def handle_npc_test_occupants_command(
    command_data: dict[str, Any],
    _current_user: dict[str, Any],
    request: Any,
    _alias_storage: AliasStorage | None,
    player_name: str,
) -> dict[str, str]:
    """
    Handle NPC test occupants command - manually trigger occupant query for debugging.

    Usage: npc test-occupants [room_id]
    If room_id is not provided, uses the current room.
    """
    logger.info("Processing NPC test occupants command", admin_name=player_name)

    try:
        app = request.app if request else None
        if not app:
            return {"result": "Server application not available."}

        player_service = app.state.player_service if app else None
        if not player_service:
            return {"result": "Player service not available."}

        _maybe_coro = player_service.resolve_player_name(player_name)
        player_obj = await _maybe_coro if inspect.isawaitable(_maybe_coro) else _maybe_coro
        if not player_obj:
            return {"result": "Player not found."}

        room_id, error_result = await _get_room_id_for_test_occupants(command_data, player_obj)
        if error_result:
            return error_result

        event_handler, error_result = _get_event_handler_for_test_occupants(app)
        if error_result or event_handler is None:
            return error_result or {"result": "Event handler not available."}

        if room_id is None:
            return {"result": "Room ID is required for testing occupants."}

        logger.info("Manually triggering occupant query for testing", admin_name=player_name, room_id=room_id)

        occupants_info = event_handler._get_room_occupants(room_id)  # noqa: SLF001  # pylint: disable=protected-access  # Reason: Accessing internal method for testing/debugging purposes, event_handler is internal implementation detail
        players, npcs = _separate_occupants(occupants_info)

        await event_handler.send_room_occupants_update(room_id)

        result_text = _format_occupants_result(room_id, players, npcs)

        logger.info(
            "NPC test occupants command completed",
            admin_name=player_name,
            room_id=room_id,
            player_count=len(players),
            npc_count=len(npcs),
        )

        return {"result": result_text}

    except Exception as e:  # noqa: B904,BLE001  # pylint: disable=broad-exception-caught  # Reason: NPC occupant testing errors unpredictable (service, player resolution, event handler), must return user-friendly error messages
        # Catching broad Exception to handle service errors, player resolution errors, and event handler errors
        # and return user-friendly error messages
        logger.error("Error testing NPC occupants", admin_name=player_name, error=str(e), exc_info=True)
        return {"result": f"Error testing NPC occupants: {str(e)}"}
