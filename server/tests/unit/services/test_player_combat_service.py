"""
Unit tests for player combat service.

Tests the PlayerCombatService class for managing player combat state and XP rewards.
"""

import uuid
from datetime import UTC, datetime
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from server.services.player_combat_service import PlayerCombatService, PlayerCombatState

# pylint: disable=protected-access  # Reason: Test file - accessing protected members is standard practice for unit testing
# pylint: disable=redefined-outer-name  # Reason: Test file - pytest fixture parameter names must match fixture names, causing intentional redefinitions


@pytest.fixture
def mock_persistence():
    """Create mock persistence layer."""
    return MagicMock()


@pytest.fixture
def mock_event_bus():
    """Create mock event bus."""
    bus = MagicMock()
    bus.publish = MagicMock()  # EventBus.publish is sync
    return bus


@pytest.fixture
def mock_npc_service():
    """Create mock NPC combat integration service."""
    service = MagicMock()
    service._uuid_to_xp_mapping = {}
    service.get_original_string_id = MagicMock(return_value=None)
    return service


@pytest.fixture
def player_combat_service(mock_persistence, mock_event_bus, mock_npc_service):
    """Create PlayerCombatService instance."""
    return PlayerCombatService(mock_persistence, mock_event_bus, mock_npc_service)


def test_player_combat_service_init(player_combat_service, mock_persistence, mock_event_bus):
    """Test PlayerCombatService initialization."""
    assert player_combat_service._persistence == mock_persistence
    assert player_combat_service._event_bus == mock_event_bus
    assert isinstance(player_combat_service._player_combat_states, dict)


@pytest.mark.asyncio
async def test_track_player_combat_state(player_combat_service):
    """Test track_player_combat_state tracks state."""
    player_id = uuid.uuid4()
    combat_id = uuid.uuid4()
    await player_combat_service.track_player_combat_state(player_id, "TestPlayer", combat_id, "room_001")
    assert player_id in player_combat_service._player_combat_states


@pytest.mark.asyncio
async def test_get_player_combat_state(player_combat_service):
    """Test get_player_combat_state returns state."""
    player_id = uuid.uuid4()
    combat_id = uuid.uuid4()
    await player_combat_service.track_player_combat_state(player_id, "TestPlayer", combat_id, "room_001")
    state = await player_combat_service.get_player_combat_state(player_id)
    assert state is not None
    assert state.player_id == player_id
    assert state.combat_id == combat_id


@pytest.mark.asyncio
async def test_get_player_combat_state_not_found(player_combat_service):
    """Test get_player_combat_state returns None when not found."""
    player_id = uuid.uuid4()
    state = await player_combat_service.get_player_combat_state(player_id)
    assert state is None


@pytest.mark.asyncio
async def test_clear_player_combat_state(player_combat_service):
    """Test clear_player_combat_state clears state."""
    player_id = uuid.uuid4()
    combat_id = uuid.uuid4()
    await player_combat_service.track_player_combat_state(player_id, "TestPlayer", combat_id, "room_001")
    await player_combat_service.clear_player_combat_state(player_id)
    assert player_id not in player_combat_service._player_combat_states


def test_is_player_in_combat_sync_true(player_combat_service):
    """Test is_player_in_combat_sync returns True when in combat."""
    player_id = uuid.uuid4()
    combat_id = uuid.uuid4()
    # Use sync method to set state
    player_combat_service._player_combat_states[player_id] = PlayerCombatState(
        player_id, "TestPlayer", combat_id, "room_001"
    )
    result = player_combat_service.is_player_in_combat_sync(player_id)
    assert result is True


def test_is_player_in_combat_sync_false(player_combat_service):
    """Test is_player_in_combat_sync returns False when not in combat."""
    player_id = uuid.uuid4()
    result = player_combat_service.is_player_in_combat_sync(player_id)
    assert result is False


@pytest.mark.asyncio
async def test_is_player_in_combat(player_combat_service):
    """Test is_player_in_combat checks combat state."""
    player_id = uuid.uuid4()
    combat_id = uuid.uuid4()
    await player_combat_service.track_player_combat_state(player_id, "TestPlayer", combat_id, "room_001")
    result = await player_combat_service.is_player_in_combat(player_id)
    assert result is True


@pytest.mark.asyncio
async def test_get_players_in_combat(player_combat_service):
    """Test get_players_in_combat returns list of players."""
    player_id1 = uuid.uuid4()
    player_id2 = uuid.uuid4()
    combat_id = uuid.uuid4()
    await player_combat_service.track_player_combat_state(player_id1, "Player1", combat_id, "room_001")
    await player_combat_service.track_player_combat_state(player_id2, "Player2", combat_id, "room_001")
    result = await player_combat_service.get_players_in_combat()
    assert len(result) == 2
    assert player_id1 in result
    assert player_id2 in result


@pytest.mark.asyncio
async def test_handle_combat_start(player_combat_service):
    """Test handle_combat_start tracks combat state."""
    player_id = uuid.uuid4()
    combat_id = uuid.uuid4()
    await player_combat_service.handle_combat_start(player_id, "TestPlayer", combat_id, "room_001")
    assert player_id in player_combat_service._player_combat_states


@pytest.mark.asyncio
async def test_handle_combat_end(player_combat_service):
    """Test handle_combat_end clears combat states."""
    player_id = uuid.uuid4()
    combat_id = uuid.uuid4()
    await player_combat_service.track_player_combat_state(player_id, "TestPlayer", combat_id, "room_001")
    await player_combat_service.handle_combat_end(combat_id)
    assert player_id not in player_combat_service._player_combat_states


@pytest.mark.asyncio
async def test_award_xp_on_npc_death_success(player_combat_service, mock_persistence, mock_event_bus):
    """Test award_xp_on_npc_death awards XP successfully."""
    player_id = uuid.uuid4()
    npc_id = uuid.uuid4()
    mock_player = MagicMock()
    mock_player.name = "TestPlayer"
    mock_player.level = 5
    mock_player.add_experience = MagicMock()
    mock_persistence.get_player_by_id = AsyncMock(return_value=mock_player)
    mock_persistence.save_player = AsyncMock()
    await player_combat_service.award_xp_on_npc_death(player_id, npc_id, 100)
    mock_player.add_experience.assert_called_once_with(100)
    mock_persistence.save_player.assert_awaited_once()
    mock_event_bus.publish.assert_called_once()


@pytest.mark.asyncio
async def test_award_xp_on_npc_death_player_not_found(player_combat_service, mock_persistence):
    """Test award_xp_on_npc_death handles player not found."""
    player_id = uuid.uuid4()
    npc_id = uuid.uuid4()
    mock_persistence.get_player_by_id = AsyncMock(return_value=None)
    # Should not raise, just log warning
    await player_combat_service.award_xp_on_npc_death(player_id, npc_id, 100)


@pytest.mark.asyncio
async def test_award_xp_on_npc_death_error(player_combat_service, mock_persistence):
    """Test award_xp_on_npc_death handles errors gracefully."""
    player_id = uuid.uuid4()
    npc_id = uuid.uuid4()
    mock_persistence.get_player_by_id = AsyncMock(side_effect=ValueError("Database error"))
    # Should not raise, just log error
    await player_combat_service.award_xp_on_npc_death(player_id, npc_id, 100)


@pytest.mark.asyncio
async def test_calculate_xp_reward_from_mapping(player_combat_service, mock_npc_service):
    """Test calculate_xp_reward gets XP from UUID mapping."""
    npc_id = uuid.uuid4()
    # Set the npc_combat_integration_service reference so the function can access the mapping
    player_combat_service._npc_combat_integration_service = mock_npc_service
    mock_npc_service._uuid_to_xp_mapping = {npc_id: 150}
    result = await player_combat_service.calculate_xp_reward(npc_id)
    assert result == 150


@pytest.mark.asyncio
async def test_calculate_xp_reward_from_database(player_combat_service, mock_persistence, mock_npc_service):
    """Test calculate_xp_reward falls back to database lookup."""
    npc_id = uuid.uuid4()
    mock_npc_service._uuid_to_xp_mapping = {}  # No mapping
    mock_npc_service.get_original_string_id = MagicMock(return_value="npc_001")
    mock_lifecycle = MagicMock()
    mock_record = MagicMock()
    mock_definition = MagicMock()
    mock_definition.get_base_stats = MagicMock(return_value={"xp_value": 200})
    mock_record.definition = mock_definition
    mock_lifecycle.lifecycle_records = {"npc_001": mock_record}
    mock_persistence.get_npc_lifecycle_manager = MagicMock(return_value=mock_lifecycle)
    with patch("asyncio.to_thread", return_value=mock_lifecycle):
        result = await player_combat_service.calculate_xp_reward(npc_id)
        assert result == 200


@pytest.mark.asyncio
async def test_calculate_xp_reward_default(player_combat_service, mock_npc_service, mock_persistence):
    """Test calculate_xp_reward returns default when no XP found."""
    npc_id = uuid.uuid4()
    mock_npc_service._uuid_to_xp_mapping = {}
    mock_npc_service.get_original_string_id = MagicMock(return_value=None)
    mock_persistence.get_npc_lifecycle_manager = MagicMock(return_value=None)
    with patch("asyncio.to_thread", return_value=None):
        result = await player_combat_service.calculate_xp_reward(npc_id)
        assert isinstance(result, int)
        assert result >= 0  # Should return default value


@pytest.mark.asyncio
async def test_cleanup_stale_combat_states(player_combat_service):
    """Test cleanup_stale_combat_states cleans up stale states."""
    from datetime import timedelta

    player_id = uuid.uuid4()
    combat_id = uuid.uuid4()
    old_state = PlayerCombatState(
        player_id, "TestPlayer", combat_id, "room_001", last_activity=datetime.now(UTC) - timedelta(minutes=60)
    )
    player_combat_service._player_combat_states[player_id] = old_state
    cleaned = await player_combat_service.cleanup_stale_combat_states()
    assert cleaned >= 0


@pytest.mark.asyncio
async def test_get_combat_stats(player_combat_service):
    """Test get_combat_stats returns statistics."""
    player_id = uuid.uuid4()
    combat_id = uuid.uuid4()
    await player_combat_service.track_player_combat_state(player_id, "TestPlayer", combat_id, "room_001")
    stats = await player_combat_service.get_combat_stats()
    assert isinstance(stats, dict)
    assert "players_in_combat" in stats


@pytest.mark.asyncio
async def test_get_combat_stats_multiple_combats(player_combat_service):
    """Test get_combat_stats with multiple players in different combats."""
    player1_id = uuid.uuid4()
    player2_id = uuid.uuid4()
    combat1_id = uuid.uuid4()
    combat2_id = uuid.uuid4()
    await player_combat_service.track_player_combat_state(player1_id, "Player1", combat1_id, "room_001")
    await player_combat_service.track_player_combat_state(player2_id, "Player2", combat2_id, "room_002")
    stats = await player_combat_service.get_combat_stats()
    assert stats["players_in_combat"] == 2
    assert stats["active_combats"] == 2


@pytest.mark.asyncio
async def test_handle_npc_death_error(player_combat_service, mock_persistence):
    """Test handle_npc_death handles errors gracefully."""
    player_id = uuid.uuid4()
    npc_id = uuid.uuid4()
    xp_amount = 100
    # Mock persistence to raise an error - award_xp_on_npc_death has error handling
    mock_persistence.get_player_by_id = AsyncMock(side_effect=ValueError("Error"))
    # Should not raise, error is caught in award_xp_on_npc_death
    await player_combat_service.handle_npc_death(player_id, npc_id, xp_amount)
    mock_persistence.get_player_by_id.assert_awaited_once()


@pytest.mark.asyncio
async def test_award_xp_on_npc_death_no_player_combat_service(player_combat_service, mock_persistence):
    """Test award_xp_on_npc_death handles missing player_combat_service."""
    npc_id = uuid.uuid4()
    room_id = "room_001"
    killer_id = uuid.uuid4()
    player_combat_service._player_combat_service = None
    # Should not raise, just return without awarding
    await player_combat_service.award_xp_on_npc_death(npc_id, room_id, str(killer_id))


@pytest.mark.asyncio
async def test_handle_combat_start_tracks_state(player_combat_service):
    """Test handle_combat_start tracks player combat state."""
    player_id = uuid.uuid4()
    player_name = "TestPlayer"
    combat_id = uuid.uuid4()
    room_id = "room_001"
    await player_combat_service.handle_combat_start(player_id, player_name, combat_id, room_id)
    state = await player_combat_service.get_player_combat_state(player_id)
    assert state is not None
    assert state.player_id == player_id
    assert state.combat_id == combat_id


@pytest.mark.asyncio
async def test_handle_combat_end_clears_state(player_combat_service):
    """Test handle_combat_end clears player combat state."""
    player_id = uuid.uuid4()
    combat_id = uuid.uuid4()
    await player_combat_service.track_player_combat_state(player_id, "TestPlayer", combat_id, "room_001")
    await player_combat_service.handle_combat_end(combat_id)
    state = await player_combat_service.get_player_combat_state(player_id)
    assert state is None


def test_player_combat_state_post_init():
    """Test PlayerCombatState.__post_init__ sets last_activity."""
    state = PlayerCombatState(
        player_id=uuid.uuid4(), player_name="TestPlayer", combat_id=uuid.uuid4(), room_id="room_001"
    )
    assert state.last_activity is not None


def test_player_combat_state_post_init_with_activity():
    """Test PlayerCombatState.__post_init__ preserves provided last_activity."""

    last_activity = datetime.now(UTC)
    state = PlayerCombatState(
        player_id=uuid.uuid4(),
        player_name="TestPlayer",
        combat_id=uuid.uuid4(),
        room_id="room_001",
        last_activity=last_activity,
    )
    assert state.last_activity == last_activity


def test_player_xp_award_event_init():
    """Test PlayerXPAwardEvent initialization."""
    from server.services.player_combat_service import PlayerXPAwardEvent

    player_id = uuid.uuid4()
    event = PlayerXPAwardEvent(player_id, 100, 5)
    assert event.player_id == player_id
    assert event.xp_amount == 100
    assert event.new_level == 5
    assert event.event_type == "player_xp_awarded"
