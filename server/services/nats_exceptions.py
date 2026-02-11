"""
NATS-specific exception hierarchy for standardized error handling.

This module provides a structured exception hierarchy for NATS operations,
enabling better error handling and debugging throughout the application.

AI: Custom exceptions provide context and enable precise error handling.
"""


class NATSError(Exception):
    """Base exception for all NATS-related errors."""


class NATSConnectionError(NATSError):
    """Raised when NATS connection operations fail."""

    def __init__(self, message: str, url: str | None = None, error: Exception | None = None) -> None:
        super().__init__(message)
        self.url = url
        self.original_error = error


class NATSPublishError(NATSError):
    """Raised when message publishing fails."""

    def __init__(self, message: str, subject: str | None = None, error: Exception | None = None) -> None:
        super().__init__(message)
        self.subject = subject
        self.original_error = error


class NATSSubscribeError(NATSError):
    """Raised when subscription operations fail."""

    def __init__(self, message: str, subject: str | None = None, error: Exception | None = None) -> None:
        super().__init__(message)
        self.subject = subject
        self.original_error = error


class NATSHealthCheckError(NATSError):
    """Raised when health check operations fail."""

    def __init__(self, message: str, consecutive_failures: int = 0) -> None:
        super().__init__(message)
        self.consecutive_failures = consecutive_failures


class NATSUnsubscribeError(NATSError):
    """Raised when unsubscribe operations fail."""

    def __init__(self, message: str, subject: str | None = None, error: Exception | None = None) -> None:
        super().__init__(message)
        self.subject = subject
        self.original_error = error


class NATSRequestError(NATSError):
    """Raised when request/response operations fail."""

    def __init__(
        self, message: str, subject: str | None = None, timeout: float | None = None, error: Exception | None = None
    ) -> None:
        super().__init__(message)
        self.subject = subject
        self.timeout = timeout
        self.original_error = error
