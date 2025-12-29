"""Application lifecycle management for MythosMUD server.

This module handles application startup and shutdown orchestration,
using ApplicationContainer for dependency injection and service lifecycle management.

ARCHITECTURE:
This module orchestrates startup and shutdown by delegating to specialized modules:
- lifespan_startup.py: All startup initialization functions
- lifespan_shutdown.py: All shutdown logic
- game_tick_processing.py: Game tick loop and processing functions
"""

import asyncio
from contextlib import asynccontextmanager

from fastapi import FastAPI

from ..container import ApplicationContainer
from ..structured_logging.enhanced_logging_config import get_logger, update_logging_with_player_service
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


@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Application lifespan manager.

    Handles startup and shutdown logic using ApplicationContainer for
    dependency injection and service lifecycle management.

    ARCHITECTURE:
    - Uses ApplicationContainer to manage all service dependencies
    - Services accessed via container instead of scattered app.state attributes
    - Proper initialization order handled by container
    - Clean separation of concerns
    - Delegates to specialized modules for startup, shutdown, and tick processing
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
    assert container.event_bus is not None, "EventBus must be initialized"
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
    assert container.task_registry is not None, "TaskRegistry must be initialized"
    tick_task = container.task_registry.register_task(game_tick_loop(app), "lifecycle/game_tick_loop", "lifecycle")
    app.state.tick_task = tick_task
    logger.info("MythosMUD server started successfully with ApplicationContainer")
    yield

    logger.info("Shutting down MythosMUD server...")

    try:
        await shutdown_services(app, container)

    except (asyncio.CancelledError, KeyboardInterrupt) as e:
        logger.warning("Shutdown interrupted", error=str(e), error_type=type(e).__name__)
        # Try to persist mythos state before cleanup
        try:
            chronicle = get_mythos_chronicle()
            chronicle.freeze()
            logger.info("Mythos chronicle state persisted during interrupted shutdown")
        except (AttributeError, KeyError, TypeError, ValueError, RuntimeError):
            logger.warning("Failed to persist mythos chronicle state during interrupted shutdown")
        # Still try to cleanup container
        try:
            await container.shutdown()
        except (AttributeError, KeyError, TypeError, ValueError, RuntimeError):
            pass
        raise
    except (AttributeError, KeyError, TypeError, ValueError, RuntimeError) as e:
        logger.error("Critical shutdown failure", error=str(e), error_type=type(e).__name__, exc_info=True)
        # Try to persist mythos state before cleanup
        try:
            chronicle = get_mythos_chronicle()
            chronicle.freeze()
            logger.info("Mythos chronicle state persisted during error shutdown")
        except (AttributeError, KeyError, TypeError, ValueError, RuntimeError):
            logger.warning("Failed to persist mythos chronicle state during error shutdown")
        # Still try to cleanup container
        try:
            await container.shutdown()
        except (AttributeError, KeyError, TypeError, ValueError, RuntimeError):
            pass

    logger.info("MythosMUD server shutdown complete")
