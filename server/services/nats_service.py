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


class NATSMetrics:
    """NATS-specific metrics collection for monitoring and alerting."""

    def __init__(self):
        self.publish_count = 0
        self.publish_errors = 0
        self.subscribe_count = 0
        self.subscribe_errors = 0
        self.message_processing_times: list[float] = []
        self.connection_health_score = 100.0
        self.batch_flush_count = 0
        self.batch_flush_errors = 0
        self.pool_utilization = 0.0

    def record_publish(self, success: bool, processing_time: float):
        """Record publish operation metrics."""
        self.publish_count += 1
        if not success:
            self.publish_errors += 1
        self.message_processing_times.append(processing_time)

        # Keep only last 1000 processing times for rolling average
        if len(self.message_processing_times) > 1000:
            self.message_processing_times = self.message_processing_times[-1000:]

    def record_subscribe(self, success: bool):
        """Record subscribe operation metrics."""
        self.subscribe_count += 1
        if not success:
            self.subscribe_errors += 1

    def record_batch_flush(self, success: bool, message_count: int):
        """Record batch flush operation metrics."""
        self.batch_flush_count += 1
        if not success:
            self.batch_flush_errors += 1

    def update_connection_health(self, health_score: float):
        """Update connection health score (0-100)."""
        self.connection_health_score = max(0.0, min(100.0, health_score))

    def update_pool_utilization(self, utilization: float):
        """Update connection pool utilization (0-1)."""
        self.pool_utilization = max(0.0, min(1.0, utilization))

    def get_metrics(self) -> dict[str, Any]:
        """Get comprehensive NATS metrics."""
        avg_processing_time = (
            sum(self.message_processing_times) / len(self.message_processing_times)
            if self.message_processing_times
            else 0
        )

        return {
            "publish_count": self.publish_count,
            "publish_error_rate": self.publish_errors / max(self.publish_count, 1),
            "subscribe_count": self.subscribe_count,
            "subscribe_error_rate": self.subscribe_errors / max(self.subscribe_count, 1),
            "avg_processing_time_ms": avg_processing_time * 1000,
            "connection_health": self.connection_health_score,
            "pool_utilization": self.pool_utilization,
            "batch_flush_count": self.batch_flush_count,
            "batch_flush_error_rate": self.batch_flush_errors / max(self.batch_flush_count, 1),
            "processing_time_samples": len(self.message_processing_times),
        }


class NATSService:
    """
    NATS service for handling pub/sub operations and real-time messaging.

    This service provides a clean interface for publishing chat messages
    and managing real-time communication between players using NATS.
    """

    def __init__(self, config: NATSConfig | dict[str, Any] | None = None):
        """
        Initialize NATS service with state machine and connection pooling.

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

        # Connection pooling for high-throughput scenarios
        self.connection_pool: list[nats.NATS] = []
        self.pool_size = getattr(self.config, "connection_pool_size", 5)
        self.available_connections: asyncio.Queue[nats.NATS] = asyncio.Queue()
        self._pool_initialized = False

        # Message batching for bulk operations
        self.message_batch: list[tuple[str, dict[str, Any]]] = []
        self.batch_size = getattr(self.config, "batch_size", 100)
        self.batch_timeout = getattr(self.config, "batch_timeout", 0.1)  # 100ms
        self._batch_task: asyncio.Task | None = None

        # NATS metrics collection
        self.metrics = NATSMetrics()

        # Legacy single connection for backward compatibility
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

            # Initialize connection pool for high-throughput scenarios
            await self._initialize_connection_pool()

            logger.info(
                "Connected to NATS server successfully",
                url=nats_url,
                state=self.state_machine.current_state.id,
                pool_size=self.pool_size,
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
        Disconnect from NATS with graceful shutdown and message draining.

        AI: State machine transitions to disconnected, enabling clean reconnection.
        """
        try:
            # Flush any pending batched messages
            if self.message_batch:
                logger.info("Flushing pending batched messages before shutdown", batch_size=len(self.message_batch))
                await self._flush_batch()

            if self.nc:
                # Drain in-flight messages before closing subscriptions
                for subject, subscription in self.subscriptions.items():
                    try:
                        await subscription.drain()  # Wait for in-flight messages
                        logger.debug("Subscription drained", subject=subject)
                    except Exception as e:
                        logger.warning("Error draining subscription", subject=subject, error=str(e))

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

            # Clean up connection pool
            if self._pool_initialized:
                await self._cleanup_connection_pool()

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
        start_time = asyncio.get_event_loop().time()
        success = False

        try:
            # Validate connection state
            if not self.nc or not self._running:
                logger.error("NATS client not connected", subject=subject)
                return False

            # Serialize message data using thread pool for CPU-bound operation
            loop = asyncio.get_running_loop()
            message_bytes = await loop.run_in_executor(None, lambda: json.dumps(data).encode("utf-8"))

            # Publish to NATS subject
            await self.nc.publish(subject, message_bytes)
            success = True

            logger.debug(
                "Message published to NATS subject",
                subject=subject,
                message_id=data.get("message_id"),
                sender_id=data.get("sender_id"),
                data_size=len(message_bytes),
                nats_client_connected=self.nc is not None,
                service_running=self._running,
            )

        except Exception as e:
            logger.error(
                "Failed to publish message to NATS subject",
                error=str(e),
                error_type=type(e).__name__,
                subject=subject,
                message_id=data.get("message_id"),
                exception_args=str(e.args) if e.args else None,
            )
        finally:
            # Record metrics
            processing_time = asyncio.get_event_loop().time() - start_time
            self.metrics.record_publish(success, processing_time)

        return success

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
                    # Decode message data using thread pool for CPU-bound operation
                    loop = asyncio.get_running_loop()
                    message_data = await loop.run_in_executor(None, lambda: json.loads(msg.data.decode("utf-8")))

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

            # Record metrics
            self.metrics.record_subscribe(True)

            logger.info("Subscribed to NATS subject", subject=subject)
            return True

        except Exception as e:
            # Record metrics
            self.metrics.record_subscribe(False)
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

            # Serialize request data using thread pool
            loop = asyncio.get_running_loop()
            request_bytes = await loop.run_in_executor(None, lambda: json.dumps(data).encode("utf-8"))

            # Send request and wait for response
            response = await self.nc.request(subject, request_bytes, timeout=timeout)

            # Decode response data using thread pool
            response_json = await loop.run_in_executor(None, lambda: json.loads(response.data.decode("utf-8")))

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
            "pool_initialized": self._pool_initialized,
            "pool_size": self.pool_size,
            "available_connections": self.available_connections.qsize(),
            **self.state_machine.get_stats(),
            **self.metrics.get_metrics(),
        }

    async def _initialize_connection_pool(self):
        """Initialize connection pool for high-throughput scenarios."""
        if self._pool_initialized:
            return

        try:
            nats_url = self.config.url
            connect_options = {
                "reconnect_time_wait": self.config.reconnect_time_wait,
                "max_reconnect_attempts": self._max_retries,
                "connect_timeout": self.config.connect_timeout,
                "ping_interval": self.config.ping_interval,
                "max_outstanding_pings": self.config.max_outstanding_pings,
            }

            # Create pool connections
            for _i in range(self.pool_size):
                connection = await nats.connect(nats_url, **connect_options)
                self.connection_pool.append(connection)
                await self.available_connections.put(connection)

            self._pool_initialized = True

            logger.info(
                "NATS connection pool initialized",
                pool_size=self.pool_size,
                url=nats_url,
            )

        except Exception as e:
            logger.error(
                "Failed to initialize NATS connection pool",
                error=str(e),
                pool_size=self.pool_size,
            )
            # Continue with single connection if pool fails
            self._pool_initialized = False

    async def _get_connection(self) -> nats.NATS:
        """Get connection from pool or fallback to single connection."""
        if self._pool_initialized and not self.available_connections.empty():
            return await self.available_connections.get()
        return self.nc

    async def _return_connection(self, connection: nats.NATS):
        """Return connection to pool."""
        if self._pool_initialized and connection in self.connection_pool:
            await self.available_connections.put(connection)

    async def publish_with_pool(self, subject: str, data: dict[str, Any]) -> bool:
        """
        Publish message using connection pool for high-throughput scenarios.

        Args:
            subject: NATS subject name
            data: Message data to publish

        Returns:
            True if published successfully, False otherwise
        """
        connection = None
        try:
            connection = await self._get_connection()
            if not connection:
                logger.error("No NATS connection available", subject=subject)
                return False

            # Serialize message data using thread pool for CPU-bound operation
            loop = asyncio.get_running_loop()
            message_bytes = await loop.run_in_executor(None, lambda: json.dumps(data).encode("utf-8"))

            # Publish to NATS subject
            await connection.publish(subject, message_bytes)

            logger.debug(
                "Message published via connection pool",
                subject=subject,
                message_id=data.get("message_id"),
                sender_id=data.get("sender_id"),
                data_size=len(message_bytes),
            )

            return True

        except Exception as e:
            logger.error(
                "Failed to publish message via connection pool",
                error=str(e),
                subject=subject,
                message_id=data.get("message_id"),
            )
            return False
        finally:
            if connection:
                await self._return_connection(connection)

    async def _cleanup_connection_pool(self):
        """Clean up connection pool during shutdown."""
        try:
            # Close all connections in pool
            for connection in self.connection_pool:
                try:
                    await connection.close()
                except Exception as e:
                    logger.warning("Error closing pool connection", error=str(e))

            # Clear pool
            self.connection_pool.clear()
            self._pool_initialized = False

            logger.info("Connection pool cleaned up", pool_size=len(self.connection_pool))

        except Exception as e:
            logger.error("Error cleaning up connection pool", error=str(e))

    async def publish_batch(self, subject: str, data: dict[str, Any]) -> bool:
        """
        Add message to batch for efficient bulk publishing.

        Args:
            subject: NATS subject name
            data: Message data to publish

        Returns:
            True if added to batch successfully, False otherwise
        """
        try:
            # Add message to batch
            self.message_batch.append((subject, data))

            # Flush batch if size threshold reached
            if len(self.message_batch) >= self.batch_size:
                await self._flush_batch()
            elif not self._batch_task:
                # Start timeout task for batch
                self._batch_task = asyncio.create_task(self._batch_timeout())

            logger.debug(
                "Message added to batch",
                subject=subject,
                batch_size=len(self.message_batch),
                message_id=data.get("message_id"),
            )

            return True

        except Exception as e:
            logger.error(
                "Failed to add message to batch",
                error=str(e),
                subject=subject,
                message_id=data.get("message_id"),
            )
            return False

    async def _batch_timeout(self):
        """Handle batch timeout for low-traffic scenarios."""
        try:
            await asyncio.sleep(self.batch_timeout)
            await self._flush_batch()
        except asyncio.CancelledError:
            # Task was cancelled, which is expected
            pass
        finally:
            self._batch_task = None

    async def _flush_batch(self):
        """Flush all batched messages efficiently."""
        if not self.message_batch:
            return

        try:
            # Group messages by subject for efficient publishing
            grouped_messages = {}
            for subject, data in self.message_batch:
                if subject not in grouped_messages:
                    grouped_messages[subject] = []
                grouped_messages[subject].append(data)

            # Publish each group using connection pool
            for subject, messages in grouped_messages.items():
                batch_data = {
                    "messages": messages,
                    "count": len(messages),
                    "batch_timestamp": asyncio.get_event_loop().time(),
                }

                # Use connection pool for batch publishing
                await self.publish_with_pool(subject, batch_data)

            # Record batch flush metrics
            self.metrics.record_batch_flush(True, len(self.message_batch))

            logger.info(
                "Message batch flushed",
                total_messages=len(self.message_batch),
                unique_subjects=len(grouped_messages),
            )

        except Exception as e:
            logger.error(
                "Failed to flush message batch",
                error=str(e),
                batch_size=len(self.message_batch),
            )
        finally:
            # Clear batch and cancel timeout task
            self.message_batch.clear()
            if self._batch_task and not self._batch_task.done():
                self._batch_task.cancel()
                self._batch_task = None


# Global NATS service instance
nats_service = NATSService()
