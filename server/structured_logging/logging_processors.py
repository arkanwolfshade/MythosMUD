"""
Logging processors for structlog event processing.

This module provides processors for sanitizing sensitive data, adding correlation IDs,
request context, and enhancing player IDs with names.
"""

# pylint: disable=too-few-public-methods  # Reason: Logging processor classes with focused responsibility, minimal public interface

import re
import threading
import uuid
from datetime import UTC, datetime
from typing import Any


# Type stub for function attribute
class _PlayerServiceHolder:  # pylint: disable=too-few-public-methods  # Reason: Holder class with focused responsibility, minimal public interface
    player_service: Any | None = None


# Module-level holder for player service to avoid global statement
_player_service_holder = _PlayerServiceHolder()

# Thread-local flag to prevent recursion in enhance_player_ids
_enhancing_player_ids = threading.local()


def set_global_player_service(player_service: Any) -> None:
    """
    Set the global player service for logging enhancement.

    This allows the logging system to access player information for
    enhancing log entries with player names.

    Args:
        player_service: The player service instance
    """
    # Store player service in module-level holder
    _player_service_holder.player_service = player_service


def sanitize_sensitive_data(_logger: Any, _name: str, event_dict: dict[str, Any]) -> dict[str, Any]:
    """
    Remove sensitive data from log entries.

    This processor automatically redacts sensitive information like passwords,
    tokens, and credentials from log entries to prevent information leakage.

    Args:
        _logger: Logger instance (unused)
        _name: Logger name (unused)
        event_dict: Event dictionary to sanitize

    Returns:
        Sanitized event dictionary
    """
    # Sensitive patterns that should be redacted
    # These patterns match whole words or specific suffixes/prefixes
    sensitive_patterns = [
        r"\bpassword\b",
        r"\btoken\b",
        r"\bsecret\b",
        r"_key\b",  # Matches fields ending with _key (api_key, private_key, etc.)
        r"\bkey_\b",  # Matches fields starting with key_ (key_id, key_value, etc.)
        r"^key$",  # Matches exact field name "key"
        r"\bcredential\b",
        r"\bauth\b",
        r"\bjwt\b",
        r"\bbearer\b",
        r"\bauthorization\b",
    ]

    # Safe field names that should never be redacted even if they match patterns
    safe_fields = {
        "subzone_key",
        "zone_key",
        "room_key",
        "object_key",
        "item_key",
        "npc_key",
    }

    def sanitize_dict(d: dict[str, Any]) -> dict[str, Any]:
        """Recursively sanitize dictionary values."""
        sanitized: dict[str, Any] = {}
        for key, value in d.items():
            if isinstance(value, dict):
                sanitized[key] = sanitize_dict(value)
            else:
                # Since dict is typed as dict[str, Any], key is always str
                key_lower = key.lower()
                # Check if field is in safe list
                if key_lower in safe_fields:
                    sanitized[key] = value
                # Check if field matches any sensitive pattern
                elif any(re.search(pattern, key_lower) for pattern in sensitive_patterns):
                    sanitized[key] = "[REDACTED]"
                else:
                    sanitized[key] = value
        return sanitized

    return sanitize_dict(event_dict)


def add_correlation_id(_logger: Any, _name: str, event_dict: dict[str, Any]) -> dict[str, Any]:
    """
    Add correlation ID to log entries if not already present.

    This processor ensures that all log entries have a correlation ID for
    request tracing and debugging.

    Args:
        _logger: Logger instance (unused)
        _name: Logger name (unused)
        event_dict: Event dictionary to enhance

    Returns:
        Enhanced event dictionary with correlation ID
    """
    if "correlation_id" not in event_dict:
        event_dict["correlation_id"] = str(uuid.uuid4())

    return event_dict


def add_request_context(_logger: Any, _name: str, event_dict: dict[str, Any]) -> dict[str, Any]:
    """
    Add request context information to log entries.

    This processor adds contextual information like request ID, user ID,
    and session information to log entries.

    Args:
        _logger: Logger instance (unused)
        _name: Logger name (unused)
        event_dict: Event dictionary to enhance

    Returns:
        Enhanced event dictionary with request context
    """
    # Add timestamp if not present
    if "timestamp" not in event_dict:
        event_dict["timestamp"] = datetime.now(UTC).isoformat()

    # Add logger name for better traceability
    if "logger_name" not in event_dict:
        event_dict["logger_name"] = _name

    # Add request ID if not present
    if "request_id" not in event_dict:
        event_dict["request_id"] = str(uuid.uuid4())

    return event_dict


def enhance_player_ids(_logger: Any, _name: str, event_dict: dict[str, Any]) -> dict[str, Any]:
    """
    Enhance player_id fields with player names for better log readability.

    This processor automatically converts player_id fields to include both
    player name and ID in the format "<name>: <ID>" for better debugging.

    Args:
        _logger: Logger instance (unused)
        _name: Logger name (unused)
        event_dict: Event dictionary to enhance

    Returns:
        Enhanced event dictionary with player names
    """
    # Access player service from module-level holder
    player_service = _player_service_holder.player_service

    # Prevent recursion: if we're already enhancing player IDs, skip immediately
    # Check this FIRST before any other operations
    if hasattr(_enhancing_player_ids, "active") and _enhancing_player_ids.active:
        return event_dict

    # Set recursion guard IMMEDIATELY before any operations that might trigger logging
    _enhancing_player_ids.active = True
    try:  # pylint: disable=too-many-nested-blocks  # Reason: Logging processor requires complex nested logic for player ID enhancement, UUID validation, and event dictionary processing
        if player_service and hasattr(player_service, "persistence"):
            # Process any player_id fields in the event dictionary
            for key, value in event_dict.items():
                if key == "player_id" and isinstance(value, str):
                    # Check if this looks like a UUID
                    if len(value) == 36 and value.count("-") == 4:
                        # Import here to avoid circular import with server.exceptions -> enhanced_logging_config
                        # Define a local exception type alias for optional dependency
                        try:
                            from server.exceptions import (
                                DatabaseError as _ImportedDatabaseError,  # noqa: F401  # pylint: disable=unused-import  # Reason: Imported for type alias assignment, unused but required for type annotation
                            )

                            _DatabaseErrorType: type[BaseException] = _ImportedDatabaseError
                        except ImportError:  # fallback if exceptions not yet available
                            _DatabaseErrorType = Exception

                        try:
                            # Try to get the player name
                            # Convert string to UUID if needed
                            player_id_uuid = uuid.UUID(value) if isinstance(value, str) else value
                            player = player_service.persistence.get_player(player_id_uuid)
                            if player and hasattr(player, "name"):
                                # Enhance the player_id field with the player name
                                event_dict[key] = f"<{player.name}>: {value}"
                        except (AttributeError, KeyError, TypeError, ValueError, _DatabaseErrorType, RecursionError):
                            # Silently skip on recursion or other errors - don't log to avoid infinite loop
                            # If lookup fails, leave the original value
                            pass
    finally:
        # Clear recursion guard - ALWAYS clear it, even if an exception occurs
        _enhancing_player_ids.active = False

    return event_dict
