"""
Type stubs for fastapi_users package.

Provides type hints for FastAPI Users authentication library.
"""

from collections.abc import AsyncGenerator, Awaitable, Callable, Sequence
from typing import Generic, TypeVar
from uuid import UUID

from fastapi import APIRouter
from fastapi.security import OAuth2PasswordRequestForm
from starlette.requests import Request

from .authentication import AuthenticationBackend
from .db import SQLAlchemyUserDatabase

UP = TypeVar("UP")  # User Protocol
UC = TypeVar("UC")  # User Create schema
UU = TypeVar("UU")  # User Update schema
U = TypeVar("U")  # Public user schema
ID = TypeVar("ID")  # User ID type

class UUIDIDMixin:
    """Mixin for UUID-based user IDs."""

    def parse_id(self, value: object) -> UUID: ...

class BaseUserManager(Generic[UP, ID]):
    """Base user manager for handling user operations."""

    def __init__(
        self,
        user_db: SQLAlchemyUserDatabase[UP, ID],
        password_helper: object | None = ...,
    ) -> None: ...
    async def get(self, id: ID) -> UP | None: ...
    async def get_by_email(self, email: str) -> UP | None: ...
    async def create(
        self,
        user_create: object,
        safe: bool = ...,
        request: Request | None = ...,
    ) -> UP: ...
    async def update(
        self,
        user_update: object,
        user: UP,
        safe: bool = ...,
        request: Request | None = ...,
    ) -> UP: ...
    async def delete(self, user: UP) -> None: ...
    async def authenticate(self, credentials: OAuth2PasswordRequestForm) -> UP | None: ...
    async def on_after_register(self, user: UP, request: Request | None = ...) -> None: ...
    async def on_after_update(
        self,
        user: UP,
        update_dict: dict[str, object],
        request: Request | None = ...,
    ) -> None: ...
    async def on_after_request_verify(
        self,
        user: UP,
        token: str,
        request: Request | None = ...,
    ) -> None: ...
    async def on_after_verify(self, user: UP, request: Request | None = ...) -> None: ...
    async def on_after_forgot_password(
        self,
        user: UP,
        token: str,
        request: Request | None = ...,
    ) -> None: ...
    async def on_after_reset_password(self, user: UP, request: Request | None = ...) -> None: ...

class FastAPIUsers(Generic[UP, ID]):
    """Main FastAPI Users class for authentication management."""

    def __init__(
        self,
        # Real fastapi-users uses a FastAPI Depends that yields UserManager.
        get_user_manager: Callable[
            ...,
            AsyncGenerator[BaseUserManager[UP, ID]] | Awaitable[BaseUserManager[UP, ID]] | BaseUserManager[UP, ID],
        ],
        auth_backends: Sequence[AuthenticationBackend[UP, ID]],
    ) -> None: ...
    def get_auth_router(
        self,
        backend: AuthenticationBackend[UP, ID],
        requires_verification: bool = ...,
    ) -> APIRouter: ...
    def get_register_router(
        self,
        user_schema: type[U],
        user_create_schema: type[UC],
    ) -> APIRouter: ...
    def get_verify_router(
        self,
        user_schema: type[U],
    ) -> APIRouter: ...
    def get_reset_password_router(self) -> APIRouter: ...
    def get_users_router(
        self,
        user_schema: type[U],
        user_update_schema: type[UU],
        requires_verification: bool = ...,
    ) -> APIRouter: ...
    def current_user(
        self,
        active: bool = ...,
        verified: bool = ...,
        superuser: bool = ...,
        optional: bool = ...,
    ) -> Callable[..., Awaitable[UP | None]]: ...

__all__ = ["AuthenticationBackend", "BaseUserManager", "FastAPIUsers", "UUIDIDMixin"]
