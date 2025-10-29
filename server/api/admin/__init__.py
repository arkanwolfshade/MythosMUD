"""
Admin API module for MythosMUD.

This module provides administrative API endpoints for managing NPCs,
NATS subjects, and other administrative functions.
"""

from .npc import npc_router
from .subject_controller import router as subject_router

__all__ = ["npc_router", "subject_router"]
