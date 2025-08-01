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
import uuid
import warnings
from contextlib import asynccontextmanager

from fastapi import Depends, FastAPI, HTTPException, WebSocket
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse
from fastapi.security import HTTPBearer

from .auth.endpoints import auth_router
from .auth.users import get_current_user
from .command_handler import router as command_router
from .config_loader import get_config
from .models.player import Player
from .persistence import get_persistence
from .real_time import (
    broadcast_game_tick,
    connection_manager,
    game_event_stream,
    websocket_endpoint,
)
from .schemas.player import PlayerRead

# Suppress passlib deprecation warning about pkg_resources
warnings.filterwarnings("ignore", category=DeprecationWarning, module="passlib")

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger(__name__)

# Global variables for game state
game_tick_task: asyncio.Task | None = None
game_tick_interval = 1.0  # seconds


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Manage application lifespan events."""
    global game_tick_task

    # Startup
    logger.info("Starting MythosMUD Server...")

    # Start game tick loop
    game_tick_task = asyncio.create_task(game_tick_loop())
    logger.info("Game tick loop started")

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
    title="MythosMUD Server",
    description="A Cthulhu Mythos-themed MUD server",
    version="1.0.0",
    lifespan=lifespan,
)

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
app.include_router(command_router, prefix="/game", tags=["game"])

# Security
security = HTTPBearer()


async def game_tick_loop():
    """Main game loop that runs every tick interval."""
    while True:
        try:
            await asyncio.sleep(game_tick_interval)
            await broadcast_game_tick()
        except asyncio.CancelledError:
            break
        except Exception as e:
            logger.error(f"Error in game tick loop: {e}")


@app.get("/")
async def root():
    """Root endpoint providing basic server information."""
    return {
        "message": "Welcome to MythosMUD Server",
        "version": "1.0.0",
        "status": "running",
        "timestamp": datetime.datetime.now().isoformat(),
    }


@app.get("/game/status")
async def game_status():
    """Get current game status and statistics."""
    return {
        "status": "running",
        "connected_players": len(connection_manager.active_connections),
        "game_tick_interval": game_tick_interval,
        "timestamp": datetime.datetime.now().isoformat(),
    }


@app.websocket("/ws/{player_id}")
async def websocket_handler(websocket: WebSocket, player_id: str):
    """Handle WebSocket connections for real-time game communication."""
    await websocket_endpoint(websocket, player_id)


@app.get("/game/events")
async def game_events():
    """Server-Sent Events endpoint for game events."""
    return StreamingResponse(
        game_event_stream(),
        media_type="text/event-stream",
        headers={
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
            "Access-Control-Allow-Origin": "*",
        },
    )


@app.get("/game/players/{player_id}", response_model=PlayerRead)
async def get_player(
    player_id: str,
    current_user=Depends(get_current_user),
    persistence=Depends(get_persistence),
):
    """Get player information by ID."""
    try:
        player = await persistence.get_player(player_id)
        if not player:
            raise HTTPException(status_code=404, detail="Player not found")
        return PlayerRead.from_orm(player)
    except Exception as e:
        logger.error(f"Error retrieving player {player_id}: {e}")
        raise HTTPException(status_code=500, detail="Internal server error") from e


@app.post("/game/players", response_model=PlayerRead)
async def create_player(
    player_data: dict,
    current_user=Depends(get_current_user),
    persistence=Depends(get_persistence),
):
    """Create a new player character."""
    try:
        player = Player(
            id=str(uuid.uuid4()),
            user_id=current_user.id,
            name=player_data.get("name", "Unknown"),
            level=player_data.get("level", 1),
            experience=player_data.get("experience", 0),
            health=player_data.get("health", 100),
            max_health=player_data.get("max_health", 100),
            mana=player_data.get("mana", 50),
            max_mana=player_data.get("max_mana", 50),
            room_id=player_data.get("room_id", "arkham_001"),
        )

        await persistence.create_player(player)
        return PlayerRead.from_orm(player)
    except Exception as e:
        logger.error(f"Error creating player: {e}")
        raise HTTPException(status_code=500, detail="Internal server error") from e


if __name__ == "__main__":
    import uvicorn

    config = get_config()
    uvicorn.run(
        "main:app",
        host=config["host"],
        port=config["port"],
        reload=True,
    )
