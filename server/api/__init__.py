"""
API module for MythosMUD.

This module provides REST API endpoints for the MythosMUD server,
including game operations, player management, and monitoring.
"""

from .base import api_router as base_router
from .game import router as game_router
from .monitoring import router as monitoring_router
from .players import router as players_router
from .real_time import router as real_time_router
from .rooms import router as rooms_router

__all__ = [
    "base_router",
    "game_router",
    "monitoring_router",
    "players_router",
    "real_time_router",
    "rooms_router",
]
