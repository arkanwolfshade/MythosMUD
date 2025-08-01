"""
Authentication module for MythosMUD.

This package contains all authentication-related functionality including:
- FastAPI Users configuration
- Invite management
- Authentication dependencies
"""

from .dependencies import get_current_active_user, get_current_user
from .invites import InviteManager
from .users import get_auth_backend, get_user_manager

__all__ = ["get_user_manager", "get_auth_backend", "InviteManager", "get_current_user", "get_current_active_user"]
