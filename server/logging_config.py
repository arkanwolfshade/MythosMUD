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
        Configured logger instance that works with uvicorn's logging
    """
    logger = logging.getLogger(name)

    # Ensure the logger has a handler (uvicorn will configure this)
    if not logger.handlers:
        # Add a console handler if none exists
        handler = logging.StreamHandler()
        formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s", datefmt="%Y-%m-%d %H:%M:%S"
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        logger.setLevel(logging.INFO)

    return logger
