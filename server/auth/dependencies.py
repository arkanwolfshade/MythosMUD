"""
Authentication dependencies for MythosMUD.

This module provides dependency injection functions for
authentication and authorization in FastAPI endpoints.
"""

from fastapi import Depends, status

from ..exceptions import LoggedHTTPException
from ..models.user import User
from .invites import InviteManager, get_invite_manager
from .users import get_current_active_user, get_current_user


async def get_current_superuser(
    current_user: User = Depends(get_current_active_user),
) -> User:
    """Get current superuser or raise 403."""

    if not current_user.is_superuser:
        raise LoggedHTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="The user doesn't have enough privileges",
            context=None,
        )
    return current_user


async def get_current_verified_user(
    current_user: User = Depends(get_current_active_user),
) -> User:
    """Get current verified user or raise 403."""

    if not current_user.is_verified:
        raise LoggedHTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="The user is not verified",
            context=None,
        )
    return current_user


async def require_invite_code(
    invite_code: str,
    invite_manager: InviteManager = Depends(get_invite_manager),
) -> None:
    """Validate invite code for registration."""

    try:
        await invite_manager.validate_invite(invite_code)
    except LoggedHTTPException as err:
        raise err
    except Exception as err:
        raise LoggedHTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid or expired invite code",
            context=None,
        ) from err


async def get_optional_current_user(
    current_user: User | None = Depends(get_current_user),
) -> User | None:
    """Get current user if authenticated, otherwise None."""
    return current_user


# Re-export commonly used dependencies
__all__ = [
    "get_current_user",
    "get_current_active_user",
    "get_current_superuser",
    "get_current_verified_user",
    "require_invite_code",
    "get_optional_current_user",
    "get_invite_manager",
]
