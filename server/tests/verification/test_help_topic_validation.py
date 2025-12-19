"""
Tests for help topic validation functionality.

This module tests the validate_help_topic function to ensure proper
validation of help topic fields in command models.
"""

import pytest

from server.validators.security_validator import validate_help_topic


class TestHelpTopicValidation:
    """Test cases for help topic validation."""

    def test_validate_help_topic_valid_topics(self) -> None:
        """Test validation of valid help topics."""
        valid_topics = [
            "commands",
            "movement",
            "chat",
            "admin",
            "help",
            "whisper",
            "teleport",
            "mute",
            "alias",
            "emote",
            "pose",
            "status",
            "inventory",
            "quit",
            "logout",
            "look",
            "go",
            "say",
            "local",
            "system",
            "me",
            "who",
            "Test123",
            "test_topic",
            "test-topic",
            "a",
            "z",
        ]

        for topic in valid_topics:
            result = validate_help_topic(topic)
            assert result == topic, f"Valid topic '{topic}' should pass validation"

    def test_validate_help_topic_invalid_topics(self) -> None:
        """Test validation of invalid help topics."""
        # Test empty string separately as it returns empty string instead of raising error
        assert validate_help_topic("") == ""

        # Test invalid topics that should raise errors
        invalid_topics = [
            "123",  # Starts with number
            "test topic",  # Contains space
            "test@topic",  # Contains @
            "test#topic",  # Contains #
            "test$topic",  # Contains $
            "test%topic",  # Contains %
            "test^topic",  # Contains ^
            "test&topic",  # Contains &
            "test*topic",  # Contains *
            "test(topic",  # Contains (
            "test)topic",  # Contains )
            "test+topic",  # Contains +
            "test=topic",  # Contains =
            "test[topic",  # Contains [
            "test]topic",  # Contains ]
            "test{topic",  # Contains {
            "test}topic",  # Contains }
            "test|topic",  # Contains |
            "test\\topic",  # Contains backslash
            "test:topic",  # Contains :
            "test;topic",  # Contains ;
            'test"topic',  # Contains double quote
            "test'topic",  # Contains single quote
            "test,topic",  # Contains comma
            "test.topic",  # Contains dot
            "test<topic",  # Contains <
            "test>topic",  # Contains >
            "test?topic",  # Contains ?
            "test/topic",  # Contains /
            "test`topic",  # Contains backtick
            "test~topic",  # Contains ~
            "test!topic",  # Contains !
        ]

        for topic in invalid_topics:
            with pytest.raises(ValueError, match="Help topic must start with a letter"):
                validate_help_topic(topic)

    def test_validate_help_topic_none_input(self) -> None:
        """Test validation with None input."""
        result = validate_help_topic(None)  # type: ignore[arg-type]
        assert result is None

    def test_validate_help_topic_empty_string(self) -> None:
        """Test validation with empty string."""
        # Empty string returns empty string instead of raising error
        result = validate_help_topic("")
        assert result == ""

    def test_validate_help_topic_whitespace_only(self) -> None:
        """Test validation with whitespace-only string."""
        with pytest.raises(ValueError, match="Help topic must start with a letter"):
            validate_help_topic("   ")

    def test_validate_help_topic_case_sensitivity(self) -> None:
        """Test that validation is case-sensitive for the first character."""
        # Valid cases
        assert validate_help_topic("Commands") == "Commands"
        assert validate_help_topic("COMMANDS") == "COMMANDS"
        assert validate_help_topic("commands") == "commands"

        # Invalid cases
        with pytest.raises(ValueError):
            validate_help_topic("123commands")

    def test_validate_help_topic_special_characters_in_middle(self) -> None:
        """Test that special characters are not allowed anywhere in the topic."""
        invalid_topics = [
            "test@topic",
            "test#topic",
            "test$topic",
            "test%topic",
            "test^topic",
            "test&topic",
            "test*topic",
            "test(topic",
            "test)topic",
            "test+topic",
            "test=topic",
            "test[topic",
            "test]topic",
            "test{topic",
            "test}topic",
            "test|topic",
            "test\\topic",
            "test:topic",
            "test;topic",
            'test"topic',
            "test'topic",
            "test,topic",
            "test.topic",
            "test<topic",
            "test>topic",
            "test?topic",
            "test/topic",
            "test`topic",
            "test~topic",
            "test!topic",
        ]

        for topic in invalid_topics:
            with pytest.raises(ValueError, match="Help topic must start with a letter"):
                validate_help_topic(topic)

    def test_validate_help_topic_edge_cases(self) -> None:
        """Test edge cases for help topic validation."""
        # Single character
        assert validate_help_topic("a") == "a"
        assert validate_help_topic("Z") == "Z"

        # Long valid topic
        long_topic = "a" + "b" * 49  # 50 characters total
        assert validate_help_topic(long_topic) == long_topic

        # Topic with numbers and underscores
        assert validate_help_topic("test123") == "test123"
        assert validate_help_topic("test_topic") == "test_topic"
        assert validate_help_topic("test-topic") == "test-topic"

    def test_validate_help_topic_error_message_format(self) -> None:
        """Test that error messages are properly formatted."""
        with pytest.raises(ValueError) as exc_info:
            validate_help_topic("123invalid")

        error_message = str(exc_info.value)
        assert "Help topic must start with a letter" in error_message
        assert "contain only letters, numbers, underscores, and hyphens" in error_message
