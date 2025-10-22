#!/usr/bin/env python3
"""
Test script to verify logging system functionality.
"""

import os
import sys

# Add the server directory to the Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "server"))

from server.config import get_config
from server.logging.enhanced_logging_config import get_logger, setup_enhanced_logging


def test_logging():
    """Test if logging system is working."""
    print("Testing logging system...")

    # Get config
    config = get_config()
    print(f"Config: {config.to_legacy_dict()}")

    # Setup logging
    print("Setting up logging...")
    setup_enhanced_logging(config.to_legacy_dict())
    print("Logging setup completed")

    # Test logger
    logger = get_logger("test_logging")
    print("Logger created")

    # Test logging
    logger.info("This is a test log message")
    logger.debug("This is a debug message")
    logger.warning("This is a warning message")
    logger.error("This is an error message")

    print("Logging test completed")


if __name__ == "__main__":
    test_logging()
