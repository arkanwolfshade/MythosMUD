"""
Tests for optimized security validation functions.

This module tests the performance-optimized versions of security validation
functions with compiled regex patterns and caching.
"""

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


class TestOptimizedSanitizeUnicodeInput:
    """Test optimized Unicode sanitization."""

    def test_optimized_sanitize_unicode_input_empty(self):
        """Test optimized_sanitize_unicode_input with empty input."""
        assert optimized_sanitize_unicode_input("") == ""
        assert optimized_sanitize_unicode_input(None) is None

    def test_optimized_sanitize_unicode_input_valid(self):
        """Test optimized_sanitize_unicode_input with valid Unicode."""
        text = "café naïve résumé"
        result = optimized_sanitize_unicode_input(text)
        assert isinstance(result, str)
        assert len(result) > 0

    def test_optimized_sanitize_unicode_input_caching(self):
        """Test that optimized_sanitize_unicode_input uses caching."""
        text = "test caching"
        result1 = optimized_sanitize_unicode_input(text)
        result2 = optimized_sanitize_unicode_input(text)
        assert result1 == result2


class TestOptimizedStripAnsiCodes:
    """Test optimized ANSI code removal."""

    def test_optimized_strip_ansi_codes_empty(self):
        """Test optimized_strip_ansi_codes with empty input."""
        assert optimized_strip_ansi_codes("") == ""
        assert optimized_strip_ansi_codes(None) is None

    def test_optimized_strip_ansi_codes_basic(self):
        """Test optimized_strip_ansi_codes removes basic ANSI codes."""
        ansi_text = "\033[31mRed text\033[0m"
        result = optimized_strip_ansi_codes(ansi_text)
        assert result == "Red text"

    def test_optimized_strip_ansi_codes_complex(self):
        """Test optimized_strip_ansi_codes removes complex ANSI sequences."""
        ansi_text = "\033[1;33;44mBold yellow on blue\033[0m"
        result = optimized_strip_ansi_codes(ansi_text)
        assert result == "Bold yellow on blue"

    def test_optimized_strip_ansi_codes_caching(self):
        """Test that optimized_strip_ansi_codes uses caching."""
        text = "\033[31mtest\033[0m"
        result1 = optimized_strip_ansi_codes(text)
        result2 = optimized_strip_ansi_codes(text)
        assert result1 == result2


class TestOptimizedComprehensiveSanitizeInput:
    """Test optimized comprehensive sanitization."""

    def test_optimized_comprehensive_sanitize_input_empty(self):
        """Test optimized_comprehensive_sanitize_input with empty input."""
        assert optimized_comprehensive_sanitize_input("") == ""
        assert optimized_comprehensive_sanitize_input(None) is None

    def test_optimized_comprehensive_sanitize_input_unicode_and_ansi(self):
        """Test optimized_comprehensive_sanitize_input handles Unicode and ANSI."""
        text = "\033[31mcafé\033[0m"
        result = optimized_comprehensive_sanitize_input(text)
        assert "\033" not in result
        assert isinstance(result, str)


class TestOptimizedValidateMessageContent:
    """Test optimized message content validation."""

    def test_optimized_validate_message_content_valid(self):
        """Test optimized_validate_message_content with valid message."""
        result = optimized_validate_message_content("Hello, world!")
        assert result == "Hello, world!"

    def test_optimized_validate_message_content_empty(self):
        """Test optimized_validate_message_content with empty message."""
        assert optimized_validate_message_content("") == ""
        assert optimized_validate_message_content(None) is None

    def test_optimized_validate_message_content_dangerous_chars(self):
        """Test optimized_validate_message_content rejects dangerous characters."""
        with pytest.raises(ValueError, match="dangerous characters"):
            optimized_validate_message_content("Hello<script>alert('xss')</script>")

    def test_optimized_validate_message_content_injection_patterns(self):
        """Test optimized_validate_message_content rejects injection patterns."""
        with pytest.raises(ValueError, match="dangerous pattern"):
            optimized_validate_message_content("Hello; rm -rf /")

    def test_optimized_validate_message_content_sanitizes_input(self):
        """Test optimized_validate_message_content sanitizes input."""
        text = "\033[31mHello\033[0m"
        result = optimized_validate_message_content(text)
        assert "\033" not in result


class TestOptimizedValidateActionContent:
    """Test optimized action content validation."""

    def test_optimized_validate_action_content_valid(self):
        """Test optimized_validate_action_content with valid action."""
        result = optimized_validate_action_content("waves hello")
        assert result == "waves hello"

    def test_optimized_validate_action_content_empty(self):
        """Test optimized_validate_action_content with empty action."""
        assert optimized_validate_action_content("") == ""
        assert optimized_validate_action_content(None) is None

    def test_optimized_validate_action_content_dangerous_chars(self):
        """Test optimized_validate_action_content rejects dangerous characters."""
        with pytest.raises(ValueError, match="dangerous characters"):
            optimized_validate_action_content("waves<script>alert('xss')</script>")

    def test_optimized_validate_action_content_injection_patterns(self):
        """Test optimized_validate_action_content rejects injection patterns."""
        with pytest.raises(ValueError, match="dangerous pattern"):
            optimized_validate_action_content("waves; rm -rf /")


class TestOptimizedValidatePlayerName:
    """Test optimized player name validation."""

    def test_optimized_validate_player_name_valid(self):
        """Test optimized_validate_player_name with valid names."""
        valid_names = ["Alice", "Bob123", "Charlie_Test", "Diana-Player"]
        for name in valid_names:
            result = optimized_validate_player_name(name)
            assert result == name

    def test_optimized_validate_player_name_empty(self):
        """Test optimized_validate_player_name with empty name."""
        assert optimized_validate_player_name("") == ""
        assert optimized_validate_player_name(None) is None

    def test_optimized_validate_player_name_invalid_format(self):
        """Test optimized_validate_player_name rejects invalid formats."""
        invalid_names = ["123Alice", "Alice Bob", "Alice@Bob"]
        for name in invalid_names:
            with pytest.raises(ValueError, match="Player name must start"):
                optimized_validate_player_name(name)


class TestOptimizedValidateAliasName:
    """Test optimized alias name validation."""

    def test_optimized_validate_alias_name_valid(self):
        """Test optimized_validate_alias_name with valid aliases."""
        valid_aliases = ["look", "go", "say", "alias123", "my_alias"]
        for alias in valid_aliases:
            result = optimized_validate_alias_name(alias)
            assert result == alias

    def test_optimized_validate_alias_name_empty(self):
        """Test optimized_validate_alias_name with empty alias."""
        assert optimized_validate_alias_name("") == ""
        assert optimized_validate_alias_name(None) is None

    def test_optimized_validate_alias_name_invalid_format(self):
        """Test optimized_validate_alias_name rejects invalid formats."""
        invalid_aliases = ["123alias", "alias name", "alias-name"]
        for alias in invalid_aliases:
            with pytest.raises(ValueError, match="Alias name must start"):
                optimized_validate_alias_name(alias)


class TestOptimizedValidateCommandContent:
    """Test optimized command content validation."""

    def test_optimized_validate_command_content_valid(self):
        """Test optimized_validate_command_content with valid command."""
        result = optimized_validate_command_content("look north")
        assert result == "look north"

    def test_optimized_validate_command_content_empty(self):
        """Test optimized_validate_command_content with empty command."""
        assert optimized_validate_command_content("") == ""
        assert optimized_validate_command_content(None) is None

    def test_optimized_validate_command_content_injection_patterns(self):
        """Test optimized_validate_command_content rejects injection patterns."""
        with pytest.raises(ValueError, match="dangerous pattern"):
            optimized_validate_command_content("look; rm -rf /")


class TestOptimizedValidateReasonContent:
    """Test optimized reason content validation."""

    def test_optimized_validate_reason_content_valid(self):
        """Test optimized_validate_reason_content with valid reason."""
        result = optimized_validate_reason_content("Spam")
        assert result == "Spam"

    def test_optimized_validate_reason_content_empty(self):
        """Test optimized_validate_reason_content with empty reason."""
        assert optimized_validate_reason_content("") == ""
        assert optimized_validate_reason_content(None) is None

    def test_optimized_validate_reason_content_injection_patterns(self):
        """Test optimized_validate_reason_content rejects injection patterns."""
        with pytest.raises(ValueError, match="dangerous pattern"):
            optimized_validate_reason_content("Spam; rm -rf /")


class TestOptimizedValidatePoseContent:
    """Test optimized pose content validation."""

    def test_optimized_validate_pose_content_valid(self):
        """Test optimized_validate_pose_content with valid pose."""
        result = optimized_validate_pose_content("sits quietly")
        assert result == "sits quietly"

    def test_optimized_validate_pose_content_empty(self):
        """Test optimized_validate_pose_content with empty pose."""
        assert optimized_validate_pose_content("") == ""
        assert optimized_validate_pose_content(None) is None

    def test_optimized_validate_pose_content_injection_patterns(self):
        """Test optimized_validate_pose_content rejects injection patterns."""
        with pytest.raises(ValueError, match="dangerous pattern"):
            optimized_validate_pose_content("sits; rm -rf /")


class TestOptimizedValidateFilterName:
    """Test optimized filter name validation."""

    def test_optimized_validate_filter_name_valid(self):
        """Test optimized_validate_filter_name with valid filter names."""
        valid_filters = ["Alice", "Bob123", "Charlie_Test", "Diana-Player"]
        for filter_name in valid_filters:
            result = optimized_validate_filter_name(filter_name)
            assert result == filter_name

    def test_optimized_validate_filter_name_empty(self):
        """Test optimized_validate_filter_name with empty filter."""
        assert optimized_validate_filter_name("") == ""
        assert optimized_validate_filter_name(None) is None

    def test_optimized_validate_filter_name_invalid_format(self):
        """Test optimized_validate_filter_name rejects invalid formats."""
        invalid_filters = ["123Alice", "Alice Bob", "Alice@Bob"]
        for filter_name in invalid_filters:
            with pytest.raises(ValueError, match="Filter name must start"):
                optimized_validate_filter_name(filter_name)


class TestOptimizedValidateTargetPlayer:
    """Test optimized target player validation."""

    def test_optimized_validate_target_player_valid(self):
        """Test optimized_validate_target_player with valid target."""
        result = optimized_validate_target_player("Alice")
        assert result == "Alice"

    def test_optimized_validate_target_player_empty(self):
        """Test optimized_validate_target_player with empty target."""
        assert optimized_validate_target_player("") == ""
        assert optimized_validate_target_player(None) is None

    def test_optimized_validate_target_player_invalid_format(self):
        """Test optimized_validate_target_player rejects invalid formats."""
        invalid_targets = ["123Alice", "Alice Bob", "Alice@Bob"]
        for target in invalid_targets:
            with pytest.raises(ValueError, match="Target player name must start"):
                optimized_validate_target_player(target)


class TestOptimizedValidateHelpTopic:
    """Test optimized help topic validation."""

    def test_optimized_validate_help_topic_valid(self):
        """Test optimized_validate_help_topic with valid topics."""
        valid_topics = ["help", "commands", "combat", "magic"]
        for topic in valid_topics:
            result = optimized_validate_help_topic(topic)
            assert result == topic

    def test_optimized_validate_help_topic_empty(self):
        """Test optimized_validate_help_topic with empty topic."""
        assert optimized_validate_help_topic("") == ""
        assert optimized_validate_help_topic(None) is None

    def test_optimized_validate_help_topic_invalid_format(self):
        """Test optimized_validate_help_topic rejects invalid formats."""
        invalid_topics = ["123topic", "help topic", "help@topic"]
        for topic in invalid_topics:
            with pytest.raises(ValueError, match="Help topic must start"):
                optimized_validate_help_topic(topic)


class TestOptimizedValidateSecurityComprehensive:
    """Test optimized comprehensive security validation."""

    def test_optimized_validate_security_comprehensive_valid(self):
        """Test optimized_validate_security_comprehensive with valid content."""
        result = optimized_validate_security_comprehensive("Hello, world!")
        assert result == "Hello, world!"

    def test_optimized_validate_security_comprehensive_empty(self):
        """Test optimized_validate_security_comprehensive with empty content."""
        assert optimized_validate_security_comprehensive("") == ""
        assert optimized_validate_security_comprehensive(None) is None

    def test_optimized_validate_security_comprehensive_dangerous_chars(self):
        """Test optimized_validate_security_comprehensive rejects dangerous chars."""
        with pytest.raises(ValueError, match="dangerous characters"):
            optimized_validate_security_comprehensive("Hello<script>alert('xss')</script>")

    def test_optimized_validate_security_comprehensive_injection_patterns(self):
        """Test optimized_validate_security_comprehensive rejects injection patterns."""
        with pytest.raises(ValueError, match="dangerous pattern"):
            optimized_validate_security_comprehensive("Hello; rm -rf /")


class TestBenchmarkValidationPerformance:
    """Test benchmark_validation_performance function."""

    def test_benchmark_validation_performance(self):
        """Test benchmark_validation_performance runs successfully."""
        result = benchmark_validation_performance()
        assert isinstance(result, float)
        assert result >= 0  # Should return a non-negative time value
