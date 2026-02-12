"""
Shared fixtures for API unit tests.

Provides mock fixtures for container loot endpoint tests and other API tests.
"""

import uuid
from unittest.mock import AsyncMock, MagicMock, Mock

import pytest
from fastapi import Request

from server.models.container import ContainerComponent
from server.models.user import User
from server.services.container_service import ContainerService

# pylint: disable=redefined-outer-name  # Reason: Test file - pytest fixture parameter names must match fixture names


@pytest.fixture
def mock_request():
    """Create a mock request object."""
    request = Mock(spec=Request)
    request.app = MagicMock()
    request.app.state = MagicMock()
    return request


@pytest.fixture
def mock_user():
    """Create a mock user."""
    user = User(
        id=str(uuid.uuid4()),
        username="testuser",
        email="test@example.com",
        hashed_password="hashed",
        is_active=True,
        is_superuser=False,
        is_verified=True,
    )
    return user


@pytest.fixture
def mock_persistence():
    """Create a mock persistence layer."""
    persistence = AsyncMock()
    return persistence


@pytest.fixture
def mock_connection_manager():
    """Create a mock connection manager."""
    manager = AsyncMock()
    return manager


@pytest.fixture
def mock_container_service():
    """Create a mock container service."""
    service = MagicMock(spec=ContainerService)
    return service


@pytest.fixture
def mock_container():
    """Create a mock container component."""
    container = MagicMock(spec=ContainerComponent)
    container.container_id = uuid.uuid4()
    container.room_id = "room_001"
    container.items = [{"item_id": str(uuid.uuid4()), "quantity": 1}]
    container.source_type = MagicMock()
    container.source_type.value = "room"
    container.model_dump = Mock(return_value={"container_id": str(container.container_id), "items": []})
    container.model_validate = Mock(return_value=container)
    return container


@pytest.fixture
def mock_player():
    """Create a mock player."""
    player = MagicMock()
    player.player_id = uuid.uuid4()
    player.name = "TestPlayer"
    return player
