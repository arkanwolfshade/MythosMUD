"""
Exploration commands for MythosMUD.

This module contains handlers for exploration-related commands like look and go.
"""

from typing import Any

from ..alias_storage import AliasStorage
from ..logging.enhanced_logging_config import get_logger
from ..utils.command_parser import get_username_from_user

logger = get_logger(__name__)


async def handle_look_command(
    command_data: dict, current_user: dict, request: Any, alias_storage: AliasStorage | None, player_name: str
) -> dict[str, str]:
    """
    Handle the look command for examining surroundings.

    Args:
        command_data: Command data dictionary containing validated command information
        current_user: Current user information
        request: FastAPI request object
        alias_storage: Alias storage instance
        player_name: Player name for logging

    Returns:
        dict: Look command result
    """
    logger.debug("Processing look command", player=player_name, args=command_data)

    app = request.app if request else None
    persistence = app.state.persistence if app else None

    if not persistence:
        logger.warning("Look command failed - no persistence layer", player=player_name)
        return {"result": "You see nothing special."}

    player = persistence.get_player_by_name(get_username_from_user(current_user))
    if not player:
        logger.warning("Look command failed - player not found", player=player_name)
        return {"result": "You see nothing special."}

    room_id = player.current_room_id
    room = persistence.get_room(room_id)
    if not room:
        logger.warning("Look command failed - room not found", player=player_name, room_id=room_id)
        return {"result": "You see nothing special."}

    # Extract direction and target from command_data
    direction = command_data.get("direction")
    target = command_data.get("target")

    # Handle target lookups (NPCs take priority over directions)
    if target:
        target_lower = target.lower()
        logger.debug("Looking at target", player=player_name, target=target, room_id=room_id)

        # Check if target is a direction
        if target_lower in ["north", "south", "east", "west", "up", "down", "n", "s", "e", "w", "u", "d"]:
            direction = target_lower
        else:
            # Look for NPC in current room
            npc_ids = room.get_npcs()
            if npc_ids:
                # Find matching NPCs (case-insensitive partial match)
                matching_npcs = []
                for npc_id in npc_ids:
                    # Get NPC instance to check name
                    from ..services.npc_instance_service import get_npc_instance_service

                    npc_instance_service = get_npc_instance_service()
                    # Use the same approach as combat system
                    if hasattr(npc_instance_service, "lifecycle_manager"):
                        lifecycle_manager = npc_instance_service.lifecycle_manager
                        if lifecycle_manager and npc_id in lifecycle_manager.active_npcs:
                            npc_instance = lifecycle_manager.active_npcs[npc_id]
                            if npc_instance and target_lower in npc_instance.name.lower():
                                matching_npcs.append(npc_instance)

                if len(matching_npcs) == 1:
                    npc = matching_npcs[0]
                    logger.debug("Found NPC to look at", player=player_name, npc_name=npc.name, npc_id=npc.npc_id)
                    description = getattr(npc.definition, "description", "Nothing remarkable about them.")
                    return {"result": f"You look at {npc.name}.\n{description}"}
                elif len(matching_npcs) > 1:
                    npc_names = [npc.name for npc in matching_npcs]
                    logger.debug("Multiple NPCs match target", player=player_name, target=target, matches=npc_names)
                    return {"result": f"You see multiple NPCs matching '{target}': {', '.join(npc_names)}"}
                else:
                    logger.debug("No NPCs match target", player=player_name, target=target, room_id=room_id)
                    return {"result": f"You don't see anyone named '{target}' here."}
            else:
                logger.debug("No NPCs in room", player=player_name, target=target, room_id=room_id)
                return {"result": f"You don't see anyone named '{target}' here."}

    # Handle direction lookups
    if direction:
        direction = direction.lower()
        logger.debug("Looking in direction", player=player_name, direction=direction, room_id=room_id)
        exits = room.exits
        target_room_id = exits.get(direction)
        if target_room_id:
            target_room = persistence.get_room(target_room_id)
            if target_room:
                name = target_room.name
                desc = target_room.description
                logger.debug(
                    "Looked at room in direction",
                    player=player_name,
                    direction=direction,
                    target_room_id=target_room_id,
                )
                return {"result": f"{name}\n{desc}"}
        logger.debug("No valid exit in direction", player=player_name, direction=direction, room_id=room_id)
        return {"result": "You see nothing special that way."}

    # Look at current room
    name = room.name
    desc = room.description
    exits = room.exits
    # Only include exits that have valid room IDs (not null)
    valid_exits = [direction for direction, room_id in exits.items() if room_id is not None]
    exit_list = ", ".join(valid_exits) if valid_exits else "none"
    logger.debug("Looked at current room", player=player_name, room_id=room_id, exits=valid_exits)
    return {"result": f"{name}\n{desc}\n\nExits: {exit_list}"}


async def handle_go_command(
    command_data: dict, current_user: dict, request: Any, alias_storage: AliasStorage | None, player_name: str
) -> dict[str, str]:
    """
    Handle the go command for movement.

    Args:
        command_data: Command data dictionary containing validated command information
        current_user: Current user information
        request: FastAPI request object
        alias_storage: Alias storage instance
        player_name: Player name for logging

    Returns:
        dict: Go command result
    """
    logger.debug("Processing go command", player=player_name, args=command_data)

    app = request.app if request else None
    persistence = app.state.persistence if app else None

    if not persistence:
        logger.warning("Go command failed - no persistence layer", player=player_name)
        return {"result": "You can't go that way"}

    # Extract direction from command_data
    direction = command_data.get("direction")
    if not direction:
        logger.warning("Go command failed - no direction specified", player=player_name, command_data=command_data)
        return {"result": "Go where? Usage: go <direction>"}

    direction = direction.lower()
    logger.debug("Player attempting to move", player=player_name, direction=direction)

    player = persistence.get_player_by_name(get_username_from_user(current_user))
    if not player:
        logger.warning("Go command failed - player not found", player=player_name)
        return {"result": "You can't go that way"}

    room_id = player.current_room_id
    room = persistence.get_room(room_id)
    if not room:
        logger.warning("Go command failed - current room not found", player=player_name, room_id=room_id)
        return {"result": "You can't go that way"}

    # Enforce posture requirements before attempting movement
    position = "standing"
    if hasattr(player, "get_stats"):
        try:
            stats = player.get_stats() or {}
            position = str(stats.get("position", "standing") or "standing").lower()
        except Exception as exc:  # pragma: no cover - defensive logging path
            logger.warning(
                "Failed to read player stats during go command",
                player=player_name,
                error=str(exc),
                room_id=room_id,
            )
            position = "standing"

    if position != "standing":
        logger.info(
            "Movement blocked - player not standing",
            player=player_name,
            position=position,
            direction=direction,
            room_id=room_id,
        )
        return {"result": "You need to stand up before moving."}

    exits = room.exits
    target_room_id = exits.get(direction)
    if not target_room_id:
        logger.debug("No exit in direction", player=player_name, direction=direction, room_id=room_id)
        return {"result": "You can't go that way"}

    target_room = persistence.get_room(target_room_id)
    if not target_room:
        logger.warning("Go command failed - target room not found", player=player_name, target_room_id=target_room_id)
        return {"result": "You can't go that way"}

    # Use movement service for the actual movement
    from ..game.movement_service import MovementService

    try:
        # Get player combat service from app state
        player_combat_service = getattr(app.state, "player_combat_service", None) if app else None

        # Pass the same event bus that persistence uses to ensure events are published correctly
        # Also pass player_combat_service to enforce combat state validation
        movement_service = MovementService(persistence._event_bus, player_combat_service=player_combat_service)
        success = movement_service.move_player(str(player.player_id), room_id, target_room_id)

        if success:
            logger.info("Player moved successfully", player=player_name, from_room=room_id, to_room=target_room_id)
            return {"result": "You move to the new location."}
        else:
            logger.warning("Movement service failed", player=player_name, from_room=room_id, to_room=target_room_id)
            return {"result": "You can't go that way."}

    except Exception as e:
        logger.error(
            "Go command error",
            player=player_name,
            command_data=command_data,
            room_id=room_id,
            target_room_id=target_room_id,
            error_type=type(e).__name__,
            error_message=str(e),
            exc_info=True,
        )
        return {"result": f"Error during movement: {str(e)}"}
