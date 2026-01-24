"""
Shared fixtures for realtime unit tests.

Provides fixtures used by NATS message handler, WebSocket handler, and other realtime tests.
"""

from unittest.mock import AsyncMock, MagicMock

import pytest

from server.realtime.nats_message_handler import NATSMessageHandler


# pylint: disable=redefined-outer-name  # Reason: pytest fixture parameter names must match fixture names
@pytest.fixture
def mock_nats_service():
    """Create a mock NATS service."""
    return MagicMock()


@pytest.fixture
def mock_subject_manager():
    """Create a mock subject manager."""
    return MagicMock()


@pytest.fixture
def mock_connection_manager():
    """Create a mock connection manager (NATS / general)."""
    return MagicMock()


@pytest.fixture
def mock_websocket():
    """Create mock WebSocket for handler tests."""
    ws = MagicMock()
    ws.send_json = AsyncMock()
    ws.close = AsyncMock()
    return ws


@pytest.fixture
def mock_ws_connection_manager():
    """Create mock connection manager for WebSocket handler tests."""
    manager = MagicMock()
    manager.get_connection_id_from_websocket = MagicMock(return_value="conn_001")
    manager.mark_player_seen = MagicMock()
    manager.get_player = AsyncMock()
    manager.async_persistence = MagicMock()
    manager.broadcast_to_room = AsyncMock()
    return manager


@pytest.fixture
def mock_user_manager():
    """Create a mock user manager."""
    return MagicMock()


@pytest.fixture
def nats_message_handler(mock_nats_service, mock_subject_manager, mock_connection_manager, mock_user_manager):
    """Create a NATSMessageHandler instance."""
    return NATSMessageHandler(
        nats_service=mock_nats_service,
        subject_manager=mock_subject_manager,
        connection_manager=mock_connection_manager,
        user_manager=mock_user_manager,
    )
