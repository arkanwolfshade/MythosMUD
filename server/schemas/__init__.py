"""
Pydantic schemas for MythosMUD.

This package contains all Pydantic schemas including:
- User schemas (FastAPI Users)
- Player schemas (game data)
- Invite schemas (custom invite system)
"""

from .invite import InviteCreate, InviteRead, InviteUpdate
from .player import PlayerCreate, PlayerRead, PlayerUpdate
from .user import UserCreate, UserRead, UserUpdate

__all__ = [
    "UserCreate",
    "UserRead",
    "UserUpdate",
    "PlayerCreate",
    "PlayerRead",
    "PlayerUpdate",
    "InviteCreate",
    "InviteRead",
    "InviteUpdate",
]
