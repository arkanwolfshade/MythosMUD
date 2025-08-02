import asyncio
import datetime
import logging
import uuid
from contextlib import asynccontextmanager
from pathlib import Path

# Fix bcrypt warning by monkey patching before importing passlib
try:
    import bcrypt

    if not hasattr(bcrypt, "__about__"):
        bcrypt.__about__ = type("About", (), {"__version__": "4.3.0"})()

except ImportError:
    pass

from fastapi import Depends, FastAPI, HTTPException, Request, WebSocket
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse
from fastapi.security import HTTPBearer

from .auth.endpoints import auth_router
from .auth.users import get_current_user
from .command_handler import router as command_router
from .models.player import Player
from .persistence import get_persistence
from .realtime.connection_manager import connection_manager
from .realtime.sse_handler import broadcast_game_event, game_event_stream
from .realtime.websocket_handler import handle_websocket_connection
from .schemas.player import PlayerRead


# Configure logging
def setup_logging():
    """Setup logging configuration for the server."""
    # Create logs directory if it doesn't exist
    # Use server directory for logs, not project root
    logs_dir = Path(__file__).parent / "logs"
    logs_dir.mkdir(exist_ok=True)

    # Rotate existing server.log if it exists
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


# Real-time communication endpoints
@app.get("/events/{player_id}")
async def game_events_stream(player_id: str, request: Request):
    """
    Server-Sent Events stream for real-time game updates.

    This endpoint provides a persistent connection for receiving game state updates,
    room changes, combat events, and other real-time information.

    Authentication is handled via JWT token in query parameter or Authorization header.
    The player_id parameter should be the player name, not the UUID.
    """
    # Extract token from query parameter or Authorization header
    token = request.query_params.get("token")
    if not token:
        auth_header = request.headers.get("Authorization")
        if auth_header and auth_header.startswith("Bearer "):
            token = auth_header[7:]  # Remove "Bearer " prefix

    if not token:
        raise HTTPException(status_code=401, detail="Authentication token required")

    # Validate the token and get user information
    try:
        # TODO: Implement SSE token validation for new auth system
        user_info = {"user_id": "test_user"}  # Placeholder
        authenticated_username = user_info["username"]
    except HTTPException:
        raise
    except Exception:
        raise HTTPException(status_code=401, detail="Invalid authentication token") from None

    # Verify the authenticated user matches the requested player
    # Get the player from persistence to check if the player_id matches
    persistence = request.app.state.persistence
    player = persistence.get_player_by_name(authenticated_username)
    if not player:
        raise HTTPException(status_code=404, detail="Player not found in database")

    # Compare the authenticated username with the requested player_id (which should be the player name)
    if authenticated_username != player_id:
        raise HTTPException(status_code=403, detail="Access denied: token does not match player ID")

    # Get security headers for SSE
    # TODO: Implement SSE auth headers for new auth system
    security_headers = {}  # Placeholder

    return StreamingResponse(
        game_event_stream(player_id),
        media_type="text/event-stream",
        headers={
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Headers": "Cache-Control",
            **security_headers,
        },
    )


@app.websocket("/ws/{player_id}")
async def websocket_endpoint_route(websocket: WebSocket, player_id: str):
    """
    WebSocket endpoint for interactive commands and chat.

    This endpoint handles bidirectional communication for:
    - Game commands (look, go, attack, etc.)
    - Chat messages
    - Real-time interactions

    Authentication is handled via JWT token in query parameter.
    The player_id parameter should be the player name, not the UUID.
    """
    # Extract token from query parameter
    token = websocket.query_params.get("token")
    if not token:
        await websocket.close(code=4001, reason="Authentication token required")
        return

    # Validate the token
    try:
        # TODO: Implement SSE token validation for new auth system
        user_info = {"user_id": "test_user"}  # Placeholder
        authenticated_username = user_info["username"]
    except Exception:
        await websocket.close(code=4001, reason="Invalid authentication token")
        return

    # Verify the authenticated user matches the requested player
    # Get the player from persistence to check if the player_id matches
    from .persistence import get_persistence

    persistence = get_persistence()
    player = persistence.get_player_by_name(authenticated_username)
    if not player:
        await websocket.close(code=4004, reason="Player not found in database")
        return

    # Compare the authenticated username with the requested player_id (which should be the player name)
    if authenticated_username != player_id:
        await websocket.close(code=4003, reason="Access denied: token does not match player ID")
        return

    # Proceed with the WebSocket connection
    await handle_websocket_connection(websocket, player_id)


@app.get("/rooms/{room_id}")
def get_room(room_id: str):
    room = app.state.persistence.get_room(room_id)
    if not room:
        return {"error": "Room not found"}
    return room


# Player management endpoints
@app.post("/players", response_model=PlayerRead)
def create_player(name: str, starting_room_id: str = "arkham_001", current_user: dict = Depends(get_current_user)):
    """Create a new player character."""
    existing_player = app.state.persistence.get_player_by_name(name)
    if existing_player:
        raise HTTPException(status_code=400, detail="Player name already exists")
    # For now, create a temporary user_id - in a real app this would come from authentication
    temp_user_id = uuid.uuid4()
    current_time = datetime.datetime.now()
    player = Player(
        player_id=uuid.uuid4(),
        user_id=temp_user_id,
        name=name,
        current_room_id=starting_room_id,
        experience_points=0,
        level=1,
        created_at=current_time,
        last_active=current_time,
    )
    app.state.persistence.save_player(player)

    # Convert Player model to PlayerRead schema format
    return PlayerRead(
        id=player.player_id,
        user_id=player.user_id,
        name=player.name,
        current_room_id=player.current_room_id,
        experience_points=player.experience_points,
        level=player.level,
        stats=player.get_stats(),
        inventory=player.get_inventory(),
        status_effects=player.get_status_effects(),
        created_at=player.created_at,
        last_active=player.last_active,
    )


@app.get("/players", response_model=list[PlayerRead])
def list_players(current_user: dict = Depends(get_current_user)):
    """Get a list of all players."""
    players = app.state.persistence.list_players()
    result = []
    for player in players:
        if hasattr(player, "player_id"):  # Player object
            result.append(
                PlayerRead(
                    id=player.player_id,
                    user_id=player.user_id,
                    name=player.name,
                    current_room_id=player.current_room_id,
                    experience_points=player.experience_points,
                    level=player.level,
                    stats=player.get_stats(),
                    inventory=player.get_inventory(),
                    status_effects=player.get_status_effects(),
                    created_at=player.created_at,
                    last_active=player.last_active,
                )
            )
        else:  # Dictionary
            result.append(
                PlayerRead(
                    id=player["player_id"],
                    user_id=player["user_id"],
                    name=player["name"],
                    current_room_id=player["current_room_id"],
                    experience_points=player["experience_points"],
                    level=player["level"],
                    stats=player["stats"],
                    inventory=player["inventory"],
                    status_effects=player["status_effects"],
                    created_at=player["created_at"],
                    last_active=player["last_active"],
                )
            )
    return result


@app.get("/players/{player_id}", response_model=PlayerRead)
def get_player(player_id: str, current_user: dict = Depends(get_current_user)):
    """Get a specific player by ID."""
    player = app.state.persistence.get_player(player_id)
    if not player:
        raise HTTPException(status_code=404, detail="Player not found")

    if hasattr(player, "player_id"):  # Player object
        return PlayerRead(
            id=player.player_id,
            user_id=player.user_id,
            name=player.name,
            current_room_id=player.current_room_id,
            experience_points=player.experience_points,
            level=player.level,
            stats=player.get_stats(),
            inventory=player.get_inventory(),
            status_effects=player.get_status_effects(),
            created_at=player.created_at,
            last_active=player.last_active,
        )
    else:  # Dictionary
        return PlayerRead(
            id=player["player_id"],
            user_id=player["user_id"],
            name=player["name"],
            current_room_id=player["current_room_id"],
            experience_points=player["experience_points"],
            level=player["level"],
            stats=player["stats"],
            inventory=player["inventory"],
            status_effects=player["status_effects"],
            created_at=player["created_at"],
            last_active=player["last_active"],
        )


@app.get("/players/name/{player_name}", response_model=PlayerRead)
def get_player_by_name(player_name: str, current_user: dict = Depends(get_current_user)):
    """Get a specific player by name."""
    player = app.state.persistence.get_player_by_name(player_name)
    if not player:
        raise HTTPException(status_code=404, detail="Player not found")

    if hasattr(player, "player_id"):  # Player object
        return PlayerRead(
            id=player.player_id,
            user_id=player.user_id,
            name=player.name,
            current_room_id=player.current_room_id,
            experience_points=player.experience_points,
            level=player.level,
            stats=player.get_stats(),
            inventory=player.get_inventory(),
            status_effects=player.get_status_effects(),
            created_at=player.created_at,
            last_active=player.last_active,
        )
    else:  # Dictionary
        return PlayerRead(
            id=player["player_id"],
            user_id=player["user_id"],
            name=player["name"],
            current_room_id=player["current_room_id"],
            experience_points=player["experience_points"],
            level=player["level"],
            stats=player["stats"],
            inventory=player["inventory"],
            status_effects=player["status_effects"],
            created_at=player["created_at"],
            last_active=player["last_active"],
        )


@app.delete("/players/{player_id}")
def delete_player(player_id: str, current_user: dict = Depends(get_current_user)):
    """Delete a player character."""
    player = app.state.persistence.get_player(player_id)
    if not player:
        raise HTTPException(status_code=404, detail="Player not found")

    # Delete the player from the database
    success = app.state.persistence.delete_player(player_id)
    if not success:
        raise HTTPException(status_code=500, detail="Failed to delete player")

    # Delete player aliases if they exist
    from .alias_storage import AliasStorage

    alias_storage = AliasStorage()
    alias_storage.delete_player_aliases(player.name)

    return {"message": f"Player {player.name} has been deleted"}


# Player stats and effects endpoints
@app.post("/players/{player_id}/sanity-loss")
def apply_sanity_loss(
    player_id: str, amount: int, source: str = "unknown", current_user: dict = Depends(get_current_user)
):
    """Apply sanity loss to a player."""
    player = app.state.persistence.get_player(player_id)
    if not player:
        raise HTTPException(status_code=404, detail="Player not found")

    app.state.persistence.apply_sanity_loss(player, amount, source)
    return {"message": f"Applied {amount} sanity loss to {player.name}"}


@app.post("/players/{player_id}/fear")
def apply_fear(player_id: str, amount: int, source: str = "unknown", current_user: dict = Depends(get_current_user)):
    """Apply fear to a player."""
    player = app.state.persistence.get_player(player_id)
    if not player:
        raise HTTPException(status_code=404, detail="Player not found")

    app.state.persistence.apply_fear(player, amount, source)
    return {"message": f"Applied {amount} fear to {player.name}"}


@app.post("/players/{player_id}/corruption")
def apply_corruption(
    player_id: str, amount: int, source: str = "unknown", current_user: dict = Depends(get_current_user)
):
    """Apply corruption to a player."""
    player = app.state.persistence.get_player(player_id)
    if not player:
        raise HTTPException(status_code=404, detail="Player not found")

    app.state.persistence.apply_corruption(player, amount, source)
    return {"message": f"Applied {amount} corruption to {player.name}"}


@app.post("/players/{player_id}/occult-knowledge")
def gain_occult_knowledge(
    player_id: str, amount: int, source: str = "unknown", current_user: dict = Depends(get_current_user)
):
    """Gain occult knowledge (with sanity loss)."""
    player = app.state.persistence.get_player(player_id)
    if not player:
        raise HTTPException(status_code=404, detail="Player not found")

    app.state.persistence.gain_occult_knowledge(player, amount, source)
    return {"message": f"Gained {amount} occult knowledge for {player.name}"}


@app.post("/players/{player_id}/heal")
def heal_player(player_id: str, amount: int, current_user: dict = Depends(get_current_user)):
    """Heal a player's health."""
    player = app.state.persistence.get_player(player_id)
    if not player:
        raise HTTPException(status_code=404, detail="Player not found")

    app.state.persistence.heal_player(player, amount)
    return {"message": f"Healed {player.name} for {amount} health"}


@app.post("/players/{player_id}/damage")
def damage_player(
    player_id: str, amount: int, damage_type: str = "physical", current_user: dict = Depends(get_current_user)
):
    """Damage a player's health."""
    player = app.state.persistence.get_player(player_id)
    if not player:
        raise HTTPException(status_code=404, detail="Player not found")

    app.state.persistence.damage_player(player, amount, damage_type)
    return {"message": f"Damaged {player.name} for {amount} {damage_type} damage"}


# Real-time game state endpoints
@app.get("/game/status")
def get_game_status():
    """Get current game status and connection information."""
    return {
        "active_connections": connection_manager.get_active_connection_count(),
        "active_players": len(connection_manager.player_websockets),
        "room_subscriptions": len(connection_manager.room_subscriptions),
        "server_time": datetime.datetime.utcnow().isoformat(),
    }


@app.post("/game/broadcast")
def broadcast_message(message: str, current_user: dict = Depends(get_current_user)):
    """Broadcast a message to all connected players (admin only)."""
    # TODO: Add admin role checking
    # For now, allow any authenticated user
    return {"message": f"Broadcast message: {message}"}
