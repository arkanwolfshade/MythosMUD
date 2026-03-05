"""
File logging setup for enhanced logging system.

This module provides the setup function for configuring file-based logging handlers
with proper categorization, rotation, and Windows safety.
"""

# pylint: disable=too-few-public-methods,too-many-locals,too-many-statements,too-many-lines  # Reason: File setup class with focused responsibility, minimal public interface, and complex setup logic requiring many intermediate variables. File setup legitimately requires many statements for comprehensive logging configuration. Module requires 648 lines to implement comprehensive logging setup with category handlers, aggregator handlers, console handlers, Windows safety, async support, and configuration management; splitting would reduce cohesion

import logging
import queue
import sys
import threading
from dataclasses import dataclass
from logging.handlers import QueueHandler, QueueListener, RotatingFileHandler
from pathlib import Path
from typing import Any, cast

from server.structured_logging.logging_handlers import SafeRotatingFileHandler, create_aggregator_handler
from server.structured_logging.logging_utilities import ensure_log_directory, resolve_log_base, rotate_log_files

# Global queue and listener for async logging (initialized once)
_log_queue: queue.Queue[logging.LogRecord] | None = None  # pylint: disable=invalid-name  # Reason: Module-level singleton pattern uses underscore prefix to indicate private module variable, not a constant
_queue_listener: QueueListener | None = None  # pylint: disable=invalid-name  # Reason: Module-level singleton pattern uses underscore prefix to indicate private module variable, not a constant
_queue_listener_lock = threading.Lock()


def _get_or_create_log_queue() -> queue.Queue[logging.LogRecord]:
    """
    Get or create the global log queue for async logging.

    Returns:
        The global log queue for async log processing
    """
    global _log_queue  # pylint: disable=global-statement  # Reason: Global queue must be shared across all QueueHandlers

    with _queue_listener_lock:
        if _log_queue is None:
            _log_queue = queue.Queue(-1)
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
            _queue_listener.stop()
            _queue_listener = None
        _log_queue = None


@dataclass(frozen=True)
class _CategoryHandlerConfig:
    """Configuration for category handler setup (reduces parameter count)."""

    env_log_dir: Path
    handler_class: type
    max_bytes: int
    backup_count: int
    player_service: Any | None
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
        handler = _create_handler_for_category(
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
            _add_handler_to_loggers(
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
    player_service: Any | None,
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
        root_logger.addHandler(QueueHandler(log_queue))
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
    player_service: Any | None
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
    handler_class = config.base_handler
    try:
        if sys.platform == "win32":
            # Windows-safe handler also needs directory safety
            base_win_handler = config.win_safe_handler

            class SafeWinHandlerConsole(base_win_handler):  # type: ignore[misc, valid-type]  # Reason: Dynamic class creation inside conditional block, mypy cannot validate type compatibility at definition time
                """Windows-safe rotating file handler with directory safety for console logs."""

                def shouldRollover(self, record: logging.LogRecord) -> bool:  # noqa: N802  # pylint: disable=invalid-name  # Reason: Method name required by parent class logging.handlers.RotatingFileHandler, cannot change to follow PEP8 naming
                    """Check if log file should roll over, ensuring directory exists first.

                    Args:
                        record: Log record to check

                    Returns:
                        bool: True if rollover should occur, False otherwise
                    """
                    if self.baseFilename:
                        log_path = Path(self.baseFilename)
                        ensure_log_directory(log_path)
                    return bool(super().shouldRollover(record))

            handler_class = SafeWinHandlerConsole
    except Exception:  # pylint: disable=broad-except  # Reason: Defensive fallback for class definition failures, must catch all exceptions to prevent logging setup from failing completely
        # Defensive fallback: if class definition fails for any reason,
        # fall back to base handler (e.g., if win_safe_handler is invalid)
        handler_class = config.base_handler

    # Ensure directory exists right before creating handler to prevent race conditions
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

    # Use enhanced formatter for console handler
    # Note: Using %(message)s only since structlog already includes all metadata (timestamp, logger name, level)
    # in the rendered message. Adding %(asctime)s - %(name)s - %(levelname)s would cause duplication.
    console_formatter: logging.Formatter
    if config.player_service is not None:
        from server.structured_logging.player_guid_formatter import PlayerGuidFormatter

        console_formatter = PlayerGuidFormatter(
            player_service=config.player_service,
            fmt="%(message)s",
            datefmt=None,
        )
    else:
        console_formatter = logging.Formatter(
            "%(message)s",
            datefmt=None,
        )
    console_handler.setFormatter(console_formatter)

    if config.enable_async and config.log_queue:
        # Do not add another QueueHandler to root; root already has one from
        # aggregator. Adding a second would duplicate every record to the queue.
        # console_handler is returned and added to all_file_handlers, so the
        # QueueListener will still write console output.
        pass
    else:
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
            # Use a larger queue size for better batching performance
            # -1 means unlimited, but in practice the queue will be bounded by memory
            _log_queue = queue.Queue(-1)

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


def _create_formatter(player_service: Any | None) -> logging.Formatter:
    """Create formatter (with or without PlayerGuidFormatter)."""
    # Note: Using %(message)s only since structlog already includes all metadata (timestamp, logger name, level)
    # in the rendered message. Adding %(asctime)s - %(name)s - %(levelname)s would cause duplication.
    if player_service is not None:
        from server.structured_logging.player_guid_formatter import PlayerGuidFormatter

        return PlayerGuidFormatter(
            player_service=player_service,
            fmt="%(message)s",
            datefmt=None,
        )
    return logging.Formatter(
        "%(message)s",
        datefmt=None,
    )


class LoggerNameFilter(logging.Filter):
    """
    Filter that only allows logs from loggers matching specified prefixes.

    This prevents cross-contamination where logs from one subsystem
    (e.g., server.npc.behavior_engine) end up in the wrong log file
    (e.g., communications.log instead of npc.log).
    """

    def __init__(self, allowed_prefixes: list[str]) -> None:
        """
        Initialize filter with allowed logger name prefixes.

        Args:
            allowed_prefixes: List of logger name prefixes to allow
        """
        super().__init__()
        self.allowed_prefixes = allowed_prefixes

    def filter(self, record: logging.LogRecord) -> bool:
        """
        Check if the log record's logger name matches any allowed prefix.

        Args:
            record: Log record to check

        Returns:
            True if logger name matches an allowed prefix, False otherwise
        """
        logger_name = record.name
        # Check if logger name starts with any allowed prefix
        for prefix in self.allowed_prefixes:
            if logger_name == prefix or logger_name.startswith(f"{prefix}."):
                return True
        return False


def _add_handler_to_loggers(
    handler: logging.Handler, prefixes: list[str], log_file: str, environment: str, log_level: str
) -> None:
    """
    Add handler to loggers that match the prefixes.

    Adds a filter to the handler to ensure it only processes logs from
    loggers matching the specified prefixes, preventing cross-contamination.
    """
    # Add filter to handler to ensure it only processes logs from intended loggers
    # This prevents logs from other subsystems (e.g., server.npc.behavior_engine)
    # from being written to the wrong log file (e.g., communications.log)
    # NOTE: When async logging is enabled, this filter is added to the QueueHandler,
    # but we also need to add it to the actual file handler (see _setup_category_handlers)
    handler.addFilter(LoggerNameFilter(prefixes))

    for prefix in prefixes:
        # Try both the prefix as-is and with "server." prefix for module-based loggers
        logger_names = [prefix]
        if not prefix.startswith("server."):
            logger_names.append(f"server.{prefix}")

        for logger_name in logger_names:
            target_logger = logging.getLogger(logger_name)
            target_logger.addHandler(handler)
            # Set DEBUG level for combat modules in local/debug environments
            if log_file == "combat" and (environment == "local" or log_level == "DEBUG"):
                target_logger.setLevel(logging.DEBUG)
            else:
                target_logger.setLevel(getattr(logging, str(log_level).upper(), logging.INFO))
            target_logger.propagate = True


def _create_handler_for_category(
    log_path: Path,
    handler_class: type,
    max_bytes: int,
    backup_count: int,
    player_service: Any | None,
) -> logging.Handler:
    """
    Create handler for a log category with graceful error handling.

    If handler creation fails, returns a NullHandler to prevent logging
    failures from crashing the application.
    """
    try:
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
        handler.setLevel(logging.DEBUG)
        formatter = _create_formatter(player_service)
        handler.setFormatter(formatter)
        result: logging.Handler = cast(logging.Handler, handler)
        return result
    except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Defensive fallback for handler creation failures, must catch all exceptions to prevent logging setup from crashing the application
        # Graceful fallback: if handler creation fails, use NullHandler
        # This prevents logging setup failures from crashing the application
        # Log the error to stderr as a last resort
        print(
            f"Warning: Failed to create log handler for {log_path}: {type(e).__name__}: {e}",
            file=sys.stderr,
        )
        return logging.NullHandler()


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


def _prepare_log_environment(log_config: dict[str, Any], environment: str, log_level: str) -> tuple[Path, int, int]:
    """Ensure log dirs exist, rotate logs, set root level; return env_log_dir, max_bytes, backup_count."""
    log_base = resolve_log_base(log_config.get("log_base", "logs"))
    env_log_dir = log_base / environment
    ensure_log_directory(env_log_dir / ".dummy")
    rotate_log_files(env_log_dir)
    root_logger = logging.getLogger()
    root_logger.setLevel(getattr(logging, str(log_level).upper(), logging.INFO))
    rotation_config = log_config.get("rotation", {})
    max_bytes = _convert_max_size_to_bytes(rotation_config.get("max_size", "10MB"))
    backup_count = rotation_config.get("backup_count", 5)
    return (env_log_dir, max_bytes, backup_count)


DEFAULT_LOG_CATEGORIES: dict[str, list[str]] = {
    "server": ["server", "uvicorn", "server.app.factory"],
    "persistence": ["persistence", "server.persistence", "PersistenceLayer", "asyncpg", "database"],
    "authentication": ["auth"],
    "inventory": [
        "inventory",
        "server.services.inventory",
        "server.services.inventory_mutation_guard",
        "server.services.container",
        "server.services.container_service",
        "server.services.wearable_container_service",
        "server.services.equipment_service",
        "services.inventory",
        "services.inventory_mutation_guard",
        "services.container",
        "services.container_service",
        "services.wearable_container_service",
        "services.equipment_service",
    ],
    "npc": [
        "npc",
        "server.npc",
        "services.npc",
        "services.npc_service",
        "services.npc_instance_service",
        "services.npc_startup_service",
    ],
    "game": [
        "game",
        "server.game",
        "server.services.player",
        "server.services.room_sync",
        "server.world_loader",
        "server.game.movement_service",
        "server.game.room_service",
        "server.game.player_service",
        "server.game.mechanics",
        "services.player",
        "services.room_sync",
        "world_loader",
        "game.movement_service",
        "game.room_service",
        "game.player_service",
        "game.mechanics",
    ],
    "api": ["api", "server.api"],
    "middleware": ["middleware", "server.middleware"],
    "monitoring": ["monitoring", "server.monitoring", "server.api.monitoring", "performance", "metrics"],
    "time": [
        "time",
        "server.time",
        "services.game_tick",
        "services.game_tick_service",
        "services.schedule",
        "server.services.schedule_service",
    ],
    "caching": ["caching", "server.caching"],
    "communications": ["realtime", "communications"],
    "commands": [
        "commands",
        "server.commands",
        "server.utils.command_parser",
        "server.utils.command_processor",
    ],
    "events": ["events", "EventBus"],
    "infrastructure": ["infrastructure", "server.infrastructure"],
    "validators": ["validators", "server.validators"],
    "combat": [
        "services.combat_service",
        "services.combat_turn_processor",
        "services.combat_event_publisher",
        "services.npc_combat_integration_service",
        "services.player_combat_service",
        "validators.combat_validator",
        "logging.combat_audit",
    ],
    "magic": ["server.game.magic", "game.magic", "magic"],
    "party": [
        "server.game.party_service",
        "server.commands.party_commands",
        "server.realtime.channel_broadcasting_strategies",
    ],
    "quests": [
        "server.game.quest",
        "server.persistence.repositories.quest_definition_repository",
        "server.persistence.repositories.quest_instance_repository",
        "server.commands.quest_commands",
    ],
    "access": ["access", "uvicorn.access"],
    "security": [
        "security",
        "server.security_utils",
        "server.utils.audit_logger",
        "server.structured_logging.admin_actions_logger",
        "server.middleware.security_headers",
        "server.validators.optimized_security_validator",
        "audit",
    ],
}


def _get_default_log_categories() -> dict[str, list[str]]:
    """Return enhanced log categories by subsystem (one log file per subsystem)."""
    return DEFAULT_LOG_CATEGORIES


def setup_enhanced_file_logging(
    environment: str,
    log_config: dict[str, Any],
    log_level: str,
    player_service: Any | None = None,
    enable_async: bool = True,
) -> None:
    """Set up enhanced file logging with async QueueHandler/QueueListener when enable_async is True."""
    win_safe_handler, base_handler = _get_handler_classes()
    env_log_dir, max_bytes, backup_count = _prepare_log_environment(log_config, environment, log_level)
    root_logger = logging.getLogger()
    log_queue = _get_or_create_log_queue() if enable_async else None
    handler_class = _get_handler_class(win_safe_handler, base_handler)
    all_file_handlers = _setup_category_handlers(
        _get_default_log_categories(),
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
