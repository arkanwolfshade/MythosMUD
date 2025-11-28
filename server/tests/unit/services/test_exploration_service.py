"""Tests for exploration service."""

from unittest.mock import AsyncMock, Mock, patch
from uuid import uuid4

import pytest
from sqlalchemy.exc import SQLAlchemyError

from server.services.exploration_service import ExplorationService, get_exploration_service

# Test UUID constants for consistent testing
TEST_PLAYER_ID = uuid4()
TEST_ROOM_UUID = uuid4()
TEST_ROOM_STABLE_ID = "earth_arkhamcity_northside_intersection_derby_high"


@pytest.fixture
def exploration_service():
    """Create an exploration service instance for testing."""
    return ExplorationService()


@pytest.fixture
def mock_session():
    """Create a mock async database session."""
    return AsyncMock()


class TestExplorationService:
    """Test suite for ExplorationService."""

    @pytest.mark.asyncio
    async def test_mark_room_as_explored_success(self, exploration_service, mock_session):
        """Test successfully marking a room as explored."""
        # Mock room UUID lookup
        mock_result = AsyncMock()
        mock_result.scalar_one_or_none.return_value = str(TEST_ROOM_UUID)
        mock_session.execute.return_value = mock_result

        # First call: room UUID lookup (returns UUID)
        # Second call: check if already explored (returns None - not explored)
        # Third call: insert exploration record
        mock_session.execute.side_effect = [
            mock_result,  # Room UUID lookup
            AsyncMock(scalar_one_or_none=Mock(return_value=None)),  # Check if explored
            AsyncMock(),  # Insert exploration
        ]

        result = await exploration_service.mark_room_as_explored(TEST_PLAYER_ID, TEST_ROOM_STABLE_ID, mock_session)

        assert result is True
        assert mock_session.execute.call_count >= 2  # At least room lookup and insert

    @pytest.mark.asyncio
    async def test_mark_room_as_explored_already_explored(self, exploration_service, mock_session):
        """Test marking a room that's already explored (idempotent)."""
        # Mock room UUID lookup
        mock_result = AsyncMock()
        mock_result.scalar_one_or_none.return_value = str(TEST_ROOM_UUID)
        mock_session.execute.return_value = mock_result

        # First call: room UUID lookup (returns UUID)
        # Second call: check if already explored (returns existing record)
        mock_session.execute.side_effect = [
            mock_result,  # Room UUID lookup
            AsyncMock(scalar_one_or_none=Mock(return_value=uuid4())),  # Already explored
        ]

        result = await exploration_service.mark_room_as_explored(TEST_PLAYER_ID, TEST_ROOM_STABLE_ID, mock_session)

        assert result is True
        # Should not insert a new record if already explored
        assert mock_session.execute.call_count == 2

    @pytest.mark.asyncio
    async def test_mark_room_as_explored_room_not_found(self, exploration_service, mock_session):
        """Test marking exploration for a room that doesn't exist."""
        # Mock room UUID lookup returning None
        mock_result = AsyncMock()
        mock_result.scalar_one_or_none.return_value = None
        mock_session.execute.return_value = mock_result

        result = await exploration_service.mark_room_as_explored(TEST_PLAYER_ID, TEST_ROOM_STABLE_ID, mock_session)

        assert result is False

    @pytest.mark.asyncio
    async def test_mark_room_as_explored_database_error(self, exploration_service, mock_session):
        """Test handling database errors when marking room as explored."""
        # Mock database error
        mock_session.execute.side_effect = SQLAlchemyError("Database connection failed")

        with pytest.raises(SQLAlchemyError):  # Should raise DatabaseError
            await exploration_service.mark_room_as_explored(TEST_PLAYER_ID, TEST_ROOM_STABLE_ID, mock_session)

    @pytest.mark.asyncio
    async def test_get_explored_rooms(self, exploration_service, mock_session):
        """Test retrieving list of explored rooms for a player."""
        # Mock database result
        mock_rows = [
            (str(TEST_ROOM_UUID),),
            (str(uuid4()),),
        ]
        mock_result = AsyncMock()
        mock_result.fetchall.return_value = mock_rows
        mock_session.execute.return_value = mock_result

        result = await exploration_service.get_explored_rooms(TEST_PLAYER_ID, mock_session)

        assert len(result) == 2
        assert str(TEST_ROOM_UUID) in result
        mock_session.execute.assert_called_once()

    @pytest.mark.asyncio
    async def test_get_explored_rooms_empty(self, exploration_service, mock_session):
        """Test retrieving explored rooms when player has explored none."""
        # Mock empty result
        mock_result = AsyncMock()
        mock_result.fetchall.return_value = []
        mock_session.execute.return_value = mock_result

        result = await exploration_service.get_explored_rooms(TEST_PLAYER_ID, mock_session)

        assert result == []

    @pytest.mark.asyncio
    async def test_is_room_explored_true(self, exploration_service, mock_session):
        """Test checking if a room is explored (returns True)."""
        # Mock room UUID lookup
        mock_room_result = AsyncMock()
        mock_room_result.scalar_one_or_none.return_value = str(TEST_ROOM_UUID)

        # Mock exploration check
        mock_exploration_result = AsyncMock()
        mock_exploration_result.scalar_one.return_value = True

        mock_session.execute.side_effect = [
            mock_room_result,  # Room UUID lookup
            mock_exploration_result,  # Exploration check
        ]

        result = await exploration_service.is_room_explored(TEST_PLAYER_ID, TEST_ROOM_STABLE_ID, mock_session)

        assert result is True

    @pytest.mark.asyncio
    async def test_is_room_explored_false(self, exploration_service, mock_session):
        """Test checking if a room is explored (returns False)."""
        # Mock room UUID lookup
        mock_room_result = AsyncMock()
        mock_room_result.scalar_one_or_none.return_value = str(TEST_ROOM_UUID)

        # Mock exploration check
        mock_exploration_result = AsyncMock()
        mock_exploration_result.scalar_one.return_value = False

        mock_session.execute.side_effect = [
            mock_room_result,  # Room UUID lookup
            mock_exploration_result,  # Exploration check
        ]

        result = await exploration_service.is_room_explored(TEST_PLAYER_ID, TEST_ROOM_STABLE_ID, mock_session)

        assert result is False

    @pytest.mark.asyncio
    async def test_is_room_explored_room_not_found(self, exploration_service, mock_session):
        """Test checking exploration for a room that doesn't exist."""
        # Mock room UUID lookup returning None
        mock_room_result = AsyncMock()
        mock_room_result.scalar_one_or_none.return_value = None
        mock_session.execute.return_value = mock_room_result

        result = await exploration_service.is_room_explored(TEST_PLAYER_ID, TEST_ROOM_STABLE_ID, mock_session)

        assert result is False

    @pytest.mark.asyncio
    async def test_mark_room_as_explored_without_session(self, exploration_service):
        """Test marking room as explored without providing a session."""
        with patch("server.services.exploration_service.get_database_manager") as mock_db_manager:
            # Mock database manager and session maker
            mock_session_maker = AsyncMock()
            mock_new_session = AsyncMock()
            mock_session_maker.return_value.__aenter__.return_value = mock_new_session
            mock_session_maker.return_value.__aexit__.return_value = None

            mock_db_instance = Mock()
            mock_db_instance.get_session_maker.return_value = mock_session_maker
            mock_db_manager.return_value = mock_db_instance

            # Mock room UUID lookup
            mock_room_result = AsyncMock()
            mock_room_result.scalar_one_or_none.return_value = str(TEST_ROOM_UUID)

            # Mock exploration check and insert
            mock_new_session.execute.side_effect = [
                mock_room_result,  # Room UUID lookup
                AsyncMock(scalar_one_or_none=Mock(return_value=None)),  # Check if explored
                AsyncMock(),  # Insert exploration
            ]

            result = await exploration_service.mark_room_as_explored(TEST_PLAYER_ID, TEST_ROOM_STABLE_ID)

            assert result is True
            mock_new_session.commit.assert_called_once()

    def test_mark_room_as_explored_sync(self, exploration_service):
        """Test synchronous wrapper for marking room as explored."""
        with patch("asyncio.get_running_loop") as mock_get_loop:
            # Mock event loop
            mock_loop = Mock()
            mock_loop.create_task = Mock()
            mock_get_loop.return_value = mock_loop

            # Call sync wrapper
            exploration_service.mark_room_as_explored_sync(TEST_PLAYER_ID, TEST_ROOM_STABLE_ID)

            # Verify task was created (fire-and-forget)
            mock_loop.create_task.assert_called_once()

    def test_mark_room_as_explored_sync_no_loop(self, exploration_service):
        """Test synchronous wrapper when no event loop is running."""
        with patch("asyncio.get_running_loop") as mock_get_loop, patch("asyncio.run") as mock_run:
            # Mock no running loop
            mock_get_loop.side_effect = RuntimeError("No running loop")

            # Call sync wrapper
            exploration_service.mark_room_as_explored_sync(TEST_PLAYER_ID, TEST_ROOM_STABLE_ID)

            # Verify asyncio.run was called
            mock_run.assert_called_once()

    def test_get_exploration_service_singleton(self):
        """Test that get_exploration_service returns a singleton."""
        service1 = get_exploration_service()
        service2 = get_exploration_service()

        assert service1 is service2
        assert isinstance(service1, ExplorationService)
