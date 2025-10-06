"""
Test-specific FastAPI application factory for dependency injection tests.

This module creates a minimal FastAPI application for testing dependency injection
without requiring external services like NATS, database connections, or file systems.
"""

from unittest.mock import AsyncMock, Mock

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from ..api.players import player_router
from ..api.rooms import room_router
from ..error_handlers import register_error_handlers
from ..logging_config import get_logger

logger = get_logger(__name__)


def create_test_app() -> FastAPI:
    """
    Create a minimal FastAPI application for testing dependency injection.

    This factory creates an app without external dependencies like NATS,
    database connections, or file systems. It's specifically designed
    for testing the dependency injection system in isolation.

    Returns:
        FastAPI: A minimal FastAPI application for testing
    """
    app = FastAPI(
        title="MythosMUD Test API",
        description="Test API for dependency injection testing",
        version="0.1.0",
    )

    # Add CORS middleware
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["http://localhost:5173", "http://127.0.0.1:5173"],
        allow_credentials=True,
        allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
        allow_headers=["Content-Type", "Authorization", "X-Requested-With"],
    )

    # Register error handlers
    register_error_handlers(app)

    # Include only the routers we need for dependency injection testing
    app.include_router(player_router)
    app.include_router(room_router)

    # Set up minimal app state for testing
    _setup_test_app_state(app)

    return app


def _setup_test_app_state(app: FastAPI) -> None:
    """
    Set up minimal app state for testing.

    This creates mock objects for all the services that would normally
    be initialized during application startup, allowing dependency injection
    tests to run without external dependencies.
    """
    # Create mock persistence layer
    mock_persistence = AsyncMock()
    mock_persistence.async_list_players.return_value = []
    mock_persistence.async_get_player.return_value = None
    mock_persistence.async_get_room.return_value = None
    mock_persistence.async_save_player.return_value = None
    mock_persistence.async_delete_player.return_value = True
    # Also mock synchronous methods for backward compatibility
    mock_persistence.list_players.return_value = []
    mock_persistence.get_player.return_value = None
    mock_persistence.get_room.return_value = None
    mock_persistence.save_player.return_value = None
    mock_persistence.delete_player.return_value = True

    app.state.persistence = mock_persistence

    # Create mock player service
    from ..game.player_service import PlayerService

    app.state.player_service = PlayerService(mock_persistence)

    # Create mock user manager
    from ..services.user_manager import UserManager

    mock_user_manager = Mock(spec=UserManager)
    app.state.user_manager = mock_user_manager

    # Create mock event handler and event bus
    mock_event_handler = Mock()
    mock_event_bus = Mock()
    mock_event_handler.event_bus = mock_event_bus
    app.state.event_handler = mock_event_handler
    app.state.event_bus = mock_event_bus

    # Create mock connection manager
    mock_connection_manager = Mock()
    mock_connection_manager.persistence = mock_persistence
    mock_connection_manager._event_bus = mock_event_bus
    mock_connection_manager.app = app
    app.state.connection_manager = mock_connection_manager

    logger.info("Test app state initialized with mock services")
