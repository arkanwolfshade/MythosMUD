"""
Authentication endpoints for MythosMUD.

This module provides endpoints for user registration, login, and authentication
management. It integrates with FastAPI Users for user management and includes
custom invite code validation.
"""

from typing import Any

from faker import Faker
from fastapi import APIRouter, Depends, HTTPException
from fastapi_users import InvalidPasswordException
from fastapi_users.schemas import BaseUserCreate
from pydantic import BaseModel
from sqlalchemy.ext.asyncio import AsyncSession

from ..database import get_async_session
from ..models.user import User
from ..schemas.invite import InviteRead
from .dependencies import get_current_superuser
from .invites import InviteManager, get_invite_manager
from .users import UserManager, get_auth_backend, get_user_manager

fake = Faker()

# Create router for auth endpoints
auth_router = APIRouter(prefix="/auth", tags=["auth"])


# Define user creation schema
class UserCreate(BaseUserCreate):
    """Schema for user creation with invite code validation."""

    invite_code: str


# Define login request schema
class LoginRequest(BaseModel):
    """Schema for login requests."""

    username: str
    password: str


# Define login response schema
class LoginResponse(BaseModel):
    """Schema for login responses."""

    access_token: str
    token_type: str = "bearer"
    user_id: str


@auth_router.post("/register", response_model=LoginResponse)
async def register_user(
    user_create: UserCreate,
    invite_manager: InviteManager = Depends(get_invite_manager),
    user_manager: UserManager = Depends(get_user_manager),
    session: AsyncSession = Depends(get_async_session),
) -> LoginResponse:
    """
    Register a new user with invite code validation.

    This endpoint validates the invite code and creates a new user account.
    The invite code is marked as used after successful registration.
    """
    print(f"Registration attempt for username: {user_create.email}")

    # Validate invite code
    invite = await invite_manager.get_invite_by_code(user_create.invite_code)
    if not invite:
        raise HTTPException(status_code=400, detail="Invalid invite code")

    if invite.used:
        raise HTTPException(status_code=400, detail="Invite code already used")

    # Create user
    try:
        user = await user_manager.create(user_create)
    except InvalidPasswordException as e:
        raise HTTPException(status_code=400, detail=str(e)) from e

    # Mark invite as used
    await invite_manager.mark_invite_used(invite.id)

    # Generate access token
    access_token = await get_auth_backend().login(
        user_manager.strategy,
        user,
    )

    return LoginResponse(
        access_token=access_token.access_token,
        user_id=str(user.id),
    )


@auth_router.post("/login", response_model=LoginResponse)
async def login_user(
    request: LoginRequest,
    user_manager: UserManager = Depends(get_user_manager),
) -> LoginResponse:
    """
    Authenticate a user and return an access token.

    This endpoint validates user credentials and returns a JWT token
    for authenticated requests.
    """
    print(f"Login attempt for username: {request.username}")

    from sqlalchemy import select

    # Find user by username
    stmt = select(User).where(User.username == request.username)
    async with user_manager.user_db.session() as session:
        result = await session.execute(stmt)
        user = result.scalar_one_or_none()

    if not user:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    # Verify password
    try:
        await user_manager.authenticate(
            user_manager.user_db.get_user_by_username(request.username),
            request.password,
        )
    except Exception:
        raise HTTPException(status_code=401, detail="Invalid credentials") from None

    # Generate access token
    try:
        access_token = await get_auth_backend().login(
            user_manager.strategy,
            user,
        )
    except Exception as e:
        print(f"Token generation failed: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Token generation failed: {str(e)}") from e

    return LoginResponse(
        access_token=access_token.access_token,
        user_id=str(user.id),
    )


@auth_router.get("/me", response_model=dict[str, Any])
async def get_current_user_info(
    current_user: User = Depends(get_current_superuser),
) -> dict[str, Any]:
    """
    Get current user information.

    This endpoint returns information about the currently authenticated user.
    """
    return {
        "id": str(current_user.id),
        "email": current_user.email,
        "username": current_user.username,
        "is_superuser": current_user.is_superuser,
    }


@auth_router.get("/invites", response_model=list[InviteRead])
async def list_invites(
    current_user: User = Depends(get_current_superuser),
    invite_manager: InviteManager = Depends(get_invite_manager),
) -> list[InviteRead]:
    """
    List all invite codes (superuser only).

    This endpoint returns all invite codes in the system.
    Only superusers can access this endpoint.
    """
    invites = await invite_manager.get_all_invites()
    return [InviteRead.from_orm(invite) for invite in invites]


@auth_router.post("/invites", response_model=InviteRead)
async def create_invite(
    current_user: User = Depends(get_current_superuser),
    invite_manager: InviteManager = Depends(get_invite_manager),
) -> InviteRead:
    """
    Create a new invite code (superuser only).

    This endpoint generates a new invite code for user registration.
    Only superusers can create invite codes.
    """
    invite = await invite_manager.create_invite()
    return InviteRead.from_orm(invite)


# Note: FastAPI Users router is included in main.py to avoid route duplication
