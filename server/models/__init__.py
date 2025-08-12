"""
Database models for MythosMUD.

This package contains all database models including:
- User model (FastAPI Users)
- Player model (game data)
- Invite model (custom invite system)
"""

from .alias import Alias
from .game import AttributeType, Stats
from .invite import Invite
from .player import Player
from .relationships import setup_relationships
from .user import User

__all__ = ["User", "Player", "Invite", "Alias", "setup_relationships", "Stats", "AttributeType"]
