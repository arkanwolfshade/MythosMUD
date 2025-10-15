"""
Dependency injection providers for MythosMUD server.

This module provides dependency injection functions for services and other
components, following the service layer pattern and ensuring proper separation
of concerns between API endpoints and business logic.

As noted in the Pnakotic Manuscripts, proper organization of arcane knowledge
requires clear separation between the presentation layer and the underlying
mysteries. This dependency injection system provides that separation.
"""

from fastapi import Depends, Request

from .game.player_service import PlayerService
from .game.room_service import RoomService
from .logging_config import get_logger

logger = get_logger(__name__)


def get_player_service(request: Request) -> PlayerService:
    """
    Get a PlayerService instance with dependency injection.

    This function provides a PlayerService instance with the persistence
    layer injected from the application state.

    Args:
        request: The FastAPI request object containing app state

    Returns:
        PlayerService: A configured PlayerService instance
    """
    logger.debug("Creating PlayerService with dependency injection")
    persistence = request.app.state.persistence
    return PlayerService(persistence)


def get_player_service_for_testing() -> PlayerService:
    """
    Get a PlayerService instance for testing purposes.

    This function provides a PlayerService instance that can be used
    in tests without requiring a full request context.

    Returns:
        PlayerService: A configured PlayerService instance for testing
    """
    logger.debug("Creating PlayerService for testing")
    # For testing, we'll use a mock persistence layer
    from unittest.mock import Mock

    mock_persistence = Mock()
    return PlayerService(mock_persistence)


def get_room_service(request: Request) -> RoomService:
    """
    Get a RoomService instance with dependency injection.

    This function provides a RoomService instance with the persistence
    layer injected from the application state.

    Args:
        request: The FastAPI request object containing app state

    Returns:
        RoomService: A configured RoomService instance
    """
    logger.debug("Creating RoomService with dependency injection")
    persistence = request.app.state.persistence
    return RoomService(persistence)


# Type aliases for dependency injection
PlayerServiceDep = Depends(get_player_service)
RoomServiceDep = Depends(get_room_service)
