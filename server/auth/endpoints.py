"""
Authentication endpoints for MythosMUD.

This module provides FastAPI endpoints for user authentication,
registration, and management with invite-only functionality.
"""

from fastapi import APIRouter, Depends

from ..models.user import User
from ..schemas.invite import InviteRead
from .dependencies import get_current_superuser, require_invite_code
from .invites import InviteManager, get_invite_manager
from .users import fastapi_users, get_auth_backend

# Create router for auth endpoints
auth_router = APIRouter(prefix="/auth", tags=["authentication"])

# Get authentication backend
auth_backend = get_auth_backend()


@auth_router.post("/register", response_model=dict)
async def register_with_invite(
    email: str,
    password: str,
    invite_code: str,
    invite_manager: InviteManager = Depends(get_invite_manager),
):
    """
    Register a new user with invite code validation.

    This endpoint validates the invite code before allowing registration.
    """

    # Validate invite code
    await require_invite_code(invite_code, invite_manager)

    # Create user using FastAPI Users
    user_manager = fastapi_users._user_manager
    user = await user_manager.create(
        {
            "email": email,
            "password": password,
            "is_active": True,
            "is_superuser": False,
            "is_verified": True,  # Auto-verify for invite-only system
        }
    )

    # Mark invite as used
    await invite_manager.use_invite(invite_code, user.user_id)

    return {"message": "User registered successfully", "user_id": str(user.id), "email": user.email}


@auth_router.post("/invites", response_model=InviteRead)
async def create_invite(
    expires_in_days: int = 30,
    current_user: User = Depends(get_current_superuser),
    invite_manager: InviteManager = Depends(get_invite_manager),
):
    """
    Create a new invite code (superuser only).
    """

    invite = await invite_manager.create_invite(expires_in_days=expires_in_days)

    return InviteRead(
        id=invite.id,
        invite_code=invite.invite_code,
        used_by_user_id=invite.used_by_user_id,
        is_used=invite.is_used,
        expires_at=invite.expires_at,
        created_at=invite.created_at,
    )


@auth_router.get("/invites", response_model=list[InviteRead])
async def list_invites(
    current_user: User = Depends(get_current_superuser),
    invite_manager: InviteManager = Depends(get_invite_manager),
):
    """
    List all invites (superuser only).
    """

    invites = await invite_manager.get_user_invites(current_user.user_id)

    return [
        InviteRead(
            id=invite.id,
            invite_code=invite.invite_code,
            used_by_user_id=invite.used_by_user_id,
            is_used=invite.is_used,
            expires_at=invite.expires_at,
            created_at=invite.created_at,
        )
        for invite in invites
    ]


@auth_router.post("/invites/cleanup")
async def cleanup_expired_invites(
    current_user: User = Depends(get_current_superuser),
    invite_manager: InviteManager = Depends(get_invite_manager),
):
    """
    Clean up expired invites (superuser only).
    """

    removed_count = await invite_manager.cleanup_expired_invites()

    return {"message": f"Cleaned up {removed_count} expired invites", "removed_count": removed_count}


@auth_router.get("/invites/unused", response_model=list[InviteRead])
async def list_unused_invites(
    current_user: User = Depends(get_current_superuser),
    invite_manager: InviteManager = Depends(get_invite_manager),
):
    """
    List all unused invites (superuser only).
    """

    invites = await invite_manager.get_unused_invites()

    return [
        InviteRead(
            id=invite.id,
            invite_code=invite.invite_code,
            used_by_user_id=invite.used_by_user_id,
            is_used=invite.is_used,
            expires_at=invite.expires_at,
            created_at=invite.created_at,
        )
        for invite in invites
    ]


# Include only JWT auth routes from FastAPI Users (avoiding conflicts)
auth_router.include_router(fastapi_users.get_auth_router(auth_backend), prefix="/jwt", tags=["authentication"])

# Don't include register router since we have custom registration
# auth_router.include_router(
#     fastapi_users.get_register_router(UserRead, UserCreate), prefix="/register", tags=["authentication"]
# )

# Don't include users router since we have custom user management
# auth_router.include_router(fastapi_users.get_users_router(UserRead, UserUpdate), prefix="/users", tags=["users"])
