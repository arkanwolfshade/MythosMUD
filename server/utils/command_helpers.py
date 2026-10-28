"""
Helper functions for command parsing and validation.

This module contains utility functions that were previously in command_parser.py,
including command safety validation, help text generation, and username extraction.
"""

import re
from collections.abc import Mapping
from typing import Protocol, cast, runtime_checkable

from ..exceptions import ValidationError as MythosValidationError
from ..structured_logging.enhanced_logging_config import get_logger
from .enhanced_error_logging import log_and_raise_enhanced

logger = get_logger(__name__)


@runtime_checkable
class _HasNameAndPlayerId(Protocol):  # pylint: disable=too-few-public-methods  # Reason: Protocol stub
    name: object
    player_id: object


@runtime_checkable
class _HasUsername(Protocol):  # pylint: disable=too-few-public-methods  # Reason: Protocol stub
    username: object


@runtime_checkable
class _HasName(Protocol):  # pylint: disable=too-few-public-methods  # Reason: Protocol stub
    name: object


def validate_command_safety(command_string: str) -> bool:
    """
    Perform additional safety validation on command string.

    Args:
        command_string: Raw command string

    Returns:
        True if command is safe, False otherwise
    """
    # Check for obvious injection attempts
    dangerous_patterns = [
        r"[;|&`$()]",  # Shell metacharacters
        r"\b(and|or)\s*=\s*",  # SQL injection
        r"__import__|eval|exec|system|os\.",  # Python injection
        r"%[a-zA-Z]",  # Format string injection
        r"<script|javascript:",  # XSS attempts
    ]

    for pattern in dangerous_patterns:
        if re.search(pattern, command_string, re.IGNORECASE):
            logger.warning("Dangerous pattern detected in command", pattern=pattern, command=command_string)
            return False

    return True


def _username_from_dict(d: Mapping[str, object]) -> str | None:
    """Extract username or name from a dict; return None if neither key present."""
    if "username" in d:
        return str(d["username"])
    if "name" in d:
        return str(d["name"])
    return None


def get_username_from_user(user_obj: object) -> str:
    """
    Safely extract username from user object or dictionary.

    This utility function eliminates code duplication across command handlers
    by providing a centralized way to extract usernames from various user object formats.
    As noted in the restricted archives, this pattern reduces maintenance burden
    and ensures consistent behavior across all command implementations.

    Args:
        user_obj: User object that may be a dict, object with attributes, or other format

    Returns:
        str: The username/name from the user object

    Raises:
        ValueError: If no username or name can be extracted from the user object
    """
    if isinstance(user_obj, _HasNameAndPlayerId):
        return str(user_obj.name)
    if isinstance(user_obj, _HasUsername):
        return str(user_obj.username)
    if isinstance(user_obj, _HasName):
        return str(user_obj.name)
    if isinstance(user_obj, dict):
        result = _username_from_dict(cast(dict[str, object], user_obj))
        if result is not None:
            return result
    log_and_raise_enhanced(
        MythosValidationError,
        "User object must have username or name attribute or key",
        user_obj_type=type(user_obj).__name__,
        user_obj=str(user_obj),
        logger_name=__name__,
    )
