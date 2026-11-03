"""
Unit tests for player death service.

Tests the PlayerDeathService class for managing player mortality and DP decay.
"""

# pyright: reportUnknownMemberType=false
# TEST_MOCK: AsyncMock attribute chains off the untyped `mock_session` fixture
# (mock_session.rollback.assert_awaited_once, ...) resolve to Unknown throughout this file.

import uuid
from unittest.mock import AsyncMock, MagicMock, patch

import pytest
from sqlalchemy.exc import SQLAlchemyError

from server.events.event_types import BaseEvent, PlayerDiedEvent, PlayerDPDecayEvent
from server.models.game import PositionState
from server.models.player import Player
from server.services.player_death_service import PlayerDeathService
from server.tests.fixtures.shared.player_registry import LucidityHarness, lucidity_registry

REGISTRY_PLAYER = uuid.uuid4()


@pytest.fixture
def mock_event_bus():
    """Create a mock event bus."""
    bus = MagicMock()
    bus.publish = MagicMock()
    return bus


@pytest.fixture
def mock_player_combat_service():
    """Create a mock player combat service."""
    service = MagicMock()
    service.clear_player_combat_state = AsyncMock()
    return service


@pytest.fixture
def player_death_service(mock_event_bus, mock_player_combat_service):
    """Create a PlayerDeathService instance."""
    return PlayerDeathService(event_bus=mock_event_bus, player_combat_service=mock_player_combat_service)


@pytest.fixture
def player_death_service_no_dependencies():
    """Create a PlayerDeathService instance without dependencies."""
    return PlayerDeathService()


@pytest.fixture
def mock_session():
    """Create a mock async session."""
    session = AsyncMock()
    session.execute = AsyncMock()
    session.get = AsyncMock()
    session.commit = AsyncMock()
    session.rollback = AsyncMock()
    return session


@pytest.fixture
def sample_player_id():
    """Create a sample player ID."""
    return uuid.uuid4()


@pytest.fixture
def mock_player(sample_player_id):
    """Create a mock player."""
    player = MagicMock(spec=Player)
    player.player_id = sample_player_id
    player.name = "TestPlayer"
    player.current_room_id = uuid.uuid4()
    player.get_stats = MagicMock(return_value={"current_dp": 0})
    player.set_stats = MagicMock()
    player.is_dead = MagicMock(return_value=False)
    player.is_mortally_wounded = MagicMock(return_value=False)
    return player


def test_player_death_service_init(player_death_service, mock_event_bus, mock_player_combat_service):
    """Test PlayerDeathService initialization."""
    assert player_death_service._event_bus == mock_event_bus
    assert player_death_service._player_combat_service == mock_player_combat_service


def test_player_death_service_init_no_dependencies(player_death_service_no_dependencies):
    """Test PlayerDeathService initialization without dependencies."""
    assert player_death_service_no_dependencies._event_bus is None
    assert player_death_service_no_dependencies._player_combat_service is None


@pytest.mark.asyncio
async def test_get_mortally_wounded_players_empty(player_death_service, mock_session):
    """Test get_mortally_wounded_players() returns empty list when no mortally wounded players."""
    mock_result = MagicMock()
    mock_result.scalars.return_value.all.return_value = []
    mock_session.execute = AsyncMock(return_value=mock_result)
    result = await player_death_service.get_mortally_wounded_players(mock_session)
    assert result == []


@pytest.mark.asyncio
async def test_get_mortally_wounded_players_finds_mortally_wounded(player_death_service, mock_session, mock_player):
    """Test get_mortally_wounded_players() finds mortally wounded players."""
    mock_player.get_stats.return_value = {"current_dp": -5}  # Mortally wounded
    mock_player.is_mortally_wounded.return_value = True
    mock_result = MagicMock()
    mock_result.scalars.return_value.all.return_value = [mock_player]
    mock_session.execute = AsyncMock(return_value=mock_result)
    result = await player_death_service.get_mortally_wounded_players(mock_session)
    assert len(result) == 1
    assert result[0] == mock_player


@pytest.mark.asyncio
async def test_get_mortally_wounded_players_excludes_healthy(player_death_service, mock_session, mock_player):
    """Test get_mortally_wounded_players() excludes healthy players."""
    mock_player.get_stats.return_value = {"current_dp": 10}  # Healthy
    mock_player.is_mortally_wounded.return_value = False
    mock_result = MagicMock()
    mock_result.scalars.return_value.all.return_value = [mock_player]
    mock_session.execute = AsyncMock(return_value=mock_result)
    result = await player_death_service.get_mortally_wounded_players(mock_session)
    assert len(result) == 0


@pytest.mark.asyncio
async def test_get_mortally_wounded_players_excludes_dead(player_death_service, mock_session, mock_player):
    """Test get_mortally_wounded_players() excludes dead players."""
    mock_player.get_stats.return_value = {"current_dp": -10}  # Dead
    mock_player.is_mortally_wounded.return_value = False  # Dead players are not mortally wounded
    mock_result = MagicMock()
    mock_result.scalars.return_value.all.return_value = [mock_player]
    mock_session.execute = AsyncMock(return_value=mock_result)
    result = await player_death_service.get_mortally_wounded_players(mock_session)
    assert len(result) == 0


@pytest.mark.asyncio
async def test_get_mortally_wounded_players_handles_error(player_death_service, mock_session):
    """Test get_mortally_wounded_players() handles errors gracefully."""
    mock_session.execute = AsyncMock(side_effect=Exception("Database error"))
    result = await player_death_service.get_mortally_wounded_players(mock_session)
    assert result == []
    # Regression: this session is shared with get_dead_players for the rest of the tick;
    # without a rollback, Postgres leaves the transaction aborted and cascades this
    # failure onto every later query on it.
    mock_session.rollback.assert_awaited_once()


@pytest.mark.asyncio
async def test_get_dead_players_empty(player_death_service, mock_session):
    """Test get_dead_players() returns empty list when no dead players."""
    mock_result = MagicMock()
    mock_result.scalars.return_value.all.return_value = []
    mock_session.execute = AsyncMock(return_value=mock_result)
    result = await player_death_service.get_dead_players(mock_session)
    assert result == []


@pytest.mark.asyncio
async def test_get_dead_players_finds_dead(player_death_service, mock_session, mock_player):
    """Test get_dead_players() finds dead players."""
    mock_player.get_stats.return_value = {"current_dp": -10}  # Dead
    mock_player.is_dead.return_value = True
    mock_result = MagicMock()
    mock_result.scalars.return_value.all.return_value = [mock_player]
    mock_session.execute = AsyncMock(return_value=mock_result)
    result = await player_death_service.get_dead_players(mock_session)
    assert len(result) == 1
    assert result[0] == mock_player


@pytest.mark.asyncio
async def test_get_dead_players_excludes_alive(player_death_service, mock_session, mock_player):
    """Test get_dead_players() excludes alive players."""
    mock_player.get_stats.return_value = {"current_dp": 5}  # Alive
    mock_result = MagicMock()
    mock_result.scalars.return_value.all.return_value = [mock_player]
    mock_session.execute = AsyncMock(return_value=mock_result)
    result = await player_death_service.get_dead_players(mock_session)
    assert len(result) == 0


@pytest.mark.asyncio
async def test_get_dead_players_handles_error(player_death_service, mock_session):
    """Test get_dead_players() handles errors gracefully."""
    # The function catches exceptions and returns empty list
    mock_session.execute = AsyncMock(side_effect=ValueError("Database error"))
    result = await player_death_service.get_dead_players(mock_session)
    assert result == []
    # Regression: same cascading-transaction concern as get_mortally_wounded_players.
    mock_session.rollback.assert_awaited_once()


class _Bus:
    """Records what the death service publishes."""

    def __init__(self) -> None:
        self.events: list[BaseEvent] = []

    def publish(self, event: BaseEvent) -> None:
        self.events.append(event)


class _Combat:
    """Records which players had their combat state cleared."""

    def __init__(self) -> None:
        self.cleared: list[uuid.UUID] = []

    async def clear_player_combat_state(self, player_id: uuid.UUID) -> None:
        self.cleared.append(player_id)


def _registry_service(
    *, current_dp: int = -5, position: str = "standing", event_bus: _Bus | None = None, combat: _Combat | None = None
) -> tuple[PlayerDeathService, LucidityHarness]:
    """A death service on a real registry holding one player (ADR-029 step 6a)."""
    harness = lucidity_registry(
        {REGISTRY_PLAYER: None},
        stats={"current_dp": current_dp, "max_dp": 20, "position": position},
        row={"name": "TestPlayer", "current_room_id": "room_001"},
    )
    service = PlayerDeathService(event_bus=event_bus, player_combat_service=combat, player_registry=harness.registry)
    return service, harness


@pytest.mark.asyncio
async def test_process_mortally_wounded_tick_player_not_found() -> None:
    service, _ = _registry_service()
    assert await service.process_mortally_wounded_tick(uuid.uuid4()) is None


@pytest.mark.asyncio
async def test_process_mortally_wounded_tick_without_a_registry_does_nothing() -> None:
    assert await PlayerDeathService().process_mortally_wounded_tick(REGISTRY_PLAYER) is None


@pytest.mark.asyncio
async def test_process_mortally_wounded_tick_already_dead() -> None:
    service, harness = _registry_service(current_dp=-10)

    assert await service.process_mortally_wounded_tick(REGISTRY_PLAYER) is None
    assert harness.db.commits == 0


@pytest.mark.asyncio
async def test_process_mortally_wounded_tick_applies_decay() -> None:
    service, harness = _registry_service(current_dp=-5, position="lying")

    change = await service.process_mortally_wounded_tick(REGISTRY_PLAYER)

    assert change is not None and (change.old_dp, change.new_dp) == (-5, -6)
    assert harness.stats(REGISTRY_PLAYER)["current_dp"] == -6
    assert harness.db.commits == 1  # sync: the next tick's database query sees it


@pytest.mark.asyncio
async def test_process_mortally_wounded_tick_reaches_minus_10() -> None:
    service, _ = _registry_service(current_dp=-9, position="lying")

    change = await service.process_mortally_wounded_tick(REGISTRY_PLAYER)

    assert change is not None and change.new_dp == -10 and change.became_dead


@pytest.mark.asyncio
async def test_process_mortally_wounded_tick_changes_posture_to_lying() -> None:
    service, harness = _registry_service(current_dp=0, position="standing")

    _ = await service.process_mortally_wounded_tick(REGISTRY_PLAYER)

    assert harness.stats(REGISTRY_PLAYER)["position"] == PositionState.LYING


@pytest.mark.asyncio
async def test_process_mortally_wounded_tick_publishes_event() -> None:
    bus = _Bus()
    service, _ = _registry_service(event_bus=bus)

    _ = await service.process_mortally_wounded_tick(REGISTRY_PLAYER)

    [published_event] = bus.events
    assert isinstance(published_event, PlayerDPDecayEvent)
    assert (published_event.player_id, published_event.new_dp, published_event.room_id) == (
        REGISTRY_PLAYER,
        -6,
        "room_001",
    )


@pytest.mark.asyncio
async def test_process_mortally_wounded_tick_handles_a_failed_commit() -> None:
    bus = _Bus()
    service, harness = _registry_service(event_bus=bus)
    harness.db.fail_commits, harness.db.commit_error = 1, SQLAlchemyError("Database error")

    assert await service.process_mortally_wounded_tick(REGISTRY_PLAYER) is None
    assert bus.events == []


@pytest.mark.asyncio
async def test_clear_player_combat_state_success(player_death_service, sample_player_id, mock_player_combat_service):
    """Test _clear_player_combat_state() clears combat state."""
    await player_death_service._clear_player_combat_state(sample_player_id)
    mock_player_combat_service.clear_player_combat_state.assert_awaited_once_with(sample_player_id)


@pytest.mark.asyncio
async def test_clear_player_combat_state_no_service(player_death_service_no_dependencies, sample_player_id):
    """Test _clear_player_combat_state() does nothing when service unavailable."""
    # Should not raise
    await player_death_service_no_dependencies._clear_player_combat_state(sample_player_id)


@pytest.mark.asyncio
async def test_clear_player_combat_state_handles_error(
    player_death_service, sample_player_id, mock_player_combat_service
):
    """Test _clear_player_combat_state() handles errors gracefully."""
    # The function catches exceptions and logs them
    mock_player_combat_service.clear_player_combat_state = AsyncMock(side_effect=ValueError("Service error"))
    # Should not raise, should handle gracefully
    await player_death_service._clear_player_combat_state(sample_player_id)


def test_get_room_name_for_death_with_room(player_death_service):
    """Test _get_room_name_for_death() returns room name when available."""
    mock_room = MagicMock()
    mock_room.name = "Test Room"
    mock_room.zone_name = "Test Zone"
    mock_room.sub_zone_name = "Test Sub"
    mock_persistence = MagicMock()
    mock_persistence.get_room_by_id.return_value = mock_room
    player_death_service._async_persistence = mock_persistence  # #679: injected, not via container
    result = player_death_service._get_room_name_for_death("room_001")
    assert result == "Test Zone › Test Sub › Test Room"


def test_get_room_name_for_death_no_room(player_death_service):
    """Test _get_room_name_for_death() never leaks the room_id when room not found (#910)."""
    mock_persistence = MagicMock()
    mock_persistence.get_room_by_id.return_value = None
    player_death_service._async_persistence = mock_persistence  # #679: injected, not via container
    result = player_death_service._get_room_name_for_death("room_001")
    assert result == "Unknown Location"


def test_get_room_name_for_death_empty_location(player_death_service):
    """Test _get_room_name_for_death() returns 'Unknown Location' for empty location."""
    result = player_death_service._get_room_name_for_death("")
    assert result == "Unknown Location"


def test_get_room_name_for_death_no_container(player_death_service):
    """Test _get_room_name_for_death() never leaks the room_id when async_persistence unavailable (#910)."""
    player_death_service._async_persistence = None
    result = player_death_service._get_room_name_for_death("room_001")
    assert result == "Unknown Location"


def test_publish_death_event_with_event_bus(player_death_service, sample_player_id, mock_event_bus):
    """Test _publish_death_event() publishes event when event bus available."""
    player_death_service._publish_death_event(sample_player_id, "TestPlayer", "room_001", None)
    mock_event_bus.publish.assert_called_once()
    published_event = mock_event_bus.publish.call_args[0][0]
    assert isinstance(published_event, PlayerDiedEvent)
    assert published_event.player_id == sample_player_id
    assert published_event.player_name == "TestPlayer"


def test_publish_death_event_with_killer_info(player_death_service, sample_player_id, mock_event_bus):
    """Test _publish_death_event() includes killer information."""
    killer_info = {"killer_id": uuid.uuid4(), "killer_name": "KillerPlayer"}
    player_death_service._publish_death_event(sample_player_id, "TestPlayer", "room_001", killer_info)
    published_event = mock_event_bus.publish.call_args[0][0]
    assert published_event.killer_id == killer_info["killer_id"]
    assert published_event.killer_name == killer_info["killer_name"]


def test_publish_death_event_no_event_bus(player_death_service_no_dependencies, sample_player_id):
    """Test _publish_death_event() does nothing when event bus unavailable."""
    # Should not raise
    player_death_service_no_dependencies._publish_death_event(sample_player_id, "TestPlayer", "room_001", None)


@pytest.mark.asyncio
async def test_handle_player_death_lays_the_player_down_and_records_the_room() -> None:
    bus, combat = _Bus(), _Combat()
    service, harness = _registry_service(current_dp=-10, event_bus=bus, combat=combat)

    with patch.object(service, "_get_room_name_for_death", return_value="Arkham › Street"):
        assert await service.handle_player_death(REGISTRY_PLAYER, "room_001", None) is True

    stats = harness.stats(REGISTRY_PLAYER)
    assert stats["position"] == PositionState.LYING
    assert (stats["death_room_id"], stats["death_location"]) == ("room_001", "Arkham › Street")
    assert harness.db.commits == 1
    assert combat.cleared == [REGISTRY_PLAYER]
    [event] = bus.events
    assert isinstance(event, PlayerDiedEvent)


@pytest.mark.asyncio
async def test_handle_player_death_player_not_found() -> None:
    service, _ = _registry_service()
    assert await service.handle_player_death(uuid.uuid4(), "room_001", None) is False


@pytest.mark.asyncio
async def test_handle_player_death_with_killer_info() -> None:
    killer_id = uuid.uuid4()
    bus = _Bus()
    service, _ = _registry_service(current_dp=-10, event_bus=bus)

    assert await service.handle_player_death(REGISTRY_PLAYER, "room_001", {"killer_id": killer_id}) is True

    [published_event] = bus.events
    assert isinstance(published_event, PlayerDiedEvent) and published_event.killer_id == killer_id


@pytest.mark.asyncio
async def test_handle_player_death_handles_a_failed_commit() -> None:
    bus = _Bus()
    service, harness = _registry_service(current_dp=-10, event_bus=bus)
    harness.db.fail_commits, harness.db.commit_error = 1, SQLAlchemyError("Database error")

    assert await service.handle_player_death(REGISTRY_PLAYER, "room_001", None) is False
    assert bus.events == []


def _session_with_players(players: list[MagicMock]) -> AsyncMock:
    """Async session whose select(Player) returns the given players."""
    scalars = MagicMock()
    scalars.all = MagicMock(return_value=players)
    result = MagicMock()
    result.scalars = MagicMock(return_value=scalars)
    return AsyncMock(execute=AsyncMock(return_value=result))


def _player(player_id: uuid.UUID, *, dead: bool = False, mortally_wounded: bool = False) -> MagicMock:
    player = MagicMock(spec=Player)
    player.player_id = player_id
    player.is_dead = MagicMock(return_value=dead)
    player.is_mortally_wounded = MagicMock(return_value=mortally_wounded)
    return player


@pytest.mark.asyncio
@pytest.mark.parametrize("dead", [False, True])
async def test_get_dead_players_debug_only_when_found(dead: bool) -> None:
    """#912: runs every tick; an empty result must not emit a debug line."""
    player_id = uuid.uuid4()
    player = _player(player_id, dead=dead)
    debug = MagicMock()
    with patch("server.services.player_death_service.logger.debug", debug):
        found = await PlayerDeathService().get_dead_players(_session_with_players([player]))
    assert len(found) == int(dead)
    assert debug.call_count == int(dead)
    if dead:
        debug.assert_called_once_with("Found dead players", count=1, player_ids=[player_id])


@pytest.mark.asyncio
@pytest.mark.parametrize("wounded", [False, True])
async def test_get_mortally_wounded_players_debug_only_when_found(wounded: bool) -> None:
    """#912: runs every game-second; an empty result must not emit a debug line."""
    player_id = uuid.uuid4()
    player = _player(player_id, mortally_wounded=wounded)
    debug = MagicMock()
    with patch("server.services.player_death_service.logger.debug", debug):
        found = await PlayerDeathService().get_mortally_wounded_players(_session_with_players([player]))
    assert len(found) == int(wounded)
    assert debug.call_count == int(wounded)
    if wounded:
        debug.assert_called_once_with("Found mortally wounded players", count=1, player_ids=[player_id])
