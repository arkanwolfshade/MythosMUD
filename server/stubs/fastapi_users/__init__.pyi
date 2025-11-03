"""
Type stubs for fastapi_users package.

Provides type hints for FastAPI Users authentication library.
"""

from typing import Any, Generic, TypeVar

from .db import SQLAlchemyUserDatabase

# Type-only imports to avoid runtime dependencies in stub files
APIRouter = Any  # Forward reference to avoid importing fastapi
AuthenticationBackend = Any  # Forward reference to avoid importing fastapi_users.authentication

# Type variables - using Any bound to be more permissive
UP = TypeVar("UP")  # User Protocol - accepts any user type
UC = TypeVar("UC")  # User Create - accepts any schema
UU = TypeVar("UU")  # User Update - accepts any schema
ID = TypeVar("ID")  # User ID type

class UUIDIDMixin:
    """Mixin for UUID-based user IDs."""

    ...

class BaseUserManager(Generic[UP, ID]):
    """Base user manager for handling user operations."""

    def __init__(
        self,
        user_db: SQLAlchemyUserDatabase,
        **kwargs: Any,
    ) -> None: ...
    async def get(self, id: ID) -> UP | None: ...
    async def get_by_email(self, email: str) -> UP | None: ...
    async def create(self, user_create: Any, safe: bool = ..., request: Any = ...) -> UP: ...
    async def update(self, user_update: Any, user: UP, safe: bool = ..., request: Any = ...) -> UP: ...
    async def delete(self, user: UP) -> None: ...
    async def authenticate(self, credentials: Any) -> UP | None: ...
    async def on_after_register(self, user: UP, request: Any | None = ...) -> None: ...
    async def on_after_update(self, user: UP, update_dict: dict[str, Any], request: Any | None = ...) -> None: ...
    async def on_after_request_verify(self, user: UP, token: str, request: Any | None = ...) -> None: ...
    async def on_after_verify(self, user: UP, request: Any | None = ...) -> None: ...
    async def on_after_forgot_password(self, user: UP, token: str, request: Any | None = ...) -> None: ...
    async def on_after_reset_password(self, user: UP, request: Any | None = ...) -> None: ...

class FastAPIUsers(Generic[UP, ID]):
    """Main FastAPI Users class for authentication management."""

    def __init__(
        self,
        get_user_manager: Any,
        auth_backends: list[AuthenticationBackend],
    ) -> None: ...
    def get_auth_router(
        self,
        backend: AuthenticationBackend,
        requires_verification: bool = ...,
    ) -> APIRouter: ...
    def get_register_router(
        self,
        user_schema: Any,  # Relaxed typing to accept any schema
        user_create_schema: Any,
    ) -> APIRouter: ...
    def get_verify_router(
        self,
        user_schema: Any,
    ) -> APIRouter: ...
    def get_reset_password_router(self) -> APIRouter: ...
    def get_users_router(
        self,
        user_schema: Any,  # Relaxed typing to accept any schema
        user_update_schema: Any,
        requires_verification: bool = ...,
    ) -> APIRouter: ...
    def current_user(
        self,
        active: bool = ...,
        verified: bool = ...,
        superuser: bool = ...,
        optional: bool = ...,
    ) -> Any: ...

__all__ = ["BaseUserManager", "FastAPIUsers", "UUIDIDMixin"]
