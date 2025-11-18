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
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

from ..database import get_async_session
from ..exceptions import LoggedHTTPException
from ..logging.enhanced_logging_config import get_logger
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

    __slots__ = ()  # Performance optimization

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

    __slots__ = ()  # Performance optimization

    username: str
    password: str


# Define login response schema
class LoginResponse(BaseModel):
    """Schema for login responses."""

    __slots__ = ()  # Performance optimization

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

    logger.info("Registration attempt", username=user_create.username)

    # Generate unique bogus email if not provided
    if not user_create.email:
        # Use a simple email format to avoid the complex generation
        user_create.email = f"{user_create.username}@wolfshade.org"
        logger.info("Generated simple bogus email", username=user_create.username, email=user_create.email)

    # Validate invite code
    validated_invite = None
    if user_create.invite_code:
        try:
            validated_invite = await invite_manager.validate_invite(user_create.invite_code, request)
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
        user.display_name = user_create_clean.username  # Default display_name to username
        user.email = user_create_clean.email
        user.hashed_password = hashed_password
        user.is_active = True
        user.is_superuser = False
        user.is_verified = False
        user.is_admin = False  # New users are not admins by default
        user.created_at = datetime.now(UTC).replace(tzinfo=None)
        user.updated_at = datetime.now(UTC).replace(tzinfo=None)

        session.add(user)
        await session.commit()
        await session.refresh(user)

        # Mark invite as used now that user registration is successful
        if validated_invite and user_create.invite_code:
            try:
                # Re-query the invite in the current session to ensure it's attached
                from sqlalchemy import text

                # Use raw SQL update to avoid UUID type mismatch issues
                # Cast used_by_user_id to UUID in the SQL to match the column type
                await session.execute(
                    text("""
                        UPDATE invites
                        SET is_active = :is_active, used_by_user_id = CAST(:used_by_user_id AS UUID)
                        WHERE invite_code = :invite_code
                    """),
                    {
                        "is_active": False,
                        "used_by_user_id": str(user.id),
                        "invite_code": user_create.invite_code,
                    },
                )
                await session.commit()
                logger.info(
                    "Invite marked as used during registration",
                    invite_code=user_create.invite_code,
                    user_id=user.id,
                    username=user.username,
                )
            except Exception as invite_error:
                # Log error but don't fail registration if invite marking fails
                logger.error(
                    "Failed to mark invite as used during registration",
                    error=str(invite_error),
                    error_type=type(invite_error).__name__,
                    invite_code=user_create.invite_code,
                    user_id=user.id,
                )

    except LoggedHTTPException:
        raise
    except IntegrityError as e:
        # Handle database integrity constraint violations (duplicate username, email, etc.)
        error_str = str(e).lower()
        constraint_errors = [
            "unique constraint failed: users.username",  # SQLite
            "duplicate key value violates unique constraint",  # PostgreSQL
            "unique_violation",  # PostgreSQL error code
            "users_username_key",  # PostgreSQL constraint name
            "users_email_key",  # PostgreSQL constraint name for email
        ]
        # Check if it's a unique constraint violation
        if any(err in error_str for err in constraint_errors):
            # Determine if it's username or email constraint
            if "username" in error_str or "users_username_key" in error_str:
                detail = "Username already exists"
            elif "email" in error_str or "users_email_key" in error_str:
                detail = "Email already exists"
            else:
                detail = "A user with this information already exists"

            context = create_context_from_request(request)
            context.metadata["username"] = user_create_clean.username
            context.metadata["operation"] = "register_user"
            context.metadata["constraint_error"] = str(e)
            raise LoggedHTTPException(status_code=400, detail=detail, context=context) from e
        # Re-raise other integrity errors
        raise e
    except Exception as e:
        # Re-raise other exceptions
        raise e

    logger.info("User registered successfully", username=user.username, user_id=user.id)

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

    logger.debug("JWT token generated for user", username=user.username)
    logger.debug("JWT data", data=data)
    logger.debug("JWT secret", jwt_secret=jwt_secret)
    logger.debug("JWT token preview", token_preview=access_token[:50])

    # Newly registered users don't have characters yet
    logger.info("Registration successful for user", username=user.username, has_character=False)

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

    logger.info("Login attempt", username=request.username)

    from sqlalchemy import select

    # Find user by username
    stmt = select(User).where(User.username == request.username)
    result = await session.execute(stmt)
    user = result.scalar_one_or_none()

    logger.info("User lookup result", user=user)

    if not user:
        logger.info("User not found", username=request.username)
        context = create_context_from_request(http_request)
        context.metadata["username"] = request.username
        context.metadata["operation"] = "login_user"
        raise LoggedHTTPException(status_code=401, detail="Invalid credentials", context=context)

    # Verify password using FastAPI Users with email lookup
    try:
        # Get the user's email for FastAPI Users authentication
        user_email = user.email
        if not user_email:
            logger.error("User has no email address", username=request.username)
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
            logger.error("User ID mismatch", expected_id=user.id, got_id=authenticated_user.id)
            context = create_context_from_request(http_request)
            context.metadata["username"] = request.username
            context.metadata["expected_user_id"] = str(user.id)
            context.metadata["actual_user_id"] = str(authenticated_user.id)
            context.metadata["operation"] = "login_user"
            raise LoggedHTTPException(status_code=401, detail="Invalid credentials", context=context)
    except Exception as e:
        logger.error("Authentication failed", error=str(e))
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

        # AI Agent: Get connection_manager from container instead of global import
        #           Use http_request (the FastAPI Request), not request (the LoginRequest body)
        connection_manager = http_request.app.state.container.connection_manager

        # Generate a new session ID for this login
        new_session_id = f"login_{uuid.uuid4().hex[:8]}"

        # Disconnect any existing connections for this player
        session_results = await connection_manager.handle_new_game_session(str(player.player_id), new_session_id)

        if session_results["success"]:
            logger.info(
                f"Login session management: Disconnected {session_results['connections_disconnected']} existing connections for player {player.player_id}"
            )
        else:
            logger.warning(
                f"Login session management failed for player {player.player_id}: {session_results['errors']}"
            )

    logger.info("Login successful for user", username=user.username, has_character=has_character)

    return LoginResponse(
        access_token=access_token,
        user_id=str(user.id),
        has_character=has_character,
        character_name=character_name,  # type: ignore[arg-type]
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


@auth_router.get("/invites")
async def list_invites(
    current_user: User = Depends(get_current_superuser),
    invite_manager: InviteManager = Depends(get_invite_manager),
) -> list[dict]:
    """
    List all invite codes.

    This endpoint returns all invite codes in the system.
    """
    invites = await invite_manager.list_invites()
    return [
        {
            "id": str(invite.id),
            "invite_code": invite.invite_code,
            "is_active": invite.is_active,
            "used_by_user_id": str(invite.used_by_user_id) if invite.used_by_user_id else None,
            "expires_at": invite.expires_at.isoformat() if invite.expires_at else None,
            "created_at": invite.created_at.isoformat() if invite.created_at else None,
        }
        for invite in invites
    ]


@auth_router.post("/invites", response_model=InviteRead)
async def create_invite(
    current_user: User = Depends(get_current_superuser),
    invite_manager: InviteManager = Depends(get_invite_manager),
) -> dict[str, Any]:  # Return dict for better performance
    """
    Create a new invite code.

    This endpoint creates a new invite code for user registration.
    """
    invite = await invite_manager.create_invite()
    # Convert SQLAlchemy model to Pydantic schema, then to dict
    invite_read = InviteRead.model_validate(invite)
    return invite_read.model_dump()


# Note: FastAPI Users authentication endpoints are included in app/factory.py
# to avoid duplicate operation ID warnings
