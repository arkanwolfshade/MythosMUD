"""Tests for the ground rescue command."""

from __future__ import annotations

import uuid
from datetime import UTC, datetime
from types import SimpleNamespace
from unittest.mock import AsyncMock, MagicMock, patch

import pytest
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.pool import StaticPool

from server.commands.rescue_commands import handle_ground_command
from server.models.base import Base
from server.models.player import Player
from server.models.sanity import PlayerSanity
from server.models.user import User


@pytest.fixture
async def session_factory():
    """Provide an in-memory SQLite session factory for tests."""

    engine = create_async_engine(
        "sqlite+aiosqlite:///:memory:",
        future=True,
        connect_args={"check_same_thread": False},
        poolclass=StaticPool,
    )
    async with engine.begin() as conn:
        await conn.exec_driver_sql("PRAGMA foreign_keys=ON")
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
    sanity: int = 100,
    tier: str = "lucid",
) -> Player:
    """Create a player for testing ground command behaviour."""

    player_id = f"player-{uuid.uuid4()}"
    user = User(
        id=str(uuid.uuid4()),
        email=f"{player_id}@example.org",
        username=name,
        hashed_password="hashed",
        is_active=True,
        is_superuser=False,
        is_verified=True,
    )
    player = Player(
        player_id=player_id,
        user_id=user.id,
        name=name,
        current_room_id="earth_arkhamcity_sanitarium_room_foyer_001",
    )
    sanity_record = PlayerSanity(
        player_id=player_id,
        current_san=sanity,
        current_tier=tier,
    )
    session.add_all([user, player, sanity_record])
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
    """Rescuing a catatonic ally should restore them to 1 SAN."""

    session_maker = session_factory
    async with session_maker() as session:
        rescuer = await create_player(session, name="rescuer", sanity=40, tier="uneasy")
        victim = await create_player(session, name="victim", sanity=-20, tier="catatonic")

        record = await session.get(PlayerSanity, victim.player_id)
        assert record is not None
        record.current_san = -20
        record.current_tier = "catatonic"
        record.catatonia_entered_at = datetime(2025, 1, 1, tzinfo=UTC)
        await session.commit()

        persistence = MagicMock()
        persistence.get_player_by_name.side_effect = lambda name: {
            "rescuer": SimpleNamespace(
                player_id=rescuer.player_id,
                name="rescuer",
                current_room_id="earth_arkhamcity_sanitarium_room_foyer_001",
            ),
            "victim": SimpleNamespace(
                player_id=victim.player_id,
                name="victim",
                current_room_id="earth_arkhamcity_sanitarium_room_foyer_001",
            ),
        }[name]
        request = build_request(persistence)

        async def fake_get_async_session():
            yield session

        command_data = {"command_type": "ground", "target_player": "victim"}
        current_user = {"username": "rescuer"}

        with patch("server.commands.rescue_commands.get_async_session", fake_get_async_session):
            result = await handle_ground_command(command_data, current_user, request, None, "rescuer")

        assert "victim" in result["result"].lower()
        assert "steadies" in result["result"].lower()

        refreshed = await session.get(PlayerSanity, victim.player_id)
        assert refreshed is not None
        assert refreshed.current_san == 1
        assert refreshed.current_tier == "deranged"
        assert refreshed.catatonia_entered_at is None


@pytest.mark.asyncio
async def test_ground_command_emits_rescue_updates(session_factory):
    """Ensure both participants receive rescue_update events throughout the ritual."""

    session_maker = session_factory
    async with session_maker() as session:
        rescuer = await create_player(session, name="rescuer", sanity=40, tier="uneasy")
        victim = await create_player(session, name="victim", sanity=-20, tier="catatonic")

        record = await session.get(PlayerSanity, victim.player_id)
        assert record is not None
        record.current_san = -20
        record.current_tier = "catatonic"
        record.catatonia_entered_at = datetime(2025, 1, 1, tzinfo=UTC)
        await session.commit()

        persistence = MagicMock()
        persistence.get_player_by_name.side_effect = lambda name: {
            "rescuer": SimpleNamespace(
                player_id=rescuer.player_id,
                name="rescuer",
                current_room_id="earth_arkhamcity_sanitarium_room_foyer_001",
            ),
            "victim": SimpleNamespace(
                player_id=victim.player_id,
                name="victim",
                current_room_id="earth_arkhamcity_sanitarium_room_foyer_001",
            ),
        }[name]
        request = build_request(persistence)

        async def fake_get_async_session():
            yield session

        command_data = {"command_type": "ground", "target_player": "victim"}
        current_user = {"username": "rescuer"}

        with patch("server.commands.rescue_commands.get_async_session", fake_get_async_session):
            with patch(
                "server.commands.rescue_commands.send_rescue_update_event",
                new_callable=AsyncMock,
            ) as mock_rescue_event:
                await handle_ground_command(command_data, current_user, request, None, "rescuer")

        statuses = [call.kwargs.get("status") for call in mock_rescue_event.await_args_list]
        assert statuses.count("channeling") == 2
        assert statuses.count("success") == 3  # Two explicit messages + sanity service resolution

        channel_targets = {
            call.args[0] for call in mock_rescue_event.await_args_list if call.kwargs.get("status") == "channeling"
        }
        assert channel_targets == {victim.player_id, rescuer.player_id}

        success_targets = [
            call.args[0] for call in mock_rescue_event.await_args_list if call.kwargs.get("status") == "success"
        ]
        assert success_targets.count(rescuer.player_id) == 1
        assert success_targets.count(victim.player_id) == 2


@pytest.mark.asyncio
async def test_ground_command_requires_catatonic_target(session_factory):
    """Rescue attempts should fail gracefully if the target is not catatonic."""

    session_maker = session_factory
    async with session_maker() as session:
        rescuer = await create_player(session, name="rescuer", sanity=50, tier="lucid")
        victim = await create_player(session, name="victim", sanity=30, tier="uneasy")
        await session.commit()

        persistence = MagicMock()
        persistence.get_player_by_name.side_effect = lambda name: {
            "rescuer": SimpleNamespace(
                player_id=rescuer.player_id,
                name="rescuer",
                current_room_id="earth_arkhamcity_sanitarium_room_foyer_001",
            ),
            "victim": SimpleNamespace(
                player_id=victim.player_id,
                name="victim",
                current_room_id="earth_arkhamcity_sanitarium_room_foyer_001",
            ),
        }[name]
        request = build_request(persistence)

        async def fake_get_async_session():
            yield session

        command_data = {"command_type": "ground", "target_player": "victim"}
        current_user = {"username": "rescuer"}

        with patch("server.commands.rescue_commands.get_async_session", fake_get_async_session):
            result = await handle_ground_command(command_data, current_user, request, None, "rescuer")

        assert "isn't catatonic" in result["result"]

        refreshed = await session.get(PlayerSanity, victim.player_id)
        assert refreshed is not None
        assert refreshed.current_san == 30
        assert refreshed.current_tier == "uneasy"
