"""
Structlog-based logging configuration for MythosMUD server.

This module provides a configurable logging system that supports multiple
environments (test, development, staging, production) with separate log files
for different categories of events. As the Pnakotic Manuscripts teach us,
proper categorization of knowledge is essential for its preservation.
"""

import os
import sys
from datetime import datetime
from pathlib import Path
from typing import Any

import structlog
from structlog.dev import ConsoleRenderer, set_exc_info
from structlog.processors import (
    JSONRenderer,
    TimeStamper,
    add_log_level,
)
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
    timestamp = datetime.now().strftime("%Y_%m_%d_%H%M%S")

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
                logger.info(f"Rotated log file: {log_file.name} -> {rotated_name}")
            except OSError as e:
                logger = get_logger("server.logging")
                logger.warning(f"Could not rotate {log_file.name}: {e}")


class MultiFileHandler:
    """
    Handler that routes logs to different files based on logger name.

    Implements the dimensional mapping principles described in the
    restricted archives for proper log categorization.
    """

    def __init__(self, log_config: dict[str, Any]):
        self.log_config = log_config
        self.handlers = {}
        self._setup_log_directories()

    def _setup_log_directories(self):
        """Create log directories for the current environment."""
        environment = self.log_config.get("environment", "development")
        log_base = _resolve_log_base(self.log_config.get("log_base", "logs"))
        env_log_dir = log_base / environment

        # Create environment-specific log directory
        env_log_dir.mkdir(parents=True, exist_ok=True)

        # Rotate existing log files before creating new ones
        _rotate_log_files(env_log_dir)

        # Create all log file directories
        for log_type in self._get_log_types():
            log_file = env_log_dir / f"{log_type}.log"
            log_file.parent.mkdir(parents=True, exist_ok=True)

    def _get_log_types(self) -> list[str]:
        """Get list of all log file types."""
        return ["server", "persistence", "authentication", "world", "communications", "commands", "errors", "access"]

    def get_log_file_path(self, logger_name: str) -> Path:
        """
        Get the appropriate log file path based on logger name.

        Args:
            logger_name: Name of the logger (e.g., "server.main",
                        "persistence.layer")

        Returns:
            Path to the appropriate log file
        """
        environment = self.log_config.get("environment", "development")
        log_base = _resolve_log_base(self.log_config.get("log_base", "logs"))
        env_log_dir = log_base / environment

        # Map logger names to log files
        logger_mapping = {
            "server": "server",
            "persistence": "persistence",
            "auth": "authentication",
            "world": "world",
            "realtime": "communications",
            "communications": "communications",
            "commands": "commands",
            "errors": "errors",
            "access": "access",
        }

        # Determine log file based on logger name
        log_type = "server"  # default
        for prefix, file_type in logger_mapping.items():
            if logger_name.startswith(prefix):
                log_type = file_type
                break

        return env_log_dir / f"{log_type}.log"


def detect_environment() -> str:
    """
    Detect the current environment based on various indicators.

    Returns:
        Environment name: "test", "development", "staging", or "production"
    """
    # Check if running under pytest
    if "pytest" in sys.modules or "pytest" in sys.argv[0]:
        return "test"

    # Check environment variable
    env = os.getenv("MYTHOSMUD_ENV")
    if env:
        return env

    # Check if test configuration is being used
    if os.getenv("MYTHOSMUD_TEST_MODE"):
        return "test"

    # Default to development
    return "development"


def configure_structlog(
    environment: str | None = None, log_level: str = "INFO", log_config: dict[str, Any] | None = None
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

    # Base processors for all environments
    processors = [
        add_log_level,
        TimeStamper(fmt="iso"),
    ]

    # Environment-specific processors
    if environment == "production":
        processors.append(JSONRenderer())
    else:
        # Check format configuration
        log_format = log_config.get("format", "colored") if log_config else "colored"

        if log_format == "json":
            processors.append(JSONRenderer())
        elif log_format == "human":
            processors.extend(
                [
                    ConsoleRenderer(colors=False),
                    set_exc_info,
                ]
            )
        else:  # colored (default)
            processors.extend(
                [
                    ConsoleRenderer(colors=True),
                    set_exc_info,
                ]
            )

    # Configure standard library logging for file output
    if log_config and not log_config.get("disable_logging", False):
        _setup_file_logging(environment, log_config)

    structlog.configure(
        processors=processors,
        context_class=dict,
        logger_factory=LoggerFactory(),
        wrapper_class=BoundLogger,
        cache_logger_on_first_use=True,
    )


def _setup_file_logging(environment: str, log_config: dict[str, Any]) -> None:
    """Set up file logging handlers for different log categories."""
    import logging
    from logging.handlers import RotatingFileHandler

    log_base = _resolve_log_base(log_config.get("log_base", "logs"))
    env_log_dir = log_base / environment
    env_log_dir.mkdir(parents=True, exist_ok=True)

    # Rotate existing log files before setting up new handlers
    _rotate_log_files(env_log_dir)

    # Configure root logger
    root_logger = logging.getLogger()
    root_logger.setLevel(logging.DEBUG)

    # Get rotation settings from config
    rotation_config = log_config.get("rotation", {})
    max_size_str = rotation_config.get("max_size", "10MB")
    backup_count = rotation_config.get("backup_count", 5)  # Keep 5 backups

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
    }

    for log_file, prefixes in log_categories.items():
        log_path = env_log_dir / f"{log_file}.log"

        # Create rotating file handler for continuous rotation
        handler = RotatingFileHandler(log_path, maxBytes=max_bytes, backupCount=backup_count, encoding="utf-8")
        handler.setLevel(logging.DEBUG)

        # Create formatter
        formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s", datefmt="%Y-%m-%d %H:%M:%S"
        )
        handler.setFormatter(formatter)

        # Add handler to loggers that match the prefixes
        for prefix in prefixes:
            logger = logging.getLogger(prefix)
            logger.addHandler(handler)
            logger.setLevel(logging.DEBUG)
            logger.propagate = False  # Prevent duplicate logs - specific logs go to their files only

    # Also capture all console output to a general log file
    console_log_path = env_log_dir / "console.log"
    console_handler = RotatingFileHandler(
        console_log_path, maxBytes=max_bytes, backupCount=backup_count, encoding="utf-8"
    )
    console_handler.setLevel(logging.DEBUG)
    console_handler.setFormatter(formatter)

    # Add console handler to root logger to capture all output
    root_logger.addHandler(console_handler)

    # Configure Structlog to use standard library logging
    structlog.configure(
        processors=[
            structlog.stdlib.filter_by_level,
            structlog.stdlib.add_logger_name,
            structlog.stdlib.add_log_level,
            structlog.stdlib.PositionalArgumentsFormatter(),
            structlog.processors.TimeStamper(fmt="iso"),
            structlog.processors.StackInfoRenderer(),
            structlog.processors.format_exc_info,
            structlog.processors.UnicodeDecoder(),
            structlog.stdlib.ProcessorFormatter.wrap_for_formatter,
        ],
        context_class=dict,
        logger_factory=structlog.stdlib.LoggerFactory(),
        wrapper_class=structlog.stdlib.BoundLogger,
        cache_logger_on_first_use=True,
    )

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


def setup_logging(config: dict[str, Any]) -> None:
    """
    Set up logging configuration based on server config.

    Args:
        config: Server configuration dictionary
    """
    logging_config = config.get("logging", {})
    environment = logging_config.get("environment", detect_environment())
    log_level = logging_config.get("level", "INFO")

    # Configure Structlog
    configure_structlog(environment, log_level, logging_config)

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


def _configure_uvicorn_logging() -> None:
    """
    Configure uvicorn to use our StructLog system.

    This ensures that all uvicorn logs (access logs, error logs, etc.)
    go through our StructLog system and are properly categorized.
    """
    import logging

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


# Initialize logging when module is imported
if __name__ != "__main__":
    # Basic configuration for import-time usage
    configure_structlog()
