"""
NATS implementation of MessageBroker protocol.

This module provides a concrete implementation of the MessageBroker protocol
using NATS as the underlying message broker.
"""

import asyncio
import json
from typing import Any
from uuid import uuid4

import nats
from nats.aio.msg import Msg
from nats.js.errors import BadRequestError  # noqa: F401

from ..config.models import NATSConfig
from ..logging.enhanced_logging_config import get_logger
from .message_broker import (
    ConnectionError,
    MessageBrokerError,
    MessageHandler,
    PublishError,
    RequestError,
    SubscribeError,
    UnsubscribeError,
)

logger = get_logger(__name__)


class NATSMessageBroker:
    """
    NATS implementation of MessageBroker protocol.

    This class wraps NATS client to provide the MessageBroker interface,
    allowing the domain layer to remain independent of NATS-specific details.
    """

    def __init__(self, config: NATSConfig):
        """
        Initialize NATS message broker.

        Args:
            config: NATS configuration
        """
        self.config = config
        self._client: Any = None  # NATS client (use Any due to nats.Client vs nats.aio.client.Client mismatch)
        self._subscriptions: dict[str, Any] = {}  # subscription_id -> NATS subscription object
        self._logger = get_logger(__name__)

    async def connect(self) -> bool:
        """
        Connect to NATS server.

        Returns:
            bool: True if connection successful, False otherwise
        """
        try:
            if self._client and self._client.is_connected:
                self._logger.info("Already connected to NATS")
                return True

            self._client = await nats.connect(
                servers=self.config.url,
                max_reconnect_attempts=self.config.max_reconnect_attempts,
                reconnect_time_wait=self.config.reconnect_time_wait,
                ping_interval=self.config.ping_interval,
                max_outstanding_pings=self.config.max_outstanding_pings,
                # Error callback
                error_cb=self._error_callback,
                # Disconnect callback
                disconnected_cb=self._disconnected_callback,
                # Reconnect callback
                reconnected_cb=self._reconnected_callback,
            )

            self._logger.info("Connected to NATS", url=self.config.url)
            return True

        except Exception as e:
            self._logger.error("Failed to connect to NATS", error=str(e), exc_info=True)
            raise ConnectionError(f"Failed to connect to NATS: {e}") from e

    async def disconnect(self) -> None:
        """Disconnect from NATS server."""
        if not self._client:
            return

        try:
            # Unsubscribe from all subscriptions
            for subscription_id in list(self._subscriptions.keys()):
                try:
                    await self.unsubscribe(subscription_id)
                except Exception as e:
                    self._logger.warning("Error unsubscribing", subscription_id=subscription_id, error=str(e))

            # Close client connection
            if self._client.is_connected:
                await self._client.close()

            self._logger.info("Disconnected from NATS")

        except Exception as e:
            self._logger.error("Error disconnecting from NATS", error=str(e))
            raise MessageBrokerError(f"Error disconnecting from NATS: {e}") from e

    def is_connected(self) -> bool:
        """
        Check if connected to NATS.

        Returns:
            bool: True if connected, False otherwise
        """
        return self._client is not None and self._client.is_connected

    async def publish(self, subject: str, message: dict[str, Any]) -> None:
        """
        Publish message to NATS subject.

        Args:
            subject: NATS subject to publish to
            message: Message data (must be JSON-serializable)

        Raises:
            PublishError: If publishing fails
        """
        if not self.is_connected():
            raise PublishError("Not connected to NATS")

        try:
            # Serialize message to JSON bytes
            message_bytes = json.dumps(message).encode("utf-8")

            # Publish to NATS
            await self._client.publish(subject, message_bytes)

            self._logger.debug("Published message", subject=subject, message_size=len(message_bytes))

        except Exception as e:
            self._logger.error("Failed to publish message", subject=subject, error=str(e))
            raise PublishError(f"Failed to publish to {subject}: {e}") from e

    async def subscribe(self, subject: str, handler: MessageHandler, queue_group: str | None = None) -> str:
        """
        Subscribe to NATS subject with message handler.

        Args:
            subject: NATS subject to subscribe to (supports wildcards)
            handler: Async callable that processes messages
            queue_group: Optional queue group for load balancing

        Returns:
            str: Subscription ID for later unsubscribe

        Raises:
            SubscribeError: If subscription fails
        """
        if not self.is_connected():
            raise SubscribeError("Not connected to NATS")

        try:
            # Create wrapper to convert NATS message to dict
            async def nats_message_wrapper(msg: Msg) -> None:
                try:
                    # Decode and deserialize message
                    message_dict = json.loads(msg.data.decode("utf-8"))
                    # Call user handler
                    await handler(message_dict)
                except Exception as e:
                    self._logger.error(
                        "Error processing NATS message", subject=msg.subject, error=str(e), exc_info=True
                    )

            # Subscribe to NATS (queue_group may be None, cast to empty string if so)
            subscription = await self._client.subscribe(subject, queue=queue_group or "", cb=nats_message_wrapper)

            # Generate subscription ID
            subscription_id = str(uuid4())
            self._subscriptions[subscription_id] = subscription

            self._logger.info("Subscribed to NATS subject", subject=subject, queue_group=queue_group)

            return subscription_id

        except Exception as e:
            self._logger.error("Failed to subscribe to NATS subject", subject=subject, error=str(e))
            raise SubscribeError(f"Failed to subscribe to {subject}: {e}") from e

    async def unsubscribe(self, subscription_id: str) -> None:
        """
        Unsubscribe from NATS subject.

        Args:
            subscription_id: ID returned from subscribe()

        Raises:
            UnsubscribeError: If unsubscribe fails
        """
        subscription = self._subscriptions.get(subscription_id)
        if not subscription:
            self._logger.warning("Subscription not found", subscription_id=subscription_id)
            return

        try:
            await subscription.unsubscribe()
            del self._subscriptions[subscription_id]

            self._logger.info("Unsubscribed from NATS", subscription_id=subscription_id)

        except Exception as e:
            self._logger.error("Failed to unsubscribe", subscription_id=subscription_id, error=str(e))
            raise UnsubscribeError(f"Failed to unsubscribe {subscription_id}: {e}") from e

    async def request(self, subject: str, message: dict[str, Any], timeout: float = 2.0) -> dict[str, Any]:
        """
        Send request and wait for reply (request-reply pattern).

        Args:
            subject: NATS subject to send request to
            message: Request message data
            timeout: Maximum time to wait for reply (seconds)

        Returns:
            dict: Reply message data

        Raises:
            RequestError: If request fails
            TimeoutError: If no reply received within timeout
        """
        if not self.is_connected():
            raise RequestError("Not connected to NATS")

        try:
            # Serialize request message
            request_bytes = json.dumps(message).encode("utf-8")

            # Send request and wait for reply
            reply_msg = await asyncio.wait_for(
                self._client.request(subject, request_bytes),
                timeout=timeout,
            )

            # Deserialize reply
            reply_dict = json.loads(reply_msg.data.decode("utf-8"))

            self._logger.debug("Received reply", subject=subject)

            return reply_dict

        except TimeoutError as e:
            self._logger.warning("Request timeout", subject=subject, timeout=timeout)
            raise TimeoutError(f"Request to {subject} timed out after {timeout}s") from e

        except Exception as e:
            self._logger.error("Request failed", subject=subject, error=str(e))
            raise RequestError(f"Request to {subject} failed: {e}") from e

    # NATS event callbacks
    async def _error_callback(self, error: Exception) -> None:
        """Handle NATS errors."""
        self._logger.error("NATS error occurred", error=str(error))

    async def _disconnected_callback(self) -> None:
        """Handle NATS disconnection."""
        self._logger.warning("Disconnected from NATS")

    async def _reconnected_callback(self) -> None:
        """Handle NATS reconnection."""
        self._logger.info("Reconnected to NATS")


# Type annotation for protocol conformance
# Note: NATSMessageBroker implements MessageBroker protocol
# Mypy may not recognize structural subtyping here
