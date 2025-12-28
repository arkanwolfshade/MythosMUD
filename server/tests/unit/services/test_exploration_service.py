"""
Unit tests for exploration service.

Tests the ExplorationService class.
"""

import uuid
from unittest.mock import AsyncMock, MagicMock

import pytest

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
