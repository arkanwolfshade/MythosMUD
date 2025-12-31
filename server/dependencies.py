"""
Dependency injection providers for MythosMUD server.

This module provides dependency injection functions for services using the
ApplicationContainer pattern, following clean architecture principles and
ensuring proper separation of concerns.

ARCHITECTURE MIGRATION:
This file has been updated to use the ApplicationContainer for dependency injection
instead of directly accessing app.state. This provides better testability and
follows the dependency inversion principle.

As noted in the Pnakotic Manuscripts, proper organization of arcane knowledge
requires clear separation between the presentation layer and the underlying
mysteries. This dependency injection system provides that separation.
"""

from fastapi import Depends, Request

from .container import ApplicationContainer
from .game.player_service import PlayerService
from .game.room_service import RoomService
from .game.stats_generator import StatsGenerator
from .structured_logging.enhanced_logging_config import get_logger

logger = get_logger(__name__)


def get_container(request: Request) -> ApplicationContainer:
    """
    Get the application container from request state.

    This is the base dependency that all other dependencies use.

    Args:
        request: The FastAPI request object

    Returns:
        ApplicationContainer: The application container with all services

    AI: This is the root of the dependency injection tree.
        All other dependencies should use this to access services.
    """
    if not hasattr(request.app.state, "container"):
        raise RuntimeError(
            "ApplicationContainer not found in app.state - ensure container is initialized in lifespan context"
        )
    return request.app.state.container


def get_player_service(request: Request) -> PlayerService:
    """
    Get a PlayerService instance with dependency injection.

    This function provides a PlayerService instance from the container,
    ensuring proper dependency injection and avoiding global state.

    Args:
        request: The FastAPI request object containing app state

    Returns:
        PlayerService: A configured PlayerService instance

    AI: Migrated from app.state direct access to container-based injection.
        This enables proper testing and follows clean architecture principles.
    """
    logger.debug("Retrieving PlayerService from container")
    container = get_container(request)

    if container.player_service is None:
        raise RuntimeError("PlayerService not initialized in container")

    return container.player_service


def get_player_service_for_testing(player_service: PlayerService | None = None) -> PlayerService:
    """
    Get a PlayerService instance for testing purposes.

    This function allows tests to provide their own PlayerService instance
    or get a mock instance for testing.

    Args:
        player_service: Optional PlayerService instance (for test injection)

    Returns:
        PlayerService: A PlayerService instance for testing

    AI: This provides a test seam without requiring full app context.
        Tests can inject mock dependencies easily.
    """
    if player_service is not None:
        return player_service

    # Create a minimal mock for testing
    from unittest.mock import Mock

    mock_persistence = Mock()
    return PlayerService(mock_persistence)


def get_room_service(request: Request) -> RoomService:
    """
    Get a RoomService instance with dependency injection.

    This function provides a RoomService instance from the container,
    ensuring proper dependency injection and avoiding global state.

    Args:
        request: The FastAPI request object containing app state

    Returns:
        RoomService: A configured RoomService instance

    AI: Migrated from app.state direct access to container-based injection.
    """
    logger.debug("Retrieving RoomService from container")
    container = get_container(request)

    if container.room_service is None:
        raise RuntimeError("RoomService not initialized in container")

    return container.room_service


def get_stats_generator() -> StatsGenerator:
    """
    Get a StatsGenerator instance via dependency injection.

    StatsGenerator is stateless and can be safely reused across requests.

    Returns:
        StatsGenerator: A StatsGenerator instance
    """
    return StatsGenerator()


# Dependency injection type aliases for use in route handlers
ContainerDep = Depends(get_container)
PlayerServiceDep = Depends(get_player_service)
RoomServiceDep = Depends(get_room_service)
StatsGeneratorDep = Depends(get_stats_generator)
