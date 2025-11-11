"""
Tests for the new command validation system using Pydantic and Click.

This module tests the secure command parsing and validation functionality.
"""

import pytest
from pydantic import ValidationError as PydanticValidationError

from server.exceptions import ValidationError as MythosValidationError
from server.models.command import (
    AddAdminCommand,
    AdminCommand,
    AliasCommand,
    AliasesCommand,
    CommandType,
    Direction,
    EmoteCommand,
    GoCommand,
    HelpCommand,
    LieCommand,
    LookCommand,
    MeCommand,
    MuteCommand,
    MuteGlobalCommand,
    MutesCommand,
    PoseCommand,
    SayCommand,
    SitCommand,
    StandCommand,
    StatusCommand,
    TeleportCommand,
    UnaliasCommand,
    UnmuteCommand,
    UnmuteGlobalCommand,
    WhoamiCommand,
)
from server.utils.command_parser import CommandParser, get_command_help, parse_command, validate_command_safety


class TestCommandModels:
    """Test Pydantic command models."""

    def test_look_command_valid(self):
        """Test valid LookCommand creation."""
        # Look without direction
        cmd = LookCommand()
        assert cmd.command_type == CommandType.LOOK
        assert cmd.direction is None

        # Look with direction
        cmd = LookCommand(direction=Direction.NORTH)
        assert cmd.command_type == CommandType.LOOK
        assert cmd.direction == Direction.NORTH

    def test_look_command_invalid_direction(self):
        """Test LookCommand with invalid direction."""
        with pytest.raises(PydanticValidationError):
            LookCommand(direction="invalid")

    def test_look_command_with_target(self):
        """Test LookCommand with target field."""
        # Look with target only
        cmd = LookCommand(target="guard")
        assert cmd.command_type == CommandType.LOOK
        assert cmd.direction is None
        assert cmd.target == "guard"

        # Look with both direction and target (direction takes precedence)
        cmd = LookCommand(direction=Direction.NORTH, target="guard")
        assert cmd.command_type == CommandType.LOOK
        assert cmd.direction == Direction.NORTH
        assert cmd.target == "guard"

        # Look with target only (no direction)
        cmd = LookCommand(target="Dr. Francis Morgan")
        assert cmd.command_type == CommandType.LOOK
        assert cmd.direction is None
        assert cmd.target == "Dr. Francis Morgan"

    def test_go_command_valid(self):
        """Test valid GoCommand creation."""
        cmd = GoCommand(direction=Direction.SOUTH)
        assert cmd.command_type == CommandType.GO
        assert cmd.direction == Direction.SOUTH

    def test_go_command_missing_direction(self):
        """Test GoCommand without required direction."""
        with pytest.raises(PydanticValidationError):
            GoCommand()

    def test_say_command_valid(self):
        """Test valid SayCommand creation."""
        cmd = SayCommand(message="Hello, world!")
        assert cmd.command_type == CommandType.SAY
        assert cmd.message == "Hello, world!"

    def test_say_command_empty_message(self):
        """Test SayCommand with empty message."""
        with pytest.raises(PydanticValidationError):
            SayCommand(message="")

    def test_say_command_too_long(self):
        """Test SayCommand with message too long."""
        long_message = "x" * 501
        with pytest.raises(PydanticValidationError):
            SayCommand(message=long_message)

    def test_say_command_dangerous_characters(self):
        """Test SayCommand with dangerous characters (only HTML tags and injection patterns now)."""
        dangerous_messages = [
            "Hello<script>alert('xss')</script>",  # HTML tags blocked
            "Hello; rm -rf /",  # Semicolon blocked
            "Hello | cat /etc/passwd",  # Pipe blocked
        ]

        for message in dangerous_messages:
            with pytest.raises(PydanticValidationError):
                SayCommand(message=message)

    def test_emote_command_valid(self):
        """Test valid EmoteCommand creation."""
        cmd = EmoteCommand(action="waves hello")
        assert cmd.command_type == CommandType.EMOTE
        assert cmd.action == "waves hello"

    def test_emote_command_dangerous_characters(self):
        """Test EmoteCommand with dangerous characters (only HTML tags and injection patterns now)."""
        dangerous_actions = [
            "waves<script>alert('xss')</script>",  # HTML tags blocked
            "waves; rm -rf /",  # Semicolon blocked
        ]

        for action in dangerous_actions:
            with pytest.raises(PydanticValidationError):
                EmoteCommand(action=action)

    def test_me_command_valid(self):
        """Test valid MeCommand creation."""
        cmd = MeCommand(action="smiles warmly")
        assert cmd.command_type == CommandType.ME
        assert cmd.action == "smiles warmly"

    def test_pose_command_valid(self):
        """Test valid PoseCommand creation."""
        # Pose without description
        cmd = PoseCommand()
        assert cmd.command_type == CommandType.POSE
        assert cmd.pose is None

        # Pose with description
        cmd = PoseCommand(pose="stands tall and proud")
        assert cmd.command_type == CommandType.POSE
        assert cmd.pose == "stands tall and proud"

    def test_sit_command_model(self):
        """Test SitCommand creation."""
        cmd = SitCommand()
        assert cmd.command_type == CommandType.SIT

    def test_stand_command_model(self):
        """Test StandCommand creation."""
        cmd = StandCommand()
        assert cmd.command_type == CommandType.STAND

    def test_lie_command_model(self):
        """Test LieCommand creation with optional modifier."""
        cmd = LieCommand()
        assert cmd.command_type == CommandType.LIE
        assert cmd.modifier is None

        cmd = LieCommand(modifier="down")
        assert cmd.modifier == "down"

        with pytest.raises(PydanticValidationError):
            LieCommand(modifier="sideways")

    def test_status_command_model(self):
        """Test StatusCommand creation."""
        cmd = StatusCommand()
        assert cmd.command_type == CommandType.STATUS

    def test_whoami_command_model(self):
        """Test WhoamiCommand creation."""
        cmd = WhoamiCommand()
        assert cmd.command_type == CommandType.WHOAMI

    def test_alias_command_valid(self):
        """Test valid AliasCommand creation."""
        # View alias
        cmd = AliasCommand(alias_name="n")
        assert cmd.command_type == CommandType.ALIAS
        assert cmd.alias_name == "n"
        assert cmd.command is None

        # Create alias
        cmd = AliasCommand(alias_name="n", command="go north")
        assert cmd.command_type == CommandType.ALIAS
        assert cmd.alias_name == "n"
        assert cmd.command == "go north"

    def test_alias_command_invalid_name(self):
        """Test AliasCommand with invalid alias name."""
        invalid_names = ["123alias", "alias name", "1alias", "alias@name", "alias.name"]

        for name in invalid_names:
            with pytest.raises(PydanticValidationError):
                AliasCommand(alias_name=name)

    def test_aliases_command_valid(self):
        """Test valid AliasesCommand creation."""
        cmd = AliasesCommand()
        assert cmd.command_type == CommandType.ALIASES

    def test_unalias_command_valid(self):
        """Test valid UnaliasCommand creation."""
        cmd = UnaliasCommand(alias_name="n")
        assert cmd.command_type == CommandType.UNALIAS
        assert cmd.alias_name == "n"

    def test_help_command_valid(self):
        """Test valid HelpCommand creation."""
        # General help
        cmd = HelpCommand()
        assert cmd.command_type == CommandType.HELP
        assert cmd.topic is None

        # Specific help
        cmd = HelpCommand(topic="look")
        assert cmd.command_type == CommandType.HELP
        assert cmd.topic == "look"

    def test_mute_command_valid(self):
        """Test valid MuteCommand creation."""
        # Mute without duration/reason
        cmd = MuteCommand(player_name="testuser")
        assert cmd.command_type == CommandType.MUTE
        assert cmd.player_name == "testuser"
        assert cmd.duration_minutes is None
        assert cmd.reason is None

        # Mute with duration
        cmd = MuteCommand(player_name="testuser", duration_minutes=30)
        assert cmd.duration_minutes == 30

        # Mute with reason
        cmd = MuteCommand(player_name="testuser", reason="spam")
        assert cmd.reason == "spam"

    def test_mute_command_invalid_duration(self):
        """Test MuteCommand with invalid duration."""
        with pytest.raises(PydanticValidationError):
            MuteCommand(player_name="testuser", duration_minutes=0)

        with pytest.raises(PydanticValidationError):
            MuteCommand(player_name="testuser", duration_minutes=10081)  # > 1 week

    def test_mute_command_invalid_player_name(self):
        """Test MuteCommand with invalid player name."""
        invalid_names = ["123user", "user name", "1user", "user@name", "user.name"]

        for name in invalid_names:
            with pytest.raises(PydanticValidationError):
                MuteCommand(player_name=name)

    def test_unmute_command_valid(self):
        """Test valid UnmuteCommand creation."""
        cmd = UnmuteCommand(player_name="testuser")
        assert cmd.command_type == CommandType.UNMUTE
        assert cmd.player_name == "testuser"

    def test_mute_global_command_valid(self):
        """Test valid MuteGlobalCommand creation."""
        cmd = MuteGlobalCommand(player_name="testuser", duration_minutes=60, reason="global spam")
        assert cmd.command_type == CommandType.MUTE_GLOBAL
        assert cmd.player_name == "testuser"
        assert cmd.duration_minutes == 60
        assert cmd.reason == "global spam"

    def test_unmute_global_command_valid(self):
        """Test valid UnmuteGlobalCommand creation."""
        cmd = UnmuteGlobalCommand(player_name="testuser")
        assert cmd.command_type == CommandType.UNMUTE_GLOBAL
        assert cmd.player_name == "testuser"

    def test_add_admin_command_valid(self):
        """Test valid AddAdminCommand creation."""
        cmd = AddAdminCommand(player_name="testuser")
        assert cmd.command_type == CommandType.ADD_ADMIN
        assert cmd.player_name == "testuser"

    def test_mutes_command_valid(self):
        """Test valid MutesCommand creation."""
        cmd = MutesCommand()
        assert cmd.command_type == CommandType.MUTES

    def test_teleport_command_with_direction(self):
        """Test TeleportCommand with optional direction."""
        cmd = TeleportCommand(player_name="testuser", direction=Direction.EAST)
        assert cmd.command_type == CommandType.TELEPORT
        assert cmd.player_name == "testuser"
        assert cmd.direction == Direction.EAST

    def test_teleport_command_invalid_direction(self):
        """Test TeleportCommand rejects invalid directions."""
        with pytest.raises(PydanticValidationError):
            TeleportCommand(player_name="testuser", direction="invalid")

    def test_admin_command_status(self):
        """Test AdminCommand status subcommand creation."""
        cmd = AdminCommand(subcommand="status")
        assert cmd.command_type == CommandType.ADMIN
        assert cmd.subcommand == "status"
        assert cmd.args == []

        with pytest.raises(PydanticValidationError):
            AdminCommand(subcommand="invalid")


class TestCommandParser:
    """Test CommandParser functionality."""

    def setup_method(self):
        """Set up test fixtures."""
        self.parser = CommandParser()

    def test_parse_look_command(self):
        """Test parsing look command."""
        # Look without direction
        cmd = self.parser.parse_command("look")
        assert isinstance(cmd, LookCommand)
        assert cmd.direction is None
        assert cmd.target is None

        # Look with direction
        cmd = self.parser.parse_command("look north")
        assert isinstance(cmd, LookCommand)
        assert cmd.direction == Direction.NORTH
        assert cmd.target == "north"

        # Look with slash prefix
        cmd = self.parser.parse_command("/look south")
        assert isinstance(cmd, LookCommand)
        assert cmd.direction == Direction.SOUTH
        assert cmd.target == "south"

    def test_parse_look_command_with_target(self):
        """Test parsing look command with NPC targets."""
        # Look at NPC
        cmd = self.parser.parse_command("look guard")
        assert isinstance(cmd, LookCommand)
        assert cmd.direction is None
        assert cmd.target == "guard"

        # Look at NPC with slash prefix
        cmd = self.parser.parse_command("/look Dr. Francis Morgan")
        assert isinstance(cmd, LookCommand)
        assert cmd.direction is None
        assert cmd.target == "Dr. Francis Morgan"

        # Look at NPC with multi-word name
        cmd = self.parser.parse_command("look town guard")
        assert isinstance(cmd, LookCommand)
        assert cmd.direction is None
        assert cmd.target == "town guard"

        # Direction should still work as target
        cmd = self.parser.parse_command("look northeast")
        assert isinstance(cmd, LookCommand)
        assert cmd.direction == Direction.NORTHEAST
        assert cmd.target == "northeast"

    def test_parse_go_command(self):
        """Test parsing go command."""
        cmd = self.parser.parse_command("go east")
        assert isinstance(cmd, GoCommand)
        assert cmd.direction == Direction.EAST

    def test_parse_say_command(self):
        """Test parsing say command."""
        cmd = self.parser.parse_command("say Hello, world!")
        assert isinstance(cmd, SayCommand)
        assert cmd.message == "Hello, world!"

    def test_parse_emote_command(self):
        """Test parsing emote command."""
        cmd = self.parser.parse_command("emote waves hello")
        assert isinstance(cmd, EmoteCommand)
        assert cmd.action == "waves hello"

    def test_parse_me_command(self):
        """Test parsing me command."""
        cmd = self.parser.parse_command("me smiles warmly")
        assert isinstance(cmd, MeCommand)
        assert cmd.action == "smiles warmly"

    def test_parse_pose_command(self):
        """Test parsing pose command."""
        # Pose without description
        cmd = self.parser.parse_command("pose")
        assert isinstance(cmd, PoseCommand)
        assert cmd.pose is None

        # Pose with description
        cmd = self.parser.parse_command("pose stands tall")
        assert isinstance(cmd, PoseCommand)
        assert cmd.pose == "stands tall"

    def test_parse_status_and_whoami_commands(self):
        """Test parsing status and whoami commands."""
        cmd = self.parser.parse_command("status")
        assert isinstance(cmd, StatusCommand)

        cmd = self.parser.parse_command("/whoami")
        assert isinstance(cmd, WhoamiCommand)

        with pytest.raises(MythosValidationError):
            self.parser.parse_command("status now")

        with pytest.raises(MythosValidationError):
            self.parser.parse_command("whoami please")

    def test_parse_sit_command(self):
        """Test parsing sit command."""
        cmd = self.parser.parse_command("sit")
        assert isinstance(cmd, SitCommand)

        cmd = self.parser.parse_command("/sit")
        assert isinstance(cmd, SitCommand)

        with pytest.raises(MythosValidationError):
            self.parser.parse_command("sit now")

    def test_parse_stand_command(self):
        """Test parsing stand command."""
        cmd = self.parser.parse_command("stand")
        assert isinstance(cmd, StandCommand)

        cmd = self.parser.parse_command("/stand")
        assert isinstance(cmd, StandCommand)

        with pytest.raises(MythosValidationError):
            self.parser.parse_command("stand quickly")

    def test_parse_lie_command(self):
        """Test parsing lie command with optional modifier."""
        cmd = self.parser.parse_command("lie")
        assert isinstance(cmd, LieCommand)
        assert cmd.modifier is None

        cmd = self.parser.parse_command("lie down")
        assert isinstance(cmd, LieCommand)
        assert cmd.modifier == "down"

        cmd = self.parser.parse_command("/lie down")
        assert isinstance(cmd, LieCommand)
        assert cmd.modifier == "down"

        with pytest.raises(MythosValidationError):
            self.parser.parse_command("lie sideways")

    def test_parse_alias_command(self):
        """Test parsing alias command."""
        # View alias
        cmd = self.parser.parse_command("alias n")
        assert isinstance(cmd, AliasCommand)
        assert cmd.alias_name == "n"
        assert cmd.command is None

        # Create alias
        cmd = self.parser.parse_command("alias n go north")
        assert isinstance(cmd, AliasCommand)
        assert cmd.alias_name == "n"
        assert cmd.command == "go north"

    def test_parse_aliases_command(self):
        """Test parsing aliases command."""
        cmd = self.parser.parse_command("aliases")
        assert isinstance(cmd, AliasesCommand)

    def test_parse_unalias_command(self):
        """Test parsing unalias command."""
        cmd = self.parser.parse_command("unalias n")
        assert isinstance(cmd, UnaliasCommand)
        assert cmd.alias_name == "n"

    def test_parse_help_command(self):
        """Test parsing help command."""
        # General help
        cmd = self.parser.parse_command("help")
        assert isinstance(cmd, HelpCommand)
        assert cmd.topic is None

        # Specific help
        cmd = self.parser.parse_command("help look")
        assert isinstance(cmd, HelpCommand)
        assert cmd.topic == "look"

    def test_parse_admin_status_command(self):
        """Test parsing admin status command."""
        cmd = self.parser.parse_command("admin status")
        assert isinstance(cmd, AdminCommand)
        assert cmd.subcommand == "status"
        assert cmd.args == []

    def test_parse_teleport_command_with_direction(self):
        """Test parsing teleport command with optional direction."""
        cmd = self.parser.parse_command("teleport Ithaqua east")
        assert isinstance(cmd, TeleportCommand)
        assert cmd.player_name == "Ithaqua"
        assert str(cmd.direction) == Direction.EAST.value

    def test_parse_mute_command(self):
        """Test parsing mute command."""
        # Basic mute
        cmd = self.parser.parse_command("mute testuser")
        assert isinstance(cmd, MuteCommand)
        assert cmd.player_name == "testuser"
        assert cmd.duration_minutes is None
        assert cmd.reason is None

        # Mute with duration
        cmd = self.parser.parse_command("mute testuser 30")
        assert isinstance(cmd, MuteCommand)
        assert cmd.player_name == "testuser"
        assert cmd.duration_minutes == 30

        # Mute with reason
        cmd = self.parser.parse_command("mute testuser spam")
        assert isinstance(cmd, MuteCommand)
        assert cmd.player_name == "testuser"
        assert cmd.reason == "spam"

        # Mute with duration and reason
        cmd = self.parser.parse_command("mute testuser 30 spam")
        assert isinstance(cmd, MuteCommand)
        assert cmd.player_name == "testuser"
        assert cmd.duration_minutes == 30
        assert cmd.reason == "spam"

    def test_parse_unmute_command(self):
        """Test parsing unmute command."""
        cmd = self.parser.parse_command("unmute testuser")
        assert isinstance(cmd, UnmuteCommand)
        assert cmd.player_name == "testuser"

    def test_parse_mute_global_command(self):
        """Test parsing mute_global command."""
        cmd = self.parser.parse_command("mute_global testuser 60 global spam")
        assert isinstance(cmd, MuteGlobalCommand)
        assert cmd.player_name == "testuser"
        assert cmd.duration_minutes == 60
        assert cmd.reason == "global spam"

    def test_parse_unmute_global_command(self):
        """Test parsing unmute_global command."""
        cmd = self.parser.parse_command("unmute_global testuser")
        assert isinstance(cmd, UnmuteGlobalCommand)
        assert cmd.player_name == "testuser"

    def test_parse_add_admin_command(self):
        """Test parsing add_admin command."""
        cmd = self.parser.parse_command("add_admin testuser")
        assert isinstance(cmd, AddAdminCommand)
        assert cmd.player_name == "testuser"

    def test_parse_mutes_command(self):
        """Test parsing mutes command."""
        cmd = self.parser.parse_command("mutes")
        assert isinstance(cmd, MutesCommand)

    def test_parse_empty_command(self):
        """Test parsing empty command."""
        with pytest.raises(MythosValidationError, match="Empty command provided"):
            self.parser.parse_command("")

        with pytest.raises(MythosValidationError, match="Empty command provided"):
            self.parser.parse_command("   ")

    def test_parse_unknown_command(self):
        """Test parsing unknown command."""
        with pytest.raises(MythosValidationError, match="Unknown command"):
            self.parser.parse_command("unknown")

    def test_parse_command_too_long(self):
        """Test parsing command that's too long."""
        long_command = "say " + "x" * 1000
        with pytest.raises(MythosValidationError, match="Command too long"):
            self.parser.parse_command(long_command)

    def test_parse_command_with_extra_whitespace(self):
        """Test parsing command with extra whitespace."""
        cmd = self.parser.parse_command("  look   north  ")
        assert isinstance(cmd, LookCommand)
        assert cmd.direction == Direction.NORTH

    def test_parse_command_case_insensitive(self):
        """Test parsing command with different cases."""
        cmd = self.parser.parse_command("LOOK NORTH")
        assert isinstance(cmd, LookCommand)
        assert cmd.direction == Direction.NORTH


class TestCommandSafety:
    """Test command safety validation."""

    def test_validate_command_safety_valid(self):
        """Test safety validation with valid commands."""
        valid_commands = [
            "look",
            "go north",
            "say Hello, world!",
            "emote waves hello",
            "me smiles warmly",
            "pose stands tall",
            "alias n go north",
            "help look",
            "sit",
            "stand",
            "lie down",
            "whoami",
            "status",
        ]

        for command in valid_commands:
            assert validate_command_safety(command) is True

    def test_validate_command_safety_dangerous(self):
        """Test safety validation with dangerous commands."""
        dangerous_commands = [
            "say Hello; rm -rf /",
            "emote waves & goodbye",
            "me smiles | cat /etc/passwd",
            "say Hello `whoami`",
            "emote waves $(ls)",
            "me smiles %s",
            "say Hello<script>alert('xss')</script>",
            "emote waves __import__('os').system('ls')",
            "me smiles eval('print(1)')",
        ]

        for command in dangerous_commands:
            assert validate_command_safety(command) is False


class TestCommandHelp:
    """Test command help functionality."""

    def test_get_command_help_general(self):
        """Test getting general help."""
        help_text = get_command_help()
        assert "Available Commands:" in help_text
        assert "look [direction]" in help_text
        assert "go <direction>" in help_text
        assert "say <message>" in help_text
        assert "sit - Sit down and adopt a seated posture" in help_text
        assert "stand - Return to a standing posture" in help_text
        assert "lie [down] - Lie down on the ground" in help_text
        assert "whoami - Show your personal status (alias of status)" in help_text

    def test_get_command_help_specific(self):
        """Test getting specific command help."""
        help_text = get_command_help("look")
        assert "look [direction] - Look around or in a specific direction" in help_text

        help_text = get_command_help("say")
        assert "say <message> - Say something to other players" in help_text

        help_text = get_command_help("sit")
        assert "sit - Sit down and adopt a seated posture" in help_text

        help_text = get_command_help("stand")
        assert "stand - Return to a standing posture" in help_text

        help_text = get_command_help("lie")
        assert "lie [down] - Lie down on the ground" in help_text

        help_text = get_command_help("whoami")
        assert "whoami - Show your personal status (alias of status)" in help_text

    def test_get_command_help_unknown(self):
        """Test getting help for unknown command."""
        help_text = get_command_help("unknown")
        assert "Unknown command: unknown" in help_text


class TestIntegration:
    """Integration tests for the command validation system."""

    def test_parse_command_function(self):
        """Test the global parse_command function."""
        cmd = parse_command("look north")
        assert isinstance(cmd, LookCommand)
        assert cmd.direction == Direction.NORTH

    def test_command_validation_workflow(self):
        """Test the complete command validation workflow."""
        # Valid command
        cmd = parse_command("say Hello, world!")
        assert isinstance(cmd, SayCommand)
        assert cmd.message == "Hello, world!"

        # Invalid command
        with pytest.raises(MythosValidationError):
            parse_command("say Hello<script>alert('xss')</script>")

        # Unknown command
        with pytest.raises(MythosValidationError, match="Unknown command"):
            parse_command("unknown")

    def test_command_safety_integration(self):
        """Test command safety validation integration."""
        # Safe command
        assert validate_command_safety("say Hello, world!")

        # Dangerous command
        assert not validate_command_safety("say Hello; rm -rf /")

    def test_help_integration(self):
        """Test help system integration."""
        help_text = get_command_help("look")
        assert "Look around or in a specific direction" in help_text
