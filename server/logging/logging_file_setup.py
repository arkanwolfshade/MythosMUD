"""
File logging setup for enhanced logging system.

This module provides the setup function for configuring file-based logging handlers
with proper categorization, rotation, and Windows safety.
"""

import logging
import sys
from logging.handlers import RotatingFileHandler
from pathlib import Path
from typing import Any

from server.logging.logging_handlers import SafeRotatingFileHandler, create_aggregator_handler
from server.logging.logging_utilities import ensure_log_directory, resolve_log_base, rotate_log_files


def setup_enhanced_file_logging(
    environment: str,
    log_config: dict[str, Any],
    log_level: str,
    player_service: Any = None,
    enable_async: bool = True,  # noqa: ARG001  # pylint: disable=unused-argument
) -> None:
    """Set up enhanced file logging handlers with async support."""
    # Use Windows-safe rotation handlers when available
    _WinSafeHandler: type[RotatingFileHandler] = RotatingFileHandler
    try:
        from server.logging.windows_safe_rotation import WindowsSafeRotatingFileHandler as _ImportedWinSafeHandler

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
    if isinstance(max_size_str, str):
        if max_size_str.endswith("MB"):
            max_bytes = int(max_size_str[:-2]) * 1024 * 1024
        elif max_size_str.endswith("KB"):
            max_bytes = int(max_size_str[:-2]) * 1024
        elif max_size_str.endswith("B"):
            max_bytes = int(max_size_str[:-1])
        else:
            max_bytes = int(max_size_str)
    else:
        max_bytes = max_size_str

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
    for log_file, prefixes in log_categories.items():
        log_path = env_log_dir / f"{log_file}.log"

        # Create rotating file handler (Windows-safe on win32, with directory safety)
        handler_class = _BaseHandler
        try:
            if sys.platform == "win32":
                # Windows-safe handler also needs directory safety
                # Create a hybrid class that combines both features
                class SafeWinHandlerCategory(_WinSafeHandler):  # type: ignore[misc, valid-type]
                    def shouldRollover(self, record):  # noqa: N802
                        if self.baseFilename:
                            log_path = Path(self.baseFilename)
                            ensure_log_directory(log_path)
                        return super().shouldRollover(record)

                handler_class = SafeWinHandlerCategory
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
        handler.setLevel(logging.DEBUG)

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

        # Add handler to loggers that match the prefixes
        # CRITICAL FIX: Add handlers to parent loggers (e.g., "server.commands") so that
        # child loggers (e.g., "server.commands.inventory_commands") can propagate to them
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
            class SafeWinHandlerConsole(_WinSafeHandler):  # type: ignore[misc, valid-type]
                def shouldRollover(self, record):  # noqa: N802
                    if self.baseFilename:
                        log_path = Path(self.baseFilename)
                        ensure_log_directory(log_path)
                    return super().shouldRollover(record)

            handler_class = SafeWinHandlerConsole
    except Exception:  # pylint: disable=broad-except
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
        from server.logging.player_guid_formatter import PlayerGuidFormatter

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
