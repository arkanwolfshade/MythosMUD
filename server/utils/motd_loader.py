"""
MOTD (Message of the Day) loading utilities for MythosMUD.

This module provides functionality for loading and displaying the Message of the Day
from configured files, with fallback handling for missing or corrupted files.
"""

import os

from ..config_loader import get_config
from ..logging_config import get_logger

logger = get_logger(__name__)


def load_motd() -> str:
    """
    Load the Message of the Day from the configured file.

    Returns:
        str: The MOTD content, or a default message if file cannot be loaded
    """
    try:
        config = get_config()
        motd_file = config.get("motd_file", "./data/motd.txt")

        # Resolve relative path from server directory to project root
        server_dir = os.path.dirname(os.path.abspath(__file__))
        project_root = os.path.dirname(os.path.dirname(server_dir))  # Go up two levels from utils/
        motd_path = os.path.join(project_root, motd_file.replace("./", ""))

        if os.path.exists(motd_path):
            with open(motd_path, encoding="utf-8") as f:
                return f.read().strip()
        else:
            logger.warning(f"MOTD file not found: {motd_path}")
            return "Welcome to MythosMUD - Enter the realm of forbidden knowledge..."

    except Exception as e:
        logger.error(f"Error loading MOTD: {e}")
        return "Welcome to MythosMUD - Enter the realm of forbidden knowledge..."
