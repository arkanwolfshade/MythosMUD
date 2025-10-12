"""
Command Processor - Integration layer for Pydantic + Click command validation.

This module provides a bridge between the existing command handler infrastructure
and our new robust command validation system using Pydantic models and Click-inspired parsing.

As noted in the Pnakotic Manuscripts: "The bridge between old and new must be
constructed with care, lest the foundations of both be compromised."
"""

from typing import Any

from pydantic import ValidationError

from ..logging_config import get_logger
from .command_parser import CommandParser, parse_command
from .error_logging import create_error_context

logger = get_logger(__name__)


class CommandProcessor:
    """
    Command processor that integrates Pydantic validation with existing command infrastructure.

    This class provides a clean interface for processing commands through our new
    validation system while maintaining compatibility with the existing command handler.
    """

    def __init__(self):
        """Initialize the command processor."""
        self.parser = CommandParser()
        logger.info("CommandProcessor initialized with Pydantic + Click validation")

    def process_command_string(self, command_line: str, player_name: str) -> tuple[Any | None, str | None, str | None]:
        """
        Process a raw command string through the new validation system.

        Args:
            command_line: The raw command string from user input
            player_name: The name of the player executing the command

        Returns:
            Tuple of (validated_command_object, error_message, command_type)
            - validated_command_object: The parsed and validated Pydantic command object
            - error_message: Error message if validation failed, None if successful
            - command_type: The type of command (e.g., 'look', 'go', 'say')
        """
        try:
            # Parse and validate the command using our new system
            validated_command = parse_command(command_line)

            # Extract command type for routing
            command_type = validated_command.command_type.value

            logger.debug(f"Command successfully validated for {player_name}: type={command_type}, cmd='{command_line}'")

            return validated_command, None, command_type

        except ValidationError as e:
            # Handle Pydantic validation errors
            error_details = []
            for error in e.errors():
                field = error.get("loc", ["unknown"])[-1]
                message = error.get("msg", "Validation error")
                error_details.append(f"{field}: {message}")

            error_message = "; ".join(error_details)
            context = create_error_context()
            context.metadata = {
                "player_name": player_name,
                "command_line": command_line,
                "validation_errors": error_details,
            }
            logger.warning(f"Command validation failed: {error_message}")

            return None, f"Invalid command: {error_message}", None

        except ValueError as e:
            # Handle parser-specific errors (e.g., unknown commands)
            error_message = str(e)
            context = create_error_context()
            context.metadata = {
                "player_name": player_name,
                "command_line": command_line,
                "error_type": "ValueError",
                "error_message": error_message,
            }
            logger.warning(f"Command parsing failed: {error_message}")

            return None, error_message, None

        except Exception as e:
            # Handle unexpected errors
            error_message = f"Unexpected error processing command: {str(e)}"
            context = create_error_context()
            context.metadata = {
                "player_name": player_name,
                "command_line": command_line,
                "error_type": type(e).__name__,
                "error_message": str(e),
            }
            logger.error(f"Unexpected error in command processing: {error_message}")

            return None, error_message, None

    def extract_command_data(self, validated_command: Any) -> dict[str, Any]:
        """
        Extract command data from a validated Pydantic command object.

        This method converts our validated command objects into a format
        compatible with the existing command processing logic.

        Args:
            validated_command: The validated Pydantic command object

        Returns:
            Dictionary containing the command data in a format expected by existing handlers
        """
        command_data = {
            "command_type": validated_command.command_type,  # Already a string value due to use_enum_values=True
            "player_name": None,  # Will be set by the calling code
        }

        # Extract command-specific data based on type
        if hasattr(validated_command, "direction"):
            # Direction is already a string value due to use_enum_values=True
            command_data["direction"] = validated_command.direction

        if hasattr(validated_command, "message"):
            command_data["message"] = validated_command.message

        if hasattr(validated_command, "action"):
            command_data["action"] = validated_command.action

        if hasattr(validated_command, "pose"):
            command_data["pose"] = validated_command.pose

        if hasattr(validated_command, "alias_name"):
            command_data["alias_name"] = validated_command.alias_name

        if hasattr(validated_command, "alias_command"):
            command_data["alias_command"] = validated_command.alias_command

        if hasattr(validated_command, "duration_minutes"):
            command_data["duration_minutes"] = validated_command.duration_minutes

        if hasattr(validated_command, "reason"):
            command_data["reason"] = validated_command.reason

        if hasattr(validated_command, "player_name"):
            command_data["target_player"] = validated_command.player_name

        if hasattr(validated_command, "filter_name"):
            command_data["filter_name"] = validated_command.filter_name

        logger.debug(f"Extracted command data: type={command_data['command_type']}, keys={list(command_data.keys())}")

        return command_data

    def validate_command_safety(self, command_line: str) -> tuple[bool, str | None]:
        """
        Perform additional safety validation on command input.

        This provides an extra layer of security validation beyond the Pydantic models.

        Args:
            command_line: The raw command string

        Returns:
            Tuple of (is_safe, error_message)
        """
        # Use our existing safety validation
        from .command_parser import validate_command_safety

        is_safe = validate_command_safety(command_line)
        if is_safe:
            return True, None
        else:
            return False, "Command contains dangerous patterns"

    def get_command_help(self, command_name: str | None = None) -> str:
        """
        Get help information for commands.

        Args:
            command_name: Specific command to get help for, or None for general help

        Returns:
            Help text for the command(s)
        """
        try:
            return self.parser.get_command_help(command_name)
        except Exception as e:
            context = create_error_context()
            context.metadata = {"command_name": command_name, "error_type": type(e).__name__, "error_message": str(e)}
            logger.error(f"Error getting command help: {str(e)}")
            return "Help system temporarily unavailable."


# Global instance for use throughout the application
command_processor = CommandProcessor()


def get_command_processor() -> CommandProcessor:
    """
    Get the global command processor instance.

    Returns:
        The global CommandProcessor instance
    """
    return command_processor
