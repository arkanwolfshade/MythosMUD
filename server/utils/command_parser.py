"""
Command parser for MythosMUD using Click for parsing and Pydantic for validation.

This module provides secure command parsing and validation to prevent command
injection and ensure type safety.
"""

import re

from pydantic import ValidationError

from ..logging_config import get_logger
from ..models.command import (
    AddAdminCommand,
    AliasCommand,
    AliasesCommand,
    Command,
    CommandType,
    EmoteCommand,
    GoCommand,
    GotoCommand,
    HelpCommand,
    LookCommand,
    MeCommand,
    MuteCommand,
    MuteGlobalCommand,
    MutesCommand,
    PoseCommand,
    SayCommand,
    TeleportCommand,
    UnaliasCommand,
    UnmuteCommand,
    UnmuteGlobalCommand,
)

logger = get_logger(__name__)


class CommandParser:
    """
    Secure command parser using Click for parsing and Pydantic for validation.

    Provides comprehensive command validation and injection prevention.
    """

    def __init__(self):
        self.max_command_length = 1000
        self.valid_commands = {cmd.value for cmd in CommandType}

        # Command factory mapping - maps command types to their creation methods
        # This eliminates the if/elif chain and provides O(1) lookup
        self._command_factory = {
            CommandType.LOOK.value: self._create_look_command,
            CommandType.GO.value: self._create_go_command,
            CommandType.SAY.value: self._create_say_command,
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
            CommandType.MUTES.value: self._create_mutes_command,
            CommandType.TELEPORT.value: self._create_teleport_command,
            CommandType.GOTO.value: self._create_goto_command,
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
            raise ValueError("Empty command")

        if len(command_string) > self.max_command_length:
            raise ValueError(f"Command too long (max {self.max_command_length} characters)")

        # Normalize command
        normalized = self._normalize_command(command_string)

        # Parse command and arguments
        command, args = self._parse_command_parts(normalized)

        # Validate command type
        if command not in self.valid_commands:
            raise ValueError(f"Unknown command: {command}")

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
        parts = command_string.split()
        if not parts:
            raise ValueError("Empty command after parsing")

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
            # Use the factory to get the creation method
            create_method = self._command_factory.get(command)
            if create_method:
                return create_method(args)
            else:
                raise ValueError(f"Unsupported command: {command}")

        except ValidationError as e:
            logger.warning("Command validation failed", command=command, args=args, errors=e.errors())
            raise ValueError(f"Invalid command format: {e}") from e
        except Exception as e:
            logger.error("Command creation failed", command=command, args=args, error=str(e))
            raise ValueError(f"Failed to create command: {e}") from e

    def _create_look_command(self, args: list[str]) -> LookCommand:
        """Create LookCommand from arguments."""
        direction = args[0] if args else None
        # Convert to lowercase for case-insensitive matching
        if direction:
            direction = direction.lower()
        return LookCommand(direction=direction)

    def _create_go_command(self, args: list[str]) -> GoCommand:
        """Create GoCommand from arguments."""
        if not args:
            raise ValueError("Go command requires a direction")
        # Convert to lowercase for case-insensitive matching
        direction = args[0].lower()
        return GoCommand(direction=direction)

    def _create_say_command(self, args: list[str]) -> SayCommand:
        """Create SayCommand from arguments."""
        if not args:
            raise ValueError("Say command requires a message")
        message = " ".join(args)
        return SayCommand(message=message)

    def _create_emote_command(self, args: list[str]) -> EmoteCommand:
        """Create EmoteCommand from arguments."""
        if not args:
            raise ValueError("Emote command requires an action")
        action = " ".join(args)
        return EmoteCommand(action=action)

    def _create_me_command(self, args: list[str]) -> MeCommand:
        """Create MeCommand from arguments."""
        if not args:
            raise ValueError("Me command requires an action")
        action = " ".join(args)
        return MeCommand(action=action)

    def _create_pose_command(self, args: list[str]) -> PoseCommand:
        """Create PoseCommand from arguments."""
        pose = " ".join(args) if args else None
        return PoseCommand(pose=pose)

    def _create_alias_command(self, args: list[str]) -> AliasCommand:
        """Create AliasCommand from arguments."""
        if not args:
            raise ValueError("Alias command requires an alias name")

        alias_name = args[0]
        command = " ".join(args[1:]) if len(args) > 1 else None

        return AliasCommand(alias_name=alias_name, command=command)

    def _create_aliases_command(self, args: list[str]) -> AliasesCommand:
        """Create AliasesCommand from arguments."""
        if args:
            raise ValueError("Aliases command takes no arguments")
        return AliasesCommand()

    def _create_unalias_command(self, args: list[str]) -> UnaliasCommand:
        """Create UnaliasCommand from arguments."""
        if not args:
            raise ValueError("Unalias command requires an alias name")
        if len(args) > 1:
            raise ValueError("Unalias command takes only one argument")

        return UnaliasCommand(alias_name=args[0])

    def _create_help_command(self, args: list[str]) -> HelpCommand:
        """Create HelpCommand from arguments."""
        topic = args[0] if args else None
        return HelpCommand(topic=topic)

    def _create_mute_command(self, args: list[str]) -> MuteCommand:
        """Create MuteCommand from arguments."""
        if not args:
            raise ValueError("Mute command requires a player name")

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
            raise ValueError("Unmute command requires a player name")
        if len(args) > 1:
            raise ValueError("Unmute command takes only one argument")

        return UnmuteCommand(player_name=args[0])

    def _create_mute_global_command(self, args: list[str]) -> MuteGlobalCommand:
        """Create MuteGlobalCommand from arguments."""
        if not args:
            raise ValueError("Mute_global command requires a player name")

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
            raise ValueError("Unmute_global command requires a player name")
        if len(args) > 1:
            raise ValueError("Unmute_global command takes only one argument")

        return UnmuteGlobalCommand(player_name=args[0])

    def _create_add_admin_command(self, args: list[str]) -> AddAdminCommand:
        """Create AddAdminCommand from arguments."""
        if not args:
            raise ValueError("Add_admin command requires a player name")
        if len(args) > 1:
            raise ValueError("Add_admin command takes only one argument")

        return AddAdminCommand(player_name=args[0])

    def _create_mutes_command(self, args: list[str]) -> MutesCommand:
        """Create MutesCommand from arguments."""
        if args:
            raise ValueError("Mutes command takes no arguments")
        return MutesCommand()

    def _create_teleport_command(self, args: list[str]) -> TeleportCommand:
        """Create TeleportCommand from arguments."""
        if not args:
            raise ValueError("Teleport command requires a player name")
        player_name = args[0]
        return TeleportCommand(player_name=player_name)

    def _create_goto_command(self, args: list[str]) -> GotoCommand:
        """Create GotoCommand from arguments."""
        if not args:
            raise ValueError("Goto command requires a player name")
        player_name = args[0]
        return GotoCommand(player_name=player_name)

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
        }

        return help_texts.get(command_type, f"No help available for: {command_type}")

    # Return general help
    return """
Available Commands:
- look [direction] - Look around or in a specific direction
- go <direction> - Move in a specific direction
- say <message> - Say something to other players
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

Directions: north, south, east, west
Use 'help <command>' for detailed information about a specific command.
"""


def get_username_from_user(user_obj) -> str:
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
