"""
API module for MythosMUD.

This module provides REST API endpoints for the MythosMUD server,
including game operations, player management, monitoring, and admin functions.
"""

from .admin import npc_router as admin_npc_router
from .base import api_router as base_router
from .game import game_router
from .monitoring import monitoring_router
from .players import player_router
from .real_time import realtime_router
from .rooms import room_router

__all__ = [
    "admin_npc_router",
    "base_router",
    "game_router",
    "monitoring_router",
    "player_router",
    "realtime_router",
    "room_router",
]
