"""
Exploration commands for MythosMUD.

This module contains handlers for exploration-related commands like look and go.
"""

from typing import Any

from ..alias_storage import AliasStorage
from ..logging_config import get_logger
from ..utils.command_parser import get_username_from_user

logger = get_logger(__name__)


async def handle_look_command(
    command_data: dict, current_user: dict, request: Any, alias_storage: AliasStorage, player_name: str
) -> dict[str, str]:
    """
    Handle the look command for examining surroundings, directions, or NPCs.

    This command supports three main modes:
    1. General room look: 'look' - shows current room details
    2. Direction look: 'look north' - shows what's in a specific direction
    3. NPC look: 'look guard' - shows details about a specific NPC

    NPCs take priority over directions when both could match the target.
    Supports case-insensitive partial matching for NPC names.

    Args:
        command_data: Command data dictionary containing 'target' and/or 'direction' fields
        current_user: Current user information
        request: FastAPI request object
        alias_storage: Alias storage instance
        player_name: Player name for logging

    Returns:
        dict: Look command result with 'result' key containing the response text
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

    # Extract target from command_data (could be NPC or direction)
    target = command_data.get("target") or command_data.get("direction")

    # Check for NPC targets first (priority over directions)
    if target:
        # Get NPCs in current room
        npc_ids = room.get_npcs()
        if npc_ids:
            matching_npcs = []
            # Get NPC service for retrieving NPC instances
            from ..services.npc_instance_service import get_npc_instance_service

            npc_service = get_npc_instance_service()

            # Search for NPCs matching the target (case-insensitive partial matching)
            for npc_id in npc_ids:
                npc = npc_service.get_npc_by_id(npc_id)
                if npc and target.lower() in npc.name.lower():
                    matching_npcs.append(npc)

            if len(matching_npcs) == 1:
                # Single match - show detailed NPC information
                npc = matching_npcs[0]
                logger.debug("Looking at NPC", player=player_name, npc_name=npc.name, npc_id=npc_id)
                return {"result": f"{npc.name}\n{npc.description}"}
            elif len(matching_npcs) > 1:
                # Multiple matches - show list of names
                npc_names = [npc.name for npc in matching_npcs]
                name_list = "\n".join(f"- {name}" for name in npc_names)
                logger.debug("Multiple NPC matches", player=player_name, matches=npc_names)
                return {"result": f"You see several people here:\n{name_list}"}

        # No NPC matches found, check if it's a direction
        direction = target.lower()
        if direction in [
            "north",
            "south",
            "east",
            "west",
            "up",
            "down",
            "northeast",
            "northwest",
            "southeast",
            "southwest",
        ]:
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

        # No NPCs or directions match
        logger.debug("No matches found for target", player=player_name, target=target)
        return {"result": "You don't see anyone like that here."}

    # Look at current room (original logic for 'look' with no target)
    name = room.name
    desc = room.description
    exits = room.exits
    # Only include exits that have valid room IDs (not null)
    valid_exits = [direction for direction, room_id in exits.items() if room_id is not None]
    exit_list = ", ".join(valid_exits) if valid_exits else "none"
    logger.debug("Looked at current room", player=player_name, room_id=room_id, exits=valid_exits)
    return {"result": f"{name}\n{desc}\n\nExits: {exit_list}"}


async def handle_go_command(
    command_data: dict, current_user: dict, request: Any, alias_storage: AliasStorage, player_name: str
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
        # Pass the same event bus that persistence uses to ensure events are published correctly
        movement_service = MovementService(persistence._event_bus)
        success = movement_service.move_player(str(player.player_id), room_id, target_room_id)

        if success:
            logger.info(f"Player moved successfully for {player_name}: from {room_id} to {target_room_id}")
            return {"result": "You move to the new location."}
        else:
            logger.warning(f"Movement service failed for {player_name}: from {room_id} to {target_room_id}")
            return {"result": "You can't go that way."}

    except Exception as e:
        logger.error(f"Go command error for {player_name}: {str(e)}")
        return {"result": f"Error during movement: {str(e)}"}
