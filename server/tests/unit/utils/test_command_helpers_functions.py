"""
Unit tests for command_helpers utility functions.

Tests the utility functions in command_helpers.py module.
"""

from unittest.mock import MagicMock

from server.utils.command_helpers import get_username_from_user, validate_command_safety


def test_validate_command_safety_safe():
    """Test validate_command_safety() returns True for safe commands."""
    assert validate_command_safety("look north") is True
    assert validate_command_safety("say hello") is True
    assert validate_command_safety("go east") is True


def test_validate_command_safety_shell_metacharacters():
    """Test validate_command_safety() returns False for shell metacharacters."""
    assert validate_command_safety("look; rm -rf") is False
    assert validate_command_safety("say | cat") is False
    assert validate_command_safety("go &") is False


def test_validate_command_safety_sql_injection():
    """Test validate_command_safety() returns False for SQL injection attempts."""
    assert validate_command_safety("look and = 1") is False
    assert validate_command_safety("say or = true") is False


def test_validate_command_safety_python_injection():
    """Test validate_command_safety() returns False for Python injection attempts."""
    assert validate_command_safety("look __import__('os')") is False
    assert validate_command_safety("say eval('code')") is False
    assert validate_command_safety("go exec('code')") is False


def test_validate_command_safety_format_string():
    """Test validate_command_safety() returns False for format string injection."""
    assert validate_command_safety("look %s") is False
    assert validate_command_safety("say %d") is False


def test_validate_command_safety_xss():
    """Test validate_command_safety() returns False for XSS attempts."""
    assert validate_command_safety("look <script>") is False
    assert validate_command_safety("say javascript:") is False


def test_get_username_from_user_with_name():
    """Test get_username_from_user() returns name when available."""
    user_obj = MagicMock()
    user_obj.name = "TestPlayer"
    user_obj.player_id = "player_123"

    result = get_username_from_user(user_obj)

    assert result == "TestPlayer"


def test_get_username_from_user_with_username():
    """Test get_username_from_user() returns username when available."""
    user_obj = MagicMock()
    del user_obj.name
    user_obj.username = "TestUser"

    result = get_username_from_user(user_obj)

    assert result == "TestUser"


def test_get_username_from_user_dict():
    """Test get_username_from_user() returns username from dict."""
    user_obj = {"username": "TestUser"}

    result = get_username_from_user(user_obj)

    assert result == "TestUser"
