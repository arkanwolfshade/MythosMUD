"""
Command Handler v2 - Integrated Pydantic + Click validation system.

This module provides a new command handling system that integrates our robust
Pydantic + Click validation with the existing MythosMUD infrastructure.

As the Necronomicon states: "The old ways must give way to the new, but the
foundations must remain strong lest the entire edifice crumble."
"""

import re
from typing import Any

from fastapi import APIRouter, Depends, HTTPException, Request, status
from pydantic import BaseModel

from .alias_storage import AliasStorage
from .auth.users import get_current_user
from .config_loader import get_config
from .game.chat_service import ChatService
from .game.movement_service import MovementService
from .logging_config import get_logger
from .utils.command_processor import get_command_processor

logger = get_logger(__name__)

router = APIRouter(prefix="/command", tags=["command"])

# Get the command processor instance
command_processor = get_command_processor()


def get_username_from_user(user_obj):
    """Safely extract username from user object or dictionary."""
    if hasattr(user_obj, "username"):
        return user_obj.username
    elif hasattr(user_obj, "name"):
        return user_obj.name
    elif isinstance(user_obj, dict) and "username" in user_obj:
        return user_obj["username"]
    elif isinstance(user_obj, dict) and "name" in user_obj:
        return user_obj["name"]
    else:
        raise ValueError("User object must have username or name attribute or key")


class CommandRequest(BaseModel):
    command: str


# Commands that traditionally use slash prefix in modern interfaces
SLASH_COMMANDS = {"help", "who", "quit", "look", "go", "say", "me", "pose", "alias", "aliases", "unalias"}


def normalize_command(command: str) -> str:
    """
    Normalize command input by removing optional slash prefix.

    Supports both traditional MUD commands (go north) and modern slash commands (/go north).
    This allows for flexible command input while maintaining backward compatibility.

    Args:
        command: The raw command string from user input

    Returns:
        Normalized command string with slash prefix removed if present
    """
    if not command:
        return command

    # Strip whitespace first
    command = command.strip()

    # Remove leading slash if present
    if command.startswith("/"):
        normalized = command[1:].strip()
        logger.debug("Slash prefix removed from command", original=command, normalized=normalized)
        return normalized

    return command


def clean_command_input(command: str) -> str:
    """Clean and normalize command input by collapsing multiple spaces and stripping whitespace."""
    cleaned = re.sub(r"\s+", " ", command).strip()
    if cleaned != command:
        logger.debug("Command input cleaned", original=command, cleaned=cleaned)
    return cleaned


def _is_predefined_emote(command: str) -> bool:
    """
    Check if a command is a predefined emote alias.

    Args:
        command: The command to check

    Returns:
        True if the command is a predefined emote, False otherwise
    """
    try:
        from .game.emote_service import EmoteService

        emote_service = EmoteService()
        return emote_service.is_emote_alias(command)
    except Exception as e:
        logger.warning(f"Error checking predefined emote: {e}")
        return False


MAX_COMMAND_LENGTH = get_config().get("max_command_length", 1000)


@router.post("", status_code=status.HTTP_200_OK)
async def handle_command(
    req: CommandRequest,
    current_user: dict = Depends(get_current_user),
    request: Request = None,
):
    """Handle incoming command requests with integrated Pydantic + Click validation."""
    command_line = req.command

    # Check if user is authenticated
    if not current_user:
        raise HTTPException(status_code=401, detail="Authentication required")

    player_name = get_username_from_user(current_user)

    logger.info(f"Command received for {player_name}: {command_line} (length: {len(command_line)})")

    # Basic length validation
    if len(command_line) > MAX_COMMAND_LENGTH:
        logger.warning(
            f"Command too long rejected for {player_name}: {command_line} (length: {len(command_line)}, max: {MAX_COMMAND_LENGTH})"
        )
        raise HTTPException(
            status_code=400,
            detail=f"Command too long (max {MAX_COMMAND_LENGTH} characters)",
        )

    # Clean and normalize the command
    command_line = clean_command_input(command_line)
    if not command_line:
        logger.debug(f"Empty command after cleaning for {player_name}")
        return {"result": ""}

    # Normalize command by removing optional slash prefix
    command_line = normalize_command(command_line)
    if not command_line:
        logger.debug(f"Empty command after normalization for {player_name}")
        return {"result": ""}

    # Initialize alias storage
    try:
        alias_storage = AliasStorage()
        logger.debug(f"AliasStorage initialized successfully for {player_name}")
    except Exception as e:
        logger.error(f"Failed to initialize AliasStorage for {player_name}: {str(e)}")
        # Continue without alias storage
        alias_storage = None

    # Check for alias expansion before command processing
    parts = command_line.split()
    cmd = parts[0].lower()
    args = parts[1:]

    logger.debug(f"Command parsed for {player_name}: command={cmd}, args={args}, original={command_line}")

    # Handle alias management commands first (don't expand these)
    if cmd in ["alias", "aliases", "unalias"]:
        logger.debug(f"Processing alias management command for {player_name}: {cmd}")
        return await process_command(cmd, args, current_user, request, alias_storage, player_name)

    # Check if this is an alias
    if alias_storage:
        alias = alias_storage.get_alias(player_name, cmd)
        if alias:
            logger.debug(f"Alias found, expanding for {player_name}: {alias.name}, original_command: {cmd}")
            # Expand the alias
            expanded_command = alias.get_expanded_command(args)
            # Recursively process the expanded command (with depth limit to prevent loops)
            result = await handle_expanded_command(
                expanded_command, current_user, request, alias_storage, player_name, depth=0, alias_chain=[]
            )
            # Add alias chain information to the result
            if "alias_chain" not in result:
                result["alias_chain"] = [{"original": cmd, "expanded": expanded_command, "alias_name": alias.name}]
            return result

    # Process command with new validation system
    logger.debug(f"Processing command with new validation system for {player_name}: {cmd}")
    return await process_command_with_validation(command_line, current_user, request, alias_storage, player_name)


async def process_command_with_validation(
    command_line: str, current_user: dict, request: Request, alias_storage: AliasStorage, player_name: str
) -> dict:
    """Process a command using the new Pydantic + Click validation system."""
    logger.debug(f"=== COMMAND HANDLER V2 DEBUG: Processing command for {player_name} ===", command=command_line)

    try:
        # Use our new command processor for validation
        validated_command, error_message, command_type = command_processor.process_command_string(
            command_line, player_name
        )

        if error_message:
            logger.warning(f"Command validation failed for {player_name}: {error_message}")
            return {"result": error_message}

        if not validated_command:
            logger.warning(f"No validated command returned for {player_name}")
            return {"result": "Invalid command format"}

        # Extract command data for processing
        command_data = command_processor.extract_command_data(validated_command)
        command_data["player_name"] = player_name

        logger.debug(f"Command validated successfully for {player_name}: type={command_type}, data={command_data}")

        # Route to appropriate handler based on command type
        app = request.app if request else None
        persistence = app.state.persistence if app else None

        if command_type == "help":
            return await handle_help_command(validated_command, command_data, player_name)
        elif command_type == "look":
            return await handle_look_command(validated_command, command_data, current_user, persistence, player_name)
        elif command_type == "go":
            return await handle_go_command(
                validated_command, command_data, current_user, request, persistence, player_name
            )
        elif command_type == "say":
            return await handle_say_command(validated_command, command_data, current_user, persistence, player_name)
        elif command_type in ["emote", "me"]:
            return await handle_emote_command(validated_command, command_data, current_user, persistence, player_name)
        elif command_type == "pose":
            return await handle_pose_command(validated_command, command_data, current_user, persistence, player_name)
        elif command_type == "alias":
            return await handle_alias_command(validated_command, command_data, alias_storage, player_name)
        elif command_type == "aliases":
            return await handle_aliases_command(validated_command, command_data, alias_storage, player_name)
        elif command_type == "unalias":
            return await handle_unalias_command(validated_command, command_data, alias_storage, player_name)
        elif command_type in ["mute", "unmute", "mute_global", "unmute_global", "add_admin", "mutes"]:
            return await handle_admin_command(validated_command, command_data, current_user, persistence, player_name)
        else:
            logger.warning(f"Unknown command type for {player_name}: {command_type}")
            return {"result": f"Unknown command: {command_type}"}

    except Exception as e:
        logger.error(f"Error processing command for {player_name}: {str(e)}", exc_info=True)
        return {"result": "An error occurred while processing your command."}


async def handle_help_command(validated_command: Any, command_data: dict[str, Any], player_name: str) -> dict:
    """Handle help command with new validation system."""
    logger.debug(f"Processing help command for {player_name}")

    # Get help content using our new system
    help_content = command_processor.get_command_help()
    return {"result": help_content}


async def handle_look_command(
    validated_command: Any, command_data: dict[str, Any], current_user: dict, persistence: Any, player_name: str
) -> dict:
    """Handle look command with new validation system."""
    logger.debug(f"Processing look command for {player_name}, direction: {command_data.get('direction')}")

    if not persistence:
        logger.warning(f"Look command failed - no persistence layer for {player_name}")
        return {"result": "You see nothing special."}

    player = persistence.get_player_by_name(get_username_from_user(current_user))
    if not player:
        logger.warning(f"Look command failed - player not found for {player_name}")
        return {"result": "You see nothing special."}

    room_id = player.current_room_id
    room = persistence.get_room(room_id)
    if not room:
        logger.warning(f"Look command failed - room not found for {player_name}, room_id: {room_id}")
        return {"result": "You see nothing special."}

    # Handle looking in a specific direction
    if command_data.get("direction"):
        direction = command_data["direction"]
        logger.debug(f"Looking in direction for {player_name}: {direction}, room_id: {room_id}")
        exits = room.exits
        target_room_id = exits.get(direction)
        if target_room_id:
            target_room = persistence.get_room(target_room_id)
            if target_room:
                name = target_room.name
                desc = target_room.description
                logger.debug(
                    f"Looked at room in direction for {player_name}: {direction}, target_room_id: {target_room_id}"
                )
                return {"result": f"{name}\n{desc}"}
        logger.debug(f"No valid exit in direction for {player_name}: {direction}, room_id: {room_id}")
        return {"result": "You see nothing special that way."}

    # Look at current room
    name = room.name
    desc = room.description
    exits = room.exits
    # Only include exits that have valid room IDs (not null)
    valid_exits = [direction for direction, room_id in exits.items() if room_id is not None]
    exit_list = ", ".join(valid_exits) if valid_exits else "none"
    logger.debug(f"Looked at current room for {player_name}, room_id: {room_id}, exits: {valid_exits}")
    return {"result": f"{name}\n{desc}\n\nExits: {exit_list}"}


async def handle_go_command(
    validated_command: Any,
    command_data: dict[str, Any],
    current_user: dict,
    request: Request,
    persistence: Any,
    player_name: str,
) -> dict:
    """Handle go command with new validation system."""
    logger.debug(f"Processing go command for {player_name}, direction: {command_data.get('direction')}")

    if not persistence:
        logger.warning(f"Go command failed - no persistence layer for {player_name}")
        return {"result": "You can't go that way"}

    if not command_data.get("direction"):
        logger.warning(f"Go command failed - no direction specified for {player_name}")
        return {"result": "Go where? Usage: go <direction>"}

    direction = command_data["direction"]
    logger.debug(f"Player attempting to move for {player_name}: {direction}")

    player = persistence.get_player_by_name(get_username_from_user(current_user))
    if not player:
        logger.warning(f"Go command failed - player not found for {player_name}")
        return {"result": "You can't go that way"}

    room_id = player.current_room_id
    room = persistence.get_room(room_id)
    if not room:
        logger.warning(f"Go command failed - current room not found for {player_name}, room_id: {room_id}")
        return {"result": "You can't go that way"}

    exits = room.exits
    target_room_id = exits.get(direction)
    if not target_room_id:
        logger.debug(f"No exit in direction for {player_name}: {direction}, room_id: {room_id}")
        return {"result": "You can't go that way"}

    target_room = persistence.get_room(target_room_id)
    if not target_room:
        logger.warning(f"Go command failed - target room not found for {player_name}, target_room_id: {target_room_id}")
        return {"result": "You can't go that way"}

    # Use MovementService for atomic movement
    app = request.app if request else None
    event_bus = getattr(app.state, "event_bus", None) if app else None
    movement_service = MovementService(event_bus)
    success = movement_service.move_player(player.player_id, room_id, target_room_id)
    if not success:
        logger.warning(f"Movement failed for {player_name}: from {room_id} to {target_room_id}")
        return {"result": "You can't go that way"}

    # Return room description
    name = target_room.name
    desc = target_room.description
    exits = target_room.exits
    # Only include exits that have valid room IDs (not null)
    valid_exits = [direction for direction, room_id in exits.items() if room_id is not None]
    exit_list = ", ".join(valid_exits) if valid_exits else "none"
    return {"result": f"{name}\n{desc}\n\nExits: {exit_list}"}


async def handle_say_command(
    validated_command: Any, command_data: dict[str, Any], current_user: dict, persistence: Any, player_name: str
) -> dict:
    """Handle say command with new validation system."""
    logger.debug(f"Processing say command for {player_name}, message: {command_data.get('message')}")

    if not persistence:
        logger.warning(f"Say command failed - no persistence layer for {player_name}")
        return {"result": "You cannot speak right now."}

    if not command_data.get("message"):
        logger.warning(f"Say command failed - no message provided for {player_name}")
        return {"result": "Say what? Usage: say <message>"}

    message = command_data["message"]
    if not message:
        return {"result": "You open your mouth, but no words come out."}

    # Get player information
    player = persistence.get_player_by_name(get_username_from_user(current_user))
    if not player:
        logger.warning(f"Say command failed - player not found for {player_name}")
        return {"result": "You cannot speak right now."}

    # Initialize chat service
    from .game.player_service import PlayerService
    from .game.room_service import RoomService

    room_service = RoomService(persistence)
    player_service = PlayerService(persistence)
    chat_service = ChatService(persistence, room_service, player_service)

    # Send the message
    logger.debug(
        f"About to call chat_service.send_say_message for player_id: {str(player.player_id)}, message: {message}"
    )
    result = await chat_service.send_say_message(str(player.player_id), message)
    logger.debug(f"chat_service.send_say_message completed, result: {result}")

    if result["success"]:
        # Format the message for display
        formatted_message = f"{player.name} says: {message}"
        logger.info(f"Say message sent successfully for {player_name}, message_length: {len(message)}")
        return {"result": formatted_message}
    else:
        logger.warning(f"Say message failed for {player_name}, error: {result.get('error')}")
        return {"result": result.get("error", "You cannot speak right now.")}


async def handle_emote_command(
    validated_command: Any, command_data: dict[str, Any], current_user: dict, persistence: Any, player_name: str
) -> dict:
    """Handle emote command with new validation system."""
    logger.debug(f"Processing emote command for {player_name}, action: {command_data.get('action')}")

    if not persistence:
        logger.warning(f"Emote command failed - no persistence layer for {player_name}")
        return {"result": "You cannot emote right now."}

    if not command_data.get("action"):
        logger.warning(f"Emote command failed - no action provided for {player_name}")
        return {"result": "Emote what? Usage: emote <action>"}

    action = command_data["action"]
    if not action:
        return {"result": "You perform no action."}

    # Get player information
    player = persistence.get_player_by_name(get_username_from_user(current_user))
    if not player:
        logger.warning(f"Emote command failed - player not found for {player_name}")
        return {"result": "You cannot emote right now."}

    # Initialize chat service
    from .game.player_service import PlayerService
    from .game.room_service import RoomService

    room_service = RoomService(persistence)
    player_service = PlayerService(persistence)
    chat_service = ChatService(persistence, room_service, player_service)

    # Send the emote
    result = await chat_service.send_emote_message(str(player.player_id), action)
    if result["success"]:
        formatted_message = f"{player.name} {action}"
        logger.info(f"Emote message sent successfully for {player_name}, action: {action}")
        return {"result": formatted_message}
    else:
        logger.warning(f"Emote message failed for {player_name}, error: {result.get('error')}")
        return {"result": result.get("error", "You cannot emote right now.")}


async def handle_pose_command(
    validated_command: Any, command_data: dict[str, Any], current_user: dict, persistence: Any, player_name: str
) -> dict:
    """Handle pose command with new validation system."""
    logger.debug(f"Processing pose command for {player_name}, pose: {command_data.get('pose')}")

    if not persistence:
        logger.warning(f"Pose command failed - no persistence layer for {player_name}")
        return {"result": "You cannot pose right now."}

    # Get player information
    player = persistence.get_player_by_name(get_username_from_user(current_user))
    if not player:
        logger.warning(f"Pose command failed - player not found for {player_name}")
        return {"result": "You cannot pose right now."}

    pose = command_data.get("pose")
    if pose:
        # Set the pose
        player.pose = pose
        persistence.update_player(player)
        logger.info(f"Pose set successfully for {player_name}: {pose}")
        return {"result": f"Your pose is now: {pose}"}
    else:
        # Clear the pose
        player.pose = None
        persistence.update_player(player)
        logger.info(f"Pose cleared successfully for {player_name}")
        return {"result": "Your pose has been cleared."}


async def handle_alias_command(
    validated_command: Any, command_data: dict[str, Any], alias_storage: AliasStorage, player_name: str
) -> dict:
    """Handle alias command with new validation system."""
    logger.debug(f"Processing alias command for {player_name}, alias_name: {command_data.get('alias_name')}")

    if not alias_storage:
        return {"result": "Alias system is not available."}

    alias_name = command_data.get("alias_name")
    alias_command = command_data.get("alias_command")

    if not alias_name:
        return {"result": "Usage: alias <name> <command>"}

    if not alias_command:
        return {"result": "Usage: alias <name> <command>"}

    # Create the alias
    try:
        alias_storage.create_alias(player_name, alias_name, alias_command)
        logger.info(f"Alias created successfully for {player_name}: {alias_name}")
        return {"result": f"Alias '{alias_name}' created for '{alias_command}'"}
    except Exception as e:
        logger.error(f"Failed to create alias for {player_name}: {alias_name}", error=str(e))
        return {"result": f"Failed to create alias: {str(e)}"}


async def handle_aliases_command(
    validated_command: Any, command_data: dict[str, Any], alias_storage: AliasStorage, player_name: str
) -> dict:
    """Handle aliases command with new validation system."""
    logger.debug(f"Processing aliases command for {player_name}")

    if not alias_storage:
        return {"result": "Alias system is not available."}

    try:
        aliases = alias_storage.get_aliases(player_name)
        if not aliases:
            return {"result": "You have no aliases defined."}

        alias_list = []
        for alias in aliases:
            alias_list.append(f"{alias.name}: {alias.command}")

        result = "Your aliases:\n" + "\n".join(alias_list)
        logger.info(f"Aliases retrieved successfully for {player_name}, count: {len(aliases)}")
        return {"result": result}
    except Exception as e:
        logger.error(f"Failed to retrieve aliases for {player_name}", error=str(e))
        return {"result": f"Failed to retrieve aliases: {str(e)}"}


async def handle_unalias_command(
    validated_command: Any, command_data: dict[str, Any], alias_storage: AliasStorage, player_name: str
) -> dict:
    """Handle unalias command with new validation system."""
    logger.debug(f"Processing unalias command for {player_name}, alias_name: {command_data.get('alias_name')}")

    if not alias_storage:
        return {"result": "Alias system is not available."}

    alias_name = command_data.get("alias_name")
    if not alias_name:
        return {"result": "Usage: unalias <name>"}

    try:
        alias_storage.delete_alias(player_name, alias_name)
        logger.info(f"Alias deleted successfully for {player_name}: {alias_name}")
        return {"result": f"Alias '{alias_name}' deleted."}
    except Exception as e:
        logger.error(f"Failed to delete alias for {player_name}: {alias_name}", error=str(e))
        return {"result": f"Failed to delete alias: {str(e)}"}


async def handle_admin_command(
    validated_command: Any, command_data: dict[str, Any], current_user: dict, persistence: Any, player_name: str
) -> dict:
    """Handle admin commands with new validation system."""
    logger.debug(f"Processing admin command for {player_name}, command_type: {command_data.get('command_type')}")

    # For now, return a placeholder response
    # TODO: Implement proper admin command handling
    return {"result": f"Admin command '{command_data.get('command_type')}' not yet implemented."}


async def handle_expanded_command(
    command_line: str,
    current_user: dict,
    request: Request,
    alias_storage: AliasStorage,
    player_name: str,
    depth: int = 0,
    alias_chain: list[dict] = None,
) -> dict:
    """Handle command processing with alias expansion and loop detection."""
    logger.debug(f"Handling expanded command for {player_name}, command_line: {command_line}, depth: {depth}")

    # Prevent infinite loops
    if depth > 10:
        logger.warning(f"Alias expansion depth limit exceeded for {player_name}, depth: {depth}")
        return {"result": "Alias expansion too deep - possible loop detected"}

    # Process the expanded command
    return await process_command_with_validation(command_line, current_user, request, alias_storage, player_name)


# Legacy function for backward compatibility
async def process_command(
    cmd: str, args: list, current_user: dict, request: Request, alias_storage: AliasStorage, player_name: str
) -> dict:
    """Legacy command processing function for backward compatibility."""
    logger.debug(f"Using legacy command processing for {player_name}, command: {cmd}, args: {args}")

    # Reconstruct the command line
    command_line = f"{cmd} {' '.join(args)}".strip()

    # Use the new validation system
    return await process_command_with_validation(command_line, current_user, request, alias_storage, player_name)
