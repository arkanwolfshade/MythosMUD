"""
Logging handlers for file-based logging with rotation and Windows safety.

This module provides handler classes and utilities for creating and configuring
file-based logging handlers with proper rotation, Windows safety, and directory management.
"""

# pylint: disable=too-few-public-methods  # Reason: Logging handler classes with focused responsibility, minimal public interface

import io
import logging
import sys
import types
from collections.abc import Callable
from logging.handlers import RotatingFileHandler
from pathlib import Path
from typing import Any, cast, override

from server.structured_logging.logging_utilities import (
    ensure_log_directory,
    load_player_guid_formatter_class,
)


class SafeRotatingFileHandler(RotatingFileHandler):
    """
    RotatingFileHandler that ensures directory exists before file operations.

    This handler wraps RotatingFileHandler to prevent FileNotFoundError
    when shouldRollover() is called from different threads in CI environments.
    """

    @override
    def _open(self) -> Any:  # noqa: N802  # Reason: Method name required by parent class logging.handlers.RotatingFileHandler, cannot change to follow PEP8 naming  # pyright: ignore[reportExplicitAny, reportAny]  # Reason: Return is TextIOWrapper from super or StringIO fallback; precise union is Liskov-incompatible with FileHandler stubs
        """
        Open the log file, ensuring directory exists first.

        This overrides the parent method to ensure the log directory exists
        before attempting to open the log file, preventing FileNotFoundError
        in CI environments where directories might be cleaned up.
        """
        if not self.baseFilename:
            return super()._open()

        log_path = Path(self.baseFilename)
        max_retries = 3

        for attempt in range(max_retries):
            # Ensure directory exists right before opening (handles race conditions)
            # This minimizes the window between directory creation and file opening
            ensure_log_directory(log_path)

            # Try to open the file - ensure directory exists again right before opening
            # to handle cases where directory is deleted between check and open
            try:
                # Double-check directory exists right before opening
                ensure_log_directory(log_path)
                return super()._open()
            except (FileNotFoundError, OSError):
                # Directory might have been deleted, will retry on next iteration
                if attempt == max_retries - 1:
                    # Final attempt failed - try one more time with directory creation
                    # This handles cases where directory is deleted between check and open
                    try:
                        ensure_log_directory(log_path)
                        # One more directory check right before opening
                        ensure_log_directory(log_path)
                        return super()._open()
                    except (FileNotFoundError, OSError):  # pylint: disable=try-except-raise  # Reason: Final fallback returns StringIO instead of raising to prevent infinite recursion in logging error handling
                        # If still failing after all retries, return a no-op StringIO as fallback
                        # This prevents infinite recursion when logging errors
                        # The logging system will handle this gracefully
                        # Using StringIO instead of sys.stderr to avoid "I/O operation on closed file" errors
                        return io.StringIO()
                # Continue to next retry attempt immediately (no sleep needed since
                # directory creation is thread-safe and retries are fast)
                continue

        # Should never reach here, but call parent as fallback
        return super()._open()

    @override
    def shouldRollover(self, record: logging.LogRecord) -> bool:  # noqa: N802  # Reason: Method name required by parent class logging.handlers.RotatingFileHandler, cannot change to follow PEP8 naming
        """
        Determine if rollover should occur, ensuring directory exists first.

        This overrides the parent method to ensure the log directory exists
        before attempting to open the log file, preventing race conditions
        in CI environments where directories might be cleaned up.

        Uses thread-safe directory creation to prevent deadlocks when multiple
        threads try to create the same directory simultaneously.
        """
        # Ensure directory exists before checking rollover (thread-safe)
        if not self.baseFilename:
            return False

        log_path = Path(self.baseFilename)
        max_retries = 3

        for attempt in range(max_retries):
            # Ensure directory exists before each attempt (handles race conditions)
            ensure_log_directory(log_path)

            # Call parent method to perform actual rollover check
            # Wrap in try-except to handle race conditions where directory might be deleted
            # between the check above and when parent tries to open the file
            try:
                return bool(super().shouldRollover(record))
            except (FileNotFoundError, OSError):
                # Directory might have been deleted, will retry on next iteration
                if attempt == max_retries - 1:
                    # Final attempt failed - return False (no rollover) rather than raising
                    # This prevents logging errors from breaking tests in CI environments
                    # where directories might be cleaned up during test execution
                    return False
                # Continue to next retry attempt
                continue

        # Should never reach here, but return False as safe fallback
        return False


class WarningOnlyFilter(logging.Filter):  # pylint: disable=too-few-public-methods  # Reason: Filter class with focused responsibility, minimal public interface
    """
    Filter that only allows WARNING level logs to pass through.

    This filter ensures that warnings.log only contains WARNING level logs,
    not ERROR or CRITICAL logs (which should only go to errors.log).
    """

    @override
    def filter(self, record: logging.LogRecord) -> bool:
        """Only allow WARNING level logs."""
        return record.levelno == logging.WARNING


def _make_exec_for_aggregator(win_base: type[RotatingFileHandler]) -> Callable[[dict[str, object]], None]:
    """Build types.new_class exec callback bound to the concrete Windows base class."""

    def _exec(ns: dict[str, object]) -> None:
        def shouldRollover(self: RotatingFileHandler, record: logging.LogRecord) -> bool:  # noqa: N802  # pylint: disable=invalid-name  # Reason: Method name required by parent class logging.handlers.RotatingFileHandler, cannot change to follow PEP8 naming
            if self.baseFilename:
                ensure_log_directory(Path(self.baseFilename))
            # Single superclass win_base; explicit call avoids super() typing on dynamic class.
            return bool(win_base.shouldRollover(self, record))

        ns["shouldRollover"] = shouldRollover
        ns["__doc__"] = "Windows-safe rotating file handler with directory safety for aggregator logs."

    return _exec


def _aggregator_handler_class_for_windows(win_base: type[RotatingFileHandler]) -> type[RotatingFileHandler]:
    """Subclass win_base with directory-safe rollover (no dynamic ``class X(base)`` for type checkers)."""
    created = types.new_class(
        "SafeWinHandlerAggregator",
        (win_base,),
        {},
        _make_exec_for_aggregator(win_base),
    )
    return cast(type[RotatingFileHandler], created)


def _resolve_aggregator_handler_class() -> type[RotatingFileHandler]:
    """Pick Windows-safe aggregator handler class when available."""
    win_safe: type[RotatingFileHandler] = RotatingFileHandler
    try:
        from server.structured_logging.windows_safe_rotation import (
            WindowsSafeRotatingFileHandler as imported_win_safe,
        )

        win_safe = imported_win_safe
    except ImportError:  # Optional enhancement - fallback to standard handler if not available
        win_safe = RotatingFileHandler

    try:
        if sys.platform == "win32":
            return _aggregator_handler_class_for_windows(win_safe)
    except ImportError:
        pass
    return SafeRotatingFileHandler


def _open_aggregator_handler(
    handler_class: type[RotatingFileHandler],
    log_path: Path,
    max_bytes: int,
    backup_count: int,
) -> RotatingFileHandler:
    """Create aggregator file handler, retrying once if the directory vanished."""
    ensure_log_directory(log_path)
    try:
        return handler_class(log_path, maxBytes=max_bytes, backupCount=backup_count, encoding="utf-8")
    except (FileNotFoundError, OSError):
        ensure_log_directory(log_path)
        return handler_class(log_path, maxBytes=max_bytes, backupCount=backup_count, encoding="utf-8")


def _aggregator_formatter(player_service: object | None) -> logging.Formatter:
    """Build aggregator formatter (PlayerGuidFormatter when service is available)."""
    # %(message)s only: structlog already embeds timestamp/name/level in the rendered message.
    if player_service is not None:
        player_guid_formatter = load_player_guid_formatter_class()
        return player_guid_formatter(player_service=player_service, fmt="%(message)s", datefmt=None)
    return logging.Formatter("%(message)s", datefmt=None)


def create_aggregator_handler(
    log_path: Path,
    log_level: int,
    max_bytes: int,
    backup_count: int,
    player_service: object | None = None,
) -> RotatingFileHandler:
    """
    Create an aggregator handler for warnings.log or errors.log.

    Aggregator handlers capture logs from ALL subsystems at a specific level
    (WARNING or ERROR) and write them to a centralized log file. This enables
    quick scanning of all warnings or errors across the entire system.

    Args:
        log_path: Path to the aggregator log file
        log_level: Logging level (logging.WARNING or logging.ERROR)
        max_bytes: Maximum file size before rotation
        backup_count: Number of backup files to keep
        player_service: Optional player service for GUID-to-name conversion

    Returns:
        Configured RotatingFileHandler instance
    """
    handler = _open_aggregator_handler(_resolve_aggregator_handler_class(), log_path, max_bytes, backup_count)
    handler.setLevel(log_level)
    if log_level == logging.WARNING:
        handler.addFilter(WarningOnlyFilter())
    handler.setFormatter(_aggregator_formatter(player_service))
    return handler
