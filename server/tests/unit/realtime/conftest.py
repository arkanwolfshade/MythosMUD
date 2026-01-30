"""
Shared fixtures for realtime unit tests.

Provides fixtures used by NATS message handler, WebSocket handler, player room event
handler, and other realtime tests.
"""

from unittest.mock import AsyncMock, MagicMock

import pytest

from server.realtime.nats_message_handler import NATSMessageHandler
from server.realtime.player_event_handlers_room import PlayerRoomEventHandler
from server.realtime.player_event_handlers_utils import PlayerEventHandlerUtils


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


# Player room event handler fixtures (shared by test_player_event_handlers_room*.py)
@pytest.fixture
def mock_room_sync_service():
    """Create a mock room sync service."""
    return MagicMock()


@pytest.fixture
def mock_chat_logger():
    """Create a mock chat logger."""
    return MagicMock()


@pytest.fixture
def mock_message_builder():
    """Create a mock message builder."""
    return MagicMock()


@pytest.fixture
def mock_name_extractor():
    """Create a mock name extractor."""
    return MagicMock()


@pytest.fixture
def mock_occupant_manager():
    """Create a mock occupant manager."""
    return MagicMock()


@pytest.fixture
def mock_utils(mock_connection_manager):
    """Create a mock PlayerEventHandlerUtils."""
    return PlayerEventHandlerUtils(mock_connection_manager, MagicMock(), MagicMock())


@pytest.fixture
def mock_logger():
    """Create a mock logger."""
    return MagicMock()


@pytest.fixture
def player_room_event_handler(
    mock_connection_manager,
    mock_room_sync_service,
    mock_chat_logger,
    mock_message_builder,
    mock_name_extractor,
    mock_occupant_manager,
    mock_utils,
    mock_logger,
):
    """Create a PlayerRoomEventHandler instance."""
    return PlayerRoomEventHandler(
        connection_manager=mock_connection_manager,
        room_sync_service=mock_room_sync_service,
        chat_logger=mock_chat_logger,
        message_builder=mock_message_builder,
        name_extractor=mock_name_extractor,
        occupant_manager=mock_occupant_manager,
        utils=mock_utils,
        logger=mock_logger,
    )
