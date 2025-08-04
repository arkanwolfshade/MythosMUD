"""
Centralized logging configuration for MythosMUD server.

This module provides a unified logging setup that ensures all loggers
are properly configured with appropriate levels and handlers. As noted
in the Pnakotic Manuscripts, proper organization of knowledge requires
systematic documentation - even of the most mundane operational details.
"""

import logging
import logging.handlers
import os
import sys
from pathlib import Path

from .config_loader import get_config


def setup_logging(
    log_file: str | None = None,
    log_level: str | None = None,
    rotate_logs: bool = False,  # Disable rotation by default to avoid permission issues
) -> None:
    """
    Configure centralized logging for the MythosMUD server.

    Args:
        log_file: Path to log file (defaults to server/logs/server.log)
        log_level: Logging level (defaults to config value or DEBUG)
        rotate_logs: Whether to rotate existing log files
    """
    # Get configuration
    config = get_config()

    # Determine log file path
    if log_file is None:
        # Get the project root directory (two levels up from server directory)
        module_dir = os.path.dirname(os.path.abspath(__file__))
        project_root = os.path.dirname(module_dir)
        log_file = os.path.join(project_root, "server", "logs", "server.log")

    # Determine log level
    if log_level is None:
        log_level = config.get("log_level", "DEBUG")

    # Convert string level to logging constant
    level_map = {
        "DEBUG": logging.DEBUG,
        "INFO": logging.INFO,
        "WARNING": logging.WARNING,
        "ERROR": logging.ERROR,
        "CRITICAL": logging.CRITICAL,
    }
    numeric_level = level_map.get(log_level.upper(), logging.DEBUG)

    # Create log directory if it doesn't exist
    log_path = Path(log_file)
    log_path.parent.mkdir(parents=True, exist_ok=True)

    # Rotate existing log file if requested
    if rotate_logs and log_path.exists():
        import datetime

        try:
            timestamp = datetime.datetime.now().strftime("%Y_%m_%d_%H%M%S")
            rotated_log = log_path.with_name(f"server.log.{timestamp}")
            log_path.rename(rotated_log)
        except (OSError, PermissionError) as e:
            # Log the error but don't fail - the new log file will be created anyway
            # Use print for this error since logger might not be set up yet
            print(f"Warning: Could not rotate log file {log_path}: {e}")
            # Continue without rotation - the new log file will be created anyway

    # Create formatter
    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s", datefmt="%Y-%m-%d %H:%M:%S")

    # Create file handler
    file_handler = logging.FileHandler(log_file)
    file_handler.setFormatter(formatter)
    file_handler.setLevel(numeric_level)

    # Create console handler (for development)
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(formatter)
    console_handler.setLevel(numeric_level)

    # Configure root logger
    root_logger = logging.getLogger()
    root_logger.setLevel(numeric_level)

    # Remove existing handlers to avoid duplicates
    for handler in root_logger.handlers[:]:
        root_logger.removeHandler(handler)

    # Add our handlers
    root_logger.addHandler(file_handler)
    root_logger.addHandler(console_handler)

    # Configure specific loggers
    _configure_uvicorn_logging(log_file, numeric_level, formatter)

    # Log the configuration
    logger = logging.getLogger(__name__)
    logger.info(f"Logging configured - Level: {log_level}, File: {log_file}")


def _configure_uvicorn_logging(log_file: str, level: int, formatter: logging.Formatter) -> None:
    """Configure uvicorn-specific loggers."""
    file_handler = logging.FileHandler(log_file)
    file_handler.setFormatter(formatter)
    file_handler.setLevel(level)

    # Configure uvicorn access logging
    uvicorn_access = logging.getLogger("uvicorn.access")
    uvicorn_access.setLevel(level)
    for handler in uvicorn_access.handlers[:]:
        uvicorn_access.removeHandler(handler)
    uvicorn_access.addHandler(file_handler)

    # Configure uvicorn error logging
    uvicorn_error = logging.getLogger("uvicorn.error")
    uvicorn_error.setLevel(level)
    for handler in uvicorn_error.handlers[:]:
        uvicorn_error.removeHandler(handler)
    uvicorn_error.addHandler(file_handler)


def get_logger(name: str) -> logging.Logger:
    """
    Get a logger with the specified name.

    This ensures all loggers are properly configured and write to the
    centralized log file. As the Pnakotic Manuscripts teach us, proper
    categorization of knowledge is essential for its preservation.

    Args:
        name: Logger name (typically __name__)

    Returns:
        Configured logger instance
    """
    return logging.getLogger(name)
