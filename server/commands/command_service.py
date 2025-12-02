"""
Command service for MythosMUD.

This module provides the main command processing service that orchestrates
command validation, routing, and execution.
"""

import traceback
from collections.abc import Awaitable, Callable
from typing import Any

from ..alias_storage import AliasStorage
from ..exceptions import ValidationError as MythosValidationError
from ..logging.enhanced_logging_config import get_logger
from ..utils.command_parser import parse_command
from ..validators.security_validator import strip_ansi_codes
from .admin_commands import (
    handle_add_admin_command,
    handle_admin_command,
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
from .admin_summon_command import handle_summon_command
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
from .inventory_commands import (
    handle_drop_command,
    handle_equip_command,
    handle_get_command,
    handle_inventory_command,
    handle_pickup_command,
    handle_put_command,
    handle_unequip_command,
)
from .lucidity_recovery_commands import (
    handle_folk_tonic_command,
    handle_group_solace_command,
    handle_meditate_command,
    handle_pray_command,
    handle_therapy_command,
)
from .npc_admin_commands import handle_npc_command
from .position_commands import handle_lie_command, handle_sit_command, handle_stand_command
from .rescue_commands import handle_ground_command
from .system_commands import handle_help_command
from .utility_commands import (
    handle_emote_command,
    handle_logout_command,
    handle_quit_command,
    handle_status_command,
    handle_time_command,
    handle_who_command,
    handle_whoami_command,
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
            "admin": handle_admin_command,
            "mutes": handle_mutes_command,
            "summon": handle_summon_command,
            # Admin teleport commands (confirmation removed for immediate execution)
            "teleport": handle_teleport_command,
            "goto": handle_goto_command,
            # Admin server management commands
            "shutdown": handle_shutdown_command,
            # Utility commands
            "who": handle_who_command,
            "whoami": handle_whoami_command,
            "quit": handle_quit_command,
            "logout": handle_logout_command,
            "status": handle_status_command,
            "time": handle_time_command,
            "inventory": handle_inventory_command,
            "pickup": handle_pickup_command,
            "drop": handle_drop_command,
            "put": handle_put_command,
            "get": handle_get_command,
            "equip": handle_equip_command,
            "unequip": handle_unequip_command,
            # Position commands
            "sit": handle_sit_command,
            "stand": handle_stand_command,
            "lie": handle_lie_command,
            # NPC Admin commands
            "npc": handle_npc_command,
            # Combat commands
            "attack": handle_attack_command,
            "punch": handle_punch_command,
            "kick": handle_kick_command,
            "strike": handle_strike_command,
            # lucidity recovery rites
            "pray": handle_pray_command,
            "meditate": handle_meditate_command,
            "group_solace": handle_group_solace_command,
            "therapy": handle_therapy_command,
            "folk_tonic": handle_folk_tonic_command,
            "ground": handle_ground_command,
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
            # Format exception traceback and sanitize ANSI codes for Windows compatibility
            try:
                exc_traceback = traceback.format_exc()
                # Strip ANSI codes to prevent UnicodeEncodeError on Windows console
                sanitized_traceback = strip_ansi_codes(exc_traceback)
                logger.error(
                    "Error in command handler",
                    player=player_name,
                    command_type=command_type,
                    command_data=command_data,
                    handler_function=str(handler),
                    error_type=type(e).__name__,
                    error_message=str(e),
                    traceback=sanitized_traceback,
                )
            except Exception as log_error:
                # If logging itself fails, use a minimal safe log
                try:
                    logger.error(
                        "Error in command handler (logging error occurred)",
                        player=player_name,
                        command_type=command_type,
                        error=str(e)[:200],  # Truncate to avoid encoding issues
                        log_error=str(log_error)[:200],
                    )
                except Exception:
                    # Last resort: silent failure to prevent test crashes
                    pass
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

            # CRITICAL: For commands with subcommands (admin, npc), reconstruct args array
            # to include subcommand as first element for backward compatibility with handlers
            if hasattr(parsed_command, "subcommand") and parsed_command.subcommand:
                args = [parsed_command.subcommand] + args

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

                # Merge parsed command fields (use Pydantic model_dump for completeness)
                try:
                    # DEBUG: Inspect parsed_command object before model_dump()
                    logger.error(
                        "DEBUG: parsed_command object inspection",
                        player=player_name,
                        command_type=cmd,
                        parsed_command_type=type(parsed_command).__name__,
                        parsed_command_module=type(parsed_command).__module__,
                        has_item=hasattr(parsed_command, "item"),
                        has_container=hasattr(parsed_command, "container"),
                    )

                    # Check if item and container exist and get their values
                    if hasattr(parsed_command, "item"):
                        item_value = getattr(parsed_command, "item", None)
                        logger.info(
                            "DEBUG: parsed_command.item value",
                            player=player_name,
                            command_type=cmd,
                            item_value=item_value,
                            item_type=type(item_value).__name__,
                        )
                    if hasattr(parsed_command, "container"):
                        container_value = getattr(parsed_command, "container", None)
                        logger.info(
                            "DEBUG: parsed_command.container value",
                            player=player_name,
                            command_type=cmd,
                            container_value=container_value,
                            container_type=type(container_value).__name__,
                        )

                    # Get all attributes of the parsed_command object
                    all_attrs = {
                        key: getattr(parsed_command, key, "<NOT FOUND>")
                        for key in dir(parsed_command)
                        if not key.startswith("_") and not callable(getattr(parsed_command, key, None))
                    }
                    logger.info(
                        "DEBUG: parsed_command all attributes",
                        player=player_name,
                        command_type=cmd,
                        all_attrs_keys=list(all_attrs.keys()),
                        all_attrs=all_attrs,
                    )

                    # Use model_dump without exclude_none to see all fields
                    # Then manually filter None values if needed
                    parsed_fields = parsed_command.model_dump()
                    logger.error(
                        "DEBUG: model_dump() result",
                        player=player_name,
                        command_type=cmd,
                        parsed_fields_keys=list(parsed_fields.keys()),
                        parsed_fields=parsed_fields,
                        has_item_in_result="item" in parsed_fields,
                        has_container_in_result="container" in parsed_fields,
                    )

                    # Filter None values manually
                    parsed_fields = {k: v for k, v in parsed_fields.items() if v is not None}
                    logger.info(
                        "DEBUG: parsed_fields after filtering None",
                        player=player_name,
                        command_type=cmd,
                        parsed_fields_keys=list(parsed_fields.keys()),
                        parsed_fields=parsed_fields,
                    )
                except AttributeError as e:
                    logger.error(
                        "ERROR: AttributeError during model_dump",
                        player=player_name,
                        command_type=cmd,
                        error=str(e),
                        error_type=type(e).__name__,
                    )
                    parsed_fields = {
                        key: getattr(parsed_command, key)
                        for key in dir(parsed_command)
                        if not key.startswith("_")
                        and not callable(getattr(parsed_command, key))
                        and key not in command_data
                    }
                except Exception as e:
                    logger.error(
                        "ERROR: Exception during model_dump",
                        player=player_name,
                        command_type=cmd,
                        error=str(e),
                        error_type=type(e).__name__,
                    )
                    raise
                command_data.update(parsed_fields)
                logger.error(
                    "Command data after merge",
                    player=player_name,
                    command_type=cmd,
                    command_data_keys=list(command_data.keys()),
                    command_data=command_data,
                )

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
