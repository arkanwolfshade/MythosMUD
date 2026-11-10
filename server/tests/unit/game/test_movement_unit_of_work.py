"""
Unit tests for how MovementService uses the player registry (ADR-029 step 7a).

A move is one unit of work on the moving player: their registry lock is held from validation to the commit, the new
room (and a tutorial exit) is committed in one sync write, and the instance flush waits until it has committed.
"""

import asyncio
import json
import uuid
from typing import cast
from unittest.mock import AsyncMock, MagicMock, patch

import pytest
from sqlalchemy.exc import SQLAlchemyError

from server.exceptions import DatabaseError
from server.game.instance_manager import InstanceManager
from server.game.movement_service import MovementService
from server.game.player_registry import DbSession, PlayerAggregate, PlayerRegistry
from server.models.room import Room
from server.services.instance_flush_service import InstanceFlushService
from server.tests.fixtures.shared.player_registry import FakeDatabase, aggregate, any_player_registry, raw_row

BEDROOM_ID = "earth_arkhamcity_sanitarium_room_tutorial_bedroom_001"
FOYER_ID = "earth_arkhamcity_sanitarium_room_foyer_001"
HALLWAY_ID = "earth_arkhamcity_sanitarium_room_hallway_001"


@pytest.fixture(name="db")
def _db() -> FakeDatabase:
    return FakeDatabase()


@pytest.fixture(name="registry")
def _registry(db: FakeDatabase) -> PlayerRegistry:
    return any_player_registry(db)


@pytest.fixture(name="persistence")
def _persistence() -> MagicMock:
    return MagicMock()


@pytest.fixture(name="service")
def _service(persistence: MagicMock, registry: PlayerRegistry) -> MovementService:
    return MovementService(async_persistence=persistence, player_registry=registry)


def _committed_changes(db: FakeDatabase) -> list[dict[str, object]]:
    """The changed columns of every update_player_row the registry committed, in order."""
    return [json.loads(str(params["changes"])) for params in db.executed if params is not None and "changes" in params]


async def _nobody(_session: DbSession, _player_id: uuid.UUID) -> None:
    return None


def _template_bedroom() -> Room:
    return Room(
        {
            "id": BEDROOM_ID,
            "attributes": {"instance_template_id": "tutorial_sanitarium", "instance_exit_room_id": FOYER_ID},
        }
    )


def _foyer() -> Room:
    return Room({"id": FOYER_ID, "attributes": {}})


def _wire_simple_move(persistence: MagicMock, player_id: uuid.UUID) -> None:
    """A persisted player in room_001, and two rooms that let them go to room_002."""
    persisted = MagicMock()
    persisted.configure_mock(player_id=player_id, current_room_id="room_001")
    from_room = MagicMock()
    from_room.configure_mock(id="room_001", has_player=MagicMock(return_value=True))
    to_room = MagicMock()
    to_room.configure_mock(id="room_002")

    def room_for(room_id: str) -> MagicMock:
        return from_room if room_id == "room_001" else to_room

    persistence.configure_mock(
        get_player_by_id=AsyncMock(return_value=persisted), get_room_by_id=MagicMock(side_effect=room_for)
    )


# --- construction ------------------------------------------------------------------------------------------------


def test_the_service_keeps_its_persistence(persistence: MagicMock, registry: PlayerRegistry) -> None:
    service = MovementService(async_persistence=persistence, player_registry=registry)

    assert service._persistence is persistence  # pyright: ignore[reportPrivateUsage] -- the construction is what is under test


def test_the_service_cannot_run_without_a_registry(persistence: MagicMock) -> None:
    """A move is a unit of work on the player registry, so there is no fallback to saving the player directly."""
    with pytest.raises(ValueError, match="player_registry is required"):
        _ = MovementService(async_persistence=persistence)


# --- placing a player ------------------------------------------------------------------------------------------


@pytest.mark.asyncio
async def test_adding_a_player_to_a_room_commits_the_room_through_the_registry(
    service: MovementService, persistence: MagicMock, db: FakeDatabase
) -> None:
    room = MagicMock()
    room.configure_mock(room_id="room_009", has_player=MagicMock(return_value=False))
    persistence.configure_mock(get_room_by_id=MagicMock(return_value=room))

    assert await service.add_player_to_room(uuid.uuid4(), "room_009") is True

    assert _committed_changes(db) == [{"current_room_id": "room_009"}]


@pytest.mark.asyncio
async def test_adding_a_player_the_registry_does_not_know_places_the_room_and_writes_nothing(
    persistence: MagicMock, db: FakeDatabase
) -> None:
    service = MovementService(async_persistence=persistence, player_registry=PlayerRegistry(db.session, loader=_nobody))
    room = MagicMock()
    room.configure_mock(room_id="room_009", has_player=MagicMock(return_value=False))
    persistence.configure_mock(get_room_by_id=MagicMock(return_value=room))

    assert await service.add_player_to_room(uuid.uuid4(), "room_009") is True

    assert db.commits == 0


# --- a move is one unit of work --------------------------------------------------------------------------------


@pytest.mark.asyncio
async def test_a_move_commits_the_new_room_once_and_never_saves_the_whole_player(
    service: MovementService, persistence: MagicMock, db: FakeDatabase
) -> None:
    player_id = uuid.uuid4()
    _wire_simple_move(persistence, player_id)

    with (
        patch.object(service, "_validate_movement", new=AsyncMock(return_value=True)),
        patch("server.game.movement_service.get_movement_monitor"),
    ):
        moved = await service.move_player(player_id, "room_001", "room_002")

    assert moved is True
    assert _committed_changes(db) == [{"current_room_id": "room_002"}]  # one changed column, not the whole row
    assert db.commits == 1


@pytest.mark.asyncio
async def test_two_moves_of_one_player_do_not_interleave(service: MovementService, persistence: MagicMock) -> None:
    """The old threading.RLock excluded nothing between coroutines: both moves validated at once."""
    player_id = uuid.uuid4()
    _wire_simple_move(persistence, player_id)
    inside = 0
    most_inside = 0

    async def slow_validation(*_args: object, **_kwargs: object) -> bool:
        nonlocal inside, most_inside
        inside += 1
        most_inside = max(most_inside, inside)
        await asyncio.sleep(0.02)
        inside -= 1
        return True

    with (
        patch.object(service, "_validate_movement", new=slow_validation),
        patch("server.game.movement_service.get_movement_monitor"),
    ):
        results = await asyncio.gather(
            service.move_player(player_id, "room_001", "room_002"),
            service.move_player(player_id, "room_001", "room_002"),
        )

    assert results == [True, True]
    assert most_inside == 1


@pytest.mark.asyncio
async def test_a_failed_commit_leaves_the_players_room_where_it_was(
    service: MovementService, persistence: MagicMock, registry: PlayerRegistry, db: FakeDatabase
) -> None:
    player_id = uuid.uuid4()
    _wire_simple_move(persistence, player_id)
    db.fail_commits = 1
    db.commit_error = SQLAlchemyError("database unavailable")

    with (
        patch.object(service, "_validate_movement", new=AsyncMock(return_value=True)),
        patch("server.game.movement_service.get_movement_monitor"),
        pytest.raises(DatabaseError),
    ):
        _ = await service.move_player(player_id, "room_001", "room_002")

    live = registry.peek(player_id)
    assert live is not None and live.row.current_room_id == "room_001"
    assert db.commits == 0


@pytest.mark.asyncio
async def test_a_player_the_registry_does_not_know_cannot_move(persistence: MagicMock, db: FakeDatabase) -> None:
    service = MovementService(async_persistence=persistence, player_registry=PlayerRegistry(db.session, loader=_nobody))
    _wire_simple_move(persistence, uuid.uuid4())

    with (
        patch.object(service, "_validate_movement", new=AsyncMock(return_value=True)),
        patch("server.game.movement_service.get_movement_monitor"),
    ):
        moved = await service.move_player(uuid.uuid4(), "room_001", "room_002")

    assert moved is False
    assert db.commits == 0


def test_room_transfer_tells_the_source_room_where_the_player_went(service: MovementService) -> None:
    """Walking sets PlayerLeftRoom.to_room_id; only such leaves count as quest exits (not disconnects)."""
    player_left = MagicMock()
    player_entered = MagicMock()
    from_room = MagicMock()
    from_room.configure_mock(id=FOYER_ID, player_left=player_left)
    to_room = MagicMock()
    to_room.configure_mock(id=HALLWAY_ID, player_entered=player_entered)

    service._execute_room_transfer(from_room, to_room, "player-1", {})  # pyright: ignore[reportPrivateUsage] -- unit-tested directly

    player_left.assert_called_once_with("player-1", to_room_id=HALLWAY_ID)
    player_entered.assert_called_once_with("player-1", force_event=True, from_room_id=FOYER_ID)


# --- leaving the tutorial ----------------------------------------------------------------------------------------


def _exit_setup(
    persistence: MagicMock, registry: PlayerRegistry, respawn_room_id: str
) -> tuple[MovementService, PlayerAggregate, str, AsyncMock]:
    rooms = {BEDROOM_ID: _template_bedroom(), FOYER_ID: _foyer()}
    instance_manager = InstanceManager(room_cache={BEDROOM_ID: rooms[BEDROOM_ID]})
    instance = instance_manager.create_instance("tutorial_sanitarium", uuid.uuid4())
    flush = AsyncMock(return_value=0)
    flusher = MagicMock()
    flusher.configure_mock(flush=flush)
    persistence.configure_mock(get_room_by_id=MagicMock(side_effect=rooms.get))
    service = MovementService(
        async_persistence=persistence,
        instance_manager=instance_manager,
        instance_flush=cast(InstanceFlushService, flusher),
        player_registry=registry,
    )
    player = aggregate(
        raw_row(
            uuid.uuid4(),
            name="Newbie",
            respawn_room_id=respawn_room_id,
            tutorial_instance_id=instance.instance_id,
        )
    )
    return service, player, instance.instance_id, flush


def test_tutorial_exit_clears_the_instance_and_moves_a_template_respawn(
    persistence: MagicMock, registry: PlayerRegistry
) -> None:
    """Walking out clears the instance from the row, and never leaves respawn on the template."""
    service, player, instance_id, _ = _exit_setup(persistence, registry, BEDROOM_ID)

    assert service._apply_tutorial_exit(player, FOYER_ID) == instance_id  # pyright: ignore[reportPrivateUsage] -- unit-tested directly

    assert player.row.tutorial_instance_id is None
    assert player.row.respawn_room_id == FOYER_ID


def test_tutorial_exit_keeps_a_normal_respawn_room(persistence: MagicMock, registry: PlayerRegistry) -> None:
    """A respawn already moved by the quest reward (or any non-template room) is left alone."""
    service, player, instance_id, _ = _exit_setup(persistence, registry, FOYER_ID)

    assert service._apply_tutorial_exit(player, FOYER_ID) == instance_id  # pyright: ignore[reportPrivateUsage] -- unit-tested directly

    assert player.row.respawn_room_id == FOYER_ID


def test_tutorial_exit_hook_ignores_other_destinations(persistence: MagicMock, registry: PlayerRegistry) -> None:
    service, player, instance_id, _ = _exit_setup(persistence, registry, BEDROOM_ID)

    assert service._apply_tutorial_exit(player, HALLWAY_ID) is None  # pyright: ignore[reportPrivateUsage] -- unit-tested directly

    assert player.row.tutorial_instance_id == instance_id
    assert not player.dirty


@pytest.mark.asyncio
async def test_the_exited_instance_is_flushed(persistence: MagicMock, registry: PlayerRegistry) -> None:
    service, player, instance_id, flush = _exit_setup(persistence, registry, FOYER_ID)

    await service._flush_exited_instance(player.player_id, instance_id)  # pyright: ignore[reportPrivateUsage] -- unit-tested directly

    flush.assert_awaited_once_with(instance_id)


@pytest.mark.asyncio
async def test_tutorial_exit_tells_the_player_their_things_are_in_the_deposit_box(
    persistence: MagicMock, registry: PlayerRegistry
) -> None:
    service, player, instance_id, flush = _exit_setup(persistence, registry, FOYER_ID)
    flush.return_value = 2
    sent: list[tuple[str, str]] = []

    async def record(player_id: str, message: str) -> None:
        sent.append((player_id, message))

    with patch("server.game.movement_service.send_system_notification", new=record):
        await service._flush_exited_instance(player.player_id, instance_id)  # pyright: ignore[reportPrivateUsage] -- unit-tested directly

    [(sent_to, message)] = sent
    assert sent_to == str(player.player_id)
    assert "deposit box at Arkham Savings & Trust" in message


@pytest.mark.asyncio
async def test_tutorial_exit_is_silent_when_nothing_was_left_behind(
    persistence: MagicMock, registry: PlayerRegistry
) -> None:
    service, player, instance_id, _ = _exit_setup(persistence, registry, FOYER_ID)  # its flush moves 0 stacks
    sent: list[tuple[str, str]] = []

    async def record(player_id: str, message: str) -> None:
        sent.append((player_id, message))

    with patch("server.game.movement_service.send_system_notification", new=record):
        await service._flush_exited_instance(player.player_id, instance_id)  # pyright: ignore[reportPrivateUsage] -- unit-tested directly

    assert sent == []


@pytest.mark.asyncio
async def test_walking_out_of_the_tutorial_flushes_its_instance_only_after_the_commit(
    persistence: MagicMock, db: FakeDatabase
) -> None:
    """The flush opens its own container unit, so it cannot run inside the player's; it follows the commit."""
    rooms = {BEDROOM_ID: _template_bedroom(), FOYER_ID: _foyer()}
    instance_manager = InstanceManager(room_cache={BEDROOM_ID: rooms[BEDROOM_ID]})
    instance = instance_manager.create_instance("tutorial_sanitarium", uuid.uuid4())
    player_id = uuid.uuid4()

    async def load(_session: DbSession, pid: uuid.UUID) -> PlayerAggregate:
        return aggregate(
            raw_row(
                pid,
                current_room_id=BEDROOM_ID,
                respawn_room_id=BEDROOM_ID,
                tutorial_instance_id=instance.instance_id,
            )
        )

    commits_when_flushed: list[int] = []

    class Flusher:
        async def flush(self, _instance_id: str) -> int:
            commits_when_flushed.append(db.commits)
            return 0

    service = MovementService(
        async_persistence=persistence,
        instance_manager=instance_manager,
        instance_flush=cast(InstanceFlushService, cast(object, Flusher())),  # records when the flush ran
        player_registry=PlayerRegistry(db.session, loader=load),
    )
    persisted = MagicMock()
    persisted.configure_mock(player_id=player_id)
    rooms[BEDROOM_ID].add_player_silently(player_id)  # real rooms: the template bedroom is what marks the respawn
    persistence.configure_mock(
        get_player_by_id=AsyncMock(return_value=persisted), get_room_by_id=MagicMock(side_effect=rooms.get)
    )

    with (
        patch.object(service, "_validate_movement", new=AsyncMock(return_value=True)),
        patch("server.game.movement_service.get_movement_monitor"),
    ):
        moved = await service.move_player(player_id, BEDROOM_ID, FOYER_ID)

    assert moved is True
    assert commits_when_flushed == [1]
    assert _committed_changes(db) == [
        {"current_room_id": FOYER_ID, "respawn_room_id": FOYER_ID, "tutorial_instance_id": None}
    ]
