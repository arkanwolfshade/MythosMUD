"""
File logging setup for enhanced logging system.

This module provides the setup function for configuring file-based logging handlers
with proper categorization, rotation, and Windows safety.
"""

# pylint: disable=too-few-public-methods,too-many-locals,too-many-statements  # Reason: File setup class with focused responsibility, minimal public interface, and complex setup logic requiring many intermediate variables. File setup legitimately requires many statements for comprehensive logging configuration.

import logging
import sys
from logging.handlers import RotatingFileHandler
from pathlib import Path
from typing import Any

from server.structured_logging.logging_handlers import SafeRotatingFileHandler, create_aggregator_handler
from server.structured_logging.logging_utilities import ensure_log_directory, resolve_log_base, rotate_log_files


def _get_handler_class(_WinSafeHandler: type, _BaseHandler: type) -> type:  # pylint: disable=invalid-name  # Reason: Parameter names match class names for type hints
    """Get the appropriate handler class (Windows-safe or base)."""
    handler_class = _BaseHandler
    try:
        if sys.platform == "win32":
            # Windows-safe handler also needs directory safety
            # Create a hybrid class that combines both features
            class SafeWinHandlerCategory(_WinSafeHandler):  # pylint: disable=too-few-public-methods  # Reason: Handler class with focused responsibility, minimal public interface
                """Windows-safe rotating file handler with directory safety for categorized logs."""

                def shouldRollover(self, record):  # noqa: N802  # pylint: disable=invalid-name  # Reason: Overrides parent class method, must match parent signature
                    """Determine if log rollover should occur.

                    Args:
                        record: The log record to check

                    Returns:
                        bool: True if rollover should occur
                    """
                    if self.baseFilename:
                        log_path = Path(self.baseFilename)
                        ensure_log_directory(log_path)
                    return super().shouldRollover(record)

            handler_class = SafeWinHandlerCategory
    except ImportError:
        # Fallback to safe handler on any detection error
        handler_class = _BaseHandler
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
    if player_service is not None:
        from server.structured_logging.player_guid_formatter import PlayerGuidFormatter

        return PlayerGuidFormatter(
            player_service=player_service,
            fmt="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
        )
    return logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )


def _add_handler_to_loggers(
    handler: logging.Handler, prefixes: list[str], log_file: str, environment: str, log_level: str
) -> None:
    """Add handler to loggers that match the prefixes."""
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
    """Create handler for a log category."""
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
    return handler


def setup_enhanced_file_logging(  # pylint: disable=too-many-locals  # Reason: File logging setup requires many intermediate variables for complex logging configuration
    environment: str,
    log_config: dict[str, Any],
    log_level: str,
    player_service: Any = None,
    enable_async: bool = True,  # noqa: ARG001  # pylint: disable=unused-argument  # Reason: Parameter kept for API compatibility with future async logging implementation, currently unused but reserved for future use
) -> None:
    """Set up enhanced file logging handlers with async support."""
    # Use Windows-safe rotation handlers when available
    _WinSafeHandler: type[RotatingFileHandler] = RotatingFileHandler
    try:
        from server.structured_logging.windows_safe_rotation import (
            WindowsSafeRotatingFileHandler as _ImportedWinSafeHandler,
        )

        _WinSafeHandler = _ImportedWinSafeHandler
    except ImportError:  # Optional enhancement - fallback to standard handler if not available
        _WinSafeHandler = RotatingFileHandler

    # Use SafeRotatingFileHandler as base for all handlers to prevent CI race conditions
    _BaseHandler = SafeRotatingFileHandler

    log_base = resolve_log_base(log_config.get("log_base", "logs"))
    env_log_dir = log_base / environment
    # Use thread-safe directory creation (pass dummy file path to ensure directory exists)
    ensure_log_directory(env_log_dir / ".dummy")

    # Rotate existing log files before setting up new handlers
    rotate_log_files(env_log_dir)

    # Configure root logger
    root_logger = logging.getLogger()
    root_logger.setLevel(getattr(logging, str(log_level).upper(), logging.INFO))

    # Get rotation settings from config
    rotation_config = log_config.get("rotation", {})
    max_size_str = rotation_config.get("max_size", "10MB")
    backup_count = rotation_config.get("backup_count", 5)

    # Convert max_size string to bytes
    max_bytes = _convert_max_size_to_bytes(max_size_str)

    # Enhanced log categories organized by subsystem
    # Each subsystem has its own log file for better organization
    log_categories = {
        "server": ["server", "uvicorn"],
        "persistence": ["persistence", "PersistenceLayer", "asyncpg", "database"],
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
        "middleware": [
            "middleware",
            "server.middleware",
        ],
        "monitoring": ["monitoring", "performance", "metrics"],
        "time": ["time", "services.game_tick", "services.schedule"],
        "caching": ["caching"],
        "communications": ["realtime", "communications"],
        "commands": [
            "commands",
            "server.commands",
        ],
        "events": ["events", "EventBus"],
        "infrastructure": ["infrastructure", "infrastructure.nats_broker", "infrastructure.message_broker"],
        "validators": ["validators"],
        "combat": [
            "services.combat_service",
            "services.combat_event_publisher",
            "services.npc_combat_integration_service",
            "services.player_combat_service",
            "validators.combat_validator",
            "logging.combat_audit",
        ],
        "magic": [
            "server.game.magic",
            "game.magic",
            "magic",
        ],
        "access": ["access", "server.app.factory"],
        "security": ["security", "audit"],
    }

    # Create handlers for different log categories
    handler_class = _get_handler_class(_WinSafeHandler, _BaseHandler)
    for log_file, prefixes in log_categories.items():
        log_path = env_log_dir / f"{log_file}.log"
        handler = _create_handler_for_category(log_path, handler_class, max_bytes, backup_count, player_service)
        _add_handler_to_loggers(handler, prefixes, log_file, environment, log_level)

    # Create warnings.log aggregator handler
    # This captures ALL WARNING level logs from ALL subsystems
    # Warnings appear in both their subsystem log AND warnings.log
    warnings_log_path = env_log_dir / "warnings.log"
    warnings_handler = create_aggregator_handler(
        warnings_log_path,
        logging.WARNING,
        max_bytes,
        backup_count,
        player_service,
    )
    root_logger.addHandler(warnings_handler)

    # Create errors.log aggregator handler
    # This captures ALL ERROR and CRITICAL level logs from ALL subsystems
    # Errors appear in both their subsystem log AND errors.log
    errors_log_path = env_log_dir / "errors.log"
    errors_handler = create_aggregator_handler(
        errors_log_path,
        logging.ERROR,
        max_bytes,
        backup_count,
        player_service,
    )
    root_logger.addHandler(errors_handler)

    # Enhanced console handler with structured output
    console_log_path = env_log_dir / "console.log"
    handler_class = _BaseHandler
    try:
        if sys.platform == "win32":
            # Windows-safe handler also needs directory safety
            class SafeWinHandlerConsole(_WinSafeHandler):  # type: ignore[misc, valid-type]  # Reason: Dynamic class creation inside conditional block, mypy cannot validate type compatibility at definition time
                """Windows-safe rotating file handler with directory safety for console logs."""

                def shouldRollover(self, record):  # noqa: N802  # Reason: Method name required by parent class logging.handlers.RotatingFileHandler, cannot change to follow PEP8 naming
                    if self.baseFilename:
                        log_path = Path(self.baseFilename)
                        ensure_log_directory(log_path)
                    return super().shouldRollover(record)

            handler_class = SafeWinHandlerConsole
    except Exception:  # pylint: disable=broad-except  # Reason: Defensive fallback for class definition failures, must catch all exceptions to prevent logging setup from failing completely
        # Defensive fallback: if class definition fails for any reason,
        # fall back to base handler (e.g., if _WinSafeHandler is invalid)
        handler_class = _BaseHandler

    # Ensure directory exists right before creating handler to prevent race conditions
    ensure_log_directory(console_log_path)
    try:
        console_handler = handler_class(
            console_log_path,
            maxBytes=max_bytes,
            backupCount=backup_count,
            encoding="utf-8",
        )
    except (FileNotFoundError, OSError):
        # If directory doesn't exist or was deleted, recreate it and try again
        ensure_log_directory(console_log_path)
        console_handler = handler_class(
            console_log_path,
            maxBytes=max_bytes,
            backupCount=backup_count,
            encoding="utf-8",
        )
    console_handler.setLevel(getattr(logging, str(log_level).upper(), logging.INFO))

    # Use enhanced formatter for console handler
    console_formatter: logging.Formatter
    if player_service is not None:
        from server.structured_logging.player_guid_formatter import PlayerGuidFormatter

        console_formatter = PlayerGuidFormatter(
            player_service=player_service,
            fmt="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
        )
    else:
        console_formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
        )
    console_handler.setFormatter(console_formatter)
    root_logger.addHandler(console_handler)

    root_logger.setLevel(logging.DEBUG)

    # AI Agent: Log after structlog is configured using structlog logger
    # This will be called after configure_enhanced_structlog() completes
