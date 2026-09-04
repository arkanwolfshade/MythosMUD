# FastAPI Integration Examples with Enhanced Logging
# This file demonstrates how to integrate enhanced logging with FastAPI applications

import time
import uuid

from fastapi import Depends, FastAPI, HTTPException, Request
from server.logging.enhanced_logging_config import bind_request_context, clear_request_context, get_logger

from server.monitoring.exception_tracker import track_exception
from server.monitoring.performance_monitor import measure_performance

# ✅ CORRECT - Enhanced logging import
logger = get_logger(__name__)

app = FastAPI()


# ✅ CORRECT - FastAPI middleware for request context
@app.middleware("http")
async def add_request_context(request: Request, call_next):
    """Add request context to all log entries using enhanced logging."""
    bind_request_context(
        correlation_id=str(uuid.uuid4()),
        user_id=getattr(request.state, "user_id", None),
        session_id=getattr(request.state, "session_id", None),
        request_id=str(request.url),
        method=request.method,
        path=request.url.path,
        client_host=getattr(request.client, "host", "unknown"),
    )

    try:
        response = await call_next(request)
        return response
    finally:
        clear_request_context()


# ✅ CORRECT - API request/response logging middleware
@app.middleware("http")
async def log_api_requests(request: Request, call_next):
    """Log API requests with performance metrics."""
    start_time = time.time()

    logger.info(
        "API request started",
        method=request.method,
        url=str(request.url),
        path=request.url.path,
        client_ip=request.client.host,
        user_agent=request.headers.get("user-agent"),
    )

    response = await call_next(request)
    duration = time.time() - start_time

    logger.info(
        "API request completed",
        method=request.method,
        url=str(request.url),
        status_code=response.status_code,
        duration_ms=duration * 1000,
        response_size=response.headers.get("content-length", 0),
    )

    return response


# ✅ CORRECT - FastAPI route handler with enhanced logging
@app.post("/api/players")
async def create_player(player_data: dict):
    """Create a new player with enhanced logging."""
    logger.info("Creating new player", player_name=player_data.get("name"), email=player_data.get("email"))

    try:
        with measure_performance("player_creation", player_name=player_data.get("name")):
            player = await player_service.create_player(player_data)

        logger.info("Player created successfully", player_id=player.id, player_name=player.name)
        return {"player_id": player.id, "status": "created"}
    except Exception as e:
        logger.error("Failed to create player", error=str(e), player_data=player_data)
        raise HTTPException(status_code=500, detail="Internal server error")


# ✅ CORRECT - FastAPI route with authentication logging
@app.get("/api/players/{player_id}")
async def get_player(player_id: str, current_user: dict = Depends(get_current_user)):
    """Get player information with enhanced logging."""
    logger.info("Retrieving player information", player_id=player_id, requesting_user=current_user.get("id"))

    try:
        player = await player_service.get_player(player_id)
        logger.info("Player information retrieved", player_id=player_id, player_name=player.name)
        return {"player": player.dict()}
    except Exception as e:
        logger.error("Failed to retrieve player", player_id=player_id, error=str(e))
        raise HTTPException(status_code=404, detail="Player not found")


# ✅ CORRECT - FastAPI dependency with enhanced logging
async def get_current_user(token: str = Depends(oauth2_scheme)) -> dict:
    """Get current user with enhanced logging."""
    logger.debug("Authenticating user", token_length=len(token))

    try:
        user = await auth_service.verify_token(token)
        logger.info("User authenticated successfully", user_id=user.id, username=user.username)
        return user
    except Exception as e:
        logger.error("Authentication failed", error=str(e), token_length=len(token))
        raise HTTPException(status_code=401, detail="Invalid authentication credentials")


# ✅ CORRECT - FastAPI exception handlers with enhanced logging
@app.exception_handler(HTTPException)
async def http_exception_handler(request: Request, exc: HTTPException):
    """Handle HTTP exceptions with enhanced logging."""
    logger.warning(
        "HTTP exception occurred",
        status_code=exc.status_code,
        detail=exc.detail,
        path=request.url.path,
        method=request.method,
    )
    return JSONResponse(status_code=exc.status_code, content={"detail": exc.detail})


@app.exception_handler(Exception)
async def general_exception_handler(request: Request, exc: Exception):
    """Handle general exceptions with enhanced logging."""
    logger.error(
        "Unhandled exception occurred",
        error_type=type(exc).__name__,
        error_message=str(exc),
        path=request.url.path,
        method=request.method,
        exc_info=True,
    )
    return JSONResponse(status_code=500, content={"detail": "Internal server error"})


# ✅ CORRECT - FastAPI WebSocket endpoint with enhanced logging
@app.websocket("/ws/{client_id}")
async def websocket_endpoint(websocket: WebSocket, client_id: str):
    """WebSocket endpoint with enhanced logging."""
    await websocket.accept()

    # Bind WebSocket context
    bind_request_context(
        correlation_id=str(uuid.uuid4()),
        connection_type="websocket",
        client_id=client_id,
        client_ip=websocket.client.host,
    )

    logger.info("WebSocket connection established", client_id=client_id, client_ip=websocket.client.host)

    try:
        while True:
            data = await websocket.receive_text()
            logger.debug("WebSocket message received", client_id=client_id, message_length=len(data))

            # Process message
            response = await process_websocket_message(data)
            await websocket.send_text(response)

            logger.debug("WebSocket message sent", client_id=client_id, response_length=len(response))
    except WebSocketDisconnect:
        logger.info("WebSocket disconnected", client_id=client_id, client_ip=websocket.client.host)
    except Exception as e:
        logger.error("WebSocket error", client_id=client_id, error=str(e))
    finally:
        clear_request_context()


# ✅ CORRECT - FastAPI background task with enhanced logging
@app.post("/api/players/{player_id}/update")
async def update_player_background(player_id: str, update_data: dict, background_tasks: BackgroundTasks):
    """Update player with background task and enhanced logging."""
    logger.info("Starting background player update", player_id=player_id, update_fields=list(update_data.keys()))

    background_tasks.add_task(update_player_background_task, player_id=player_id, update_data=update_data)

    return {"message": "Player update started", "player_id": player_id}


async def update_player_background_task(player_id: str, update_data: dict):
    """Background task for player update with enhanced logging."""
    bind_request_context(correlation_id=str(uuid.uuid4()), task_type="background_update", player_id=player_id)

    try:
        logger.info("Starting background player update", player_id=player_id)

        with measure_performance("background_player_update", player_id=player_id):
            await player_service.update_player(player_id, update_data)

        logger.info("Background player update completed", player_id=player_id)
    except Exception as e:
        logger.error("Background player update failed", player_id=player_id, error=str(e))
        track_exception(e, player_id=player_id, task_type="background_update")
    finally:
        clear_request_context()


# ✅ CORRECT - FastAPI route with database logging
@app.get("/api/players")
async def list_players(skip: int = 0, limit: int = 100):
    """List players with enhanced database logging."""
    logger.info("Listing players", skip=skip, limit=limit)

    start_time = time.time()
    try:
        with measure_performance("player_list_query", skip=skip, limit=limit):
            players = await player_service.list_players(skip=skip, limit=limit)

        duration = time.time() - start_time
        logger.info(
            "Players listed successfully", skip=skip, limit=limit, count=len(players), duration_ms=duration * 1000
        )
        return {"players": [player.dict() for player in players], "count": len(players)}
    except Exception as e:
        duration = time.time() - start_time
        logger.error("Failed to list players", skip=skip, limit=limit, error=str(e), duration_ms=duration * 1000)
        raise HTTPException(status_code=500, detail="Internal server error")


# ✅ CORRECT - FastAPI route with file upload logging
@app.post("/api/players/{player_id}/avatar")
async def upload_avatar(player_id: str, file: UploadFile = File(...)):
    """Upload player avatar with enhanced logging."""
    logger.info("Uploading player avatar", player_id=player_id, filename=file.filename, content_type=file.content_type)

    try:
        with measure_performance("avatar_upload", player_id=player_id, filename=file.filename):
            avatar_url = await player_service.upload_avatar(player_id, file)

        logger.info("Player avatar uploaded successfully", player_id=player_id, avatar_url=avatar_url)
        return {"avatar_url": avatar_url}
    except Exception as e:
        logger.error("Failed to upload player avatar", player_id=player_id, filename=file.filename, error=str(e))
        raise HTTPException(status_code=500, detail="Failed to upload avatar")


# Helper functions for examples
async def player_service():
    """Simulate player service."""
    pass


async def auth_service():
    """Simulate auth service."""
    pass


async def process_websocket_message(data: str) -> str:
    """Simulate WebSocket message processing."""
    return f"Processed: {data}"


# Simulate services
class player_service:
    @staticmethod
    async def create_player(player_data: dict):
        class Player:
            id = "player123"
            name = player_data.get("name")

        return Player()

    @staticmethod
    async def get_player(player_id: str):
        class Player:
            id = player_id
            name = "Test Player"

            def dict(self):
                return {"id": self.id, "name": self.name}

        return Player()

    @staticmethod
    async def list_players(skip: int = 0, limit: int = 100):
        class Player:
            id = "player123"
            name = "Test Player"

            def dict(self):
                return {"id": self.id, "name": self.name}

        return [Player()]

    @staticmethod
    async def update_player(player_id: str, update_data: dict):
        pass

    @staticmethod
    async def upload_avatar(player_id: str, file):
        return f"https://example.com/avatars/{player_id}.jpg"


class auth_service:
    @staticmethod
    async def verify_token(token: str):
        class User:
            id = "user123"
            username = "testuser"

        return User()


# Simulate FastAPI components
class oauth2_scheme:
    pass


class JSONResponse:
    def __init__(self, status_code: int, content: dict):
        self.status_code = status_code
        self.content = content


class WebSocket:
    async def accept(self):
        pass

    async def receive_text(self):
        return "test message"

    async def send_text(self, text: str):
        pass

    @property
    def client(self):
        class Client:
            host = "192.168.1.1"

        return Client()


class WebSocketDisconnect(Exception):
    pass


class BackgroundTasks:
    def add_task(self, func, **kwargs):
        pass


class File:
    def __init__(self, **kwargs):
        self.filename = "test.jpg"
        self.content_type = "image/jpeg"


class UploadFile:
    def __init__(self, **kwargs):
        self.filename = "test.jpg"
        self.content_type = "image/jpeg"
