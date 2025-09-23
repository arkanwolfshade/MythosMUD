"""Application lifecycle management for MythosMUD server.

This module handles application startup and shutdown logic,
including the game tick loop and persistence layer initialization."""

import asyncio
import datetime
from contextlib import asynccontextmanager
from pathlib import Path

from fastapi import FastAPI

from ..config_loader import get_config
from ..database import init_db
from ..logging_config import get_logger
from ..npc_database import init_npc_database
from ..persistence import get_persistence
from ..realtime.connection_manager import connection_manager
from ..realtime.event_handler import get_real_time_event_handler
from ..realtime.nats_message_handler import get_nats_message_handler
from ..realtime.sse_handler import broadcast_game_event
from ..services.nats_service import nats_service

logger = get_logger("server.lifespan")
TICK_INTERVAL = 1.0  # seconds

# Log directory creation is now handled by logging_config.py


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Application lifespan manager.

    Handles startup and shutdown logic for the FastAPI application,
    including persistence layer initialization and game tick loop."""
    logger.info("Starting MythosMUD server...")
    await init_db()
    await init_npc_database()
    # Initialize real-time event handler first to obtain its EventBus
    app.state.event_handler = get_real_time_event_handler()
    # Ensure the event handler has access to the connection manager
    app.state.event_handler.connection_manager = connection_manager

    # Make EventBus available directly on app.state for easier access
    app.state.event_bus = app.state.event_handler.event_bus

    # Make connection_manager available directly on app.state for command handlers
    app.state.connection_manager = connection_manager

    # Initialize persistence with the same EventBus so Rooms publish to it
    app.state.persistence = get_persistence(event_bus=app.state.event_handler.event_bus)
    connection_manager.persistence = app.state.persistence
    # Ensure connection manager exposes the same EventBus for command handlers
    connection_manager._event_bus = app.state.event_handler.event_bus
    # Give connection manager access to app for WebSocket command processing
    connection_manager.app = app

    # Initialize critical services and add to app.state
    from ..game.player_service import PlayerService
    from ..services.user_manager import UserManager

    app.state.player_service = PlayerService(app.state.persistence)

    # Initialize UserManager with proper data directory from config
    config = get_config()
    data_dir = config.get("data_dir", "data")
    user_management_dir = Path(data_dir) / "user_management"
    app.state.user_manager = UserManager(data_dir=user_management_dir)

    logger.info("Critical services (player_service, user_manager) added to app.state")
    logger.info(f"app.state.player_service: {app.state.player_service}")
    logger.info(f"app.state.user_manager: {app.state.user_manager}")

    # Initialize NPC services
    from ..npc.lifecycle_manager import NPCLifecycleManager
    from ..npc.population_control import NPCPopulationController
    from ..npc.spawning_service import NPCSpawningService
    from ..services.npc_instance_service import initialize_npc_instance_service

    # Create NPC services
    app.state.npc_population_controller = NPCPopulationController(app.state.event_bus)
    app.state.npc_spawning_service = NPCSpawningService(app.state.event_bus, app.state.npc_population_controller)
    app.state.npc_lifecycle_manager = NPCLifecycleManager(
        app.state.event_bus, app.state.npc_spawning_service, app.state.npc_population_controller
    )

    # Initialize the NPC instance service
    initialize_npc_instance_service(
        lifecycle_manager=app.state.npc_lifecycle_manager,
        spawning_service=app.state.npc_spawning_service,
        population_controller=app.state.npc_population_controller,
        event_bus=app.state.event_bus,
    )

    logger.info("NPC services initialized and added to app.state")

    # Enhance logging system with PlayerGuidFormatter now that player service is available
    from ..logging_config import update_logging_with_player_service

    update_logging_with_player_service(app.state.player_service)
    logger.info("Logging system enhanced with PlayerGuidFormatter")

    # Set the main event loop for the EventBus to handle async event handlers
    main_loop = asyncio.get_running_loop()
    app.state.event_handler.event_bus.set_main_loop(main_loop)

    logger.info("Real-time event handler initialized")

    # Initialize NATS service for real-time messaging
    config = get_config()
    nats_config = config.get("nats", {})

    if nats_config.get("enabled", False):
        logger.info("Initializing NATS service for real-time messaging")
        try:
            # Configure NATS service with config
            nats_service.config = nats_config

            # Connect to NATS server
            connected = await nats_service.connect()
            if connected:
                logger.info("NATS service connected successfully")
                app.state.nats_service = nats_service

                # Initialize NATS message handler
                try:
                    nats_message_handler = get_nats_message_handler(nats_service)
                    await nats_message_handler.start()
                    app.state.nats_message_handler = nats_message_handler
                    logger.info("NATS message handler started successfully")
                except Exception as e:
                    logger.error("Error initializing NATS message handler", error=str(e))
                    app.state.nats_message_handler = None
            else:
                logger.error("Failed to connect to NATS server - NATS is required for chat functionality")
                raise RuntimeError("NATS connection failed - NATS is mandatory for chat system")
        except Exception as e:
            logger.error("Error initializing NATS service", error=str(e))
            raise RuntimeError(f"NATS initialization failed: {str(e)} - NATS is mandatory for chat system") from e
    else:
        logger.error("NATS service disabled - NATS is mandatory for chat functionality")
        raise RuntimeError("NATS service is disabled - NATS is mandatory for chat system")

    # Initialize chat service and add to app.state (after NATS initialization)
    from ..game.chat_service import ChatService

    # Initialize chat service with required dependencies using proper dependency injection
    app.state.chat_service = ChatService(
        persistence=app.state.persistence,
        room_service=app.state.persistence,  # Persistence layer provides room service functionality
        player_service=app.state.player_service,
        nats_service=app.state.nats_service,  # Pass the properly configured NATS service
    )

    # Verify NATS service connection in chat service
    if app.state.chat_service.nats_service and app.state.chat_service.nats_service.is_connected():
        logger.info("Chat service NATS connection verified - NATS is connected and ready")
    else:
        logger.error("Chat service NATS connection failed - NATS is not connected")
        raise RuntimeError("Chat service NATS connection failed - NATS is mandatory for chat system")

    logger.info("Chat service added to app.state")
    logger.info(f"app.state.chat_service: {app.state.chat_service}")

    # Start the game tick loop
    tick_task = asyncio.create_task(game_tick_loop(app))
    app.state.tick_task = tick_task
    logger.info("MythosMUD server started successfully")
    yield

    # Shutdown logic
    logger.info("Shutting down MythosMUD server...")

    # Stop NATS message handler if running
    if hasattr(app.state, "nats_message_handler") and app.state.nats_message_handler:
        logger.info("Stopping NATS message handler")
        try:
            await app.state.nats_message_handler.stop()
            logger.info("NATS message handler stopped successfully")
        except Exception as e:
            logger.error("Error stopping NATS message handler", error=str(e))

    # Disconnect NATS service if connected
    if hasattr(app.state, "nats_service") and app.state.nats_service:
        logger.info("Disconnecting NATS service")
        try:
            await app.state.nats_service.disconnect()
            logger.info("NATS service disconnected successfully")
        except Exception as e:
            logger.error("Error disconnecting NATS service", error=str(e))

    # Cancel and await the game tick task
    if hasattr(app.state, "tick_task") and app.state.tick_task:
        logger.info("Cancelling game tick task")
        app.state.tick_task.cancel()
        try:
            await app.state.tick_task
        except asyncio.CancelledError:
            logger.info("Game tick task cancelled successfully")
        except Exception as e:
            logger.error(f"Error cancelling game tick task: {e}")

    # Clean up any remaining tasks in the connection manager
    if hasattr(app.state, "connection_manager") and app.state.connection_manager:
        logger.info("Cleaning up connection manager tasks")
        try:
            await app.state.connection_manager.force_cleanup()
        except Exception as e:
            logger.error(f"Error during connection manager cleanup: {e}")

    # Cancel any remaining tasks in the event loop
    try:
        # Get all running tasks and cancel them (except the current one)
        current_task = asyncio.current_task()
        tasks = [task for task in asyncio.all_tasks() if task is not current_task and not task.done()]

        if tasks:
            logger.info(f"Cancelling {len(tasks)} remaining tasks")
            for task in tasks:
                task.cancel()

            # Wait for all tasks to complete
            await asyncio.gather(*tasks, return_exceptions=True)
            logger.info("All remaining tasks cancelled successfully")
    except Exception as e:
        logger.error(f"Error during task cleanup: {e}")

    logger.info("MythosMUD server shutdown complete")


async def game_tick_loop(app: FastAPI):
    """Main game tick loop.

    This function runs continuously and handles periodic game updates,
    including broadcasting tick information to connected players."""
    tick_count = 0
    logger.info("Game tick loop started")

    while True:
        try:
            # TODO: Implement status/effect ticks using persistence layer
            logger.debug(f"Game tick {tick_count}")

            # Broadcast game tick to all connected players
            tick_data = {
                "tick_number": tick_count,
                "timestamp": datetime.datetime.now(datetime.UTC).isoformat(),
                "active_players": len(connection_manager.player_websockets),
            }
            await broadcast_game_event("game_tick", tick_data)
            tick_count += 1
            await asyncio.sleep(TICK_INTERVAL)
        except asyncio.CancelledError:
            logger.info("Game tick loop cancelled")
            break
        except Exception as e:
            logger.error(f"Error in game tick loop: {e}")
            await asyncio.sleep(TICK_INTERVAL)
