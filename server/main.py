import asyncio
import datetime
import logging
from contextlib import asynccontextmanager
from pathlib import Path

# Fix bcrypt warning by monkey patching before importing passlib
try:
    import bcrypt

    if not hasattr(bcrypt, "__about__"):
        bcrypt.__about__ = type("About", (), {"__version__": "4.3.0"})()

except ImportError:
    pass

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import HTTPBearer

from .api.game import game_router
from .api.players import player_router
from .api.real_time import realtime_router
from .api.rooms import room_router
from .auth.endpoints import auth_router
from .command_handler import router as command_router
from .persistence import get_persistence
from .realtime.connection_manager import connection_manager
from .realtime.sse_handler import broadcast_game_event


# Configure logging
def setup_logging():
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

        # Rename the existing log file
        try:
            server_log_path.rename(rotated_log_path)
            print(f"Rotated log file: {rotated_log_path}")
        except Exception as e:
            print(f"Warning: Could not rotate log file: {e}")

    # Configure logging
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        handlers=[
            logging.FileHandler(server_log_path),
            logging.StreamHandler(),  # Also log to console
        ],
    )

    # Also configure uvicorn logging to go to our file
    uvicorn_logger = logging.getLogger("uvicorn")
    uvicorn_logger.handlers = []
    uvicorn_logger.addHandler(logging.FileHandler(server_log_path))
    uvicorn_logger.addHandler(logging.StreamHandler())
    uvicorn_logger.setLevel(logging.INFO)

    # Configure access logger
    access_logger = logging.getLogger("uvicorn.access")
    access_logger.handlers = []
    access_logger.addHandler(logging.FileHandler(server_log_path))
    access_logger.addHandler(logging.StreamHandler())
    access_logger.setLevel(logging.INFO)


# Setup logging
setup_logging()


TICK_INTERVAL = 1.0  # seconds

# Security scheme for WebSocket authentication
bearer_scheme = HTTPBearer(auto_error=False)


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup logic
    app.state.persistence = get_persistence()
    # Set persistence reference in connection manager
    connection_manager.persistence = app.state.persistence
    asyncio.create_task(game_tick_loop(app))
    yield
    # (Optional) Add shutdown logic here


app = FastAPI(
    title="MythosMUD API",
    description="A Cthulhu Mythos-themed MUD game API with real-time communication",
    version="0.1.0",
    lifespan=lifespan,
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://127.0.0.1:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router)
app.include_router(command_router)
app.include_router(player_router)
app.include_router(game_router)
app.include_router(room_router)
app.include_router(realtime_router)


async def game_tick_loop(app: FastAPI):
    tick_count = 0
    while True:
        # TODO: Implement status/effect ticks using persistence layer
        logging.info(f"Game tick {tick_count}!")

        # Broadcast game tick to all connected players
        tick_data = {
            "tick_number": tick_count,
            "timestamp": datetime.datetime.utcnow().isoformat(),
            "active_players": len(connection_manager.player_websockets),
        }
        await broadcast_game_event("game_tick", tick_data)

        tick_count += 1
        await asyncio.sleep(TICK_INTERVAL)


@app.get("/")
def read_root():
    return {"message": "Welcome to MythosMUD!"}


# All endpoints migrated to modular API structure:
# - Player endpoints: api/players.py
# - Game endpoints: api/game.py
# - Room endpoints: api/rooms.py
# - Real-time endpoints: api/real_time.py
