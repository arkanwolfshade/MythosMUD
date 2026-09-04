# WebSocket Integration Examples with Enhanced Logging
# This file demonstrates how to integrate enhanced logging with WebSocket connections

import asyncio
import time
import uuid

from server.logging.enhanced_logging_config import bind_request_context, clear_request_context, get_logger

from server.monitoring.exception_tracker import track_exception
from server.monitoring.performance_monitor import measure_performance

# ✅ CORRECT - Enhanced logging import
logger = get_logger(__name__)


# ✅ CORRECT - WebSocket connection management with enhanced logging
class WebSocketManager:
    """WebSocket connection manager with enhanced logging."""

    def __init__(self):
        self.connections = {}
        logger.info("WebSocket manager initialized")

    async def connect(self, websocket, client_id: str):
        """Establish WebSocket connection with enhanced logging."""
        await websocket.accept()

        # Bind WebSocket context
        bind_request_context(
            correlation_id=str(uuid.uuid4()),
            connection_type="websocket",
            client_id=client_id,
            client_ip=websocket.client.host,
        )

        self.connections[client_id] = websocket
        logger.info(
            "WebSocket connection established",
            client_id=client_id,
            client_ip=websocket.client.host,
            total_connections=len(self.connections),
        )

    async def disconnect(self, client_id: str):
        """Disconnect WebSocket with enhanced logging."""
        if client_id in self.connections:
            del self.connections[client_id]
            logger.info("WebSocket connection closed", client_id=client_id, total_connections=len(self.connections))
        clear_request_context()

    async def send_message(self, client_id: str, message: str):
        """Send message to specific client with enhanced logging."""
        if client_id in self.connections:
            try:
                websocket = self.connections[client_id]
                await websocket.send_text(message)
                logger.debug("WebSocket message sent", client_id=client_id, message_length=len(message))
            except Exception as e:
                logger.error("Failed to send WebSocket message", client_id=client_id, error=str(e))
                await self.disconnect(client_id)

    async def broadcast_message(self, message: str, exclude_client: str = None):
        """Broadcast message to all connected clients with enhanced logging."""
        logger.info(
            "Broadcasting WebSocket message",
            message_length=len(message),
            total_connections=len(self.connections),
            exclude_client=exclude_client,
        )

        disconnected_clients = []
        for client_id, websocket in self.connections.items():
            if exclude_client and client_id == exclude_client:
                continue

            try:
                await websocket.send_text(message)
                logger.debug("WebSocket broadcast sent", client_id=client_id)
            except Exception as e:
                logger.error("WebSocket broadcast failed", client_id=client_id, error=str(e))
                disconnected_clients.append(client_id)

        # Remove disconnected clients
        for client_id in disconnected_clients:
            await self.disconnect(client_id)


# ✅ CORRECT - WebSocket message handler with enhanced logging
async def handle_websocket_message(websocket, client_id: str, message: str):
    """Handle WebSocket message with enhanced logging."""
    logger.debug("WebSocket message received", client_id=client_id, message_type="text", message_length=len(message))

    try:
        with measure_performance("websocket_message_processing", client_id=client_id):
            # Parse message
            parsed_message = parse_websocket_message(message)

            # Process message based on type
            if parsed_message["type"] == "chat":
                response = await handle_chat_message(parsed_message, client_id)
            elif parsed_message["type"] == "game_action":
                response = await handle_game_action(parsed_message, client_id)
            else:
                response = {"error": "Unknown message type"}

            # Send response
            await websocket.send_text(str(response))
            logger.debug(
                "WebSocket message processed and response sent",
                client_id=client_id,
                message_type=parsed_message["type"],
            )
    except Exception as e:
        logger.error("Failed to process WebSocket message", client_id=client_id, error=str(e))
        await websocket.send_text('{"error": "Message processing failed"}')


# ✅ CORRECT - WebSocket chat message handler
async def handle_chat_message(message_data: dict, client_id: str):
    """Handle chat message with enhanced logging."""
    logger.info(
        "Processing chat message",
        client_id=client_id,
        channel=message_data.get("channel"),
        message_length=len(message_data.get("text", "")),
    )

    try:
        # Validate message
        if not message_data.get("text"):
            logger.warning("Empty chat message received", client_id=client_id)
            return {"error": "Message cannot be empty"}

        # Process chat message
        processed_message = await chat_service.process_message(message_data, client_id)

        # Broadcast to other clients
        await websocket_manager.broadcast_message(str(processed_message), exclude_client=client_id)

        logger.info("Chat message processed and broadcasted", client_id=client_id)
        return {"status": "success"}
    except Exception as e:
        logger.error("Chat message processing failed", client_id=client_id, error=str(e))
        return {"error": "Chat processing failed"}


# ✅ CORRECT - WebSocket game action handler
async def handle_game_action(action_data: dict, client_id: str):
    """Handle game action with enhanced logging."""
    logger.info(
        "Processing game action",
        client_id=client_id,
        action_type=action_data.get("action"),
        target=action_data.get("target"),
    )

    try:
        with measure_performance("game_action_processing", client_id=client_id, action=action_data.get("action")):
            # Process game action
            result = await game_service.process_action(action_data, client_id)

            # Broadcast action result to relevant clients
            await websocket_manager.broadcast_message(str(result), exclude_client=client_id)

            logger.info("Game action processed and broadcasted", client_id=client_id, action=action_data.get("action"))
            return result
    except Exception as e:
        logger.error("Game action processing failed", client_id=client_id, error=str(e))
        return {"error": "Action processing failed"}


# ✅ CORRECT - WebSocket connection handler with enhanced logging
async def websocket_endpoint(websocket, client_id: str):
    """WebSocket endpoint with enhanced logging and error handling."""
    await websocket_manager.connect(websocket, client_id)

    try:
        while True:
            # Receive message
            message = await websocket.receive_text()

            # Handle message
            await handle_websocket_message(websocket, client_id, message)

    except WebSocketDisconnect:
        logger.info("WebSocket disconnected", client_id=client_id)
    except Exception as e:
        logger.error("WebSocket error", client_id=client_id, error=str(e))
        track_exception(e, client_id=client_id, connection_type="websocket")
    finally:
        await websocket_manager.disconnect(client_id)


# ✅ CORRECT - WebSocket heartbeat handler with enhanced logging
async def websocket_heartbeat(websocket, client_id: str):
    """WebSocket heartbeat handler with enhanced logging."""
    logger.debug("Starting WebSocket heartbeat", client_id=client_id)

    try:
        while True:
            await asyncio.sleep(30)  # Send heartbeat every 30 seconds

            if client_id in websocket_manager.connections:
                await websocket.send_text('{"type": "heartbeat", "timestamp": "' + str(time.time()) + '"}')
                logger.debug("WebSocket heartbeat sent", client_id=client_id)
            else:
                logger.debug("WebSocket heartbeat stopped - connection closed", client_id=client_id)
                break
    except Exception as e:
        logger.error("WebSocket heartbeat error", client_id=client_id, error=str(e))


# ✅ CORRECT - WebSocket authentication with enhanced logging
async def authenticate_websocket_connection(websocket, token: str) -> str:
    """Authenticate WebSocket connection with enhanced logging."""
    logger.info("Authenticating WebSocket connection", token_length=len(token))

    try:
        # Verify token
        user = await auth_service.verify_token(token)

        logger.info("WebSocket authentication successful", user_id=user.id, username=user.username)
        return user.id
    except Exception as e:
        logger.error("WebSocket authentication failed", error=str(e))
        await websocket.send_text('{"error": "Authentication failed"}')
        raise


# ✅ CORRECT - WebSocket rate limiting with enhanced logging
class WebSocketRateLimiter:
    """WebSocket rate limiter with enhanced logging."""

    def __init__(self, max_messages_per_minute: int = 60):
        self.max_messages_per_minute = max_messages_per_minute
        self.message_counts = {}
        logger.info("WebSocket rate limiter initialized", max_messages_per_minute=max_messages_per_minute)

    async def check_rate_limit(self, client_id: str) -> bool:
        """Check if client is within rate limit with enhanced logging."""
        current_time = time.time()
        minute_ago = current_time - 60

        # Clean old entries
        if client_id in self.message_counts:
            self.message_counts[client_id] = [
                timestamp for timestamp in self.message_counts[client_id] if timestamp > minute_ago
            ]
        else:
            self.message_counts[client_id] = []

        # Check rate limit
        if len(self.message_counts[client_id]) >= self.max_messages_per_minute:
            logger.warning(
                "WebSocket rate limit exceeded",
                client_id=client_id,
                message_count=len(self.message_counts[client_id]),
                limit=self.max_messages_per_minute,
            )
            return False

        # Add current message
        self.message_counts[client_id].append(current_time)
        return True


# ✅ CORRECT - WebSocket message validation with enhanced logging
def validate_websocket_message(message: str) -> dict:
    """Validate WebSocket message with enhanced logging."""
    logger.debug("Validating WebSocket message", message_length=len(message))

    try:
        import json

        parsed_message = json.loads(message)

        # Validate required fields
        if "type" not in parsed_message:
            logger.warning("WebSocket message missing type field")
            return {"error": "Message type is required"}

        logger.debug("WebSocket message validation successful", message_type=parsed_message["type"])
        return parsed_message
    except json.JSONDecodeError as e:
        logger.warning("WebSocket message JSON decode error", error=str(e))
        return {"error": "Invalid JSON format"}
    except Exception as e:
        logger.error("WebSocket message validation error", error=str(e))
        return {"error": "Message validation failed"}


# ✅ CORRECT - WebSocket error handling with enhanced logging
async def handle_websocket_error(websocket, client_id: str, error: Exception):
    """Handle WebSocket error with enhanced logging."""
    logger.error(
        "WebSocket error occurred", client_id=client_id, error_type=type(error).__name__, error_message=str(error)
    )

    try:
        error_response = {"type": "error", "message": "An error occurred", "timestamp": time.time()}
        await websocket.send_text(str(error_response))
    except Exception as send_error:
        logger.error("Failed to send error response", client_id=client_id, error=str(send_error))


# Helper functions for examples
def parse_websocket_message(message: str) -> dict:
    """Parse WebSocket message."""
    import json

    return json.loads(message)


class WebSocketDisconnect(Exception):
    pass


class websocket_manager:
    @staticmethod
    async def broadcast_message(message: str, exclude_client: str = None):
        pass


class chat_service:
    @staticmethod
    async def process_message(message_data: dict, client_id: str):
        return {"type": "chat", "message": message_data.get("text")}


class game_service:
    @staticmethod
    async def process_action(action_data: dict, client_id: str):
        return {"type": "game_action", "result": "success"}


class auth_service:
    @staticmethod
    async def verify_token(token: str):
        class User:
            id = "user123"
            username = "testuser"

        return User()


# Simulate WebSocket object
class WebSocket:
    async def accept(self):
        pass

    async def send_text(self, text: str):
        pass

    async def receive_text(self):
        return '{"type": "chat", "text": "Hello World"}'

    @property
    def client(self):
        class Client:
            host = "192.168.1.1"

        return Client()
