"""
Integration tests for db/procedures/containers.sql's update_container() return-type change (#633).

update_container() was RETURNS void; #633 changed it to RETURNS uuid (the updated row's id, or
NULL) so server/persistence/container_persistence.py can detect "container not found" the same
way the raw UPDATE ... RETURNING it replaced did -- a scalar-function SELECT always returns
exactly one row, so callers must check the *value*, not row presence.
"""

import uuid

import pytest
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker


@pytest.fixture
async def container_row(session_factory: async_sessionmaker[AsyncSession]):
    """Create one container row. Yields its container_instance_id."""
    container_id = uuid.uuid4()
    async with session_factory() as session:
        await session.execute(
            text(
                "INSERT INTO containers (container_instance_id, source_type, lock_state, "
                "capacity_slots, created_at, updated_at) "
                "VALUES (:id, 'environment', 'unlocked', 5, now(), now())"
            ),
            {"id": container_id},
        )
        await session.commit()
    yield container_id


@pytest.mark.asyncio
async def test_update_container_found_returns_the_id(
    session_factory: async_sessionmaker[AsyncSession], container_row: uuid.UUID
) -> None:
    """update_container() on an existing container returns its id, and the row is updated."""
    async with session_factory() as session:
        result = await session.execute(
            text("SELECT update_container(:id, 'locked', NULL)"),
            {"id": container_row},
        )
        returned_id = result.scalar()
        assert returned_id is not None
        assert uuid.UUID(str(returned_id)) == container_row
        await session.commit()

        lock_state = (
            await session.execute(
                text("SELECT lock_state FROM containers WHERE container_instance_id = :id"),
                {"id": container_row},
            )
        ).scalar()
        assert lock_state == "locked"


@pytest.mark.asyncio
async def test_update_container_missing_container_returns_null(
    session_factory: async_sessionmaker[AsyncSession],
) -> None:
    """update_container() on a nonexistent container_instance_id returns NULL, no exception."""
    async with session_factory() as session:
        result = await session.execute(
            text("SELECT update_container(:id, 'locked', NULL)"),
            {"id": uuid.uuid4()},
        )
        assert result.scalar() is None


@pytest.mark.asyncio
async def test_update_container_null_fields_leave_them_unchanged(
    session_factory: async_sessionmaker[AsyncSession], container_row: uuid.UUID
) -> None:
    """NULL p_lock_state/p_metadata_json leave the existing values alone (COALESCE), matching
    the dynamic-UPDATE-builder behavior this procedure replaces."""
    async with session_factory() as session:
        await session.execute(text("SELECT update_container(:id, NULL, NULL)"), {"id": container_row})
        await session.commit()

        lock_state = (
            await session.execute(
                text("SELECT lock_state FROM containers WHERE container_instance_id = :id"),
                {"id": container_row},
            )
        ).scalar()
        assert lock_state == "unlocked"
