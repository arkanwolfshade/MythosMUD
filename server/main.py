"""
MythosMUD Server - Main Application Entry Point

This module serves as the primary entry point for the MythosMUD server,
providing FastAPI application setup, WebSocket handling, and real-time
game functionality. It integrates authentication, command handling, and
persistence layers into a cohesive gaming experience.

As noted in the Pnakotic Manuscripts, the proper organization of arcane
knowledge is essential for maintaining the delicate balance between order
and chaos in our digital realm.
"""

import asyncio
import datetime
import logging
import warnings
from contextlib import asynccontextmanager
from pathlib import Path

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import HTTPBearer
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request as StarletteRequest

from .api.game import game_router
from .api.players import player_router
from .api.real_time import realtime_router
from .api.rooms import room_router
from .auth.endpoints import auth_router
from .command_handler import router as command_router
from .config_loader import get_config
from .logging_config import get_logger, setup_logging
from .persistence import get_persistence
from .realtime.connection_manager import connection_manager
from .realtime.sse_handler import broadcast_game_event

# Suppress passlib deprecation warning about pkg_resources
warnings.filterwarnings("ignore", category=DeprecationWarning, module="passlib")


def setup_server_logging():
    """Setup logging configuration for the server."""
    # Get server log path from environment variable or use default
    import os

    server_log_path = os.environ.get("SERVER_LOG")
    if server_log_path:
        server_log_path = Path(server_log_path)
        # Create parent directory if it doesn't exist
        server_log_path.parent.mkdir(parents=True, exist_ok=True)
        # For rotation, use the parent directory of the server log path
        logs_dir = server_log_path.parent
    else:
        # Default to server/logs/server.log
        logs_dir = Path(__file__).parent / "logs"
        logs_dir.mkdir(exist_ok=True)
        server_log_path = logs_dir / "server.log"

    if server_log_path.exists():
        # Generate timestamp for the rotated log file
        timestamp = datetime.datetime.now().strftime("%Y_%m_%d_%H%M%S")
        rotated_log_path = logs_dir / f"server.log.{timestamp}"
        server_log_path.rename(rotated_log_path)


def _ensure_logging_initialized():
    """Ensure logging is initialized only once."""
    global _logging_initialized
    if not _logging_initialized:
        setup_logging()
        _logging_initialized = True


# Initialize logging
_logging_initialized = False
_ensure_logging_initialized()
logger = get_logger(__name__)

# Global variables for game state
game_tick_task: asyncio.Task | None = None
game_tick_interval = 1.0  # seconds


class ErrorLoggingMiddleware(BaseHTTPMiddleware):
    """Middleware to log all errors and exceptions."""

    async def dispatch(self, request: StarletteRequest, call_next):
        try:
            response = await call_next(request)
            return response
        except Exception as e:
            logger.error(f"Unhandled exception in {request.url.path}: {str(e)}", exc_info=True)
            # Re-raise the exception to maintain the error handling chain
            raise e


def get_tick_interval() -> float:
    """Get the game tick interval from configuration with validation."""
    config = get_config()
    tick_rate = config.get("game_tick_rate", 1.0)

    # Validate tick rate (must be positive and reasonable)
    if not isinstance(tick_rate, int | float) or tick_rate <= 0:
        logging.warning(f"Invalid game_tick_rate in config: {tick_rate}. Using default value of 1.0 seconds.")
        return 1.0

    if tick_rate > 60:  # Maximum 60 seconds between ticks
        logging.warning(f"Game tick rate too high: {tick_rate}. Using maximum value of 60.0 seconds.")
        return 60.0

    logging.info(f"Game tick rate configured: {tick_rate} seconds")
    return float(tick_rate)


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup logic
    app.state.persistence = get_persistence()
    # Set persistence reference in connection manager
    connection_manager.persistence = app.state.persistence
    asyncio.create_task(game_tick_loop(app))
    yield

    # Shutdown
    logger.info("Shutting down MythosMUD Server...")

    if game_tick_task:
        game_tick_task.cancel()
        try:
            await game_tick_task
        except asyncio.CancelledError:
            pass
        logger.info("Game tick loop stopped")


# Create FastAPI app
app = FastAPI(
    title="MythosMUD API",
    description=("A Cthulhu Mythos-themed MUD game API with real-time communication"),
    version="0.1.0",
    lifespan=lifespan,
)

# Add error logging middleware
app.add_middleware(ErrorLoggingMiddleware)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Configure appropriately for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(auth_router)
app.include_router(command_router)
app.include_router(player_router)
app.include_router(game_router)
app.include_router(room_router)
app.include_router(realtime_router)

# Security
security = HTTPBearer()


async def game_tick_loop(app: FastAPI = None):
    """Main game loop that runs every tick interval."""
    tick_count = 0
    # Cache the tick interval to avoid repeated logging
    tick_interval = get_tick_interval()

    while True:
        try:
            # TODO: Implement status/effect ticks using persistence layer
            logger.info(f"Game tick {tick_count}!")

            # Broadcast game tick to all connected players
            tick_data = {
                "tick_number": tick_count,
                "timestamp": datetime.datetime.utcnow().isoformat(),
                "active_players": len(connection_manager.player_websockets),
            }
            await broadcast_game_event("game_tick", tick_data)

            tick_count += 1
            await asyncio.sleep(tick_interval)
        except asyncio.CancelledError:
            break
        except Exception as e:
            logger.error(f"Error in game tick loop: {e}")


@app.get("/")
async def root():
    """Root endpoint providing basic server information."""
    return {"message": "Welcome to MythosMUD!"}


# All endpoints migrated to modular API structure:
# - Player endpoints: api/players.py
# - Game endpoints: api/game.py
# - Room endpoints: api/rooms.py
# - Real-time endpoints: api/real_time.py


if __name__ == "__main__":
    import uvicorn

    config = get_config()
    uvicorn.run(
        "main:app",
        host=config["host"],
        port=config["port"],
        reload=True,
    )
