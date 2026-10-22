"""
Integration test for the catatonia clock's candidate query against real Postgres (#1148).

`get_catatonic_player_ids()` (db/procedures/lucidity.sql) feeds game_tick_catatonia every decay interval, so it must
return exactly the players inside the countdown, 0 >= LCD > -10, and nobody else: not the healthy, not delirium's
(-10 and below), not soft-deleted players.

`make test-playwright` runs this against the live e2e database while its server is ticking, and that server takes
1 LCD per interval from catatonic rows. So no in-band row sits within a few steps of -10 (-9 would leave the band
mid-test): the -10 boundary is pinned from the delirium side instead.
"""

import uuid
from typing import cast

import pytest
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker

from server.models.lucidity import PlayerLucidity
from server.models.player import Player
from server.models.user import User

_CANDIDATE_IDS_SQL = text("SELECT player_id FROM get_catatonic_player_ids()")

# name -> (stored current_lcd, stored tier, soft-deleted)
_CASES: dict[str, tuple[int, str, bool]] = {
    "healthy": (100, "lucid", False),
    "alive_at_one": (1, "deranged", False),
    "boundary_zero": (0, "catatonic", False),
    "catatonic": (-4, "catatonic", False),
    "catatonic_deep": (-7, "catatonic", False),
    "delirium_boundary": (-10, "catatonic", False),
    "past_delirium": (-50, "catatonic", False),
    "deleted_catatonic": (-3, "catatonic", True),
}
_EXPECTED = {"boundary_zero", "catatonic", "catatonic_deep"}


@pytest.fixture
async def cleanup_test_user(session_factory: async_sessionmaker[AsyncSession]):
    """Yield a fresh user id; deleting the user cascades to its players and their lucidity rows."""
    user_id = uuid.uuid4()
    yield user_id
    async with session_factory() as session:
        _ = await session.execute(text("DELETE FROM users WHERE id = :id"), {"id": str(user_id)})
        await session.commit()


@pytest.mark.asyncio
async def test_the_candidate_query_returns_exactly_the_players_inside_the_countdown(
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
        for case_name, (lcd, tier, deleted) in _CASES.items():
            player_id = str(uuid.uuid4())
            names_by_id[player_id] = case_name
            session.add(
                Player(
                    player_id=player_id,
                    user_id=str(user_id),
                    name=f"lcd_{case_name}_{player_id[:8]}",
                    current_room_id="earth_arkhamcity_sanitarium_room_foyer_001",
                    stats={"strength": 50, "constitution": 50, "size": 50},
                    is_deleted=deleted,
                )
            )
            await session.flush()
            session.add(PlayerLucidity(player_id=player_id, current_lcd=lcd, current_tier=tier))
        await session.commit()

    async with session_factory() as session:
        returned_ids = {
            str(player_id)
            for player_id in cast("list[object]", (await session.execute(_CANDIDATE_IDS_SQL)).scalars().all())
        }

    returned = {name for player_id, name in names_by_id.items() if player_id in returned_ids}
    assert returned == _EXPECTED
