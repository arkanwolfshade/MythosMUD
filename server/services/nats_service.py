"""
NATS service for MythosMUD chat system.

This module provides NATS pub/sub functionality for real-time chat messaging,
replacing the previous Redis-based implementation with a more lightweight
and Windows-native solution.
"""

import json
from collections.abc import Callable
from typing import Any

import nats

from ..logging_config import get_logger

logger = get_logger("nats")


class NATSService:
    """
    NATS service for handling pub/sub operations and real-time messaging.

    This service provides a clean interface for publishing chat messages
    and managing real-time communication between players using NATS.
    """

    def __init__(self, config: dict[str, Any] | None = None):
        """
        Initialize NATS service.

        Args:
            config: NATS configuration dictionary
        """
        self.config = config or {}
        self.nc: nats.NATS | None = None
        self.subscriptions: dict[str, nats.Subscription] = {}
        self._running = False
        self._connection_retries = 0
        self._max_retries = self.config.get("max_reconnect_attempts", 5)

    async def connect(self) -> bool:
        """
        Connect to NATS server.

        Returns:
            True if connection successful, False otherwise
        """
        try:
            # Get NATS connection URL from config
            nats_url = self.config.get("url", "nats://localhost:4222")

            # Connection options
            connect_options = {
                "reconnect_time_wait": self.config.get("reconnect_time_wait", 1),
                "max_reconnect_attempts": self._max_retries,
                "connect_timeout": self.config.get("connect_timeout", 5),
                "ping_interval": self.config.get("ping_interval", 30),
                "max_outstanding_pings": self.config.get("max_outstanding_pings", 5),
            }

            logger.info("Connecting to NATS server", url=nats_url)

            # Connect to NATS
            self.nc = await nats.connect(nats_url, **connect_options)

            # Set up connection event handlers
            self.nc.add_error_listener(self._on_error)
            self.nc.add_disconnect_listener(self._on_disconnect)
            self.nc.add_reconnect_listener(self._on_reconnect)

            self._running = True
            self._connection_retries = 0

            logger.info("Connected to NATS server successfully", url=nats_url)
            return True

        except Exception as e:
            self._connection_retries += 1
            logger.error(
                "Failed to connect to NATS server",
                error=str(e),
                url=self.config.get("url", "nats://localhost:4222"),
                retry_count=self._connection_retries,
                max_retries=self._max_retries,
            )
            return False

    async def disconnect(self):
        """Disconnect from NATS and cleanup resources."""
        try:
            if self.nc:
                # Close all subscriptions
                for subject, subscription in self.subscriptions.items():
                    try:
                        await subscription.unsubscribe()
                        logger.debug("Unsubscribed from NATS subject", subject=subject)
                    except Exception as e:
                        logger.warning("Error unsubscribing from subject", subject=subject, error=str(e))

                # Close NATS connection
                await self.nc.close()
                self.nc = None
                self.subscriptions.clear()
                self._running = False

                logger.info("Disconnected from NATS server")
        except Exception as e:
            logger.error("Error disconnecting from NATS server", error=str(e))

    async def publish(self, subject: str, data: dict[str, Any]) -> bool:
        """
        Publish a message to a NATS subject.

        Args:
            subject: NATS subject name (e.g., 'chat.say', 'chat.global')
            data: Message data to publish

        Returns:
            True if published successfully, False otherwise
        """
        try:
            if not self.nc or not self._running:
                logger.error("NATS client not connected")
                return False

            # Serialize message data
            message_json = json.dumps(data)
            message_bytes = message_json.encode('utf-8')

            # Publish to NATS subject
            await self.nc.publish(subject, message_bytes)

            logger.debug(
                "Message published to NATS subject",
                subject=subject,
                message_id=data.get("message_id"),
                sender_id=data.get("sender_id"),
                data_size=len(message_bytes),
            )

            return True

        except Exception as e:
            logger.error(
                "Failed to publish message to NATS subject",
                error=str(e),
                subject=subject,
                message_id=data.get("message_id"),
            )
            return False

    async def subscribe(self, subject: str, callback: Callable[[dict[str, Any]], None]) -> bool:
        """
        Subscribe to a NATS subject and register a callback for incoming messages.

        Args:
            subject: NATS subject name to subscribe to
            callback: Function to call when messages are received

        Returns:
            True if subscribed successfully, False otherwise
        """
        try:
            if not self.nc or not self._running:
                logger.error("NATS client not connected")
                return False

            # Create message handler
            async def message_handler(msg):
                try:
                    # Decode message data
                    data = msg.data.decode('utf-8')
                    message_data = json.loads(data)

                    # Call the registered callback
                    callback(message_data)

                    logger.debug(
                        "Message received from NATS subject",
                        subject=subject,
                        message_id=message_data.get("message_id"),
                        sender_id=message_data.get("sender_id"),
                    )

                except json.JSONDecodeError as e:
                    logger.error("Failed to decode NATS message", error=str(e), subject=subject)
                except Exception as e:
                    logger.error("Error handling NATS message", error=str(e), subject=subject)

            # Subscribe to subject
            subscription = await self.nc.subscribe(subject, cb=message_handler)
            self.subscriptions[subject] = subscription

            logger.info("Subscribed to NATS subject", subject=subject)
            return True

        except Exception as e:
            logger.error("Failed to subscribe to NATS subject", error=str(e), subject=subject)
            return False

    async def unsubscribe(self, subject: str) -> bool:
        """
        Unsubscribe from a NATS subject.

        Args:
            subject: NATS subject name to unsubscribe from

        Returns:
            True if unsubscribed successfully, False otherwise
        """
        try:
            if subject not in self.subscriptions:
                logger.warning("Not subscribed to NATS subject", subject=subject)
                return False

            subscription = self.subscriptions[subject]
            await subscription.unsubscribe()
            del self.subscriptions[subject]

            logger.info("Unsubscribed from NATS subject", subject=subject)
            return True

        except Exception as e:
            logger.error("Failed to unsubscribe from NATS subject", error=str(e), subject=subject)
            return False

    async def request(self, subject: str, data: dict[str, Any], timeout: float = 5.0) -> dict[str, Any] | None:
        """
        Send a request to a NATS subject and wait for a response.

        Args:
            subject: NATS subject name to send request to
            data: Request data to send
            timeout: Timeout in seconds for the response

        Returns:
            Response data if successful, None otherwise
        """
        try:
            if not self.nc or not self._running:
                logger.error("NATS client not connected")
                return None

            # Serialize request data
            request_json = json.dumps(data)
            request_bytes = request_json.encode('utf-8')

            # Send request and wait for response
            response = await self.nc.request(subject, request_bytes, timeout=timeout)

            # Decode response data
            response_data = response.data.decode('utf-8')
            response_json = json.loads(response_data)

            logger.debug(
                "Request/response completed",
                subject=subject,
                request_id=data.get("request_id"),
                response_size=len(response.data),
            )

            return response_json

        except TimeoutError:
            logger.warning("Request timeout", subject=subject, timeout=timeout)
            return None
        except Exception as e:
            logger.error("Failed to send request", error=str(e), subject=subject)
            return None

    def is_connected(self) -> bool:
        """
        Check if NATS client is connected.

        Returns:
            True if connected, False otherwise
        """
        return self.nc is not None and self._running

    def get_subscription_count(self) -> int:
        """
        Get the number of active subscriptions.

        Returns:
            Number of active subscriptions
        """
        return len(self.subscriptions)

    # Event handlers
    def _on_error(self, error):
        """Handle NATS connection errors."""
        logger.error("NATS connection error", error=str(error))

    def _on_disconnect(self):
        """Handle NATS disconnection events."""
        logger.warning("NATS client disconnected")
        self._running = False

    def _on_reconnect(self):
        """Handle NATS reconnection events."""
        logger.info("NATS client reconnected")
        self._running = True
        self._connection_retries = 0


# Global NATS service instance
nats_service = NATSService()
