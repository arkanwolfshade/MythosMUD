"""
Integration tests for db/procedures/experience.sql's #879 rewrite: level_for_xp() and
award_player_xp(). Replaces the old update_player_xp() (XP-only, no level) --
ExperienceRepository is the only caller, but the row-locking and level curve can only be
proven against a real database; unit tests mock the session.
"""

# pyright: reportAny=false
# SQLAlchemy's raw Row attribute access (row.new_xp etc.) has no static column typing here --
# the columns come from a raw `text()` query, not a typed ORM select.

import uuid

import pytest
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker


@pytest.fixture
async def player_row(session_factory: async_sessionmaker[AsyncSession]):
    """Create a user and a player row (level 1, 0 XP, the schema defaults). Yields player_id."""
    user_id = uuid.uuid4()
    player_id = uuid.uuid4()
    username = f"xp_test_{uuid.uuid4().hex[:8]}"
    async with session_factory() as session:
        _ = await session.execute(
            text(
                "INSERT INTO users (id, username, display_name, email, hashed_password, is_active) "
                + "VALUES (:id, :username, :username, :email, 'hashed', true)"
            ),
            {"id": user_id, "username": username, "email": f"{username}@example.com"},
        )
        _ = await session.execute(
            text("INSERT INTO players (player_id, user_id, name) VALUES (:player_id, :user_id, :name)"),
            {"player_id": player_id, "user_id": user_id, "name": username},
        )
        await session.commit()
    yield player_id
    async with session_factory() as session:
        _ = await session.execute(text("DELETE FROM users WHERE id = :id"), {"id": user_id})
        await session.commit()


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "xp,expected_level",
    [(0, 1), (99, 1), (100, 2), (299, 2), (300, 3), (4500, 10)],
)
async def test_level_for_xp_boundaries(
    session_factory: async_sessionmaker[AsyncSession], xp: int, expected_level: int
) -> None:
    """total(L) = 50*L*(L-1): L2=100, L3=300, L10=4500. Boundaries land exactly, not off-by-one."""
    async with session_factory() as session:
        level = (await session.execute(text("SELECT level_for_xp(:xp)"), {"xp": xp})).scalar()
        assert level == expected_level


@pytest.mark.asyncio
async def test_award_player_xp_below_first_level_up_does_not_change_level(
    session_factory: async_sessionmaker[AsyncSession], player_row: uuid.UUID
) -> None:
    async with session_factory() as session:
        row = (
            await session.execute(
                text("SELECT * FROM award_player_xp(:player_id, :delta)"),
                {"player_id": player_row, "delta": 50},
            )
        ).one()
        await session.commit()
        assert row.new_xp == 50
        assert row.old_level == 1
        assert row.new_level == 1


@pytest.mark.asyncio
async def test_award_player_xp_crossing_boundary_levels_up(
    session_factory: async_sessionmaker[AsyncSession], player_row: uuid.UUID
) -> None:
    async with session_factory() as session:
        row = (
            await session.execute(
                text("SELECT * FROM award_player_xp(:player_id, :delta)"),
                {"player_id": player_row, "delta": 100},
            )
        ).one()
        await session.commit()
        assert row.new_xp == 100
        assert row.old_level == 1
        assert row.new_level == 2


@pytest.mark.asyncio
async def test_award_player_xp_is_monotonic_never_decreases_level(
    session_factory: async_sessionmaker[AsyncSession], player_row: uuid.UUID
) -> None:
    """A player boosted straight to a high level by one award, then given a tiny follow-up
    award, must not have their level recomputed down to what that tiny amount alone implies."""
    async with session_factory() as session:
        _ = await session.execute(
            text("SELECT * FROM award_player_xp(:player_id, :delta)"), {"player_id": player_row, "delta": 4500}
        )
        await session.commit()
        row = (
            await session.execute(
                text("SELECT * FROM award_player_xp(:player_id, :delta)"),
                {"player_id": player_row, "delta": 1},
            )
        ).one()
        await session.commit()
        assert row.old_level == 10
        assert row.new_level == 10


@pytest.mark.asyncio
async def test_award_player_xp_rejects_negative_delta(
    session_factory: async_sessionmaker[AsyncSession], player_row: uuid.UUID
) -> None:
    async with session_factory() as session:
        with pytest.raises(Exception, match="non-negative"):
            _ = await session.execute(
                text("SELECT * FROM award_player_xp(:player_id, :delta)"),
                {"player_id": player_row, "delta": -1},
            )
        await session.rollback()


@pytest.mark.asyncio
async def test_award_player_xp_unknown_player_returns_no_row(
    session_factory: async_sessionmaker[AsyncSession],
) -> None:
    async with session_factory() as session:
        row = (
            await session.execute(
                text("SELECT * FROM award_player_xp(:player_id, :delta)"),
                {"player_id": uuid.uuid4(), "delta": 10},
            )
        ).one_or_none()
        assert row is None
