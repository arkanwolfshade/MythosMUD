"""
Integration test for lucidity on the player registry (ADR-029 step 5b-i), against real PostgreSQL.

A LucidityService change lands in the registry's lucidity part and stays there (lazy) until a flush, which writes
``upsert_player_lucidity`` and the ``lucidity_adjustment_log`` row in one transaction. A fresh registry then reads it
back through ``get_player_lucidity``, catatonia timestamp included.
"""

import uuid
from typing import cast
from unittest.mock import AsyncMock, patch

import pytest
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker

from server.game.player_registry import PlayerRegistry, RegistrySettings, SessionFactory
from server.models.player import Player
from server.models.user import User
from server.services.lucidity_service import LucidityService


@pytest.fixture
async def cleanup_test_user(session_factory: async_sessionmaker[AsyncSession]):
    """Yield a fresh user id and guarantee its row is deleted after the test, pass or fail.
    Deleting the user cascades to players/player_lucidity/lucidity_adjustment_log/
    lucidity_cooldowns/lucidity_exposure_state."""
    user_id = uuid.uuid4()
    yield user_id
    async with session_factory() as session:
        _ = await session.execute(text("DELETE FROM users WHERE id = :id"), {"id": str(user_id)})
        await session.commit()


async def _create_player(session_factory: async_sessionmaker[AsyncSession], user_id: uuid.UUID) -> uuid.UUID:
    player_id = uuid.uuid4()
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
        session.add(
            Player(
                player_id=str(player_id),
                user_id=str(user_id),
                name=f"testplayer_{str(player_id)[:8]}",
                current_room_id="earth_arkhamcity_sanitarium_room_foyer_001",
            )
        )
        await session.commit()
    return player_id


async def _stored(session_factory: async_sessionmaker[AsyncSession], player_id: uuid.UUID) -> tuple[object, ...] | None:
    async with session_factory() as session:
        row = (
            await session.execute(
                text(
                    "SELECT current_lcd, current_tier, catatonia_entered_at FROM player_lucidity WHERE player_id = :id"
                ),
                {"id": str(player_id)},
            )
        ).first()
    return tuple(row) if row is not None else None


async def _ledger(session_factory: async_sessionmaker[AsyncSession], player_id: uuid.UUID) -> list[tuple[object, ...]]:
    async with session_factory() as session:
        rows = await session.execute(
            text("SELECT delta, reason_code FROM lucidity_adjustment_log WHERE player_id = :id ORDER BY id"),
            {"id": str(player_id)},
        )
    return [tuple(row) for row in rows]


@pytest.mark.asyncio
async def test_lucidity_adjustment_round_trip(
    session_factory: async_sessionmaker[AsyncSession], cleanup_test_user: uuid.UUID
):
    player_id = await _create_player(session_factory, cleanup_test_user)
    registry = PlayerRegistry(cast(SessionFactory, session_factory), settings=RegistrySettings(idle_ttl_seconds=0))
    service = LucidityService(registry)

    with patch("server.services.lucidity_service.send_lucidity_change_event", new=AsyncMock()):
        result = await service.apply_lucidity_adjustment(player_id, -60, reason_code="test_adjustment")

    # A new character has no row yet: the registry starts from 100 / lucid.
    assert (result.previous_lcd, result.previous_tier, result.new_lcd, result.new_tier) == (100, "lucid", 40, "uneasy")
    assert await _stored(session_factory, player_id) is None  # lazy: nothing written before the sweep
    assert registry.is_loaded(player_id)  # a dirty player stays in memory even with no idle TTL

    assert await registry.flush_dirty() == 1

    assert await _stored(session_factory, player_id) == (40, "uneasy", None)
    assert await _ledger(session_factory, player_id) == [(-60, "test_adjustment")]
    assert not registry.is_loaded(player_id)  # clean again, so evicted

    # A fresh registry reads the written row back, and catatonia's timestamp survives the round trip.
    fresh_registry = PlayerRegistry(
        cast(SessionFactory, session_factory), settings=RegistrySettings(idle_ttl_seconds=0)
    )
    fresh = LucidityService(fresh_registry)
    with (
        patch("server.services.lucidity_service.send_lucidity_change_event", new=AsyncMock()),
        patch("server.services.lucidity_trigger_handlers.send_catatonia_event", new=AsyncMock()),
    ):
        catatonic = await fresh.apply_lucidity_adjustment(player_id, -45, reason_code="shock")
    assert (catatonic.previous_lcd, catatonic.new_lcd, catatonic.new_tier) == (40, -5, "catatonic")
    assert await fresh_registry.flush_dirty() == 1

    stored = await _stored(session_factory, player_id)
    assert stored is not None and stored[:2] == (-5, "catatonic") and stored[2] is not None
    assert await _ledger(session_factory, player_id) == [(-60, "test_adjustment"), (-45, "shock")]
