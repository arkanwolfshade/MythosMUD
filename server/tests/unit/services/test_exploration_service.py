"""
Unit tests for exploration service.

Tests the ExplorationService for tracking player room exploration.
"""

import uuid
from unittest.mock import AsyncMock, MagicMock, patch
from uuid import UUID

import pytest
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.engine import Result

from server.exceptions import DatabaseError
from server.services.exploration_service import ExplorationService


@pytest.fixture
def mock_database_manager():
    """Create a mock database manager."""
    manager = MagicMock()
    session_maker = MagicMock()
    manager.get_session_maker.return_value = session_maker
    return manager


@pytest.fixture
def exploration_service(mock_database_manager):
    """Create an ExplorationService instance."""
    return ExplorationService(database_manager=mock_database_manager)


@pytest.fixture
def mock_session():
    """Create a mock async session."""
    session = MagicMock()
    session.execute = AsyncMock()
    session.commit = AsyncMock()
    session.rollback = AsyncMock()
    return session


@pytest.fixture
def sample_player_id():
    """Create a sample player ID."""
    return uuid.uuid4()


@pytest.fixture
def sample_room_id():
    """Create a sample room ID."""
    return "earth_arkhamcity_street_room_001"


@pytest.fixture
def sample_room_uuid():
    """Create a sample room UUID."""
    return uuid.uuid4()


def test_exploration_service_initialization(exploration_service, mock_database_manager):
    """Test ExplorationService initializes correctly."""
    assert exploration_service._database_manager == mock_database_manager


def test_exploration_service_initialization_default():
    """Test ExplorationService initializes with default database manager."""
    with patch("server.database.DatabaseManager") as mock_db_class:
        mock_instance = MagicMock()
        mock_db_class.get_instance.return_value = mock_instance
        service = ExplorationService()
        # The service should use the instance from get_instance()
        assert service._database_manager == mock_instance


@pytest.mark.asyncio
async def test_get_room_uuid_by_stable_id_success(exploration_service, mock_session, sample_room_uuid):
    """Test getting room UUID by stable_id successfully."""
    result_mock = MagicMock(spec=Result)
    result_mock.scalar_one_or_none = MagicMock(return_value=sample_room_uuid)
    mock_session.execute.return_value = result_mock

    result = await exploration_service._get_room_uuid_by_stable_id("room_001", mock_session)
    assert result == sample_room_uuid


@pytest.mark.asyncio
async def test_get_room_uuid_by_stable_id_not_found(exploration_service, mock_session):
    """Test getting room UUID when room not found."""
    result_mock = MagicMock(spec=Result)
    result_mock.scalar_one_or_none = MagicMock(return_value=None)
    mock_session.execute.return_value = result_mock

    result = await exploration_service._get_room_uuid_by_stable_id("nonexistent_room", mock_session)
    assert result is None


@pytest.mark.asyncio
async def test_get_room_uuid_by_stable_id_string_uuid(exploration_service, mock_session, sample_room_uuid):
    """Test getting room UUID when database returns string UUID."""
    result_mock = MagicMock(spec=Result)
    result_mock.scalar_one_or_none = MagicMock(return_value=str(sample_room_uuid))
    mock_session.execute.return_value = result_mock

    result = await exploration_service._get_room_uuid_by_stable_id("room_001", mock_session)
    assert result == sample_room_uuid


@pytest.mark.asyncio
async def test_get_room_uuid_by_stable_id_with_new_session(exploration_service, mock_database_manager, sample_room_uuid):
    """Test getting room UUID with new session."""
    mock_session = MagicMock()
    mock_session.execute = AsyncMock()
    mock_session.__aenter__ = AsyncMock(return_value=mock_session)
    mock_session.__aexit__ = AsyncMock(return_value=None)

    result_mock = MagicMock(spec=Result)
    result_mock.scalar_one_or_none = MagicMock(return_value=sample_room_uuid)
    mock_session.execute.return_value = result_mock

    session_maker = MagicMock()
    session_maker.return_value = mock_session
    mock_database_manager.get_session_maker.return_value = session_maker

    result = await exploration_service._get_room_uuid_by_stable_id("room_001", None)
    assert result == sample_room_uuid


@pytest.mark.asyncio
async def test_mark_explored_in_session_success(exploration_service, mock_session, sample_player_id, sample_room_uuid):
    """Test marking room as explored in session successfully."""
    result_mock = MagicMock(spec=Result)
    result_mock.rowcount = 0  # No existing record
    mock_session.execute.return_value = result_mock

    result = await exploration_service._mark_explored_in_session(mock_session, sample_player_id, sample_room_uuid)
    assert result is True
    mock_session.execute.assert_awaited()


@pytest.mark.asyncio
async def test_mark_explored_in_session_already_explored(exploration_service, mock_session, sample_player_id, sample_room_uuid):
    """Test marking room as explored when already explored."""
    result_mock = MagicMock(spec=Result)
    result_mock.rowcount = 1  # Record already exists
    mock_session.execute.return_value = result_mock

    result = await exploration_service._mark_explored_in_session(mock_session, sample_player_id, sample_room_uuid)
    assert result is True  # Should still return True (idempotent)


@pytest.mark.asyncio
async def test_mark_room_as_explored_success(exploration_service, mock_session, sample_player_id, sample_room_id, sample_room_uuid):
    """Test marking room as explored successfully."""
    # Mock _get_room_uuid_by_stable_id
    with patch.object(exploration_service, "_get_room_uuid_by_stable_id", return_value=sample_room_uuid):
        with patch.object(exploration_service, "_mark_explored_in_session", return_value=True):
            result = await exploration_service.mark_room_as_explored(sample_player_id, sample_room_id, mock_session)
            assert result is True


@pytest.mark.asyncio
async def test_mark_room_as_explored_room_not_found(exploration_service, mock_session, sample_player_id, sample_room_id):
    """Test marking room as explored when room not found."""
    with patch.object(exploration_service, "_get_room_uuid_by_stable_id", return_value=None):
        result = await exploration_service.mark_room_as_explored(sample_player_id, sample_room_id, mock_session)
        assert result is False


@pytest.mark.asyncio
async def test_mark_room_as_explored_with_new_session(exploration_service, mock_database_manager, sample_player_id, sample_room_id, sample_room_uuid):
    """Test marking room as explored with new session."""
    mock_session = MagicMock()
    mock_session.execute = AsyncMock()
    mock_session.commit = AsyncMock()
    mock_session.__aenter__ = AsyncMock(return_value=mock_session)
    mock_session.__aexit__ = AsyncMock(return_value=None)

    session_maker = MagicMock()
    session_maker.return_value = mock_session
    mock_database_manager.get_session_maker.return_value = session_maker

    with patch.object(exploration_service, "_get_room_uuid_by_stable_id", return_value=sample_room_uuid):
        with patch.object(exploration_service, "_mark_explored_in_session", return_value=True):
            result = await exploration_service.mark_room_as_explored(sample_player_id, sample_room_id, None)
            assert result is True
            mock_session.commit.assert_awaited_once()


@pytest.mark.asyncio
async def test_mark_room_as_explored_database_error(exploration_service, mock_session, sample_player_id, sample_room_id):
    """Test marking room as explored with database error."""
    with patch.object(exploration_service, "_get_room_uuid_by_stable_id", side_effect=SQLAlchemyError("DB error", None, None)):
        with pytest.raises(DatabaseError):
            await exploration_service.mark_room_as_explored(sample_player_id, sample_room_id, mock_session)


@pytest.mark.asyncio
async def test_get_explored_rooms_success(exploration_service, mock_session, sample_player_id, sample_room_uuid):
    """Test getting explored rooms successfully."""
    result_mock = MagicMock(spec=Result)
    result_mock.fetchall = MagicMock(return_value=[(sample_room_uuid,)])
    mock_session.execute.return_value = result_mock

    result = await exploration_service.get_explored_rooms(sample_player_id, mock_session)
    assert len(result) == 1
    assert result[0] == str(sample_room_uuid)


@pytest.mark.asyncio
async def test_get_explored_rooms_empty(exploration_service, mock_session, sample_player_id):
    """Test getting explored rooms when none explored."""
    result_mock = MagicMock(spec=Result)
    result_mock.fetchall = MagicMock(return_value=[])
    mock_session.execute.return_value = result_mock

    result = await exploration_service.get_explored_rooms(sample_player_id, mock_session)
    assert result == []


@pytest.mark.asyncio
async def test_get_explored_rooms_with_session(exploration_service, mock_session, sample_player_id):
    """Test getting explored rooms with session."""
    result_mock = MagicMock(spec=Result)
    result_mock.fetchall = MagicMock(return_value=[])
    mock_session.execute.return_value = result_mock

    result = await exploration_service.get_explored_rooms(sample_player_id, mock_session)
    assert result == []


@pytest.mark.asyncio
async def test_get_explored_rooms_database_error(exploration_service, mock_session, sample_player_id):
    """Test getting explored rooms with database error."""
    mock_session.execute.side_effect = SQLAlchemyError("DB error", None, None)

    with pytest.raises(DatabaseError):
        await exploration_service.get_explored_rooms(sample_player_id, mock_session)


@pytest.mark.asyncio
async def test_is_room_explored_true(exploration_service, mock_session, sample_player_id, sample_room_uuid):
    """Test checking if room is explored (returns True)."""
    # Mock _get_room_uuid_by_stable_id to return room UUID
    with patch.object(exploration_service, "_get_room_uuid_by_stable_id", return_value=sample_room_uuid):
        result_mock = MagicMock(spec=Result)
        result_mock.scalar_one = MagicMock(return_value=True)  # Record exists
        mock_session.execute.return_value = result_mock

        result = await exploration_service.is_room_explored(sample_player_id, "room_001", mock_session)
        assert result is True


@pytest.mark.asyncio
async def test_is_room_explored_false(exploration_service, mock_session, sample_player_id, sample_room_uuid):
    """Test checking if room is explored (returns False)."""
    # Mock _get_room_uuid_by_stable_id to return room UUID
    with patch.object(exploration_service, "_get_room_uuid_by_stable_id", return_value=sample_room_uuid):
        result_mock = MagicMock(spec=Result)
        result_mock.scalar_one = MagicMock(return_value=False)  # No record
        mock_session.execute.return_value = result_mock

        result = await exploration_service.is_room_explored(sample_player_id, "room_001", mock_session)
        assert result is False


@pytest.mark.asyncio
async def test_is_room_explored_room_not_found(exploration_service, mock_session, sample_player_id):
    """Test checking if room is explored when room not found."""
    # Mock _get_room_uuid_by_stable_id to return None
    with patch.object(exploration_service, "_get_room_uuid_by_stable_id", return_value=None):
        result = await exploration_service.is_room_explored(sample_player_id, "nonexistent_room", mock_session)
        assert result is False


@pytest.mark.asyncio
async def test_is_room_explored_database_error(exploration_service, mock_session, sample_player_id):
    """Test checking if room is explored with database error."""
    mock_session.execute.side_effect = SQLAlchemyError("DB error", None, None)

    with pytest.raises(DatabaseError):
        await exploration_service.is_room_explored(sample_player_id, "room_001", mock_session)


@pytest.mark.asyncio
async def test_mark_room_as_explored_sync_success(exploration_service, sample_player_id, sample_room_id):
    """Test synchronous wrapper for marking room as explored."""
    with patch("asyncio.get_running_loop") as mock_loop:
        mock_event_loop = MagicMock()
        mock_task = MagicMock()
        mock_event_loop.create_task = MagicMock(return_value=mock_task)
        mock_loop.return_value = mock_event_loop

        with patch.object(exploration_service, "mark_room_as_explored", new_callable=AsyncMock):
            exploration_service.mark_room_as_explored_sync(sample_player_id, sample_room_id)
            mock_event_loop.create_task.assert_called_once()


@pytest.mark.asyncio
async def test_mark_room_as_explored_sync_no_loop(exploration_service, sample_player_id, sample_room_id):
    """Test synchronous wrapper when no event loop available."""
    with patch("asyncio.get_running_loop", side_effect=RuntimeError("No running loop")):
        # Should not raise, just log warning
        exploration_service.mark_room_as_explored_sync(sample_player_id, sample_room_id)


@pytest.mark.asyncio
async def test_mark_room_as_explored_sync_with_error_handler(exploration_service, sample_player_id, sample_room_id):
    """Test synchronous wrapper with error handler."""
    error_handler = MagicMock()

    with patch("asyncio.get_running_loop") as mock_loop:
        mock_event_loop = MagicMock()
        mock_task = MagicMock()
        mock_event_loop.create_task = MagicMock(return_value=mock_task)
        mock_loop.return_value = mock_event_loop

        with patch.object(exploration_service, "mark_room_as_explored", new_callable=AsyncMock):
            exploration_service.mark_room_as_explored_sync(sample_player_id, sample_room_id, error_handler)
            mock_event_loop.create_task.assert_called_once()
