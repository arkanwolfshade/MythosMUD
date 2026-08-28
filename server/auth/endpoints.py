"""
Authentication endpoints for MythosMUD.

This module provides endpoints for user registration, login, and authentication
management. It integrates with FastAPI Users for user management and includes
custom invite code validation.
"""

import uuid
from typing import TYPE_CHECKING, Annotated, NoReturn, TypedDict, cast

from fastapi import APIRouter, Depends, HTTPException, Request
from fastapi.security import OAuth2PasswordRequestForm
from fastapi_users import schemas
from pydantic import BaseModel, Field, field_validator
from sqlalchemy.exc import IntegrityError, SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession

from ..async_persistence import AsyncPersistenceLayer
from ..auth_utils import create_access_token
from ..database import get_async_session
from ..dependencies import get_container
from ..exceptions import LoggedHTTPException
from ..models.user import User
from ..schemas.auth import InviteRead
from ..schemas.players import CharacterInfo
from ..structured_logging.enhanced_logging_config import get_logger
from .dependencies import get_current_active_user, get_current_superuser
from .invites import InviteManager, capture_invite, get_invite_manager, reserve_invite
from .token_epoch import get_auth_epoch
from .users import UserManager, get_user_manager, validate_jwt_secret

if TYPE_CHECKING:
    from ..container import ApplicationContainer
logger = get_logger("auth.endpoints")

# Maximum password length to prevent DoS attacks (matches argon2_utils.py)
MAX_PASSWORD_LENGTH = 1024

# Create router for auth endpoints
auth_router = APIRouter(prefix="/auth", tags=["auth"])


# Define user schemas compatible with FastAPI Users v14
class UserRead(schemas.BaseUser[uuid.UUID]):  # pylint: disable=too-few-public-methods  # Reason: Pydantic schema class, inherits methods from BaseUser
    """Schema for user read operations."""

    username: str


class UserUpdate(schemas.BaseUserUpdate):
    """Schema for user update operations."""

    username: str | None = None


# Mythos registration allows optional email (generated in _ensure_user_email). FastAPI Users
# get_register_router requires BaseUserCreate; factory.py casts at the call site.
class UserCreate(BaseModel):
    """Schema for user creation with invite code validation."""

    username: str
    password: str
    invite_code: str
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
        if len(v) > MAX_PASSWORD_LENGTH:
            raise ValueError(f"Password must not exceed {MAX_PASSWORD_LENGTH} characters")  # pylint: disable=redefined-outer-name  # Reason: MAX_PASSWORD_LENGTH is a module-level constant, not being redefined; Pylint false positive
        return v

    # Invite-only registration: reject absent/whitespace-only codes at the schema boundary
    # (server/api/real_time.py's websocket_player_id_fallback_allowed() config-gated pattern was
    # considered and rejected here - see #733's remediation grill - since no config surface for
    # relaxing this is needed anywhere in the codebase).
    @field_validator("invite_code")
    @classmethod
    def validate_invite_code(cls, v: str) -> str:
        """Validate invite code is present and non-blank."""
        if not v or not v.strip():
            raise ValueError("Invite code is required")
        return v


# Define login request schema
class LoginRequest(BaseModel):
    """Schema for login requests."""

    username: str
    password: str


# Define login response schema
class LoginResponse(BaseModel):
    """Schema for login responses.

    MULTI-CHARACTER: Updated to return list of characters instead of single character.
    """

    access_token: str
    token_type: str = "bearer"
    user_id: str
    characters: list[CharacterInfo] = Field(default_factory=list, description="List of active characters")


class CurrentUserInfo(TypedDict):
    """Payload for GET /auth/me."""

    id: str
    email: str | None
    username: str
    is_superuser: bool


def _check_shutdown_status(request: Request, operation: str = "register_user") -> None:
    """Check if server is shutting down and raise exception if so."""
    from ..commands.admin_shutdown_command import get_shutdown_blocking_message, is_shutdown_pending

    # Starlette types Request.app as Any; cast so reportAny does not fire at the call site.
    if is_shutdown_pending(cast(object, request.app)):
        raise LoggedHTTPException(
            status_code=503,
            detail=get_shutdown_blocking_message("login"),
            operation=operation,
            reason="server_shutdown",
        )


def _ensure_user_email(user_create: UserCreate) -> None:
    """Generate email if not provided."""
    if not user_create.email:
        user_create.email = f"{user_create.username}@wolfshade.org"
        logger.info("Generated simple bogus email", username=user_create.username, email=user_create.email)


def _build_clean_user_create(user_create: UserCreate) -> UserCreate:
    """Rebuild UserCreate via keyword args.

    Not **dict: mixing email (str|None) into a dict widens values to str|None.
    """
    return UserCreate(
        username=user_create.username,
        password=user_create.password,
        invite_code=user_create.invite_code,
        email=user_create.email,
    )


async def _check_username_exists(session: AsyncSession, username: str, _request: Request) -> None:
    """Check if username already exists and raise exception if so."""
    from sqlalchemy import text

    result = await session.execute(text("SELECT get_user_id_by_username_ci(:username)"), {"username": username})
    existing_user_id = result.scalar_one_or_none()

    if existing_user_id:
        raise LoggedHTTPException(
            status_code=400,
            detail="Username already exists (names are case-insensitive)",
            username=username,
            operation="register_user",
        )


def _create_user_object(user_create_clean: UserCreate) -> User:
    """Create and configure a new User object."""
    from datetime import UTC, datetime

    from .argon2_utils import hash_password

    hashed_password = hash_password(user_create_clean.password)

    user = User()
    user.username = user_create_clean.username
    user.display_name = user_create_clean.username
    # User.email is non-null; UserCreate.email is optional (filled by _ensure_user_email).
    user.email = user_create_clean.email or f"{user_create_clean.username}@wolfshade.org"
    user.hashed_password = hashed_password
    user.is_active = True
    user.is_superuser = False
    user.is_verified = False
    user.is_admin = False
    user.created_at = datetime.now(UTC).replace(tzinfo=None)
    user.updated_at = datetime.now(UTC).replace(tzinfo=None)

    return user


def _handle_integrity_error(e: IntegrityError, username: str, _request: Request) -> NoReturn:
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

    raise LoggedHTTPException(
        status_code=400,
        detail=detail,
        username=username,
        operation="register_user",
        constraint_error=str(e),
        original_error=orig_error_str if hasattr(e, "orig") else "",
    ) from e


async def _persist_new_user(
    session: AsyncSession, user_create: UserCreate, user_create_clean: UserCreate, request: Request
) -> User:
    """Reserve the invite, create and flush the user, capture the invite, commit.

    The DB-transaction core of register_user, split out so register_user itself stays a thin
    prep/response wrapper. Raises on any failure; the caller has nothing left to do afterward
    except build the response.
    """
    try:
        await reserve_invite(session, user_create.invite_code)

        await _check_username_exists(session, user_create_clean.username, request)

        user = _create_user_object(user_create_clean)

        session.add(user)
        await session.flush()

        await capture_invite(session, user, user_create.invite_code)

        await session.commit()
        await session.refresh(user)

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

    return user


def _generate_jwt_token(user: User) -> str:
    """Generate JWT token for user. Includes server auth epoch so tokens are invalid after restart."""
    data: dict[str, object] = {
        "sub": str(user.id),
        "aud": ["fastapi-users:auth"],
        "srv": get_auth_epoch(),
    }
    jwt_secret = validate_jwt_secret()
    access_token = create_access_token(data, secret_key=jwt_secret)
    logger.debug(
        "JWT token generated for user",
        username=user.username,
        data=data,
        jwt_secret=jwt_secret,
        token_preview=access_token[:50],
    )
    return access_token


@auth_router.post("/register", response_model=LoginResponse)
async def register_user(
    user_create: UserCreate,
    request: Request,
    invite_manager: Annotated[InviteManager, Depends(get_invite_manager)],
    session: Annotated[AsyncSession, Depends(get_async_session)],
) -> LoginResponse:
    """
    Register a new user with invite code validation.

    Invite enforcement follows an auth-and-capture model. reserve_invite (AUTH) takes a row
    lock on the invite and holds it for the rest of this transaction; capture_invite (CAPTURE)
    finalizes it after the user is flushed but still before commit. A failure anywhere between
    the two rolls the whole transaction back - releasing the lock and leaving the invite
    untouched - rather than leaving an orphaned account behind an already-used invite.
    """
    _check_shutdown_status(request)

    logger.info("Registration attempt", username=user_create.username)

    _ensure_user_email(user_create)

    # Early rejection (better logging, differentiated invalid/expired/used messages, fails
    # before any user object is built). Non-locking - authoritative enforcement against
    # concurrent reuse is the reserve/capture pair below.
    _ = await invite_manager.validate_invite(user_create.invite_code, request)

    user_create_clean = _build_clean_user_create(user_create)
    user = await _persist_new_user(session, user_create, user_create_clean, request)

    access_token = _generate_jwt_token(user)
    logger.info("Registration successful", username=user.username, user_id=user.id, character_count=0)

    return LoginResponse(
        access_token=access_token,
        user_id=str(user.id),
        characters=[],
    )


async def _find_user_by_username(session: AsyncSession, username: str, _http_request: Request) -> User:
    """Find user by username (case-insensitive). Raises exception if not found."""
    from sqlalchemy import text

    id_result = await session.execute(text("SELECT get_user_id_by_username_ci(:username)"), {"username": username})
    user_id = id_result.scalar_one_or_none()
    user = await session.get(User, user_id) if user_id else None

    logger.info("User lookup result", user=user)

    if not user:
        logger.info("User not found", username=username)
        raise LoggedHTTPException(
            status_code=401,
            detail="Invalid credentials",
            username=username,
            operation="login_user",
        )

    return user


def _invalid_credentials_exc(username: str, **context: str) -> LoggedHTTPException:
    """Build a 401 LoggedHTTPException for failed login credential checks."""
    return LoggedHTTPException(
        status_code=401,
        detail="Invalid credentials",
        operation="login_user",
        username=username,
        **context,
    )


async def _authenticate_user_credentials(
    user: User, password: str, username: str, user_manager: UserManager, _http_request: Request
) -> None:
    """Authenticate user credentials. Raises exception if authentication fails."""
    try:
        user_email = user.email
        if not user_email:
            logger.error("User has no email address", username=username)
            raise _invalid_credentials_exc(username, user_id=str(user.id))

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
            raise _invalid_credentials_exc(username, user_id=str(user.id))

        if authenticated_user.id != user.id:
            logger.error("User ID mismatch", expected_id=user.id, got_id=authenticated_user.id)
            raise _invalid_credentials_exc(
                username,
                expected_user_id=str(user.id),
                actual_user_id=str(authenticated_user.id),
            )
    except (LoggedHTTPException, HTTPException):
        raise
    except Exception as e:
        logger.error("Authentication failed", error=str(e), error_type=type(e).__name__)
        raise _invalid_credentials_exc(username, error=str(e)) from None


async def _get_user_characters(user: User, async_persistence: AsyncPersistenceLayer) -> list[CharacterInfo]:
    """Get all active characters for user."""
    active_players = await async_persistence.get_active_players_by_user_id(str(user.id))

    characters: list[CharacterInfo] = []
    for player in active_players:
        profession_name = None
        if player.profession_id and hasattr(async_persistence, "get_profession_by_id"):
            try:
                profession = await async_persistence.get_profession_by_id(int(player.profession_id))
                if profession:
                    profession_name = profession.name
            except SQLAlchemyError:
                pass

        characters.append(
            CharacterInfo(
                player_id=str(player.player_id),
                name=player.name,
                profession_id=player.profession_id,
                profession_name=profession_name,
                level=player.level,
                created_at=player.created_at,
                last_active=player.last_active,
            )
        )

    return characters


@auth_router.post("/login", response_model=LoginResponse)
async def login_user(
    request: LoginRequest,
    http_request: Request,
    user_manager: Annotated[UserManager, Depends(get_user_manager)],
    session: Annotated[AsyncSession, Depends(get_async_session)],
    container: Annotated["ApplicationContainer", Depends(get_container)],
) -> LoginResponse:
    """
    Authenticate a user and return an access token.

    This endpoint validates user credentials and returns a JWT token
    for authenticated requests.
    """
    _check_shutdown_status(http_request, "login_user")

    logger.info("Login attempt", username=request.username)

    user = await _find_user_by_username(session, request.username, http_request)

    await _authenticate_user_credentials(user, request.password, request.username, user_manager, http_request)

    access_token = _generate_jwt_token(user)

    # Container attributes are typed Any; narrow at the use site for reportAny.
    async_persistence = cast(AsyncPersistenceLayer | None, container.async_persistence)
    if async_persistence is None:
        logger.error("Async persistence layer not available during login", username=user.username)
        raise RuntimeError("Database connection not available")

    characters = await _get_user_characters(user, async_persistence)

    logger.info("Login successful for user", username=user.username, character_count=len(characters))

    return LoginResponse(
        access_token=access_token,
        user_id=str(user.id),
        characters=characters,
    )


@auth_router.get("/me", response_model=CurrentUserInfo)
async def get_current_user_info(
    current_user: Annotated[User, Depends(get_current_active_user)],
) -> CurrentUserInfo:
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
    _current_user: Annotated[User, Depends(get_current_superuser)],
    invite_manager: Annotated[InviteManager, Depends(get_invite_manager)],
) -> list[InviteRead]:
    """
    List all invite codes.

    This endpoint returns all invite codes in the system.
    """
    invites = await invite_manager.list_invites()
    return [InviteRead.model_validate(invite) for invite in invites]


@auth_router.post("/invites", response_model=InviteRead)
async def create_invite(
    _current_user: Annotated[User, Depends(get_current_superuser)],
    invite_manager: Annotated[InviteManager, Depends(get_invite_manager)],
) -> InviteRead:
    """
    Create a new invite code.

    This endpoint creates a new invite code for user registration.
    """
    invite = await invite_manager.create_invite()
    return InviteRead.model_validate(invite)


# Note: FastAPI Users authentication endpoints are included in app/factory.py
# to avoid duplicate operation ID warnings
