"""
Structlog-based logging configuration for MythosMUD server.

This module provides a configurable logging system that supports multiple
environments (test, development, staging, production) with separate log files
for different categories of events. As the Pnakotic Manuscripts teach us,
proper categorization of knowledge is essential for its preservation.

CRITICAL LOGGING REQUIREMENT:
All service modules MUST use get_logger() from this module instead of
logging.getLogger(). Standard Python loggers do not support the 'context'
parameter that our structlog-based system requires. Using logging.getLogger()
will cause server startup failures when services attempt to log with context.

CORRECT USAGE:
    from ..logging_config import get_logger
    logger = get_logger(__name__)
    logger.info("Message", context={"key": "value"})

INCORRECT USAGE (WILL CAUSE FAILURES):
    import logging
    logger = logging.getLogger(__name__)
    logger.info("Message", context={"key": "value"})  # TypeError!
"""

import logging
import os
import sys
from datetime import UTC, datetime
from pathlib import Path
from typing import Any

import structlog

# Using fully-qualified names (structlog.processors.*) below; no direct imports
from structlog.stdlib import BoundLogger, LoggerFactory


def _resolve_log_base(log_base: str) -> Path:
    """
    Resolve log_base path to absolute path relative to project root.

    Args:
        log_base: Relative or absolute path to log directory

    Returns:
        Absolute path to log directory
    """
    log_path = Path(log_base)

    # If already absolute, return as is
    if log_path.is_absolute():
        return log_path

    # Find the project root (where pyproject.toml is located)
    current_dir = Path.cwd()
    project_root = None

    # Look for pyproject.toml in current directory or parents
    for parent in [current_dir] + list(current_dir.parents):
        if (parent / "pyproject.toml").exists():
            project_root = parent
            break

    if project_root:
        return project_root / log_path
    else:
        # Fallback to current directory if project root not found
        return current_dir / log_path


def _rotate_log_files(env_log_dir: Path) -> None:
    """
    Rotate existing log files by renaming them with timestamps.

    This function implements the startup-time log rotation as described in the
    restricted archives. When the server starts, existing log files are renamed
    with timestamps before new log files are created, ensuring clean separation
    between server sessions.

    Args:
        env_log_dir: Path to the environment-specific log directory
    """
    if not env_log_dir.exists():
        return

    # Generate timestamp for rotation
    timestamp = datetime.now(UTC).strftime("%Y_%m_%d_%H%M%S")

    # Get all log files in the directory
    log_files = list(env_log_dir.glob("*.log"))

    if not log_files:
        return

    # Rotate each log file by renaming with timestamp
    for log_file in log_files:
        # Only rotate non-empty files
        if log_file.exists() and log_file.stat().st_size > 0:
            rotated_name = f"{log_file.stem}.log.{timestamp}"
            rotated_path = log_file.parent / rotated_name

            try:
                log_file.rename(rotated_path)
                # Log the rotation (this will go to the new log file)
                logger = get_logger("server.logging")
                logger.info(
                    "Rotated log file",
                    old_name=log_file.name,
                    new_name=rotated_name,
                )
            except OSError as e:
                logger = get_logger("server.logging")
                logger.warning(
                    "Could not rotate log file",
                    name=log_file.name,
                    error=str(e),
                )


def detect_environment() -> str:
    """
    Detect the current environment based on various indicators.

    Returns:
        Environment name: "e2e_test", "unit_test", "local", or "production"

    Note: Valid environments are defined in server_config.*.yaml files:
        - e2e_test: End-to-end testing with Playwright
        - unit_test: Unit and integration testing with pytest
        - local: Local development
        - production: Production deployment
    """
    # Check if running under pytest (unit tests)
    if "pytest" in sys.modules or "pytest" in sys.argv[0]:
        return "unit_test"

    # Check explicit environment variable
    env = os.getenv("MYTHOSMUD_ENV")
    if env:
        return env

    # Check if test configuration is being used
    if os.getenv("MYTHOSMUD_TEST_MODE"):
        return "unit_test"

    # Try to determine from config path
    config_path = os.getenv("MYTHOSMUD_CONFIG_PATH", "")
    if "e2e_test" in config_path:
        return "e2e_test"
    elif "unit_test" in config_path:
        return "unit_test"
    elif "production" in config_path:
        return "production"
    elif "local" in config_path:
        return "local"

    # Default to local (not "development" - that's not a valid environment)
    return "local"


def _event_only_renderer(_logger: Any, _name: str, event_dict: dict[str, Any]) -> str:
    """
    Render only the core event/message string for file logs.

    This ensures file logs contain simple messages without ANSI or
    additional structlog fields.
    """
    event = event_dict.get("event")
    return "" if event is None else str(event)


def configure_structlog(
    environment: str | None = None,
    log_level: str = "INFO",
    log_config: dict[str, Any] | None = None,
    player_service: Any = None,
) -> None:
    """
    Configure Structlog based on environment.

    Args:
        environment: Environment name (auto-detected if None)
        log_level: Logging level (DEBUG, INFO, WARNING, ERROR)
        log_config: Logging configuration dictionary
    """
    if environment is None:
        environment = detect_environment()

    # When writing to stdlib logging handlers (for file logs), configure
    # structlog to defer final rendering to logging.Formatter via
    # ProcessorFormatter.wrap_for_formatter. This prevents ANSI codes from
    # ConsoleRenderer from appearing in file logs.
    processors = [
        structlog.stdlib.filter_by_level,
        structlog.stdlib.add_logger_name,
        structlog.stdlib.add_log_level,
        structlog.stdlib.PositionalArgumentsFormatter(),
        structlog.processors.TimeStamper(fmt="iso"),
        structlog.processors.StackInfoRenderer(),
        structlog.processors.format_exc_info,
        structlog.processors.UnicodeDecoder(),
        # Final renderer ensures only the message text is rendered to stdlib
        # and thus to file handlers.
        _event_only_renderer,
    ]

    # Configure standard library logging for file output
    if log_config and not log_config.get("disable_logging", False):
        _setup_file_logging(environment, log_config, log_level, player_service)

    structlog.configure(
        processors=processors,
        context_class=dict,
        logger_factory=LoggerFactory(),
        wrapper_class=BoundLogger,
        # Disable caching so that later configuration (e.g., file logging
        # setup) applies to all existing loggers. This prevents early colored
        # renderers from leaking ANSI codes into file logs.
        cache_logger_on_first_use=False,
    )


def _setup_file_logging(
    environment: str,
    log_config: dict[str, Any],
    log_level: str,
    player_service: Any = None,
) -> None:
    """Set up file logging handlers for different log categories."""
    from logging.handlers import RotatingFileHandler

    log_base = _resolve_log_base(log_config.get("log_base", "logs"))
    env_log_dir = log_base / environment
    env_log_dir.mkdir(parents=True, exist_ok=True)

    # Rotate existing log files before setting up new handlers
    _rotate_log_files(env_log_dir)

    # Configure root logger
    root_logger = logging.getLogger()
    root_logger.setLevel(getattr(logging, str(log_level).upper(), logging.INFO))

    # Get rotation settings from config
    rotation_config = log_config.get("rotation", {})
    max_size_str = rotation_config.get("max_size", "10MB")
    # Keep 5 backups
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

    # Create handlers for different log categories
    log_categories = {
        "server": ["server", "uvicorn"],
        "persistence": ["persistence", "PersistenceLayer", "aiosqlite"],
        "authentication": ["auth"],
        "world": ["world"],
        "communications": ["realtime", "communications"],
        "commands": ["commands"],
        "errors": ["errors"],
        "access": ["access", "server.app.factory"],
        # "redis": ["redis", "services.redis_service", "realtime.redis_message_handler"],  # Redis removed from system
    }

    for log_file, prefixes in log_categories.items():
        log_path = env_log_dir / f"{log_file}.log"

        # Create rotating file handler for continuous rotation
        handler = RotatingFileHandler(
            log_path,
            maxBytes=max_bytes,
            backupCount=backup_count,
            encoding="utf-8",
        )
        handler.setLevel(logging.DEBUG)

        # Create formatter - use PlayerGuidFormatter if player_service is available
        if player_service is not None:
            from .logging.player_guid_formatter import PlayerGuidFormatter

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
        for prefix in prefixes:
            logger = logging.getLogger(prefix)
            logger.addHandler(handler)
            logger.setLevel(getattr(logging, str(log_level).upper(), logging.INFO))
            # Allow propagation so the root logger can also capture WARN+ into
            # errors.log while category files still receive their logs.
            logger.propagate = True

    # Also capture all console output to a general log file
    console_log_path = env_log_dir / "console.log"
    console_handler = RotatingFileHandler(
        console_log_path,
        maxBytes=max_bytes,
        backupCount=backup_count,
        encoding="utf-8",
    )
    console_handler.setLevel(getattr(logging, str(log_level).upper(), logging.INFO))

    # Use the same formatter logic for console handler
    if player_service is not None:
        from .logging.player_guid_formatter import PlayerGuidFormatter

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

    # Add console handler to root logger to capture all output
    root_logger.addHandler(console_handler)

    # Global errors handler that captures WARNING and above for all loggers
    errors_log_path = env_log_dir / "errors.log"
    errors_handler = RotatingFileHandler(
        errors_log_path,
        maxBytes=max_bytes,
        backupCount=backup_count,
        encoding="utf-8",
    )
    errors_handler.setLevel(logging.WARNING)

    # Use the same formatter logic for errors handler
    if player_service is not None:
        from .logging.player_guid_formatter import PlayerGuidFormatter

        errors_formatter = PlayerGuidFormatter(
            player_service=player_service,
            fmt="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
        )
    else:
        errors_formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
        )
    errors_handler.setFormatter(errors_formatter)
    root_logger.addHandler(errors_handler)

    # Nothing else to do here; structlog is already configured in
    # configure_structlog to defer formatting to stdlib handlers

    # Ensure root logger also gets the console handler for any unhandled logs
    root_logger.setLevel(logging.DEBUG)


def get_logger(name: str) -> BoundLogger:
    """
    Get a Structlog logger with the specified name.

    This ensures all loggers are properly configured and write to the
    appropriate log files based on their category. As noted in the
    Pnakotic Manuscripts, proper categorization of knowledge is essential
    for its preservation.

    Args:
        name: Logger name (typically __name__)

    Returns:
        Configured Structlog logger instance
    """
    return structlog.get_logger(name)


def setup_logging(config: dict[str, Any], player_service: Any = None) -> None:
    """
    Set up logging configuration based on server config.

    Args:
        config: Server configuration dictionary
        player_service: Optional player service for GUID-to-name conversion
    """
    logging_config = config.get("logging", {})
    environment = logging_config.get("environment", detect_environment())
    log_level = logging_config.get("level", "INFO")

    # Check if logging should be disabled
    disable_logging = logging_config.get("disable_logging", False)

    if disable_logging:
        # Configure minimal logging without file handlers
        configure_structlog(environment, log_level, {"disable_logging": True}, player_service)
        return

    # Configure Structlog
    configure_structlog(environment, log_level, logging_config, player_service)

    # Configure uvicorn to use our StructLog system
    _configure_uvicorn_logging()

    # Log the setup
    logger = get_logger("server.logging")
    logger.info(
        "Logging system initialized",
        environment=environment,
        log_level=log_level,
        log_base=logging_config.get("log_base", "logs"),
    )


def update_logging_with_player_service(player_service: Any) -> None:
    """
    Update existing logging handlers to use PlayerGuidFormatter.

    This function should be called after the player service becomes available
    to enhance existing log handlers with GUID-to-name conversion.

    Args:
        player_service: The player service for GUID-to-name conversion
    """
    from .logging.player_guid_formatter import PlayerGuidFormatter

    # Create the enhanced formatter
    enhanced_formatter = PlayerGuidFormatter(
        player_service=player_service,
        fmt="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    # Update all existing handlers with the enhanced formatter
    root_logger = logging.getLogger()
    for handler in root_logger.handlers:
        if hasattr(handler, "setFormatter"):
            handler.setFormatter(enhanced_formatter)

    # Update handlers for specific log categories
    log_categories = [
        "server",
        "persistence",
        "authentication",
        "world",
        "communications",
        "commands",
        "errors",
        "access",
    ]

    for category in log_categories:
        logger = logging.getLogger(category)
        for handler in logger.handlers:
            if hasattr(handler, "setFormatter"):
                handler.setFormatter(enhanced_formatter)

    # Log that the enhancement has been applied
    logger = get_logger("server.logging")
    logger.info("Logging system enhanced with PlayerGuidFormatter", player_service_available=True)


def _configure_uvicorn_logging() -> None:
    """
    Configure uvicorn to use our StructLog system.

    This ensures that all uvicorn logs (access logs, error logs, etc.)
    go through our StructLog system and are properly categorized.
    """
    # use outer-scope logging import

    # Get our StructLog logger
    logger = get_logger("uvicorn")

    # Configure uvicorn's access logger to use our system
    uvicorn_access_logger = logging.getLogger("uvicorn.access")
    uvicorn_access_logger.handlers = []  # Remove default handlers
    uvicorn_access_logger.propagate = True  # Let it propagate to our system
    uvicorn_access_logger.setLevel(logging.DEBUG)

    # Configure uvicorn's error logger
    uvicorn_error_logger = logging.getLogger("uvicorn.error")
    uvicorn_error_logger.handlers = []
    uvicorn_error_logger.propagate = True
    uvicorn_error_logger.setLevel(logging.DEBUG)

    # Configure uvicorn's main logger
    uvicorn_logger = logging.getLogger("uvicorn")
    uvicorn_logger.handlers = []
    uvicorn_logger.propagate = True
    uvicorn_logger.setLevel(logging.DEBUG)

    logger.info("Uvicorn logging configured to use StructLog system")


# Note: We intentionally avoid configuring Structlog at import time to prevent
# early logger instances from caching a colored console renderer that would
# leak ANSI sequences into file logs. The application calls setup_logging()
# early in startup to configure logging properly based on runtime config.
