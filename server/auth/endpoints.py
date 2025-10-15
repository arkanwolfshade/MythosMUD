"""
Authentication endpoints for MythosMUD.

This module provides endpoints for user registration, login, and authentication
management. It integrates with FastAPI Users for user management and includes
custom invite code validation.
"""

import uuid
from typing import Any

from fastapi import APIRouter, Depends, Request
from fastapi_users import schemas
from pydantic import BaseModel, field_validator
from sqlalchemy.ext.asyncio import AsyncSession

from ..database import get_async_session
from ..exceptions import LoggedHTTPException
from ..logging_config import get_logger
from ..models.user import User
from ..schemas.invite import InviteRead
from ..utils.error_logging import create_context_from_request
from .dependencies import get_current_active_user, get_current_superuser
from .invites import InviteManager, get_invite_manager
from .users import UserManager, get_user_manager

logger = get_logger("auth.endpoints")

# Create router for auth endpoints
auth_router = APIRouter(prefix="/auth", tags=["auth"])


# Define user schemas compatible with FastAPI Users v14
class UserRead(schemas.BaseUser[uuid.UUID]):
    """Schema for user read operations."""

    username: str


class UserUpdate(schemas.BaseUserUpdate):
    """Schema for user update operations."""

    username: str | None = None


# Define user creation schema
class UserCreate(BaseModel):
    """Schema for user creation with invite code validation."""

    username: str
    password: str
    invite_code: str | None = None
    email: str | None = None

    # Add password validation to reject empty passwords
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
    has_character: bool = True
    character_name: str | None = None


@auth_router.post("/register", response_model=LoginResponse)
async def register_user(
    user_create: UserCreate,
    request: Request,
    invite_manager: InviteManager = Depends(get_invite_manager),
    user_manager: UserManager = Depends(get_user_manager),
    session: AsyncSession = Depends(get_async_session),
) -> LoginResponse:
    """
    Register a new user with invite code validation.

    This endpoint validates the invite code and creates a new user account.
    The invite code is marked as used after successful registration.
    """
    # Check if server is shutting down
    from ..commands.admin_shutdown_command import get_shutdown_blocking_message, is_shutdown_pending

    if is_shutdown_pending(request.app):
        context = create_context_from_request(request)
        context.metadata["operation"] = "register_user"
        context.metadata["reason"] = "server_shutdown"
        raise LoggedHTTPException(status_code=503, detail=get_shutdown_blocking_message("login"), context=context)

    logger.info(f"Registration attempt for username: {user_create.username}")

    # Generate unique bogus email if not provided
    if not user_create.email:
        # Use a simple email format to avoid the complex generation
        user_create.email = f"{user_create.username}@wolfshade.org"
        logger.info(f"Generated simple bogus email for {user_create.username}: {user_create.email}")

    # Validate invite code (but don't use it yet)
    if user_create.invite_code:
        try:
            await invite_manager.validate_invite(user_create.invite_code, request)
        except LoggedHTTPException as e:
            raise e

    # Create user without invite_code field
    user_data = {"username": user_create.username, "password": user_create.password, "email": user_create.email}
    user_create_clean = UserCreate(**user_data)

    try:
        # Create user directly using SQLAlchemy to bypass FastAPI Users issues
        from sqlalchemy import select

        from ..models.user import User
        from .argon2_utils import hash_password

        # Check if username already exists
        stmt = select(User).where(User.username == user_create_clean.username)
        result = await session.execute(stmt)
        existing_user = result.scalar_one_or_none()

        if existing_user:
            context = create_context_from_request(request)
            context.metadata["username"] = user_create_clean.username
            context.metadata["operation"] = "register_user"
            raise LoggedHTTPException(status_code=400, detail="Username already exists", context=context)

        # Hash password using Argon2
        hashed_password = hash_password(user_create_clean.password)

        # Create user with explicit timestamps to avoid None issues
        from datetime import UTC, datetime

        # Create a minimal user object to avoid FastAPI Users issues
        user = User()
        user.username = user_create_clean.username
        user.email = user_create_clean.email
        user.hashed_password = hashed_password
        user.is_active = True
        user.is_superuser = False
        user.is_verified = False
        user.created_at = datetime.now(UTC).replace(tzinfo=None)
        user.updated_at = datetime.now(UTC).replace(tzinfo=None)

        session.add(user)
        await session.commit()
        await session.refresh(user)

    except LoggedHTTPException:
        raise
    except Exception as e:
        # Check if it's a duplicate username error
        constraint_error = "UNIQUE constraint failed: users.username"
        if constraint_error in str(e):
            context = create_context_from_request(request)
            context.metadata["username"] = user_create_clean.username
            context.metadata["operation"] = "register_user"
            context.metadata["constraint_error"] = constraint_error
            raise LoggedHTTPException(status_code=400, detail="Username already exists", context=context) from e
        # Re-raise other exceptions
        raise e

    # Store invite code in user session for later use during character creation
    # We'll mark it as used when the character is actually created
    logger.info(
        f"User {user.username} registered successfully - invite code reserved, player creation pending stats acceptance"
    )

    # Generate JWT token using FastAPI Users' built-in method
    import os

    from fastapi_users.jwt import generate_jwt

    # Create JWT token with the same format as FastAPI Users expects
    data = {"sub": str(user.id), "aud": ["fastapi-users:auth"]}
    jwt_secret = os.getenv("MYTHOSMUD_JWT_SECRET", "dev-jwt-secret")
    access_token = generate_jwt(
        data,
        jwt_secret,
        lifetime_seconds=3600,  # 1 hour
    )

    logger.debug(f"JWT token generated for user {user.username}")
    logger.debug(f"JWT data: {data}")
    logger.debug(f"JWT secret: {jwt_secret}")
    logger.debug(f"JWT token preview: {access_token[:50]}...")

    # Newly registered users don't have characters yet
    logger.info(f"Registration successful for user {user.username}, has_character: False")

    return LoginResponse(
        access_token=access_token,
        user_id=str(user.id),
        has_character=False,
        character_name=None,
    )


@auth_router.post("/login", response_model=LoginResponse)
async def login_user(
    request: LoginRequest,
    http_request: Request,
    user_manager: UserManager = Depends(get_user_manager),
    session: AsyncSession = Depends(get_async_session),
) -> LoginResponse:
    """
    Authenticate a user and return an access token.

    This endpoint validates user credentials and returns a JWT token
    for authenticated requests.
    """
    # Check if server is shutting down
    from ..commands.admin_shutdown_command import get_shutdown_blocking_message, is_shutdown_pending

    if is_shutdown_pending(http_request.app):
        context = create_context_from_request(http_request)
        context.metadata["operation"] = "login_user"
        context.metadata["reason"] = "server_shutdown"
        raise LoggedHTTPException(status_code=503, detail=get_shutdown_blocking_message("login"), context=context)

    logger.info(f"Login attempt for username: {request.username}")

    from sqlalchemy import select

    # Find user by username
    stmt = select(User).where(User.username == request.username)
    result = await session.execute(stmt)
    user = result.scalar_one_or_none()

    logger.info(f"User lookup result: {user}")

    if not user:
        logger.info(f"User not found: {request.username}")
        context = create_context_from_request(http_request)
        context.metadata["username"] = request.username
        context.metadata["operation"] = "login_user"
        raise LoggedHTTPException(status_code=401, detail="Invalid credentials", context=context)

    # Verify password using FastAPI Users with email lookup
    try:
        # Get the user's email for FastAPI Users authentication
        user_email = user.email
        if not user_email:
            logger.error(f"User {request.username} has no email address")
            context = create_context_from_request(http_request)
            context.metadata["username"] = request.username
            context.metadata["user_id"] = str(user.id)
            context.metadata["operation"] = "login_user"
            raise LoggedHTTPException(status_code=401, detail="Invalid credentials", context=context)

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
            context = create_context_from_request(http_request)
            context.metadata["username"] = request.username
            context.metadata["user_id"] = str(user.id)
            context.metadata["operation"] = "login_user"
            raise LoggedHTTPException(status_code=401, detail="Invalid credentials", context=context)

        # Verify we got the same user back
        if authenticated_user.id != user.id:
            logger.error(f"User ID mismatch: expected {user.id}, got {authenticated_user.id}")
            context = create_context_from_request(http_request)
            context.metadata["username"] = request.username
            context.metadata["expected_user_id"] = str(user.id)
            context.metadata["actual_user_id"] = str(authenticated_user.id)
            context.metadata["operation"] = "login_user"
            raise LoggedHTTPException(status_code=401, detail="Invalid credentials", context=context)
    except Exception as e:
        logger.error(f"Authentication failed: {str(e)}")
        context = create_context_from_request(http_request)
        context.metadata["username"] = request.username
        context.metadata["operation"] = "login_user"
        context.metadata["error"] = str(e)
        raise LoggedHTTPException(status_code=401, detail="Invalid credentials", context=context) from None

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

    # Check if user has a character
    from ..persistence import get_persistence

    persistence = get_persistence()
    player = persistence.get_player_by_user_id(str(user.id))

    has_character = player is not None
    character_name = player.name if player else None

    # CRITICAL FIX: Handle new game session to disconnect any existing connections
    # This prevents the duplicate login bug where the same player can be logged in multiple times
    if has_character and player:
        import uuid

        from ..realtime.connection_manager import connection_manager

        # Generate a new session ID for this login
        new_session_id = f"login_{uuid.uuid4().hex[:8]}"

        # Disconnect any existing connections for this player
        session_results = await connection_manager.handle_new_game_session(player.player_id, new_session_id)

        if session_results["success"]:
            logger.info(
                f"Login session management: Disconnected {session_results['connections_disconnected']} existing connections for player {player.player_id}"
            )
        else:
            logger.warning(
                f"Login session management failed for player {player.player_id}: {session_results['errors']}"
            )

    logger.info(f"Login successful for user {user.username}, has_character: {has_character}")

    return LoginResponse(
        access_token=access_token,
        user_id=str(user.id),
        has_character=has_character,
        character_name=character_name,
    )


@auth_router.get("/me", response_model=dict[str, Any])
async def get_current_user_info(
    current_user: User = Depends(get_current_active_user),
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


# Note: FastAPI Users authentication endpoints are included in app/factory.py
# to avoid duplicate operation ID warnings
