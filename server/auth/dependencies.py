"""
Authentication dependencies for MythosMUD.

This module provides dependency injection functions for
authentication and authorization in FastAPI endpoints.
"""

from fastapi import Depends, Request, status

from ..exceptions import LoggedHTTPException
from ..models.user import User
from ..utils.error_logging import create_context_from_request
from .invites import InviteManager, get_invite_manager
from .users import get_current_active_user, get_current_user


async def get_current_superuser(
    current_user: User = Depends(get_current_active_user),
    request: Request = None,
) -> User:
    """Get current superuser or raise 403."""

    if not current_user.is_superuser:
        context = create_context_from_request(request) if request else None
        if context:
            context.metadata["user_id"] = str(current_user.id)
            context.metadata["username"] = current_user.username
            context.metadata["operation"] = "get_current_superuser"
        raise LoggedHTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="The user doesn't have enough privileges", context=context
        )
    return current_user


async def get_current_verified_user(
    current_user: User = Depends(get_current_active_user),
    request: Request = None,
) -> User:
    """Get current verified user or raise 403."""

    if not current_user.is_verified:
        context = create_context_from_request(request) if request else None
        if context:
            context.metadata["user_id"] = str(current_user.id)
            context.metadata["username"] = current_user.username
            context.metadata["operation"] = "get_current_verified_user"
        raise LoggedHTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="The user is not verified", context=context
        )
    return current_user


async def require_invite_code(
    invite_code: str,
    invite_manager: InviteManager = Depends(get_invite_manager),
    request: Request = None,
) -> None:
    """Validate invite code for registration."""

    try:
        await invite_manager.validate_invite(invite_code)
    except LoggedHTTPException as err:
        raise err
    except Exception as err:
        context = create_context_from_request(request) if request else None
        if context:
            context.metadata["invite_code"] = invite_code
            context.metadata["operation"] = "require_invite_code"
        raise LoggedHTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid or expired invite code", context=context
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
