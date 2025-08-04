"""
Logging configuration for MythosMUD server.

This module handles all logging setup, including file rotation,
console output, and uvicorn logging configuration.
"""

import datetime
import logging
import sys
from pathlib import Path


def setup_logging():
    """
    Setup logging configuration for the server.

    This function configures logging with both file and console output,
    including log file rotation and uvicorn logging integration.
    """
    # Get server log path from environment variable or use default
    import os

    server_log_path = os.environ.get("SERVER_LOG")
    if server_log_path:
        server_log_path = Path(server_log_path)
        # Create parent directory if it doesn't exist
        server_log_path.parent.mkdir(parents=True, exist_ok=True)
        logs_dir = server_log_path.parent
    else:
        # Default to server/logs/server.log
        logs_dir = Path(__file__).parent.parent / "logs"
        logs_dir.mkdir(exist_ok=True)
        server_log_path = logs_dir / "server.log"

    if server_log_path.exists():
        # Generate timestamp for the rotated log file
        timestamp = datetime.datetime.now().strftime("%Y_%m_%d_%H%M%S")
        rotated_log_path = logs_dir / f"server.log.{timestamp}"

        # Rename the existing log file
        try:
            server_log_path.rename(rotated_log_path)
            sys.stderr.write(f"Rotated log file: {rotated_log_path}\n")
        except Exception as e:
            sys.stderr.write(f"Warning: Could not rotate log file: {e}\n")

    # Configure logging
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        handlers=[
            logging.FileHandler(server_log_path),
            logging.StreamHandler(),  # Also log to console
        ],
    )

    # Also configure uvicorn logging to go to our file
    uvicorn_logger = logging.getLogger("uvicorn")
    uvicorn_logger.handlers = []
    uvicorn_logger.addHandler(logging.FileHandler(server_log_path))
    uvicorn_logger.addHandler(logging.StreamHandler())
    uvicorn_logger.setLevel(logging.INFO)

    # Configure access logger
    access_logger = logging.getLogger("uvicorn.access")
    access_logger.handlers = []
    access_logger.addHandler(logging.FileHandler(server_log_path))
    access_logger.addHandler(logging.StreamHandler())
    access_logger.setLevel(logging.INFO)
