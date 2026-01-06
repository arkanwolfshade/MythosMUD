"""
Message Broker abstraction for MythosMUD.

This module defines the MessageBroker protocol (interface) that abstracts
message broker implementations (NATS, RabbitMQ, Redis Pub/Sub, etc.).

Following hexagonal architecture principles, the domain layer depends on this
abstraction, not specific broker implementations.

As noted in the Pnakotic Manuscripts: "One must not bind oneself to a single
messenger, for the dimensions may shift and new conduits may be required."
"""

from collections.abc import Callable
from typing import Any, Protocol

# Type alias for message handlers
MessageHandler = Callable[[dict[str, Any]], Any]


class MessageBroker(Protocol):
    """
    Protocol defining the message broker interface.

    This abstract interface allows the domain to publish and subscribe to messages
    without coupling to specific broker implementations (NATS, RabbitMQ, etc.).

    Implementations must provide:
    - Connection management (connect, disconnect, is_connected)
    - Publishing messages to subjects/topics
    - Subscribing to subjects/topics with handlers
    - Unsubscribing from subjects/topics
    """

    async def connect(self) -> bool:
        """
        Connect to the message broker.

        Returns:
            bool: True if connection successful, False otherwise
        """
        ...  # pylint: disable=unnecessary-ellipsis  # Reason: Abstract method placeholder required by ABC

    async def disconnect(self) -> None:
        """
        Disconnect from the message broker.

        Closes all subscriptions and releases resources.
        """
        ...  # pylint: disable=unnecessary-ellipsis  # Reason: Abstract method placeholder required by ABC

    def is_connected(self) -> bool:
        """
        Check if connected to the message broker.

        Returns:
            bool: True if connected, False otherwise
        """
        ...  # pylint: disable=unnecessary-ellipsis  # Reason: Abstract method placeholder required by ABC

    async def publish(self, subject: str, message: dict[str, Any]) -> None:
        """
        Publish a message to a subject/topic.

        Args:
            subject: Subject/topic to publish to
            message: Message data (must be JSON-serializable)

        Raises:
            MessageBrokerError: If publishing fails
        """
        ...  # pylint: disable=unnecessary-ellipsis  # Reason: Abstract method placeholder required by ABC

    async def subscribe(self, subject: str, handler: MessageHandler, queue_group: str | None = None) -> str:
        """
        Subscribe to a subject/topic with a message handler.

        Args:
            subject: Subject/topic to subscribe to (may include wildcards)
            handler: Async callable that processes received messages
            queue_group: Optional queue group for load balancing

        Returns:
            str: Subscription ID for later unsubscribe

        Raises:
            MessageBrokerError: If subscription fails
        """
        ...  # pylint: disable=unnecessary-ellipsis  # Reason: Abstract method placeholder required by ABC

    async def unsubscribe(self, subscription_id: str) -> None:
        """
        Unsubscribe from a subject/topic.

        Args:
            subscription_id: ID returned from subscribe()

        Raises:
            MessageBrokerError: If unsubscribe fails
        """
        ...  # pylint: disable=unnecessary-ellipsis  # Reason: Abstract method placeholder required by ABC

    async def request(self, subject: str, message: dict[str, Any], timeout: float = 2.0) -> dict[str, Any]:  # pylint: disable=unnecessary-ellipsis  # Reason: Abstract method placeholder required by ABC
        """
        Send a request and wait for a reply (request-reply pattern).

        Args:
            subject: Subject to send request to
            message: Request message data
            timeout: Maximum time to wait for reply (seconds)

        Returns:
            dict: Reply message data

        Raises:
            MessageBrokerError: If request fails
            TimeoutError: If no reply received within timeout
        """
        ...  # pylint: disable=unnecessary-ellipsis  # Reason: Abstract method placeholder required by ABC


class MessageBrokerError(Exception):
    """Base exception for message broker errors."""


class MessageBrokerConnectionError(MessageBrokerError):
    """Exception raised when connection to message broker fails."""


class PublishError(MessageBrokerError):
    """Exception raised when publishing message fails."""


class SubscribeError(MessageBrokerError):
    """Exception raised when subscribing to subject fails."""


class UnsubscribeError(MessageBrokerError):
    """Exception raised when unsubscribing from subject fails."""


class RequestError(MessageBrokerError):
    """Exception raised when request-reply fails."""
