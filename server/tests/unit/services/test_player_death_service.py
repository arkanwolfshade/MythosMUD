"""
Unit tests for player death service.

Tests the PlayerDeathService class for managing player mortality and DP decay.
"""

import uuid
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from server.events.event_types import PlayerDiedEvent, PlayerDPDecayEvent
from server.models.game import PositionState
from server.models.player import Player
from server.services.player_death_service import PlayerDeathService


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


@pytest.mark.asyncio
async def test_process_mortally_wounded_tick_player_not_found(player_death_service, mock_session, sample_player_id):
    """Test process_mortally_wounded_tick() returns False when player not found."""
    mock_session.get = AsyncMock(return_value=None)
    result = await player_death_service.process_mortally_wounded_tick(sample_player_id, mock_session)
    assert result is False


@pytest.mark.asyncio
async def test_process_mortally_wounded_tick_already_dead(
    player_death_service, mock_session, sample_player_id, mock_player
):
    """Test process_mortally_wounded_tick() returns False when player already dead."""
    mock_player.is_dead.return_value = True
    mock_session.get = AsyncMock(return_value=mock_player)
    result = await player_death_service.process_mortally_wounded_tick(sample_player_id, mock_session)
    assert result is False


@pytest.mark.asyncio
async def test_process_mortally_wounded_tick_applies_decay(
    player_death_service, mock_session, sample_player_id, mock_player
):
    """Test process_mortally_wounded_tick() applies DP decay via Player.apply_dp_decay."""
    mock_player.get_stats.return_value = {"current_dp": -5, "position": "standing"}
    mock_player.is_dead.return_value = False
    mock_player.apply_dp_decay = MagicMock(return_value=(-5, -6, False))
    mock_session.get = AsyncMock(return_value=mock_player)
    result = await player_death_service.process_mortally_wounded_tick(sample_player_id, mock_session)
    assert result is True
    mock_player.apply_dp_decay.assert_called_once_with(amount=1)
    mock_session.commit.assert_awaited_once()


@pytest.mark.asyncio
async def test_process_mortally_wounded_tick_caps_at_negative_10(
    player_death_service, mock_session, sample_player_id, mock_player
):
    """Test process_mortally_wounded_tick() caps DP at -10 via Player.apply_dp_decay."""
    mock_player.get_stats.return_value = {"current_dp": -10, "position": "lying"}
    mock_player.is_dead.return_value = False
    mock_player.apply_dp_decay = MagicMock(return_value=(-10, -10, False))
    mock_session.get = AsyncMock(return_value=mock_player)
    result = await player_death_service.process_mortally_wounded_tick(sample_player_id, mock_session)
    assert result is True
    mock_player.apply_dp_decay.assert_called_once_with(amount=1)


@pytest.mark.asyncio
async def test_process_mortally_wounded_tick_changes_posture_to_lying(
    player_death_service, mock_session, sample_player_id, mock_player
):
    """Test process_mortally_wounded_tick() delegates posture change to Player.apply_dp_decay."""
    mock_player.get_stats.return_value = {"current_dp": 0, "position": "standing"}
    mock_player.is_dead.return_value = False
    mock_player.apply_dp_decay = MagicMock(return_value=(0, -1, True))  # posture_changed=True
    mock_session.get = AsyncMock(return_value=mock_player)
    result = await player_death_service.process_mortally_wounded_tick(sample_player_id, mock_session)
    assert result is True
    mock_player.apply_dp_decay.assert_called_once_with(amount=1)


@pytest.mark.asyncio
async def test_process_mortally_wounded_tick_publishes_event(
    player_death_service, mock_session, sample_player_id, mock_player, mock_event_bus
):
    """Test process_mortally_wounded_tick() publishes DP decay event."""
    mock_player.get_stats.return_value = {"current_dp": -5, "position": "standing"}
    mock_player.is_dead.return_value = False
    mock_player.apply_dp_decay = MagicMock(return_value=(-5, -6, False))
    mock_session.get = AsyncMock(return_value=mock_player)
    result = await player_death_service.process_mortally_wounded_tick(sample_player_id, mock_session)
    assert result is True
    mock_event_bus.publish.assert_called_once()
    published_event = mock_event_bus.publish.call_args[0][0]
    assert isinstance(published_event, PlayerDPDecayEvent)
    assert published_event.player_id == sample_player_id


@pytest.mark.asyncio
async def test_process_mortally_wounded_tick_handles_error(player_death_service, mock_session, sample_player_id):
    """Test process_mortally_wounded_tick() handles errors gracefully."""
    mock_session.get = AsyncMock(side_effect=Exception("Database error"))
    result = await player_death_service.process_mortally_wounded_tick(sample_player_id, mock_session)
    assert result is False
    mock_session.rollback.assert_awaited_once()


@pytest.mark.asyncio
async def test_ensure_player_posture_lying_already_lying(player_death_service, mock_player, sample_player_id):
    """Test _ensure_player_posture_lying() does nothing when already lying."""
    mock_player.get_stats.return_value = {"position": PositionState.LYING}
    await player_death_service._ensure_player_posture_lying(mock_player, sample_player_id)
    # Should not call set_stats if already lying
    mock_player.set_stats.assert_not_called()


@pytest.mark.asyncio
async def test_ensure_player_posture_lying_changes_posture(player_death_service, mock_player, sample_player_id):
    """Test _ensure_player_posture_lying() changes posture to lying."""
    mock_player.get_stats.return_value = {"position": "standing"}
    await player_death_service._ensure_player_posture_lying(mock_player, sample_player_id)
    mock_player.set_stats.assert_called_once()
    call_args = mock_player.set_stats.call_args
    assert call_args[0][0]["position"] == PositionState.LYING


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
    with patch("server.container.ApplicationContainer") as mock_container:
        mock_instance = MagicMock()
        mock_instance.async_persistence.get_room_by_id.return_value = mock_room
        mock_container.get_instance.return_value = mock_instance
        result = player_death_service._get_room_name_for_death("room_001")
        assert result == "Test Room"


def test_get_room_name_for_death_no_room(player_death_service):
    """Test _get_room_name_for_death() returns room_id when room not found."""
    with patch("server.container.ApplicationContainer") as mock_container:
        mock_instance = MagicMock()
        mock_instance.async_persistence.get_room_by_id.return_value = None
        mock_container.get_instance.return_value = mock_instance
        result = player_death_service._get_room_name_for_death("room_001")
        assert result == "room_001"


def test_get_room_name_for_death_empty_location(player_death_service):
    """Test _get_room_name_for_death() returns 'Unknown' for empty location."""
    result = player_death_service._get_room_name_for_death("")
    assert result == "Unknown"


def test_get_room_name_for_death_no_container(player_death_service):
    """Test _get_room_name_for_death() returns room_id when container unavailable."""
    with patch("server.container.ApplicationContainer") as mock_container:
        mock_container.get_instance.return_value = None
        result = player_death_service._get_room_name_for_death("room_001")
        assert result == "room_001"


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
async def test_handle_player_death_success(player_death_service, mock_session, sample_player_id, mock_player):
    """Test handle_player_death() successfully handles player death."""
    mock_session.get = AsyncMock(return_value=mock_player)
    result = await player_death_service.handle_player_death(sample_player_id, "room_001", None, mock_session)
    assert result is True
    mock_session.commit.assert_awaited_once()
    player_death_service._event_bus.publish.assert_called_once()


@pytest.mark.asyncio
async def test_handle_player_death_player_not_found(player_death_service, mock_session, sample_player_id):
    """Test handle_player_death() returns False when player not found."""
    mock_session.get = AsyncMock(return_value=None)
    result = await player_death_service.handle_player_death(sample_player_id, "room_001", None, mock_session)
    assert result is False


@pytest.mark.asyncio
async def test_handle_player_death_with_killer_info(player_death_service, mock_session, sample_player_id, mock_player):
    """Test handle_player_death() handles death with killer information."""
    killer_info = {"killer_id": uuid.uuid4(), "killer_name": "KillerPlayer"}
    mock_session.get = AsyncMock(return_value=mock_player)
    result = await player_death_service.handle_player_death(sample_player_id, "room_001", killer_info, mock_session)
    assert result is True
    published_event = player_death_service._event_bus.publish.call_args[0][0]
    assert published_event.killer_id == killer_info["killer_id"]


@pytest.mark.asyncio
async def test_handle_player_death_clears_combat_state(
    player_death_service, mock_session, sample_player_id, mock_player, mock_player_combat_service
):
    """Test handle_player_death() clears combat state."""
    mock_session.get = AsyncMock(return_value=mock_player)
    await player_death_service.handle_player_death(sample_player_id, "room_001", None, mock_session)
    mock_player_combat_service.clear_player_combat_state.assert_awaited_once_with(sample_player_id)


@pytest.mark.asyncio
async def test_handle_player_death_handles_error(player_death_service, mock_session, sample_player_id):
    """Test handle_player_death() handles errors gracefully."""
    mock_session.get = AsyncMock(side_effect=Exception("Database error"))
    result = await player_death_service.handle_player_death(sample_player_id, "room_001", None, mock_session)
    assert result is False
    mock_session.rollback.assert_awaited_once()
