"""
Unit tests for player respawn service.

Tests the PlayerRespawnService for managing player resurrection and limbo state. Every transition is one sync unit on
the player registry (ADR-029 step 6a), so these run it on a real registry and read back what it holds and wrote.
"""

import json
import uuid
from collections.abc import Callable, Mapping

import pytest
from sqlalchemy.exc import SQLAlchemyError

from server.events.event_types import BaseEvent, PlayerRespawnedEvent
from server.exceptions import DatabaseError
from server.models.game import PositionState
from server.models.room import Room
from server.services.player_respawn_service import (
    DEFAULT_RESPAWN_ROOM,
    LIMBO_ROOM_ID,
    PlayerRespawnService,
)
from server.services.player_respawn_state import DEATH_ROOM_ID_STAT
from server.tests.fixtures.shared.player_registry import LucidityHarness, lucidity_registry

STREET = "earth_arkhamcity_street_room_001"
BEDROOM_ID = "earth_arkhamcity_sanitarium_room_tutorial_bedroom_001"
FOYER_ID = "earth_arkhamcity_sanitarium_room_foyer_001"
PLAYER_ID = uuid.uuid4()


def _harness(*, current_dp: int = -10, respawn_room_id: str | None = None, **stats: object) -> LucidityHarness:
    return lucidity_registry(
        {PLAYER_ID: None},
        stats={"current_dp": current_dp, "max_dp": 30, "position": PositionState.LYING, **stats},
        row={"current_room_id": STREET, "respawn_room_id": respawn_room_id, "name": "TestPlayer"},
    )


def _written_stats(harness: LucidityHarness) -> list[Mapping[str, object]]:
    return [
        json.loads(str(params["stats_changes"]))
        for params in harness.db.executed
        if params is not None and "stats_changes" in params
    ]


class _Bus:
    """Records what the respawn publishes."""

    def __init__(self) -> None:
        self.events: list[BaseEvent] = []

    def publish(self, event: BaseEvent) -> None:
        self.events.append(event)


class _Combat:
    """Records which players had their combat state cleared; ``error`` makes clearing fail."""

    def __init__(self, error: Exception | None = None) -> None:
        self.cleared: list[uuid.UUID] = []
        self._error: Exception | None = error

    async def clear_player_combat_state(self, player_id: uuid.UUID) -> None:
        if self._error is not None:
            raise self._error
        self.cleared.append(player_id)


def _service(
    harness: LucidityHarness,
    *,
    event_bus: _Bus | None = None,
    player_combat_service: _Combat | None = None,
    room_lookup: Callable[[str], Room | None] | None = None,
) -> PlayerRespawnService:
    return PlayerRespawnService(
        event_bus=event_bus,
        player_combat_service=player_combat_service,
        room_lookup=room_lookup,
        player_registry=harness.registry,
    )


@pytest.mark.asyncio
async def test_move_player_to_limbo_moves_the_dead_and_records_the_death_room() -> None:
    harness = _harness()

    assert await _service(harness).move_player_to_limbo(PLAYER_ID, STREET) is True

    assert harness.room(PLAYER_ID) == LIMBO_ROOM_ID
    assert harness.stats(PLAYER_ID)[DEATH_ROOM_ID_STAT] == STREET
    assert harness.db.commits == 1  # sync: committed before returning


@pytest.mark.asyncio
async def test_move_player_to_limbo_refused_when_not_dead() -> None:
    harness = _harness(current_dp=-9)

    assert await _service(harness).move_player_to_limbo(PLAYER_ID, STREET) is False

    assert harness.room(PLAYER_ID) == STREET
    assert harness.db.commits == 0


@pytest.mark.asyncio
async def test_move_player_to_limbo_catatonia_failover_needs_no_dp() -> None:
    """Catatonia failover is lucidity-based: the player goes to limbo at any DP, and no death room is recorded."""
    harness = _harness(current_dp=20)

    assert await _service(harness).move_player_to_limbo(PLAYER_ID, "catatonia_failover") is True

    assert harness.room(PLAYER_ID) == LIMBO_ROOM_ID
    assert DEATH_ROOM_ID_STAT not in harness.stats(PLAYER_ID)


@pytest.mark.asyncio
async def test_move_player_to_limbo_player_not_found() -> None:
    assert await _service(lucidity_registry({})).move_player_to_limbo(uuid.uuid4(), STREET) is False


@pytest.mark.asyncio
@pytest.mark.parametrize("error", [DatabaseError("db down"), SQLAlchemyError("db down")])
async def test_move_player_to_limbo_failed_commit_rolls_back(error: Exception) -> None:
    harness = _harness()
    harness.db.fail_commits, harness.db.commit_error = 1, error

    assert await _service(harness).move_player_to_limbo(PLAYER_ID, STREET) is False

    player = harness.registry.peek(PLAYER_ID)
    assert player is None or player.row.current_room_id == STREET  # the in-memory change rolled back too


@pytest.mark.asyncio
async def test_without_a_registry_nothing_happens() -> None:
    service = PlayerRespawnService()

    assert await service.move_player_to_limbo(PLAYER_ID, STREET) is False
    assert await service.respawn_player(PLAYER_ID) is False
    assert await service.get_respawn_room(PLAYER_ID) == DEFAULT_RESPAWN_ROOM


@pytest.mark.asyncio
async def test_get_respawn_room_custom_and_default() -> None:
    assert await _service(_harness(respawn_room_id=FOYER_ID)).get_respawn_room(PLAYER_ID) == FOYER_ID
    assert await _service(_harness()).get_respawn_room(PLAYER_ID) == DEFAULT_RESPAWN_ROOM
    assert await _service(lucidity_registry({})).get_respawn_room(uuid.uuid4()) == DEFAULT_RESPAWN_ROOM


@pytest.mark.asyncio
async def test_respawn_player_restores_full_dp_standing_in_the_respawn_room() -> None:
    harness = _harness(respawn_room_id=FOYER_ID, death_room_id=STREET, death_location="Street")
    bus, combat = _Bus(), _Combat()
    service = _service(harness, event_bus=bus, player_combat_service=combat)

    assert await service.respawn_player(PLAYER_ID) is True

    stats = harness.stats(PLAYER_ID)
    assert (stats["current_dp"], stats["position"]) == (30, PositionState.STANDING)
    assert harness.room(PLAYER_ID) == FOYER_ID
    assert DEATH_ROOM_ID_STAT not in stats
    assert _written_stats(harness)[-1] == {
        "current_dp": 30,
        "position": "standing",
        "death_room_id": None,  # null removes the key (update_player_row)
        "death_location": None,
    }
    assert combat.cleared == [PLAYER_ID]
    [event] = bus.events
    assert isinstance(event, PlayerRespawnedEvent)
    assert (event.old_dp, event.new_dp, event.respawn_room_id) == (-10, 30, FOYER_ID)


@pytest.mark.asyncio
async def test_respawn_player_survives_a_combat_clear_error() -> None:
    harness = _harness()

    assert await _service(harness, player_combat_service=_Combat(DatabaseError("db down"))).respawn_player(PLAYER_ID)
    assert harness.room(PLAYER_ID) == DEFAULT_RESPAWN_ROOM


@pytest.mark.asyncio
async def test_respawn_player_not_found_and_failed_commit() -> None:
    assert await _service(lucidity_registry({})).respawn_player(uuid.uuid4()) is False

    harness = _harness()
    harness.db.fail_commits, harness.db.commit_error = 1, SQLAlchemyError("db down")
    assert await _service(harness).respawn_player(PLAYER_ID) is False


@pytest.mark.asyncio
async def test_respawn_player_from_delirium_player_not_found() -> None:
    assert await _service(lucidity_registry({})).respawn_player_from_delirium(uuid.uuid4()) is False


def _template_bedroom() -> Room:
    return Room(
        {
            "id": BEDROOM_ID,
            "attributes": {"instance_template_id": "tutorial_sanitarium", "instance_exit_room_id": FOYER_ID},
        }
    )


def _foyer() -> Room:
    return Room({"id": FOYER_ID, "attributes": {}})


@pytest.mark.asyncio
async def test_get_respawn_room_redirects_template_to_exit_room() -> None:
    """A respawn room that is an instance template sends the player to its exit room."""
    rooms = {BEDROOM_ID: _template_bedroom(), FOYER_ID: _foyer()}
    service = _service(_harness(respawn_room_id=BEDROOM_ID), room_lookup=rooms.get)

    assert await service.get_respawn_room(PLAYER_ID) == FOYER_ID


@pytest.mark.asyncio
async def test_get_respawn_room_keeps_normal_custom_room() -> None:
    """Ordinary custom respawn rooms (and services without a room lookup) are unchanged."""
    rooms = {FOYER_ID: _foyer()}

    assert await _service(_harness(respawn_room_id=FOYER_ID), room_lookup=rooms.get).get_respawn_room(PLAYER_ID) == (
        FOYER_ID
    )
    assert await _service(_harness(respawn_room_id=BEDROOM_ID)).get_respawn_room(PLAYER_ID) == BEDROOM_ID
