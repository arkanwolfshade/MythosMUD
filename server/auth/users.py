"""
FastAPI Users configuration for MythosMUD.

This module configures FastAPI Users with SQLAlchemy backend
for user authentication and management.
"""

import os
import uuid
from collections.abc import AsyncGenerator
from typing import Any, cast

from fastapi import Depends, HTTPException, Request
from fastapi_users import BaseUserManager, FastAPIUsers, UUIDIDMixin
from fastapi_users.authentication import AuthenticationBackend, BearerTransport
from fastapi_users.db import SQLAlchemyUserDatabase
from fastapi_users.exceptions import InvalidID
from sqlalchemy.ext.asyncio import AsyncSession

from server.auth.jwt_strategy import RestartInvalidatingJWTStrategy

from ..database import get_async_session
from ..models.user import User
from ..structured_logging.enhanced_logging_config import get_logger
from .argon2_utils import hash_password, verify_password
from .email_utils import is_bogus_email

logger = get_logger(__name__)


class UserManager(UUIDIDMixin, BaseUserManager[User, uuid.UUID]):
    """
    Custom user manager for MythosMUD.

    Extends FastAPI Users BaseUserManager to provide custom
    user creation and validation logic with Argon2 password hashing.
    """

    def __init__(self, user_db: SQLAlchemyUserDatabase) -> None:
        """Initialize UserManager with validated secrets."""
        super().__init__(user_db)
        # Validate and set token secrets from environment
        reset_secret = os.getenv("MYTHOSMUD_RESET_TOKEN_SECRET")
        if not reset_secret or reset_secret.startswith("dev-"):
            raise ValueError("MYTHOSMUD_RESET_TOKEN_SECRET must be set to a secure value (not starting with 'dev-')")
        self.reset_password_token_secret = reset_secret

        verification_secret = os.getenv("MYTHOSMUD_VERIFICATION_TOKEN_SECRET")
        if not verification_secret or verification_secret.startswith("dev-"):
            raise ValueError(
                "MYTHOSMUD_VERIFICATION_TOKEN_SECRET must be set to a secure value (not starting with 'dev-')"
            )
        self.verification_token_secret = verification_secret

    def _hash_password(self, password: str) -> str:
        """Hash password using Argon2 instead of bcrypt."""
        return hash_password(password)

    def _verify_password(self, plain_password: str, hashed_password: str) -> bool:
        """Verify password using Argon2 instead of bcrypt."""
        return verify_password(plain_password, hashed_password)

    async def on_after_register(self, user: User, request: Request | None = None) -> None:
        """Handle post-registration logic."""
        logger.info("User has registered", username=user.username)

        # Auto-verify bogus emails for privacy protection
        if user.email and is_bogus_email(user.email):
            user.is_verified = True
            logger.info("Auto-verified bogus email for user", username=user.username, email=user.email)

    async def on_after_forgot_password(self, user: User, token: str, request: Request | None = None) -> None:
        """Handle forgot password logic."""
        logger.info("User has forgot their password", username=user.username, reset_token=token)

    async def on_after_request_verify(self, user: User, token: str, request: Request | None = None) -> None:
        """Handle username verification logic."""
        logger.info("Verification requested for user", username=user.username, verification_token=token)

    def parse_id(self, value: Any) -> uuid.UUID:
        """Parse a value into a UUID instance."""
        if isinstance(value, uuid.UUID):
            return value
        # Convert non-string values to string first
        if not isinstance(value, str):
            try:
                value = str(value)
            except Exception as err:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: String conversion errors unpredictable, must raise InvalidID
                raise InvalidID() from err
        try:
            return uuid.UUID(value)
        except (ValueError, TypeError, AttributeError) as err:
            raise InvalidID() from err


async def get_user_db(
    session: AsyncSession = Depends(get_async_session),
) -> AsyncGenerator[SQLAlchemyUserDatabase, None]:
    """Get user database dependency."""
    yield SQLAlchemyUserDatabase(session, User)


async def get_user_manager(
    user_db: SQLAlchemyUserDatabase = Depends(get_user_db),
) -> AsyncGenerator[UserManager, None]:
    """Get user manager dependency."""
    yield UserManager(user_db)


def _validate_jwt_secret() -> str:
    """
    Validate and return JWT secret from environment.

    Raises ValueError if secret is not set or starts with "dev-".
    """
    jwt_secret = os.getenv("MYTHOSMUD_JWT_SECRET")
    if not jwt_secret:
        raise ValueError(
            "MYTHOSMUD_JWT_SECRET environment variable must be set. "
            "Generate a secure random key for production deployment."
        )
    if jwt_secret.startswith("dev-"):
        raise ValueError(
            "MYTHOSMUD_JWT_SECRET must not start with 'dev-'. "
            "This indicates an insecure development secret. "
            "Generate a secure random key for production deployment."
        )
    return jwt_secret


def get_auth_backend() -> AuthenticationBackend[User, uuid.UUID]:  # type: ignore[type-var]
    """Get authentication backend configuration."""

    # Bearer token transport
    bearer_transport = BearerTransport(tokenUrl="auth/jwt/login")

    # JWT strategy - invalidates all tokens after server restart
    def get_jwt_strategy() -> RestartInvalidatingJWTStrategy[User, uuid.UUID]:  # type: ignore[type-var]
        jwt_secret = _validate_jwt_secret()
        return RestartInvalidatingJWTStrategy(
            secret=jwt_secret,
            lifetime_seconds=3600,  # 1 hour
            token_audience=["fastapi-users:auth"],
        )

    return AuthenticationBackend(  # type: ignore[type-var]
        name="jwt",
        transport=bearer_transport,
        get_strategy=get_jwt_strategy,
    )


class UsernameAuthenticationBackend(AuthenticationBackend):  # type: ignore[type-arg]
    """Custom authentication backend that uses username instead of email."""

    def __init__(self, name: str, transport: Any, get_strategy: Any) -> None:
        super().__init__(name, transport, get_strategy)

    async def login(self, strategy: Any, user: Any) -> Any:
        """Custom login that uses username."""
        # Note: Parent class login signature is (strategy, user), not (strategy, user_manager, user)
        return await super().login(strategy, user)


def get_username_auth_backend() -> UsernameAuthenticationBackend:
    """Get username-based authentication backend configuration."""

    # Bearer token transport
    bearer_transport = BearerTransport(tokenUrl="auth/jwt/login")

    # JWT strategy - invalidates all tokens after server restart
    def get_jwt_strategy() -> RestartInvalidatingJWTStrategy[User, uuid.UUID]:  # type: ignore[type-var]
        jwt_secret = _validate_jwt_secret()
        return RestartInvalidatingJWTStrategy(
            secret=jwt_secret,
            lifetime_seconds=3600,  # 1 hour
            token_audience=["fastapi-users:auth"],
        )

    return UsernameAuthenticationBackend(
        name="jwt",
        transport=bearer_transport,
        get_strategy=get_jwt_strategy,
    )


# Create authentication backends
auth_backend = get_auth_backend()

# Create FastAPI Users instance
fastapi_users = FastAPIUsers[User, uuid.UUID](
    get_user_manager,
    [auth_backend],
)

# Export commonly used functions
get_current_user = fastapi_users.current_user(optional=True)
get_current_active_user = fastapi_users.current_user(active=True)


# Enhanced logging wrapper for get_current_user (returns FastAPI Depends dependency)
def get_current_user_with_logging() -> Any:
    """Enhanced get_current_user with detailed logging."""

    async def _get_current_user_with_logging(request: Request | None = None) -> dict[str, Any] | None:
        try:
            # Log the request details
            auth_header = request.headers.get("Authorization", "Not provided") if request else "No request"
            auth_preview = (
                auth_header[:50] + "..." if auth_header != "Not provided" and len(auth_header) > 50 else auth_header
            )
            logger.debug("Authentication attempt - Auth header", auth_preview=auth_preview)

            # Get the raw dependency result
            user = await get_current_user(request)

            if user:
                logger.info("Authentication successful for user", username=user.username, user_id=user.id)
            else:
                logger.warning("Authentication failed: No user returned from get_current_user")

            result: dict[Any, Any] | None = cast(dict[Any, Any] | None, user)
            return result
        except HTTPException as e:
            logger.warning("Authentication HTTP error", status_code=e.status_code, detail=e.detail)
            return None
        except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Authentication errors unpredictable, must return None
            logger.error("Unexpected authentication error", error_type=type(e).__name__, error=str(e))
            logger.debug("Authentication error details", error_type=type(e).__name__, error=str(e))
            return None

    return Depends(_get_current_user_with_logging)
