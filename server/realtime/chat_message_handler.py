"""
Chat message handler for MythosMUD.

This module handles Redis chat message subscriptions and broadcasts
messages to WebSocket clients in real-time.
"""

import asyncio
from typing import Any

from ..logging_config import get_logger
from ..services.redis_service import redis_service
from .connection_manager import connection_manager
from .envelope import build_event

logger = get_logger(__name__)


class ChatMessageHandler:
    """
    Handles chat message processing from Redis and broadcasting to WebSocket clients.

    This class subscribes to Redis chat channels and broadcasts messages
    to the appropriate WebSocket clients based on room subscriptions.
    """

    def __init__(self):
        """Initialize the chat message handler."""
        self._running = False
        self._subscribed_channels = set()

    async def start(self):
        """Start the chat message handler."""
        if self._running:
            logger.warning("Chat message handler already running")
            return

        self._running = True
        logger.info("Starting chat message handler")

        # Connect to Redis if not already connected
        if not redis_service.redis_client:
            success = await redis_service.connect()
            if not success:
                logger.error("Failed to connect to Redis for chat message handler")
                self._running = False
                return

        # Subscribe to all chat channels (single channel per chat type)
        await self._subscribe_to_chat_channels()

        # Start the Redis message processing loop
        await redis_service.start_message_loop()

    async def stop(self):
        """Stop the chat message handler."""
        self._running = False
        logger.info("Stopping chat message handler")

        # Stop Redis message loop
        await redis_service.stop_message_loop()

        # Unsubscribe from all channels
        for channel in self._subscribed_channels:
            await redis_service.unsubscribe_from_chat_channel(channel)
        self._subscribed_channels.clear()

    async def _subscribe_to_chat_channels(self):
        """
        Subscribe to all chat channels.

        We use a single channel per chat type (say, global, party) and filter
        messages by room_id in the application logic.
        """
        chat_channels = [
            "chat:say",  # All say messages
            "chat:global",  # All global messages
            "chat:party",  # All party messages
            "chat:whisper",  # All whisper messages
        ]

        for channel in chat_channels:
            await redis_service.subscribe_to_chat_channel(channel, self._handle_chat_message)
            self._subscribed_channels.add(channel)
            logger.info("Subscribed to chat channel", channel=channel)

    def _handle_chat_message(self, message_data: dict[str, Any]):
        """
        Handle incoming chat messages from Redis and broadcast to WebSocket clients.

        This method is called by the Redis message loop when a chat message
        is received on a subscribed channel. It filters messages by room_id
        and broadcasts to the appropriate players.

        Args:
            message_data: The chat message data from Redis
        """
        try:
            # Extract message details
            sender_id = message_data.get("sender_id")
            player_name = message_data.get("player_name")
            channel = message_data.get("channel")
            message = message_data.get("message")
            message_id = message_data.get("message_id")
            room_id = message_data.get("room_id")
            timestamp = message_data.get("timestamp")

            if not all([sender_id, player_name, channel, message]):
                logger.warning("Incomplete chat message data received", message_data=message_data)
                return

            logger.debug(
                "Processing chat message from Redis",
                message_id=message_id,
                sender_id=sender_id,
                player_name=player_name,
                channel=channel,
                room_id=room_id,
            )

            # Create WebSocket event for broadcasting
            chat_event = build_event(
                "chat_message",
                {
                    "sender_id": sender_id,
                    "player_name": player_name,
                    "channel": channel,
                    "message": message,
                    "message_id": message_id,
                    "timestamp": timestamp,
                },
                player_id=sender_id,
            )

            # Route message based on channel type
            if channel == "say" and room_id:
                # Say messages: broadcast to players in the same room
                asyncio.create_task(connection_manager.broadcast_to_room(room_id, chat_event, exclude_player=sender_id))
                logger.info(
                    "Say message broadcasted to room",
                    message_id=message_id,
                    sender_id=sender_id,
                    player_name=player_name,
                    room_id=room_id,
                )

            elif channel == "global":
                # Global messages: broadcast to all connected players
                asyncio.create_task(connection_manager.broadcast_global(chat_event, exclude_player=sender_id))
                logger.info(
                    "Global message broadcasted to all players",
                    message_id=message_id,
                    sender_id=sender_id,
                    player_name=player_name,
                )

            elif channel == "party" and room_id:
                # Party messages: broadcast to party members (future implementation)
                # For now, treat like say messages
                asyncio.create_task(connection_manager.broadcast_to_room(room_id, chat_event, exclude_player=sender_id))
                logger.info(
                    "Party message broadcasted to room (placeholder)",
                    message_id=message_id,
                    sender_id=sender_id,
                    player_name=player_name,
                    room_id=room_id,
                )

            elif channel == "whisper":
                # Whisper messages: send to specific player (future implementation)
                # For now, log but don't broadcast
                logger.info(
                    "Whisper message received (not yet implemented)",
                    message_id=message_id,
                    sender_id=sender_id,
                    player_name=player_name,
                )

            else:
                logger.warning(
                    "Unknown chat channel or missing room_id", channel=channel, room_id=room_id, message_id=message_id
                )

        except Exception as e:
            logger.error("Error handling chat message from Redis", error=str(e), message_data=message_data)


# Global chat message handler instance
chat_message_handler = ChatMessageHandler()
