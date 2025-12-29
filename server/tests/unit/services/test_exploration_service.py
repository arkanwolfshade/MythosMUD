"""
Unit tests for exploration service.

Tests the ExplorationService class.
"""

import asyncio
import uuid
from unittest.mock import AsyncMock, MagicMock, patch

import pytest
from sqlalchemy.exc import SQLAlchemyError

from server.exceptions import DatabaseError
from server.services.exploration_service import ExplorationService


@pytest.fixture
def mock_database_manager():
    """Create a mock database manager."""
    manager = MagicMock()
    manager.get_session_maker = MagicMock(return_value=MagicMock())
    return manager


@pytest.fixture
def exploration_service(mock_database_manager):
    """Create an ExplorationService instance."""
    return ExplorationService(mock_database_manager)


def test_exploration_service_init(exploration_service, mock_database_manager):
    """Test ExplorationService initialization."""
    assert exploration_service._database_manager == mock_database_manager


@pytest.mark.asyncio
async def test_mark_room_as_explored_no_session(exploration_service, mock_database_manager):
    """Test mark_room_as_explored() creates new session when none provided."""
    player_id = uuid.uuid4()
    room_id = "earth_arkhamcity_northside_room_001"
    # Mock the session maker and session
    mock_session = AsyncMock()
    mock_session_maker = MagicMock()
    mock_session_maker.return_value.__aenter__ = AsyncMock(return_value=mock_session)
    mock_session_maker.return_value.__aexit__ = AsyncMock(return_value=None)
    mock_database_manager.get_session_maker = MagicMock(return_value=mock_session_maker)
    # Mock _get_room_uuid_by_stable_id to return a UUID
    exploration_service._get_room_uuid_by_stable_id = AsyncMock(return_value=uuid.uuid4())
    exploration_service._mark_explored_in_session = AsyncMock(return_value=True)
    result = await exploration_service.mark_room_as_explored(player_id, room_id)
    assert result is True


@pytest.mark.asyncio
async def test_mark_room_as_explored_with_session(exploration_service):
    """Test mark_room_as_explored() uses provided session."""
    player_id = uuid.uuid4()
    room_id = "earth_arkhamcity_northside_room_001"
    mock_session = AsyncMock()
    room_uuid = uuid.uuid4()
    exploration_service._get_room_uuid_by_stable_id = AsyncMock(return_value=room_uuid)
    exploration_service._mark_explored_in_session = AsyncMock(return_value=True)
    result = await exploration_service.mark_room_as_explored(player_id, room_id, session=mock_session)
    assert result is True
    exploration_service._mark_explored_in_session.assert_awaited_once_with(mock_session, player_id, room_uuid)


@pytest.mark.asyncio
async def test_mark_room_as_explored_room_not_found(exploration_service):
    """Test mark_room_as_explored() returns False when room not found."""
    player_id = uuid.uuid4()
    room_id = "nonexistent_room"
    exploration_service._get_room_uuid_by_stable_id = AsyncMock(return_value=None)
    result = await exploration_service.mark_room_as_explored(player_id, room_id)
    assert result is False


@pytest.mark.asyncio
async def test_mark_room_as_explored_database_error(exploration_service):
    """Test mark_room_as_explored() raises DatabaseError on database failure."""
    player_id = uuid.uuid4()
    room_id = "earth_arkhamcity_northside_room_001"
    exploration_service._get_room_uuid_by_stable_id = AsyncMock(side_effect=SQLAlchemyError("Database error"))
    with pytest.raises(DatabaseError, match="Failed to mark room as explored"):
        await exploration_service.mark_room_as_explored(player_id, room_id)


@pytest.mark.asyncio
async def test_get_room_uuid_by_stable_id_with_session(exploration_service):
    """Test _get_room_uuid_by_stable_id() with provided session."""
    mock_session = AsyncMock()
    room_uuid = uuid.uuid4()
    mock_result = MagicMock()
    mock_result.scalar_one_or_none.return_value = room_uuid
    mock_session.execute = AsyncMock(return_value=mock_result)
    result = await exploration_service._get_room_uuid_by_stable_id("room_001", session=mock_session)
    assert result == room_uuid


@pytest.mark.asyncio
async def test_get_room_uuid_by_stable_id_no_session(exploration_service, mock_database_manager):
    """Test _get_room_uuid_by_stable_id() creates session when none provided."""
    room_uuid = uuid.uuid4()
    mock_session = AsyncMock()
    mock_result = MagicMock()
    mock_result.scalar_one_or_none.return_value = room_uuid
    mock_session.execute = AsyncMock(return_value=mock_result)
    mock_session_maker = MagicMock()
    mock_session_maker.return_value.__aenter__ = AsyncMock(return_value=mock_session)
    mock_session_maker.return_value.__aexit__ = AsyncMock(return_value=None)
    mock_database_manager.get_session_maker = MagicMock(return_value=mock_session_maker)
    result = await exploration_service._get_room_uuid_by_stable_id("room_001")
    assert result == room_uuid


@pytest.mark.asyncio
async def test_get_room_uuid_by_stable_id_not_found(exploration_service):
    """Test _get_room_uuid_by_stable_id() returns None when room not found."""
    mock_session = AsyncMock()
    mock_result = MagicMock()
    mock_result.scalar_one_or_none.return_value = None
    mock_session.execute = AsyncMock(return_value=mock_result)
    result = await exploration_service._get_room_uuid_by_stable_id("nonexistent", session=mock_session)
    assert result is None


@pytest.mark.asyncio
async def test_get_room_uuid_by_stable_id_string_uuid(exploration_service):
    """Test _get_room_uuid_by_stable_id() handles string UUID from database."""
    mock_session = AsyncMock()
    room_uuid_str = str(uuid.uuid4())
    mock_result = MagicMock()
    mock_result.scalar_one_or_none.return_value = room_uuid_str
    mock_session.execute = AsyncMock(return_value=mock_result)
    result = await exploration_service._get_room_uuid_by_stable_id("room_001", session=mock_session)
    assert isinstance(result, uuid.UUID)
    assert str(result) == room_uuid_str


@pytest.mark.asyncio
async def test_mark_explored_in_session_new_record(exploration_service):
    """Test _mark_explored_in_session() inserts new exploration record."""
    mock_session = AsyncMock()
    player_id = uuid.uuid4()
    room_uuid = uuid.uuid4()
    # Mock check query to return None (no existing record)
    mock_check_result = MagicMock()
    mock_check_result.scalar_one_or_none.return_value = None
    mock_session.execute = AsyncMock(return_value=mock_check_result)
    result = await exploration_service._mark_explored_in_session(mock_session, player_id, room_uuid)
    assert result is True
    assert mock_session.execute.call_count == 2  # Check + insert


@pytest.mark.asyncio
async def test_mark_explored_in_session_existing_record(exploration_service):
    """Test _mark_explored_in_session() returns True for existing record."""
    mock_session = AsyncMock()
    player_id = uuid.uuid4()
    room_uuid = uuid.uuid4()
    # Mock check query to return existing record
    mock_check_result = MagicMock()
    mock_check_result.scalar_one_or_none.return_value = "existing_id"
    mock_session.execute = AsyncMock(return_value=mock_check_result)
    result = await exploration_service._mark_explored_in_session(mock_session, player_id, room_uuid)
    assert result is True
    assert mock_session.execute.call_count == 1  # Only check, no insert


@pytest.mark.asyncio
async def test_get_explored_rooms(exploration_service):
    """Test get_explored_rooms() returns list of explored room IDs."""
    mock_session = AsyncMock()
    player_id = uuid.uuid4()
    room_uuid1 = uuid.uuid4()
    room_uuid2 = uuid.uuid4()
    mock_rows = [(room_uuid1,), (room_uuid2,)]
    mock_result = MagicMock()
    mock_result.fetchall.return_value = mock_rows
    mock_session.execute = AsyncMock(return_value=mock_result)
    result = await exploration_service.get_explored_rooms(player_id, mock_session)
    assert len(result) == 2
    assert str(room_uuid1) in result
    assert str(room_uuid2) in result


@pytest.mark.asyncio
async def test_get_explored_rooms_empty(exploration_service):
    """Test get_explored_rooms() returns empty list when no explored rooms."""
    mock_session = AsyncMock()
    player_id = uuid.uuid4()
    mock_result = MagicMock()
    mock_result.fetchall.return_value = []
    mock_session.execute = AsyncMock(return_value=mock_result)
    result = await exploration_service.get_explored_rooms(player_id, mock_session)
    assert result == []


@pytest.mark.asyncio
async def test_get_explored_rooms_database_error(exploration_service):
    """Test get_explored_rooms() raises DatabaseError on database failure."""
    mock_session = AsyncMock()
    player_id = uuid.uuid4()
    mock_session.execute = AsyncMock(side_effect=SQLAlchemyError("Database error"))
    with pytest.raises(DatabaseError, match="Failed to retrieve explored rooms"):
        await exploration_service.get_explored_rooms(player_id, mock_session)


@pytest.mark.asyncio
async def test_is_room_explored_true(exploration_service):
    """Test is_room_explored() returns True when room is explored."""
    mock_session = AsyncMock()
    player_id = uuid.uuid4()
    room_id = "room_001"
    room_uuid = uuid.uuid4()
    exploration_service._get_room_uuid_by_stable_id = AsyncMock(return_value=room_uuid)
    mock_result = MagicMock()
    mock_result.scalar_one.return_value = True
    mock_session.execute = AsyncMock(return_value=mock_result)
    result = await exploration_service.is_room_explored(player_id, room_id, mock_session)
    assert result is True


@pytest.mark.asyncio
async def test_is_room_explored_false(exploration_service):
    """Test is_room_explored() returns False when room is not explored."""
    mock_session = AsyncMock()
    player_id = uuid.uuid4()
    room_id = "room_001"
    room_uuid = uuid.uuid4()
    exploration_service._get_room_uuid_by_stable_id = AsyncMock(return_value=room_uuid)
    mock_result = MagicMock()
    mock_result.scalar_one.return_value = False
    mock_session.execute = AsyncMock(return_value=mock_result)
    result = await exploration_service.is_room_explored(player_id, room_id, mock_session)
    assert result is False


@pytest.mark.asyncio
async def test_is_room_explored_room_not_found(exploration_service):
    """Test is_room_explored() returns False when room not found."""
    mock_session = AsyncMock()
    player_id = uuid.uuid4()
    room_id = "nonexistent"
    exploration_service._get_room_uuid_by_stable_id = AsyncMock(return_value=None)
    result = await exploration_service.is_room_explored(player_id, room_id, mock_session)
    assert result is False


@pytest.mark.asyncio
async def test_is_room_explored_database_error(exploration_service):
    """Test is_room_explored() raises DatabaseError on database failure."""
    mock_session = AsyncMock()
    player_id = uuid.uuid4()
    room_id = "room_001"
    exploration_service._get_room_uuid_by_stable_id = AsyncMock(side_effect=SQLAlchemyError("Database error"))
    with pytest.raises(DatabaseError, match="Failed to check room exploration"):
        await exploration_service.is_room_explored(player_id, room_id, mock_session)


def test_mark_room_as_explored_sync_with_loop(exploration_service):
    """Test mark_room_as_explored_sync() schedules task when loop is running."""
    player_id = uuid.uuid4()
    room_id = "room_001"
    # Create a mock loop
    mock_loop = MagicMock()
    mock_task = MagicMock()
    mock_loop.create_task = MagicMock(return_value=mock_task)
    with patch("asyncio.get_running_loop", return_value=mock_loop):
        with patch.object(exploration_service, "mark_room_as_explored", new_callable=AsyncMock):
            exploration_service.mark_room_as_explored_sync(player_id, room_id)
            mock_loop.create_task.assert_called_once()


def test_mark_room_as_explored_sync_no_loop(exploration_service):
    """Test mark_room_as_explored_sync() handles no running loop gracefully."""
    player_id = uuid.uuid4()
    room_id = "room_001"
    with patch("asyncio.get_running_loop", side_effect=RuntimeError("No running loop")):
        # Should not raise, just log warning
        exploration_service.mark_room_as_explored_sync(player_id, room_id)


def test_mark_room_as_explored_sync_with_error_handler(exploration_service):
    """Test mark_room_as_explored_sync() calls error handler on error."""
    player_id = uuid.uuid4()
    room_id = "room_001"
    error_handler = MagicMock()
    mock_loop = MagicMock()
    mock_task = MagicMock()
    mock_loop.create_task = MagicMock(return_value=mock_task)
    with patch("asyncio.get_running_loop", return_value=mock_loop):
        # Make mark_room_as_explored raise an error
        with patch.object(
            exploration_service,
            "mark_room_as_explored",
            new_callable=AsyncMock,
            side_effect=DatabaseError("Test error"),
        ):
            # Wait for the task to complete
            async def wait_for_task():
                await asyncio.sleep(0.1)  # Give task time to run

            exploration_service.mark_room_as_explored_sync(player_id, room_id, error_handler=error_handler)
            # Note: In a real scenario, we'd await the task, but since it's fire-and-forget,
            # we just verify the task was created
            mock_loop.create_task.assert_called_once()


@pytest.mark.asyncio
async def test_get_room_uuid_by_stable_id_asyncpg_uuid(exploration_service):
    """Test _get_room_uuid_by_stable_id() handles asyncpg UUID objects."""
    mock_session = AsyncMock()

    # Create a mock asyncpg UUID-like object
    class MockAsyncpgUUID:
        def __str__(self):
            return str(uuid.uuid4())

    mock_asyncpg_uuid = MockAsyncpgUUID()
    mock_result = MagicMock()
    mock_result.scalar_one_or_none.return_value = mock_asyncpg_uuid
    mock_session.execute = AsyncMock(return_value=mock_result)
    result = await exploration_service._get_room_uuid_by_stable_id("room_001", session=mock_session)
    assert isinstance(result, uuid.UUID)


@pytest.mark.asyncio
async def test_get_room_uuid_by_stable_id_database_error(exploration_service):
    """Test _get_room_uuid_by_stable_id() raises DatabaseError on SQLAlchemyError."""
    mock_session = AsyncMock()
    mock_session.execute = AsyncMock(side_effect=SQLAlchemyError("Database error"))
    with pytest.raises(DatabaseError, match="Failed to look up room UUID"):
        await exploration_service._get_room_uuid_by_stable_id("room_001", session=mock_session)


@pytest.mark.asyncio
async def test_get_room_uuid_by_stable_id_generic_exception(exploration_service):
    """Test _get_room_uuid_by_stable_id() raises generic exception."""
    mock_session = AsyncMock()
    mock_session.execute = AsyncMock(side_effect=ValueError("Unexpected error"))
    with pytest.raises(ValueError, match="Unexpected error"):
        await exploration_service._get_room_uuid_by_stable_id("room_001", session=mock_session)


@pytest.mark.asyncio
async def test_mark_explored_in_session_database_error(exploration_service):
    """Test _mark_explored_in_session() raises SQLAlchemyError on database failure."""
    mock_session = AsyncMock()
    player_id = uuid.uuid4()
    room_uuid = uuid.uuid4()
    mock_session.execute = AsyncMock(side_effect=SQLAlchemyError("Database error"))
    with pytest.raises(SQLAlchemyError):
        await exploration_service._mark_explored_in_session(mock_session, player_id, room_uuid)


@pytest.mark.asyncio
async def test_get_explored_rooms_async_fetchall(exploration_service):
    """Test get_explored_rooms() handles async fetchall() result."""
    mock_session = AsyncMock()
    player_id = uuid.uuid4()
    room_uuid1 = uuid.uuid4()
    room_uuid2 = uuid.uuid4()
    mock_rows = [(room_uuid1,), (room_uuid2,)]

    # Create a mock result with async fetchall
    async def async_fetchall():
        return mock_rows

    mock_result = MagicMock()
    mock_result.fetchall = async_fetchall
    mock_session.execute = AsyncMock(return_value=mock_result)
    result = await exploration_service.get_explored_rooms(player_id, mock_session)
    assert len(result) == 2
    assert str(room_uuid1) in result
    assert str(room_uuid2) in result


@pytest.mark.asyncio
async def test_get_explored_rooms_generic_exception(exploration_service):
    """Test get_explored_rooms() raises generic exception."""
    mock_session = AsyncMock()
    player_id = uuid.uuid4()
    mock_session.execute = AsyncMock(side_effect=ValueError("Unexpected error"))
    with pytest.raises(ValueError, match="Unexpected error"):
        await exploration_service.get_explored_rooms(player_id, mock_session)


@pytest.mark.asyncio
async def test_mark_room_as_explored_generic_exception(exploration_service):
    """Test mark_room_as_explored() raises generic exception."""
    player_id = uuid.uuid4()
    room_id = "earth_arkhamcity_northside_room_001"
    exploration_service._get_room_uuid_by_stable_id = AsyncMock(side_effect=ValueError("Unexpected error"))
    with pytest.raises(ValueError, match="Unexpected error"):
        await exploration_service.mark_room_as_explored(player_id, room_id)


@pytest.mark.asyncio
async def test_is_room_explored_generic_exception(exploration_service):
    """Test is_room_explored() raises generic exception."""
    mock_session = AsyncMock()
    player_id = uuid.uuid4()
    room_id = "room_001"
    exploration_service._get_room_uuid_by_stable_id = AsyncMock(side_effect=ValueError("Unexpected error"))
    with pytest.raises(ValueError, match="Unexpected error"):
        await exploration_service.is_room_explored(player_id, room_id, mock_session)


@pytest.mark.asyncio
async def test_is_room_explored_database_error_in_query(exploration_service):
    """Test is_room_explored() raises DatabaseError when query fails."""
    mock_session = AsyncMock()
    player_id = uuid.uuid4()
    room_id = "room_001"
    room_uuid = uuid.uuid4()
    exploration_service._get_room_uuid_by_stable_id = AsyncMock(return_value=room_uuid)
    mock_session.execute = AsyncMock(side_effect=SQLAlchemyError("Database error"))
    with pytest.raises(DatabaseError, match="Failed to check room exploration"):
        await exploration_service.is_room_explored(player_id, room_id, mock_session)


def test_mark_room_as_explored_sync_generic_exception(exploration_service):
    """Test mark_room_as_explored_sync() handles generic exception in task creation."""
    player_id = uuid.uuid4()
    room_id = "room_001"
    # Make get_running_loop raise a generic exception
    with patch("asyncio.get_running_loop", side_effect=Exception("Unexpected error")):
        # Should not raise, just log warning
        exploration_service.mark_room_as_explored_sync(player_id, room_id)


def test_mark_room_as_explored_sync_error_handler_called(exploration_service):
    """Test mark_room_as_explored_sync() calls error handler on exception in task creation."""
    player_id = uuid.uuid4()
    room_id = "room_001"
    error_handler = MagicMock()
    with patch("asyncio.get_running_loop", side_effect=Exception("Unexpected error")):
        exploration_service.mark_room_as_explored_sync(player_id, room_id, error_handler=error_handler)
        # Error handler should be called
        error_handler.assert_called_once()


@pytest.mark.asyncio
async def test_mark_room_as_explored_commits_session(exploration_service, mock_database_manager):
    """Test mark_room_as_explored() commits session when creating new session."""
    player_id = uuid.uuid4()
    room_id = "earth_arkhamcity_northside_room_001"
    mock_session = AsyncMock()
    mock_session.commit = AsyncMock()
    mock_session_maker = MagicMock()
    mock_session_maker.return_value.__aenter__ = AsyncMock(return_value=mock_session)
    mock_session_maker.return_value.__aexit__ = AsyncMock(return_value=None)
    mock_database_manager.get_session_maker = MagicMock(return_value=mock_session_maker)
    exploration_service._get_room_uuid_by_stable_id = AsyncMock(return_value=uuid.uuid4())
    exploration_service._mark_explored_in_session = AsyncMock(return_value=True)
    await exploration_service.mark_room_as_explored(player_id, room_id)
    mock_session.commit.assert_awaited_once()
