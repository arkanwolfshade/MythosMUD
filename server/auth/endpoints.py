"""
Authentication endpoints for MythosMUD.

This module provides endpoints for user registration, login, and authentication
management. It integrates with FastAPI Users for user management and includes
custom invite code validation.
"""

import uuid
from typing import Any

from fastapi import APIRouter, Depends, HTTPException, Request
from fastapi_users import schemas
from pydantic import BaseModel, Field, field_validator
from sqlalchemy.exc import IntegrityError, SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession

from ..database import get_async_session
from ..exceptions import LoggedHTTPException
from ..models.user import User
from ..schemas.invite import InviteRead
from ..structured_logging.enhanced_logging_config import get_logger
from ..utils.error_logging import create_context_from_request
from .dependencies import get_current_active_user, get_current_superuser
from .invites import InviteManager, get_invite_manager
from .users import UserManager, get_user_manager

logger = get_logger("auth.endpoints")

# Create router for auth endpoints
auth_router = APIRouter(prefix="/auth", tags=["auth"])


# Define user schemas compatible with FastAPI Users v14
class UserRead(schemas.BaseUser[uuid.UUID]):  # pylint: disable=too-few-public-methods  # Reason: Pydantic schema class, inherits methods from BaseUser
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

    # Add password validation to reject empty passwords and enforce length limits
    @field_validator("password")
    @classmethod
    def validate_password(cls, v: str) -> str:
        """Validate password length and content."""
        if not v or not v.strip():
            raise ValueError("Password cannot be empty")
        if len(v) < 8:
            raise ValueError("Password must be at least 8 characters long")
        # Enforce maximum length to prevent DoS attacks (matches argon2_utils.py)
        MAX_PASSWORD_LENGTH = 1024
        if len(v) > MAX_PASSWORD_LENGTH:
            raise ValueError(f"Password must not exceed {MAX_PASSWORD_LENGTH} characters")
        return v


# Define login request schema
class LoginRequest(BaseModel):
    """Schema for login requests."""

    __slots__ = ()  # Performance optimization

    username: str
    password: str


# Define login response schema
class LoginResponse(BaseModel):
    """Schema for login responses.

    MULTI-CHARACTER: Updated to return list of characters instead of single character.
    """

    __slots__ = ()  # Performance optimization

    access_token: str
    token_type: str = "bearer"
    user_id: str
    characters: list[dict[str, Any]] = Field(default_factory=list, description="List of active characters")


def _check_shutdown_status(request: Request) -> None:
    """Check if server is shutting down and raise exception if so."""
    from ..commands.admin_shutdown_command import get_shutdown_blocking_message, is_shutdown_pending

    if is_shutdown_pending(request.app):
        context = create_context_from_request(request)
        context.metadata["operation"] = "register_user"
        context.metadata["reason"] = "server_shutdown"
        raise LoggedHTTPException(status_code=503, detail=get_shutdown_blocking_message("login"), context=context)


def _ensure_user_email(user_create: UserCreate) -> None:
    """Generate email if not provided."""
    if not user_create.email:
        user_create.email = f"{user_create.username}@wolfshade.org"
        logger.info("Generated simple bogus email", username=user_create.username, email=user_create.email)


async def _validate_invite_code(user_create: UserCreate, invite_manager: InviteManager, request: Request) -> Any:
    """Validate invite code. Returns validated invite or None."""
    if not user_create.invite_code:
        return None

    try:
        return await invite_manager.validate_invite(user_create.invite_code, request)
    except LoggedHTTPException as e:
        raise e


async def _check_username_exists(session: AsyncSession, username: str, request: Request) -> None:
    """Check if username already exists and raise exception if so."""
    from sqlalchemy import func, select

    stmt = select(User).where(func.lower(User.username) == func.lower(username))
    result = await session.execute(stmt)
    existing_user = result.scalar_one_or_none()

    if existing_user:
        context = create_context_from_request(request)
        context.metadata["username"] = username
        context.metadata["operation"] = "register_user"
        raise LoggedHTTPException(
            status_code=400,
            detail="Username already exists (names are case-insensitive)",
            context=context,
        )


def _create_user_object(user_create_clean: UserCreate) -> User:
    """Create and configure a new User object."""
    from datetime import UTC, datetime

    from .argon2_utils import hash_password

    hashed_password = hash_password(user_create_clean.password)

    user = User()
    user.username = user_create_clean.username
    user.display_name = user_create_clean.username
    user.email = user_create_clean.email
    user.hashed_password = hashed_password
    user.is_active = True
    user.is_superuser = False
    user.is_verified = False
    user.is_admin = False
    user.created_at = datetime.now(UTC).replace(tzinfo=None)
    user.updated_at = datetime.now(UTC).replace(tzinfo=None)

    return user


async def _mark_invite_as_used(
    session: AsyncSession, user: User, invite_code: str | None, validated_invite: Any
) -> None:
    """Mark invite as used after successful registration."""
    if not validated_invite or not invite_code:
        return

    try:
        from sqlalchemy import text

        await session.execute(
            text("""
                UPDATE invites
                SET is_active = :is_active, used_by_user_id = CAST(:used_by_user_id AS UUID)
                WHERE invite_code = :invite_code
            """),
            {
                "is_active": False,
                "used_by_user_id": str(user.id),
                "invite_code": invite_code,
            },
        )
        await session.commit()
        logger.info(
            "Invite marked as used during registration",
            invite_code=invite_code,
            user_id=user.id,
            username=user.username,
        )
    except SQLAlchemyError as invite_error:
        logger.error(
            "Failed to mark invite as used during registration",
            error=str(invite_error),
            error_type=type(invite_error).__name__,
            invite_code=invite_code,
            user_id=user.id,
        )


def _handle_integrity_error(e: IntegrityError, username: str, request: Request) -> None:
    """Handle IntegrityError during registration."""
    error_str = str(e).lower()
    orig_error_str = str(e.orig).lower() if hasattr(e, "orig") else ""
    combined_error = f"{error_str} {orig_error_str}".lower()

    if "username" in combined_error or "users_username_key" in combined_error:
        detail = "Username already exists"
    elif "email" in combined_error or "users_email_key" in combined_error:
        detail = "Email already exists"
    else:
        detail = "A user with this information already exists"

    context = create_context_from_request(request)
    context.metadata["username"] = username
    context.metadata["operation"] = "register_user"
    context.metadata["constraint_error"] = str(e)
    context.metadata["original_error"] = orig_error_str if hasattr(e, "orig") else ""
    raise LoggedHTTPException(status_code=400, detail=detail, context=context) from e


def _generate_jwt_token(user: User) -> str:
    """Generate JWT token for user."""
    import os

    from fastapi_users.jwt import generate_jwt

    data = {"sub": str(user.id), "aud": ["fastapi-users:auth"]}
    jwt_secret = os.getenv("MYTHOSMUD_JWT_SECRET", "dev-jwt-secret")
    access_token = generate_jwt(data, jwt_secret, lifetime_seconds=3600)

    logger.debug("JWT token generated for user", username=user.username)
    logger.debug("JWT data", data=data)
    logger.debug("JWT secret", jwt_secret=jwt_secret)
    logger.debug("JWT token preview", token_preview=access_token[:50])

    return access_token


@auth_router.post("/register", response_model=LoginResponse)
async def register_user(
    user_create: UserCreate,
    request: Request,
    invite_manager: InviteManager = Depends(get_invite_manager),
    session: AsyncSession = Depends(get_async_session),
) -> LoginResponse:
    """
    Register a new user with invite code validation.

    This endpoint validates the invite code and creates a new user account.
    The invite code is marked as used after successful registration.
    """
    _check_shutdown_status(request)

    logger.info("Registration attempt", username=user_create.username)

    _ensure_user_email(user_create)

    validated_invite = await _validate_invite_code(user_create, invite_manager, request)

    user_data = {"username": user_create.username, "password": user_create.password, "email": user_create.email}
    user_create_clean = UserCreate(**user_data)

    try:
        await _check_username_exists(session, user_create_clean.username, request)

        user = _create_user_object(user_create_clean)

        session.add(user)
        await session.commit()
        await session.refresh(user)

        await _mark_invite_as_used(session, user, user_create.invite_code, validated_invite)

    except LoggedHTTPException:
        raise
    except IntegrityError as e:
        _handle_integrity_error(e, user_create_clean.username, request)
    except HTTPException:
        raise
    except Exception as e:
        logger.error(
            "Unexpected error during registration",
            error=str(e),
            error_type=type(e).__name__,
            username=user_create_clean.username,
        )
        raise e

    logger.info("User registered successfully", username=user.username, user_id=user.id)

    access_token = _generate_jwt_token(user)

    logger.info("Registration successful for user", username=user.username, character_count=0)

    return LoginResponse(
        access_token=access_token,
        user_id=str(user.id),
        characters=[],
    )


def _check_login_shutdown_status(http_request: Request) -> None:
    """Check if server is shutting down and raise exception if so."""
    from ..commands.admin_shutdown_command import get_shutdown_blocking_message, is_shutdown_pending

    if is_shutdown_pending(http_request.app):
        context = create_context_from_request(http_request)
        context.metadata["operation"] = "login_user"
        context.metadata["reason"] = "server_shutdown"
        raise LoggedHTTPException(status_code=503, detail=get_shutdown_blocking_message("login"), context=context)


async def _find_user_by_username(session: AsyncSession, username: str, http_request: Request) -> User:
    """Find user by username (case-insensitive). Raises exception if not found."""
    from sqlalchemy import func, select

    stmt = select(User).where(func.lower(User.username) == func.lower(username))
    result = await session.execute(stmt)
    user = result.scalar_one_or_none()

    logger.info("User lookup result", user=user)

    if not user:
        logger.info("User not found", username=username)
        context = create_context_from_request(http_request)
        context.metadata["username"] = username
        context.metadata["operation"] = "login_user"
        raise LoggedHTTPException(status_code=401, detail="Invalid credentials", context=context)

    return user


async def _authenticate_user_credentials(
    user: User, password: str, username: str, user_manager: UserManager, http_request: Request
) -> None:
    """Authenticate user credentials. Raises exception if authentication fails."""
    try:
        user_email = user.email
        if not user_email:
            logger.error("User has no email address", username=username)
            context = create_context_from_request(http_request)
            context.metadata["username"] = username
            context.metadata["user_id"] = str(user.id)
            context.metadata["operation"] = "login_user"
            raise LoggedHTTPException(status_code=401, detail="Invalid credentials", context=context)

        from fastapi.security import OAuth2PasswordRequestForm

        credentials = OAuth2PasswordRequestForm(
            username=user_email,
            password=password,
            grant_type="password",
            scope="",
            client_id=None,
            client_secret=None,
        )

        authenticated_user = await user_manager.authenticate(credentials)
        if not authenticated_user:
            context = create_context_from_request(http_request)
            context.metadata["username"] = username
            context.metadata["user_id"] = str(user.id)
            context.metadata["operation"] = "login_user"
            raise LoggedHTTPException(status_code=401, detail="Invalid credentials", context=context)

        if authenticated_user.id != user.id:
            logger.error("User ID mismatch", expected_id=user.id, got_id=authenticated_user.id)
            context = create_context_from_request(http_request)
            context.metadata["username"] = username
            context.metadata["expected_user_id"] = str(user.id)
            context.metadata["actual_user_id"] = str(authenticated_user.id)
            context.metadata["operation"] = "login_user"
            raise LoggedHTTPException(status_code=401, detail="Invalid credentials", context=context)
    except (LoggedHTTPException, HTTPException):
        raise
    except Exception as e:
        logger.error("Authentication failed", error=str(e), error_type=type(e).__name__)
        context = create_context_from_request(http_request)
        context.metadata["username"] = username
        context.metadata["operation"] = "login_user"
        context.metadata["error"] = str(e)
        raise LoggedHTTPException(status_code=401, detail="Invalid credentials", context=context) from None


def _generate_login_jwt_token(user: User) -> str:
    """Generate JWT token for logged-in user."""
    import os

    from fastapi_users.jwt import generate_jwt

    data = {"sub": str(user.id), "aud": ["fastapi-users:auth"]}
    jwt_secret = os.getenv("MYTHOSMUD_JWT_SECRET", "dev-jwt-secret")
    return generate_jwt(data, jwt_secret, lifetime_seconds=3600)


async def _get_user_characters(user: User) -> list[dict[str, Any]]:
    """Get all active characters for user."""
    from ..async_persistence import get_async_persistence
    from ..schemas.player import CharacterInfo

    async_persistence = get_async_persistence()
    active_players = await async_persistence.get_active_players_by_user_id(str(user.id))

    characters = []
    for player in active_players:
        profession_name = None
        if player.profession_id and hasattr(async_persistence, "get_profession_by_id"):
            try:
                profession = await async_persistence.get_profession_by_id(int(player.profession_id))
                if profession:
                    profession_name = profession.name
            except SQLAlchemyError:
                pass

        character_info = CharacterInfo(
            player_id=str(player.player_id),
            name=player.name,
            profession_id=player.profession_id,
            profession_name=profession_name,
            level=player.level,
            created_at=player.created_at,
            last_active=player.last_active,
        )
        characters.append(character_info.model_dump())

    return characters


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
    _check_login_shutdown_status(http_request)

    logger.info("Login attempt", username=request.username)

    user = await _find_user_by_username(session, request.username, http_request)

    await _authenticate_user_credentials(user, request.password, request.username, user_manager, http_request)

    access_token = _generate_login_jwt_token(user)

    characters = await _get_user_characters(user)

    logger.info("Login successful for user", username=user.username, character_count=len(characters))

    return LoginResponse(
        access_token=access_token,
        user_id=str(user.id),
        characters=characters,
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
    _current_user: User = Depends(get_current_superuser),
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
    _current_user: User = Depends(get_current_superuser),
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
