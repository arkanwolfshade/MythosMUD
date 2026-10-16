"""
Integration test for PlayerDeathService's DP queries against real Postgres.

get_dead_players / get_mortally_wounded_players run every game tick, so they prefilter in Postgres
(the `get_players_not_clearly_alive()` function in db/procedures/players.sql) instead of loading the
whole players table. The prefilter must only ever drop rows the Python predicates would drop anyway;
this proves that on the real JSONB column, including the odd stored shapes `coerce_int` tolerates.
"""

import uuid
from typing import cast

import pytest
from sqlalchemy import select, text
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker

from server.models.player import Player
from server.models.user import User
from server.services.player_death_service import PlayerDeathService

_MISSING = object()

_PREFILTER_IDS_SQL = text("SELECT player_id FROM get_players_not_clearly_alive()")

# name -> stored current_dp (JSONB), and the state coerce_int()/Player.is_* assign it.
_DP_CASES: dict[str, object] = {
    "healthy": 5,
    "alive_at_one": 1,
    "boundary_zero": 0,
    "wounded": -3,
    "wounded_floor": -9,
    "dead_boundary": -10,
    "dead_deep": -15,
    "string_dead": "-12",
    "float_wounded": -4.0,
    "json_null": None,
    "not_numeric": "abc",
    "missing_key": _MISSING,
}
_EXPECTED_DEAD = {"dead_boundary", "dead_deep", "string_dead"}
_EXPECTED_MORTALLY_WOUNDED = {
    "boundary_zero",
    "wounded",
    "wounded_floor",
    "float_wounded",
    "json_null",  # coerce_int(None) -> default 0
    "not_numeric",  # coerce_int("abc") -> default 0
    "missing_key",  # stats.get default 0
}


@pytest.fixture
async def cleanup_test_user(session_factory: async_sessionmaker[AsyncSession]):
    """Yield a fresh user id; deleting the user cascades to its players."""
    user_id = uuid.uuid4()
    yield user_id
    async with session_factory() as session:
        _ = await session.execute(text("DELETE FROM users WHERE id = :id"), {"id": str(user_id)})
        await session.commit()


def _stats_for(dp_value: object) -> dict[str, object]:
    stats: dict[str, object] = {"strength": 50, "constitution": 50, "size": 50}
    if dp_value is not _MISSING:
        stats["current_dp"] = dp_value
    return stats


@pytest.mark.asyncio
async def test_dp_queries_match_python_predicates_on_real_jsonb(
    session_factory: async_sessionmaker[AsyncSession], cleanup_test_user: uuid.UUID
):
    user_id = cleanup_test_user
    names_by_id: dict[str, str] = {}

    async with session_factory() as session:
        session.add(
            User(
                id=str(user_id),
                email=f"test_{user_id}@example.com",
                username=f"testuser_{str(user_id)[:8]}",
                display_name=f"Test User {str(user_id)[:8]}",
                hashed_password="hashed",
                is_active=True,
                is_superuser=False,
                is_verified=True,
            )
        )
        await session.flush()
        for case_name, dp_value in _DP_CASES.items():
            player_id = str(uuid.uuid4())
            names_by_id[player_id] = case_name
            session.add(
                Player(
                    player_id=player_id,
                    user_id=str(user_id),
                    name=f"dp_{case_name}_{player_id[:8]}",
                    current_room_id="earth_arkhamcity_sanitarium_room_foyer_001",
                    stats=_stats_for(dp_value),
                )
            )
        await session.commit()

    service = PlayerDeathService()
    async with session_factory() as session:
        dead = {
            names_by_id[str(p.player_id)]
            for p in await service.get_dead_players(session)
            if str(p.player_id) in names_by_id
        }
        wounded = {
            names_by_id[str(p.player_id)]
            for p in await service.get_mortally_wounded_players(session)
            if str(p.player_id) in names_by_id
        }

        # Parity with the pre-prefilter behaviour: load everything, filter in Python.
        everyone = [
            p for p in (await session.execute(select(Player))).scalars().all() if str(p.player_id) in names_by_id
        ]
        python_dead = {names_by_id[str(p.player_id)] for p in everyone if p.is_dead()}
        python_wounded = {names_by_id[str(p.player_id)] for p in everyone if p.is_mortally_wounded()}

    async with session_factory() as session:
        prefiltered_ids = {
            str(player_id)
            for player_id in cast("list[object]", (await session.execute(_PREFILTER_IDS_SQL)).scalars().all())
        }
        prefiltered = {name for player_id, name in names_by_id.items() if player_id in prefiltered_ids}
        # The service maps the function's rows onto Player entities by column name. Reading every mapped
        # column off the entities it returns turns a column missing from its SELECT list (or from the
        # function) into a loud MissingGreenlet here, instead of a surprise on first access in the tick.
        returned = [*await service.get_dead_players(session), *await service.get_mortally_wounded_players(session)]
        for player in returned:
            for column_name in Player.__table__.columns.keys():
                assert hasattr(player, column_name)  # an unloaded column raises MissingGreenlet, not AttributeError

    # Parity alone would pass with a no-op filter: the point is that healthy rows never leave Postgres.
    assert prefiltered == set(_DP_CASES) - {"healthy", "alive_at_one"}
    assert returned  # the column-coverage loop above must have had entities to check
    assert dead == _EXPECTED_DEAD
    assert wounded == _EXPECTED_MORTALLY_WOUNDED
    assert dead == python_dead
    assert wounded == python_wounded
