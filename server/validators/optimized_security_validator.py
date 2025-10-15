"""
Optimized security validation functions for MythosMUD.

This module provides performance-optimized versions of the security validation
functions, using compiled regex patterns, caching, and other optimizations
to improve validation speed while maintaining security.

As noted in the Pnakotic Manuscripts: "Efficiency in our eldritch defenses
is paramount, lest the ancient ones overwhelm us with their infinite patience."
"""

import re
from functools import lru_cache

import ftfy
import strip_ansi

# Pre-compile regex patterns for better performance
INJECTION_PATTERNS_COMPILED = [
    re.compile(pattern, re.IGNORECASE)
    for pattern in [
        r"[;|&]",  # shell metacharacters
        r"\b(or|and)\b.*=",  # SQL injection
        r"__import__|eval|exec|system|os\.",  # Python injection
        r"%[a-zA-Z]",  # format string
        r"<script[^>]*>",  # XSS script tags
        r"javascript:",  # javascript: URLs
        r"on\w+\s*=",  # event handlers (onclick, onload, etc.)
        r"data:text/html",  # data URLs with HTML
        r"\.\.\/",  # path traversal (../)
        r"\.\.\\",  # path traversal (..\)
        r"\.\.%2f",  # URL encoded path traversal
        r"\.\.%5c",  # URL encoded path traversal
        r"\.\.%252f",  # double URL encoded path traversal
        r"\.\.%255c",  # double URL encoded path traversal
    ]
]

# Pre-compile validation patterns
PLAYER_NAME_PATTERN = re.compile(r"^[a-zA-Z][a-zA-Z0-9_-]*$")
ALIAS_NAME_PATTERN = re.compile(r"^[a-zA-Z][a-zA-Z0-9_]*$")
HELP_TOPIC_PATTERN = re.compile(r"^[a-zA-Z][a-zA-Z0-9_-]*$")

# Pre-compile ANSI pattern
ANSI_PATTERN = re.compile(r"\x1b\[[0-9;]*[a-zA-Z]")

# Dangerous characters set for fast lookup
DANGEROUS_CHARS = set("<>\"'&")


@lru_cache(maxsize=1000)
def _cached_ftfy_fix(text: str) -> str:
    """Cached version of ftfy.fix_text for repeated inputs."""
    return ftfy.fix_text(text)


@lru_cache(maxsize=1000)
def _cached_strip_ansi(text: str) -> str:
    """Cached version of strip_ansi for repeated inputs."""
    return strip_ansi.strip_ansi(text)


def optimized_sanitize_unicode_input(text: str) -> str:
    """
    Optimized Unicode sanitization with caching.

    Args:
        text: Raw input text that may contain Unicode issues

    Returns:
        str: Sanitized text with Unicode issues fixed
    """
    if not text:
        return text

    return _cached_ftfy_fix(text)


def optimized_strip_ansi_codes(text: str) -> str:
    """
    Optimized ANSI code removal with caching.

    Args:
        text: Input text that may contain ANSI escape codes

    Returns:
        str: Text with ANSI codes removed
    """
    if not text:
        return text

    # Use cached strip_ansi first
    cleaned = _cached_strip_ansi(text)

    # Then remove any remaining ANSI escape sequences
    cleaned = ANSI_PATTERN.sub("", cleaned)

    return cleaned


def optimized_comprehensive_sanitize_input(text: str) -> str:
    """
    Optimized comprehensive input sanitization.

    Args:
        text: Raw input text to sanitize

    Returns:
        str: Sanitized text
    """
    if not text:
        return text

    # Step 1: Unicode sanitization (cached)
    sanitized = optimized_sanitize_unicode_input(text)

    # Step 2: ANSI code removal (cached)
    sanitized = optimized_strip_ansi_codes(sanitized)

    return sanitized


def optimized_validate_message_content(value: str) -> str:
    """
    Optimized validation for message content fields.

    Args:
        value: The message to validate

    Returns:
        str: The validated message

    Raises:
        ValueError: If the message contains dangerous patterns
    """
    if not value:
        return value

    # Fast check for dangerous characters first
    if any(char in DANGEROUS_CHARS for char in value):
        raise ValueError("Message contains dangerous characters")

    # Sanitize input
    sanitized = optimized_comprehensive_sanitize_input(value)

    # Check for injection patterns using pre-compiled regex
    for pattern in INJECTION_PATTERNS_COMPILED:
        if pattern.search(sanitized):
            raise ValueError(f"Message contains potentially dangerous pattern: {pattern.pattern}")

    return sanitized


def optimized_validate_action_content(value: str) -> str:
    """
    Optimized validation for action content fields.

    Args:
        value: The action to validate

    Returns:
        str: The validated action

    Raises:
        ValueError: If the action contains dangerous patterns
    """
    if not value:
        return value

    # Fast check for dangerous characters first
    if any(char in DANGEROUS_CHARS for char in value):
        raise ValueError("Action contains dangerous characters")

    # Sanitize input
    sanitized = optimized_comprehensive_sanitize_input(value)

    # Check for injection patterns using pre-compiled regex
    for pattern in INJECTION_PATTERNS_COMPILED:
        if pattern.search(sanitized):
            raise ValueError(f"Action contains potentially dangerous pattern: {pattern.pattern}")

    return sanitized


def optimized_validate_player_name(value: str) -> str:
    """
    Optimized validation for player name fields.

    Args:
        value: The player name to validate

    Returns:
        str: The validated player name

    Raises:
        ValueError: If the player name has invalid format
    """
    if not value:
        return value

    # Use pre-compiled pattern for faster matching
    if not PLAYER_NAME_PATTERN.match(value):
        raise ValueError(
            "Player name must start with a letter and contain only letters, numbers, underscores, and hyphens"
        )

    return value


def optimized_validate_alias_name(value: str) -> str:
    """
    Optimized validation for alias name fields.

    Args:
        value: The alias name to validate

    Returns:
        str: The validated alias name

    Raises:
        ValueError: If the alias name has invalid format
    """
    if not value:
        return value

    # Use pre-compiled pattern for faster matching
    if not ALIAS_NAME_PATTERN.match(value):
        raise ValueError("Alias name must start with a letter and contain only letters, numbers, and underscores")

    return value


def optimized_validate_command_content(value: str) -> str:
    """
    Optimized validation for command content fields.

    Args:
        value: The command content to validate

    Returns:
        str: The validated command content

    Raises:
        ValueError: If the command contains dangerous patterns
    """
    if not value:
        return value

    # Sanitize input
    sanitized = optimized_comprehensive_sanitize_input(value)

    # Check for injection patterns using pre-compiled regex
    for pattern in INJECTION_PATTERNS_COMPILED:
        if pattern.search(sanitized):
            raise ValueError(f"Command contains potentially dangerous pattern: {pattern.pattern}")

    return sanitized


def optimized_validate_reason_content(value: str) -> str:
    """
    Optimized validation for reason content fields.

    Args:
        value: The reason to validate

    Returns:
        str: The validated reason

    Raises:
        ValueError: If the reason contains dangerous patterns
    """
    if not value:
        return value

    # Sanitize input
    sanitized = optimized_comprehensive_sanitize_input(value)

    # Check for injection patterns using pre-compiled regex
    for pattern in INJECTION_PATTERNS_COMPILED:
        if pattern.search(sanitized):
            raise ValueError(f"Reason contains potentially dangerous pattern: {pattern.pattern}")

    return sanitized


def optimized_validate_pose_content(value: str) -> str:
    """
    Optimized validation for pose content fields.

    Args:
        value: The pose to validate

    Returns:
        str: The validated pose

    Raises:
        ValueError: If the pose contains dangerous patterns
    """
    if not value:
        return value

    # Sanitize input
    sanitized = optimized_comprehensive_sanitize_input(value)

    # Check for injection patterns using pre-compiled regex
    for pattern in INJECTION_PATTERNS_COMPILED:
        if pattern.search(sanitized):
            raise ValueError(f"Pose contains potentially dangerous pattern: {pattern.pattern}")

    return sanitized


def optimized_validate_filter_name(value: str) -> str:
    """
    Optimized validation for filter name fields.

    Args:
        value: The filter name to validate

    Returns:
        str: The validated filter name

    Raises:
        ValueError: If the filter name has invalid format
    """
    if not value:
        return value

    # Use pre-compiled pattern for faster matching
    if not PLAYER_NAME_PATTERN.match(value):
        raise ValueError(
            "Filter name must start with a letter and contain only letters, numbers, underscores, and hyphens"
        )

    return value


def optimized_validate_target_player(value: str) -> str:
    """
    Optimized validation for target player fields.

    Args:
        value: The target player name to validate

    Returns:
        str: The validated target player name

    Raises:
        ValueError: If the target player name has invalid format
    """
    if not value:
        return value

    # Use pre-compiled pattern for faster matching
    if not PLAYER_NAME_PATTERN.match(value):
        raise ValueError(
            "Target player name must start with a letter and contain only letters, numbers, underscores, and hyphens"
        )

    return value


def optimized_validate_help_topic(value: str) -> str:
    """
    Optimized validation for help topic fields.

    Args:
        value: The help topic to validate

    Returns:
        str: The validated help topic

    Raises:
        ValueError: If the help topic has invalid format
    """
    if not value:
        return value

    # Use pre-compiled pattern for faster matching
    if not HELP_TOPIC_PATTERN.match(value):
        raise ValueError(
            "Help topic must start with a letter and contain only letters, numbers, underscores, and hyphens"
        )

    return value


def optimized_validate_security_comprehensive(value: str) -> str:
    """
    Optimized comprehensive security validation entry point.

    Args:
        value: The value to validate

    Returns:
        str: The validated value

    Raises:
        ValueError: If the value contains dangerous patterns
    """
    if not value:
        return value

    # Fast check for dangerous characters first
    if any(char in DANGEROUS_CHARS for char in value):
        raise ValueError("Content contains dangerous characters")

    # Sanitize input
    sanitized = optimized_comprehensive_sanitize_input(value)

    # Check for injection patterns using pre-compiled regex
    for pattern in INJECTION_PATTERNS_COMPILED:
        if pattern.search(sanitized):
            raise ValueError(f"Content contains potentially dangerous pattern: {pattern.pattern}")

    return sanitized


# Performance benchmarking functions
def benchmark_validation_performance():
    """Benchmark the performance of optimized vs original validation functions."""
    import time

    test_inputs = [
        "Hello world!",
        "Say hello to <script>alert('xss')</script>",
        "Go north; rm -rf /",
        "Player with spaces and special chars!",
        "Normal player name",
        "alias_name_test",
        "help topic with spaces",
        "Very long message that contains many characters and should test the performance of the validation functions",
    ]

    print("=== Validation Performance Benchmark ===")

    # Test optimized functions
    start_time = time.perf_counter()
    for _ in range(1000):
        for test_input in test_inputs:
            try:
                optimized_validate_message_content(test_input)
            except ValueError:
                pass  # Expected for some test inputs
    optimized_time = time.perf_counter() - start_time

    print(f"Optimized validation: {optimized_time:.6f}s for {len(test_inputs) * 1000} validations")
    print(f"Average per validation: {optimized_time / (len(test_inputs) * 1000):.8f}s")

    return optimized_time
