"""
Integration tests for db/procedures/players.sql's #633 additions:
get_user_id_by_username_ci() and mark_invite_used(). Replace raw SQL/ORM previously inline in
server/auth/endpoints.py.
"""

import uuid

import pytest
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker


@pytest.fixture
async def user_row(session_factory: async_sessionmaker[AsyncSession]):
    """Create one user with a mixed-case username. Yields (user_id, username)."""
    user_id = uuid.uuid4()
    username = f"TestUser_{uuid.uuid4().hex[:8]}"
    async with session_factory() as session:
        await session.execute(
            text(
                "INSERT INTO users (id, username, display_name, email, hashed_password, is_active) "
                "VALUES (:id, :username, :username, :email, 'hashed', true)"
            ),
            {"id": user_id, "username": username, "email": f"{username}@example.com"},
        )
        await session.commit()
    yield user_id, username


@pytest.mark.asyncio
async def test_get_user_id_by_username_ci_matches_regardless_of_case(
    session_factory: async_sessionmaker[AsyncSession], user_row: tuple[uuid.UUID, str]
) -> None:
    user_id, username = user_row
    async with session_factory() as session:
        found = (
            await session.execute(
                text("SELECT get_user_id_by_username_ci(:username)"),
                {"username": username.upper()},
            )
        ).scalar()
        assert found is not None
        assert uuid.UUID(str(found)) == user_id


@pytest.mark.asyncio
async def test_get_user_id_by_username_ci_unknown_username_returns_null(
    session_factory: async_sessionmaker[AsyncSession],
) -> None:
    async with session_factory() as session:
        found = (
            await session.execute(text("SELECT get_user_id_by_username_ci(:username)"), {"username": "nobody_here"})
        ).scalar()
        assert found is None


@pytest.fixture
async def invite_row(session_factory: async_sessionmaker[AsyncSession]):
    """Create one active invite. Yields its invite_code."""
    invite_code = f"TEST-{uuid.uuid4().hex[:8]}"
    async with session_factory() as session:
        await session.execute(
            text("INSERT INTO invites (id, invite_code, is_active) VALUES (:id, :code, true)"),
            {"id": uuid.uuid4(), "code": invite_code},
        )
        await session.commit()
    yield invite_code


@pytest.mark.asyncio
async def test_mark_invite_used_deactivates_and_records_user(
    session_factory: async_sessionmaker[AsyncSession], invite_row: str, user_row: tuple[uuid.UUID, str]
) -> None:
    user_id, _username = user_row
    async with session_factory() as session:
        result = await session.execute(
            text("SELECT mark_invite_used(:code, :user_id)"),
            {"code": invite_row, "user_id": user_id},
        )
        assert bool(result.scalar()) is True
        await session.commit()

        row = (
            (
                await session.execute(
                    text("SELECT is_active, used_by_user_id FROM invites WHERE invite_code = :code"),
                    {"code": invite_row},
                )
            )
            .mappings()
            .one()
        )
        assert row["is_active"] is False
        assert row["used_by_user_id"] == user_id


@pytest.mark.asyncio
async def test_mark_invite_used_unknown_code_returns_false(
    session_factory: async_sessionmaker[AsyncSession], user_row: tuple[uuid.UUID, str]
) -> None:
    user_id, _username = user_row
    async with session_factory() as session:
        result = await session.execute(
            text("SELECT mark_invite_used(:code, :user_id)"),
            {"code": "does-not-exist", "user_id": user_id},
        )
        assert bool(result.scalar()) is False
