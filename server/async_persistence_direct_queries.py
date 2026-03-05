"""
Direct async SQL queries used by AsyncPersistenceLayer.

Extracted to keep async_persistence.py under file-nloc limit.
"""

from sqlalchemy import func, select
from sqlalchemy.exc import SQLAlchemyError

from .database import get_async_session
from .exceptions import DatabaseError, ValidationError
from .models.profession import Profession
from .models.user import User
from .utils.error_logging import log_and_raise


async def fetch_user_by_username_case_insensitive(username: str) -> User | None:
    """
    Get a user by username (case-insensitive).

    MULTI-CHARACTER: Usernames are stored case-sensitively but checked case-insensitively.
    """
    try:
        async for session in get_async_session():
            stmt = select(User).where(func.lower(User.username) == func.lower(username))
            result = await session.execute(stmt)
            return result.scalar_one_or_none()
        return None
    except (DatabaseError, ValidationError, SQLAlchemyError) as e:
        log_and_raise(
            DatabaseError,
            f"Database error retrieving user by username '{username}': {e}",
            operation="get_user_by_username_case_insensitive",
            username=username,
            details={"username": username, "error": str(e)},
            user_friendly="Failed to retrieve user information",
        )


async def fetch_professions() -> list[Profession]:
    """Get all available professions using SQLAlchemy ORM."""
    try:
        async for session in get_async_session():
            stmt = select(Profession).where(Profession.is_available.is_(True)).order_by(Profession.id)
            result = await session.execute(stmt)
            return list(result.scalars().all())
        return []
    except (SQLAlchemyError, OSError) as e:
        log_and_raise(
            DatabaseError,
            f"Database error retrieving professions: {e}",
            operation="async_get_professions",
            details={"error": str(e)},
            user_friendly="Failed to retrieve professions",
        )
