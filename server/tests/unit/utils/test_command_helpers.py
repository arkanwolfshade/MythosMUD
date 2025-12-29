"""
Unit tests for command helper utilities.

Tests helper functions for command parsing and validation.
"""

import pytest

from server.exceptions import ValidationError as MythosValidationError
from server.models.command import CommandType
from server.utils.command_helpers import get_command_help, get_username_from_user, validate_command_safety


def test_validate_command_safety_safe_commands():
    """Test validate_command_safety with safe commands."""
    assert validate_command_safety("look") is True
    assert validate_command_safety("go north") is True
    assert validate_command_safety("say hello world") is True
    assert validate_command_safety("whisper player hello") is True


def test_validate_command_safety_shell_metacharacters():
    """Test validate_command_safety detects shell metacharacters."""
    assert validate_command_safety("look; rm -rf") is False
    assert validate_command_safety("go | cat") is False
    assert validate_command_safety("say & echo") is False
    assert validate_command_safety("whisper `ls`") is False
    assert validate_command_safety("say $(whoami)") is False


def test_validate_command_safety_sql_injection():
    """Test validate_command_safety detects SQL injection patterns."""
    assert validate_command_safety("look and = 1") is False
    assert validate_command_safety("go or = 1") is False


def test_validate_command_safety_python_injection():
    """Test validate_command_safety detects Python injection patterns."""
    assert validate_command_safety("look __import__('os')") is False
    assert validate_command_safety("go eval('1+1')") is False
    assert validate_command_safety("say exec('print(1)')") is False
    assert validate_command_safety("whisper system('ls')") is False
    assert validate_command_safety("look os.system") is False


def test_validate_command_safety_format_string_injection():
    """Test validate_command_safety detects format string injection."""
    assert validate_command_safety("look %s") is False
    assert validate_command_safety("go %d") is False
    assert validate_command_safety("say %x") is False


def test_validate_command_safety_xss_attempts():
    """Test validate_command_safety detects XSS attempts."""
    assert validate_command_safety("look <script>") is False
    assert validate_command_safety("go javascript:alert(1)") is False


def test_get_command_help_no_command():
    """Test get_command_help with no command (general help)."""
    result = get_command_help()

    assert "Available Commands:" in result
    assert "look" in result
    assert "go" in result
    assert "say" in result


def test_get_command_help_specific_commands():
    """Test get_command_help with specific command types."""
    assert "Look around" in get_command_help(CommandType.LOOK.value)
    assert "Move in" in get_command_help(CommandType.GO.value)
    assert "Say something" in get_command_help(CommandType.SAY.value)
    assert "Send private message" in get_command_help(CommandType.WHISPER.value)
    assert "Reply to last whisper" in get_command_help(CommandType.REPLY.value)


def test_get_command_help_unknown_command():
    """Test get_command_help with unknown command."""
    result = get_command_help("unknown_command")

    assert "Unknown command: unknown_command" == result


def test_get_command_help_case_insensitive():
    """Test get_command_help is case insensitive."""
    result_upper = get_command_help("LOOK")
    result_lower = get_command_help("look")

    assert result_upper == result_lower


def test_get_username_from_user_player_object():
    """Test get_username_from_user with Player object."""
    class MockPlayer:
        def __init__(self):
            self.name = "TestPlayer"
            self.player_id = "123"

    player = MockPlayer()
    assert get_username_from_user(player) == "TestPlayer"


def test_get_username_from_user_username_attribute():
    """Test get_username_from_user with username attribute."""
    class MockUser:
        def __init__(self):
            self.username = "testuser"

    user = MockUser()
    assert get_username_from_user(user) == "testuser"


def test_get_username_from_user_name_attribute():
    """Test get_username_from_user with name attribute."""
    class MockUser:
        def __init__(self):
            self.name = "TestUser"

    user = MockUser()
    assert get_username_from_user(user) == "TestUser"


def test_get_username_from_user_dict_username():
    """Test get_username_from_user with dict containing username."""
    user_dict = {"username": "testuser"}
    assert get_username_from_user(user_dict) == "testuser"


def test_get_username_from_user_dict_name():
    """Test get_username_from_user with dict containing name."""
    user_dict = {"name": "TestUser"}
    assert get_username_from_user(user_dict) == "TestUser"


def test_get_username_from_user_invalid():
    """Test get_username_from_user raises error with invalid user object."""
    with pytest.raises(MythosValidationError, match="username or name"):
        get_username_from_user({})


def test_get_username_from_user_empty_dict():
    """Test get_username_from_user raises error with empty dict."""
    with pytest.raises(MythosValidationError, match="username or name"):
        get_username_from_user({})


def test_get_username_from_user_none():
    """Test get_username_from_user raises error with None."""
    with pytest.raises(MythosValidationError, match="username or name"):
        get_username_from_user(None)


def test_get_username_from_user_priority_player_over_username():
    """Test get_username_from_user prioritizes player name over username."""
    class MockPlayer:
        def __init__(self):
            self.name = "TestPlayer"
            self.player_id = "123"
            self.username = "testuser"

    player = MockPlayer()
    # Should return name, not username, because it has player_id
    assert get_username_from_user(player) == "TestPlayer"
