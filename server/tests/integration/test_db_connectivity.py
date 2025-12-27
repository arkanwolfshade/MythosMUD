"""
Integration test for database connectivity.
"""

import pytest

from server.models.user import User


@pytest.mark.asyncio
@pytest.mark.serial  # Ensure this runs serially to avoid event loop conflicts
async def test_db_connectivity_create_and_read_user(session_factory):
    """
    Test that we can create and read a User from the database.

    CRITICAL: This test is marked as serial to ensure it runs sequentially
    and avoids Windows event loop issues with asyncpg.
    """
    import uuid

    async with session_factory() as session:
        # Create a user
        user_id = str(uuid.uuid4())
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
