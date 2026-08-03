"""
Type stubs for fastapi_users.db module.

Provides type hints for SQLAlchemy user base classes used in FastAPI Users.

Plain attribute types match fastapi-users TYPE_CHECKING / UserProtocol so our
User model is accepted by AuthenticationBackend. SQLAlchemy column comparisons
against these stub fields may need a narrow type: ignore at call sites.
"""

from collections.abc import AsyncGenerator
from typing import Generic, TypeVar
from uuid import UUID

from sqlalchemy.ext.asyncio import AsyncSession

UP = TypeVar("UP")
ID = TypeVar("ID")

class SQLAlchemyBaseOAuthAccountTable:
    """Minimal stub for FastAPI Users OAuth account table base."""

    id: UUID
    oauth_name: str
    access_token: str
    account_id: str
    account_email: str
    user_id: UUID

class SQLAlchemyBaseUserTableUUID:
    """
    Base user table with UUID primary key for FastAPI Users.

    This stub provides proper type hints for the base class fields
    to enable better mypy checking and SQLAlchemy 2.0 compatibility.
    """

    # Primary key
    id: UUID

    # Authentication fields (plain types for UserProtocol structural match)
    email: str
    hashed_password: str

    # Status fields
    is_active: bool
    is_superuser: bool
    is_verified: bool

    def __init__(
        self,
        *,
        id: UUID = ...,
        email: str = ...,
        hashed_password: str = ...,
        is_active: bool = ...,
        is_superuser: bool = ...,
        is_verified: bool = ...,
    ) -> None: ...

class SQLAlchemyUserDatabase(Generic[UP, ID]):
    """User database adapter for SQLAlchemy."""

    def __init__(
        self,
        session: AsyncSession | AsyncGenerator[AsyncSession],
        user_table: type[UP],
        oauth_account_table: type[SQLAlchemyBaseOAuthAccountTable] | None = ...,
    ) -> None: ...
    async def get(self, id: ID) -> UP | None: ...
    async def get_by_email(self, email: str) -> UP | None: ...
    async def create(self, create_dict: dict[str, object]) -> UP: ...
    async def update(self, user: UP, update_dict: dict[str, object]) -> UP: ...
    async def delete(self, user: UP) -> None: ...
