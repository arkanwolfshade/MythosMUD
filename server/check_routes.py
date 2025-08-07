#!/usr/bin/env python3
"""Check FastAPI app routes."""

import sys
from pathlib import Path

# Add the server directory to the path
sys.path.insert(0, str(Path(__file__).parent))

from logging_config import get_logger
from main import app

logger = get_logger(__name__)

logger.info("Routes:")
for route in app.routes:
    logger.info(f"{route.methods} {route.path}")
