"""
Sanitization helpers for legacy MythosMUD error responses.

Extracted from legacy_error_handlers to keep file size within quality thresholds
while preserving identical redaction and XSS-prevention behavior.
"""

from typing import cast

import bleach

from .exceptions import ErrorContext


def is_safe_detail_key(key: str) -> bool:
    """
    Check if a detail key is safe to expose to users.

    Args:
        key: The detail key to check

    Returns:
        True if the key is safe to expose, False otherwise
    """
    # Safe keys that don't expose sensitive information
    safe_keys = {
        "auth_type",
        "operation",
        "table",
        "field",
        "value",
        "game_action",
        "config_key",
        "connection_type",
        "resource_type",
        "resource_id",
        "limit_type",
        "retry_after",
    }

    # Block keys that might contain sensitive information
    unsafe_patterns = [
        "password",
        "secret",
        "key",
        "token",
        "credential",
        "path",
        "file",
        "sql",
        "query",
        "stack",
        "trace",
        "internal",
        "debug",
        "sensitive",
        "private",
    ]

    key_lower = key.lower()

    # Check if key is explicitly safe
    if key in safe_keys:
        return True

    # Check if key contains unsafe patterns
    for pattern in unsafe_patterns:
        if pattern in key_lower:
            return False

    return True


_DETAIL_VALUE_MAX_LENGTH = 100
_SENSITIVE_DETAIL_PATTERNS = ("traceback", "stack", "file:", "line:", "/", "\\")


def _contains_sensitive_detail_pattern(value: str) -> bool:
    """Return True when a string resembles internal error or path disclosure."""
    value_lower = value.lower()
    return any(pattern in value_lower for pattern in _SENSITIVE_DETAIL_PATTERNS)


def _truncate_detail_string(value: str, max_length: int = _DETAIL_VALUE_MAX_LENGTH) -> str:
    """Limit detail string length to prevent information disclosure."""
    if len(value) <= max_length:
        return value
    return value[:max_length] + "..."


def _sanitize_detail_string(value: str) -> str:
    """Sanitize a string detail value with bleach and redaction rules."""
    if _contains_sensitive_detail_pattern(value):
        return "[REDACTED]"

    # Use bleach to sanitize any HTML content
    # This prevents XSS if error messages contain HTML
    sanitized = bleach.clean(
        value,
        tags=[],  # No HTML tags allowed
        attributes={},  # No attributes allowed
        strip=True,  # Strip all HTML
        strip_comments=True,  # Strip comments
    )
    return _truncate_detail_string(sanitized)


def _sanitize_detail_dict(value: dict[str, object]) -> dict[str, object]:
    """Sanitize dictionary detail values, keeping only safe keys."""
    return {k: sanitize_detail_value(v) for k, v in value.items() if is_safe_detail_key(k)}


def _sanitize_detail_list(value: list[object]) -> list[object]:
    """Sanitize each element in a list detail value."""
    return [sanitize_detail_value(v) for v in value]


def sanitize_safe_details(details: dict[str, object]) -> dict[str, object]:
    """Return detail dict entries that use safe keys with sanitized values."""
    safe_details: dict[str, object] = {}
    for key, value in details.items():
        if is_safe_detail_key(key):
            safe_details[key] = sanitize_detail_value(value)
    return safe_details


def sanitize_detail_value(value: object) -> object:
    """
    Sanitize a detail value to prevent information exposure.

    Uses bleach for HTML sanitization and custom logic for error-specific patterns.

    Args:
        value: The value to sanitize

    Returns:
        Sanitized value safe for user exposure
    """
    if isinstance(value, str):
        return _sanitize_detail_string(value)
    if isinstance(value, int | float | bool):
        return value
    if isinstance(value, dict):
        return _sanitize_detail_dict(cast(dict[str, object], value))
    if isinstance(value, list):
        return _sanitize_detail_list(cast(list[object], value))
    return _sanitize_detail_string(_truncate_detail_string(str(value)))


def _collect_safe_context_fields(context: ErrorContext) -> dict[str, object]:
    """Collect sanitized safe fields and timestamp from error context."""
    safe_field_values: dict[str, str | None] = {
        "user_id": context.user_id,
        "room_id": context.room_id,
        "command": context.command,
        "session_id": context.session_id,
        "request_id": context.request_id,
    }
    safe_context: dict[str, object] = {
        field: sanitize_detail_value(value) for field, value in safe_field_values.items() if value is not None
    }
    if context.timestamp:
        safe_context["timestamp"] = context.timestamp.isoformat()
    return safe_context


def _sanitize_context_metadata(metadata: dict[str, object] | None) -> dict[str, object] | None:
    """Sanitize context metadata, keeping only safe keys."""
    if not metadata:
        return None

    safe_metadata: dict[str, object] = {}
    for key, metadata_value in metadata.items():
        if is_safe_detail_key(key):
            safe_metadata[key] = sanitize_detail_value(metadata_value)
    return safe_metadata or None


def sanitize_context(context: ErrorContext | None) -> dict[str, object] | None:
    """
    Sanitize error context to prevent information exposure.

    Args:
        context: The error context to sanitize

    Returns:
        Sanitized context dict or None if no safe fields
    """
    if context is None:
        return None

    safe_context = _collect_safe_context_fields(context)

    safe_metadata = _sanitize_context_metadata(context.metadata)
    if safe_metadata:
        safe_context["metadata"] = safe_metadata

    return safe_context or None


def sanitize_html_content(content: str, allow_tags: list[str] | None = None) -> str:
    """
    Sanitize HTML content to prevent XSS attacks.

    This is a general utility function that can be used throughout the application
    for sanitizing user-provided HTML content.

    Args:
        content: The HTML content to sanitize
        allow_tags: List of allowed HTML tags (default: basic formatting only)

    Returns:
        Sanitized HTML content
    """
    if not content:
        return ""

    # Default safe tags for basic formatting
    if allow_tags is None:
        allow_tags = ["p", "br", "strong", "em", "u", "i", "b", "ul", "ol", "li", "h1", "h2", "h3", "h4", "h5", "h6"]

    # Default safe attributes
    safe_attributes = {
        "p": ["class"],
        "span": ["class"],
        "div": ["class"],
        "h1": ["class"],
        "h2": ["class"],
        "h3": ["class"],
        "h4": ["class"],
        "h5": ["class"],
        "h6": ["class"],
    }

    # Sanitize the content
    sanitized = bleach.clean(
        content,
        tags=allow_tags,
        attributes=safe_attributes,
        strip=True,
        strip_comments=True,
    )

    return str(sanitized)  # Explicit str for mypy no-any-return (bleach.clean returns str)


def sanitize_text_content(content: str, max_length: int = 1000) -> str:
    """
    Sanitize plain text content to prevent information exposure.

    Args:
        content: The text content to sanitize
        max_length: Maximum allowed length (default: 1000 characters)

    Returns:
        Sanitized text content
    """
    if not content:
        return ""

    # Remove any HTML tags
    sanitized = bleach.clean(content, tags=[], strip=True)

    # Limit length
    if len(sanitized) > max_length:
        sanitized = sanitized[:max_length] + "..."

    return str(sanitized)  # Explicit str for mypy no-any-return (bleach.clean returns str)


__all__ = [
    "is_safe_detail_key",
    "sanitize_context",
    "sanitize_detail_value",
    "sanitize_html_content",
    "sanitize_safe_details",
    "sanitize_text_content",
]
