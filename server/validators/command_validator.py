"""
Command input validation utilities for MythosMUD.

This module provides functions for validating, cleaning, and normalizing
command input to ensure security and consistency.
"""

import re

from ..logging_config import get_logger
from .security_validator import INJECTION_PATTERNS

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
    Clean and normalize command input by collapsing multiple spaces and stripping whitespace.

    Args:
        command: The raw command string

    Returns:
        str: Cleaned command string
    """
    cleaned = re.sub(r"\s+", " ", command).strip()
    if cleaned != command:
        logger.debug("Command input cleaned", original=command, cleaned=cleaned)
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
