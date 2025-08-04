"""
Logging configuration for MythosMUD server.

This module provides a simple get_logger function that works with
uvicorn's built-in logging system. All logging configuration is now
handled by uvicorn_logging_config.py.
"""

import logging


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
