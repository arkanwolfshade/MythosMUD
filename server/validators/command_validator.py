"""
Command input validation utilities for MythosMUD.

This module provides functions for validating, cleaning, and normalizing
command input to ensure security and consistency.
Focuses on sanitization (cleaning) rather than validation (rejection)
to preserve user expression freedom.
"""

import re

from ..logging_config import get_logger
from .security_validator import INJECTION_PATTERNS, comprehensive_sanitize_input

logger = get_logger(__name__)


def normalize_command(command: str) -> str:
    """
    Normalize command input by removing optional slash prefix.

    Supports both traditional MUD commands (go north) and modern slash commands (/go north).
    This allows for flexible command input while maintaining backward compatibility.

    Args:
        command: The raw command string from user input

    Returns:
        Normalized command string with slash prefix removed if present
    """
    if not command:
        return command

    # Remove leading slash if present
    if command.startswith("/"):
        normalized = command[1:].strip()
        logger.debug("Slash prefix removed from command", original=command, normalized=normalized)
        return normalized

    return command.strip()


def is_suspicious_input(command: str) -> bool:
    """
    Check if command contains suspicious patterns that might indicate injection attempts.

    This function focuses on true injection attempts rather than legitimate user expression.
    It's designed to catch malicious patterns while avoiding false positives on
    creative user input.

    Args:
        command: The command string to validate

    Returns:
        bool: True if suspicious patterns are detected, False otherwise
    """
    for pat in INJECTION_PATTERNS:
        if re.search(pat, command, re.IGNORECASE):
            logger.warning("Suspicious command pattern detected", pattern=pat, command=command)
            return True
    return False


def clean_command_input(command: str) -> str:
    """
    Clean and normalize command input with comprehensive sanitization.

    This function applies multiple layers of sanitization:
    1. Unicode normalization and fixing (ftfy)
    2. ANSI code removal (strip-ansi)
    3. Control character removal
    4. Whitespace normalization

    Focuses on sanitization (cleaning) rather than validation (rejection)
    to preserve user expression freedom.

    Args:
        command: The raw command string

    Returns:
        str: Fully sanitized command string
    """
    if not command:
        return command

    # Apply comprehensive sanitization first
    sanitized = comprehensive_sanitize_input(command)

    # Then apply traditional cleaning (whitespace normalization)
    cleaned = re.sub(r"\s+", " ", sanitized).strip()

    if cleaned != command:
        logger.debug("Command input sanitized and cleaned", original=command, cleaned=cleaned)

    return cleaned


def validate_command_length(command: str, max_length: int = 1000) -> bool:
    """
    Validate that command length is within acceptable limits.

    Args:
        command: The command string to validate
        max_length: Maximum allowed command length

    Returns:
        bool: True if command length is acceptable, False otherwise
    """
    if len(command) > max_length:
        logger.warning("Command too long", command_length=len(command), max_length=max_length)
        return False
    return True


def validate_command_format(command: str) -> tuple[bool, str]:
    """
    Validate command format and return validation result with error message.

    Args:
        command: The command string to validate

    Returns:
        tuple[bool, str]: (is_valid, error_message)
    """
    if not command:
        return False, "Empty command"

    if is_suspicious_input(command):
        return False, "Command contains suspicious patterns"

    if not validate_command_length(command):
        return False, "Command too long"

    return True, ""
