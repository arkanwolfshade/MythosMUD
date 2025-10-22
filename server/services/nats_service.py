"""
NATS service for MythosMUD chat system.

This module provides NATS pub/sub functionality for real-time chat messaging,
replacing the previous Redis-based implementation with a more lightweight
and Windows-native solution.
"""

import asyncio
import json
from collections.abc import Callable
from typing import Any

import nats

from ..config.models import NATSConfig
from ..logging.enhanced_logging_config import get_logger
from ..realtime.connection_state_machine import NATSConnectionStateMachine

logger = get_logger("nats")


class NATSService:
    """
    NATS service for handling pub/sub operations and real-time messaging.

    This service provides a clean interface for publishing chat messages
    and managing real-time communication between players using NATS.
    """

    def __init__(self, config: NATSConfig | dict[str, Any] | None = None):
        """
        Initialize NATS service with state machine.

        Args:
            config: NATS configuration (NATSConfig model, dict, or None for defaults)

        AI: State machine tracks connection lifecycle and prevents invalid state transitions.
        AI: Accepts dict for backward compatibility but converts to Pydantic model for type safety.
        """
        # Convert dict to Pydantic model or use default if None
        if isinstance(config, dict):
            self.config = NATSConfig(**config)
        elif config is None:
            self.config = NATSConfig()
        else:
            self.config = config

        self.nc: nats.NATS | None = None
        self.subscriptions: dict[str, Any] = {}
        self._running = False
        self._connection_retries = 0
        self._max_retries = self.config.max_reconnect_attempts

        # NEW: Connection state machine (CRITICAL-1)
        # AI: FSM provides robust connection management with automatic recovery
        self.state_machine = NATSConnectionStateMachine(
            connection_id="nats-primary", max_reconnect_attempts=self._max_retries
        )

    async def connect(self) -> bool:
        """
        Connect to NATS server with state machine tracking.

        Returns:
            True if connection successful, False otherwise

        AI: State machine tracks connection lifecycle and enables circuit breaker integration.
        """
        # Check if connection attempt is allowed by state machine
        if not self.state_machine.can_attempt_connection():
            logger.warning(
                "Connection attempt blocked by state machine",
                current_state=self.state_machine.current_state.id,
                reconnect_attempts=self.state_machine.reconnect_attempts,
            )
            return False

        # Transition to connecting state
        if self.state_machine.current_state.id == "disconnected":
            self.state_machine.connect()
        elif self.state_machine.current_state.id == "reconnecting":
            # Already in reconnecting, continue
            pass

        try:
            # Get NATS connection URL from config (Pydantic attribute access)
            nats_url = self.config.url

            # Connection options (Pydantic attribute access)
            connect_options = {
                "reconnect_time_wait": self.config.reconnect_time_wait,
                "max_reconnect_attempts": self._max_retries,
                "connect_timeout": self.config.connect_timeout,
                "ping_interval": self.config.ping_interval,
                "max_outstanding_pings": self.config.max_outstanding_pings,
            }

            logger.info("Connecting to NATS server", url=nats_url, state=self.state_machine.current_state.id)

            # Connect to NATS
            self.nc = await nats.connect(nats_url, **connect_options)

            # Set up connection event handlers (if available)
            try:
                self.nc.add_error_listener(self._on_error)
                self.nc.add_disconnect_listener(self._on_disconnect)
                self.nc.add_reconnect_listener(self._on_reconnect)
            except AttributeError:
                # Event listeners not available in this version of nats-py
                logger.debug("Event listeners not available in nats-py version")

            self._running = True
            self._connection_retries = 0

            # Transition to connected state
            self.state_machine.connected_successfully()

            logger.info(
                "Connected to NATS server successfully",
                url=nats_url,
                state=self.state_machine.current_state.id,
            )
            return True

        except Exception as e:
            self._connection_retries += 1

            # Transition to failed state
            self.state_machine.connection_failed(e)

            logger.error(
                "Failed to connect to NATS server",
                error=str(e),
                url=self.config.url,
                retry_count=self._connection_retries,
                max_retries=self._max_retries,
                state=self.state_machine.current_state.id,
            )

            # Check if circuit breaker should be triggered
            if self.state_machine.should_open_circuit():
                if self.state_machine.current_state.id == "disconnected":
                    # Need to be in reconnecting to open circuit
                    self.state_machine.start_reconnect()
                self.state_machine.open_circuit()
                logger.critical(
                    "NATS connection circuit breaker opened",
                    state=self.state_machine.current_state.id,
                )

            return False

    async def disconnect(self):
        """
        Disconnect from NATS and cleanup resources with state machine tracking.

        AI: State machine transitions to disconnected, enabling clean reconnection.
        """
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

                # Transition to disconnected state
                if self.state_machine.current_state.id in ["connected", "degraded"]:
                    self.state_machine.disconnect()

                logger.info("Disconnected from NATS server", state=self.state_machine.current_state.id)
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
            logger.debug(f"=== NATS SERVICE DEBUG: Publishing to subject: {subject} ===")
            logger.debug(f"NATS client (nc): {self.nc}")
            logger.debug(f"NATS running: {self._running}")
            logger.debug(f"Message data: {data}")

            if not self.nc or not self._running:
                logger.error("NATS client not connected")
                return False

            # Serialize message data
            message_json = json.dumps(data)
            message_bytes = message_json.encode("utf-8")

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
                error_type=type(e).__name__,
                subject=subject,
                message_id=data.get("message_id"),
            )
            logger.debug("=== NATS SERVICE DEBUG: Exception details ===")
            logger.debug(f"Exception type: {type(e).__name__}")
            logger.debug(f"Exception message: {str(e)}")
            logger.debug(f"Exception args: {e.args}")
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
                    data = msg.data.decode("utf-8")
                    message_data = json.loads(data)

                    # Call the registered callback (await if it's async)
                    if asyncio.iscoroutinefunction(callback):
                        await callback(message_data)
                    else:
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
            request_bytes = request_json.encode("utf-8")

            # Send request and wait for response
            response = await self.nc.request(subject, request_bytes, timeout=timeout)

            # Decode response data
            response_data = response.data.decode("utf-8")
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

    # Event handlers with state machine integration
    def _on_error(self, error):
        """
        Handle NATS connection errors with state machine tracking.

        AI: Errors may trigger degradation or reconnection.
        """
        logger.error("NATS connection error", error=str(error), state=self.state_machine.current_state.id)

        # Degrade connection if currently connected
        if self.state_machine.current_state.id == "connected":
            self.state_machine.degrade()

    def _on_disconnect(self):
        """
        Handle NATS disconnection events with state machine tracking.

        AI: Disconnection triggers reconnection attempt.
        """
        logger.warning("NATS client disconnected", state=self.state_machine.current_state.id)
        self._running = False

        # Transition to reconnecting if we were connected
        if self.state_machine.current_state.id in ["connected", "degraded"]:
            self.state_machine.disconnect()
            self.state_machine.start_reconnect()

    def _on_reconnect(self):
        """
        Handle NATS reconnection events with state machine tracking.

        AI: Successful reconnection transitions to connected state.
        """
        logger.info("NATS client reconnected", state=self.state_machine.current_state.id)
        self._running = True
        self._connection_retries = 0

        # Transition to connected if we were reconnecting
        if self.state_machine.current_state.id == "reconnecting":
            self.state_machine.connected_successfully()
        elif self.state_machine.current_state.id == "degraded":
            self.state_machine.recover()

    def get_connection_stats(self) -> dict[str, Any]:
        """
        Get connection statistics from state machine.

        Returns:
            Dictionary with connection state and metrics

        AI: For monitoring dashboards and health checks.
        """
        return {
            "nats_connected": self._running,
            **self.state_machine.get_stats(),
        }


# Global NATS service instance
nats_service = NATSService()
