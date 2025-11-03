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
        ...

    async def disconnect(self) -> None:
        """
        Disconnect from the message broker.

        Closes all subscriptions and releases resources.
        """
        ...

    def is_connected(self) -> bool:
        """
        Check if connected to the message broker.

        Returns:
            bool: True if connected, False otherwise
        """
        ...

    async def publish(self, subject: str, message: dict[str, Any]) -> None:
        """
        Publish a message to a subject/topic.

        Args:
            subject: Subject/topic to publish to
            message: Message data (must be JSON-serializable)

        Raises:
            MessageBrokerError: If publishing fails
        """
        ...

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
        ...

    async def unsubscribe(self, subscription_id: str) -> None:
        """
        Unsubscribe from a subject/topic.

        Args:
            subscription_id: ID returned from subscribe()

        Raises:
            MessageBrokerError: If unsubscribe fails
        """
        ...

    async def request(self, subject: str, message: dict[str, Any], timeout: float = 2.0) -> dict[str, Any]:
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
        ...


class MessageBrokerError(Exception):
    """Base exception for message broker errors."""

    pass


class ConnectionError(MessageBrokerError):
    """Exception raised when connection to message broker fails."""

    pass


class PublishError(MessageBrokerError):
    """Exception raised when publishing message fails."""

    pass


class SubscribeError(MessageBrokerError):
    """Exception raised when subscribing to subject fails."""

    pass


class UnsubscribeError(MessageBrokerError):
    """Exception raised when unsubscribing from subject fails."""

    pass


class RequestError(MessageBrokerError):
    """Exception raised when request-reply fails."""

    pass
