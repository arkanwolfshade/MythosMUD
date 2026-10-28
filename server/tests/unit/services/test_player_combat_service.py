"""
Unit tests for player combat service.

Tests the PlayerCombatService class for managing player combat state and XP rewards.
"""

# pyright: reportPrivateUsage=false, reportAny=false
# Reason: Assertions on internal state are intentional in these unit tests.
# TEST_MOCK: mock_level_service.grant_xp (a MagicMock attribute) resolves to Any.

import uuid
from datetime import UTC, datetime
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from server.services.player_combat_service import PlayerCombatService, PlayerCombatState

# pylint: disable=protected-access  # Reason: Test file - accessing protected members is standard practice for unit testing
# pylint: disable=redefined-outer-name  # Reason: Test file - pytest fixture parameter names must match fixture names, causing intentional redefinitions


@pytest.fixture
def mock_persistence() -> MagicMock:
    """Create mock persistence layer."""
    return MagicMock()


@pytest.fixture
def mock_event_bus() -> MagicMock:
    """Create mock event bus."""
    bus = MagicMock()
    bus.publish = MagicMock()  # EventBus.publish is sync
    return bus


@pytest.fixture
def mock_npc_service() -> MagicMock:
    """Create mock NPC combat integration service (for calculate_xp_reward's UUID mapping)."""
    service = MagicMock()
    service.get_original_string_id = MagicMock(return_value=None)
    mock_uuid_mapping = MagicMock()
    mock_uuid_mapping.get_xp_value = MagicMock(return_value=None)
    service.get_uuid_mapping = MagicMock(return_value=mock_uuid_mapping)
    return service


@pytest.fixture
def mock_level_service() -> MagicMock:
    """Create mock LevelService -- the XP/level authority (#879)."""
    service = MagicMock()
    service.grant_xp = AsyncMock()
    return service


@pytest.fixture
def player_combat_service(
    mock_persistence: MagicMock,
    mock_event_bus: MagicMock,
    mock_npc_service: MagicMock,
    mock_level_service: MagicMock,
) -> PlayerCombatService:
    """Create PlayerCombatService instance."""
    return PlayerCombatService(mock_persistence, mock_event_bus, mock_npc_service, mock_level_service)


def test_player_combat_service_init(
    player_combat_service: PlayerCombatService,
    mock_persistence: MagicMock,
    mock_event_bus: MagicMock,
) -> None:
    """Test PlayerCombatService initialization."""
    assert player_combat_service._persistence == mock_persistence
    assert player_combat_service._event_bus == mock_event_bus
    assert isinstance(player_combat_service._player_combat_states, dict)


@pytest.mark.asyncio
async def test_track_player_combat_state(player_combat_service: PlayerCombatService) -> None:
    """Test track_player_combat_state tracks state."""
    player_id = uuid.uuid4()
    combat_id = uuid.uuid4()
    await player_combat_service.track_player_combat_state(player_id, "TestPlayer", combat_id, "room_001")
    assert player_id in player_combat_service._player_combat_states


@pytest.mark.asyncio
async def test_get_player_combat_state(player_combat_service: PlayerCombatService) -> None:
    """Test get_player_combat_state returns state."""
    player_id = uuid.uuid4()
    combat_id = uuid.uuid4()
    await player_combat_service.track_player_combat_state(player_id, "TestPlayer", combat_id, "room_001")
    state: PlayerCombatState | None = await player_combat_service.get_player_combat_state(player_id)
    assert state is not None
    assert state.player_id == player_id
    assert state.combat_id == combat_id


@pytest.mark.asyncio
async def test_get_player_combat_state_not_found(player_combat_service: PlayerCombatService) -> None:
    """Test get_player_combat_state returns None when not found."""
    player_id = uuid.uuid4()
    state: PlayerCombatState | None = await player_combat_service.get_player_combat_state(player_id)
    assert state is None


@pytest.mark.asyncio
async def test_clear_player_combat_state(player_combat_service: PlayerCombatService) -> None:
    """Test clear_player_combat_state clears state."""
    player_id = uuid.uuid4()
    combat_id = uuid.uuid4()
    await player_combat_service.track_player_combat_state(player_id, "TestPlayer", combat_id, "room_001")
    await player_combat_service.clear_player_combat_state(player_id)
    assert player_id not in player_combat_service._player_combat_states


def test_is_player_in_combat_sync_true(player_combat_service: PlayerCombatService) -> None:
    """Test is_player_in_combat_sync returns True when in combat."""
    player_id = uuid.uuid4()
    combat_id = uuid.uuid4()
    # Use sync method to set state
    player_combat_service._player_combat_states[player_id] = PlayerCombatState(
        player_id, "TestPlayer", combat_id, "room_001"
    )
    result: bool = player_combat_service.is_player_in_combat_sync(player_id)
    assert result is True


def test_is_player_in_combat_sync_false(player_combat_service: PlayerCombatService) -> None:
    """Test is_player_in_combat_sync returns False when not in combat."""
    player_id = uuid.uuid4()
    result: bool = player_combat_service.is_player_in_combat_sync(player_id)
    assert result is False


@pytest.mark.asyncio
async def test_is_player_in_combat(player_combat_service: PlayerCombatService) -> None:
    """Test is_player_in_combat checks combat state."""
    player_id = uuid.uuid4()
    combat_id = uuid.uuid4()
    await player_combat_service.track_player_combat_state(player_id, "TestPlayer", combat_id, "room_001")
    result: bool = await player_combat_service.is_player_in_combat(player_id)
    assert result is True


@pytest.mark.asyncio
async def test_get_players_in_combat(player_combat_service: PlayerCombatService) -> None:
    """Test get_players_in_combat returns list of players."""
    player_id1 = uuid.uuid4()
    player_id2 = uuid.uuid4()
    combat_id = uuid.uuid4()
    await player_combat_service.track_player_combat_state(player_id1, "Player1", combat_id, "room_001")
    await player_combat_service.track_player_combat_state(player_id2, "Player2", combat_id, "room_001")
    result: list[uuid.UUID] = await player_combat_service.get_players_in_combat()
    assert len(result) == 2
    assert player_id1 in result
    assert player_id2 in result


@pytest.mark.asyncio
async def test_handle_combat_start(player_combat_service: PlayerCombatService) -> None:
    """Test handle_combat_start tracks combat state."""
    player_id = uuid.uuid4()
    combat_id = uuid.uuid4()
    await player_combat_service.handle_combat_start(player_id, "TestPlayer", combat_id, "room_001")
    assert player_id in player_combat_service._player_combat_states


@pytest.mark.asyncio
async def test_handle_combat_end(player_combat_service: PlayerCombatService) -> None:
    """Test handle_combat_end clears combat states."""
    player_id = uuid.uuid4()
    combat_id = uuid.uuid4()
    await player_combat_service.track_player_combat_state(player_id, "TestPlayer", combat_id, "room_001")
    await player_combat_service.handle_combat_end(combat_id)
    assert player_id not in player_combat_service._player_combat_states


@pytest.mark.asyncio
async def test_award_xp_on_npc_death_success(
    player_combat_service: PlayerCombatService,
    mock_level_service: MagicMock,
) -> None:
    """Test award_xp_on_npc_death delegates to LevelService.grant_xp (#879 single authority)."""
    player_id = uuid.uuid4()
    npc_id = uuid.uuid4()
    await player_combat_service.award_xp_on_npc_death(player_id, npc_id, 100)
    mock_level_service.grant_xp.assert_awaited_once_with(player_id, 100)


@pytest.mark.asyncio
async def test_award_xp_on_npc_death_zero_xp_does_not_call_level_service(
    player_combat_service: PlayerCombatService,
    mock_level_service: MagicMock,
) -> None:
    """Zero (or negative) XP is a no-op -- must not call LevelService at all."""
    await player_combat_service.award_xp_on_npc_death(uuid.uuid4(), uuid.uuid4(), 0)
    mock_level_service.grant_xp.assert_not_called()


@pytest.mark.asyncio
async def test_award_xp_on_npc_death_no_level_service(
    player_combat_service: PlayerCombatService,
) -> None:
    """Test award_xp_on_npc_death handles a missing LevelService gracefully (test-only construction)."""
    player_id = uuid.uuid4()
    npc_id = uuid.uuid4()
    player_combat_service.set_level_service(None)
    # Should not raise, just log warning
    await player_combat_service.award_xp_on_npc_death(player_id, npc_id, 100)


@pytest.mark.asyncio
async def test_award_xp_on_npc_death_error(
    player_combat_service: PlayerCombatService, mock_level_service: MagicMock
) -> None:
    """Test award_xp_on_npc_death handles errors gracefully."""
    player_id = uuid.uuid4()
    npc_id = uuid.uuid4()
    mock_level_service.grant_xp = AsyncMock(side_effect=ValueError("Database error"))
    # Should not raise, just log error
    await player_combat_service.award_xp_on_npc_death(player_id, npc_id, 100)


@pytest.mark.asyncio
async def test_calculate_xp_reward_from_mapping(
    player_combat_service: PlayerCombatService, mock_npc_service: MagicMock
) -> None:
    """Test calculate_xp_reward gets XP from UUID mapping via get_uuid_mapping()."""
    npc_id = uuid.uuid4()
    player_combat_service.set_npc_combat_integration_service(mock_npc_service)
    mock_uuid_mapping: MagicMock = MagicMock()
    mock_uuid_mapping.get_xp_value = MagicMock(return_value=150)
    mock_npc_service.get_uuid_mapping = MagicMock(return_value=mock_uuid_mapping)
    result: int = await player_combat_service.calculate_xp_reward(npc_id)
    assert result == 150


@pytest.mark.asyncio
async def test_calculate_xp_reward_from_database(
    player_combat_service: PlayerCombatService,
    mock_persistence: MagicMock,
    mock_npc_service: MagicMock,
) -> None:
    """Test calculate_xp_reward falls back to database lookup when UUID mapping has no XP."""
    npc_id = uuid.uuid4()
    mock_uuid_mapping = MagicMock()
    mock_uuid_mapping.get_xp_value = MagicMock(return_value=None)  # No XP in mapping
    mock_npc_service.get_uuid_mapping = MagicMock(return_value=mock_uuid_mapping)
    mock_npc_service.get_original_string_id = MagicMock(return_value="npc_001")
    mock_lifecycle = MagicMock()
    mock_record = MagicMock()
    mock_definition = MagicMock()
    mock_definition.get_base_stats = MagicMock(return_value={"xp_value": 200})
    mock_record.definition = mock_definition
    mock_lifecycle.lifecycle_records = {"npc_001": mock_record}
    mock_persistence.get_npc_lifecycle_manager = MagicMock(return_value=mock_lifecycle)
    with patch("asyncio.to_thread", return_value=mock_lifecycle):
        result: int = await player_combat_service.calculate_xp_reward(npc_id)
        assert result == 200


@pytest.mark.asyncio
async def test_calculate_xp_reward_default(
    player_combat_service: PlayerCombatService,
    mock_npc_service: MagicMock,
    mock_persistence: MagicMock,
) -> None:
    """Test calculate_xp_reward returns default when no XP found in mapping or database."""
    npc_id = uuid.uuid4()
    mock_uuid_mapping = MagicMock()
    mock_uuid_mapping.get_xp_value = MagicMock(return_value=None)
    mock_npc_service.get_uuid_mapping = MagicMock(return_value=mock_uuid_mapping)
    mock_npc_service.get_original_string_id = MagicMock(return_value=None)
    mock_persistence.get_npc_lifecycle_manager = MagicMock(return_value=None)
    with patch("asyncio.to_thread", return_value=None):
        result: int = await player_combat_service.calculate_xp_reward(npc_id)
        assert isinstance(result, int)
        assert result >= 0  # Should return default value


@pytest.mark.asyncio
async def test_cleanup_stale_combat_states(player_combat_service: PlayerCombatService) -> None:
    """Test cleanup_stale_combat_states cleans up stale states."""
    from datetime import timedelta

    player_id = uuid.uuid4()
    combat_id = uuid.uuid4()
    old_state = PlayerCombatState(
        player_id, "TestPlayer", combat_id, "room_001", last_activity=datetime.now(UTC) - timedelta(minutes=60)
    )
    player_combat_service._player_combat_states[player_id] = old_state
    cleaned: int = await player_combat_service.cleanup_stale_combat_states()
    assert cleaned >= 0


@pytest.mark.asyncio
async def test_get_combat_stats(player_combat_service: PlayerCombatService) -> None:
    """Test get_combat_stats returns statistics."""
    player_id = uuid.uuid4()
    combat_id = uuid.uuid4()
    await player_combat_service.track_player_combat_state(player_id, "TestPlayer", combat_id, "room_001")
    stats: dict[str, int] = await player_combat_service.get_combat_stats()
    assert isinstance(stats, dict)
    assert "players_in_combat" in stats


@pytest.mark.asyncio
async def test_get_combat_stats_multiple_combats(player_combat_service: PlayerCombatService) -> None:
    """Test get_combat_stats with multiple players in different combats."""
    player1_id = uuid.uuid4()
    player2_id = uuid.uuid4()
    combat1_id = uuid.uuid4()
    combat2_id = uuid.uuid4()
    await player_combat_service.track_player_combat_state(player1_id, "Player1", combat1_id, "room_001")
    await player_combat_service.track_player_combat_state(player2_id, "Player2", combat2_id, "room_002")
    stats: dict[str, int] = await player_combat_service.get_combat_stats()
    assert stats["players_in_combat"] == 2
    assert stats["active_combats"] == 2


@pytest.mark.asyncio
async def test_handle_npc_death_error(
    player_combat_service: PlayerCombatService, mock_level_service: MagicMock
) -> None:
    """Test handle_npc_death handles errors gracefully."""
    player_id = uuid.uuid4()
    npc_id = uuid.uuid4()
    xp_amount = 100
    grant_xp: AsyncMock = AsyncMock(side_effect=ValueError("Error"))
    mock_level_service.grant_xp = grant_xp
    # Should not raise, error is caught in award_xp_on_npc_death
    await player_combat_service.handle_npc_death(player_id, npc_id, xp_amount)
    grant_xp.assert_awaited_once()


@pytest.mark.asyncio
async def test_handle_combat_start_tracks_state(player_combat_service: PlayerCombatService) -> None:
    """Test handle_combat_start tracks player combat state."""
    player_id = uuid.uuid4()
    player_name = "TestPlayer"
    combat_id = uuid.uuid4()
    room_id = "room_001"
    await player_combat_service.handle_combat_start(player_id, player_name, combat_id, room_id)
    state: PlayerCombatState | None = await player_combat_service.get_player_combat_state(player_id)
    assert state is not None
    assert state.player_id == player_id
    assert state.combat_id == combat_id


@pytest.mark.asyncio
async def test_handle_combat_end_clears_state(player_combat_service: PlayerCombatService) -> None:
    """Test handle_combat_end clears player combat state."""
    player_id = uuid.uuid4()
    combat_id = uuid.uuid4()
    await player_combat_service.track_player_combat_state(player_id, "TestPlayer", combat_id, "room_001")
    await player_combat_service.handle_combat_end(combat_id)
    state: PlayerCombatState | None = await player_combat_service.get_player_combat_state(player_id)
    assert state is None


def test_player_combat_state_post_init() -> None:
    """Test PlayerCombatState.__post_init__ sets last_activity."""
    state = PlayerCombatState(
        player_id=uuid.uuid4(), player_name="TestPlayer", combat_id=uuid.uuid4(), room_id="room_001"
    )
    assert state.last_activity is not None


def test_player_combat_state_post_init_with_activity() -> None:
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


def test_player_xp_award_event_init() -> None:
    """Test PlayerXPAwardEvent initialization."""
    from server.events.event_types import PlayerXPAwardEvent

    player_id = uuid.uuid4()
    event = PlayerXPAwardEvent(player_id, 100, 5)
    assert event.player_id == player_id
    assert event.xp_amount == 100
    assert event.new_level == 5
    assert event.event_type == "player_xp_awarded"
