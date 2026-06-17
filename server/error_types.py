"""
Centralized error types and constants for MythosMUD.

This module defines standardized error types and constants to ensure
consistent error handling across all application layers. As the Pnakotic
Manuscripts teach us, proper categorization is essential for understanding
and managing the eldritch forces we encounter.
"""

from collections.abc import Mapping
from enum import Enum
from typing import TypedDict, cast


class ErrorType(Enum):
    """Standardized error types for consistent categorization."""

    # Authentication and Authorization
    AUTHENTICATION_FAILED = "authentication_failed"
    AUTHORIZATION_DENIED = "authorization_denied"
    INVALID_TOKEN = "invalid_token"  # nosec B105: Error code string, not a password
    TOKEN_EXPIRED = "token_expired"  # nosec B105: Error code string, not a password

    # Validation Errors
    VALIDATION_ERROR = "validation_error"
    INVALID_INPUT = "invalid_input"
    MISSING_REQUIRED_FIELD = "missing_required_field"
    INVALID_FORMAT = "invalid_format"

    # Resource Errors
    RESOURCE_NOT_FOUND = "resource_not_found"
    RESOURCE_ALREADY_EXISTS = "resource_already_exists"
    RESOURCE_CONFLICT = "resource_conflict"

    # Game Logic Errors
    GAME_LOGIC_ERROR = "game_logic_error"
    INVALID_COMMAND = "invalid_command"
    INVALID_MOVEMENT = "invalid_movement"
    PLAYER_NOT_IN_ROOM = "player_not_in_room"

    # Database Errors
    DATABASE_ERROR = "database_error"
    DATABASE_CONNECTION_ERROR = "database_connection_error"
    DATABASE_QUERY_ERROR = "database_query_error"

    # Network and Communication
    NETWORK_ERROR = "network_error"
    CONNECTION_ERROR = "connection_error"
    TIMEOUT_ERROR = "timeout_error"

    # Rate Limiting
    RATE_LIMIT_EXCEEDED = "rate_limit_exceeded"
    TOO_MANY_REQUESTS = "too_many_requests"

    # Configuration and System
    CONFIGURATION_ERROR = "configuration_error"
    SYSTEM_ERROR = "system_error"
    INTERNAL_ERROR = "internal_error"

    # Real-time Communication
    WEBSOCKET_ERROR = "websocket_error"
    SSE_ERROR = "sse_error"  # Deprecated - kept for backward compatibility
    MESSAGE_PROCESSING_ERROR = "message_processing_error"


class ErrorSeverity(Enum):
    """Error severity levels for logging and handling."""

    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"


class ValidationFieldErrorDetail(TypedDict):
    """Single field validation error included in error response details."""

    field: str
    type: str
    message: str
    input: object


class ErrorContextDetail(TypedDict, total=False):
    """Request context included in error response details when available."""

    user_id: str | None
    session_id: str | None
    request_id: str | None


class ErrorResponseDetails(TypedDict, total=False):
    """Structured details attached to standardized error responses."""

    validation_errors: list[ValidationFieldErrorDetail]
    error_count: int
    model_class: str | None
    context: ErrorContextDetail
    fallback: bool


class StandardErrorPayload(TypedDict):
    """Nested error payload for HTTP standardized responses."""

    type: str
    message: str
    user_friendly: str
    details: ErrorResponseDetails
    severity: str
    timestamp: str


class HttpStandardErrorResponse(TypedDict):
    """HTTP standardized error response envelope."""

    error: StandardErrorPayload


class RealtimeErrorResponse(TypedDict):
    """WebSocket or SSE standardized error response."""

    type: str
    error_type: str
    message: str
    user_friendly: str
    details: ErrorResponseDetails


StandardizedErrorResponseDict = HttpStandardErrorResponse | RealtimeErrorResponse

ErrorResponseDetailsInput = ErrorResponseDetails | Mapping[str, object]


def _normalize_error_response_details(
    details: ErrorResponseDetailsInput | None,
) -> ErrorResponseDetails:
    """Coerce caller-provided detail mappings into the response TypedDict shape."""
    if details is None:
        return {}
    return cast(ErrorResponseDetails, dict(details))


def create_standard_error_response(
    error_type: ErrorType,
    message: str,
    user_friendly: str | None = None,
    details: ErrorResponseDetailsInput | None = None,
    severity: ErrorSeverity = ErrorSeverity.MEDIUM,
) -> HttpStandardErrorResponse:
    """
    Create a standardized error response.

    Args:
        error_type: The type of error
        message: Technical error message
        user_friendly: User-friendly error message (optional)
        details: Additional error details (optional)
        severity: Error severity level (optional)

    Returns:
        Standardized error response dictionary
    """
    from datetime import UTC, datetime

    normalized_details = _normalize_error_response_details(details)

    return {
        "error": {
            "type": error_type.value,
            "message": message,
            "user_friendly": user_friendly or message,
            "details": normalized_details,
            "severity": severity.value,
            "timestamp": datetime.now(UTC).isoformat(),
        }
    }


def create_websocket_error_response(
    error_type: ErrorType,
    message: str,
    user_friendly: str | None = None,
    details: ErrorResponseDetailsInput | None = None,
) -> RealtimeErrorResponse:
    """
    Create a standardized WebSocket error response.

    Args:
        error_type: The type of error
        message: Technical error message
        user_friendly: User-friendly error message (optional)
        details: Additional error details (optional)

    Returns:
        WebSocket error response dictionary
    """
    normalized_details = _normalize_error_response_details(details)

    return {
        "type": "error",
        "error_type": error_type.value,
        "message": message,
        "user_friendly": user_friendly or message,
        "details": normalized_details,
    }


def create_sse_error_response(
    error_type: ErrorType,
    message: str,
    user_friendly: str | None = None,
    details: ErrorResponseDetailsInput | None = None,
) -> RealtimeErrorResponse:
    """
    DEPRECATED: SSE connections are no longer supported.
    This function is kept for backward compatibility but returns the same format as WebSocket errors.

    Args:
        error_type: The type of error
        message: Technical error message
        user_friendly: User-friendly error message (optional)
        details: Additional error details (optional)

    Returns:
        Error response dictionary (same format as WebSocket errors)
    """
    normalized_details = _normalize_error_response_details(details)

    return {
        "type": "error",
        "error_type": error_type.value,
        "message": message,
        "user_friendly": user_friendly or message,
        "details": normalized_details,
    }


# Common error messages for consistency
class ErrorMessages:  # pylint: disable=too-few-public-methods  # Reason: Utility class with class-level constants, no instance methods needed
    """Common error messages for consistent user experience."""

    # Authentication
    AUTHENTICATION_REQUIRED = "Authentication required"
    INVALID_CREDENTIALS = "Invalid username or password"
    TOKEN_EXPIRED = "Your session has expired. Please log in again."  # nosec B105: Error message string, not a password

    # Validation
    INVALID_INPUT = "Invalid input provided"
    MISSING_REQUIRED_FIELD = "Required field is missing"
    INVALID_FORMAT = "Invalid format provided"

    # Resources
    RESOURCE_NOT_FOUND = "Resource not found"
    PLAYER_NOT_FOUND = "Player not found"
    ROOM_NOT_FOUND = "Room not found"
    USER_NOT_FOUND = "User not found"
    PROFESSION_NOT_FOUND = "Profession not found"

    # Game Logic
    INVALID_COMMAND = "Invalid command"
    INVALID_MOVEMENT = "You cannot move in that direction"
    PLAYER_NOT_IN_ROOM = "Player is not in the specified room"

    # Network
    CONNECTION_ERROR = "Connection error occurred"
    TIMEOUT_ERROR = "Request timed out"

    # System
    INTERNAL_ERROR = "An internal error occurred"
    SYSTEM_UNAVAILABLE = "System temporarily unavailable"
    TOO_MANY_REQUESTS = "Too many requests. Please try again later."

    # Real-time
    WEBSOCKET_ERROR = "WebSocket connection error"
    SSE_ERROR = "Server-Sent Events connection error"  # Deprecated - kept for backward compatibility
    MESSAGE_PROCESSING_ERROR = "Error processing message"
    RATE_LIMIT_EXCEEDED = "Rate limit exceeded. Please slow down your requests."
