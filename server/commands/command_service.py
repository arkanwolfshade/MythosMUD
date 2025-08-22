"""
Command service for MythosMUD.

This module provides the main command processing service that orchestrates
command validation, routing, and execution.
"""

from typing import Any

from ..alias_storage import AliasStorage
from ..logging_config import get_logger
from ..validators.command_validator import (
    clean_command_input,
    normalize_command,
    validate_command_format,
)
from .admin_commands import (
    handle_add_admin_command,
    handle_mute_command,
    handle_mute_global_command,
    handle_mutes_command,
    handle_unmute_command,
    handle_unmute_global_command,
)
from .admin_teleport_commands import (
    handle_confirm_goto_command,
    handle_confirm_teleport_command,
    handle_goto_command,
    handle_teleport_command,
)
from .alias_commands import handle_alias_command, handle_aliases_command, handle_unalias_command
from .communication_commands import handle_me_command, handle_pose_command, handle_say_command
from .exploration_commands import handle_go_command, handle_look_command
from .system_commands import handle_help_command
from .utility_commands import (
    handle_emote_command,
    handle_inventory_command,
    handle_quit_command,
    handle_status_command,
    handle_who_command,
)

logger = get_logger(__name__)


class CommandService:
    """
    Main command processing service for MythosMUD.

    This service handles command validation, routing, and execution
    with proper error handling and logging.
    """

    def __init__(self):
        """Initialize the command service."""
        self.command_handlers = {
            # System commands
            "help": handle_help_command,
            # Alias commands
            "alias": handle_alias_command,
            "aliases": handle_aliases_command,
            "unalias": handle_unalias_command,
            # Exploration commands
            "look": handle_look_command,
            "go": handle_go_command,
            # Communication commands
            "say": handle_say_command,
            "me": handle_me_command,
            "pose": handle_pose_command,
            "emote": handle_emote_command,
            # Administrative commands
            "mute": handle_mute_command,
            "unmute": handle_unmute_command,
            "mute_global": handle_mute_global_command,
            "unmute_global": handle_unmute_global_command,
            "add_admin": handle_add_admin_command,
            "mutes": handle_mutes_command,
            # Admin teleport commands
            "teleport": handle_teleport_command,
            "goto": handle_goto_command,
            "confirm_teleport": handle_confirm_teleport_command,
            "confirm_goto": handle_confirm_goto_command,
            # Utility commands
            "who": handle_who_command,
            "quit": handle_quit_command,
            "status": handle_status_command,
            "inventory": handle_inventory_command,
        }

    async def process_validated_command(
        self,
        command_data: dict,
        current_user: dict,
        request: Any,
        alias_storage: AliasStorage,
        player_name: str,
    ) -> dict[str, str]:
        """
        Process a validated command with routing.

        Args:
            command_data: The validated command data dictionary
            current_user: Current user information
            request: FastAPI request object
            alias_storage: Alias storage instance
            player_name: Player name for logging

        Returns:
            dict: Command result with 'result' key
        """
        logger.debug("Processing validated command", player=player_name, command_data=command_data)

        command_type = command_data.get("command_type")
        if not command_type:
            logger.error("No command type in validated command data", player=player_name, command_data=command_data)
            return {"result": "Invalid command format"}

        # Get the appropriate handler
        handler = self.command_handlers.get(command_type)
        if not handler:
            logger.error("No handler found for command type", player=player_name, command_type=command_type)
            return {"result": f"Unknown command: {command_type}"}

        try:
            # Call the handler with the command data
            result = await handler(command_data, current_user, request, alias_storage, player_name)
            logger.debug("Command processed successfully", player=player_name, command_type=command_type)
            return result
        except Exception as e:
            logger.error(
                "Error in command handler", player=player_name, command_type=command_type, error=str(e), exc_info=True
            )
            return {"result": f"Error processing {command_type} command"}

    async def process_command(
        self,
        command: str,
        current_user: dict,
        request: Any,
        alias_storage: AliasStorage,
        player_name: str,
    ) -> dict[str, str]:
        """
        Process a command with full validation and routing.

        Args:
            command: The raw command string
            current_user: Current user information
            request: FastAPI request object
            alias_storage: Alias storage instance
            player_name: Player name for logging

        Returns:
            dict: Command result with 'result' key
        """
        logger.debug("Processing command", player=player_name, command=command)

        # Step 1: Validate and clean command
        validation_result, error_message = validate_command_format(command)
        if not validation_result:
            logger.info("Command validation failed", error=error_message)
            return {"result": f"Invalid command: {error_message}"}

        # Step 2: Normalize command
        normalized_command = normalize_command(command)
        cleaned_command = clean_command_input(normalized_command)

        if not cleaned_command:
            logger.debug("Empty command after cleaning", player=player_name)
            return {"result": "Empty command"}

        # Step 3: Parse command and arguments
        parts = cleaned_command.split()
        if not parts:
            logger.debug("No command parts after splitting", player=player_name)
            return {"result": "Empty command"}

        cmd = parts[0].lower()
        args = parts[1:] if len(parts) > 1 else []

        logger.debug("Command parsed", player=player_name, command=cmd, args=args)

        # Step 4: Route to appropriate handler
        if cmd in self.command_handlers:
            handler = self.command_handlers[cmd]
            try:
                result = await handler(args, current_user, request, alias_storage, player_name)
                logger.debug("Command processed successfully", player=player_name, command=cmd)
                return result
            except Exception as e:
                logger.error("Command processing error", player=player_name, command=cmd, error=str(e))
                return {"result": f"Error processing command: {str(e)}"}
        else:
            logger.info("Unknown command", command=cmd)
            return {"result": f"Unknown command: {cmd}. Use 'help' for available commands."}

    def get_available_commands(self) -> list[str]:
        """Get list of available commands."""
        return list(self.command_handlers.keys())

    def register_command_handler(self, command: str, handler: callable) -> None:
        """
        Register a new command handler.

        Args:
            command: Command name
            handler: Handler function
        """
        self.command_handlers[command] = handler
        logger.info("Command handler registered", command=command)

    def unregister_command_handler(self, command: str) -> None:
        """
        Unregister a command handler.

        Args:
            command: Command name to unregister
        """
        if command in self.command_handlers:
            del self.command_handlers[command]
            logger.info("Command handler unregistered", command=command)
