"""
Command Processor - Integration layer for Pydantic + Click command validation.

This module provides a bridge between the existing command handler infrastructure
and our new robust command validation system using Pydantic models and Click-inspired parsing.

As noted in the Pnakotic Manuscripts: "The bridge between old and new must be
constructed with care, lest the foundations of both be compromised."
"""

from typing import Any

from pydantic import ValidationError as PydanticValidationError

from ..exceptions import ValidationError as MythosValidationError
from ..logging.enhanced_logging_config import get_logger
from ..models.command import CommandType
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

            logger.debug(
                "Command successfully validated",
                player_name=player_name,
                command_type=command_type,
                command_line=command_line,
            )

            return validated_command, None, command_type

        except PydanticValidationError as e:
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
            logger.warning("Command validation failed", error_message=error_message)

            return None, f"Invalid command: {error_message}", None

        except MythosValidationError as e:
            # Handle validation errors with user-friendly messages
            error_message = str(e)
            logger.warning("Command validation failed", error_message=error_message)

            return None, error_message, None

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
            logger.warning("Command parsing failed", error_message=error_message)

            return None, error_message, None

        except (TypeError, AttributeError, KeyError, RuntimeError) as e:
            # Handle unexpected errors
            error_message = f"Unexpected error processing command: {str(e)}"
            context = create_error_context()
            context.metadata = {
                "player_name": player_name,
                "command_line": command_line,
                "error_type": type(e).__name__,
                "error_message": str(e),
            }
            logger.error("Unexpected error in command processing", error_message=error_message)

            return None, error_message, None

    def _extract_attributes(self, validated_command: Any, attribute_map: dict[str, str]) -> dict[str, Any]:
        """
        Extract attributes from validated command using a mapping configuration.

        Args:
            validated_command: The validated Pydantic command object
            attribute_map: Dictionary mapping source attribute names to target keys

        Returns:
            Dictionary containing extracted attributes
        """
        extracted = {}
        for source_attr, target_key in attribute_map.items():
            if hasattr(validated_command, source_attr):
                extracted[target_key] = getattr(validated_command, source_attr)
        return extracted

    def _is_combat_command(self, command_type: CommandType) -> bool:
        """
        Check if a command type is a combat command.

        Args:
            command_type: The command type to check

        Returns:
            True if the command is a combat command, False otherwise
        """
        return command_type in [
            CommandType.ATTACK,
            CommandType.PUNCH,
            CommandType.KICK,
            CommandType.STRIKE,
        ]

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

        # Define attribute mappings: source_attribute -> target_key
        # Special cases (target, player_name) are handled separately below
        attribute_map = {
            "direction": "direction",
            "message": "message",
            "target_player": "target_player",
            "index": "index",
            "quantity": "quantity",
            "item": "item",
            "container": "container",
            "prototype_id": "prototype_id",
            "target_type": "target_type",
            "search_term": "search_term",
            "action": "action",
            "pose": "pose",
            "alias_name": "alias_name",
            "subcommand": "subcommand",
            "alias_command": "alias_command",
            "duration_minutes": "duration_minutes",
            "reason": "reason",
            "filter_name": "filter_name",
            "target_slot": "target_slot",
            "slot": "slot",
            "look_in": "look_in",
            "instance_number": "instance_number",
            "spell_name": "spell_name",
            "args": "args",
        }

        # Extract standard attributes
        command_data.update(self._extract_attributes(validated_command, attribute_map))

        # Handle special case: target attribute
        if hasattr(validated_command, "target"):
            command_data["target"] = validated_command.target
            # For combat commands, also set target_player for compatibility
            if self._is_combat_command(command_data["command_type"]):
                command_data["target_player"] = validated_command.target

        # Handle special case: player_name maps to target_player
        if hasattr(validated_command, "player_name"):
            command_data["target_player"] = validated_command.player_name

        logger.debug(
            "Extracted command data", command_type=command_data["command_type"], keys=list(command_data.keys())
        )

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
        except (ValueError, TypeError, AttributeError, KeyError, RuntimeError) as e:
            context = create_error_context()
            context.metadata = {"command_name": command_name, "error_type": type(e).__name__, "error_message": str(e)}
            logger.error("Error getting command help", error=str(e))
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
