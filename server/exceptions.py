"""
Comprehensive exception handling for MythosMUD server.

This module defines the exception hierarchy and error handling utilities
for the MythosMUD system. As the Pnakotic Manuscripts teach us, proper
categorization of knowledge - including errors - is essential for its
preservation and understanding.
"""

import traceback
from dataclasses import dataclass, field
from datetime import datetime
from typing import Any

from .logging_config import get_logger

logger = get_logger(__name__)


@dataclass
class ErrorContext:
    """
    Contextual information for error handling.

    Provides structured context for error reporting and debugging,
    following the dimensional mapping principles described in the
    restricted archives.
    """

    user_id: str | None = None
    room_id: str | None = None
    command: str | None = None
    session_id: str | None = None
    request_id: str | None = None
    timestamp: datetime = field(default_factory=datetime.now)
    metadata: dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> dict[str, Any]:
        """Convert context to dictionary for logging."""
        return {
            "user_id": self.user_id,
            "room_id": self.room_id,
            "command": self.command,
            "session_id": self.session_id,
            "request_id": self.request_id,
            "timestamp": self.timestamp.isoformat(),
            "metadata": self.metadata,
        }


class MythosMUDError(Exception):
    """
    Base exception for all MythosMUD errors.

    Provides structured error handling with context and metadata
    for proper error categorization and debugging.
    """

    def __init__(
        self,
        message: str,
        context: ErrorContext | None = None,
        details: dict[str, Any] | None = None,
        user_friendly: str | None = None,
    ):
        """
        Initialize MythosMUD error.

        Args:
            message: Technical error message
            context: Error context information
            details: Additional error details
            user_friendly: User-friendly error message
        """
        super().__init__(message)
        self.message = message
        self.context = context or ErrorContext()
        self.details = details or {}
        self.user_friendly = user_friendly or message
        self.timestamp = datetime.now()

        # Log the error with context
        self._log_error()

    def _log_error(self):
        """Log the error with structured context."""
        log_data = {
            "error_type": self.__class__.__name__,
            "message": self.message,
            "context": self.context.to_dict(),
            "details": self.details,
            "timestamp": self.timestamp.isoformat(),
        }
        logger.error("MythosMUD error occurred", **log_data)

    def to_dict(self) -> dict[str, Any]:
        """Convert error to dictionary for API responses."""
        return {
            "error_type": self.__class__.__name__,
            "message": self.message,
            "user_friendly": self.user_friendly,
            "context": self.context.to_dict(),
            "details": self.details,
            "timestamp": self.timestamp.isoformat(),
        }


class AuthenticationError(MythosMUDError):
    """Authentication and authorization errors."""

    def __init__(self, message: str, context: ErrorContext | None = None, auth_type: str = "unknown", **kwargs):
        super().__init__(message, context, **kwargs)
        self.auth_type = auth_type
        self.details["auth_type"] = auth_type


class DatabaseError(MythosMUDError):
    """Database operation errors."""

    def __init__(
        self,
        message: str,
        context: ErrorContext | None = None,
        operation: str = "unknown",
        table: str | None = None,
        **kwargs,
    ):
        super().__init__(message, context, **kwargs)
        self.operation = operation
        self.table = table
        self.details["operation"] = operation
        if table:
            self.details["table"] = table


class ValidationError(MythosMUDError):
    """Data validation errors."""

    def __init__(
        self,
        message: str,
        context: ErrorContext | None = None,
        field: str | None = None,
        value: Any | None = None,
        **kwargs,
    ):
        super().__init__(message, context, **kwargs)
        self.field = field
        self.value = value
        if field:
            self.details["field"] = field
        if value is not None:
            self.details["value"] = str(value)


class GameLogicError(MythosMUDError):
    """Game mechanics and logic errors."""

    def __init__(self, message: str, context: ErrorContext | None = None, game_action: str | None = None, **kwargs):
        super().__init__(message, context, **kwargs)
        self.game_action = game_action
        if game_action:
            self.details["game_action"] = game_action


class ConfigurationError(MythosMUDError):
    """Configuration and setup errors."""

    def __init__(self, message: str, context: ErrorContext | None = None, config_key: str | None = None, **kwargs):
        super().__init__(message, context, **kwargs)
        self.config_key = config_key
        if config_key:
            self.details["config_key"] = config_key


class NetworkError(MythosMUDError):
    """Network and communication errors."""

    def __init__(self, message: str, context: ErrorContext | None = None, connection_type: str = "unknown", **kwargs):
        super().__init__(message, context, **kwargs)
        self.connection_type = connection_type
        self.details["connection_type"] = connection_type


class ResourceNotFoundError(MythosMUDError):
    """Resource not found errors."""

    def __init__(
        self,
        message: str,
        context: ErrorContext | None = None,
        resource_type: str | None = None,
        resource_id: str | None = None,
        **kwargs,
    ):
        super().__init__(message, context, **kwargs)
        self.resource_type = resource_type
        self.resource_id = resource_id
        if resource_type:
            self.details["resource_type"] = resource_type
        if resource_id:
            self.details["resource_id"] = resource_id


class RateLimitError(MythosMUDError):
    """Rate limiting errors."""

    def __init__(
        self,
        message: str,
        context: ErrorContext | None = None,
        limit_type: str = "unknown",
        retry_after: int | None = None,
        **kwargs,
    ):
        super().__init__(message, context, **kwargs)
        self.limit_type = limit_type
        self.retry_after = retry_after
        self.details["limit_type"] = limit_type
        if retry_after:
            self.details["retry_after"] = retry_after


def create_error_context(**kwargs) -> ErrorContext:
    """
    Create an error context with the given parameters.

    Args:
        **kwargs: Context parameters

    Returns:
        ErrorContext object
    """
    return ErrorContext(**kwargs)


def handle_exception(exc: Exception, context: ErrorContext | None = None) -> MythosMUDError:
    """
    Convert a generic exception to a MythosMUD error.

    Args:
        exc: The original exception
        context: Error context

    Returns:
        MythosMUDError instance
    """
    if isinstance(exc, MythosMUDError):
        return exc

    # Convert common exceptions to MythosMUD errors
    if isinstance(exc, ValueError | TypeError):
        return ValidationError(str(exc), context, details={"original_type": type(exc).__name__})
    elif isinstance(exc, FileNotFoundError):
        return ResourceNotFoundError(str(exc), context, details={"original_type": type(exc).__name__})
    elif isinstance(exc, ConnectionError | TimeoutError):
        return NetworkError(str(exc), context, details={"original_type": type(exc).__name__})
    elif isinstance(exc, OSError):
        # OSError is a parent of FileNotFoundError, so check it after FileNotFoundError
        return ResourceNotFoundError(str(exc), context, details={"original_type": type(exc).__name__})
    else:
        # Generic error for unknown exceptions
        return MythosMUDError(
            str(exc), context, details={"original_type": type(exc).__name__, "traceback": traceback.format_exc()}
        )
