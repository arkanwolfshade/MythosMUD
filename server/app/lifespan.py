"""Application lifecycle management for MythosMUD server.

This module handles application startup and shutdown logic,
including the game tick loop and persistence layer initialization."""

import asyncio
import datetime
from contextlib import asynccontextmanager

from fastapi import FastAPI

from ..config_loader import get_config
from ..database import init_db
from ..logging_config import get_logger
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
    # Initialize real-time event handler first to obtain its EventBus
    app.state.event_handler = get_real_time_event_handler()
    # Ensure the event handler has access to the connection manager
    app.state.event_handler.connection_manager = connection_manager

    # Make EventBus available directly on app.state for easier access
    app.state.event_bus = app.state.event_handler.event_bus

    # Initialize persistence with the same EventBus so Rooms publish to it
    app.state.persistence = get_persistence(event_bus=app.state.event_handler.event_bus)
    connection_manager.persistence = app.state.persistence
    # Ensure connection manager exposes the same EventBus for command handlers
    connection_manager._event_bus = app.state.event_handler.event_bus

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
                logger.warning("Failed to connect to NATS server - falling back to direct WebSocket broadcasting")
                app.state.nats_service = None
                app.state.nats_message_handler = None
        except Exception as e:
            logger.error("Error initializing NATS service", error=str(e))
            logger.info("Falling back to direct WebSocket broadcasting for chat messages")
            app.state.nats_service = None
            app.state.nats_message_handler = None
    else:
        logger.info("NATS service disabled - using direct WebSocket broadcasting for chat messages")
        app.state.nats_service = None
        app.state.nats_message_handler = None

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

    if hasattr(app.state, "tick_task"):
        app.state.tick_task.cancel()
        try:
            await app.state.tick_task
        except asyncio.CancelledError:
            pass
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
