"""
Integration test for corruption on the player registry (ADR-029 step 5c), against real PostgreSQL.

A CorruptionService change is one sync unit: ``stats.corruption`` (merged into the stored stats, never the whole
blob), its ``corruption_adjustment_log`` row and any cleanse cooldown commit before the call returns. A fresh
registry reads the cooldown back (the table stores naive UTC). And a legacy full-row save of a copy loaded before the
change (``upsert_player``) can no longer write the old corruption back.
"""

import uuid
from datetime import UTC, datetime, timedelta
from typing import cast
from unittest.mock import AsyncMock, patch

import pytest
import structlog
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker

from server.async_persistence import AsyncPersistenceLayer
from server.game.player_registry import PlayerRegistry, RegistrySettings, SessionFactory
from server.persistence.repositories.player_repository_save import PlayerSavePreparer
from server.services.corruption_service import CorruptionActionOnCooldownError, CorruptionService
from server.services.corruption_tier_cache import corruption_tier_cache
from server.tests.fixtures.integration.players import create_test_player, delete_test_user


@pytest.fixture
async def cleanup_test_user(session_factory: async_sessionmaker[AsyncSession]):
    """Yield a fresh user id; deleting it afterwards cascades to the player and its corruption rows."""
    user_id = uuid.uuid4()
    yield user_id
    await delete_test_user(session_factory, user_id)


def _registry(session_factory: async_sessionmaker[AsyncSession]) -> PlayerRegistry:
    return PlayerRegistry(cast(SessionFactory, session_factory), settings=RegistrySettings(idle_ttl_seconds=0))


async def _stats(session_factory: async_sessionmaker[AsyncSession], player_id: uuid.UUID) -> dict[str, object]:
    async with session_factory() as session:
        row = (
            await session.execute(text("SELECT stats FROM players WHERE player_id = :id"), {"id": str(player_id)})
        ).one()
    return cast(dict[str, object], row[0])


async def _ledger(session_factory: async_sessionmaker[AsyncSession], player_id: uuid.UUID) -> list[tuple[object, ...]]:
    async with session_factory() as session:
        rows = await session.execute(
            text("SELECT delta, reason_code FROM corruption_adjustment_log WHERE player_id = :id ORDER BY id"),
            {"id": str(player_id)},
        )
    return [tuple(row) for row in rows]


async def _cleanse_expiry(session_factory: async_sessionmaker[AsyncSession], player_id: uuid.UUID) -> datetime | None:
    async with session_factory() as session:
        row = (
            await session.execute(
                text(
                    """SELECT cooldown_expires_at FROM corruption_cooldowns
                    WHERE player_id = :id AND action_code = 'cleanse'"""
                ),
                {"id": str(player_id)},
            )
        ).first()
    return cast(datetime, row[0]) if row is not None else None


@pytest.mark.asyncio
async def test_corruption_and_its_cleanse_cooldown_round_trip(
    session_factory: async_sessionmaker[AsyncSession], cleanup_test_user: uuid.UUID
):
    player_id = await create_test_player(
        session_factory, cleanup_test_user, stats={"current_dp": 20, "max_dp": 20, "corruption": 0}
    )
    registry = _registry(session_factory)
    try:
        with (
            patch("server.realtime.connection_manager_api.send_game_event", new_callable=AsyncMock),
            patch("server.game.chat_npc_system.deliver_personal_system", new_callable=AsyncMock),
        ):
            gained = await CorruptionService(registry).apply_corruption_adjustment(
                player_id, 5, reason_code="spell_cast"
            )
            assert gained.new_value == 5
            # Sync: committed before the call returned, so nothing is left in memory to sweep.
            assert not registry.is_loaded(player_id)
            assert await _stats(session_factory, player_id) == {"current_dp": 20, "max_dp": 20, "corruption": 5}

            cleansed = await CorruptionService(registry).perform_recovery_action(player_id, action_code="cleanse")

        assert cleansed.new_value == 1  # 5 - 8, held at the permanence floor
        assert (await _stats(session_factory, player_id))["corruption"] == 1
        assert await _ledger(session_factory, player_id) == [(5, "spell_cast"), (-8, "ritual_cleanse")]
        stored = await _cleanse_expiry(session_factory, player_id)
        assert stored is not None and stored.tzinfo is None  # naive UTC, as the column is
        assert timedelta(hours=5) < stored.replace(tzinfo=UTC) - datetime.now(UTC) <= timedelta(hours=6)

        # A fresh registry reads the cooldown back, aware and equal, and refuses a second cleanse.
        fresh = CorruptionService(_registry(session_factory))
        assert await fresh.get_cooldown_expiry(player_id, "cleanse") == stored.replace(tzinfo=UTC)
        with pytest.raises(CorruptionActionOnCooldownError):
            _ = await fresh.perform_recovery_action(player_id, action_code="cleanse")
    finally:
        corruption_tier_cache.clear(player_id)


@pytest.mark.asyncio
@pytest.mark.usefixtures("fresh_database_manager")
async def test_a_stale_full_row_save_keeps_the_stored_corruption(
    session_factory: async_sessionmaker[AsyncSession], cleanup_test_user: uuid.UUID
):
    """upsert_player of a Player loaded before a corruption change keeps the new corruption; its other stats land."""
    player_id = await create_test_player(
        session_factory, cleanup_test_user, stats={"current_dp": 20, "max_dp": 20, "corruption": 0}
    )
    persistence = AsyncPersistenceLayer(_skip_room_cache=True)
    stale = await persistence.get_player_by_id(player_id)
    assert stale is not None
    try:
        with (
            patch("server.realtime.connection_manager_api.send_game_event", new_callable=AsyncMock),
            patch("server.game.chat_npc_system.deliver_personal_system", new_callable=AsyncMock),
        ):
            _ = await CorruptionService(_registry(session_factory)).apply_corruption_adjustment(
                player_id, 7, reason_code="spell_cast"
            )

        stats = stale.get_stats()
        stats["luck"] = 12  # the stale copy's own change, to a stat the registry does not own yet
        stale.set_stats(stats)
        preparer = PlayerSavePreparer(structlog.get_logger())
        async with session_factory() as session:
            await preparer.execute(session, preparer.prepare(stale))
            await session.commit()

        after = await _stats(session_factory, player_id)
        assert after["corruption"] == 7  # not the stale copy's 0
        assert after["luck"] == 12
    finally:
        corruption_tier_cache.clear(player_id)
