"""
Exploration command factory methods.

This module contains factory methods for movement and exploration commands:
look, go, sit, stand, lie, ground.
"""

# pylint: disable=too-many-return-statements  # Reason: Command factory methods require multiple return statements for early validation returns (input validation, permission checks, error handling)

from typing import Literal, cast

from ..exceptions import ValidationError as MythosValidationError
from ..models.command import (
    Direction,
    GoCommand,
    GroundCommand,
    LieCommand,
    LookCommand,
    SitCommand,
    StandCommand,
)
from ..structured_logging.enhanced_logging_config import get_logger
from .enhanced_error_logging import create_error_context, log_and_raise_enhanced

logger = get_logger(__name__)


class ExplorationCommandFactory:
    """Factory class for creating exploration and movement command objects."""

    @staticmethod
    def _parse_instance_number(target: str) -> tuple[str, int | None]:
        """
        Parse instance number from target string.

        Supports two formats:
        - "backpack-2" (hyphen syntax)
        - "backpack 2" (space syntax)

        Args:
            target: Target string that may contain instance number

        Returns:
            Tuple of (target_name, instance_number) where instance_number is None if not found
        """
        import re

        # Try hyphen syntax first: "backpack-2"
        hyphen_match = re.match(r"^(.+)-(\d+)$", target)
        if hyphen_match:
            target_name = hyphen_match.group(1)
            instance_number = int(hyphen_match.group(2))
            return (target_name, instance_number)

        # Try space syntax: "backpack 2"
        space_match = re.match(r"^(.+)\s+(\d+)$", target)
        if space_match:
            target_name = space_match.group(1).rstrip()
            instance_number = int(space_match.group(2))
            return (target_name, instance_number)

        # No instance number found
        return (target, None)

    @staticmethod
    def create_look_command(args: list[str]) -> LookCommand:
        """
        Create LookCommand from arguments.

        Handles multiple types of look commands:
        1. 'look' - no arguments, general room look
        2. 'look north' - direction argument, look in specific direction (cardinal only)
        3. 'look guard' - NPC argument, look at specific NPC
        4. 'look player Armitage' - explicit player target type
        5. 'look item lantern' - explicit item target type
        6. 'look container backpack' - explicit container target type
        7. 'look in backpack' - container inspection mode
        8. 'look backpack-2' or 'look backpack 2' - instance targeting

        Args:
            args: List of command arguments

        Returns:
            LookCommand: Configured command object
        """
        if not args:
            # No arguments - general room look
            return LookCommand()

        # Check for explicit type syntax: /look player <name>, /look item <name>, etc.
        valid_target_types = ["player", "npc", "item", "container", "direction"]
        if args[0].lower() in valid_target_types:
            target_type_str = args[0].lower()
            # Cast to Literal type after validation
            target_type = cast(Literal["player", "npc", "item", "container", "direction"], target_type_str)
            # Get the rest of the arguments as the target
            remaining_args = args[1:] if len(args) > 1 else []
            if not remaining_args:
                # Explicit type but no target - treat as implicit
                return LookCommand()
            target = " ".join(remaining_args)
            # Parse instance number from target
            target, instance_number = ExplorationCommandFactory._parse_instance_number(target)
            return LookCommand(
                target=target,
                target_type=target_type,
                instance_number=instance_number,
            )

        # Check for container inspection syntax: /look in <container>
        if args[0].lower() == "in":
            remaining_args = args[1:] if len(args) > 1 else []
            if not remaining_args:
                # "in" but no target - treat as implicit
                return LookCommand()
            target = " ".join(remaining_args)
            # Parse instance number from target
            target, instance_number = ExplorationCommandFactory._parse_instance_number(target)
            return LookCommand(target=target, look_in=True, instance_number=instance_number)

        # Regular target parsing (implicit type)
        target = " ".join(args)
        # Parse instance number from target
        target, instance_number = ExplorationCommandFactory._parse_instance_number(target)
        target_lower = target.lower()

        # Check if it's a valid cardinal direction (diagonal directions removed)
        valid_directions = ["north", "south", "east", "west", "up", "down"]
        if target_lower in valid_directions:
            # Direction target - set both direction and target fields
            # Convert string to Direction enum after validation
            direction_enum = Direction(target_lower)
            return LookCommand(
                direction=direction_enum,
                target=target,
                instance_number=instance_number,
            )
        # Implicit target (will be resolved by priority in handler)
        return LookCommand(target=target, instance_number=instance_number)

    @staticmethod
    def create_go_command(args: list[str]) -> GoCommand:
        """Create GoCommand from arguments."""
        # #region agent log
        import json

        try:
            with open(r"e:\projects\GitHub\MythosMUD\.cursor\debug.log", "a", encoding="utf-8") as f:
                f.write(
                    json.dumps(
                        {
                            "sessionId": "debug-session",
                            "runId": "run1",
                            "hypothesisId": "E",
                            "location": "command_factories_exploration.py:142",
                            "message": "create_go_command entry",
                            "data": {"args": args},
                            "timestamp": int(__import__("time").time() * 1000),
                        }
                    )
                    + "\n"
                )
        except Exception:  # pylint: disable=broad-exception-caught  # noqa: B904, E722  # Reason: Debug logging must not fail, catch all exceptions to prevent failures
            pass
        # #endregion
        if not args:
            context = create_error_context()
            context.metadata = {"args": args}
            log_and_raise_enhanced(
                MythosValidationError, "Go command requires a direction", context=context, logger_name=__name__
            )
        # Convert to lowercase for case-insensitive matching
        direction = args[0].lower()
        # #region agent log
        try:
            with open(r"e:\projects\GitHub\MythosMUD\.cursor\debug.log", "a", encoding="utf-8") as f:
                f.write(
                    json.dumps(
                        {
                            "sessionId": "debug-session",
                            "runId": "run1",
                            "hypothesisId": "E",
                            "location": "command_factories_exploration.py:151",
                            "message": "Before GoCommand creation",
                            "data": {"direction": direction, "args": args},
                            "timestamp": int(__import__("time").time() * 1000),
                        }
                    )
                    + "\n"
                )
        except Exception:  # pylint: disable=broad-exception-caught  # noqa: B904, E722  # Reason: Debug logging must not fail, catch all exceptions to prevent failures
            pass
        # #endregion
        return GoCommand(direction=direction)

    @staticmethod
    def create_sit_command(args: list[str]) -> SitCommand:
        """Create SitCommand from arguments."""
        if args:
            context = create_error_context()
            context.metadata = {"args": args}
            log_and_raise_enhanced(
                MythosValidationError, "Sit command takes no arguments", context=context, logger_name=__name__
            )
        return SitCommand()

    @staticmethod
    def create_stand_command(args: list[str]) -> StandCommand:
        """Create StandCommand from arguments."""
        if args:
            context = create_error_context()
            context.metadata = {"args": args}
            log_and_raise_enhanced(
                MythosValidationError, "Stand command takes no arguments", context=context, logger_name=__name__
            )
        return StandCommand()

    @staticmethod
    def create_lie_command(args: list[str]) -> LieCommand:
        """Create LieCommand from arguments."""
        modifier: str | None = None
        if args:
            if len(args) == 1 and args[0].lower() == "down":
                modifier = "down"
            else:
                context = create_error_context()
                context.metadata = {"args": args}
                log_and_raise_enhanced(
                    MythosValidationError,
                    "Usage: lie [down]",
                    context=context,
                    logger_name=__name__,
                )
        return LieCommand(modifier=modifier)

    @staticmethod
    def create_ground_command(args: list[str]) -> GroundCommand:
        """Create GroundCommand from arguments."""

        if not args:
            context = create_error_context()
            context.metadata = {"args": args}
            log_and_raise_enhanced(
                MythosValidationError,
                "Usage: ground <player>",
                context=context,
                logger_name=__name__,
            )

        target = " ".join(args).strip()
        if not target:
            context = create_error_context()
            context.metadata = {"args": args}
            log_and_raise_enhanced(
                MythosValidationError,
                "Usage: ground <player>",
                context=context,
                logger_name=__name__,
            )

        return GroundCommand(target_player=target)
