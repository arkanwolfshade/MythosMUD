"""
Unit tests for target resolution service.

Tests the TargetResolutionService class.
"""

import uuid
from unittest.mock import AsyncMock, MagicMock

import pytest

from server.services.target_resolution_service import TargetResolutionService


@pytest.fixture
def mock_persistence():
    """Create a mock persistence layer."""
    return AsyncMock()


@pytest.fixture
def mock_player_service():
    """Create a mock player service."""
    return AsyncMock()


@pytest.fixture
def target_service(mock_persistence, mock_player_service):
    """Create a TargetResolutionService instance."""
    return TargetResolutionService(mock_persistence, mock_player_service)


@pytest.mark.asyncio
async def test_target_resolution_service_init(mock_persistence, mock_player_service):
    """Test TargetResolutionService initialization."""
    service = TargetResolutionService(mock_persistence, mock_player_service)
    assert service.persistence == mock_persistence
    assert service.player_service == mock_player_service


@pytest.mark.asyncio
async def test_resolve_target_no_persistence_methods(target_service, mock_persistence):
    """Test resolve_target() when persistence has no get methods."""
    # Remove the methods by deleting the attributes
    if hasattr(mock_persistence, "get_player_by_id"):
        delattr(mock_persistence, "get_player_by_id")
    if hasattr(mock_persistence, "get_player"):
        delattr(mock_persistence, "get_player")
    result = await target_service.resolve_target(uuid.uuid4(), "target")
    assert result.success is False
    assert "error" in result.error_message.lower() or "not configured" in result.error_message.lower()


@pytest.mark.asyncio
async def test_resolve_target_player_not_found(target_service, mock_persistence):
    """Test resolve_target() when player is not found."""
    mock_persistence.get_player_by_id = AsyncMock(return_value=None)
    result = await target_service.resolve_target(uuid.uuid4(), "target")
    assert result.success is False
    assert "not found" in result.error_message.lower() or "error" in result.error_message.lower()


@pytest.mark.asyncio
async def test_resolve_target_no_room(target_service, mock_persistence):
    """Test resolve_target() when player has no room."""
    mock_player = MagicMock()
    mock_player.current_room_id = None
    mock_persistence.get_player_by_id = AsyncMock(return_value=mock_player)
    result = await target_service.resolve_target(uuid.uuid4(), "target")
    assert result.success is False
    assert "not in a room" in result.error_message.lower() or "room" in result.error_message.lower()
