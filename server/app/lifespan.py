"""Application lifecycle management for MythosMUD server.

This module handles application startup and shutdown orchestration,
using ApplicationContainer for dependency injection and service lifecycle management.

ARCHITECTURE:
This module orchestrates startup and shutdown by delegating to specialized modules:
- lifespan_startup.py: All startup initialization functions
- lifespan_shutdown.py: All shutdown logic
- game_tick_processing.py: Game tick loop and processing functions

This module also integrates enhanced logging and monitoring systems.
"""

import asyncio
from collections.abc import AsyncGenerator
from contextlib import asynccontextmanager
from typing import Any

from fastapi import FastAPI

from ..container import ApplicationContainer
from ..monitoring.exception_tracker import get_exception_tracker
from ..monitoring.monitoring_dashboard import get_monitoring_dashboard
from ..monitoring.performance_monitor import get_performance_monitor
from ..structured_logging.enhanced_logging_config import (
    get_logger,
    log_exception_once,
    update_logging_with_player_service,
)
from ..structured_logging.log_aggregator import get_log_aggregator
from ..time.time_service import get_mythos_chronicle
from .game_tick_processing import game_tick_loop, get_current_tick, reset_current_tick
from .lifespan_shutdown import shutdown_services
from .lifespan_startup import (
    initialize_chat_service,
    initialize_combat_services,
    initialize_container_and_legacy_services,
    initialize_magic_services,
    initialize_mythos_time_consumer,
    initialize_nats_and_combat_services,
    initialize_npc_services,
    initialize_npc_startup_spawning,
    setup_connection_manager,
)

logger = get_logger("server.lifespan")

# Re-export tick functions for backward compatibility
__all__ = ["lifespan", "get_current_tick", "reset_current_tick"]


async def _initialize_enhanced_systems() -> Any:
    """
    Initialize enhanced logging and monitoring systems.

    Returns:
        LogAggregator instance if successful

    Raises:
        Exception: If initialization fails
    """
    get_performance_monitor()
    get_exception_tracker()
    get_monitoring_dashboard()
    log_aggregator = get_log_aggregator()

    logger.info(
        "Enhanced logging and monitoring systems initialized",
        performance_monitoring=True,
        exception_tracking=True,
        log_aggregation=True,
        monitoring_dashboard=True,
    )
    return log_aggregator


async def _startup_application(app: FastAPI) -> ApplicationContainer:
    """
    Perform application startup and return initialized container.

    Args:
        app: FastAPI application instance

    Returns:
        Initialized ApplicationContainer

    Raises:
        RuntimeError: If required services are not initialized
    """
    logger.info("Starting MythosMUD server with ApplicationContainer...")

    container = ApplicationContainer()
    await container.initialize()
    await initialize_container_and_legacy_services(app, container)
    await setup_connection_manager(app, container)
    await initialize_npc_services(app, container)
    await initialize_combat_services(app, container)
    await initialize_mythos_time_consumer(app, container)
    await initialize_npc_startup_spawning(app)

    # Enhance logging system with PlayerGuidFormatter now that player service is available
    update_logging_with_player_service(container.player_service)
    logger.info("Logging system enhanced with PlayerGuidFormatter")

    # Set the main event loop for the EventBus to handle async event handlers
    if container.event_bus is None:
        raise RuntimeError("EventBus must be initialized")
    main_loop = asyncio.get_running_loop()
    container.event_bus.set_main_loop(main_loop)

    if container.mythos_tick_scheduler is not None:
        await container.mythos_tick_scheduler.start()
        app.state.mythos_tick_scheduler = container.mythos_tick_scheduler
        logger.info("Mythos tick scheduler running")

    logger.info("Real-time event handler initialized")

    await initialize_nats_and_combat_services(app, container)
    await initialize_chat_service(app, container)
    await initialize_magic_services(app, container)

    # Start the game tick loop using TaskRegistry from container
    if container.task_registry is None:
        raise RuntimeError("TaskRegistry must be initialized")
    tick_task = container.task_registry.register_task(game_tick_loop(app), "lifecycle/game_tick_loop", "lifecycle")
    app.state.tick_task = tick_task
    logger.info("MythosMUD server started successfully with ApplicationContainer")
    return container


async def _shutdown_with_error_handling(app: FastAPI, container: ApplicationContainer) -> None:
    """
    Perform application shutdown with comprehensive error handling.

    Args:
        app: FastAPI application instance
        container: ApplicationContainer instance
    """
    logger.info("Shutting down MythosMUD server...")

    try:
        await shutdown_services(app, container)
        logger.info("MythosMUD server shutdown complete")
    except (asyncio.CancelledError, KeyboardInterrupt) as e:
        logger.warning("Shutdown interrupted", error=str(e), error_type=type(e).__name__)
        _persist_mythos_state_on_error()
        await _cleanup_container_on_error(container)
        raise
    except (AttributeError, KeyError, TypeError, ValueError, RuntimeError) as e:
        logger.error("Critical shutdown failure", error=str(e), error_type=type(e).__name__, exc_info=True)
        _persist_mythos_state_on_error()
        await _cleanup_container_on_error(container)


def _persist_mythos_state_on_error() -> None:
    """Attempt to persist mythos chronicle state during error conditions."""
    try:
        chronicle = get_mythos_chronicle()
        chronicle.freeze()
        logger.info("Mythos chronicle state persisted during error shutdown")
    except (AttributeError, KeyError, TypeError, ValueError, RuntimeError):
        logger.warning("Failed to persist mythos chronicle state during error shutdown")


async def _cleanup_container_on_error(container: ApplicationContainer | None) -> None:
    """Attempt to cleanup container during error conditions."""
    if container is None:
        return
    try:
        await container.shutdown()
    except (AttributeError, KeyError, TypeError, ValueError, RuntimeError):
        pass


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None, None]:
    """
    Application lifespan manager with comprehensive monitoring and logging.

    Handles startup and shutdown logic using ApplicationContainer for
    dependency injection and service lifecycle management.

    This lifespan integrates:
    - Enhanced logging and monitoring systems
    - ApplicationContainer for service management
    - Game tick loop initialization
    - Proper resource cleanup on shutdown

    ARCHITECTURE:
    - Uses ApplicationContainer to manage all service dependencies
    - Services accessed via container instead of scattered app.state attributes
    - Proper initialization order handled by container
    - Clean separation of concerns
    - Delegates to specialized modules for startup, shutdown, and tick processing
    """
    # Initialize enhanced logging and monitoring systems first
    log_aggregator = None
    try:
        log_aggregator = await _initialize_enhanced_systems()
    except Exception as error:
        log_exception_once(
            logger,
            "error",
            "Failed to initialize enhanced systems",
            exc=error,
            lifespan_phase="startup",
            exc_info=True,
        )
        raise

    # Application startup
    container: ApplicationContainer | None = None
    try:
        container = await _startup_application(app)
        yield

        # Application shutdown
        await _shutdown_with_error_handling(app, container)

    except (asyncio.CancelledError, KeyboardInterrupt) as e:
        logger.warning("Startup interrupted", error=str(e), error_type=type(e).__name__)
        await _cleanup_container_on_error(container)
        raise
    except (AttributeError, KeyError, TypeError, ValueError, RuntimeError) as e:
        logger.error("Critical startup failure", error=str(e), error_type=type(e).__name__, exc_info=True)
        await _cleanup_container_on_error(container)
        raise
    finally:
        # Always cleanup enhanced systems, even if shutdown failed
        try:
            if log_aggregator is not None:
                log_aggregator.shutdown()
                logger.info("Enhanced systems shutdown complete")
        except Exception as error:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Lifespan cleanup must not fail, catch all errors
            log_exception_once(
                logger,
                "error",
                "Error during enhanced systems shutdown",
                exc=error,
                lifespan_phase="shutdown",
                exc_info=True,
            )
