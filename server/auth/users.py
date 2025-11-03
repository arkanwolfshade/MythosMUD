"""
FastAPI Users configuration for MythosMUD.

This module configures FastAPI Users with SQLAlchemy backend
for user authentication and management.
"""

import os
import uuid
from typing import Any

from fastapi import Depends, Request
from fastapi_users import BaseUserManager, FastAPIUsers, UUIDIDMixin
from fastapi_users.authentication import (
    AuthenticationBackend,
    BearerTransport,
    JWTStrategy,
)
from fastapi_users.db import SQLAlchemyUserDatabase
from fastapi_users.exceptions import InvalidID
from sqlalchemy.ext.asyncio import AsyncSession

from ..database import get_async_session
from ..logging.enhanced_logging_config import get_logger
from ..models.user import User
from .argon2_utils import hash_password, verify_password
from .email_utils import is_bogus_email

logger = get_logger(__name__)


class UserManager(UUIDIDMixin, BaseUserManager[User, uuid.UUID]):
    """
    Custom user manager for MythosMUD.

    Extends FastAPI Users BaseUserManager to provide custom
    user creation and validation logic with Argon2 password hashing.
    """

    # Use environment variables for all secrets - CRITICAL: Must be set in production
    reset_password_token_secret = os.getenv("MYTHOSMUD_RESET_TOKEN_SECRET", "dev-reset-secret")
    verification_token_secret = os.getenv("MYTHOSMUD_VERIFICATION_TOKEN_SECRET", "dev-verification-secret")

    def _hash_password(self, password: str) -> str:
        """Hash password using Argon2 instead of bcrypt."""
        return hash_password(password)

    def _verify_password(self, plain_password: str, hashed_password: str) -> bool:
        """Verify password using Argon2 instead of bcrypt."""
        return verify_password(plain_password, hashed_password)

    async def on_after_register(self, user: User, request: Request | None = None):
        """Handle post-registration logic."""
        logger.info("User has registered", username=user.username)

        # Auto-verify bogus emails for privacy protection
        if user.email and is_bogus_email(user.email):
            user.is_verified = True
            logger.info("Auto-verified bogus email for user", username=user.username, email=user.email)

    async def on_after_forgot_password(self, user: User, token: str, request: Request | None = None):
        """Handle forgot password logic."""
        logger.info("User has forgot their password", username=user.username, reset_token=token)

    async def on_after_request_verify(self, user: User, token: str, request: Request | None = None):
        """Handle username verification logic."""
        logger.info("Verification requested for user", username=user.username, verification_token=token)

    def parse_id(self, value: Any) -> uuid.UUID:
        """Parse a value into a UUID instance."""
        if isinstance(value, uuid.UUID):
            return value
        try:
            return uuid.UUID(value)
        except (ValueError, TypeError) as err:
            raise InvalidID() from err


async def get_user_db(session: AsyncSession = Depends(get_async_session)):
    """Get user database dependency."""
    yield SQLAlchemyUserDatabase(session, User)


async def get_user_manager(user_db: SQLAlchemyUserDatabase = Depends(get_user_db)):
    """Get user manager dependency."""
    yield UserManager(user_db)


def get_auth_backend() -> AuthenticationBackend:
    """Get authentication backend configuration."""

    # Bearer token transport
    bearer_transport = BearerTransport(tokenUrl="auth/jwt/login")

    # JWT strategy - return a function that creates the strategy
    def get_jwt_strategy() -> JWTStrategy:
        # Use environment variable for JWT secret - CRITICAL: Must be set in production
        jwt_secret = os.getenv("MYTHOSMUD_JWT_SECRET", "dev-jwt-secret")
        return JWTStrategy(
            secret=jwt_secret,
            lifetime_seconds=3600,  # 1 hour
            token_audience=["fastapi-users:auth"],
        )

    return AuthenticationBackend(
        name="jwt",
        transport=bearer_transport,
        get_strategy=get_jwt_strategy,
    )


class UsernameAuthenticationBackend(AuthenticationBackend):
    """Custom authentication backend that uses username instead of email."""

    def __init__(self, name: str, transport, get_strategy):
        super().__init__(name, transport, get_strategy)

    async def login(self, strategy, user_manager, user):
        """Custom login that uses username."""
        return await super().login(strategy, user_manager, user)


def get_username_auth_backend() -> UsernameAuthenticationBackend:
    """Get username-based authentication backend configuration."""

    # Bearer token transport
    bearer_transport = BearerTransport(tokenUrl="auth/jwt/login")

    # JWT strategy - return a function that creates the strategy
    def get_jwt_strategy() -> JWTStrategy:
        return JWTStrategy(
            secret="SECRET",  # TODO: Move to env vars
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


# Enhanced logging wrapper for get_current_user
def get_current_user_with_logging():
    """Enhanced get_current_user with detailed logging."""
    logger = get_logger(__name__)

    async def _get_current_user_with_logging(request: Request | None = None) -> dict | None:
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

            return user
        except Exception as e:
            logger.error("Authentication error", error_type=type(e).__name__, error=str(e))
            logger.debug("Authentication error details", error_type=type(e).__name__, error=str(e))
            return None

    return Depends(_get_current_user_with_logging)
