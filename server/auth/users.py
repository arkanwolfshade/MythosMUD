"""
FastAPI Users configuration for MythosMUD.

This module configures FastAPI Users with SQLAlchemy backend
for user authentication and management.
"""

import uuid

from fastapi import Depends, Request
from fastapi_users import BaseUserManager, FastAPIUsers
from fastapi_users.authentication import (
    AuthenticationBackend,
    BearerTransport,
    JWTStrategy,
)
from fastapi_users.db import SQLAlchemyUserDatabase
from sqlalchemy.ext.asyncio import AsyncSession

from ..database import get_async_session
from ..logging_config import get_logger
from ..models.user import User

logger = get_logger(__name__)


class UserManager(BaseUserManager[User, uuid.UUID]):
    """
    Custom user manager for MythosMUD.

    Extends FastAPI Users BaseUserManager to provide custom
    user creation and validation logic.
    """

    reset_password_token_secret = "SECRET"  # TODO: Move to env vars
    verification_token_secret = "SECRET"  # TODO: Move to env vars

    async def on_after_register(self, user: User, request: Request | None = None):
        """Handle post-registration logic."""
        logger.info(f"User {user.username} has registered.")

    async def on_after_forgot_password(self, user: User, token: str, request: Request | None = None):
        """Handle forgot password logic."""
        logger.info(f"User {user.username} has forgot their password. Reset token: {token}")

    async def on_after_request_verify(self, user: User, token: str, request: Request | None = None):
        """Handle username verification logic."""
        logger.info(f"Verification requested for user {user.username}. Verification token: {token}")


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
        return JWTStrategy(
            secret="SECRET",  # TODO: Move to env vars
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
