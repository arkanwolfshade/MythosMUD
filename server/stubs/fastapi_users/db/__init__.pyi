"""
Type stubs for fastapi_users.db module.

Provides type hints for SQLAlchemy user base classes used in FastAPI Users.
"""

from collections.abc import AsyncGenerator
from typing import Any
from uuid import UUID

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Mapped

class SQLAlchemyBaseUserTableUUID:
    """
    Base user table with UUID primary key for FastAPI Users.

    This stub provides proper type hints for the base class fields
    to enable better mypy checking and SQLAlchemy 2.0 compatibility.
    """

    # Primary key
    id: Mapped[UUID]

    # Authentication fields
    email: Mapped[str | None]
    hashed_password: Mapped[str]

    # Status fields
    is_active: Mapped[bool]
    is_superuser: Mapped[bool]
    is_verified: Mapped[bool]

    def __init__(self, **kwargs: Any) -> None: ...

class SQLAlchemyUserDatabase:
    """User database adapter for SQLAlchemy."""

    def __init__(
        self,
        session: AsyncSession | AsyncGenerator[AsyncSession, None],
        user_table: type[SQLAlchemyBaseUserTableUUID],
    ) -> None: ...
    async def get(self, id: UUID) -> SQLAlchemyBaseUserTableUUID | None: ...
    async def get_by_email(self, email: str) -> SQLAlchemyBaseUserTableUUID | None: ...
    async def create(self, create_dict: dict[str, Any]) -> SQLAlchemyBaseUserTableUUID: ...
    async def update(
        self, user: SQLAlchemyBaseUserTableUUID, update_dict: dict[str, Any]
    ) -> SQLAlchemyBaseUserTableUUID: ...
    async def delete(self, user: SQLAlchemyBaseUserTableUUID) -> None: ...
