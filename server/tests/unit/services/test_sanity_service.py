"""Tests for the sanity service adjustment and liability logic."""

from __future__ import annotations

import json
import uuid
from datetime import UTC, datetime
from unittest.mock import AsyncMock, MagicMock, patch

import pytest
from sqlalchemy import select, text
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

from server.models.base import Base
from server.models.player import Player
from server.models.sanity import PlayerSanity, SanityAdjustmentLog
from server.models.user import User
from server.services.sanity_service import (
    SanityService,
    decode_liabilities,
    resolve_tier,
)


@pytest.fixture
async def session_factory():
    engine = create_async_engine("sqlite+aiosqlite:///:memory:", future=True)
    async with engine.begin() as conn:
        await conn.execute(text("PRAGMA foreign_keys=ON"))
        await conn.run_sync(Base.metadata.create_all)

    factory = async_sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)
    try:
        yield factory
    finally:
        await engine.dispose()


async def create_player(session: AsyncSession, username: str) -> Player:
    """Provision a user/player pair for sanity service tests."""
    user = User(
        id=str(uuid.uuid4()),
        email=f"{username}@example.com",
        username=username,
        hashed_password="hashed",
        is_active=True,
        is_superuser=False,
        is_verified=True,
    )
    player = Player(
        player_id=f"player-{uuid.uuid4()}",
        user_id=user.id,
        name=username.capitalize(),
    )
    session.add_all([user, player])
    await session.flush()
    return player


@pytest.mark.asyncio
async def test_apply_sanity_adjustment_updates_state_and_logs(session_factory):
    session_maker = session_factory
    async with session_maker() as session:
        player = await create_player(session, "arkhamite")
        service = SanityService(session)

        result = await service.apply_sanity_adjustment(
            player.player_id,
            -12,
            reason_code="encounter_star_vampire",
            metadata={"archetype": "star_vampire"},
            location_id="earth.arkham.tunnels.001",
        )

        await session.commit()

        assert result.previous_san == 100
        assert result.new_san == 88
        assert result.previous_tier == "lucid"
        assert result.new_tier == "lucid"

        sanity_row = await service.get_player_sanity(player.player_id)
        assert sanity_row.current_san == 88
        assert sanity_row.current_tier == "lucid"

        log_entries = (
            (
                await session.execute(
                    select(SanityAdjustmentLog).where(SanityAdjustmentLog.player_id == player.player_id)
                )
            )
            .scalars()
            .all()
        )
        assert len(log_entries) == 1
        log_entry = log_entries[0]
        assert log_entry.delta == -12
        assert json.loads(log_entry.metadata_payload)["archetype"] == "star_vampire"


@pytest.mark.asyncio
async def test_apply_sanity_adjustment_assigns_liability(session_factory):
    session_maker = session_factory
    async with session_maker() as session:
        player = await create_player(session, "miskatonic")
        # Seed a lower starting SAN to test tier drops.
        session.add(
            PlayerSanity(
                player_id=player.player_id,
                current_san=80,
                current_tier=resolve_tier(80),
            )
        )
        await session.flush()

        service = SanityService(
            session,
            liability_picker=lambda *_args: "bleak_outlook",
        )

        result = await service.apply_sanity_adjustment(
            player.player_id,
            -25,
            reason_code="cosmic_horror",
        )
        await session.commit()

        assert result.liabilities_added == ["bleak_outlook"]
        sanity_row = await service.get_player_sanity(player.player_id)
        liabilities = decode_liabilities(sanity_row.liabilities)
        assert liabilities
        assert liabilities[0]["code"] == "bleak_outlook"
        assert liabilities[0]["stacks"] == 1


@pytest.mark.asyncio
async def test_liability_stacks_and_clearing(session_factory):
    session_maker = session_factory
    async with session_maker() as session:
        player = await create_player(session, "investigator")
        service = SanityService(session)

        await service.add_liability(player.player_id, "night_frayed_reflexes")
        await service.add_liability(player.player_id, "night_frayed_reflexes")
        await session.flush()

        sanity_row = await service.get_player_sanity(player.player_id)
        liabilities = decode_liabilities(sanity_row.liabilities)
        assert liabilities[0]["stacks"] == 2

        changed = await service.clear_liability(player.player_id, "night_frayed_reflexes")
        assert changed
        sanity_row = await service.get_player_sanity(player.player_id)
        liabilities = decode_liabilities(sanity_row.liabilities)
        assert liabilities[0]["stacks"] == 1

        await service.clear_liability(player.player_id, "night_frayed_reflexes", remove_all=True)
        sanity_row = await service.get_player_sanity(player.player_id)
        liabilities = decode_liabilities(sanity_row.liabilities)
        assert not liabilities


@pytest.mark.asyncio
async def test_apply_sanity_adjustment_emits_failover_rescue_update(session_factory):
    session_maker = session_factory
    async with session_maker() as session:
        player = await create_player(session, "catatonic")
        session.add(
            PlayerSanity(
                player_id=player.player_id,
                current_san=-99,
                current_tier="catatonic",
                catatonia_entered_at=datetime(2025, 1, 1, tzinfo=UTC),
            )
        )
        await session.flush()

        observer = MagicMock()
        observer.on_catatonia_entered = MagicMock()
        observer.on_catatonia_cleared = MagicMock()
        observer.on_sanitarium_failover = MagicMock()

        service = SanityService(session, catatonia_observer=observer)

        with patch(
            "server.services.sanity_service.send_rescue_update_event",
            new_callable=AsyncMock,
        ) as mock_rescue_event:
            await service.apply_sanity_adjustment(
                player.player_id,
                -5,
                reason_code="passive_flux",
            )

        observer.on_sanitarium_failover.assert_called_once()
        assert observer.on_sanitarium_failover.call_args.kwargs["player_id"] == player.player_id

        statuses = [call.kwargs.get("status") for call in mock_rescue_event.await_args_list]
        assert "sanitarium" in statuses


@pytest.mark.asyncio
async def test_apply_sanity_adjustment_emits_success_rescue_update_on_recovery(session_factory):
    session_maker = session_factory
    async with session_maker() as session:
        player = await create_player(session, "recovery")
        session.add(
            PlayerSanity(
                player_id=player.player_id,
                current_san=-10,
                current_tier="catatonic",
                catatonia_entered_at=datetime(2025, 1, 1, tzinfo=UTC),
            )
        )
        await session.flush()

        service = SanityService(session)

        with patch(
            "server.services.sanity_service.send_rescue_update_event",
            new_callable=AsyncMock,
        ) as mock_rescue_event:
            await service.apply_sanity_adjustment(
                player.player_id,
                20,
                reason_code="ground_rescue",
            )

        success_calls = [call for call in mock_rescue_event.await_args_list if call.kwargs.get("status") == "success"]
        assert success_calls
        # The first success call should target the recovering player
        first_call = success_calls[0]
        if first_call.args:
            assert first_call.args[0] == player.player_id
        else:
            assert first_call.kwargs.get("player_id") == player.player_id
