"""
Command parser for MythosMUD using Click for parsing and Pydantic for validation.

This module provides secure command parsing and validation to prevent command
injection and ensure type safety.
"""

import re
from typing import Any, Literal, cast

from pydantic import ValidationError as PydanticValidationError

from ..exceptions import ValidationError as MythosValidationError
from ..logging.enhanced_logging_config import get_logger
from ..models.command import (
    AddAdminCommand,
    AdminCommand,
    AliasCommand,
    AliasesCommand,
    AttackCommand,
    Command,
    CommandType,
    Direction,
    DropCommand,
    EmoteCommand,
    EquipCommand,
    GetCommand,
    GoCommand,
    GotoCommand,
    GroundCommand,
    HelpCommand,
    InventoryCommand,
    KickCommand,
    LieCommand,
    LocalCommand,
    LogoutCommand,
    LookCommand,
    MeCommand,
    MuteCommand,
    MuteGlobalCommand,
    MutesCommand,
    NPCCommand,
    PickupCommand,
    PoseCommand,
    PunchCommand,
    PutCommand,
    QuitCommand,
    ReplyCommand,
    SayCommand,
    ShutdownCommand,
    SitCommand,
    StandCommand,
    StatusCommand,
    StrikeCommand,
    SummonCommand,
    SystemCommand,
    TeleportCommand,
    TimeCommand,
    UnaliasCommand,
    UnequipCommand,
    UnmuteCommand,
    UnmuteGlobalCommand,
    WhisperCommand,
    WhoamiCommand,
    WhoCommand,
)
from .enhanced_error_logging import create_error_context, log_and_raise_enhanced

logger = get_logger(__name__)


class CommandParser:
    """
    Secure command parser using Click for parsing and Pydantic for validation.

    Provides comprehensive command validation and injection prevention.
    """

    def __init__(self) -> None:
        self.max_command_length = 1000
        self.valid_commands = {cmd.value for cmd in CommandType}

        # Command factory mapping - maps command types to their creation methods
        # This eliminates the if/elif chain and provides O(1) lookup
        self._command_factory = {
            CommandType.LOOK.value: self._create_look_command,
            CommandType.GO.value: self._create_go_command,
            CommandType.SAY.value: self._create_say_command,
            CommandType.LOCAL.value: self._create_local_command,
            CommandType.SYSTEM.value: self._create_system_command,
            CommandType.EMOTE.value: self._create_emote_command,
            CommandType.ME.value: self._create_me_command,
            CommandType.POSE.value: self._create_pose_command,
            CommandType.ALIAS.value: self._create_alias_command,
            CommandType.ALIASES.value: self._create_aliases_command,
            CommandType.UNALIAS.value: self._create_unalias_command,
            CommandType.HELP.value: self._create_help_command,
            CommandType.MUTE.value: self._create_mute_command,
            CommandType.UNMUTE.value: self._create_unmute_command,
            CommandType.MUTE_GLOBAL.value: self._create_mute_global_command,
            CommandType.UNMUTE_GLOBAL.value: self._create_unmute_global_command,
            CommandType.ADD_ADMIN.value: self._create_add_admin_command,
            CommandType.ADMIN.value: self._create_admin_command,
            CommandType.NPC.value: self._create_npc_command,
            CommandType.SUMMON.value: self._create_summon_command,
            CommandType.MUTES.value: self._create_mutes_command,
            CommandType.TELEPORT.value: self._create_teleport_command,
            CommandType.GOTO.value: self._create_goto_command,
            # Utility commands
            CommandType.WHO.value: self._create_who_command,
            CommandType.STATUS.value: self._create_status_command,
            CommandType.TIME.value: self._create_time_command,
            CommandType.WHOAMI.value: self._create_whoami_command,
            CommandType.INVENTORY.value: self._create_inventory_command,
            CommandType.PICKUP.value: self._create_pickup_command,
            CommandType.DROP.value: self._create_drop_command,
            CommandType.PUT.value: self._create_put_command,
            CommandType.GET.value: self._create_get_command,
            CommandType.EQUIP.value: self._create_equip_command,
            CommandType.UNEQUIP.value: self._create_unequip_command,
            CommandType.QUIT.value: self._create_quit_command,
            CommandType.LOGOUT.value: self._create_logout_command,
            CommandType.SIT.value: self._create_sit_command,
            CommandType.STAND.value: self._create_stand_command,
            CommandType.LIE.value: self._create_lie_command,
            CommandType.GROUND.value: self._create_ground_command,
            # Communication commands
            CommandType.WHISPER.value: self._create_whisper_command,
            CommandType.REPLY.value: self._create_reply_command,
            # Admin server management commands
            CommandType.SHUTDOWN.value: self._create_shutdown_command,
            # Combat commands
            CommandType.ATTACK.value: self._create_attack_command,
            CommandType.PUNCH.value: self._create_punch_command,
            CommandType.KICK.value: self._create_kick_command,
            CommandType.STRIKE.value: self._create_strike_command,
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
            context = create_error_context()
            context.metadata = {"command_length": len(command_string) if command_string else 0}
            log_and_raise_enhanced(
                MythosValidationError, "Empty command provided", context=context, logger_name=__name__
            )

        if len(command_string) > self.max_command_length:
            context = create_error_context()
            context.metadata = {"command_length": len(command_string), "max_length": self.max_command_length}
            log_and_raise_enhanced(
                MythosValidationError,
                f"Command too long (max {self.max_command_length} characters)",
                context=context,
                logger_name=__name__,
            )

        # Normalize command
        normalized = self._normalize_command(command_string)

        # Parse command and arguments
        command, args = self._parse_command_parts(normalized)

        # Validate command type (including aliases)
        valid_commands_with_aliases = self.valid_commands | {"l", "g"}  # Add aliases (no w for whisper)
        if command not in valid_commands_with_aliases:
            context = create_error_context()
            context.metadata = {"command": command, "valid_commands": list(valid_commands_with_aliases)}
            log_and_raise_enhanced(
                MythosValidationError, f"Unknown command: {command}", context=context, logger_name=__name__
            )

        # Create and validate command object
        return self._create_command_object(command, args)

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
            context = create_error_context()
            context.metadata = {"command_string": str(command_string)}
            log_and_raise_enhanced(
                MythosValidationError,
                "Mock object passed to command parser - test setup issue",
                context=context,
                logger_name=__name__,
            )

        parts = command_string.split()
        if not parts:
            context = create_error_context()
            context.metadata = {"command_string": command_string}
            log_and_raise_enhanced(
                MythosValidationError, "Empty command after parsing", context=context, logger_name=__name__
            )

        command = parts[0].lower()
        args = parts[1:] if len(parts) > 1 else []

        logger.debug("Command parsed", command=command, args=args)
        return command, args

    def _create_command_object(self, command: str, args: list[str]) -> Command:
        """
        Create and validate command object based on command type.

        Args:
            command: Command name
            args: Command arguments

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
                return create_method(args)  # type: ignore[return-value]
            else:
                context = create_error_context()
                context.metadata = {
                    "command": command,
                    "args": args,
                    "available_commands": list(self._command_factory.keys()),
                }
                log_and_raise_enhanced(
                    MythosValidationError, f"Unsupported command: {command}", context=context, logger_name=__name__
                )

        except MythosValidationError:
            # Re-raise MythosValidationError without wrapping it
            raise
        except PydanticValidationError as e:
            logger.warning("Command validation failed", command=command, args=args, errors=e.errors())
            context = create_error_context()
            context.metadata = {"command": command, "args": args, "validation_errors": e.errors()}
            log_and_raise_enhanced(
                MythosValidationError, f"Invalid command format: {e}", context=context, logger_name=__name__
            )
        except Exception as e:
            logger.error("Command creation failed", command=command, args=args, error=str(e))
            context = create_error_context()
            context.metadata = {
                "command": command,
                "args": args,
                "error_type": type(e).__name__,
                "error_message": str(e),
            }
            log_and_raise_enhanced(
                MythosValidationError, f"Failed to create command: {e}", context=context, logger_name=__name__
            )
            # This should never be reached due to log_and_raise_enhanced above
            raise RuntimeError("Unreachable code") from None

    def _create_look_command(self, args: list[str]) -> LookCommand:
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
            target, instance_number = self._parse_instance_number(target)
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
            target, instance_number = self._parse_instance_number(target)
            return LookCommand(target=target, look_in=True, instance_number=instance_number)

        # Regular target parsing (implicit type)
        target = " ".join(args)
        # Parse instance number from target
        target, instance_number = self._parse_instance_number(target)
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
        else:
            # Implicit target (will be resolved by priority in handler)
            return LookCommand(target=target, instance_number=instance_number)

    def _parse_instance_number(self, target: str) -> tuple[str, int | None]:
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

    def _create_go_command(self, args: list[str]) -> GoCommand:
        """Create GoCommand from arguments."""
        if not args:
            context = create_error_context()
            context.metadata = {"args": args}
            log_and_raise_enhanced(
                MythosValidationError, "Go command requires a direction", context=context, logger_name=__name__
            )
        # Convert to lowercase for case-insensitive matching
        direction = args[0].lower()
        return GoCommand(direction=direction)  # type: ignore[arg-type]

    def _create_say_command(self, args: list[str]) -> SayCommand:
        """Create SayCommand from arguments."""
        if not args:
            context = create_error_context()
            context.metadata = {"args": args}
            log_and_raise_enhanced(
                MythosValidationError, "Say command requires a message", context=context, logger_name=__name__
            )
        message = " ".join(args)
        return SayCommand(message=message)

    def _create_local_command(self, args: list[str]) -> LocalCommand:
        """Create LocalCommand from arguments."""
        if not args:
            context = create_error_context()
            context.metadata = {"args": args}
            log_and_raise_enhanced(
                MythosValidationError,
                "You must provide a message to send locally",
                context=context,
                logger_name=__name__,
            )
        message = " ".join(args)
        if len(message) > 500:
            context = create_error_context()
            context.metadata = {"args": args, "message_length": len(message)}
            log_and_raise_enhanced(
                MythosValidationError, "Local message too long", context=context, logger_name=__name__
            )
        return LocalCommand(message=message)

    def _create_system_command(self, args: list[str]) -> SystemCommand:
        """Create SystemCommand from arguments."""
        if not args:
            context = create_error_context()
            context.metadata = {"args": args}
            log_and_raise_enhanced(
                MythosValidationError, "System command requires a message", context=context, logger_name=__name__
            )
        message = " ".join(args)
        return SystemCommand(message=message)

    def _create_emote_command(self, args: list[str]) -> EmoteCommand:
        """Create EmoteCommand from arguments."""
        if not args:
            context = create_error_context()
            context.metadata = {"args": args}
            log_and_raise_enhanced(
                MythosValidationError, "Emote command requires an action", context=context, logger_name=__name__
            )
        action = " ".join(args)
        return EmoteCommand(action=action)

    def _create_me_command(self, args: list[str]) -> MeCommand:
        """Create MeCommand from arguments."""
        if not args:
            context = create_error_context()
            context.metadata = {"args": args}
            log_and_raise_enhanced(
                MythosValidationError, "Me command requires an action", context=context, logger_name=__name__
            )
        action = " ".join(args)
        return MeCommand(action=action)

    def _create_pose_command(self, args: list[str]) -> PoseCommand:
        """Create PoseCommand from arguments."""
        pose = " ".join(args) if args else None
        return PoseCommand(pose=pose)

    def _create_alias_command(self, args: list[str]) -> AliasCommand:
        """Create AliasCommand from arguments."""
        if not args:
            context = create_error_context()
            context.metadata = {"args": args}
            log_and_raise_enhanced(
                MythosValidationError, "Alias command requires an alias name", context=context, logger_name=__name__
            )

        alias_name = args[0]
        command = " ".join(args[1:]) if len(args) > 1 else None

        return AliasCommand(alias_name=alias_name, command=command)

    def _create_aliases_command(self, args: list[str]) -> AliasesCommand:
        """Create AliasesCommand from arguments."""
        if args:
            context = create_error_context()
            context.metadata = {"args": args}
            log_and_raise_enhanced(
                MythosValidationError, "Aliases command takes no arguments", context=context, logger_name=__name__
            )
        return AliasesCommand()

    def _create_unalias_command(self, args: list[str]) -> UnaliasCommand:
        """Create UnaliasCommand from arguments."""
        if not args:
            context = create_error_context()
            context.metadata = {"args": args}
            log_and_raise_enhanced(
                MythosValidationError, "Unalias command requires an alias name", context=context, logger_name=__name__
            )
        if len(args) > 1:
            context = create_error_context()
            context.metadata = {"args": args, "arg_count": len(args)}
            log_and_raise_enhanced(
                MythosValidationError, "Unalias command takes only one argument", context=context, logger_name=__name__
            )

        return UnaliasCommand(alias_name=args[0])

    def _create_help_command(self, args: list[str]) -> HelpCommand:
        """Create HelpCommand from arguments."""
        topic = args[0] if args else None
        return HelpCommand(topic=topic)

    def _create_mute_command(self, args: list[str]) -> MuteCommand:
        """Create MuteCommand from arguments."""
        if not args:
            context = create_error_context()
            context.metadata = {"args": args}
            log_and_raise_enhanced(
                MythosValidationError, "Mute command requires a player name", context=context, logger_name=__name__
            )

        player_name = args[0]
        duration_minutes = None
        reason = None

        # Parse optional duration
        if len(args) > 1:
            try:
                duration_minutes = int(args[1])
                # Reason is everything after duration
                if len(args) > 2:
                    reason = " ".join(args[2:])
            except ValueError:
                # If second arg isn't a number, treat everything after player name as reason
                reason = " ".join(args[1:])

        return MuteCommand(player_name=player_name, duration_minutes=duration_minutes, reason=reason)

    def _create_unmute_command(self, args: list[str]) -> UnmuteCommand:
        """Create UnmuteCommand from arguments."""
        if not args:
            context = create_error_context()
            context.metadata = {"args": args}
            log_and_raise_enhanced(
                MythosValidationError, "Unmute command requires a player name", context=context, logger_name=__name__
            )
        if len(args) > 1:
            context = create_error_context()
            context.metadata = {"args": args, "arg_count": len(args)}
            log_and_raise_enhanced(
                MythosValidationError, "Unmute command takes only one argument", context=context, logger_name=__name__
            )

        return UnmuteCommand(player_name=args[0])

    def _create_mute_global_command(self, args: list[str]) -> MuteGlobalCommand:
        """Create MuteGlobalCommand from arguments."""
        if not args:
            context = create_error_context()
            context.metadata = {"args": args}
            log_and_raise_enhanced(
                MythosValidationError,
                "Mute_global command requires a player name",
                context=context,
                logger_name=__name__,
            )

        player_name = args[0]
        duration_minutes = None
        reason = None

        # Parse optional duration
        if len(args) > 1:
            try:
                duration_minutes = int(args[1])
                # Reason is everything after duration
                if len(args) > 2:
                    reason = " ".join(args[2:])
            except ValueError:
                # If second arg isn't a number, treat everything after player name as reason
                reason = " ".join(args[1:])

        return MuteGlobalCommand(player_name=player_name, duration_minutes=duration_minutes, reason=reason)

    def _create_unmute_global_command(self, args: list[str]) -> UnmuteGlobalCommand:
        """Create UnmuteGlobalCommand from arguments."""
        if not args:
            context = create_error_context()
            context.metadata = {"args": args}
            log_and_raise_enhanced(
                MythosValidationError,
                "Unmute_global command requires a player name",
                context=context,
                logger_name=__name__,
            )
        if len(args) > 1:
            context = create_error_context()
            context.metadata = {"args": args, "arg_count": len(args)}
            log_and_raise_enhanced(
                MythosValidationError,
                "Unmute_global command takes only one argument",
                context=context,
                logger_name=__name__,
            )

        return UnmuteGlobalCommand(player_name=args[0])

    def _create_add_admin_command(self, args: list[str]) -> AddAdminCommand:
        """Create AddAdminCommand from arguments."""
        if not args:
            context = create_error_context()
            context.metadata = {"args": args}
            log_and_raise_enhanced(
                MythosValidationError, "Add_admin command requires a player name", context=context, logger_name=__name__
            )
        if len(args) > 1:
            context = create_error_context()
            context.metadata = {"args": args, "arg_count": len(args)}
            log_and_raise_enhanced(
                MythosValidationError,
                "Add_admin command takes only one argument",
                context=context,
                logger_name=__name__,
            )

        return AddAdminCommand(player_name=args[0])

    def _create_admin_command(self, args: list[str]) -> AdminCommand:
        """Create AdminCommand from arguments."""
        if not args:
            context = create_error_context()
            context.metadata = {"args": args}
            log_and_raise_enhanced(
                MythosValidationError, "Admin command requires a subcommand", context=context, logger_name=__name__
            )

        subcommand = args[0].lower()
        remaining_args = args[1:]

        if subcommand == "status" and remaining_args:
            context = create_error_context()
            context.metadata = {"args": args, "subcommand": subcommand}
            log_and_raise_enhanced(
                MythosValidationError,
                "Admin status command does not accept additional arguments",
                context=context,
                logger_name=__name__,
            )

        return AdminCommand(subcommand=subcommand, args=remaining_args)

    def _create_npc_command(self, args: list[str]) -> NPCCommand:
        """Create NPCCommand from arguments."""
        # NPC command can be called with or without subcommand
        # If no args, subcommand is None (will show help)
        # If args, first arg is subcommand, rest are args
        if not args:
            return NPCCommand(subcommand=None, args=[])

        subcommand = args[0].lower()
        remaining_args = args[1:]

        return NPCCommand(subcommand=subcommand, args=remaining_args)

    def _create_summon_command(self, args: list[str]) -> SummonCommand:
        """Create SummonCommand from arguments."""
        if not args:
            context = create_error_context()
            context.metadata = {"args": args}
            log_and_raise_enhanced(
                MythosValidationError,
                "Usage: summon <prototype_id> [quantity] [item|npc]",
                context=context,
                logger_name=__name__,
            )

        prototype_id = args[0]
        quantity: int | None = None
        target_type: Literal["item", "npc"] | None = None

        for token in args[1:]:
            lowered = token.lower()
            if lowered in {"item", "npc"} and target_type is None:
                target_type = cast(Literal["item", "npc"], lowered)
                continue
            if quantity is None:
                try:
                    parsed_quantity = int(token)
                except ValueError as error:
                    context = create_error_context()
                    context.metadata = {"args": args, "invalid_token": token}
                    log_and_raise_enhanced(
                        MythosValidationError,
                        "Usage: summon <prototype_id> [quantity] [item|npc]",
                        context=context,
                        logger_name=__name__,
                        error=error,
                    )
                if parsed_quantity <= 0:
                    context = create_error_context()
                    context.metadata = {"args": args, "invalid_quantity": parsed_quantity}
                    log_and_raise_enhanced(
                        MythosValidationError,
                        "Summon quantity must be a positive number.",
                        context=context,
                        logger_name=__name__,
                    )
                quantity = parsed_quantity
                continue

            # Extra positional argument that we don't recognise.
            context = create_error_context()
            context.metadata = {"args": args, "unexpected_token": token}
            log_and_raise_enhanced(
                MythosValidationError,
                "Usage: summon <prototype_id> [quantity] [item|npc]",
                context=context,
                logger_name=__name__,
            )

        return SummonCommand(
            prototype_id=prototype_id,
            quantity=quantity if quantity is not None else 1,
            target_type=target_type if target_type is not None else "item",
        )

    def _create_mutes_command(self, args: list[str]) -> MutesCommand:
        """Create MutesCommand from arguments."""
        if args:
            context = create_error_context()
            context.metadata = {"args": args}
            log_and_raise_enhanced(
                MythosValidationError, "Mutes command takes no arguments", context=context, logger_name=__name__
            )
        return MutesCommand()

    def _create_teleport_command(self, args: list[str]) -> TeleportCommand:
        """Create TeleportCommand from arguments."""
        if not args:
            context = create_error_context()
            context.metadata = {"args": args}
            log_and_raise_enhanced(
                MythosValidationError, "Teleport command requires a player name", context=context, logger_name=__name__
            )

        player_name = args[0]
        direction = None

        if len(args) > 1:
            if len(args) > 2:
                context = create_error_context()
                context.metadata = {"args": args}
                log_and_raise_enhanced(
                    MythosValidationError,
                    "Teleport command accepts at most one direction argument",
                    context=context,
                    logger_name=__name__,
                )
            raw_direction = args[1].lower()
            try:
                direction = Direction(raw_direction)
            except ValueError as error:
                context = create_error_context()
                context.metadata = {"args": args, "direction": raw_direction}
                log_and_raise_enhanced(
                    MythosValidationError,
                    "Teleport command direction must be a valid Mythos cardinal or intercardinal direction",
                    context=context,
                    logger_name=__name__,
                    error=error,
                )

        return TeleportCommand(player_name=player_name, direction=direction)

    def _create_goto_command(self, args: list[str]) -> GotoCommand:
        """Create GotoCommand from arguments."""
        if not args:
            context = create_error_context()
            context.metadata = {"args": args}
            log_and_raise_enhanced(
                MythosValidationError, "Goto command requires a player name", context=context, logger_name=__name__
            )
        player_name = args[0]
        return GotoCommand(player_name=player_name)

    def _create_who_command(self, args: list[str]) -> WhoCommand:
        """Create WhoCommand from arguments."""
        filter_name = args[0] if args else None
        return WhoCommand(filter_name=filter_name)

    def _create_status_command(self, args: list[str]) -> StatusCommand:
        """Create StatusCommand from arguments."""
        if args:
            context = create_error_context()
            context.metadata = {"args": args}
            log_and_raise_enhanced(
                MythosValidationError, "Status command takes no arguments", context=context, logger_name=__name__
            )
        return StatusCommand()

    def _create_time_command(self, args: list[str]) -> TimeCommand:
        """Create TimeCommand from arguments."""
        if args:
            context = create_error_context()
            context.metadata = {"args": args}
            log_and_raise_enhanced(
                MythosValidationError, "Time command takes no arguments", context=context, logger_name=__name__
            )
        return TimeCommand()

    def _create_whoami_command(self, args: list[str]) -> WhoamiCommand:
        """Create WhoamiCommand from arguments."""
        if args:
            context = create_error_context()
            context.metadata = {"args": args}
            log_and_raise_enhanced(
                MythosValidationError, "Whoami command takes no arguments", context=context, logger_name=__name__
            )
        return WhoamiCommand()

    def _create_inventory_command(self, args: list[str]) -> InventoryCommand:
        """Create InventoryCommand from arguments."""
        if args:
            context = create_error_context()
            context.metadata = {"args": args}
            log_and_raise_enhanced(
                MythosValidationError, "Inventory command takes no arguments", context=context, logger_name=__name__
            )
        return InventoryCommand()

    def _create_pickup_command(self, args: list[str]) -> PickupCommand:
        """Create pickup command supporting numeric indices or fuzzy names."""

        if not args:
            context = create_error_context()
            log_and_raise_enhanced(
                MythosValidationError,
                "Usage: pickup <item-number|item-name> [quantity]",
                context=context,
                logger_name=__name__,
            )

        quantity: int | None = None
        selector_tokens = list(args)

        if len(selector_tokens) > 1:
            potential_quantity = selector_tokens[-1]
            try:
                quantity_candidate = int(potential_quantity)
            except ValueError:
                quantity_candidate = None

            if quantity_candidate is not None:
                if quantity_candidate <= 0:
                    context = create_error_context()
                    context.metadata = {"args": args, "quantity": quantity_candidate}
                    log_and_raise_enhanced(
                        MythosValidationError,
                        "Quantity must be a positive integer.",
                        context=context,
                        logger_name=__name__,
                    )
                quantity = quantity_candidate
                selector_tokens = selector_tokens[:-1]

        if not selector_tokens:
            context = create_error_context()
            context.metadata = {"args": args}
            log_and_raise_enhanced(
                MythosValidationError,
                "Usage: pickup <item-number|item-name> [quantity]",
                context=context,
                logger_name=__name__,
            )

        primary_token = selector_tokens[0]
        index: int | None = None
        search_term: str | None = None

        try:
            index_candidate = int(primary_token)
        except ValueError:
            index_candidate = None

        if index_candidate is not None:
            if index_candidate <= 0:
                context = create_error_context()
                context.metadata = {"args": args, "index": index_candidate}
                log_and_raise_enhanced(
                    MythosValidationError,
                    "Item number must be a positive integer.",
                    context=context,
                    logger_name=__name__,
                )

            if len(selector_tokens) > 1:
                context = create_error_context()
                context.metadata = {"args": args}
                log_and_raise_enhanced(
                    MythosValidationError,
                    "Usage: pickup <item-number|item-name> [quantity]",
                    context=context,
                    logger_name=__name__,
                )

            index = index_candidate
        else:
            search_term = " ".join(selector_tokens).strip()
            if not search_term:
                context = create_error_context()
                context.metadata = {"args": args}
                log_and_raise_enhanced(
                    MythosValidationError,
                    "Pickup item name cannot be empty.",
                    context=context,
                    logger_name=__name__,
                )

        return PickupCommand(index=index, search_term=search_term, quantity=quantity)

    def _create_drop_command(self, args: list[str]) -> DropCommand:
        """Create drop command."""

        if not args:
            context = create_error_context()
            log_and_raise_enhanced(
                MythosValidationError,
                "Usage: drop <inventory-number> [quantity]",
                context=context,
                logger_name=__name__,
            )

        try:
            index = int(args[0])
        except ValueError:
            context = create_error_context()
            context.metadata = {"args": args}
            log_and_raise_enhanced(
                MythosValidationError, "Inventory index must be an integer", context=context, logger_name=__name__
            )

        quantity = None
        if len(args) > 1:
            try:
                quantity = int(args[1])
            except ValueError:
                context = create_error_context()
                context.metadata = {"args": args}
                log_and_raise_enhanced(
                    MythosValidationError,
                    "Quantity must be an integer",
                    context=context,
                    logger_name=__name__,
                )

        return DropCommand(index=index, quantity=quantity)

    def _create_put_command(self, args: list[str]) -> PutCommand:
        """
        Create put command.

        Supports: put <item> [in] <container> [quantity]
        The "in" keyword is optional.
        """
        if not args:
            context = create_error_context()
            log_and_raise_enhanced(
                MythosValidationError,
                "Usage: put <item> [in] <container> [quantity]",
                context=context,
                logger_name=__name__,
            )

        # Remove optional "in" keyword
        args_clean = [arg for arg in args if arg.lower() != "in"]

        if len(args_clean) < 2:
            context = create_error_context()
            log_and_raise_enhanced(
                MythosValidationError,
                "Usage: put <item> [in] <container> [quantity]",
                context=context,
                logger_name=__name__,
            )

        item = args_clean[0]
        container = args_clean[1]
        quantity = None

        # Check if last argument is a quantity
        if len(args_clean) > 2:
            try:
                quantity = int(args_clean[-1])
                if quantity <= 0:
                    context = create_error_context()
                    context.metadata = {"quantity": quantity}
                    log_and_raise_enhanced(
                        MythosValidationError,
                        "Quantity must be a positive integer",
                        context=context,
                        logger_name=__name__,
                    )
                # If quantity was parsed, container might be multi-word
                if len(args_clean) > 3:
                    container = " ".join(args_clean[1:-1])
            except ValueError:
                # Last arg is not a number, container might be multi-word
                container = " ".join(args_clean[1:])

        return PutCommand(item=item, container=container, quantity=quantity)

    def _create_get_command(self, args: list[str]) -> GetCommand:
        """
        Create get command.

        Supports: get <item> [from] <container> [quantity]
        The "from" keyword is optional.
        """
        if not args:
            context = create_error_context()
            log_and_raise_enhanced(
                MythosValidationError,
                "Usage: get <item> [from] <container> [quantity]",
                context=context,
                logger_name=__name__,
            )

        # Remove optional "from" keyword
        args_clean = [arg for arg in args if arg.lower() != "from"]

        if len(args_clean) < 2:
            context = create_error_context()
            log_and_raise_enhanced(
                MythosValidationError,
                "Usage: get <item> [from] <container> [quantity]",
                context=context,
                logger_name=__name__,
            )

        item = args_clean[0]
        container = args_clean[1]
        quantity = None

        # Check if last argument is a quantity
        if len(args_clean) > 2:
            try:
                quantity = int(args_clean[-1])
                if quantity <= 0:
                    context = create_error_context()
                    context.metadata = {"quantity": quantity}
                    log_and_raise_enhanced(
                        MythosValidationError,
                        "Quantity must be a positive integer",
                        context=context,
                        logger_name=__name__,
                    )
                # If quantity was parsed, container might be multi-word
                if len(args_clean) > 3:
                    container = " ".join(args_clean[1:-1])
            except ValueError:
                # Last arg is not a number, container might be multi-word
                container = " ".join(args_clean[1:])

        return GetCommand(item=item, container=container, quantity=quantity)

    def _create_equip_command(self, args: list[str]) -> EquipCommand:
        """Create equip command."""

        if not args:
            context = create_error_context()
            log_and_raise_enhanced(
                MythosValidationError,
                "Usage: equip <inventory-number|item-name> [slot]",
                context=context,
                logger_name=__name__,
            )

        selector_tokens = list(args)
        index: int | None = None
        search_term: str | None = None
        target_slot: str | None = None

        def _maybe_extract_slot(tokens: list[str]) -> tuple[list[str], str | None]:
            if not tokens:
                return tokens, None

            possible_slot = tokens[-1]
            normalized = possible_slot.strip().lower()
            known_slots = {
                "head",
                "torso",
                "legs",
                "feet",
                "hands",
                "left_hand",
                "right_hand",
                "main_hand",
                "off_hand",
                "accessory",
                "ring",
                "amulet",
                "belt",
                "backpack",
                "waist",
                "neck",
            }
            if normalized in known_slots:
                return tokens[:-1], normalized
            return tokens, None

        try:
            index_candidate = int(selector_tokens[0])
        except ValueError:
            index_candidate = None

        if index_candidate is not None:
            if index_candidate <= 0:
                context = create_error_context()
                context.metadata = {"args": args, "index": index_candidate}
                log_and_raise_enhanced(
                    MythosValidationError,
                    "Inventory index must be a positive integer.",
                    context=context,
                    logger_name=__name__,
                )
            index = index_candidate
            if len(selector_tokens) > 1:
                target_slot = selector_tokens[1].strip().lower()
        else:
            trimmed_tokens, inferred_slot = _maybe_extract_slot(selector_tokens)
            search_term = " ".join(trimmed_tokens or selector_tokens).strip()
            if not search_term:
                context = create_error_context()
                context.metadata = {"args": args}
                log_and_raise_enhanced(
                    MythosValidationError,
                    "Equip item name cannot be empty.",
                    context=context,
                    logger_name=__name__,
                )
            target_slot = inferred_slot

        return EquipCommand(index=index, search_term=search_term, target_slot=target_slot)

    def _create_unequip_command(self, args: list[str]) -> UnequipCommand:
        """Create unequip command."""

        if not args:
            context = create_error_context()
            log_and_raise_enhanced(
                MythosValidationError,
                "Usage: unequip <slot|item-name>",
                context=context,
                logger_name=__name__,
            )

        candidate = " ".join(args).strip()
        if not candidate:
            context = create_error_context()
            context.metadata = {"args": args}
            log_and_raise_enhanced(
                MythosValidationError,
                "Usage: unequip <slot|item-name>",
                context=context,
                logger_name=__name__,
            )

        normalized = candidate.lower()
        known_slots = {
            "head",
            "torso",
            "legs",
            "feet",
            "hands",
            "left_hand",
            "right_hand",
            "main_hand",
            "off_hand",
            "accessory",
            "ring",
            "amulet",
            "belt",
            "backpack",
            "waist",
            "neck",
        }

        if normalized in known_slots:
            return UnequipCommand(slot=candidate)

        return UnequipCommand(search_term=candidate)

    def _create_quit_command(self, args: list[str]) -> QuitCommand:
        """Create QuitCommand from arguments."""
        if args:
            context = create_error_context()
            context.metadata = {"args": args}
            log_and_raise_enhanced(
                MythosValidationError, "Quit command takes no arguments", context=context, logger_name=__name__
            )
        return QuitCommand()

    def _create_logout_command(self, args: list[str]) -> LogoutCommand:
        """Create LogoutCommand from arguments."""
        # Logout command ignores arguments (like quit command)
        # This allows for commands like "logout force now" to work
        return LogoutCommand()

    def _create_sit_command(self, args: list[str]) -> SitCommand:
        """Create SitCommand from arguments."""
        if args:
            context = create_error_context()
            context.metadata = {"args": args}
            log_and_raise_enhanced(
                MythosValidationError, "Sit command takes no arguments", context=context, logger_name=__name__
            )
        return SitCommand()

    def _create_stand_command(self, args: list[str]) -> StandCommand:
        """Create StandCommand from arguments."""
        if args:
            context = create_error_context()
            context.metadata = {"args": args}
            log_and_raise_enhanced(
                MythosValidationError, "Stand command takes no arguments", context=context, logger_name=__name__
            )
        return StandCommand()

    def _create_lie_command(self, args: list[str]) -> LieCommand:
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

    def _create_ground_command(self, args: list[str]) -> GroundCommand:
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

    def _create_shutdown_command(self, args: list[str]) -> ShutdownCommand:
        """
        Create ShutdownCommand from arguments.

        Args can be:
        - Empty: Default 10 second countdown
        - Number: Countdown duration in seconds
        - "cancel": Cancel active shutdown
        """
        return ShutdownCommand(args=args)

    def _create_whisper_command(self, args: list[str]) -> WhisperCommand:
        """Create a WhisperCommand from parsed arguments."""
        # Check if target is provided
        if len(args) < 1:
            context = create_error_context()
            context.metadata = {"args": args, "arg_count": len(args)}
            log_and_raise_enhanced(
                MythosValidationError, "Usage: whisper <player> <message>", context=context, logger_name=__name__
            )

        target = args[0]
        message = " ".join(args[1:]) if len(args) > 1 else ""

        # Check if message is provided (not empty or whitespace-only)
        if not message.strip():
            context = create_error_context()
            context.metadata = {"args": args, "target": target}
            log_and_raise_enhanced(
                MythosValidationError, "You must provide a message to whisper", context=context, logger_name=__name__
            )

        if len(message) > 500:
            context = create_error_context()
            context.metadata = {"args": args, "message_length": len(message)}
            log_and_raise_enhanced(
                MythosValidationError, "Whisper message too long", context=context, logger_name=__name__
            )

        return WhisperCommand(target=target, message=message)

    def _create_reply_command(self, args: list[str]) -> ReplyCommand:
        """Create a ReplyCommand from parsed arguments."""
        if not args:
            context = create_error_context()
            context.metadata = {"args": args}
            log_and_raise_enhanced(
                MythosValidationError, "Usage: reply <message>", context=context, logger_name=__name__
            )

        message = " ".join(args)

        if not message.strip():
            context = create_error_context()
            context.metadata = {"args": args, "message": message}
            log_and_raise_enhanced(
                MythosValidationError, "Usage: reply <message>", context=context, logger_name=__name__
            )

        return ReplyCommand(message=message)

    def _create_attack_command(self, args: list[str]) -> AttackCommand:
        """Create AttackCommand from arguments."""
        # Allow attack commands without targets - let the combat handler validate
        target = " ".join(args) if args else None
        return AttackCommand(target=target)

    def _create_punch_command(self, args: list[str]) -> PunchCommand:
        """Create PunchCommand from arguments."""
        # Allow punch commands without targets - let the combat handler validate
        target = " ".join(args) if args else None
        return PunchCommand(target=target)

    def _create_kick_command(self, args: list[str]) -> KickCommand:
        """Create KickCommand from arguments."""
        # Allow kick commands without targets - let the combat handler validate
        target = " ".join(args) if args else None
        return KickCommand(target=target)

    def _create_strike_command(self, args: list[str]) -> StrikeCommand:
        """Create StrikeCommand from arguments."""
        # Allow strike commands without targets - let the combat handler validate
        target = " ".join(args) if args else None
        return StrikeCommand(target=target)

    # Confirmation command creators removed - teleport commands now execute immediately
    # TODO: Add confirmation command creators as future feature for enhanced safety

    def get_command_help(self, command_name: str | None = None) -> str:
        """
        Get help information for commands.

        Args:
            command_name: Specific command to get help for, or None for general help

        Returns:
            Help text for the command(s)
        """
        # Define basic command help
        COMMAND_HELP = {
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
        }

        if command_name:
            # Return specific command help
            if command_name.lower() in COMMAND_HELP:
                return COMMAND_HELP[command_name.lower()]
            else:
                return f"No help available for command '{command_name}'"
        else:
            # Return general help
            help_text = "Available commands:\n"
            for cmd, info in COMMAND_HELP.items():
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


def validate_command_safety(command_string: str) -> bool:
    """
    Perform additional safety validation on command string.

    Args:
        command_string: Raw command string

    Returns:
        True if command is safe, False otherwise
    """
    # Check for obvious injection attempts
    dangerous_patterns = [
        r"[;|&`$()]",  # Shell metacharacters
        r"\b(and|or)\s*=\s*",  # SQL injection
        r"__import__|eval|exec|system|os\.",  # Python injection
        r"%[a-zA-Z]",  # Format string injection
        r"<script|javascript:",  # XSS attempts
    ]

    for pattern in dangerous_patterns:
        if re.search(pattern, command_string, re.IGNORECASE):
            logger.warning("Dangerous pattern detected in command", pattern=pattern, command=command_string)
            return False

    return True


def get_command_help(command_type: str | None = None) -> str:
    """
    Get help text for commands.

    Args:
        command_type: Specific command to get help for, or None for general help

    Returns:
        Help text string
    """
    if command_type:
        command_type = command_type.lower()
        if command_type not in [cmd.value for cmd in CommandType]:
            return f"Unknown command: {command_type}"

        # Return specific help for command
        help_texts = {
            CommandType.LOOK.value: "look [direction] - Look around or in a specific direction",
            CommandType.GO.value: "go <direction> - Move in a specific direction",
            CommandType.SAY.value: "say <message> - Say something to other players",
            CommandType.LOCAL.value: "local <message> - Send message to local channel (sub-zone)",
            CommandType.WHISPER.value: "whisper <player> <message> - Send private message to player",
            CommandType.REPLY.value: "reply <message> - Reply to last whisper received",
            CommandType.EMOTE.value: "emote <action> - Perform an action",
            CommandType.ME.value: "me <action> - Describe an action",
            CommandType.POSE.value: "pose [description] - Set or display your pose",
            CommandType.ALIAS.value: "alias <name> [command] - Create or view an alias",
            CommandType.ALIASES.value: "aliases - List all your aliases",
            CommandType.UNALIAS.value: "unalias <name> - Remove an alias",
            CommandType.HELP.value: "help [command] - Get help on commands",
            CommandType.MUTE.value: "mute <player> [duration] [reason] - Mute a player",
            CommandType.UNMUTE.value: "unmute <player> - Unmute a player",
            CommandType.MUTE_GLOBAL.value: "mute_global <player> [duration] [reason] - Globally mute a player",
            CommandType.UNMUTE_GLOBAL.value: "unmute_global <player> - Globally unmute a player",
            CommandType.ADD_ADMIN.value: "add_admin <player> - Make a player an admin",
            CommandType.MUTES.value: "mutes - Show your mute status",
            CommandType.SUMMON.value: "summon <prototype_id> [quantity] [item|npc] - Admin: conjure items or NPCs",
            CommandType.WHO.value: "who [player] - List online players with optional filtering",
            CommandType.STATUS.value: "status - Show your character status",
            CommandType.TIME.value: "time - Show the current Mythos time",
            CommandType.WHOAMI.value: "whoami - Show your personal status (alias of status)",
            CommandType.INVENTORY.value: "inventory - Show your inventory",
            CommandType.PICKUP.value: "pickup <item-number> [quantity] - Pick up a room item",
            CommandType.DROP.value: "drop <inventory-number> [quantity] - Drop an inventory item",
            CommandType.EQUIP.value: "equip <inventory-number> [slot] - Equip an item",
            CommandType.UNEQUIP.value: "unequip <slot> - Unequip an item",
            CommandType.QUIT.value: "quit - Quit the game",
            CommandType.SIT.value: "sit - Sit down and adopt a seated posture",
            CommandType.STAND.value: "stand - Return to a standing posture",
            CommandType.LIE.value: "lie [down] - Lie down on the ground",
        }

        return help_texts.get(command_type, f"No help available for: {command_type}")

    # Return general help
    return """
Available Commands:
- look [direction] - Look around or in a specific direction
- go <direction> - Move in a specific direction
- say <message> - Say something to other players
- local <message> - Send message to local channel (sub-zone)
- whisper <player> <message> - Send private message to player
- reply <message> - Reply to last whisper received
- emote <action> - Perform an action
- me <action> - Describe an action
- pose [description] - Set or display your pose
- alias <name> [command] - Create or view an alias
- aliases - List all your aliases
- unalias <name> - Remove an alias
- help [command] - Get help on commands
- mute <player> [duration] [reason] - Mute a player
- unmute <player> - Unmute a player
- mute_global <player> [duration] [reason] - Globally mute a player
- unmute_global <player> - Globally unmute a player
- add_admin <player> - Make a player an admin
- mutes - Show your mute status
- summon <prototype_id> [quantity] [item|npc] - Admin: conjure items or NPCs
- who [player] - List online players with optional filtering
- status - Show your character status
- time - Show the current Mythos time
- whoami - Show your personal status (alias of status)
- inventory - Show your inventory
- quit - Quit the game
- sit - Sit down and adopt a seated posture
- stand - Return to a standing posture
- lie [down] - Lie down on the ground

Directions: north, south, east, west
Use 'help <command>' for detailed information about a specific command.
"""


def get_username_from_user(user_obj: Any) -> str:
    """
    Safely extract username from user object or dictionary.

    This utility function eliminates code duplication across command handlers
    by providing a centralized way to extract usernames from various user object formats.
    As noted in the restricted archives, this pattern reduces maintenance burden
    and ensures consistent behavior across all command implementations.

    Args:
        user_obj: User object that may be a dict, object with attributes, or other format

    Returns:
        str: The username/name from the user object

    Raises:
        ValueError: If no username or name can be extracted from the user object
    """
    # User object attribute extraction factory - maps common attribute patterns
    # This eliminates the need for repetitive if/elif chains across command files

    # Handle Player objects (which have 'name' attribute)
    if hasattr(user_obj, "name") and hasattr(user_obj, "player_id"):
        return str(user_obj.name)
    elif hasattr(user_obj, "username"):
        return str(user_obj.username)
    elif hasattr(user_obj, "name"):
        return str(user_obj.name)
    elif isinstance(user_obj, dict) and "username" in user_obj:
        return str(user_obj["username"])
    elif isinstance(user_obj, dict) and "name" in user_obj:
        return str(user_obj["name"])
    else:
        context = create_error_context()
        context.metadata = {"user_obj_type": type(user_obj).__name__, "user_obj": str(user_obj)}
        log_and_raise_enhanced(
            MythosValidationError,
            "User object must have username or name attribute or key",
            context=context,
            logger_name=__name__,
        )
        # This should never be reached due to log_and_raise_enhanced above
        raise RuntimeError("Unreachable code")
