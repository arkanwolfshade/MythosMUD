"""
Unit tests for player respawn service.

Tests the PlayerRespawnService for managing player resurrection and limbo state.
"""

import uuid
from datetime import datetime
from unittest.mock import AsyncMock, MagicMock

import pytest
from sqlalchemy.exc import SQLAlchemyError

from server.events.event_types import PlayerDeliriumRespawnedEvent, PlayerRespawnedEvent
from server.exceptions import DatabaseError
from server.models.game import PositionState
from server.models.lucidity import PlayerLucidity
from server.models.player import Player
from server.services.player_respawn_service import (
    DEFAULT_RESPAWN_ROOM,
    LIMBO_ROOM_ID,
    PlayerRespawnService,
    _utc_now,
)


@pytest.fixture
def mock_event_bus():
    """Create a mock event bus."""
    return MagicMock()


@pytest.fixture
def mock_player_combat_service():
    """Create a mock player combat service."""
    service = MagicMock()
    service.clear_player_combat_state = AsyncMock()
    return service


@pytest.fixture
def respawn_service(mock_event_bus, mock_player_combat_service):
    """Create a PlayerRespawnService instance."""
    return PlayerRespawnService(event_bus=mock_event_bus, player_combat_service=mock_player_combat_service)


@pytest.fixture
def respawn_service_no_deps():
    """Create a PlayerRespawnService instance without dependencies."""
    return PlayerRespawnService()


@pytest.fixture
def mock_session():
    """Create a mock async session."""
    session = MagicMock()
    session.get = AsyncMock()
    session.commit = AsyncMock()
    session.rollback = AsyncMock()
    return session


@pytest.fixture
def sample_player():
    """Create a sample player for testing."""
    player = MagicMock(spec=Player)
    player.player_id = uuid.uuid4()
    player.id = player.player_id
    player.name = "TestPlayer"
    player.current_room_id = "earth_arkhamcity_street_room_001"
    player.respawn_room_id = None
    player.get_stats = MagicMock(return_value={"current_dp": 50, "max_dp": 100, "position": PositionState.STANDING})
    player.set_stats = MagicMock()
    return player


def test_utc_now():
    """Test _utc_now returns naive UTC datetime."""
    result = _utc_now()
    assert isinstance(result, datetime)
    assert result.tzinfo is None


def test_respawn_service_initialization(respawn_service, mock_event_bus, mock_player_combat_service):
    """Test PlayerRespawnService initializes correctly."""
    assert respawn_service._event_bus == mock_event_bus
    assert respawn_service._player_combat_service == mock_player_combat_service


def test_respawn_service_initialization_no_deps(respawn_service_no_deps):
    """Test PlayerRespawnService initializes without dependencies."""
    assert respawn_service_no_deps._event_bus is None
    assert respawn_service_no_deps._player_combat_service is None


@pytest.mark.asyncio
async def test_move_player_to_limbo_success(respawn_service, mock_session, sample_player):
    """Test moving player to limbo successfully."""
    mock_session.get.return_value = sample_player

    result = await respawn_service.move_player_to_limbo(sample_player.player_id, "death_room", mock_session)

    assert result is True
    assert sample_player.current_room_id == LIMBO_ROOM_ID
    mock_session.get.assert_awaited_once_with(Player, sample_player.player_id)
    mock_session.commit.assert_awaited_once()


@pytest.mark.asyncio
async def test_move_player_to_limbo_player_not_found(respawn_service, mock_session):
    """Test moving player to limbo when player not found."""
    mock_session.get.return_value = None
    player_id = uuid.uuid4()

    result = await respawn_service.move_player_to_limbo(player_id, "death_room", mock_session)

    assert result is False
    mock_session.get.assert_awaited_once_with(Player, player_id)
    mock_session.commit.assert_not_awaited()


@pytest.mark.asyncio
async def test_move_player_to_limbo_database_error(respawn_service, mock_session, sample_player):
    """Test moving player to limbo with database error."""
    mock_session.get.return_value = sample_player
    mock_session.commit.side_effect = DatabaseError("Database error")

    result = await respawn_service.move_player_to_limbo(sample_player.player_id, "death_room", mock_session)

    assert result is False
    mock_session.rollback.assert_awaited_once()


@pytest.mark.asyncio
async def test_move_player_to_limbo_sqlalchemy_error(respawn_service, mock_session, sample_player):
    """Test moving player to limbo with SQLAlchemy error."""
    mock_session.get.return_value = sample_player
    mock_session.commit.side_effect = SQLAlchemyError("SQL error", None, None)

    result = await respawn_service.move_player_to_limbo(sample_player.player_id, "death_room", mock_session)

    assert result is False
    mock_session.rollback.assert_awaited_once()


@pytest.mark.asyncio
async def test_get_respawn_room_custom(respawn_service, mock_session, sample_player):
    """Test getting custom respawn room."""
    sample_player.respawn_room_id = "custom_respawn_room"
    mock_session.get.return_value = sample_player

    result = await respawn_service.get_respawn_room(sample_player.player_id, mock_session)

    assert result == "custom_respawn_room"
    mock_session.get.assert_awaited_once_with(Player, sample_player.player_id)


@pytest.mark.asyncio
async def test_get_respawn_room_default(respawn_service, mock_session, sample_player):
    """Test getting default respawn room when custom not set."""
    sample_player.respawn_room_id = None
    mock_session.get.return_value = sample_player

    result = await respawn_service.get_respawn_room(sample_player.player_id, mock_session)

    assert result == DEFAULT_RESPAWN_ROOM
    mock_session.get.assert_awaited_once_with(Player, sample_player.player_id)


@pytest.mark.asyncio
async def test_get_respawn_room_player_not_found(respawn_service, mock_session):
    """Test getting respawn room when player not found."""
    mock_session.get.return_value = None
    player_id = uuid.uuid4()

    result = await respawn_service.get_respawn_room(player_id, mock_session)

    assert result == DEFAULT_RESPAWN_ROOM
    mock_session.get.assert_awaited_once_with(Player, player_id)


@pytest.mark.asyncio
async def test_get_respawn_room_database_error(respawn_service, mock_session):
    """Test getting respawn room with database error."""
    mock_session.get.side_effect = DatabaseError("Database error")
    player_id = uuid.uuid4()

    result = await respawn_service.get_respawn_room(player_id, mock_session)

    assert result == DEFAULT_RESPAWN_ROOM


@pytest.mark.asyncio
async def test_respawn_player_success(respawn_service, mock_session, sample_player, mock_event_bus):
    """Test respawning player successfully."""
    sample_player.current_room_id = LIMBO_ROOM_ID
    sample_player.get_stats.return_value = {"current_dp": 0, "max_dp": 100, "position": PositionState.LYING}
    mock_session.get.side_effect = [sample_player, sample_player]  # First for respawn, second for get_respawn_room

    result = await respawn_service.respawn_player(sample_player.player_id, mock_session)

    assert result is True
    assert sample_player.current_room_id == DEFAULT_RESPAWN_ROOM
    sample_player.set_stats.assert_called_once()
    stats = sample_player.set_stats.call_args[0][0]
    assert stats["current_dp"] == 100
    assert stats["position"] == PositionState.STANDING
    mock_session.commit.assert_awaited_once()
    mock_event_bus.publish.assert_called_once()
    published_event = mock_event_bus.publish.call_args[0][0]
    assert isinstance(published_event, PlayerRespawnedEvent)
    assert published_event.player_id == sample_player.player_id


@pytest.mark.asyncio
async def test_respawn_player_with_custom_respawn_room(respawn_service, mock_session, sample_player):
    """Test respawning player with custom respawn room."""
    sample_player.current_room_id = LIMBO_ROOM_ID
    sample_player.respawn_room_id = "custom_respawn_room"
    sample_player.get_stats.return_value = {"current_dp": 0, "max_dp": 100, "position": PositionState.LYING}
    mock_session.get.side_effect = [sample_player, sample_player]

    result = await respawn_service.respawn_player(sample_player.player_id, mock_session)

    assert result is True
    assert sample_player.current_room_id == "custom_respawn_room"


@pytest.mark.asyncio
async def test_respawn_player_clears_combat_state(
    respawn_service, mock_session, sample_player, mock_player_combat_service
):
    """Test respawning player clears combat state."""
    sample_player.current_room_id = LIMBO_ROOM_ID
    sample_player.get_stats.return_value = {"current_dp": 0, "max_dp": 100, "position": PositionState.LYING}
    mock_session.get.side_effect = [sample_player, sample_player]

    result = await respawn_service.respawn_player(sample_player.player_id, mock_session)

    assert result is True
    mock_player_combat_service.clear_player_combat_state.assert_awaited_once_with(sample_player.player_id)


@pytest.mark.asyncio
async def test_respawn_player_no_combat_service(respawn_service_no_deps, mock_session, sample_player):
    """Test respawning player without combat service."""
    sample_player.current_room_id = LIMBO_ROOM_ID
    sample_player.get_stats.return_value = {"current_dp": 0, "max_dp": 100, "position": PositionState.LYING}
    mock_session.get.side_effect = [sample_player, sample_player]

    result = await respawn_service_no_deps.respawn_player(sample_player.player_id, mock_session)

    assert result is True
    mock_session.commit.assert_awaited_once()


@pytest.mark.asyncio
async def test_respawn_player_combat_clear_error(
    respawn_service, mock_session, sample_player, mock_player_combat_service
):
    """Test respawning player when combat clear fails."""
    sample_player.current_room_id = LIMBO_ROOM_ID
    sample_player.get_stats.return_value = {"current_dp": 0, "max_dp": 100, "position": PositionState.LYING}
    mock_session.get.side_effect = [sample_player, sample_player]
    mock_player_combat_service.clear_player_combat_state.side_effect = DatabaseError("Combat clear error")

    result = await respawn_service.respawn_player(sample_player.player_id, mock_session)

    assert result is True  # Respawn should still succeed even if combat clear fails
    mock_session.commit.assert_awaited_once()


@pytest.mark.asyncio
async def test_respawn_player_not_found(respawn_service, mock_session):
    """Test respawning player when player not found."""
    mock_session.get.return_value = None
    player_id = uuid.uuid4()

    result = await respawn_service.respawn_player(player_id, mock_session)

    assert result is False
    mock_session.commit.assert_not_awaited()


@pytest.mark.asyncio
async def test_respawn_player_database_error(respawn_service, mock_session, sample_player):
    """Test respawning player with database error."""
    mock_session.get.return_value = sample_player
    mock_session.commit.side_effect = DatabaseError("Database error")

    result = await respawn_service.respawn_player(sample_player.player_id, mock_session)

    assert result is False
    mock_session.rollback.assert_awaited_once()


@pytest.mark.asyncio
async def test_respawn_player_from_delirium_success(respawn_service, mock_session, sample_player, mock_event_bus):
    """Test respawning player from delirium successfully."""
    sample_player.current_room_id = LIMBO_ROOM_ID
    sample_player.get_stats.return_value = {"position": PositionState.LYING}
    lucidity_record = MagicMock(spec=PlayerLucidity)
    lucidity_record.current_lcd = 0
    lucidity_record.current_tier = "delirious"
    mock_session.get.side_effect = [sample_player, lucidity_record]

    result = await respawn_service.respawn_player_from_delirium(sample_player.player_id, mock_session)

    assert result is True
    assert lucidity_record.current_lcd == 10
    assert lucidity_record.current_tier == "lucid"
    assert sample_player.current_room_id == DEFAULT_RESPAWN_ROOM
    sample_player.set_stats.assert_called_once()
    stats = sample_player.set_stats.call_args[0][0]
    assert stats["position"] == PositionState.STANDING
    mock_session.commit.assert_awaited_once()
    mock_event_bus.publish.assert_called_once()
    published_event = mock_event_bus.publish.call_args[0][0]
    assert isinstance(published_event, PlayerDeliriumRespawnedEvent)
    assert published_event.player_id == sample_player.player_id


@pytest.mark.asyncio
async def test_respawn_player_from_delirium_clears_combat_state(
    respawn_service, mock_session, sample_player, mock_player_combat_service
):
    """Test respawning player from delirium clears combat state."""
    sample_player.current_room_id = LIMBO_ROOM_ID
    sample_player.get_stats.return_value = {"position": PositionState.LYING}
    lucidity_record = MagicMock(spec=PlayerLucidity)
    lucidity_record.current_lcd = 0
    lucidity_record.current_tier = "delirious"
    mock_session.get.side_effect = [sample_player, lucidity_record]

    result = await respawn_service.respawn_player_from_delirium(sample_player.player_id, mock_session)

    assert result is True
    mock_player_combat_service.clear_player_combat_state.assert_awaited_once_with(sample_player.player_id)


@pytest.mark.asyncio
async def test_respawn_player_from_delirium_no_combat_service(respawn_service_no_deps, mock_session, sample_player):
    """Test respawning player from delirium without combat service."""
    sample_player.current_room_id = LIMBO_ROOM_ID
    sample_player.get_stats.return_value = {"position": PositionState.LYING}
    lucidity_record = MagicMock(spec=PlayerLucidity)
    lucidity_record.current_lcd = 0
    lucidity_record.current_tier = "delirious"
    mock_session.get.side_effect = [sample_player, lucidity_record]

    result = await respawn_service_no_deps.respawn_player_from_delirium(sample_player.player_id, mock_session)

    assert result is True
    mock_session.commit.assert_awaited_once()


@pytest.mark.asyncio
async def test_respawn_player_from_delirium_player_not_found(respawn_service, mock_session):
    """Test respawning player from delirium when player not found."""
    mock_session.get.return_value = None
    player_id = uuid.uuid4()

    result = await respawn_service.respawn_player_from_delirium(player_id, mock_session)

    assert result is False
    mock_session.commit.assert_not_awaited()


@pytest.mark.asyncio
async def test_respawn_player_from_delirium_lucidity_not_found(respawn_service, mock_session, sample_player):
    """Test respawning player from delirium when lucidity record not found."""
    mock_session.get.side_effect = [sample_player, None]
    player_id = sample_player.player_id

    result = await respawn_service.respawn_player_from_delirium(player_id, mock_session)

    assert result is False
    mock_session.commit.assert_not_awaited()


@pytest.mark.asyncio
async def test_respawn_player_from_delirium_database_error(respawn_service, mock_session, sample_player):
    """Test respawning player from delirium with database error."""
    sample_player.get_stats.return_value = {"position": PositionState.LYING}
    lucidity_record = MagicMock(spec=PlayerLucidity)
    lucidity_record.current_lcd = 0
    mock_session.get.side_effect = [sample_player, lucidity_record]
    mock_session.commit.side_effect = DatabaseError("Database error")

    result = await respawn_service.respawn_player_from_delirium(sample_player.player_id, mock_session)

    assert result is False
    mock_session.rollback.assert_awaited_once()


@pytest.mark.asyncio
async def test_respawn_player_from_delirium_combat_clear_error(
    respawn_service, mock_session, sample_player, mock_player_combat_service
):
    """Test respawning player from delirium when combat clear fails."""
    sample_player.current_room_id = LIMBO_ROOM_ID
    sample_player.get_stats.return_value = {"position": PositionState.LYING}
    lucidity_record = MagicMock(spec=PlayerLucidity)
    lucidity_record.current_lcd = 0
    lucidity_record.current_tier = "delirious"
    mock_session.get.side_effect = [sample_player, lucidity_record]
    mock_player_combat_service.clear_player_combat_state.side_effect = DatabaseError("Combat clear error")

    result = await respawn_service.respawn_player_from_delirium(sample_player.player_id, mock_session)

    assert result is True  # Respawn should still succeed even if combat clear fails
    mock_session.commit.assert_awaited_once()
