"""
Security validation constants and patterns for MythosMUD.

This module defines security patterns and constants used for
validating command input and preventing injection attacks.
Focuses on sanitization (cleaning) rather than validation (rejection)
to preserve user expression freedom.

As noted in the Pnakotic Manuscripts: "Security must be consistent across all
gateways, lest the ancient ones find a way through the cracks in our defenses."
"""

import re

import ftfy
import strip_ansi

# Patterns to reject for command injection (expand as needed)
# These patterns are more specific than the command model validators
# to avoid false positives while still catching injection attempts
# NOTE: Focus on actual code execution patterns, not just keywords
INJECTION_PATTERNS = [
    r"[;|]",  # shell metacharacters (removed & as it's safe in messages)
    r"\b(or|and)\b.*=",  # SQL injection with assignment (flexible spacing)
    r"(__import__|eval|exec)\s*\(|os\.system\s*\(|os\.popen\s*\(",  # Python function calls, not keywords
    r"%\d*[sdxXfFgGeEcCbrpP]",  # format string specifiers (not just %)
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

# Commands that traditionally use slash prefix in modern interfaces
SLASH_COMMANDS = {"help", "who", "quit", "look", "go", "say", "me", "pose", "alias", "aliases", "unalias", "npc"}


def sanitize_unicode_input(text: str) -> str:
    """
    Sanitize Unicode input using ftfy to fix common encoding issues.

    This function addresses issues like:
    - Mojibake (double-encoded text)
    - Combining characters that should be precomposed
    - Invisible Unicode characters
    - Control characters

    Focuses on sanitization (cleaning) rather than validation (rejection)
    to preserve user expression freedom.

    Args:
        text: Raw input text that may contain Unicode issues

    Returns:
        str: Sanitized text with Unicode issues fixed
    """
    if not text:
        return text

    # Fix Unicode issues using ftfy with recommended settings for MUD environment
    # The default configuration already includes most of what we need
    # We'll use the default settings which are well-tuned for text cleaning
    sanitized = ftfy.fix_text(text)

    return sanitized


def strip_ansi_codes(text: str) -> str:
    """
    Remove ANSI escape codes from text input.

    ANSI codes can be used to hide malicious content or cause display issues.
    This is particularly important for terminal-based clients.
    Focuses on sanitization (cleaning) rather than validation (rejection).

    Args:
        text: Input text that may contain ANSI escape codes

    Returns:
        str: Text with ANSI codes removed
    """
    if not text:
        return text

    # First use strip-ansi for color and formatting codes
    cleaned = strip_ansi.strip_ansi(text)

    # Then remove any remaining ANSI escape sequences that strip-ansi missed
    # This handles cursor movement codes and other terminal sequences
    cleaned = re.sub(r"\x1b\[[0-9;]*[a-zA-Z]", "", cleaned)

    return cleaned


def comprehensive_sanitize_input(text: str) -> str:
    """
    Apply comprehensive input sanitization including Unicode fixes and ANSI removal.

    This is the main function that should be called for all user input
    before further processing or validation. Focuses on sanitization
    (cleaning) rather than validation (rejection) to preserve user
    expression freedom.

    Args:
        text: Raw user input text

    Returns:
        str: Fully sanitized text ready for further processing
    """
    if not text:
        return text

    # Step 1: Fix Unicode issues
    sanitized = sanitize_unicode_input(text)

    # Step 2: Remove ANSI codes
    sanitized = strip_ansi_codes(sanitized)

    # Step 3: Additional security checks
    # Remove null bytes and other control characters (except newlines and tabs)
    # Also remove invisible Unicode characters that could hide malicious content
    # This preserves user intent while removing dangerous control sequences
    sanitized = re.sub(r"[\x00-\x08\x0B\x0C\x0E-\x1F\x7F]", "", sanitized)
    # Remove zero-width characters and other invisible Unicode
    sanitized = re.sub(
        r"[\u200B-\u200D\uFEFF]", "", sanitized
    )  # Zero-width space, zero-width non-joiner, zero-width joiner, zero-width no-break space

    return sanitized


# Centralized validation functions for command models
def validate_message_content(value: str) -> str:
    """
    Centralized validation for message content fields.

    This function provides consistent validation for all message-based fields
    across command models, including say, local, system, whisper, and reply commands.

    Args:
        value: The message content to validate

    Returns:
        str: The validated message content

    Raises:
        ValueError: If the message contains dangerous characters or patterns
    """
    if not value:
        return value

    # First sanitize the input
    sanitized = comprehensive_sanitize_input(value)

    # Check for truly dangerous characters (HTML/XSS only)
    # Allow special chars like !@#$%^&*() as they're safe in messages
    dangerous_chars = ["<", ">"]  # Only block HTML tags
    found_dangerous = [char for char in dangerous_chars if char in sanitized]

    if found_dangerous:
        raise ValueError(f"Message contains dangerous characters: {found_dangerous}")

    # Check for injection patterns
    for pattern in INJECTION_PATTERNS:
        if re.search(pattern, sanitized, re.IGNORECASE):
            raise ValueError(f"Message contains potentially dangerous pattern: {pattern}")

    return sanitized


def validate_action_content(value: str) -> str:
    """
    Centralized validation for action content fields.

    This function provides consistent validation for all action-based fields
    across command models, including emote and me commands.

    Args:
        value: The action content to validate

    Returns:
        str: The validated action content

    Raises:
        ValueError: If the action contains dangerous characters or patterns
    """
    if not value:
        return value

    # First sanitize the input
    sanitized = comprehensive_sanitize_input(value)

    # Check for truly dangerous characters (HTML/XSS only)
    dangerous_chars = ["<", ">"]
    found_dangerous = [char for char in dangerous_chars if char in sanitized]

    if found_dangerous:
        raise ValueError(f"Action contains dangerous characters: {found_dangerous}")

    # Check for injection patterns
    for pattern in INJECTION_PATTERNS:
        if re.search(pattern, sanitized, re.IGNORECASE):
            raise ValueError(f"Action contains potentially dangerous pattern: {pattern}")

    return sanitized


def validate_player_name(value: str) -> str:
    """
    Centralized validation for player name fields.

    This function provides consistent validation for all player name fields
    across command models, ensuring proper format and security.

    Args:
        value: The player name to validate

    Returns:
        str: The validated player name

    Raises:
        ValueError: If the player name has invalid format
    """
    if not value:
        return value

    # Check format: must start with letter, contain only letters, numbers, underscores, and hyphens
    if not re.match(r"^[a-zA-Z][a-zA-Z0-9_-]*$", value):
        raise ValueError(
            "Player name must start with a letter and contain only letters, numbers, underscores, and hyphens"
        )

    return value


def validate_alias_name(value: str) -> str:
    """
    Centralized validation for alias name fields.

    This function provides consistent validation for alias name fields,
    ensuring proper format and security.

    Args:
        value: The alias name to validate

    Returns:
        str: The validated alias name

    Raises:
        ValueError: If the alias name has invalid format
    """
    if not value:
        return value

    # Check format: must start with letter, contain only letters, numbers, and underscores
    if not re.match(r"^[a-zA-Z][a-zA-Z0-9_]*$", value):
        raise ValueError("Alias name must start with a letter and contain only letters, numbers, and underscores")

    return value


def validate_command_content(value: str) -> str:
    """
    Centralized validation for command content fields.

    This function provides consistent validation for command content fields,
    such as those used in alias commands.

    Args:
        value: The command content to validate

    Returns:
        str: The validated command content

    Raises:
        ValueError: If the command contains dangerous patterns
    """
    if not value:
        return value

    # First sanitize the input
    sanitized = comprehensive_sanitize_input(value)

    # Check for injection patterns (more strict for command content)
    for pattern in INJECTION_PATTERNS:
        if re.search(pattern, sanitized, re.IGNORECASE):
            raise ValueError(f"Command contains potentially dangerous pattern: {pattern}")

    return sanitized


def validate_reason_content(value: str) -> str:
    """
    Centralized validation for reason content fields.

    This function provides consistent validation for reason fields,
    such as those used in mute commands.

    Args:
        value: The reason content to validate

    Returns:
        str: The validated reason content

    Raises:
        ValueError: If the reason contains dangerous characters or patterns
    """
    if not value:
        return value

    # First sanitize the input
    sanitized = comprehensive_sanitize_input(value)

    # Check for truly dangerous characters (HTML/XSS only)
    dangerous_chars = ["<", ">"]
    found_dangerous = [char for char in dangerous_chars if char in sanitized]

    if found_dangerous:
        raise ValueError(f"Reason contains dangerous characters: {found_dangerous}")

    # Check for injection patterns
    for pattern in INJECTION_PATTERNS:
        if re.search(pattern, sanitized, re.IGNORECASE):
            raise ValueError(f"Reason contains potentially dangerous pattern: {pattern}")

    return sanitized


def validate_pose_content(value: str) -> str:
    """
    Centralized validation for pose content fields.

    This function provides consistent validation for pose fields,
    such as those used in pose commands.

    Args:
        value: The pose content to validate

    Returns:
        str: The validated pose content

    Raises:
        ValueError: If the pose contains dangerous characters or patterns
    """
    if not value:
        return value

    # First sanitize the input
    sanitized = comprehensive_sanitize_input(value)

    # Check for truly dangerous characters (HTML/XSS only)
    dangerous_chars = ["<", ">"]
    found_dangerous = [char for char in dangerous_chars if char in sanitized]

    if found_dangerous:
        raise ValueError(f"Pose contains dangerous characters: {found_dangerous}")

    # Check for injection patterns
    for pattern in INJECTION_PATTERNS:
        if re.search(pattern, sanitized, re.IGNORECASE):
            raise ValueError(f"Pose contains potentially dangerous pattern: {pattern}")

    return sanitized


def validate_filter_name(value: str) -> str:
    """
    Centralized validation for filter name fields.

    This function provides consistent validation for filter name fields,
    such as those used in who commands.

    Args:
        value: The filter name to validate

    Returns:
        str: The validated filter name

    Raises:
        ValueError: If the filter name has invalid format
    """
    if not value:
        return value

    # Check format: must start with letter, contain only letters, numbers, underscores, and hyphens
    if not re.match(r"^[a-zA-Z][a-zA-Z0-9_-]*$", value):
        raise ValueError(
            "Filter name must start with a letter and contain only letters, numbers, underscores, and hyphens"
        )

    return value


def validate_target_player(value: str) -> str:
    """
    Centralized validation for target player fields.

    This function provides consistent validation for target player fields,
    such as those used in whisper commands.

    Args:
        value: The target player name to validate

    Returns:
        str: The validated target player name

    Raises:
        ValueError: If the target player name has invalid format
    """
    if not value:
        return value

    # Check format: must start with letter, contain only letters, numbers, underscores, and hyphens
    if not re.match(r"^[a-zA-Z][a-zA-Z0-9_-]*$", value):
        raise ValueError(
            "Target player name must start with a letter and contain only letters, numbers, underscores, and hyphens"
        )

    return value


def validate_help_topic(value: str) -> str:
    """
    Centralized validation for help topic fields.

    This function provides consistent validation for help topic fields,
    ensuring proper format and security.

    Args:
        value: The help topic to validate

    Returns:
        str: The validated help topic

    Raises:
        ValueError: If the help topic has invalid format
    """
    if not value:
        return value

    # Check format: must start with letter, contain only letters, numbers, underscores, and hyphens
    if not re.match(r"^[a-zA-Z][a-zA-Z0-9_-]*$", value):
        raise ValueError(
            "Help topic must start with a letter and contain only letters, numbers, underscores, and hyphens"
        )

    return value


# Utility functions for centralized validation
def get_dangerous_characters() -> list[str]:
    """
    Get the list of dangerous characters used in validation.

    Returns:
        List[str]: List of dangerous characters (HTML/XSS only)
    """
    return ["<", ">"]  # Only block HTML tags


def get_injection_patterns() -> list[str]:
    """
    Get the list of injection patterns used in validation.

    Returns:
        List[str]: List of injection patterns
    """
    return INJECTION_PATTERNS.copy()


def check_dangerous_characters(text: str) -> tuple[bool, list[str]]:
    """
    Check if text contains dangerous characters.

    Args:
        text: The text to check

    Returns:
        Tuple[bool, List[str]]: (has_dangerous_chars, list_of_found_chars)
    """
    if not text:
        return False, []

    dangerous_chars = get_dangerous_characters()
    found_chars = [char for char in dangerous_chars if char in text]
    return len(found_chars) > 0, found_chars


def check_injection_patterns(text: str) -> tuple[bool, list[str]]:
    """
    Check if text matches injection patterns.

    Args:
        text: The text to check

    Returns:
        Tuple[bool, List[str]]: (has_injection_patterns, list_of_matched_patterns)
    """
    if not text:
        return False, []

    injection_patterns = get_injection_patterns()
    matched_patterns = []

    for pattern in injection_patterns:
        if re.search(pattern, text, re.IGNORECASE):
            matched_patterns.append(pattern)

    return len(matched_patterns) > 0, matched_patterns


def validate_security_comprehensive(text: str, field_type: str = "message") -> str:
    """
    Comprehensive security validation for any text field.

    This is the main validation function that should be used for all text fields
    in command models. It provides consistent security validation based on field type.

    Args:
        text: The text to validate
        field_type: The type of field being validated (message, action, player_name, etc.)

    Returns:
        str: The validated text

    Raises:
        ValueError: If the text fails validation
    """
    if not text:
        return text

    # Apply appropriate validation based on field type
    if field_type in ["message", "reason", "pose"]:
        return validate_message_content(text)
    elif field_type == "action":
        return validate_action_content(text)
    elif field_type == "player_name":
        return validate_player_name(text)
    elif field_type == "alias_name":
        return validate_alias_name(text)
    elif field_type == "command":
        return validate_command_content(text)
    elif field_type == "filter_name":
        return validate_filter_name(text)
    elif field_type == "target":
        return validate_target_player(text)
    else:
        # Default to message validation for unknown field types
        return validate_message_content(text)
