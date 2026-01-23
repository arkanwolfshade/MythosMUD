"""
NATS implementation of MessageBroker protocol.

This module provides a concrete implementation of the MessageBroker protocol
using NATS as the underlying message broker.
"""

# pylint: disable=too-many-lines  # Reason: NATS broker implementation requires 551 lines to implement message broker protocol with subscription management, connection handling, error recovery, and async operations; splitting would reduce cohesion

import asyncio
import json
from typing import Any, cast
from uuid import uuid4

import nats
from anyio import sleep
from nats.aio.msg import Msg

# BadRequestError removed - unused import
from ..config.models import NATSConfig
from ..schemas.nats_messages import validate_message
from ..services.nats_subject_manager import NATSSubjectManager, SubjectValidationError
from ..structured_logging.enhanced_logging_config import get_logger
from .message_broker import (
    MessageBrokerConnectionError,
    MessageBrokerError,
    MessageHandler,
    PublishError,
    RequestError,
    SubscribeError,
    UnsubscribeError,
)

logger = get_logger(__name__)


class NATSMessageBroker:  # pylint: disable=too-many-instance-attributes  # Reason: NATS broker requires multiple attributes for configuration, client state, subscriptions, health monitoring, and validation. All attributes are necessary for proper functionality.
    """
    NATS implementation of MessageBroker protocol.

    This class wraps NATS client to provide the MessageBroker interface,
    allowing the domain layer to remain independent of NATS-specific details.
    """

    def __init__(
        self,
        config: NATSConfig,
        enable_message_validation: bool = True,
        subject_manager: NATSSubjectManager | None = None,
    ):
        """
        Initialize NATS message broker.

        Args:
            config: NATS configuration
            enable_message_validation: Enable message schema validation (default: True)
            subject_manager: NATSSubjectManager instance for subject validation and building (optional)

        AI: Message validation prevents malformed messages from being published.
        AI: Subject manager provides centralized subject management and validation.
        """
        self.config = config
        self._client: Any = None  # NATS client (use Any due to nats.Client vs nats.aio.client.Client mismatch)
        self._subscriptions: dict[str, Any] = {}  # subscription_id -> NATS subscription object
        self._logger = get_logger(__name__)
        self._enable_validation = enable_message_validation

        # Initialize subject manager if not provided and validation is enabled
        if subject_manager is None and self.config.enable_subject_validation:
            subject_manager = NATSSubjectManager(strict_validation=self.config.strict_subject_validation)
        self.subject_manager = subject_manager

        # Health monitoring
        self._health_check_task: asyncio.Task | None = None
        self._last_health_check: float = 0.0
        self._consecutive_health_failures = 0
        self._health_check_timeout = 5.0  # seconds
        self._running = False

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
            self._running = True

            # Start health check monitoring if enabled
            await self._start_health_monitoring()

            return True

        except Exception as e:
            self._logger.error("Failed to connect to NATS", error=str(e), exc_info=True)
            raise MessageBrokerConnectionError(f"Failed to connect to NATS: {e}") from e

    async def disconnect(self) -> None:
        """Disconnect from NATS server."""
        if not self._client:
            return

        try:
            # Unsubscribe from all subscriptions
            for subscription_id in list(self._subscriptions.keys()):
                try:
                    await self.unsubscribe(subscription_id)
                except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Unsubscribe errors unpredictable, must handle gracefully
                    self._logger.warning("Error unsubscribing", subscription_id=subscription_id, error=str(e))

            # Stop health check monitoring
            await self._stop_health_monitoring()

            # Close client connection
            if self._client.is_connected:
                await self._client.close()

            self._running = False
            self._logger.info("Disconnected from NATS")

        except Exception as e:
            self._logger.error("Error disconnecting from NATS", error=str(e))
            raise MessageBrokerError(f"Error disconnecting from NATS: {e}") from e

    def is_connected(self) -> bool:
        """
        Check if connected to NATS and healthy.

        Returns:
            bool: True if connected and healthy, False otherwise

        AI: Verifies both connection state and recent health check success.
            A stale connection (no recent successful health check) is considered disconnected.
        """
        if not self._client or not self._running:
            return False

        if not self._client.is_connected:
            return False

        # Check if we have a recent successful health check
        # If health checks are enabled and we haven't had one recently, consider disconnected
        health_check_interval = getattr(self.config, "health_check_interval", 30)
        if health_check_interval > 0:
            try:
                current_time = asyncio.get_running_loop().time()
            except RuntimeError:
                # No event loop running, can't check time - assume connected if client is connected
                result: bool = cast(bool, self._client.is_connected)
                return result

            time_since_last_check = current_time - self._last_health_check

            # If it's been more than 2x the interval since last check, consider unhealthy
            if self._last_health_check > 0 and time_since_last_check > (health_check_interval * 2):
                self._logger.warning(
                    "Connection health check stale",
                    time_since_last_check=time_since_last_check,
                    health_check_interval=health_check_interval,
                )
                return False

            # If we've had too many consecutive failures, consider disconnected
            if self._consecutive_health_failures >= 3:
                self._logger.warning(
                    "Too many consecutive health check failures",
                    failures=self._consecutive_health_failures,
                )
                return False

        return True

    async def publish(self, subject: str, message: dict[str, Any]) -> None:
        """
        Publish message to NATS subject.

        Args:
            subject: NATS subject to publish to
            message: Message data (must be JSON-serializable)

        Raises:
            PublishError: If publishing fails or message validation fails

        AI: Validates message schema if validation is enabled to prevent malformed messages.
        """
        if not self.is_connected():
            raise PublishError("Not connected to NATS")

        try:
            # Validate subject if subject manager is available and validation is enabled
            if self.subject_manager and self.config.enable_subject_validation:
                try:
                    if not self.subject_manager.validate_subject(subject):
                        error_msg = f"Subject validation failed: {subject}"
                        self._logger.error(
                            "Subject validation failed",
                            subject=subject,
                            message_id=message.get("message_id"),
                        )
                        raise PublishError(error_msg)
                except SubjectValidationError as validation_error:
                    error_msg = f"Subject validation error: {str(validation_error)}"
                    self._logger.error(
                        "Subject validation error",
                        error=str(validation_error),
                        subject=subject,
                        message_id=message.get("message_id"),
                    )
                    raise PublishError(error_msg) from validation_error

            # Validate message schema if validation is enabled
            if self._enable_validation:
                try:
                    # Auto-detect message type based on structure
                    message_type = "event" if ("event_type" in message or "event_data" in message) else "chat"
                    validate_message(message, message_type=message_type)
                    self._logger.debug("Message validated", subject=subject, message_type=message_type)
                except ValueError as validation_error:
                    error_msg = f"Message validation failed: {str(validation_error)}"
                    self._logger.error(
                        "Message validation failed",
                        subject=subject,
                        error=str(validation_error),
                        message_keys=list(message.keys()) if isinstance(message, dict) else None,
                    )
                    raise PublishError(error_msg) from validation_error

            # Serialize message to JSON bytes
            message_bytes = json.dumps(message).encode("utf-8")

            # Publish to NATS
            await self._client.publish(subject, message_bytes)

            self._logger.debug("Published message", subject=subject, message_size=len(message_bytes))

        except PublishError:
            raise
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

                    # Validate message schema if validation is enabled
                    if self._enable_validation:
                        try:
                            # Auto-detect message type based on structure
                            message_type = (
                                "event" if ("event_type" in message_dict or "event_data" in message_dict) else "chat"
                            )
                            validate_message(message_dict, message_type=message_type)
                            self._logger.debug(
                                "Incoming message validated", subject=msg.subject, message_type=message_type
                            )
                        except ValueError as validation_error:
                            self._logger.error(
                                "Incoming message validation failed",
                                subject=msg.subject,
                                error=str(validation_error),
                                message_keys=list(message_dict.keys()) if isinstance(message_dict, dict) else None,
                            )
                            # Continue processing even if validation fails (log and proceed)
                            # This allows for backward compatibility with unvalidated messages

                    # Call user handler
                    await handler(message_dict)
                except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Message handler errors unpredictable, must handle gracefully
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

            result: dict[str, Any] = cast(dict[str, Any], reply_dict)
            return result

        except TimeoutError as e:
            self._logger.warning("Request timeout", subject=subject, timeout=timeout)
            raise TimeoutError(f"Request to {subject} timed out after {timeout}s") from e

        except Exception as e:
            self._logger.error("Request failed", subject=subject, error=str(e))
            raise RequestError(f"Request to {subject} failed: {e}") from e

    # NATS event callbacks
    def _error_callback(self, error: Exception) -> None:
        """
        Handle NATS errors.

        AI: Runs as fire-and-forget async task to prevent blocking NATS client.
        """
        # Fire-and-forget async task to prevent blocking
        try:
            asyncio.create_task(self._handle_error_async(error))
        except RuntimeError:
            # No event loop available - log synchronously
            self._logger.error("NATS error occurred", error=str(error))

    async def _handle_error_async(self, error: Exception) -> None:
        """Async handler for NATS connection errors."""
        try:
            self._logger.error("NATS error occurred", error=str(error))
        except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Error handler errors unpredictable
            self._logger.error("Error in async error handler", error=str(e), original_error=str(error))

    def _disconnected_callback(self) -> None:
        """
        Handle NATS disconnection.

        AI: Runs as fire-and-forget async task to prevent blocking NATS client.
        """
        # Fire-and-forget async task to prevent blocking
        try:
            asyncio.create_task(self._handle_disconnect_async())
        except RuntimeError:
            # No event loop available - log synchronously
            self._logger.warning("Disconnected from NATS")
            self._running = False

    async def _handle_disconnect_async(self) -> None:
        """Async handler for NATS disconnection events."""
        try:
            self._logger.warning("Disconnected from NATS")
            self._running = False
        except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Disconnect handler errors unpredictable
            self._logger.error("Error in async disconnect handler", error=str(e))

    def _reconnected_callback(self) -> None:
        """
        Handle NATS reconnection.

        AI: Runs as fire-and-forget async task to prevent blocking NATS client.
        """
        # Fire-and-forget async task to prevent blocking
        try:
            asyncio.create_task(self._handle_reconnect_async())
        except RuntimeError:
            # No event loop available - log synchronously
            self._logger.info("Reconnected to NATS")
            self._running = True
            self._consecutive_health_failures = 0

    async def _handle_reconnect_async(self) -> None:
        """Async handler for NATS reconnection events."""
        try:
            self._logger.info("Reconnected to NATS")
            self._running = True
            self._consecutive_health_failures = 0
            # Restart health monitoring
            await self._start_health_monitoring()
        except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Reconnect handler errors unpredictable
            self._logger.error("Error in async reconnect handler", error=str(e))

    async def _start_health_monitoring(self) -> None:
        """Start periodic health check monitoring task."""
        health_check_interval = getattr(self.config, "health_check_interval", 30)
        if health_check_interval <= 0:
            self._logger.debug("Health monitoring disabled (interval <= 0)")
            return

        # Cancel existing task if any
        if self._health_check_task and not self._health_check_task.done():
            self._health_check_task.cancel()
            try:
                await self._health_check_task
            except asyncio.CancelledError:
                pass

        # Start new health check task
        self._health_check_task = asyncio.create_task(self._health_check_loop())
        self._logger.info("Health monitoring started", interval_seconds=health_check_interval)

    async def _stop_health_monitoring(self) -> None:
        """Stop health check monitoring task."""
        if self._health_check_task and not self._health_check_task.done():
            self._health_check_task.cancel()
            try:
                await self._health_check_task
            except asyncio.CancelledError:
                pass
            self._health_check_task = None
        self._logger.debug("Health monitoring stopped")

    async def _health_check_loop(self) -> None:
        """Periodic health check loop using ping/pong."""
        health_check_interval = getattr(self.config, "health_check_interval", 30)

        while self._running:
            try:
                await sleep(health_check_interval)

                if not self._client or not self._running:
                    break

                # Perform health check via flush (lightweight ping/pong check)
                health_ok = await self._perform_health_check()

                if health_ok:
                    self._consecutive_health_failures = 0
                    self._last_health_check = asyncio.get_running_loop().time()
                else:
                    self._consecutive_health_failures += 1
                    self._logger.warning(
                        "Health check failed",
                        consecutive_failures=self._consecutive_health_failures,
                    )

            except asyncio.CancelledError:
                break
            except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Health check errors unpredictable, must continue loop
                self._logger.error("Error in health check loop", error=str(e))
                self._consecutive_health_failures += 1
                await sleep(health_check_interval)  # Wait before retrying

    async def _perform_health_check(self) -> bool:
        """
        Perform a single health check via flush.

        Returns:
            True if health check passed, False otherwise
        """
        if not self._client:
            return False

        try:
            # Try to flush any pending operations (lightweight check)
            await asyncio.wait_for(self._client.flush(), timeout=self._health_check_timeout)
            return True

        except TimeoutError:
            self._logger.warning("Health check timeout", timeout=self._health_check_timeout)
            return False
        except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Health check errors unpredictable, must return False
            self._logger.warning("Health check failed", error=str(e), error_type=type(e).__name__)
            return False


# Type annotation for protocol conformance
# Note: NATSMessageBroker implements MessageBroker protocol
# Mypy may not recognize structural subtyping here
