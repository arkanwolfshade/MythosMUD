"""
Integration test for the integration tier's own cleanup (#949).

The cleanup iterates the shared metadata's sorted_tables. A ForeignKey into npc_metadata once made
that raise NoReferencedTableError, which the fixture logged as a warning, so for months cleanup
deleted nothing and rows leaked between integration tests. This proves it really deletes.
"""

# pyright: reportPrivateUsage=false
# Reason: this module tests the integration fixtures' private cleanup helper directly.

import uuid

import pytest
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker

from server.models.user import User
from server.tests.fixtures.integration import _delete_mutable_integration_test_rows


@pytest.mark.asyncio
async def test_cleanup_deletes_rows_from_mutable_tables(
    session_factory: async_sessionmaker[AsyncSession],
) -> None:
    user_id = str(uuid.uuid4())
    async with session_factory() as session:
        session.add(
            User(
                id=user_id,
                email=f"cleanup_{user_id}@example.com",
                username=f"cleanup_{user_id[:8]}",
                display_name=f"Cleanup {user_id[:8]}",
                hashed_password="hashed",
                is_active=True,
                is_superuser=False,
                is_verified=True,
            )
        )
        await session.commit()

    async with session_factory() as session:
        await _delete_mutable_integration_test_rows(session)

    async with session_factory() as session:
        remaining = await session.get(User, user_id)

    assert remaining is None
