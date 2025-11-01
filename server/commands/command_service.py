"""
Command service for MythosMUD.

This module provides the main command processing service that orchestrates
command validation, routing, and execution.
"""

from collections.abc import Awaitable, Callable
from typing import Any

from ..alias_storage import AliasStorage
from ..exceptions import ValidationError as MythosValidationError
from ..logging.enhanced_logging_config import get_logger
from ..utils.command_parser import parse_command
from .admin_commands import (
    handle_add_admin_command,
    # Teleport commands now consolidated into admin_commands.py
    handle_goto_command,
    handle_mute_command,
    handle_mute_global_command,
    handle_mutes_command,
    handle_teleport_command,
    handle_unmute_command,
    handle_unmute_global_command,
)
from .admin_shutdown_command import handle_shutdown_command
from .alias_commands import (
    handle_alias_command,
    handle_aliases_command,
    handle_unalias_command,
)
from .combat import (
    handle_attack_command,
    handle_kick_command,
    handle_punch_command,
    handle_strike_command,
)
from .communication_commands import (
    handle_global_command,
    handle_local_command,
    handle_me_command,
    handle_pose_command,
    handle_reply_command,
    handle_say_command,
    handle_system_command,
    handle_whisper_command,
)
from .exploration_commands import handle_go_command, handle_look_command
from .npc_admin_commands import handle_npc_command
from .system_commands import handle_help_command
from .utility_commands import (
    handle_emote_command,
    handle_inventory_command,
    handle_logout_command,
    handle_quit_command,
    handle_status_command,
    handle_who_command,
)

logger = get_logger(__name__)

# Type alias for command handler functions
CommandHandler = Callable[[dict, dict, Any, AliasStorage | None, str], Awaitable[dict[str, str]]]


class CommandService:
    """
    Main command processing service for MythosMUD.

    This service handles command validation, routing, and execution
    with proper error handling and logging.
    """

    def __init__(self) -> None:
        """Initialize the command service."""
        self.command_handlers: dict[str, CommandHandler] = {
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
            "local": handle_local_command,
            "l": handle_local_command,  # Alias for local
            "global": handle_global_command,
            "g": handle_global_command,  # Alias for global
            "system": handle_system_command,
            "whisper": handle_whisper_command,
            "reply": handle_reply_command,
            "emote": handle_emote_command,
            # Administrative commands
            "mute": handle_mute_command,
            "unmute": handle_unmute_command,
            "mute_global": handle_mute_global_command,
            "unmute_global": handle_unmute_global_command,
            "add_admin": handle_add_admin_command,
            "mutes": handle_mutes_command,
            # Admin teleport commands (confirmation removed for immediate execution)
            "teleport": handle_teleport_command,
            "goto": handle_goto_command,
            # Admin server management commands
            "shutdown": handle_shutdown_command,
            # Utility commands
            "who": handle_who_command,
            "quit": handle_quit_command,
            "logout": handle_logout_command,
            "status": handle_status_command,
            "inventory": handle_inventory_command,
            # NPC Admin commands
            "npc": handle_npc_command,
            # Combat commands
            "attack": handle_attack_command,
            "punch": handle_punch_command,
            "kick": handle_kick_command,
            "strike": handle_strike_command,
        }

    async def process_validated_command(
        self,
        command_data: dict,
        current_user: dict,
        request: Any,
        alias_storage: AliasStorage | None,
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
        handler: CommandHandler | None = self.command_handlers.get(command_type)
        if not handler:
            logger.error("No handler found for command type", player=player_name, command_type=command_type)
            return {"result": f"Unknown command: {command_type}"}

        try:
            # Call handler with command_data (standardized format)
            # At this point handler is guaranteed to be CommandHandler (not None) due to check above
            logger.debug("DEBUG: About to call handler", handler=handler, command_data=command_data)
            assert handler is not None  # Type narrowing for mypy
            result = await handler(command_data, current_user, request, alias_storage, player_name)
            logger.debug(
                "Command processed successfully with command_data", player=player_name, command_type=command_type
            )
            # Type assertion to help MyPy understand the return type
            assert isinstance(result, dict)
            return result
        except Exception as e:
            logger.error(
                "Error in command handler",
                player=player_name,
                command_type=command_type,
                command_data=command_data,
                handler_function=str(handler),
                error_type=type(e).__name__,
                error_message=str(e),
                exc_info=True,
            )
            return {"result": f"Error processing {command_type} command: {str(e)}"}

    async def process_command(
        self,
        command: str,
        current_user: dict,
        request: Any,
        alias_storage: AliasStorage | None,
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

        # Step 1: Parse and validate command using the command parser
        try:
            parsed_command = parse_command(command)
            cmd = parsed_command.command_type.value
            args = getattr(parsed_command, "args", [])

            logger.debug("Command parsed successfully", player=player_name, command=cmd, args=args)
        except MythosValidationError as e:
            logger.info("Command validation failed", error=str(e))
            return {"result": str(e)}
        except Exception as e:
            logger.error("Unexpected error during command parsing", error=str(e))
            return {"result": f"Error processing command: {str(e)}"}

        # Step 4: Route to appropriate handler
        if cmd in self.command_handlers:
            handler: CommandHandler = self.command_handlers[cmd]
            try:
                # Create command_data dictionary for handler using parsed command data
                command_data = {
                    "command_type": cmd,
                    "args": args,
                    "target_player": args[0] if args else None,
                    "parsed_command": parsed_command,  # Include the full parsed command object
                }

                # Add command-specific data based on the parsed command
                if hasattr(parsed_command, "message"):
                    command_data["message"] = parsed_command.message
                if hasattr(parsed_command, "direction"):
                    command_data["direction"] = parsed_command.direction
                if hasattr(parsed_command, "target"):
                    command_data["target"] = parsed_command.target

                assert handler is not None  # Type narrowing for mypy
                result = await handler(command_data, current_user, request, alias_storage, player_name)
                logger.debug("Command processed successfully with command_data", player=player_name, command=cmd)
                # Type assertion to help MyPy understand the return type
                assert isinstance(result, dict)
                return result
            except Exception as e:
                logger.error(
                    "Command processing error",
                    player=player_name,
                    command=cmd,
                    command_data=command_data,
                    parsed_command=str(parsed_command),
                    handler_function=str(handler),
                    error_type=type(e).__name__,
                    error_message=str(e),
                    exc_info=True,
                )
                return {"result": f"Error processing command: {str(e)}"}
        else:
            logger.info("Unknown command", command=cmd)
            return {"result": f"Unknown command: {cmd}. Use 'help' for available commands."}

    def get_available_commands(self) -> list[str]:
        """Get list of available commands."""
        return list(self.command_handlers.keys())

    def register_command_handler(self, command: str, handler: Callable[..., Awaitable[dict[str, str]]]) -> None:
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
