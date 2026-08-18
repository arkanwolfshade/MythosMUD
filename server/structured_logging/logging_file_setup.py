"""
File logging setup for enhanced logging system.

This module provides the setup function for configuring file-based logging handlers
with proper categorization, rotation, and Windows safety.
"""

# pylint: disable=too-few-public-methods,too-many-locals,too-many-statements  # Reason: File setup helpers have focused responsibility; setup uses many locals/statements for category, aggregator, console, and async wiring

import logging
import queue
import sys
import threading
from dataclasses import dataclass
from logging.handlers import QueueHandler, QueueListener, RotatingFileHandler
from pathlib import Path
from typing import cast, override

from server.structured_logging.logging_file_categories import (
    DEFAULT_LOG_CATEGORIES,
    LoggerNameFilter,
    add_handler_to_loggers,
    create_formatter,
    create_handler_for_category,
)
from server.structured_logging.logging_handlers import SafeRotatingFileHandler, create_aggregator_handler
from server.structured_logging.logging_utilities import (
    ensure_log_directory,
    resolve_log_base,
    rotate_log_files,
)

# Global queue and listener for async logging (initialized once)
# ponytail: 10k cap; Queue(-1) retained copied LogRecords through Windows rotation stalls (13GB soak).
LOG_QUEUE_MAXSIZE = 10000
_log_queue: queue.Queue[logging.LogRecord] | None = None  # pylint: disable=invalid-name  # Reason: Module-level singleton pattern uses underscore prefix to indicate private module variable, not a constant
_queue_listener: QueueListener | None = None  # pylint: disable=invalid-name  # Reason: Module-level singleton pattern uses underscore prefix to indicate private module variable, not a constant
_queue_listener_lock = threading.Lock()


class DropOldestQueueHandler(QueueHandler):
    """Enqueue LogRecords; if the queue is full, drop the oldest instead of growing."""

    def __init__(self, log_queue: queue.Queue[logging.LogRecord]) -> None:
        super().__init__(log_queue)
        self._bounded_queue: queue.Queue[logging.LogRecord] = log_queue

    @override
    def enqueue(self, record: logging.LogRecord) -> None:
        try:
            self._bounded_queue.put_nowait(record)
            return
        except queue.Full:
            pass
        try:
            _ = self._bounded_queue.get_nowait()
        except queue.Empty:
            pass
        try:
            self._bounded_queue.put_nowait(record)
        except queue.Full:
            pass


def _new_log_queue() -> queue.Queue[logging.LogRecord]:
    return queue.Queue(LOG_QUEUE_MAXSIZE)


def _get_or_create_log_queue() -> queue.Queue[logging.LogRecord]:
    """
    Get or create the global log queue for async logging.

    Returns:
        The global log queue for async log processing
    """
    global _log_queue  # pylint: disable=global-statement  # Reason: Global queue must be shared across all QueueHandlers

    with _queue_listener_lock:
        if _log_queue is None:
            _log_queue = _new_log_queue()
        return _log_queue


def get_queue_listener() -> QueueListener | None:
    """
    Return the global QueueListener if running (for tests and shutdown).

    Returns:
        The current QueueListener instance or None if async logging not started
    """
    with _queue_listener_lock:
        return _queue_listener


def stop_queue_listener() -> None:
    """
    Stop the global QueueListener and reset state (for tests and shutdown).

    Allows the next setup_enhanced_file_logging(enable_async=True) to create
    a fresh listener and queue.
    """
    global _queue_listener, _log_queue  # pylint: disable=global-statement  # Reason: Must reset module state for teardown
    with _queue_listener_lock:
        if _queue_listener is not None:
            try:
                _queue_listener.stop()
            except AttributeError:
                # QueueListener.stop() sets _thread to None; a second stop must not crash.
                pass
            _queue_listener = None
        _log_queue = None


@dataclass(frozen=True)
class _CategoryHandlerConfig:
    """Configuration for category handler setup (reduces parameter count)."""

    env_log_dir: Path
    handler_class: type[RotatingFileHandler]
    max_bytes: int
    backup_count: int
    player_service: object | None
    enable_async: bool
    log_queue: queue.Queue[logging.LogRecord] | None
    environment: str
    log_level: str


def _setup_category_handlers(
    log_categories: dict[str, list[str]],
    config: _CategoryHandlerConfig,
) -> list[logging.Handler]:
    """
    Set up handlers for log categories.

    Returns:
        List of file handlers created
    """
    all_file_handlers: list[logging.Handler] = []

    for log_file, prefixes in log_categories.items():
        log_path = config.env_log_dir / f"{log_file}.log"
        handler = create_handler_for_category(
            log_path,
            config.handler_class,
            config.max_bytes,
            config.backup_count,
            config.player_service,
        )

        # Add filter to the actual file handler to prevent cross-contamination
        # This is critical when async logging is enabled, because the QueueHandler
        # gets the filter, but the actual file handler also needs it since it
        # processes records from the queue
        handler.addFilter(LoggerNameFilter(prefixes))
        all_file_handlers.append(handler)

        # If async is enabled, do NOT add QueueHandlers to category loggers; only root
        # has a QueueHandler. Otherwise each record is enqueued once per matching
        # category logger and again from root, causing duplicate lines in aggregator files.
        if config.enable_async and config.log_queue:
            # Category handler is already in all_file_handlers; listener will dispatch to it.
            # Skip _add_handler_to_loggers so we do not add QueueHandlers to child loggers.
            pass
        else:
            add_handler_to_loggers(
                handler,
                prefixes,
                log_file,
                config.environment,
                config.log_level,
            )

    return all_file_handlers


def _setup_aggregator_handlers(  # pylint: disable=too-many-arguments,too-many-positional-arguments  # Reason: Aggregator handler setup requires 7 parameters for directory paths, handler configuration, async settings, and logger reference; extracting into a config object would reduce clarity
    env_log_dir: Path,
    max_bytes: int,
    backup_count: int,
    player_service: object | None,
    enable_async: bool,
    log_queue: queue.Queue[logging.LogRecord] | None,
    root_logger: logging.Logger,
) -> list[logging.Handler]:
    """
    Set up aggregator handlers (warnings.log and errors.log).

    Uses a single QueueHandler on root when async is enabled so each record
    is queued once; the listener dispatches to both warnings and errors
    file handlers. Also removes any existing QueueHandlers from root to
    avoid duplicate writes when setup runs multiple times in the same process.

    Returns:
        List of aggregator handlers created
    """
    all_file_handlers: list[logging.Handler] = []

    # Remove existing QueueHandlers from root to avoid duplicate log lines
    # when setup runs more than once (e.g. in tests or e2e).
    for h in root_logger.handlers[:]:
        if isinstance(h, QueueHandler):
            root_logger.removeHandler(h)

    # Create warnings.log aggregator handler
    warnings_log_path = env_log_dir / "warnings.log"
    warnings_handler = create_aggregator_handler(
        warnings_log_path,
        logging.WARNING,
        max_bytes,
        backup_count,
        player_service,
    )
    all_file_handlers.append(warnings_handler)
    if enable_async and log_queue:
        # Single QueueHandler so each record is queued once; listener
        # dispatches to both warnings_handler and errors_handler.
        root_logger.addHandler(DropOldestQueueHandler(log_queue))
    else:
        root_logger.addHandler(warnings_handler)

    # Create errors.log aggregator handler (file handler only; root already
    # has the single QueueHandler when async)
    errors_log_path = env_log_dir / "errors.log"
    errors_handler = create_aggregator_handler(
        errors_log_path,
        logging.ERROR,
        max_bytes,
        backup_count,
        player_service,
    )
    all_file_handlers.append(errors_handler)
    if not (enable_async and log_queue):
        root_logger.addHandler(errors_handler)

    return all_file_handlers


@dataclass(frozen=True)
class _ConsoleHandlerConfig:
    """Configuration for console handler setup (reduces parameter count)."""

    env_log_dir: Path
    max_bytes: int
    backup_count: int
    player_service: object | None
    log_level: str
    win_safe_handler: type[RotatingFileHandler]
    base_handler: type[RotatingFileHandler]
    enable_async: bool
    log_queue: queue.Queue[logging.LogRecord] | None
    root_logger: logging.Logger


def _setup_console_handler(
    config: _ConsoleHandlerConfig,
) -> logging.Handler:
    """
    Set up console handler with structured output.

    Returns:
        Console handler created
    """
    console_log_path = config.env_log_dir / "console.log"
    handler_class = _get_handler_class(config.win_safe_handler, config.base_handler)
    ensure_log_directory(console_log_path)
    try:
        console_handler = handler_class(
            console_log_path,
            maxBytes=config.max_bytes,
            backupCount=config.backup_count,
            encoding="utf-8",
        )
    except (FileNotFoundError, OSError):
        # If directory doesn't exist or was deleted, recreate it and try again
        ensure_log_directory(console_log_path)
        console_handler = handler_class(
            console_log_path,
            maxBytes=config.max_bytes,
            backupCount=config.backup_count,
            encoding="utf-8",
        )
    console_handler.setLevel(getattr(logging, str(config.log_level).upper(), logging.INFO))
    console_handler.setFormatter(create_formatter(config.player_service))
    # Async path: root already has a QueueHandler; the listener still writes console.log.
    if not (config.enable_async and config.log_queue):
        config.root_logger.addHandler(console_handler)
    return console_handler


def _setup_async_logging_queue(handlers: list[logging.Handler]) -> None:
    """
    Set up async logging queue listener for non-blocking file I/O.

    Uses QueueHandler/QueueListener pattern to offload file writing to a
    background thread, improving performance for high-throughput logging.
    Implements log batching by processing multiple log records in the queue
    before writing to disk, reducing I/O operations.

    Args:
        handlers: List of file handlers to process asynchronously
    """
    global _queue_listener, _log_queue  # pylint: disable=global-statement  # Reason: Global queue listener must be initialized once and kept alive

    with _queue_listener_lock:
        if _queue_listener is not None:
            # Queue listener already initialized
            return

        if _log_queue is None:
            _log_queue = _new_log_queue()

        try:
            # Create queue listener with all file handlers
            # The QueueListener automatically batches writes for better performance
            _queue_listener = QueueListener(_log_queue, *handlers, respect_handler_level=True)

            # Start the listener in a background thread
            _queue_listener.start()
        except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Defensive fallback for async logging setup failures, must catch all exceptions to prevent logging setup from failing completely
            # Graceful fallback: if async logging setup fails, log error and continue
            # Application will still work with synchronous logging
            print(
                f"Warning: Failed to set up async logging: {type(e).__name__}: {e}",
                file=sys.stderr,
            )
            # Reset global state so retry is possible
            _queue_listener = None


def _get_handler_class(
    win_safe_handler: type[RotatingFileHandler], base_handler: type[RotatingFileHandler]
) -> type[RotatingFileHandler]:
    """Get the appropriate handler class (Windows-safe or base)."""
    handler_class = base_handler
    try:
        if sys.platform == "win32":
            # Windows-safe handler also needs directory safety
            # Create a hybrid class that combines both features
            class SafeWinHandlerCategory(win_safe_handler):  # type: ignore[valid-type,misc]  # mypy: parameter as base class; pylint: disable=too-few-public-methods  # Reason: Handler class with focused responsibility, minimal public interface
                """Windows-safe rotating file handler with directory safety for categorized logs."""

                @override
                def shouldRollover(self, record: logging.LogRecord) -> bool:  # noqa: N802  # pylint: disable=invalid-name  # Reason: Overrides parent class method, must match parent signature
                    """Determine if log rollover should occur.

                    Args:
                        record: The log record to check

                    Returns:
                        bool: True if rollover should occur
                    """
                    if self.baseFilename:
                        log_path = Path(self.baseFilename)
                        ensure_log_directory(log_path)
                    return bool(super().shouldRollover(record))

            handler_class = SafeWinHandlerCategory
    except ImportError:
        # Fallback to safe handler on any detection error
        handler_class = base_handler  # pylint: disable=undefined-variable  # Reason: base_handler is a function parameter, not _BaseHandler
    return handler_class


def _convert_max_size_to_bytes(max_size_str: str | int) -> int:
    """Convert max_size string to bytes."""
    if isinstance(max_size_str, str):
        if max_size_str.endswith("MB"):
            return int(max_size_str[:-2]) * 1024 * 1024
        if max_size_str.endswith("KB"):
            return int(max_size_str[:-2]) * 1024
        if max_size_str.endswith("B"):
            return int(max_size_str[:-1])
        return int(max_size_str)
    return max_size_str


def _get_handler_classes() -> tuple[type[RotatingFileHandler], type[RotatingFileHandler]]:
    """Resolve Windows-safe and base handler classes for file logging."""
    win_safe: type[RotatingFileHandler] = RotatingFileHandler
    try:
        from server.structured_logging.windows_safe_rotation import (
            WindowsSafeRotatingFileHandler as _ImportedWinSafeHandler,
        )

        win_safe = _ImportedWinSafeHandler
    except ImportError:
        win_safe = RotatingFileHandler
    return (win_safe, SafeRotatingFileHandler)


def _rotation_subconfig(log_config: dict[str, object]) -> dict[str, object]:
    """Return rotation settings as dict[str, object] for typed .get() without Any."""
    raw = log_config.get("rotation", {})
    if not isinstance(raw, dict):
        return {}
    # Rotation blocks in config use string keys; cast narrows dict[Unknown, Unknown] for type checkers.
    return dict(cast(dict[str, object], raw).items())


def _prepare_log_environment(log_config: dict[str, object], environment: str, log_level: str) -> tuple[Path, int, int]:
    """Ensure log dirs exist, rotate logs, set root level; return env_log_dir, max_bytes, backup_count."""
    log_base_raw = log_config.get("log_base", "logs")
    log_base = resolve_log_base(str(log_base_raw) if log_base_raw is not None else "logs")
    env_log_dir = log_base / environment
    ensure_log_directory(env_log_dir / ".dummy")
    rotate_log_files(env_log_dir)
    root_logger = logging.getLogger()
    root_logger.setLevel(getattr(logging, str(log_level).upper(), logging.INFO))
    rotation_config = _rotation_subconfig(log_config)
    max_size_raw = rotation_config.get("max_size", "10MB")
    if isinstance(max_size_raw, (str, int)):
        max_bytes = _convert_max_size_to_bytes(max_size_raw)
    else:
        max_bytes = _convert_max_size_to_bytes("10MB")
    backup_count_raw = rotation_config.get("backup_count", 5)
    backup_count = backup_count_raw if isinstance(backup_count_raw, int) else 5
    return (env_log_dir, max_bytes, backup_count)


def setup_enhanced_file_logging(
    environment: str,
    log_config: dict[str, object],
    log_level: str,
    player_service: object | None = None,
    enable_async: bool = True,
) -> None:
    """Set up enhanced file logging with async QueueHandler/QueueListener when enable_async is True."""
    win_safe_handler, base_handler = _get_handler_classes()
    env_log_dir, max_bytes, backup_count = _prepare_log_environment(log_config, environment, log_level)
    root_logger = logging.getLogger()
    log_queue = _get_or_create_log_queue() if enable_async else None
    handler_class = _get_handler_class(win_safe_handler, base_handler)
    all_file_handlers = _setup_category_handlers(
        DEFAULT_LOG_CATEGORIES,
        _CategoryHandlerConfig(
            env_log_dir=env_log_dir,
            handler_class=handler_class,
            max_bytes=max_bytes,
            backup_count=backup_count,
            player_service=player_service,
            enable_async=enable_async,
            log_queue=log_queue,
            environment=environment,
            log_level=log_level,
        ),
    )
    all_file_handlers.extend(
        _setup_aggregator_handlers(
            env_log_dir, max_bytes, backup_count, player_service, enable_async, log_queue, root_logger
        )
    )
    all_file_handlers.append(
        _setup_console_handler(
            _ConsoleHandlerConfig(
                env_log_dir=env_log_dir,
                max_bytes=max_bytes,
                backup_count=backup_count,
                player_service=player_service,
                log_level=log_level,
                win_safe_handler=win_safe_handler,
                base_handler=base_handler,
                enable_async=enable_async,
                log_queue=log_queue,
                root_logger=root_logger,
            )
        )
    )
    root_logger.setLevel(logging.DEBUG)
    if enable_async and all_file_handlers:
        _setup_async_logging_queue(all_file_handlers)
