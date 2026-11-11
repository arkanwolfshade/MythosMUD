"""
Integration tests: the e2e harness resets, places and reads characters through the registry (ADR-029 step 8b).

The unit tests use fakes; these run the harness's registry units against the real procedures, including the new
``delete_quest_instances_by_player`` and the sync write of a character with every part changed at once.
"""

import uuid
from datetime import UTC, datetime, timedelta
from typing import cast
from uuid import UUID

import pytest
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker

from server.constants.instance_rooms import PENDING_INSTANCE_ID
from server.constants.spawn_defaults import DEFAULT_RESPAWN_ROOM
from server.game.player_registry import PlayerRegistry, RegistrySettings, SessionFactory
from server.models.player import Player
from server.models.user import User
from server.services import e2e_player_support
from server.services.e2e_player_support import E2ePlayerSupport, UnknownRoomError

ELSEWHERE = "earth_arkhamcity_downtown_room_arkham_savings_001"


class _Named:
    def __init__(self, player_id: UUID) -> None:
        self.player_id: UUID = player_id


class _Persistence:
    """Names to ids; the character has no bank box and the foyer has no chest (containers are not under test here)."""

    def __init__(self, ids: dict[str, UUID]) -> None:
        self.ids: dict[str, UUID] = ids

    async def get_player_by_name(self, name: str) -> _Named | None:
        player_id = self.ids.get(name)
        return _Named(player_id) if player_id is not None else None

    async def get_bank_container(self, owner_id: UUID) -> None:
        _ = owner_id

    async def get_containers_by_room_id(self, room_id: str) -> list[dict[str, object]]:
        _ = room_id
        return []

    async def update_container(self, container_id: UUID, items_json: list[dict[str, object]] | None = None) -> None:
        raise AssertionError(f"no container should be emptied: {container_id} {items_json}")


class _Rooms:
    async def get_room(self, room_id: str) -> dict[str, object] | None:
        return {"id": room_id} if room_id in {ELSEWHERE, DEFAULT_RESPAWN_ROOM} else None


async def _create_player(session_factory: async_sessionmaker[AsyncSession], name: str) -> tuple[UUID, UUID]:
    user_id = uuid.uuid4()
    player_id = uuid.uuid4()
    async with session_factory() as session:
        session.add(
            User(
                id=str(user_id),
                email=f"e2e_support_{user_id}@example.com",
                username=f"e2e_{str(user_id)[:8]}",
                display_name=f"E2E {str(user_id)[:8]}",
                hashed_password="hashed",
                is_active=True,
                is_superuser=False,
                is_verified=True,
            )
        )
        await session.flush()
        session.add(Player(player_id=str(player_id), user_id=str(user_id), name=name))
        await session.commit()
    return player_id, user_id


async def _define_quests(session_factory: async_sessionmaker[AsyncSession]) -> tuple[str, str]:
    """Two quest definitions only this test knows, since quest instances reference one."""
    suffix = uuid.uuid4().hex[:8]
    ids = (f"e2e_support_active_{suffix}", f"e2e_support_done_{suffix}")
    async with session_factory() as session:
        for quest_id in ids:
            _ = await session.execute(
                text(
                    """
                    INSERT INTO quest_definitions (id, definition, created_at, updated_at)
                    VALUES (:id, CAST('{}' AS jsonb), NOW(), NOW())
                    """
                ),
                {"id": quest_id},
            )
        await session.commit()
    return ids


async def _drop_quests(session_factory: async_sessionmaker[AsyncSession], quest_ids: tuple[str, str]) -> None:
    async with session_factory() as session:
        for quest_id in quest_ids:
            _ = await session.execute(text("DELETE FROM quest_definitions WHERE id = :id"), {"id": quest_id})
        await session.commit()


async def _cleanup(session_factory: async_sessionmaker[AsyncSession], player_id: UUID, user_id: UUID) -> None:
    async with session_factory() as session:
        for table in ("quest_instances", "player_effects", "lucidity_cooldowns", "player_lucidity"):
            _ = await session.execute(text(f"DELETE FROM {table} WHERE player_id = :id"), {"id": str(player_id)})  # noqa: S608  # nosec B608  # nosemgrep: python.sqlalchemy.security.audit.avoid-sqlalchemy-text.avoid-sqlalchemy-text  # Reason: table names are the literals above
        _ = await session.execute(text("DELETE FROM players WHERE player_id = :id"), {"id": str(player_id)})
        _ = await session.execute(text("DELETE FROM users WHERE id = :id"), {"id": str(user_id)})
        await session.commit()


def _registry(session_factory: async_sessionmaker[AsyncSession]) -> PlayerRegistry:
    """No idle TTL, so every unit and read loads the player fresh from the database."""
    return PlayerRegistry(cast(SessionFactory, session_factory), settings=RegistrySettings(idle_ttl_seconds=0))


async def _dirty_up(registry: PlayerRegistry, player_id: UUID, quests: tuple[str, str]) -> None:
    """Give the character everything a finished tutorial run leaves behind, in one synchronous unit."""
    async with registry.mutate(player_id, sync=True) as player:  # pylint: disable=contextmanager-generator-missing-cleanup  # Reason: @asynccontextmanager always drives this generator to completion; pylint cannot see through the wrapper
        player.row.set_current_room_id(ELSEWHERE, sync=True)
        player.row.set_tutorial_instance_id("instance-1")
        player.row.set_stat("current_dp", 3, sync=True)
        player.row.set_stat("max_dp", 80, sync=True)
        player.row.set_stat("corruption", 12, sync=True)
        player.row.set_stat("position", "sitting", sync=True)
        player.inventory.replace([], {})
        _ = player.quests.set(quests[0], state="active")
        _ = player.quests.set(quests[1], state="completed", completed_at=datetime.now(UTC))
        _ = player.effects.add("poison", "debuff", remaining_seconds=30)
        _ = player.effects.add("login_warded", "entry_ward", remaining_seconds=30)
        _ = player.lucidity.set(lcd=-40, tier="uneasy")
        player.cooldowns.set("debrief_pending", datetime.now(UTC) + timedelta(hours=1))
        player.cooldowns.set("folk_tonic", datetime.now(UTC) + timedelta(minutes=30))


@pytest.mark.asyncio
@pytest.mark.usefixtures("fresh_database_manager")
async def test_reset_tutorial_character_starts_a_used_character_over(
    session_factory: async_sessionmaker[AsyncSession],
) -> None:
    name = f"E2ETut_{uuid.uuid4().hex[:8]}"
    player_id, user_id = await _create_player(session_factory, name)
    quests = await _define_quests(session_factory)
    registry = _registry(session_factory)
    support = E2ePlayerSupport(registry, _Persistence({name: player_id}), _Rooms())
    try:
        await _dirty_up(registry, player_id, quests)
        assert (await support.state(name)).quests == {quests[0]: "active", quests[1]: "completed"}

        await support.reset_tutorial_character(name)

        state = await support.state(name)  # a fresh load: TTL 0, so this is what the database holds
        assert state.current_room_id == DEFAULT_RESPAWN_ROOM and state.respawn_room_id == DEFAULT_RESPAWN_ROOM
        assert state.tutorial_instance_id == PENDING_INSTANCE_ID
        assert (state.current_dp, state.corruption) == (80, 0)
        assert state.inventory_items == ["Sling"]
        assert state.quests == {}
        assert state.current_lcd == 100
        assert state.debrief_pending is False
        player = await registry.get(player_id)
        assert player is not None
        assert player.row.stats["position"] == "standing"
        assert [effect.effect_type for effect in player.effects.effects] == ["login_warded"]
        assert player.cooldowns.expires_at("folk_tonic") is None
    finally:
        await _cleanup(session_factory, player_id, user_id)
        await _drop_quests(session_factory, quests)


@pytest.mark.asyncio
@pytest.mark.usefixtures("fresh_database_manager")
async def test_reset_shared_players_returns_them_standing_in_the_default_room(
    session_factory: async_sessionmaker[AsyncSession], monkeypatch: pytest.MonkeyPatch
) -> None:
    names = (f"Shared1_{uuid.uuid4().hex[:8]}", f"Shared2_{uuid.uuid4().hex[:8]}")
    created = [await _create_player(session_factory, name) for name in names]
    quests = await _define_quests(session_factory)
    monkeypatch.setattr(e2e_player_support, "SHARED_PLAYERS", names)
    registry = _registry(session_factory)
    support = E2ePlayerSupport(
        registry, _Persistence({name: pid for name, (pid, _uid) in zip(names, created, strict=True)}), _Rooms()
    )
    try:
        for player_id, _user_id in created:
            await _dirty_up(registry, player_id, quests)

        await support.reset_shared_players()

        for name in names:
            state = await support.state(name)
            assert state.current_room_id == DEFAULT_RESPAWN_ROOM and state.current_dp == 50
            assert state.debrief_pending is True  # only the folk tonic cooldown is forgotten
            assert state.quests == {quests[0]: "active", quests[1]: "completed"}  # a shared reset leaves quests alone
    finally:
        for player_id, user_id in created:
            await _cleanup(session_factory, player_id, user_id)
        await _drop_quests(session_factory, quests)


@pytest.mark.asyncio
@pytest.mark.usefixtures("fresh_database_manager")
async def test_place_moves_the_character_out_of_the_tutorial_and_refuses_an_unknown_room(
    session_factory: async_sessionmaker[AsyncSession],
) -> None:
    name = f"E2EPlace_{uuid.uuid4().hex[:8]}"
    player_id, user_id = await _create_player(session_factory, name)
    quests = await _define_quests(session_factory)
    registry = _registry(session_factory)
    support = E2ePlayerSupport(registry, _Persistence({name: player_id}), _Rooms())
    try:
        await _dirty_up(registry, player_id, quests)

        await support.place(name, DEFAULT_RESPAWN_ROOM)
        with pytest.raises(UnknownRoomError):
            await support.place(name, "no_such_room")

        state = await support.state(name)
        assert state.current_room_id == DEFAULT_RESPAWN_ROOM and state.tutorial_instance_id is None
    finally:
        await _cleanup(session_factory, player_id, user_id)
        await _drop_quests(session_factory, quests)
