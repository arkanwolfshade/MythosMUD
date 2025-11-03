"""
NPC Admin Commands for MythosMUD.

This module provides administrative slash commands for managing NPCs,
including CRUD operations for NPC definitions, instance management,
population monitoring, and relationship management.

As documented in the Cultes des Goules, proper administrative protocols
are essential for maintaining control over the eldritch entities that
lurk in the shadows of our world.
"""

import inspect
from typing import Any

from ..alias_storage import AliasStorage
from ..logging.enhanced_logging_config import get_logger
from ..models.npc import NPCDefinitionType
from ..services.npc_instance_service import get_npc_instance_service
from ..services.npc_service import npc_service

logger = get_logger(__name__)


# --- Permission Validation ---


def validate_npc_admin_permission(player, player_name: str) -> bool:
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
        if not hasattr(player, "is_admin") or not getattr(player, "is_admin", False):
            logger.warning("NPC admin permission check failed - player is not an admin", player_name=player_name)
            return False

        logger.debug("NPC admin permission check passed", player_name=player_name)
        return True

    except Exception as e:
        logger.error("Error checking NPC admin permission", player_name=player_name, error=str(e))
        return False


# --- Main NPC Command Handler ---


async def handle_npc_command(
    command_data: dict, current_user: dict, request: Any, alias_storage: AliasStorage | None, player_name: str
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

    # Extract subcommand
    args = command_data.get("args", [])
    if not args:
        return _get_npc_help()

    subcommand = args[0].lower()

    # Route to appropriate subcommand handler
    if subcommand == "help":
        return _get_npc_help()
    elif subcommand == "create":
        return await handle_npc_create_command(command_data, current_user, request, alias_storage, player_name)
    elif subcommand == "edit":
        return await handle_npc_edit_command(command_data, current_user, request, alias_storage, player_name)
    elif subcommand == "delete":
        return await handle_npc_delete_command(command_data, current_user, request, alias_storage, player_name)
    elif subcommand == "list":
        return await handle_npc_list_command(command_data, current_user, request, alias_storage, player_name)
    elif subcommand == "spawn":
        return await handle_npc_spawn_command(command_data, current_user, request, alias_storage, player_name)
    elif subcommand == "despawn":
        return await handle_npc_despawn_command(command_data, current_user, request, alias_storage, player_name)
    elif subcommand == "move":
        return await handle_npc_move_command(command_data, current_user, request, alias_storage, player_name)
    elif subcommand == "stats":
        return await handle_npc_stats_command(command_data, current_user, request, alias_storage, player_name)
    elif subcommand == "population":
        return await handle_npc_population_command(command_data, current_user, request, alias_storage, player_name)
    elif subcommand == "zone":
        return await handle_npc_zone_command(command_data, current_user, request, alias_storage, player_name)
    elif subcommand == "status":
        return await handle_npc_status_command(command_data, current_user, request, alias_storage, player_name)
    elif subcommand == "behavior":
        return await handle_npc_behavior_command(command_data, current_user, request, alias_storage, player_name)
    elif subcommand == "react":
        return await handle_npc_react_command(command_data, current_user, request, alias_storage, player_name)
    elif subcommand == "stop":
        return await handle_npc_stop_command(command_data, current_user, request, alias_storage, player_name)
    else:
        return {"result": f"Unknown NPC command: {subcommand}. Use 'npc help' for available commands."}


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

Help:
  help                                          - Show this help message

NPC Types: shopkeeper, passive_mob, aggressive_mob, quest_giver, merchant
"""
    return {"result": help_text.strip()}


# --- NPC Definition Management Commands ---


async def handle_npc_create_command(
    command_data: dict, current_user: dict, request: Any, alias_storage: AliasStorage | None, player_name: str
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

    except Exception as e:
        logger.error("Error creating NPC", admin_name=player_name, error=str(e))
        return {"result": f"Error creating NPC: {str(e)}"}


async def handle_npc_edit_command(
    command_data: dict, current_user: dict, request: Any, alias_storage: AliasStorage | None, player_name: str
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

    except Exception as e:
        logger.error("Error editing NPC", npc_id=npc_id, admin_name=player_name, error=str(e))
        return {"result": f"Error editing NPC: {str(e)}"}


async def handle_npc_delete_command(
    command_data: dict, current_user: dict, request: Any, alias_storage: AliasStorage | None, player_name: str
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

    except Exception as e:
        logger.error("Error deleting NPC", npc_id=npc_id, admin_name=player_name, error=str(e))
        return {"result": f"Error deleting NPC: {str(e)}"}


async def handle_npc_list_command(
    command_data: dict, current_user: dict, request: Any, alias_storage: AliasStorage | None, player_name: str
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

    except Exception as e:
        logger.error("Error listing NPCs", admin_name=player_name, error=str(e))
        return {"result": f"Error listing NPCs: {str(e)}"}


# --- NPC Instance Management Commands ---


async def handle_npc_spawn_command(
    command_data: dict, current_user: dict, request: Any, alias_storage: AliasStorage | None, player_name: str
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

    except Exception as e:
        logger.error("Error spawning NPC", admin_name=player_name, error=str(e))
        return {"result": f"Error spawning NPC: {str(e)}"}


async def handle_npc_despawn_command(
    command_data: dict, current_user: dict, request: Any, alias_storage: AliasStorage | None, player_name: str
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

    except Exception as e:
        logger.error("Error despawning NPC", npc_id=npc_id, admin_name=player_name, error=str(e))
        return {"result": f"Error despawning NPC: {str(e)}"}


async def handle_npc_move_command(
    command_data: dict, current_user: dict, request: Any, alias_storage: AliasStorage | None, player_name: str
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

    except Exception as e:
        logger.error("Error moving NPC", npc_id=npc_id, admin_name=player_name, error=str(e))
        return {"result": f"Error moving NPC: {str(e)}"}


async def handle_npc_stats_command(
    command_data: dict, current_user: dict, request: Any, alias_storage: AliasStorage | None, player_name: str
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

    except Exception as e:
        logger.error("Error getting NPC stats", admin_name=player_name, error=str(e))
        return {"result": f"Error getting NPC stats: {str(e)}"}


# --- NPC Monitoring Commands ---


async def handle_npc_population_command(
    command_data: dict, current_user: dict, request: Any, alias_storage: AliasStorage | None, player_name: str
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

    except Exception as e:
        logger.error("Error getting NPC population stats", admin_name=player_name, error=str(e))
        return {"result": f"Error getting NPC population stats: {str(e)}"}


async def handle_npc_zone_command(
    command_data: dict, current_user: dict, request: Any, alias_storage: AliasStorage | None, player_name: str
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

    except Exception as e:
        logger.error("Error getting NPC zone stats", admin_name=player_name, error=str(e))
        return {"result": f"Error getting NPC zone stats: {str(e)}"}


async def handle_npc_status_command(
    command_data: dict, current_user: dict, request: Any, alias_storage: AliasStorage | None, player_name: str
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

    except Exception as e:
        logger.error("Error getting NPC system status", admin_name=player_name, error=str(e))
        return {"result": f"Error getting NPC system status: {str(e)}"}


# --- NPC Behavior Control Commands ---


async def handle_npc_behavior_command(
    command_data: dict, current_user: dict, request: Any, alias_storage: AliasStorage | None, player_name: str
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

        # TODO: Implement set_npc_behavior method in NPCInstanceService
        # For now, return not implemented message
        return {"result": "NPC behavior modification not yet implemented"}

    except Exception as e:
        logger.error("Error setting NPC behavior", npc_id=npc_id, admin_name=player_name, error=str(e))
        return {"result": f"Error setting NPC behavior: {str(e)}"}


async def handle_npc_react_command(
    command_data: dict, current_user: dict, request: Any, alias_storage: AliasStorage | None, player_name: str
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

        # TODO: Implement trigger_npc_reaction method in NPCInstanceService
        # For now, return not implemented message
        return {"result": "NPC reaction triggering not yet implemented"}

    except Exception as e:
        logger.error("Error triggering NPC reaction", npc_id=npc_id, admin_name=player_name, error=str(e))
        return {"result": f"Error triggering NPC reaction: {str(e)}"}


async def handle_npc_stop_command(
    command_data: dict, current_user: dict, request: Any, alias_storage: AliasStorage | None, player_name: str
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

        # TODO: Implement stop_npc_behavior method in NPCInstanceService
        # For now, return not implemented message
        return {"result": "NPC behavior stopping not yet implemented"}

    except Exception as e:
        logger.error("Error stopping NPC behavior", npc_id=npc_id, admin_name=player_name, error=str(e))
        return {"result": f"Error stopping NPC behavior: {str(e)}"}
