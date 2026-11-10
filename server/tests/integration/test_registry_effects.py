"""
Integration tests: a player's status effects live in the registry (ADR-029 step 6d), against a real database.

The effects part writes row by row, with the ids it names itself, and loads with the player through
``get_player_lucidity_state``. These tests pin that round trip through the real procedures, the tick's candidate
query, and the sequence that started the whole redesign: the status-effect tick running while a pickup commits.
"""

import asyncio
import uuid
from dataclasses import dataclass, field
from typing import cast
from uuid import UUID

import pytest
from fastapi import FastAPI
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker

from server.app.game_tick_status_effects import process_status_effects
from server.async_persistence import AsyncPersistenceLayer
from server.game.player_registry import PlayerRegistry, RegistrySettings, SessionFactory
from server.models.player import Player
from server.models.user import User

SECOND = 10  # tick_count on a game second (ticks are 0.1 s)
ITEM_PROTOTYPE_ID = "furniture.sanitarium.lost_and_found_chest"


def _stack(name: str) -> dict[str, object]:
    return {
        "item_id": ITEM_PROTOTYPE_ID,
        "prototype_id": ITEM_PROTOTYPE_ID,
        "item_instance_id": f"effects-test-{name}-{uuid.uuid4().hex[:8]}",
        "item_name": name,
        "slot_type": "backpack",
        "quantity": 1,
    }


async def _create_player(session_factory: async_sessionmaker[AsyncSession]) -> tuple[UUID, UUID]:
    user_id = uuid.uuid4()
    player_id = uuid.uuid4()
    async with session_factory() as session:
        session.add(
            User(
                id=str(user_id),
                email=f"effects_{user_id}@example.com",
                username=f"effects_{str(user_id)[:8]}",
                display_name=f"Effects {str(user_id)[:8]}",
                hashed_password="hashed",
                is_active=True,
                is_superuser=False,
                is_verified=True,
            )
        )
        await session.flush()
        session.add(Player(player_id=str(player_id), user_id=str(user_id), name=f"effects_{str(player_id)[:8]}"))
        await session.commit()
    return player_id, user_id


async def _cleanup(session_factory: async_sessionmaker[AsyncSession], player_id: UUID, user_id: UUID) -> None:
    async with session_factory() as session:
        _ = await session.execute(text("DELETE FROM player_effects WHERE player_id = :id"), {"id": str(player_id)})
        _ = await session.execute(text("DELETE FROM players WHERE player_id = :id"), {"id": str(player_id)})
        _ = await session.execute(text("DELETE FROM users WHERE id = :id"), {"id": str(user_id)})
        await session.commit()


def _registry(session_factory: async_sessionmaker[AsyncSession]) -> PlayerRegistry:
    """As in production for now: no idle TTL, so every unit loads the player fresh from the database."""
    return PlayerRegistry(cast(SessionFactory, session_factory), settings=RegistrySettings(idle_ttl_seconds=0))


async def _effects(registry: PlayerRegistry, player_id: UUID) -> list[tuple[str, int | None, dict[str, object]]]:
    """What a fresh load of the player holds: (type, seconds left, payload) per running effect, oldest first."""
    player = await registry.get(player_id)
    assert player is not None
    return [(effect.effect_type, effect.remaining_seconds, dict(effect.payload)) for effect in player.effects.effects]


@pytest.mark.asyncio
@pytest.mark.usefixtures("fresh_database_manager")
async def test_effects_round_trip_through_the_real_procedures(
    session_factory: async_sessionmaker[AsyncSession],
) -> None:
    player_id, user_id = await _create_player(session_factory)
    registry = _registry(session_factory)
    try:
        async with registry.mutate(player_id) as player:  # pylint: disable=contextmanager-generator-missing-cleanup  # Reason: @asynccontextmanager always drives this generator to completion; pylint cannot see through the wrapper
            _ = player.effects.add("login_warded", "entry_ward", remaining_seconds=2, source="game_entry")
        async with registry.mutate(player_id) as player:  # pylint: disable=contextmanager-generator-missing-cleanup  # Reason: @asynccontextmanager always drives this generator to completion; pylint cannot see through the wrapper
            _ = player.effects.add(
                "lucidity_drain_over_time", "scripted", payload={"rate": 1, "elapsed": 0}, instance_scoped=True
            )

        assert await _effects(registry, player_id) == [
            ("login_warded", 2, {}),
            ("lucidity_drain_over_time", None, {"rate": 1, "elapsed": 0}),
        ]

        async with registry.mutate(player_id) as player:  # pylint: disable=contextmanager-generator-missing-cleanup  # Reason: @asynccontextmanager always drives this generator to completion; pylint cannot see through the wrapper
            drain = player.effects.effects[1]
            assert player.effects.set_payload(drain.id, {"rate": 1, "elapsed": 1})
            assert player.effects.advance_second() == []  # the ward has a second left

        assert await _effects(registry, player_id) == [
            ("login_warded", 1, {}),
            ("lucidity_drain_over_time", None, {"rate": 1, "elapsed": 1}),
        ]

        async with registry.mutate(player_id) as player:  # pylint: disable=contextmanager-generator-missing-cleanup  # Reason: @asynccontextmanager always drives this generator to completion; pylint cannot see through the wrapper
            ended = player.effects.advance_second()
            assert [effect.effect_type for effect in ended] == ["login_warded"]

        assert [kind for kind, _left, _payload in await _effects(registry, player_id)] == ["lucidity_drain_over_time"]

        async with registry.mutate(player_id) as player:  # pylint: disable=contextmanager-generator-missing-cleanup  # Reason: @asynccontextmanager always drives this generator to completion; pylint cannot see through the wrapper
            assert player.effects.clear_instance_scoped() == 1

        assert await _effects(registry, player_id) == []
    finally:
        await _cleanup(session_factory, player_id, user_id)


@pytest.mark.asyncio
@pytest.mark.usefixtures("fresh_database_manager")
async def test_the_ticks_candidates_are_the_online_players_with_a_running_effect(
    session_factory: async_sessionmaker[AsyncSession],
) -> None:
    with_effect, user_a = await _create_player(session_factory)
    without_effect, user_b = await _create_player(session_factory)
    registry = _registry(session_factory)
    persistence = AsyncPersistenceLayer(_skip_room_cache=True)
    try:
        async with registry.mutate(with_effect) as player:  # pylint: disable=contextmanager-generator-missing-cleanup  # Reason: @asynccontextmanager always drives this generator to completion; pylint cannot see through the wrapper
            _ = player.effects.add("blinded", "spell", remaining_seconds=5)

        assert await persistence.get_player_ids_with_effects([with_effect, without_effect]) == [with_effect]
        assert await persistence.get_player_ids_with_effects([without_effect]) == []
        assert await persistence.get_player_ids_with_effects([]) == []
    finally:
        await _cleanup(session_factory, with_effect, user_a)
        await _cleanup(session_factory, without_effect, user_b)


@dataclass
class _Connections:
    online_players: dict[UUID, dict[str, object]]
    player_websockets: dict[UUID, list[str]] = field(default_factory=lambda: dict[UUID, list[str]]())


@dataclass
class _Container:
    async_persistence: AsyncPersistenceLayer
    connection_manager: _Connections
    player_registry: PlayerRegistry


@pytest.mark.asyncio
@pytest.mark.usefixtures("fresh_database_manager")
async def test_the_status_effect_tick_racing_a_pickup_loses_neither(
    session_factory: async_sessionmaker[AsyncSession],
) -> None:
    """The 15:15:23 sequence, now with the tick on the registry: every second's heal and every pickup survive."""
    player_id, user_id = await _create_player(session_factory)
    registry = _registry(session_factory)
    app = FastAPI()
    app.state.container = _Container(
        AsyncPersistenceLayer(_skip_room_cache=True), _Connections({player_id: {}}), registry
    )
    try:
        async with registry.mutate(player_id) as player:  # pylint: disable=contextmanager-generator-missing-cleanup  # Reason: @asynccontextmanager always drives this generator to completion; pylint cannot see through the wrapper
            player.row.set_stat("max_dp", 20, sync=True)
            player.row.set_stat("current_dp", 5, sync=True)
            player.inventory.replace([_stack("lantern"), _stack("coin")], {})
            _ = player.effects.add("heal_over_time", "scripted", remaining_seconds=30, payload={"healing": 1})

        async def pick_up(name: str) -> None:
            async with registry.mutate(player_id) as player:  # pylint: disable=contextmanager-generator-missing-cleanup  # Reason: @asynccontextmanager always drives this generator to completion; pylint cannot see through the wrapper
                player.inventory.set_carried([*(dict(stack) for stack in player.inventory.carried), _stack(name)])

        for second in range(5):
            _ = await asyncio.gather(process_status_effects(app, SECOND), pick_up(f"item{second}"))

        player = await registry.get(player_id)
        assert player is not None
        assert len(player.inventory.carried) == 2 + 5  # no pickup was lost to a tick's copy
        assert player.row.stats["current_dp"] == 10  # five seconds of healing 1
        assert await _effects(registry, player_id) == [("heal_over_time", 25, {"healing": 1})]
    finally:
        await _cleanup(session_factory, player_id, user_id)
