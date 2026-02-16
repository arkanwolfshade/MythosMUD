"""
Command parser for MythosMUD using Click for parsing and Pydantic for validation.

This module provides secure command parsing and validation to prevent command
injection and ensure type safety.
"""

import re

from pydantic import ValidationError as PydanticValidationError

from ..exceptions import ValidationError as MythosValidationError
from ..models.command import (
    Command,
    CommandType,
)
from ..structured_logging.enhanced_logging_config import get_logger
from .command_factories import CommandFactory
from .command_helpers import (  # noqa: F401  # pylint: disable=unused-import  # Reason: Imported for backwards compatibility, may be used in tests or external code, unused in this module
    get_command_help,
    get_username_from_user,
    validate_command_safety,
)
from .enhanced_error_logging import log_and_raise_enhanced

logger = get_logger(__name__)


class CommandParser:
    """
    Secure command parser using Click for parsing and Pydantic for validation.

    Provides comprehensive command validation and injection prevention.
    """

    def __init__(self) -> None:
        self.max_command_length = 1000
        self.valid_commands = {cmd.value for cmd in CommandType}
        self.factory = CommandFactory()

        # Command factory mapping - maps command types to their creation methods
        # This eliminates the if/elif chain and provides O(1) lookup
        self._command_factory = {
            CommandType.LOOK.value: self.factory.create_look_command,
            CommandType.GO.value: self.factory.create_go_command,
            CommandType.SAY.value: self.factory.create_say_command,
            CommandType.LOCAL.value: self.factory.create_local_command,
            CommandType.SYSTEM.value: self.factory.create_system_command,
            CommandType.EMOTE.value: self.factory.create_emote_command,
            CommandType.ME.value: self.factory.create_me_command,
            CommandType.POSE.value: self.factory.create_pose_command,
            CommandType.ALIAS.value: self.factory.create_alias_command,
            CommandType.ALIASES.value: self.factory.create_aliases_command,
            CommandType.UNALIAS.value: self.factory.create_unalias_command,
            CommandType.HELP.value: self.factory.create_help_command,
            CommandType.MUTE.value: self.factory.create_mute_command,
            CommandType.UNMUTE.value: self.factory.create_unmute_command,
            CommandType.MUTE_GLOBAL.value: self.factory.create_mute_global_command,
            CommandType.UNMUTE_GLOBAL.value: self.factory.create_unmute_global_command,
            CommandType.ADD_ADMIN.value: self.factory.create_add_admin_command,
            CommandType.ADMIN.value: self.factory.create_admin_command,
            CommandType.NPC.value: self.factory.create_npc_command,
            CommandType.SUMMON.value: self.factory.create_summon_command,
            CommandType.MUTES.value: self.factory.create_mutes_command,
            CommandType.TELEPORT.value: self.factory.create_teleport_command,
            CommandType.GOTO.value: self.factory.create_goto_command,
            # Utility commands
            CommandType.WHO.value: self.factory.create_who_command,
            CommandType.STATUS.value: self.factory.create_status_command,
            CommandType.TIME.value: self.factory.create_time_command,
            CommandType.WHOAMI.value: self.factory.create_whoami_command,
            CommandType.INVENTORY.value: self.factory.create_inventory_command,
            CommandType.PICKUP.value: self.factory.create_pickup_command,
            CommandType.DROP.value: self.factory.create_drop_command,
            CommandType.PUT.value: self.factory.create_put_command,
            CommandType.GET.value: self.factory.create_get_command,
            CommandType.EQUIP.value: self.factory.create_equip_command,
            CommandType.UNEQUIP.value: self.factory.create_unequip_command,
            CommandType.QUIT.value: self.factory.create_quit_command,
            CommandType.LOGOUT.value: self.factory.create_logout_command,
            CommandType.SIT.value: self.factory.create_sit_command,
            CommandType.STAND.value: self.factory.create_stand_command,
            CommandType.LIE.value: self.factory.create_lie_command,
            CommandType.REST.value: self.factory.create_rest_command,
            CommandType.GROUND.value: self.factory.create_ground_command,
            CommandType.FOLLOW.value: self.factory.create_follow_command,
            CommandType.UNFOLLOW.value: self.factory.create_unfollow_command,
            CommandType.FOLLOWING.value: self.factory.create_following_command,
            CommandType.PARTY.value: self.factory.create_party_command,
            # Communication commands
            CommandType.CHANNEL.value: self.factory.create_channel_command,
            CommandType.WHISPER.value: self.factory.create_whisper_command,
            CommandType.REPLY.value: self.factory.create_reply_command,
            # Admin server management commands
            CommandType.SHUTDOWN.value: self.factory.create_shutdown_command,
            # Combat commands
            CommandType.ATTACK.value: self.factory.create_attack_command,
            CommandType.PUNCH.value: self.factory.create_punch_command,
            CommandType.KICK.value: self.factory.create_kick_command,
            CommandType.STRIKE.value: self.factory.create_strike_command,
            # Magic commands
            CommandType.CAST.value: self.factory.create_cast_command,
            CommandType.SPELL.value: self.factory.create_spell_command,
            CommandType.SPELLS.value: self.factory.create_spells_command,
            CommandType.LEARN.value: self.factory.create_learn_command,
        }

    def parse_command(self, command_string: str) -> Command:
        """
        Parse and validate a command string.

        Args:
            command_string: Raw command string from user input

        Returns:
            Validated Command object

        Raises:
            ValueError: If command is invalid or contains injection attempts
            ValidationError: If command data doesn't match expected schema
        """
        logger.debug("Parsing command", command=command_string, length=len(command_string))

        # Basic input validation
        if not command_string or not command_string.strip():
            log_and_raise_enhanced(
                MythosValidationError,
                "Empty command provided",
                command_length=len(command_string) if command_string else 0,
                logger_name=__name__,
            )

        if len(command_string) > self.max_command_length:
            log_and_raise_enhanced(
                MythosValidationError,
                f"Command too long (max {self.max_command_length} characters)",
                command_length=len(command_string),
                max_length=self.max_command_length,
                logger_name=__name__,
            )

        # Normalize command
        normalized = self._normalize_command(command_string)

        # Parse command and arguments
        command, args = self._parse_command_parts(normalized)

        # Validate command type (including aliases)
        valid_commands_with_aliases = self.valid_commands | {"l", "g"}  # Add aliases (no w for whisper)
        if command not in valid_commands_with_aliases:
            log_and_raise_enhanced(
                MythosValidationError,
                f"Unknown command: {command}",
                command=command,
                valid_commands=list(valid_commands_with_aliases),
                logger_name=__name__,
            )

        # Create and validate command object (pass normalized + original for debug e.g. empty local)
        return self._create_command_object(command, args, raw_command=normalized, original_command=command_string)

    def _normalize_command(self, command_string: str) -> str:
        """
        Normalize command string by removing slash prefix and cleaning whitespace.

        Args:
            command_string: Raw command string

        Returns:
            Normalized command string
        """
        # Remove leading slash if present
        if command_string.startswith("/"):
            command_string = command_string[1:].strip()

        # Clean whitespace
        normalized = re.sub(r"\s+", " ", command_string).strip()

        logger.debug("Command normalized", original=command_string, normalized=normalized)
        return normalized

    def _parse_command_parts(self, command_string: str) -> tuple[str, list[str]]:
        """
        Parse command string into command and arguments.

        Args:
            command_string: Normalized command string

        Returns:
            Tuple of (command, arguments)
        """
        # Defensive programming: Handle mock objects during testing
        if hasattr(command_string, "_mock_name") or hasattr(command_string, "_mock_return_value"):
            logger.warning("Mock object passed to _parse_command_parts - this should not happen in production")
            log_and_raise_enhanced(
                MythosValidationError,
                "Mock object passed to command parser - test setup issue",
                command_string=str(command_string),
                logger_name=__name__,
            )

        parts = command_string.split()
        if not parts:
            log_and_raise_enhanced(
                MythosValidationError,
                "Empty command after parsing",
                command_string=command_string,
                logger_name=__name__,
            )

        command = parts[0].lower()
        args = parts[1:] if len(parts) > 1 else []

        logger.debug("Command parsed", command=command, args=args)
        return command, args

    def _create_command_object(
        self,
        command: str,
        args: list[str],
        raw_command: str | None = None,
        original_command: str | None = None,
    ) -> Command:
        """
        Create and validate command object based on command type.

        Args:
            command: Command name
            args: Command arguments
            raw_command: Normalized raw command string (for debug e.g. empty local)
            original_command: Pre-normalized command string from client (for debug)

        Returns:
            Validated Command object

        Raises:
            ValueError: If command creation fails
            ValidationError: If command validation fails
        """
        try:
            # Handle command aliases
            if command == "w":
                command = "whisper"
            elif command == "l":
                command = "local"
            elif command == "g":
                command = "global"

            # Use the factory to get the creation method
            create_method = self._command_factory.get(command)
            if create_method:
                from collections.abc import Callable
                from typing import cast

                # Pass raw_command and original_command for local so empty-args debug log can include them
                if command == "local":
                    result = cast(
                        Command,
                        self.factory.create_local_command(
                            args,
                            raw_command=raw_command,
                            original_command=original_command,
                        ),
                    )
                else:
                    # Dict values are heterogenous callables; cast to Callable for mypy operator
                    fn = cast(Callable[..., Command], create_method)
                    result = fn(args)  # fn returns Command after cast
                return result
            log_and_raise_enhanced(
                MythosValidationError,
                f"Unsupported command: {command}",
                command=command,
                args=args,
                available_commands=list(self._command_factory.keys()),
                logger_name=__name__,
            )

        except MythosValidationError:
            # Re-raise MythosValidationError without wrapping it
            raise
        except PydanticValidationError as e:
            log_and_raise_enhanced(
                MythosValidationError,
                f"Invalid command format: {e}",
                command=command,
                args=args,
                validation_errors=e.errors(),
                logger_name=__name__,
            )
        except (ValueError, TypeError, AttributeError, KeyError, RuntimeError) as e:
            logger.error("Command creation failed", command=command, args=args, error=str(e))
            log_and_raise_enhanced(
                MythosValidationError,
                f"Failed to create command: {e}",
                command=command,
                args=args,
                error_type=type(e).__name__,
                error_message=str(e),
                logger_name=__name__,
            )

    def get_command_help(self, command_name: str | None = None) -> str:
        """
        Get help information for commands.

        Args:
            command_name: Specific command to get help for, or None for general help

        Returns:
            Help text for the command(s)
        """
        # Define basic command help
        command_help = {  # pylint: disable=invalid-name  # Reason: Local variable, not a constant
            "look": "Examine your surroundings or look in a specific direction",
            "go": "Move in a specific direction (north, south, east, west)",
            "say": "Speak to other players in your current room",
            "emote": "Perform an action or emote",
            "me": "Perform an action or emote (alias for emote)",
            "pose": "Set or clear your pose description",
            "alias": "Create a command alias",
            "aliases": "List your command aliases",
            "unalias": "Remove a command alias",
            "help": "Show this help information",
            "summon": "Admin command: /summon <prototype_id> [quantity] [item|npc]",
            "sit": "Sit down and adopt a seated posture",
            "stand": "Return to a standing posture",
            "lie": "Lie down (optionally use 'lie down')",
            "ground": "Stabilise a catatonic ally back to lucidity",
            "time": "Show the current Mythos time",
            "learn": "Learn a spell by name (temporary command until quests/vendors are implemented)",
        }

        if command_name:
            # Return specific command help
            if command_name.lower() in command_help:
                return command_help[command_name.lower()]
            return f"No help available for command '{command_name}'"
        # Return general help
        help_text = "Available commands:\n"
        for cmd, info in command_help.items():
            help_text += f"  {cmd}: {info}\n"
        return help_text


# Global command parser instance
command_parser = CommandParser()


def parse_command(command_string: str) -> Command:
    """
    Parse and validate a command string using the global parser.

    Args:
        command_string: Raw command string from user input

    Returns:
        Validated Command object

    Raises:
        ValueError: If command is invalid or contains injection attempts
        ValidationError: If command data doesn't match expected schema
    """
    return command_parser.parse_command(command_string)


# Re-export helper functions for backward compatibility (imported at top)

__all__ = [
    "CommandParser",
    "command_parser",
    "parse_command",
    "validate_command_safety",
    "get_command_help",
    "get_username_from_user",
]
