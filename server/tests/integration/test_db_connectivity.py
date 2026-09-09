"""
Integration test for database connectivity.
"""

import uuid

import pytest
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker

from server.models.user import User


@pytest.fixture
async def cleanup_test_user(session_factory: async_sessionmaker[AsyncSession]):
    """Yield a fresh user id and guarantee its row is deleted after the test, pass or fail --
    independent of whatever the test itself commits. Deleting cascades to any dependent rows."""
    user_id = str(uuid.uuid4())
    yield user_id
    async with session_factory() as session:
        _ = await session.execute(text("DELETE FROM users WHERE id = :id"), {"id": user_id})
        await session.commit()


@pytest.mark.asyncio
async def test_db_connectivity_create_and_read_user(
    session_factory: async_sessionmaker[AsyncSession], cleanup_test_user: str
):
    """
    Test that we can create and read a User from the database.
    """
    user_id = cleanup_test_user

    async with session_factory() as session:
        # Create a user
        user = User(
            id=user_id,
            email=f"test_{user_id}@example.com",
            username=f"testuser_{user_id[:8]}",
            display_name=f"Test User {user_id[:8]}",
            hashed_password="hashed_password",
            is_active=True,
            is_superuser=False,
            is_verified=True,
        )
        session.add(user)
        await session.commit()

        # Read it back
        fetched = await session.get(User, user_id)

        assert fetched is not None
        assert fetched.id == user_id
        assert fetched.username == user.username
        assert fetched.email == user.email
