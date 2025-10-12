"""
Security validation constants and patterns for MythosMUD.

This module defines security patterns and constants used for
validating command input and preventing injection attacks.
Focuses on sanitization (cleaning) rather than validation (rejection)
to preserve user expression freedom.
"""

import re

import ftfy
import strip_ansi

# Patterns to reject for command injection (expand as needed)
# These patterns are more specific than the command model validators
# to avoid false positives while still catching injection attempts
INJECTION_PATTERNS = [
    r"[;|&]",  # shell metacharacters
    r"\b(or|and)\b.*=",  # SQL injection
    r"__import__|eval|exec|system|os\.",  # Python injection
    r"%[a-zA-Z]",  # format string
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
