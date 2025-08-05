"""
Structlog-based logging configuration for MythosMUD server.

This module provides a configurable logging system that supports multiple
environments (test, development, staging, production) with separate log files
for different categories of events. As the Pnakotic Manuscripts teach us,
proper categorization of knowledge is essential for its preservation.
"""

import os
import sys
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

    log_base = _resolve_log_base(log_config.get("log_base", "logs"))
    env_log_dir = log_base / environment
    env_log_dir.mkdir(parents=True, exist_ok=True)

    # Configure root logger
    root_logger = logging.getLogger()
    root_logger.setLevel(logging.DEBUG)

    # Create handlers for different log categories
    log_categories = {
        "server": ["server"],
        "persistence": ["persistence"],
        "authentication": ["auth"],
        "world": ["world"],
        "communications": ["realtime", "communications"],
        "commands": ["commands"],
        "errors": ["errors"],
        "access": ["access"],
    }

    for log_file, prefixes in log_categories.items():
        log_path = env_log_dir / f"{log_file}.log"

        # Create file handler
        handler = logging.FileHandler(log_path, encoding="utf-8")
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
            logger.propagate = False  # Prevent duplicate logs


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

    # Log the setup
    logger = get_logger("server.logging")
    logger.info(
        "Logging system initialized",
        environment=environment,
        log_level=log_level,
        log_base=logging_config.get("log_base", "logs"),
    )


# Initialize logging when module is imported
if __name__ != "__main__":
    # Basic configuration for import-time usage
    configure_structlog()
