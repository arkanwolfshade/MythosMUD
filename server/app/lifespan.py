"""Application lifecycle management for MythosMUD server.

This module handles application startup and shutdown logic,
including the game tick loop and persistence layer initialization."""

import asyncio
import datetime
import logging
from contextlib import asynccontextmanager
from pathlib import Path

from fastapi import FastAPI

from ..database import init_db
from ..persistence import get_persistence
from ..realtime.connection_manager import ConnectionManager
from ..realtime.sse_handler import broadcast_game_event

# Global connection manager instance
connection_manager = ConnectionManager()
logger = logging.getLogger(__name__)
TICK_INTERVAL = 1.0  # seconds

# Ensure log directory exists
Path("logs").mkdir(exist_ok=True)


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Application lifespan manager.

    Handles startup and shutdown logic for the FastAPI application,
    including persistence layer initialization and game tick loop."""
    logger.info("Starting MythosMUD server...")
    await init_db()
    app.state.persistence = get_persistence()
    connection_manager.persistence = app.state.persistence

    # Start the game tick loop
    tick_task = asyncio.create_task(game_tick_loop(app))
    app.state.tick_task = tick_task
    logger.info("MythosMUD server started successfully")
    yield

    # Shutdown logic
    logger.info("Shutting down MythosMUD server...")
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
                "timestamp": datetime.datetime.utcnow().isoformat(),
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
