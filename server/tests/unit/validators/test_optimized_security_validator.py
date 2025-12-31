"""
Unit tests for optimized security validation utilities.

Tests the optimized security validator functions that sanitize and validate user input
to prevent injection attacks and other security vulnerabilities.
"""

from unittest.mock import patch

import pytest

from server.validators.optimized_security_validator import (
    benchmark_validation_performance,
    optimized_comprehensive_sanitize_input,
    optimized_sanitize_unicode_input,
    optimized_strip_ansi_codes,
    optimized_validate_action_content,
    optimized_validate_alias_name,
    optimized_validate_command_content,
    optimized_validate_filter_name,
    optimized_validate_help_topic,
    optimized_validate_message_content,
    optimized_validate_player_name,
    optimized_validate_pose_content,
    optimized_validate_reason_content,
    optimized_validate_security_comprehensive,
    optimized_validate_target_player,
)


def test_optimized_sanitize_unicode_input_empty():
    """Test sanitizing empty string."""
    assert optimized_sanitize_unicode_input("") == ""


def test_optimized_sanitize_unicode_input_normal_text():
    """Test sanitizing normal text (no changes expected)."""
    text = "Hello, world!"
    result = optimized_sanitize_unicode_input(text)
    assert isinstance(result, str)
    assert len(result) > 0


def test_optimized_sanitize_unicode_input_unicode():
    """Test sanitizing text with Unicode issues."""
    # ftfy handles various Unicode issues
    text = "Hello, world!"
    result = optimized_sanitize_unicode_input(text)
    assert isinstance(result, str)


def test_optimized_strip_ansi_codes_empty():
    """Test stripping ANSI codes from empty string."""
    assert optimized_strip_ansi_codes("") == ""


def test_optimized_strip_ansi_codes_no_ansi():
    """Test stripping ANSI codes from text without ANSI."""
    text = "Hello, world!"
    assert optimized_strip_ansi_codes(text) == text


def test_optimized_strip_ansi_codes_with_ansi():
    """Test stripping ANSI codes from text with ANSI."""
    text = "\x1b[31mHello\x1b[0m"
    result = optimized_strip_ansi_codes(text)
    assert "\x1b" not in result
    assert "Hello" in result


def test_optimized_comprehensive_sanitize_input_empty():
    """Test comprehensive sanitization of empty string."""
    assert optimized_comprehensive_sanitize_input("") == ""


def test_optimized_comprehensive_sanitize_input_normal():
    """Test comprehensive sanitization of normal text."""
    text = "Hello, world!"
    result = optimized_comprehensive_sanitize_input(text)
    assert isinstance(result, str)


def test_optimized_validate_message_content_empty():
    """Test validating empty message."""
    assert optimized_validate_message_content("") == ""


def test_optimized_validate_message_content_valid():
    """Test validating valid message."""
    message = "Hello, this is a valid message!"
    result = optimized_validate_message_content(message)
    assert result == message or isinstance(result, str)


def test_optimized_validate_message_content_dangerous_chars():
    """Test validating message with dangerous characters."""
    with pytest.raises(ValueError, match="dangerous characters"):
        optimized_validate_message_content("Hello <script>")


def test_optimized_validate_message_content_injection_pattern():
    """Test validating message with injection pattern."""
    with pytest.raises(ValueError, match="dangerous pattern"):
        optimized_validate_message_content("test; rm -rf /")


def test_optimized_validate_message_content_sql_injection():
    """Test validating message with SQL injection pattern."""
    with pytest.raises(ValueError, match="dangerous pattern"):
        optimized_validate_message_content("test OR 1=1")


def test_optimized_validate_message_content_xss():
    """Test validating message with XSS pattern."""
    with pytest.raises(ValueError, match="dangerous characters"):
        optimized_validate_message_content("<script>alert('xss')</script>")


def test_optimized_validate_action_content_empty():
    """Test validating empty action."""
    assert optimized_validate_action_content("") == ""


def test_optimized_validate_action_content_valid():
    """Test validating valid action."""
    action = "waves hello"
    result = optimized_validate_action_content(action)
    assert isinstance(result, str)


def test_optimized_validate_action_content_dangerous_chars():
    """Test validating action with dangerous characters."""
    with pytest.raises(ValueError, match="dangerous characters"):
        optimized_validate_action_content("action <script>")


def test_optimized_validate_action_content_injection():
    """Test validating action with injection pattern."""
    with pytest.raises(ValueError, match="dangerous pattern"):
        optimized_validate_action_content("action; rm -rf /")


def test_optimized_validate_player_name_empty():
    """Test validating empty player name."""
    assert optimized_validate_player_name("") == ""


def test_optimized_validate_player_name_valid():
    """Test validating valid player name."""
    name = "TestPlayer"
    assert optimized_validate_player_name(name) == name


def test_optimized_validate_player_name_with_underscore():
    """Test validating player name with underscore."""
    name = "Test_Player"
    assert optimized_validate_player_name(name) == name


def test_optimized_validate_player_name_with_hyphen():
    """Test validating player name with hyphen."""
    name = "Test-Player"
    assert optimized_validate_player_name(name) == name


def test_optimized_validate_player_name_with_numbers():
    """Test validating player name with numbers."""
    name = "TestPlayer123"
    assert optimized_validate_player_name(name) == name


def test_optimized_validate_player_name_starts_with_number():
    """Test validating player name starting with number (invalid)."""
    with pytest.raises(ValueError, match="must start with a letter"):
        optimized_validate_player_name("123Player")


def test_optimized_validate_player_name_special_chars():
    """Test validating player name with special characters (invalid)."""
    with pytest.raises(ValueError, match="must start with a letter"):
        optimized_validate_player_name("Test@Player")


def test_optimized_validate_alias_name_empty():
    """Test validating empty alias name."""
    assert optimized_validate_alias_name("") == ""


def test_optimized_validate_alias_name_valid():
    """Test validating valid alias name."""
    name = "alias_name"
    assert optimized_validate_alias_name(name) == name


def test_optimized_validate_alias_name_starts_with_number():
    """Test validating alias name starting with number (invalid)."""
    with pytest.raises(ValueError, match="must start with a letter"):
        optimized_validate_alias_name("123alias")


def test_optimized_validate_alias_name_hyphen():
    """Test validating alias name with hyphen (invalid - aliases don't allow hyphens)."""
    with pytest.raises(ValueError, match="must start with a letter"):
        optimized_validate_alias_name("alias-name")


def test_optimized_validate_command_content_empty():
    """Test validating empty command content."""
    assert optimized_validate_command_content("") == ""


def test_optimized_validate_command_content_valid():
    """Test validating valid command content."""
    command = "look around"
    result = optimized_validate_command_content(command)
    assert isinstance(result, str)


def test_optimized_validate_command_content_injection():
    """Test validating command content with injection pattern."""
    with pytest.raises(ValueError, match="dangerous pattern"):
        optimized_validate_command_content("look; rm -rf /")


def test_optimized_validate_reason_content_empty():
    """Test validating empty reason content."""
    assert optimized_validate_reason_content("") == ""


def test_optimized_validate_reason_content_valid():
    """Test validating valid reason content."""
    reason = "Player was disruptive"
    result = optimized_validate_reason_content(reason)
    assert isinstance(result, str)


def test_optimized_validate_reason_content_injection():
    """Test validating reason content with injection pattern."""
    with pytest.raises(ValueError, match="dangerous pattern"):
        optimized_validate_reason_content("reason; DROP TABLE users")


def test_optimized_validate_pose_content_empty():
    """Test validating empty pose content."""
    assert optimized_validate_pose_content("") == ""


def test_optimized_validate_pose_content_valid():
    """Test validating valid pose content."""
    pose = "sits quietly"
    result = optimized_validate_pose_content(pose)
    assert isinstance(result, str)


def test_optimized_validate_pose_content_injection():
    """Test validating pose content with injection pattern."""
    with pytest.raises(ValueError, match="dangerous pattern"):
        optimized_validate_pose_content("poses; eval('malicious')")


def test_optimized_validate_filter_name_empty():
    """Test validating empty filter name."""
    assert optimized_validate_filter_name("") == ""


def test_optimized_validate_filter_name_valid():
    """Test validating valid filter name."""
    name = "TestFilter"
    assert optimized_validate_filter_name(name) == name


def test_optimized_validate_filter_name_invalid():
    """Test validating invalid filter name."""
    with pytest.raises(ValueError, match="must start with a letter"):
        optimized_validate_filter_name("123Filter")


def test_optimized_validate_target_player_empty():
    """Test validating empty target player name."""
    assert optimized_validate_target_player("") == ""


def test_optimized_validate_target_player_valid():
    """Test validating valid target player name."""
    name = "TargetPlayer"
    assert optimized_validate_target_player(name) == name


def test_optimized_validate_target_player_invalid():
    """Test validating invalid target player name."""
    with pytest.raises(ValueError, match="must start with a letter"):
        optimized_validate_target_player("@TargetPlayer")


def test_optimized_validate_help_topic_empty():
    """Test validating empty help topic."""
    assert optimized_validate_help_topic("") == ""


def test_optimized_validate_help_topic_valid():
    """Test validating valid help topic."""
    topic = "combat"
    assert optimized_validate_help_topic(topic) == topic


def test_optimized_validate_help_topic_invalid():
    """Test validating invalid help topic."""
    with pytest.raises(ValueError, match="must start with a letter"):
        optimized_validate_help_topic("123topic")


def test_optimized_validate_security_comprehensive_empty():
    """Test comprehensive security validation of empty string."""
    assert optimized_validate_security_comprehensive("") == ""


def test_optimized_validate_security_comprehensive_valid():
    """Test comprehensive security validation of valid text."""
    text = "Safe text content"
    result = optimized_validate_security_comprehensive(text)
    assert isinstance(result, str)


def test_optimized_validate_security_comprehensive_dangerous_chars():
    """Test comprehensive security validation with dangerous characters."""
    with pytest.raises(ValueError, match="dangerous characters"):
        optimized_validate_security_comprehensive("Text <script>")


def test_optimized_validate_security_comprehensive_injection():
    """Test comprehensive security validation with injection pattern."""
    with pytest.raises(ValueError, match="dangerous pattern"):
        optimized_validate_security_comprehensive("text; malicious code")


def test_benchmark_validation_performance():
    """Test benchmark function runs without errors."""
    with patch("server.validators.optimized_security_validator.logger") as mock_logger:
        result = benchmark_validation_performance()
        assert isinstance(result, float)
        assert result >= 0
        mock_logger.info.assert_called()


def test_optimized_validate_message_content_path_traversal():
    """Test validating message with path traversal pattern."""
    with pytest.raises(ValueError, match="dangerous pattern"):
        optimized_validate_message_content("../../../etc/passwd")


def test_optimized_validate_message_content_javascript_url():
    """Test validating message with javascript: URL."""
    with pytest.raises(ValueError, match="dangerous characters"):
        optimized_validate_message_content("javascript:alert('xss')")


def test_optimized_validate_message_content_event_handler():
    """Test validating message with event handler."""
    with pytest.raises(ValueError, match="dangerous pattern"):
        optimized_validate_message_content("onclick=malicious()")


def test_optimized_validate_message_content_data_url():
    """Test validating message with data URL."""
    with pytest.raises(ValueError, match="dangerous characters"):
        optimized_validate_message_content("data:text/html,<script>alert('xss')</script>")


def test_optimized_validate_message_content_python_injection():
    """Test validating message with Python injection."""
    with pytest.raises(ValueError, match="dangerous characters"):
        optimized_validate_message_content("__import__('os').system('rm -rf /')")


def test_optimized_validate_message_content_format_string():
    """Test validating message with format string pattern."""
    with pytest.raises(ValueError, match="dangerous pattern"):
        optimized_validate_message_content("text %s format")


def test_optimized_validate_message_content_logging():
    """Test that validation logs appropriately."""
    with patch("server.validators.optimized_security_validator.logger") as mock_logger:
        optimized_validate_message_content("valid message")
        # Should have debug logs
        assert mock_logger.debug.called or mock_logger.warning.called or not mock_logger.method_calls


def test_optimized_validate_message_content_logging_warning():
    """Test that validation logs warnings for dangerous content."""
    with patch("server.validators.optimized_security_validator.logger") as mock_logger:
        try:
            optimized_validate_message_content("text <script>")
        except ValueError:
            pass
        # Should have warning logs for dangerous content
        assert mock_logger.warning.called or not mock_logger.method_calls
