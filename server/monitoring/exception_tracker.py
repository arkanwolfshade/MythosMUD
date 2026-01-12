"""
Comprehensive exception tracking system for MythosMUD server.

This module provides 100% exception tracking with full context information,
enabling comprehensive error monitoring and debugging capabilities.

As noted in the Pnakotic Manuscripts, understanding the nature and patterns
of anomalies is essential for maintaining the stability of our systems.
"""

import traceback
import uuid
from collections import defaultdict
from collections.abc import Callable
from dataclasses import dataclass, field
from datetime import UTC, datetime
from typing import Any

from server.structured_logging.enhanced_logging_config import get_logger, log_with_context
from server.utils.enhanced_error_logging import create_enhanced_error_context

logger = get_logger(__name__)


@dataclass
class ExceptionRecord:  # pylint: disable=too-many-instance-attributes  # Reason: Exception record requires many fields to capture complete exception context
    """Represents a tracked exception with full context."""

    exception_id: str
    exception_type: str
    exception_message: str
    timestamp: datetime
    traceback: str
    context: dict[str, Any] = field(default_factory=dict)
    user_id: str | None = None
    session_id: str | None = None
    correlation_id: str | None = None
    request_id: str | None = None
    severity: str = "error"
    handled: bool = False
    metadata: dict[str, Any] = field(default_factory=dict)


@dataclass
class ExceptionStats:
    """Statistics for exception tracking."""

    total_exceptions: int
    exceptions_by_type: dict[str, int]
    exceptions_by_hour: dict[str, int]
    exceptions_by_user: dict[str, int]
    unhandled_exceptions: int
    critical_exceptions: int
    error_rate: float


class ExceptionTracker:
    """
    Comprehensive exception tracking system.

    This class provides 100% exception tracking with full context information,
    enabling comprehensive error monitoring and debugging capabilities.
    """

    def __init__(self, max_records: int = 10000):
        """
        Initialize the exception tracker.

        Args:
            max_records: Maximum number of exception records to keep in memory
        """
        self.max_records = max_records
        self.exception_records: list[ExceptionRecord] = []
        self.exception_stats = ExceptionStats(
            total_exceptions=0,
            exceptions_by_type=defaultdict(int),
            exceptions_by_hour=defaultdict(int),
            exceptions_by_user=defaultdict(int),
            unhandled_exceptions=0,
            critical_exceptions=0,
            error_rate=0.0,
        )

        # Exception handlers
        self.exception_handlers: dict[type[Exception], list[Callable]] = defaultdict(list)
        self.global_handlers: list[Callable] = []

        logger.info("Exception tracker initialized", max_records=max_records)

    def track_exception(  # pylint: disable=too-many-arguments,too-many-positional-arguments  # Reason: Exception tracking requires many parameters for complete exception context
        self,
        exception: Exception,
        context: dict[str, Any] | None = None,
        user_id: str | None = None,
        session_id: str | None = None,
        correlation_id: str | None = None,
        request_id: str | None = None,
        severity: str = "error",
        handled: bool = False,
        metadata: dict[str, Any] | None = None,
    ) -> str:
        """
        Track an exception with full context information.

        Args:
            exception: The exception to track
            context: Additional context information
            user_id: User ID if available
            session_id: Session ID if available
            correlation_id: Correlation ID for request tracing
            request_id: Request ID if available
            severity: Severity level (debug, info, warning, error, critical)
            handled: Whether the exception was handled
            metadata: Additional metadata

        Returns:
            Unique exception ID
        """
        exception_id = str(uuid.uuid4())

        if context is None:
            context = {}
        if metadata is None:
            metadata = {}

        # Create exception record
        record = ExceptionRecord(
            exception_id=exception_id,
            exception_type=type(exception).__name__,
            exception_message=str(exception),
            timestamp=datetime.now(UTC),
            traceback=traceback.format_exc(),
            context=context,
            user_id=user_id,
            session_id=session_id,
            correlation_id=correlation_id,
            request_id=request_id,
            severity=severity,
            handled=handled,
            metadata=metadata,
        )

        # Store the record
        self.exception_records.append(record)

        # Maintain max records limit
        if len(self.exception_records) > self.max_records:
            self.exception_records = self.exception_records[-self.max_records :]

        # Update statistics
        self._update_stats(record)

        # Log the exception with full context
        log_with_context(
            logger,
            severity,
            f"Exception tracked: {type(exception).__name__}",
            exception_id=exception_id,
            exception_type=type(exception).__name__,
            exception_message=str(exception),
            user_id=user_id,
            session_id=session_id,
            correlation_id=correlation_id,
            request_id=request_id,
            severity=severity,
            handled=handled,
            context=context,
            metadata=metadata,
            traceback=traceback.format_exc(),
        )

        # Call exception handlers
        self._call_handlers(exception, record)

        return exception_id

    def get_exception_record(self, exception_id: str) -> ExceptionRecord | None:
        """
        Get an exception record by ID.

        Args:
            exception_id: Unique exception ID

        Returns:
            Exception record or None if not found
        """
        for record in self.exception_records:
            if record.exception_id == exception_id:
                return record
        return None

    def get_exceptions_by_type(self, exception_type: str) -> list[ExceptionRecord]:
        """
        Get all exceptions of a specific type.

        Args:
            exception_type: Exception type name

        Returns:
            List of exception records
        """
        return [r for r in self.exception_records if r.exception_type == exception_type]

    def get_exceptions_by_user(self, user_id: str) -> list[ExceptionRecord]:
        """
        Get all exceptions for a specific user.

        Args:
            user_id: User ID

        Returns:
            List of exception records
        """
        return [r for r in self.exception_records if r.user_id == user_id]

    def get_exceptions_by_correlation(self, correlation_id: str) -> list[ExceptionRecord]:
        """
        Get all exceptions for a specific correlation ID.

        Args:
            correlation_id: Correlation ID

        Returns:
            List of exception records
        """
        return [r for r in self.exception_records if r.correlation_id == correlation_id]

    def get_unhandled_exceptions(self) -> list[ExceptionRecord]:
        """
        Get all unhandled exceptions.

        Returns:
            List of unhandled exception records
        """
        return [r for r in self.exception_records if not r.handled]

    def get_critical_exceptions(self) -> list[ExceptionRecord]:
        """
        Get all critical exceptions.

        Returns:
            List of critical exception records
        """
        return [r for r in self.exception_records if r.severity == "critical"]

    def get_recent_exceptions(self, count: int = 100) -> list[ExceptionRecord]:
        """
        Get the most recent exceptions.

        Args:
            count: Number of recent exceptions to return

        Returns:
            List of recent exception records
        """
        return self.exception_records[-count:]

    def get_stats(self) -> ExceptionStats:
        """
        Get exception tracking statistics.

        Returns:
            Current exception statistics
        """
        return self.exception_stats

    def add_exception_handler(self, exception_type: type[Exception], handler: Callable) -> None:
        """
        Add an exception handler for a specific exception type.

        Args:
            exception_type: Exception type to handle
            handler: Handler function
        """
        self.exception_handlers[exception_type].append(handler)

    def add_global_exception_handler(self, handler: Callable) -> None:
        """
        Add a global exception handler for all exceptions.

        Args:
            handler: Global handler function
        """
        self.global_handlers.append(handler)

    def reset_records(self) -> None:
        """Reset all exception records."""
        self.exception_records.clear()
        self.exception_stats = ExceptionStats(
            total_exceptions=0,
            exceptions_by_type=defaultdict(int),
            exceptions_by_hour=defaultdict(int),
            exceptions_by_user=defaultdict(int),
            unhandled_exceptions=0,
            critical_exceptions=0,
            error_rate=0.0,
        )

        logger.info("Exception records reset")

    def _update_stats(self, record: ExceptionRecord) -> None:
        """Update exception statistics."""
        self.exception_stats.total_exceptions += 1
        self.exception_stats.exceptions_by_type[record.exception_type] += 1

        # Group by hour
        hour_key = record.timestamp.strftime("%Y-%m-%d %H:00")
        self.exception_stats.exceptions_by_hour[hour_key] += 1

        # Group by user
        if record.user_id:
            self.exception_stats.exceptions_by_user[record.user_id] += 1

        # Count unhandled exceptions
        if not record.handled:
            self.exception_stats.unhandled_exceptions += 1

        # Count critical exceptions
        if record.severity == "critical":
            self.exception_stats.critical_exceptions += 1

        # Calculate error rate (simplified)
        if self.exception_stats.total_exceptions > 0:
            self.exception_stats.error_rate = (
                self.exception_stats.unhandled_exceptions / self.exception_stats.total_exceptions * 100
            )

    def _call_handlers(self, exception: Exception, record: ExceptionRecord) -> None:
        """Call exception handlers."""
        # Call type-specific handlers
        exception_type = type(exception)
        for handler in self.exception_handlers[exception_type]:
            try:
                handler(exception, record)
            except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Handler errors unpredictable, must not fail exception tracking
                logger.error("Exception handler failed", handler=str(handler), error=str(e), exc_info=True)

        # Call global handlers
        for handler in self.global_handlers:
            try:
                handler(exception, record)
            except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Handler errors unpredictable, must not fail exception tracking
                logger.error("Global exception handler failed", handler=str(handler), error=str(e), exc_info=True)


# Global exception tracker instance
_exception_tracker: ExceptionTracker | None = None  # pylint: disable=invalid-name  # Reason: Private module-level singleton, intentionally uses _ prefix


def get_exception_tracker() -> ExceptionTracker:
    """
    Get the global exception tracker instance.

    Returns:
        Global ExceptionTracker instance
    """
    global _exception_tracker  # pylint: disable=global-statement  # Reason: Singleton pattern for exception tracking
    if _exception_tracker is None:
        _exception_tracker = ExceptionTracker()
    return _exception_tracker


def track_exception(  # pylint: disable=too-many-arguments,too-many-positional-arguments  # Reason: Exception tracking requires many parameters for complete exception context
    exception: Exception,
    context: dict[str, Any] | None = None,
    user_id: str | None = None,
    session_id: str | None = None,
    correlation_id: str | None = None,
    request_id: str | None = None,
    severity: str = "error",
    handled: bool = False,
    metadata: dict[str, Any] | None = None,
    tracker: ExceptionTracker | None = None,
) -> str:
    """
    Track an exception with full context information.

    Args:
        exception: The exception to track
        context: Additional context information
        user_id: User ID if available
        session_id: Session ID if available
        correlation_id: Correlation ID for request tracing
        request_id: Request ID if available
        severity: Severity level (debug, info, warning, error, critical)
        handled: Whether the exception was handled
        metadata: Additional metadata
        tracker: Exception tracker instance (uses global if None)

    Returns:
        Unique exception ID
    """
    if tracker is None:
        tracker = get_exception_tracker()

    return tracker.track_exception(
        exception=exception,
        context=context,
        user_id=user_id,
        session_id=session_id,
        correlation_id=correlation_id,
        request_id=request_id,
        severity=severity,
        handled=handled,
        metadata=metadata,
    )


def track_exception_with_context(  # pylint: disable=too-many-arguments,too-many-positional-arguments  # Reason: Exception tracking requires many parameters for complete exception context
    exception: Exception,
    request=None,
    websocket=None,
    user_id: str | None = None,
    session_id: str | None = None,
    severity: str = "error",
    handled: bool = False,
    metadata: dict[str, Any] | None = None,
    tracker: ExceptionTracker | None = None,
) -> str:
    """
    Track an exception with enhanced context from request/websocket.

    Args:
        exception: The exception to track
        request: FastAPI request object
        websocket: WebSocket connection
        user_id: User ID if available
        session_id: Session ID if available
        severity: Severity level (debug, info, warning, error, critical)
        handled: Whether the exception was handled
        metadata: Additional metadata
        tracker: Exception tracker instance (uses global if None)

    Returns:
        Unique exception ID
    """
    if tracker is None:
        tracker = get_exception_tracker()

    # Create enhanced context
    context = create_enhanced_error_context(
        request=request, websocket=websocket, user_id=user_id, session_id=session_id, **(metadata or {})
    )

    # Extract correlation and request IDs
    correlation_id: str | None = getattr(context, "correlation_id", None)
    request_id: str | None = getattr(context, "request_id", None)

    return tracker.track_exception(
        exception=exception,
        context=context.to_dict() if hasattr(context, "to_dict") else {},
        user_id=user_id,
        session_id=session_id,
        correlation_id=correlation_id,
        request_id=request_id,
        severity=severity,
        handled=handled,
        metadata=metadata or {},
    )
