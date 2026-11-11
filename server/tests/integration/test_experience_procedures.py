"""
Integration tests for XP and level against a real database (ADR-029 step 7b).

The registry grants XP now, using the curve in ``models.player_xp``; the SQL function ``level_for_xp`` is the curve's
reference. These tests pin the two together, prove an award reaches the database through the registry, and prove a
``save_player`` of a copy loaded before the award cannot write the old XP and level back.
"""

import uuid
from typing import cast

import pytest
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker

from server.async_persistence import AsyncPersistenceLayer
from server.game.level_service import LevelService
from server.game.player_registry import PlayerRegistry, RegistrySettings, SessionFactory
from server.models.player_xp import level_for_xp


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


async def _stored(session_factory: async_sessionmaker[AsyncSession], player_id: uuid.UUID) -> tuple[int, int]:
    """(experience_points, level) as stored."""
    async with session_factory() as session:
        row = (
            await session.execute(
                text("SELECT experience_points, level FROM players WHERE player_id = :id"), {"id": str(player_id)}
            )
        ).one()
    return cast(int, row[0]), cast(int, row[1])


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
        level = cast(int | None, (await session.execute(text("SELECT level_for_xp(:xp)"), {"xp": xp})).scalar())
        assert level == expected_level


@pytest.mark.asyncio
async def test_the_python_curve_is_the_sql_curve(session_factory: async_sessionmaker[AsyncSession]) -> None:
    """Every level boundary and the XP either side of it, a spread in between, and the top of the integer range."""
    boundaries = [50 * level * (level - 1) for level in range(1, 6000)]
    samples = {0, 1, 2_000_000_000, 2_147_483_647}
    samples.update(xp for boundary in boundaries for xp in (boundary - 1, boundary, boundary + 1) if xp >= 0)
    samples.update(range(0, 5000, 7))
    xps = sorted(samples)

    async with session_factory() as session:
        rows = (
            await session.execute(
                text("SELECT x, level_for_xp(x) FROM unnest(CAST(:xps AS integer[])) AS x"), {"xps": xps}
            )
        ).all()

    assert len(rows) == len(xps)
    pairs = [(cast(int, row[0]), cast(int, row[1])) for row in rows]
    mismatches = [(xp, sql, level_for_xp(xp)) for xp, sql in pairs if sql != level_for_xp(xp)]
    assert mismatches == [], f"(xp, sql level, python level): {mismatches[:5]}"


@pytest.mark.asyncio
@pytest.mark.usefixtures("fresh_database_manager")
async def test_an_award_through_the_registry_reaches_the_database(
    session_factory: async_sessionmaker[AsyncSession], player_row: uuid.UUID
) -> None:
    registry = PlayerRegistry(cast(SessionFactory, session_factory), settings=RegistrySettings(idle_ttl_seconds=0))
    levels = LevelService(registry)

    await levels.grant_xp(player_row, 50)
    assert await _stored(session_factory, player_row) == (50, 1)

    await levels.grant_xp(player_row, 250)  # 300 XP is level 3
    assert await _stored(session_factory, player_row) == (300, 3)


@pytest.mark.asyncio
@pytest.mark.usefixtures("fresh_database_manager")
async def test_a_save_of_a_copy_loaded_before_an_award_keeps_the_xp_and_level(
    session_factory: async_sessionmaker[AsyncSession], player_row: uuid.UUID
) -> None:
    """upsert_player used to write the loaded copy's XP and level back: now only the registry writes them."""
    registry = PlayerRegistry(cast(SessionFactory, session_factory), settings=RegistrySettings(idle_ttl_seconds=0))
    persistence = AsyncPersistenceLayer(_skip_room_cache=True)
    stale_copy = await persistence.get_player_by_id(player_row)  # loaded at 0 XP, level 1
    assert stale_copy is not None

    await LevelService(registry).grant_xp(player_row, 100)
    await persistence.save_player(stale_copy)

    assert await _stored(session_factory, player_row) == (100, 2)
