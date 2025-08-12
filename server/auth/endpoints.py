"""
Authentication endpoints for MythosMUD.

This module provides endpoints for user registration, login, and authentication
management. It integrates with FastAPI Users for user management and includes
custom invite code validation.
"""

from typing import Any

from fastapi import APIRouter, Depends, HTTPException
from fastapi_users import InvalidPasswordException
from fastapi_users.exceptions import UserAlreadyExists
from fastapi_users.schemas import BaseUserCreate
from pydantic import BaseModel
from sqlalchemy.ext.asyncio import AsyncSession

from ..database import get_async_session
from ..logging_config import get_logger
from ..models.user import User
from ..schemas.invite import InviteRead
from .dependencies import get_current_superuser
from .invites import InviteManager, get_invite_manager
from .users import UserManager, auth_backend, fastapi_users, get_user_manager

logger = get_logger("auth.endpoints")

# Create router for auth endpoints
auth_router = APIRouter(prefix="/auth", tags=["auth"])


# Define user schemas
class UserRead(BaseModel):
    """Schema for user read operations."""

    id: str
    username: str
    email: str | None = None
    is_active: bool = True
    is_superuser: bool = False
    is_verified: bool = False


class UserUpdate(BaseModel):
    """Schema for user update operations."""

    username: str | None = None
    email: str | None = None
    password: str | None = None


# Define user creation schema
class UserCreate(BaseUserCreate):
    """Schema for user creation with invite code validation."""

    username: str
    invite_code: str | None = None

    # Override email to make it optional
    email: str | None = None

    # Add password validation to reject empty passwords
    from pydantic import field_validator

    @field_validator("password")
    @classmethod
    def validate_password_not_empty(cls, v: str) -> str:
        """Validate that password is not empty."""
        if not v or not v.strip():
            raise ValueError("Password cannot be empty")
        return v


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
    logger.info(f"Registration attempt for username: {user_create.username}")

    # Generate bogus email if not provided
    if not user_create.email:
        user_create.email = f"{user_create.username}@wolfshade.org"

    # Validate invite code (but don't use it yet)
    try:
        await invite_manager.validate_invite(user_create.invite_code)
    except HTTPException as e:
        raise e

    # Create user without invite_code field
    user_data = user_create.model_dump(exclude={"invite_code"})
    user_create_clean = UserCreate(**user_data)

    try:
        user = await user_manager.create(user_create_clean)
    except InvalidPasswordException as e:
        raise HTTPException(status_code=400, detail=str(e)) from e
    except UserAlreadyExists as e:
        raise HTTPException(status_code=400, detail="Username already exists") from e
    except Exception as e:
        # Check if it's a duplicate username error
        constraint_error = "UNIQUE constraint failed: users.username"
        if constraint_error in str(e):
            raise HTTPException(status_code=400, detail="Username already exists") from e
        # Re-raise other exceptions
        raise e

    # Store invite code in user session for later use during character creation
    # We'll mark it as used when the character is actually created
    logger.info(f"User {user.username} registered successfully - invite code reserved, player creation pending stats acceptance")

    # Generate access token using FastAPI Users approach
    import os

    from fastapi_users.jwt import generate_jwt

    # Create JWT token manually (without invite code to avoid validation issues)
    data = {
        "sub": str(user.id),
        "aud": ["fastapi-users:auth"]
    }
    jwt_secret = os.getenv("MYTHOSMUD_JWT_SECRET", "dev-jwt-secret")
    access_token = generate_jwt(
        data,
        jwt_secret,
        lifetime_seconds=3600,  # 1 hour
    )

    return LoginResponse(
        access_token=access_token,
        user_id=str(user.user_id),
    )


@auth_router.post("/login", response_model=LoginResponse)
async def login_user(
    request: LoginRequest,
    user_manager: UserManager = Depends(get_user_manager),
    session: AsyncSession = Depends(get_async_session),
) -> LoginResponse:
    """
    Authenticate a user and return an access token.

    This endpoint validates user credentials and returns a JWT token
    for authenticated requests.
    """
    logger.info(f"Login attempt for username: {request.username}")

    from sqlalchemy import select

    # Find user by username
    stmt = select(User).where(User.username == request.username)
    result = await session.execute(stmt)
    user = result.scalar_one_or_none()

    logger.info(f"User lookup result: {user}")

    if not user:
        logger.warning(f"User not found: {request.username}")
        raise HTTPException(status_code=401, detail="Invalid credentials")

    # Verify password using FastAPI Users with email lookup
    try:
        # Get the user's email for FastAPI Users authentication
        user_email = user.email
        if not user_email:
            logger.error(f"User {request.username} has no email address")
            raise HTTPException(status_code=401, detail="Invalid credentials")

        # Create OAuth2PasswordRequestForm for FastAPI Users authentication
        from fastapi.security import OAuth2PasswordRequestForm

        # Create credentials form with email (not username) for FastAPI Users
        credentials = OAuth2PasswordRequestForm(
            username=user_email,  # Use email for FastAPI Users
            password=request.password,
            grant_type="password",
            scope="",
            client_id=None,
            client_secret=None,
        )

        # Use the user manager's authenticate method with email
        authenticated_user = await user_manager.authenticate(credentials)
        if not authenticated_user:
            raise HTTPException(status_code=401, detail="Invalid credentials")

        # Verify we got the same user back
        if authenticated_user.user_id != user.user_id:
            logger.error(f"User ID mismatch: expected {user.user_id}, got {authenticated_user.user_id}")
            raise HTTPException(status_code=401, detail="Invalid credentials")
    except Exception as e:
        logger.error(f"Authentication failed: {str(e)}")
        raise HTTPException(status_code=401, detail="Invalid credentials") from None

    # Generate access token using FastAPI Users approach
    import os

    from fastapi_users.jwt import generate_jwt

    # Create JWT token manually using the same secret as the auth backend
    data = {"sub": str(user.id), "aud": ["fastapi-users:auth"]}
    jwt_secret = os.getenv("MYTHOSMUD_JWT_SECRET", "dev-jwt-secret")
    access_token = generate_jwt(
        data,
        jwt_secret,
        lifetime_seconds=3600,  # 1 hour
    )

    return LoginResponse(
        access_token=access_token,
        user_id=str(user.user_id),
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
        "id": str(current_user.user_id),
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
    List all invite codes.

    This endpoint returns all invite codes in the system.
    """
    return await invite_manager.list_invites()


@auth_router.post("/invites", response_model=InviteRead)
async def create_invite(
    current_user: User = Depends(get_current_superuser),
    invite_manager: InviteManager = Depends(get_invite_manager),
) -> InviteRead:
    """
    Create a new invite code.

    This endpoint creates a new invite code for user registration.
    """
    return await invite_manager.create_invite()


# Include FastAPI Users authentication endpoints
auth_router.include_router(fastapi_users.get_auth_router(auth_backend), prefix="/jwt", tags=["auth"])
auth_router.include_router(fastapi_users.get_register_router(UserRead, UserCreate), prefix="/jwt", tags=["auth"])
auth_router.include_router(fastapi_users.get_users_router(UserRead, UserUpdate), prefix="/users", tags=["users"])
