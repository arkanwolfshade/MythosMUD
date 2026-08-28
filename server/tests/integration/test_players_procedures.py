"""
Integration tests for db/procedures/players.sql's #633/#733 additions:
get_user_id_by_username_ci() and the reserve_invite/capture_invite auth-and-capture pair
(#733 - replaces the old, non-atomic mark_invite_used). These are the only tests that actually
pin the DDL/procedure change: unit tests mock the session and cannot exercise real row locking.
"""

import asyncio
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
async def test_reserve_invite_true_for_active_code(
    session_factory: async_sessionmaker[AsyncSession], invite_row: str
) -> None:
    async with session_factory() as session:
        result = await session.execute(text("SELECT reserve_invite(:code)"), {"code": invite_row})
        assert bool(result.scalar()) is True
        await session.commit()


@pytest.mark.asyncio
async def test_reserve_invite_false_for_unknown_code(
    session_factory: async_sessionmaker[AsyncSession],
) -> None:
    async with session_factory() as session:
        result = await session.execute(text("SELECT reserve_invite(:code)"), {"code": "does-not-exist"})
        assert bool(result.scalar()) is False
        await session.commit()


@pytest.mark.asyncio
async def test_capture_invite_after_reserve_deactivates_and_records_user(
    session_factory: async_sessionmaker[AsyncSession], invite_row: str, user_row: tuple[uuid.UUID, str]
) -> None:
    """reserve_invite then capture_invite in the same transaction (the real auth-and-capture shape)."""
    user_id, _username = user_row
    async with session_factory() as session:
        reserved = await session.execute(text("SELECT reserve_invite(:code)"), {"code": invite_row})
        assert bool(reserved.scalar()) is True

        captured = await session.execute(
            text("SELECT capture_invite(:code, :user_id)"),
            {"code": invite_row, "user_id": user_id},
        )
        assert bool(captured.scalar()) is True
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
async def test_capture_invite_unknown_code_returns_false(
    session_factory: async_sessionmaker[AsyncSession], user_row: tuple[uuid.UUID, str]
) -> None:
    user_id, _username = user_row
    async with session_factory() as session:
        result = await session.execute(
            text("SELECT capture_invite(:code, :user_id)"),
            {"code": "does-not-exist", "user_id": user_id},
        )
        assert bool(result.scalar()) is False
        await session.commit()


@pytest.mark.asyncio
async def test_capture_invite_second_call_returns_false(
    session_factory: async_sessionmaker[AsyncSession], invite_row: str, user_row: tuple[uuid.UUID, str]
) -> None:
    """A caller that captures twice for the same code (skipping a fresh reserve) gets false the
    second time - defense-in-depth for a caller that violates the reserve-then-capture contract."""
    user_id, _username = user_row
    async with session_factory() as session:
        _ = await session.execute(text("SELECT reserve_invite(:code)"), {"code": invite_row})
        first = await session.execute(
            text("SELECT capture_invite(:code, :user_id)"), {"code": invite_row, "user_id": user_id}
        )
        assert bool(first.scalar()) is True
        second = await session.execute(
            text("SELECT capture_invite(:code, :user_id)"), {"code": invite_row, "user_id": user_id}
        )
        assert bool(second.scalar()) is False
        await session.commit()


@pytest.mark.asyncio
async def test_reserve_invite_blocks_concurrent_reservation_until_release(
    session_factory: async_sessionmaker[AsyncSession], invite_row: str, user_row: tuple[uuid.UUID, str]
) -> None:
    """Two sessions racing reserve_invite() on the same code: the second's reserve_invite() call
    blocks at the database level (row lock from FOR UPDATE) until the first's transaction ends,
    then correctly sees the post-commit state and returns false. This is the actual race #733's
    auth-and-capture design closes - the unit tests can only mock this, not exercise it."""
    user_id, _username = user_row
    winner_result: list[bool] = []
    loser_result: list[bool] = []

    async def holder() -> None:
        async with session_factory() as session:
            reserved = await session.execute(text("SELECT reserve_invite(:code)"), {"code": invite_row})
            winner_result.append(bool(reserved.scalar()))
            # Hold the lock briefly so the racer's reserve_invite() call is guaranteed to block
            # inside Postgres, not just get lucky with ordering.
            await asyncio.sleep(0.3)
            _ = await session.execute(
                text("SELECT capture_invite(:code, :user_id)"), {"code": invite_row, "user_id": user_id}
            )
            await session.commit()

    async def racer() -> None:
        await asyncio.sleep(0.05)  # let holder acquire the lock first
        async with session_factory() as session:
            reserved = await session.execute(text("SELECT reserve_invite(:code)"), {"code": invite_row})
            loser_result.append(bool(reserved.scalar()))
            await session.commit()

    _ = await asyncio.gather(holder(), racer())

    assert winner_result == [True]
    assert loser_result == [False]
