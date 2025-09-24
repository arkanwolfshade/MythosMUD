"""
Centralized error types and constants for MythosMUD.

This module defines standardized error types and constants to ensure
consistent error handling across all application layers. As the Pnakotic
Manuscripts teach us, proper categorization is essential for understanding
and managing the eldritch forces we encounter.
"""

from enum import Enum
from typing import Any


class ErrorType(Enum):
    """Standardized error types for consistent categorization."""

    # Authentication and Authorization
    AUTHENTICATION_FAILED = "authentication_failed"
    AUTHORIZATION_DENIED = "authorization_denied"
    INVALID_TOKEN = "invalid_token"
    TOKEN_EXPIRED = "token_expired"

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
    SSE_ERROR = "sse_error"
    MESSAGE_PROCESSING_ERROR = "message_processing_error"


class ErrorSeverity(Enum):
    """Error severity levels for logging and handling."""

    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"


def create_standard_error_response(
    error_type: ErrorType,
    message: str,
    user_friendly: str | None = None,
    details: dict[str, Any] | None = None,
    severity: ErrorSeverity = ErrorSeverity.MEDIUM,
) -> dict[str, Any]:
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

    return {
        "error": {
            "type": error_type.value,
            "message": message,
            "user_friendly": user_friendly or message,
            "details": details or {},
            "severity": severity.value,
            "timestamp": datetime.now(UTC).isoformat(),
        }
    }


def create_websocket_error_response(
    error_type: ErrorType,
    message: str,
    user_friendly: str | None = None,
    details: dict[str, Any] | None = None,
) -> dict[str, Any]:
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
    return {
        "type": "error",
        "error_type": error_type.value,
        "message": message,
        "user_friendly": user_friendly or message,
        "details": details or {},
    }


def create_sse_error_response(
    error_type: ErrorType,
    message: str,
    user_friendly: str | None = None,
    details: dict[str, Any] | None = None,
) -> dict[str, Any]:
    """
    Create a standardized SSE error response.

    Args:
        error_type: The type of error
        message: Technical error message
        user_friendly: User-friendly error message (optional)
        details: Additional error details (optional)

    Returns:
        SSE error response dictionary
    """
    return {
        "type": "error",
        "error_type": error_type.value,
        "message": message,
        "user_friendly": user_friendly or message,
        "details": details or {},
    }


# Common error messages for consistency
class ErrorMessages:
    """Common error messages for consistent user experience."""

    # Authentication
    AUTHENTICATION_REQUIRED = "Authentication required"
    INVALID_CREDENTIALS = "Invalid username or password"
    TOKEN_EXPIRED = "Your session has expired. Please log in again."

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
    SSE_ERROR = "Server-Sent Events connection error"
    MESSAGE_PROCESSING_ERROR = "Error processing message"
