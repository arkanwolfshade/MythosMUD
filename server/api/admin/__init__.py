"""
Admin API module for MythosMUD.

This module provides administrative API endpoints for managing NPCs,
including CRUD operations, instance management, and monitoring.
"""

from .npc import npc_router

__all__ = ["npc_router"]
