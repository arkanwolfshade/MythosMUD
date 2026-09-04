"""
Shared fixtures for unit tests in the infrastructure package.
"""

# pylint: disable=redefined-outer-name  # Reason: pytest fixture parameter names must match fixture names

from unittest.mock import MagicMock

import pytest

from server.async_persistence import AsyncPersistenceLayer


@pytest.fixture
def mock_event_bus() -> MagicMock:
    """Create a mock event bus."""
    return MagicMock()


@pytest.fixture
def async_persistence_layer(mock_event_bus: MagicMock) -> AsyncPersistenceLayer:
    """Create an AsyncPersistenceLayer instance with skipped room cache."""
    return AsyncPersistenceLayer(event_bus=mock_event_bus, _skip_room_cache=True)
