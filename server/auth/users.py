"""
FastAPI Users configuration for MythosMUD.

This module configures FastAPI Users with SQLAlchemy backend
for user authentication and management.
"""

import os
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
from ..models.user import User


class UserManager(BaseUserManager[User, uuid.UUID]):
    """
    Custom user manager for MythosMUD.

    Extends FastAPI Users BaseUserManager to provide custom
    user creation and validation logic.
    """

    # Use environment variables for all secrets - CRITICAL: Must be set in production
    reset_password_token_secret = os.getenv("MYTHOSMUD_RESET_TOKEN_SECRET", "dev-reset-secret")
    verification_token_secret = os.getenv("MYTHOSMUD_VERIFICATION_TOKEN_SECRET", "dev-verification-secret")

    async def on_after_register(self, user: User, request: Request | None = None):
        """Handle post-registration logic."""
        print(f"User {user.email} has registered.")

    async def on_after_forgot_password(self, user: User, token: str, request: Request | None = None):
        """Handle forgot password logic."""
        print(f"User {user.email} has forgot their password. Reset token: {token}")

    async def on_after_request_verify(self, user: User, token: str, request: Request | None = None):
        """Handle email verification logic."""
        print(f"Verification requested for user {user.email}. Verification token: {token}")


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
