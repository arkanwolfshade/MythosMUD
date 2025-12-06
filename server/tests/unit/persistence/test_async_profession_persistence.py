"""
Greenfield async unit tests for AsyncPersistenceLayer profession operations.

These tests cover all profession-related persistence operations using the
async persistence layer directly.
"""

from unittest.mock import AsyncMock, Mock, patch

import pytest

from server.async_persistence import AsyncPersistenceLayer
from server.events.event_bus import EventBus
from server.models.profession import Profession


class TestAsyncProfessionPersistence:
    """Test async profession persistence operations."""

    @pytest.fixture
    def event_bus(self):
        """Create an event bus for testing."""
        return EventBus()

    @pytest.fixture
    def async_persistence(self, event_bus):
        """Create an AsyncPersistenceLayer instance for testing."""
        return AsyncPersistenceLayer(event_bus=event_bus)

    @pytest.fixture
    def sample_profession(self):
        """Create a sample profession for testing."""
        profession = Mock(spec=Profession)
        profession.id = 1
        profession.name = "Scholar"
        profession.description = "A learned academic"
        profession.is_available = True
        return profession

    @pytest.mark.asyncio
    async def test_get_professions(self, async_persistence, sample_profession):
        """Test getting all available professions."""
        professions = [sample_profession]
        # Mock the async session and query
        with patch("server.async_persistence.get_async_session") as mock_session:
            mock_session.return_value.__aenter__.return_value.execute = AsyncMock()
            mock_session.return_value.__aenter__.return_value.execute.return_value.scalars.return_value.all.return_value = professions

            result = await async_persistence.get_professions()

            assert isinstance(result, list)
            assert len(result) == 1
            assert result[0].name == "Scholar"

    @pytest.mark.asyncio
    async def test_get_profession_by_id_exists(self, async_persistence, sample_profession):
        """Test getting a profession by ID when profession exists."""
        # Mock the repository get method
        async_persistence._profession_repo.get_profession_by_id = AsyncMock(return_value=sample_profession)

        result = await async_persistence.get_profession_by_id(1)

        assert result is not None
        assert result.id == 1
        assert result.name == "Scholar"
        async_persistence._profession_repo.get_profession_by_id.assert_called_once_with(1)

    @pytest.mark.asyncio
    async def test_get_profession_by_id_not_exists(self, async_persistence):
        """Test getting a profession by ID when profession does not exist."""
        # Mock the repository to return None
        async_persistence._profession_repo.get_profession_by_id = AsyncMock(return_value=None)

        result = await async_persistence.get_profession_by_id(999)

        assert result is None
        async_persistence._profession_repo.get_profession_by_id.assert_called_once_with(999)
