"""Tests for the ground rescue command."""

from __future__ import annotations

import uuid
from datetime import datetime
from types import SimpleNamespace
from typing import Any
from unittest.mock import AsyncMock, MagicMock, patch

import pytest
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

from server.commands.rescue_commands import handle_ground_command
from server.models.base import Base
from server.models.lucidity import PlayerLucidity
from server.models.player import Player
from server.models.user import User


@pytest.fixture
async def session_factory():
    """Provide a PostgreSQL session factory for tests."""

    import os

    database_url = os.getenv("DATABASE_URL")
    if not database_url or not database_url.startswith("postgresql"):
        raise ValueError("DATABASE_URL must be set to a PostgreSQL URL. SQLite is no longer supported.")
    engine = create_async_engine(database_url, future=True)
    async with engine.begin() as conn:
        # PostgreSQL always enforces foreign keys - no PRAGMA needed
        await conn.run_sync(Base.metadata.create_all)

    factory = async_sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)
    try:
        yield factory
    finally:
        await engine.dispose()


async def create_player(
    session: AsyncSession,
    *,
    name: str,
    lucidity: int = 100,
    tier: str = "lucid",
) -> Player:
    """Create a player for testing ground command behaviour."""

    player_id = str(uuid.uuid4())
    # Use unique username to avoid IntegrityError in parallel test runs
    unique_username = f"{name}_{uuid.uuid4().hex[:8]}"
    user = User(
        id=str(uuid.uuid4()),
        email=f"{player_id}@example.org",
        username=unique_username,
        display_name=unique_username,
        hashed_password="hashed",
        is_active=True,
        is_superuser=False,
        is_verified=True,
    )
    # Use unique player name to avoid IntegrityError in parallel test runs
    unique_player_name = f"{name}_{uuid.uuid4().hex[:8]}"
    player = Player(
        player_id=player_id,
        user_id=user.id,
        name=unique_player_name,
        current_room_id="earth_arkhamcity_LCDitarium_room_foyer_001",
    )
    lucidity_record = PlayerLucidity(
        player_id=player_id,
        current_lcd=lucidity,
        current_tier=tier,
    )
    session.add_all([user, player, lucidity_record])
    await session.flush()
    return player


def build_request(persistence: MagicMock) -> SimpleNamespace:
    """Construct a mock request with app state."""

    state = SimpleNamespace(
        persistence=persistence,
        event_bus=MagicMock(),
        catatonia_registry=MagicMock(),
    )
    app = SimpleNamespace(state=state)
    return SimpleNamespace(app=app)


@pytest.mark.asyncio
async def test_ground_command_revives_catatonic_player(session_factory):
    """Rescuing a catatonic ally should restore them to 1 LCD."""

    session_maker = session_factory
    async with session_maker() as session:
        rescuer = await create_player(session, name="rescuer", lucidity=40, tier="uneasy")
        victim = await create_player(session, name="victim", lucidity=-20, tier="catatonic")

        record = await session.get(PlayerLucidity, victim.player_id)
        assert record is not None
        record.current_lcd = -20
        record.current_tier = "catatonic"
        # Use timezone-naive datetime for TIMESTAMP WITHOUT TIME ZONE column
        record.catatonia_entered_at = datetime(2025, 1, 1)
        await session.commit()

        persistence = MagicMock()
        persistence.get_player_by_name.side_effect = lambda name: {
            "rescuer": SimpleNamespace(
                player_id=rescuer.player_id,
                name="rescuer",
                current_room_id="earth_arkhamcity_LCDitarium_room_foyer_001",
            ),
            "victim": SimpleNamespace(
                player_id=victim.player_id,
                name="victim",
                current_room_id="earth_arkhamcity_LCDitarium_room_foyer_001",
            ),
        }[name]
        request = build_request(persistence)

        async def fake_get_async_session():
            yield session

        command_data = {"command_type": "ground", "target_player": "victim"}
        current_user = {"username": "rescuer"}

        with patch("server.commands.rescue_commands.get_async_session", fake_get_async_session):
            result = await handle_ground_command(command_data, current_user, request, None, rescuer.name)

        # Check for base name pattern (command output uses base name, not unique name)
        assert "victim" in result["result"].lower()
        assert "steadies" in result["result"].lower()

        refreshed = await session.get(PlayerLucidity, victim.player_id)
        assert refreshed is not None
        assert refreshed.current_lcd == 1
        assert refreshed.current_tier == "deranged"
        assert refreshed.catatonia_entered_at is None


@pytest.mark.asyncio
async def test_ground_command_emits_rescue_updates(session_factory):
    """Ensure both participants receive rescue_update events throughout the ritual."""

    session_maker = session_factory
    async with session_maker() as session:
        rescuer = await create_player(session, name="rescuer", lucidity=40, tier="uneasy")
        victim = await create_player(session, name="victim", lucidity=-20, tier="catatonic")

        record = await session.get(PlayerLucidity, victim.player_id)
        assert record is not None
        record.current_lcd = -20
        record.current_tier = "catatonic"
        # Use timezone-naive datetime for TIMESTAMP WITHOUT TIME ZONE column
        record.catatonia_entered_at = datetime(2025, 1, 1)
        await session.commit()

        persistence = MagicMock()
        persistence.get_player_by_name.side_effect = lambda name: {
            "rescuer": SimpleNamespace(
                player_id=rescuer.player_id,
                name="rescuer",
                current_room_id="earth_arkhamcity_LCDitarium_room_foyer_001",
            ),
            "victim": SimpleNamespace(
                player_id=victim.player_id,
                name="victim",
                current_room_id="earth_arkhamcity_LCDitarium_room_foyer_001",
            ),
        }[name]
        request = build_request(persistence)

        async def fake_get_async_session():
            yield session

        command_data = {"command_type": "ground", "target_player": "victim"}
        current_user = {"username": "rescuer"}

        with patch("server.commands.rescue_commands.get_async_session", fake_get_async_session):
            with patch(
                "server.services.lucidity_event_dispatcher.send_rescue_update_event",
                new_callable=AsyncMock,
            ) as mock_rescue_event:
                with patch("server.commands.rescue_commands.send_rescue_update_event", mock_rescue_event):
                    with patch("server.services.lucidity_service.send_rescue_update_event", mock_rescue_event):
                        await handle_ground_command(command_data, current_user, request, None, rescuer.name)

        statuses = [call.kwargs.get("status") for call in mock_rescue_event.await_args_list]
        assert statuses.count("channeling") == 2
        assert statuses.count("success") == 3  # Two explicit messages + lucidity service resolution

        def _call_target(call: Any) -> uuid.UUID | str | None:
            """Extract player_id from call, returning as-is (could be UUID or string)."""
            if call.args:
                return call.args[0]
            return call.kwargs.get("player_id")

        channel_targets = {
            _call_target(call)
            for call in mock_rescue_event.await_args_list
            if call.kwargs.get("status") == "channeling"
        }

        # Convert values to comparable format (normalize UUIDs and strings)
        def normalize_id(pid: uuid.UUID | str) -> uuid.UUID:
            """Normalize player ID to UUID for comparison."""
            if isinstance(pid, uuid.UUID):
                return pid
            return uuid.UUID(pid)

        victim_uuid = normalize_id(victim.player_id)
        rescuer_uuid = normalize_id(rescuer.player_id)
        channel_targets_normalized = {normalize_id(t) for t in channel_targets}
        assert channel_targets_normalized == {victim_uuid, rescuer_uuid}

        success_targets = [
            _call_target(call) for call in mock_rescue_event.await_args_list if call.kwargs.get("status") == "success"
        ]
        success_targets_normalized = [normalize_id(t) for t in success_targets]
        assert success_targets_normalized.count(rescuer_uuid) == 1
        assert success_targets_normalized.count(victim_uuid) == 2


@pytest.mark.asyncio
async def test_ground_command_requires_catatonic_target(session_factory):
    """Rescue attempts should fail gracefully if the target is not catatonic."""

    session_maker = session_factory
    async with session_maker() as session:
        rescuer = await create_player(session, name="rescuer", lucidity=50, tier="lucid")
        victim = await create_player(session, name="victim", lucidity=30, tier="uneasy")
        await session.commit()

        persistence = MagicMock()
        # Use actual player names from created players (now unique)
        persistence.get_player_by_name.side_effect = lambda name: {
            rescuer.name: SimpleNamespace(
                player_id=rescuer.player_id,
                name=rescuer.name,
                current_room_id="earth_arkhamcity_LCDitarium_room_foyer_001",
            ),
            victim.name: SimpleNamespace(
                player_id=victim.player_id,
                name=victim.name,
                current_room_id="earth_arkhamcity_LCDitarium_room_foyer_001",
            ),
        }[name]
        request = build_request(persistence)

        async def fake_get_async_session():
            yield session

        command_data = {"command_type": "ground", "target_player": victim.name}
        current_user = {"username": rescuer.name}

        with patch("server.commands.rescue_commands.get_async_session", fake_get_async_session):
            result = await handle_ground_command(command_data, current_user, request, None, rescuer.name)

        assert "isn't catatonic" in result["result"]

        refreshed = await session.get(PlayerLucidity, victim.player_id)
        assert refreshed is not None
        assert refreshed.current_lcd == 30
        assert refreshed.current_tier == "uneasy"
