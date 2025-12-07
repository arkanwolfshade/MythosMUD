"""Tests for the lucidity service adjustment and liability logic."""

from __future__ import annotations

import json
import uuid
from datetime import UTC, datetime
from unittest.mock import AsyncMock, MagicMock, patch

import pytest
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

from server.models.base import Base
from server.models.lucidity import LucidityAdjustmentLog, PlayerLucidity
from server.models.player import Player
from server.models.user import User
from server.services.lucidity_service import (
    LucidityService,
    decode_liabilities,
    resolve_tier,
)


@pytest.fixture
async def session_factory():
    import os

    database_url = os.getenv("DATABASE_URL")
    if not database_url or not database_url.startswith("postgresql"):
        raise ValueError("DATABASE_URL must be set to a PostgreSQL URL for this test.")
    engine = create_async_engine(database_url, future=True)
    async with engine.begin() as conn:
        # PostgreSQL always enforces foreign keys - no PRAGMA needed
        await conn.run_sync(Base.metadata.create_all)

    factory = async_sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)
    try:
        yield factory
    finally:
        await engine.dispose()


async def create_player(session: AsyncSession, username: str) -> Player:
    """Provision a user/player pair for lucidity service tests."""
    user = User(
        id=str(uuid.uuid4()),
        email=f"{username}@example.com",
        username=username,
        display_name=username,
        hashed_password="hashed",
        is_active=True,
        is_superuser=False,
        is_verified=True,
    )
    player = Player(
        player_id=str(uuid.uuid4()),
        user_id=user.id,
        name=username.capitalize(),
    )
    session.add_all([user, player])
    await session.flush()
    return player


@pytest.mark.asyncio
async def test_apply_lucidity_adjustment_updates_state_and_logs(session_factory):
    session_maker = session_factory
    async with session_maker() as session:
        player = await create_player(session, "arkhamite")
        service = LucidityService(session)

        result = await service.apply_lucidity_adjustment(
            player.player_id,
            -12,
            reason_code="encounter_star_vampire",
            metadata={"archetype": "star_vampire"},
            location_id="earth.arkham.tunnels.001",
        )

        await session.commit()

        assert result.previous_lcd == 100
        assert result.new_lcd == 88
        assert result.previous_tier == "lucid"
        assert result.new_tier == "lucid"

        lucidity_row = await service.get_player_lucidity(player.player_id)
        assert lucidity_row.current_lcd == 88
        assert lucidity_row.current_tier == "lucid"

        log_entries = (
            (
                await session.execute(
                    select(LucidityAdjustmentLog).where(LucidityAdjustmentLog.player_id == player.player_id)
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
async def test_apply_lucidity_adjustment_assigns_liability(session_factory):
    session_maker = session_factory
    async with session_maker() as session:
        player = await create_player(session, "miskatonic")
        # Seed a lower starting LCD to test tier drops.
        session.add(
            PlayerLucidity(
                player_id=player.player_id,
                current_lcd=80,
                current_tier=resolve_tier(80),
            )
        )
        await session.flush()

        service = LucidityService(
            session,
            liability_picker=lambda *_args: "bleak_outlook",
        )

        result = await service.apply_lucidity_adjustment(
            player.player_id,
            -25,
            reason_code="cosmic_horror",
        )
        await session.commit()

        assert result.liabilities_added == ["bleak_outlook"]
        lucidity_row = await service.get_player_lucidity(player.player_id)
        liabilities = decode_liabilities(lucidity_row.liabilities)
        assert liabilities
        assert liabilities[0]["code"] == "bleak_outlook"
        assert liabilities[0]["stacks"] == 1


@pytest.mark.asyncio
async def test_liability_stacks_and_clearing(session_factory):
    session_maker = session_factory
    async with session_maker() as session:
        player = await create_player(session, "investigator")
        service = LucidityService(session)

        await service.add_liability(player.player_id, "night_frayed_reflexes")
        await service.add_liability(player.player_id, "night_frayed_reflexes")
        await session.flush()

        lucidity_row = await service.get_player_lucidity(player.player_id)
        liabilities = decode_liabilities(lucidity_row.liabilities)
        assert liabilities[0]["stacks"] == 2

        changed = await service.clear_liability(player.player_id, "night_frayed_reflexes")
        assert changed
        lucidity_row = await service.get_player_lucidity(player.player_id)
        liabilities = decode_liabilities(lucidity_row.liabilities)
        assert liabilities[0]["stacks"] == 1

        await service.clear_liability(player.player_id, "night_frayed_reflexes", remove_all=True)
        lucidity_row = await service.get_player_lucidity(player.player_id)
        liabilities = decode_liabilities(lucidity_row.liabilities)
        assert not liabilities


@pytest.mark.asyncio
async def test_apply_lucidity_adjustment_emits_failover_rescue_update(session_factory):
    session_maker = session_factory
    async with session_maker() as session:
        player = await create_player(session, "catatonic")
        session.add(
            PlayerLucidity(
                player_id=player.player_id,
                current_lcd=-99,
                current_tier="catatonic",
                catatonia_entered_at=datetime(2025, 1, 1, tzinfo=UTC).replace(tzinfo=None),
            )
        )
        await session.flush()

        observer = MagicMock()
        observer.on_catatonia_entered = MagicMock()
        observer.on_catatonia_cleared = MagicMock()
        observer.on_sanitarium_failover = MagicMock()

        service = LucidityService(session, catatonia_observer=observer)

        with patch(
            "server.services.lucidity_service.send_rescue_update_event",
            new_callable=AsyncMock,
        ) as mock_rescue_event:
            await service.apply_lucidity_adjustment(
                player.player_id,
                -5,
                reason_code="passive_flux",
            )

        observer.on_sanitarium_failover.assert_called_once()
        assert observer.on_sanitarium_failover.call_args.kwargs["player_id"] == player.player_id

        statuses = [call.kwargs.get("status") for call in mock_rescue_event.await_args_list]
        assert "sanitarium" in statuses


@pytest.mark.asyncio
async def test_apply_lucidity_adjustment_emits_success_rescue_update_on_recovery(session_factory):
    session_maker = session_factory
    async with session_maker() as session:
        player = await create_player(session, "recovery")
        session.add(
            PlayerLucidity(
                player_id=player.player_id,
                current_lcd=-10,
                current_tier="catatonic",
                catatonia_entered_at=datetime(2025, 1, 1, tzinfo=UTC).replace(tzinfo=None),
            )
        )
        await session.flush()

        service = LucidityService(session)

        with patch(
            "server.services.lucidity_service.send_rescue_update_event",
            new_callable=AsyncMock,
        ) as mock_rescue_event:
            await service.apply_lucidity_adjustment(
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


@pytest.mark.asyncio
async def test_apply_lucidity_adjustment_triggers_delirium_respawn_at_minus_10(session_factory):
    """Test that lucidity adjustment triggers delirium respawn event when reaching -10."""
    session_maker = session_factory
    async with session_maker() as session:
        player = await create_player(session, "delirious")
        session.add(
            PlayerLucidity(
                player_id=player.player_id,
                current_lcd=-9,  # Just above threshold
                current_tier="catatonic",
            )
        )
        await session.flush()

        service = LucidityService(session)

        with patch(
            "server.services.lucidity_service.send_rescue_update_event",
            new_callable=AsyncMock,
        ) as mock_rescue_event:
            # Apply adjustment that brings lucidity to exactly -10
            result = await service.apply_lucidity_adjustment(
                player.player_id,
                -1,
                reason_code="test_delirium",
            )

        # Verify lucidity reached -10
        assert result.new_lcd == -10

        # Verify delirium rescue event was sent
        delirium_calls = [
            call
            for call in mock_rescue_event.await_args_list
            if call.kwargs.get("status") == "delirium"
        ]
        assert len(delirium_calls) > 0
        delirium_call = delirium_calls[0]
        assert delirium_call.kwargs.get("current_lcd") == -10
        assert "delirium" in delirium_call.kwargs.get("message", "").lower()


@pytest.mark.asyncio
async def test_apply_lucidity_adjustment_triggers_delirium_respawn_below_minus_10(session_factory):
    """Test that lucidity adjustment triggers delirium respawn event when going below -10."""
    session_maker = session_factory
    async with session_maker() as session:
        player = await create_player(session, "delirious")
        session.add(
            PlayerLucidity(
                player_id=player.player_id,
                current_lcd=-5,  # Above threshold
                current_tier="catatonic",
            )
        )
        await session.flush()

        service = LucidityService(session)

        with patch(
            "server.services.lucidity_service.send_rescue_update_event",
            new_callable=AsyncMock,
        ) as mock_rescue_event:
            # Apply adjustment that brings lucidity below -10
            result = await service.apply_lucidity_adjustment(
                player.player_id,
                -10,
                reason_code="test_delirium",
            )

        # Verify lucidity went below -10
        assert result.new_lcd == -15

        # Verify delirium rescue event was sent
        delirium_calls = [
            call
            for call in mock_rescue_event.await_args_list
            if call.kwargs.get("status") == "delirium"
        ]
        assert len(delirium_calls) > 0
        delirium_call = delirium_calls[0]
        assert delirium_call.kwargs.get("current_lcd") == -15


@pytest.mark.asyncio
async def test_apply_lucidity_adjustment_no_delirium_event_when_above_threshold(session_factory):
    """Test that delirium respawn event is NOT triggered when lucidity is above -10."""
    session_maker = session_factory
    async with session_maker() as session:
        player = await create_player(session, "stable")
        session.add(
            PlayerLucidity(
                player_id=player.player_id,
                current_lcd=-5,  # Above -10 threshold
                current_tier="catatonic",
            )
        )
        await session.flush()

        service = LucidityService(session)

        with patch(
            "server.services.lucidity_service.send_rescue_update_event",
            new_callable=AsyncMock,
        ) as mock_rescue_event:
            # Apply adjustment that keeps lucidity above -10
            result = await service.apply_lucidity_adjustment(
                player.player_id,
                -2,
                reason_code="test_stable",
            )

        # Verify lucidity is still above -10
        assert result.new_lcd == -7

        # Verify NO delirium rescue event was sent
        delirium_calls = [
            call
            for call in mock_rescue_event.await_args_list
            if call.kwargs.get("status") == "delirium"
        ]
        assert len(delirium_calls) == 0
