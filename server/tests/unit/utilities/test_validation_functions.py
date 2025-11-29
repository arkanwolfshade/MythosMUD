"""
Tests for centralized validation functions.

This module tests the new centralized validation functions that will replace
the duplicated validation logic across command models.

As noted in the Pnakotic Manuscripts: "Consistency in validation is the key
to maintaining the integrity of our digital realm against the chaos of the outer darkness."
"""

import pytest

from server.validators.security_validator import (
    check_dangerous_characters,
    check_injection_patterns,
    get_dangerous_characters,
    get_injection_patterns,
    validate_action_content,
    validate_alias_name,
    validate_command_content,
    validate_filter_name,
    validate_message_content,
    validate_player_name,
    validate_pose_content,
    validate_reason_content,
    validate_security_comprehensive,
    validate_target_player,
)


class TestMessageContentValidation:
    """Test centralized message content validation."""

    def test_validate_message_content_valid(self):
        """Test validation with valid message content."""
        valid_messages = [
            "Hello, world!",
            "How are you today?",
            "I love this game!",
            "Can you help me?",
            "Thank you very much.",
            "The weather is nice today.",
        ]

        for message in valid_messages:
            result = validate_message_content(message)
            assert result == message

    def test_validate_message_content_empty(self):
        """Test validation with empty message."""
        result = validate_message_content("")
        assert result == ""

        result = validate_message_content(None)
        assert result is None

    def test_validate_message_content_dangerous_characters(self):
        """Test validation with dangerous characters (only HTML tags now blocked)."""
        dangerous_messages = [
            "Hello<script>alert('xss')</script>",  # HTML tags still blocked
            "Hello<div>content</div>",  # HTML tags still blocked
            "Test <tag> content",  # HTML-like tags still blocked
        ]

        for message in dangerous_messages:
            with pytest.raises(ValueError, match="Message contains"):
                validate_message_content(message)

    def test_validate_message_content_injection_patterns(self):
        """Test validation with injection patterns (still blocks actual code execution)."""
        injection_messages = [
            "Hello; rm -rf /",  # Semicolon still blocked
            "Hello | malicious_command",  # Pipe still blocked
            "Hello OR 1=1",  # OR with = assignment blocked
            "Hello AND password='admin'",  # AND with = assignment blocked
            "Hello __import__('os')",  # Python import function call blocked
            "Hello eval('malicious')",  # Python eval function call blocked
            "Hello os.system('rm')",  # OS system call blocked
        ]

        for message in injection_messages:
            with pytest.raises(ValueError, match="Message contains"):
                validate_message_content(message)


class TestActionContentValidation:
    """Test centralized action content validation."""

    def test_validate_action_content_valid(self):
        """Test validation with valid action content."""
        valid_actions = [
            "waves hello",
            "smiles warmly",
            "nods in agreement",
            "looks around curiously",
            "stretches and yawns",
        ]

        for action in valid_actions:
            result = validate_action_content(action)
            assert result == action

    def test_validate_action_content_dangerous_characters(self):
        """Test validation with dangerous characters in actions (only HTML tags now)."""
        dangerous_actions = [
            "looks <script>alert('xss')</script>",  # HTML tags still blocked
            "waves <div>content</div>",  # HTML tags still blocked
        ]

        for action in dangerous_actions:
            with pytest.raises(ValueError, match="Action contains dangerous characters"):
                validate_action_content(action)

    def test_validate_action_content_injection_patterns(self):
        """Test validation with injection patterns in actions (semicolon and pipe blocked)."""
        injection_actions = [
            "waves; rm -rf /",  # Semicolon blocked
            "smiles | cat /etc/passwd",  # Pipe blocked
            # Note: & is no longer blocked
        ]

        for action in injection_actions:
            with pytest.raises(ValueError, match="Action contains"):
                validate_action_content(action)


class TestPlayerNameValidation:
    """Test centralized player name validation."""

    def test_validate_player_name_valid(self):
        """Test validation with valid player names."""
        valid_names = [
            "Alice",
            "Bob123",
            "Charlie_Test",
            "Diana-Player",
            "Eve_123-Player",
            "Frank",
        ]

        for name in valid_names:
            result = validate_player_name(name)
            assert result == name

    def test_validate_player_name_invalid_format(self):
        """Test validation with invalid player name formats."""
        invalid_names = [
            "123Alice",  # Starts with number
            "Alice Bob",  # Contains space
            "Alice@Bob",  # Contains special character
            "Alice.Bob",  # Contains dot
            "Alice#Bob",  # Contains hash
        ]

        for name in invalid_names:
            with pytest.raises(ValueError, match="Player name must start with a letter"):
                validate_player_name(name)

        # Test empty string separately (should return empty string, not raise error)
        result = validate_player_name("")
        assert result == ""

    def test_validate_player_name_edge_cases(self):
        """Test validation with edge cases."""
        # Single letter should be valid
        result = validate_player_name("A")
        assert result == "A"

        # Very long name should be valid
        long_name = "A" + "1" * 100
        result = validate_player_name(long_name)
        assert result == long_name


class TestAliasNameValidation:
    """Test centralized alias name validation."""

    def test_validate_alias_name_valid(self):
        """Test validation with valid alias names."""
        valid_aliases = [
            "look",
            "go",
            "say",
            "alias123",
            "my_alias",
            "test_alias_123",
        ]

        for alias in valid_aliases:
            result = validate_alias_name(alias)
            assert result == alias

    def test_validate_alias_name_invalid_format(self):
        """Test validation with invalid alias name formats."""
        invalid_aliases = [
            "123alias",  # Starts with number
            "alias name",  # Contains space
            "alias-name",  # Contains hyphen
            "alias@name",  # Contains special character
            "alias.name",  # Contains dot
        ]

        for alias in invalid_aliases:
            with pytest.raises(ValueError, match="Alias name must start with a letter"):
                validate_alias_name(alias)


class TestCommandContentValidation:
    """Test centralized command content validation."""

    def test_validate_command_content_valid(self):
        """Test validation with valid command content."""
        valid_commands = [
            "look north",
            "go south",
            "say hello world",
            "emote waves",
            "who",
            "help",
        ]

        for command in valid_commands:
            result = validate_command_content(command)
            assert result == command

    def test_validate_command_content_injection_patterns(self):
        """Test validation with injection patterns in commands (semicolon, pipe, function calls blocked)."""
        injection_commands = [
            "look; rm -rf /",  # Semicolon blocked
            "go | malicious",  # Pipe blocked
            "who __import__('os')",  # Python import function call blocked
            "emote eval('code')",  # Python eval function call blocked
            "say os.system('rm')",  # OS system call blocked
        ]

        for command in injection_commands:
            with pytest.raises(ValueError, match="Command contains potentially dangerous pattern"):
                validate_command_content(command)


class TestReasonContentValidation:
    """Test centralized reason content validation."""

    def test_validate_reason_content_valid(self):
        """Test validation with valid reason content."""
        valid_reasons = [
            "Spam",
            "Inappropriate behavior",
            "Harassment",
            "Breaking rules",
            "Temporary mute",
        ]

        for reason in valid_reasons:
            result = validate_reason_content(reason)
            assert result == reason

    def test_validate_reason_content_dangerous_characters(self):
        """Test validation with dangerous characters in reasons (only HTML tags now)."""
        dangerous_reasons = [
            "Spam<script>alert('xss')</script>",  # HTML tags still blocked
            "Bad<div>behavior</div>",  # HTML tags still blocked
        ]

        for reason in dangerous_reasons:
            with pytest.raises(ValueError, match="Reason contains dangerous characters"):
                validate_reason_content(reason)


class TestPoseContentValidation:
    """Test centralized pose content validation."""

    def test_validate_pose_content_valid(self):
        """Test validation with valid pose content."""
        valid_poses = [
            "sits quietly",
            "stands tall",
            "leans against the wall",
            "looks thoughtful",
            "smiles warmly",
        ]

        for pose in valid_poses:
            result = validate_pose_content(pose)
            assert result == pose

    def test_validate_pose_content_dangerous_characters(self):
        """Test validation with dangerous characters in poses (only HTML tags now)."""
        dangerous_poses = [
            "sits<script>alert('xss')</script>",  # HTML tags still blocked
            "stands<div>content</div>",  # HTML tags still blocked
        ]

        for pose in dangerous_poses:
            with pytest.raises(ValueError, match="Pose contains dangerous characters"):
                validate_pose_content(pose)


class TestFilterNameValidation:
    """Test centralized filter name validation."""

    def test_validate_filter_name_valid(self):
        """Test validation with valid filter names."""
        valid_filters = [
            "Alice",
            "Bob123",
            "Charlie_Test",
            "Diana-Player",
            "Eve_123-Player",
        ]

        for filter_name in valid_filters:
            result = validate_filter_name(filter_name)
            assert result == filter_name

    def test_validate_filter_name_invalid_format(self):
        """Test validation with invalid filter name formats."""
        invalid_filters = [
            "123Alice",  # Starts with number
            "Alice Bob",  # Contains space
            "Alice@Bob",  # Contains special character
        ]

        for filter_name in invalid_filters:
            with pytest.raises(ValueError, match="Filter name must start with a letter"):
                validate_filter_name(filter_name)


class TestTargetPlayerValidation:
    """Test centralized target player validation."""

    def test_validate_target_player_valid(self):
        """Test validation with valid target player names."""
        valid_targets = [
            "Alice",
            "Bob123",
            "Charlie_Test",
            "Diana-Player",
        ]

        for target in valid_targets:
            result = validate_target_player(target)
            assert result == target

    def test_validate_target_player_invalid_format(self):
        """Test validation with invalid target player name formats."""
        invalid_targets = [
            "123Alice",  # Starts with number
            "Alice Bob",  # Contains space
            "Alice@Bob",  # Contains special character
        ]

        for target in invalid_targets:
            with pytest.raises(ValueError, match="Target player name must start with a letter"):
                validate_target_player(target)


class TestComprehensiveValidation:
    """Test comprehensive security validation."""

    def test_validate_security_comprehensive_message_type(self):
        """Test comprehensive validation with message field type."""
        result = validate_security_comprehensive("Hello, world!", "message")
        assert result == "Hello, world!"

        with pytest.raises(ValueError):
            validate_security_comprehensive("Hello<script>alert('xss')</script>", "message")

    def test_validate_security_comprehensive_action_type(self):
        """Test comprehensive validation with action field type."""
        result = validate_security_comprehensive("waves hello", "action")
        assert result == "waves hello"

        with pytest.raises(ValueError):
            validate_security_comprehensive("waves; rm -rf /", "action")

    def test_validate_security_comprehensive_player_name_type(self):
        """Test comprehensive validation with player_name field type."""
        result = validate_security_comprehensive("Alice", "player_name")
        assert result == "Alice"

        with pytest.raises(ValueError):
            validate_security_comprehensive("123Alice", "player_name")

    def test_validate_security_comprehensive_unknown_type(self):
        """Test comprehensive validation with unknown field type defaults to message."""
        result = validate_security_comprehensive("Hello, world!", "unknown_type")
        assert result == "Hello, world!"

        with pytest.raises(ValueError):
            validate_security_comprehensive("Hello<script>alert('xss')</script>", "unknown_type")

    def test_validate_security_comprehensive_empty_input(self):
        """Test comprehensive validation with empty input."""
        result = validate_security_comprehensive("", "message")
        assert result == ""

        result = validate_security_comprehensive(None, "message")
        assert result is None


class TestUtilityFunctions:
    """Test utility functions for centralized validation."""

    def test_get_dangerous_characters(self):
        """Test getting dangerous characters list (only HTML tags now)."""
        dangerous_chars = get_dangerous_characters()
        assert isinstance(dangerous_chars, list)
        assert len(dangerous_chars) == 2  # Only < and > now
        assert "<" in dangerous_chars
        assert ">" in dangerous_chars
        # & is no longer considered dangerous
        assert "&" not in dangerous_chars

    def test_get_injection_patterns(self):
        """Test getting injection patterns list."""
        patterns = get_injection_patterns()
        assert isinstance(patterns, list)
        assert len(patterns) > 0
        # Should be a copy, not the original
        assert patterns is not get_injection_patterns()

    def test_check_dangerous_characters(self):
        """Test checking for dangerous characters."""
        has_dangerous, found_chars = check_dangerous_characters("Hello, world!")
        assert not has_dangerous
        assert found_chars == []

        has_dangerous, found_chars = check_dangerous_characters("Hello<script>alert('xss')</script>")
        assert has_dangerous
        assert "<" in found_chars
        assert ">" in found_chars

    def test_check_injection_patterns(self):
        """Test checking for injection patterns."""
        has_patterns, matched_patterns = check_injection_patterns("Hello, world!")
        assert not has_patterns
        assert matched_patterns == []

        has_patterns, matched_patterns = check_injection_patterns("Hello; rm -rf /")
        assert has_patterns
        assert len(matched_patterns) > 0

    def test_check_functions_with_empty_input(self):
        """Test utility functions with empty input."""
        has_dangerous, found_chars = check_dangerous_characters("")
        assert not has_dangerous
        assert found_chars == []

        has_dangerous, found_chars = check_dangerous_characters(None)
        assert not has_dangerous
        assert found_chars == []

        has_patterns, matched_patterns = check_injection_patterns("")
        assert not has_patterns
        assert matched_patterns == []

        has_patterns, matched_patterns = check_injection_patterns(None)
        assert not has_patterns
        assert matched_patterns == []


class TestValidationConsistency:
    """Test consistency of validation functions."""

    def test_validation_consistency_across_functions(self):
        """Test that validation functions are consistent."""
        test_input = "Hello<script>alert('xss')</script>"

        # All message-type validations should behave the same
        with pytest.raises(ValueError, match="contains dangerous characters"):
            validate_message_content(test_input)

        with pytest.raises(ValueError, match="contains dangerous characters"):
            validate_reason_content(test_input)

        with pytest.raises(ValueError, match="contains dangerous characters"):
            validate_pose_content(test_input)

    def test_validation_consistency_with_comprehensive(self):
        """Test that comprehensive validation is consistent with individual functions."""
        test_cases = [
            ("Hello, world!", "message"),
            ("waves hello", "action"),
            ("Alice", "player_name"),
            ("my_alias", "alias_name"),
            ("look north", "command"),
            ("Spam", "reason"),
            ("sits quietly", "pose"),
            ("Alice", "filter_name"),
            ("Bob", "target"),
        ]

        for test_input, field_type in test_cases:
            # Comprehensive validation should match individual validation
            if field_type == "message":
                individual_result = validate_message_content(test_input)
            elif field_type == "action":
                individual_result = validate_action_content(test_input)
            elif field_type == "player_name":
                individual_result = validate_player_name(test_input)
            elif field_type == "alias_name":
                individual_result = validate_alias_name(test_input)
            elif field_type == "command":
                individual_result = validate_command_content(test_input)
            elif field_type == "reason":
                individual_result = validate_reason_content(test_input)
            elif field_type == "pose":
                individual_result = validate_pose_content(test_input)
            elif field_type == "filter_name":
                individual_result = validate_filter_name(test_input)
            elif field_type == "target":
                individual_result = validate_target_player(test_input)

            comprehensive_result = validate_security_comprehensive(test_input, field_type)
            assert individual_result == comprehensive_result

    def test_validation_performance(self):
        """Test validation performance."""
        import time

        test_input = "Hello, world! " * 100

        start_time = time.time()
        for _ in range(1000):
            validate_message_content(test_input)
        end_time = time.time()

        # Should complete quickly (under 1.5 seconds for 1000 iterations)
        # Increased threshold to account for system load and timing variations
        assert end_time - start_time < 1.5
