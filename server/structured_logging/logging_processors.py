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
from typing import cast

from structlog.typing import EventDict


# Type stub for function attribute
class _PlayerServiceHolder:  # pylint: disable=too-few-public-methods  # Reason: Holder class with focused responsibility, minimal public interface
    player_service: object | None = None


# Module-level holder for player service to avoid global statement
_player_service_holder = _PlayerServiceHolder()


class _EnhancePlayerIdsTls(threading.local):
    """Thread-local recursion guard for enhance_player_ids (typed .active for static analysis)."""

    active: bool

    def __init__(self) -> None:
        super().__init__()
        self.active = False


# Thread-local flag to prevent recursion in enhance_player_ids
_enhancing_player_ids = _EnhancePlayerIdsTls()


def set_global_player_service(player_service: object) -> None:
    """
    Set the global player service for logging enhancement.

    This allows the logging system to access player information for
    enhancing log entries with player names.

    Args:
        player_service: The player service instance
    """
    # Store player service in module-level holder
    _player_service_holder.player_service = player_service


def sanitize_sensitive_data(_logger: object, _name: str, event_dict: EventDict) -> EventDict:
    """sanitize_sensitive_data."""
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
        r"\bssn\b",  # Social Security Number
        r"\bsocial_security\b",
        r"\bcredit_card\b",
        r"\bcard_number\b",
        r"\bcvv\b",  # Card Verification Value
        r"\bcvc\b",  # Card Verification Code
        r"\bpin\b",  # Personal Identification Number
        r"\bapi_key\b",
        r"\bprivate_key\b",
        r"\baccess_token\b",
        r"\brefresh_token\b",
        r"\bsession_id\b",  # May contain sensitive session data
        r"\bcookie\b",
        r"\bcsrf\b",  # CSRF token
    ]
    safe_fields = {
        "subzone_key",
        "zone_key",
        "room_key",
        "object_key",
        "item_key",
        "npc_key",
    }

    def sanitize_dict(d: dict[str, object]) -> dict[str, object]:
        """Recursively sanitize dictionary values."""
        sanitized: dict[str, object] = {}
        for key, value in d.items():
            if isinstance(value, dict):
                sanitized[key] = sanitize_dict(cast(dict[str, object], value))
            else:
                key_lower = key.lower()
                if key_lower in safe_fields:
                    sanitized[key] = value
                elif any(re.search(pattern, key_lower) for pattern in sensitive_patterns):
                    sanitized[key] = "[REDACTED]"
                else:
                    sanitized[key] = value
        return sanitized

    return cast(EventDict, sanitize_dict(cast(dict[str, object], dict(event_dict))))


def add_correlation_id(_logger: object, _name: str, event_dict: EventDict) -> EventDict:
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


def add_request_context(_logger: object, _name: str, event_dict: EventDict) -> EventDict:
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


def _database_error_type() -> type[BaseException]:
    try:
        from server.exceptions import DatabaseError as imported

        return imported
    except ImportError:
        return Exception


def _enhance_one_player_id(event_dict: EventDict, key: str, value: str, get_player: object) -> None:
    if len(value) != 36 or value.count("-") != 4:
        return
    err_t = _database_error_type()
    try:
        player = get_player(uuid.UUID(value))  # type: ignore[operator]
        player_name = getattr(player, "name", None) if player is not None else None
        if player_name is not None:
            event_dict[key] = f"<{player_name}>: {value}"
    except (AttributeError, KeyError, TypeError, ValueError, err_t, RecursionError):
        pass


def enhance_player_ids(_logger: object, _name: str, event_dict: EventDict) -> EventDict:
    """Enhance player_id fields with display names when available."""
    player_service = _player_service_holder.player_service
    if _enhancing_player_ids.active:
        return event_dict
    _enhancing_player_ids.active = True
    try:
        persistence = cast(object | None, getattr(player_service, "persistence", None)) if player_service else None
        get_player = cast(object | None, getattr(persistence, "get_player", None)) if persistence is not None else None
        if callable(get_player):
            for key, value in cast(dict[str, object], event_dict).items():
                if key == "player_id" and isinstance(value, str):
                    _enhance_one_player_id(event_dict, key, value, get_player)
    finally:
        _enhancing_player_ids.active = False
    return event_dict
