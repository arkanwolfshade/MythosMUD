"""
Logging handlers for file-based logging with rotation and Windows safety.

This module provides handler classes and utilities for creating and configuring
file-based logging handlers with proper rotation, Windows safety, and directory management.
"""

import io
import logging
import sys
from logging.handlers import RotatingFileHandler
from pathlib import Path
from typing import Any

from server.logging.logging_utilities import ensure_log_directory


class SafeRotatingFileHandler(RotatingFileHandler):
    """
    RotatingFileHandler that ensures directory exists before file operations.

    This handler wraps RotatingFileHandler to prevent FileNotFoundError
    when shouldRollover() is called from different threads in CI environments.
    """

    def _open(self):  # noqa: N802
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
                    except (FileNotFoundError, OSError):  # pylint: disable=try-except-raise
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

    def shouldRollover(self, record):  # noqa: N802
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
                return super().shouldRollover(record)
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


class WarningOnlyFilter(logging.Filter):
    """
    Filter that only allows WARNING level logs to pass through.

    This filter ensures that warnings.log only contains WARNING level logs,
    not ERROR or CRITICAL logs (which should only go to errors.log).
    """

    def filter(self, record: logging.LogRecord) -> bool:
        """Only allow WARNING level logs."""
        return record.levelno == logging.WARNING


def create_aggregator_handler(
    log_path: Path,
    log_level: int,
    max_bytes: int,
    backup_count: int,
    player_service: Any = None,
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
    # Use Windows-safe rotation handlers when available
    _WinSafeHandler: type[RotatingFileHandler] = RotatingFileHandler
    try:
        from server.logging.windows_safe_rotation import WindowsSafeRotatingFileHandler as _ImportedWinSafeHandler

        _WinSafeHandler = _ImportedWinSafeHandler
    except ImportError:  # Optional enhancement - fallback to standard handler if not available
        _WinSafeHandler = RotatingFileHandler

    # Use SafeRotatingFileHandler as base for all handlers
    _BaseHandler = SafeRotatingFileHandler

    # Determine handler class with Windows safety
    handler_class = _BaseHandler
    try:
        if sys.platform == "win32":
            # Windows-safe handler also needs directory safety
            class SafeWinHandlerAggregator(_WinSafeHandler):  # type: ignore[misc, valid-type]
                def shouldRollover(self, record):  # noqa: N802
                    if self.baseFilename:
                        log_path = Path(self.baseFilename)
                        ensure_log_directory(log_path)
                    return super().shouldRollover(record)

            handler_class = SafeWinHandlerAggregator
    except ImportError:
        # Fallback to safe handler on any detection error
        handler_class = _BaseHandler

    # Ensure directory exists right before creating handler to prevent race conditions
    ensure_log_directory(log_path)
    try:
        handler = handler_class(
            log_path,
            maxBytes=max_bytes,
            backupCount=backup_count,
            encoding="utf-8",
        )
    except (FileNotFoundError, OSError):
        # If directory doesn't exist or was deleted, recreate it and try again
        ensure_log_directory(log_path)
        handler = handler_class(
            log_path,
            maxBytes=max_bytes,
            backupCount=backup_count,
            encoding="utf-8",
        )

    handler.setLevel(log_level)

    # Add filter for warnings handler to exclude ERROR and CRITICAL
    # Warnings.log should ONLY contain WARNING level logs
    if log_level == logging.WARNING:
        handler.addFilter(WarningOnlyFilter())

    # Create formatter - use PlayerGuidFormatter if player_service is available
    formatter: logging.Formatter
    if player_service is not None:
        from server.logging.player_guid_formatter import PlayerGuidFormatter

        formatter = PlayerGuidFormatter(
            player_service=player_service,
            fmt="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
        )
    else:
        formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
        )
    handler.setFormatter(formatter)

    return handler
