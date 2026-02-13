"""
MOTD (Message of the Day) loading utilities for MythosMUD.

This module provides functionality for loading and displaying the Message of the Day
from configured files, with fallback handling for missing or corrupted files.
"""

import os

from ..config import get_config
from ..structured_logging.enhanced_logging_config import get_logger

logger = get_logger(__name__)


def load_motd() -> str:
    """
    Load the Message of the Day from the configured file.

    Returns:
        str: The MOTD content, or a default message if file cannot be loaded
    """
    motd_path = None
    motd_file = None

    try:
        config = get_config()
        motd_file = config.get("motd_file", "./data/motd.txt")  # type: ignore[attr-defined]  # Reason: Legacy dict format support for tests, config.get() not available on AppConfig but supported for backward compatibility

        # Resolve relative path from server directory to project root
        server_dir = os.path.dirname(os.path.abspath(__file__))
        project_root = os.path.dirname(os.path.dirname(server_dir))  # Go up two levels from utils/
        motd_path = os.path.join(project_root, motd_file.replace("./", ""))

        if os.path.exists(motd_path):
            with open(motd_path, encoding="utf-8") as f:
                return f.read().strip()
        else:
            logger.warning("MOTD file not found", motd_path=motd_path, motd_file=motd_file)
            return "Welcome to MythosMUD - Enter the realm of forbidden knowledge..."

    except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: MOTD loading errors unpredictable, must return default message
        logger.error(
            "Error loading MOTD",
            motd_path=motd_path,
            motd_file=motd_file,
            error_type=type(e).__name__,
            error_message=str(e),
        )
        return "Welcome to MythosMUD - Enter the realm of forbidden knowledge..."
