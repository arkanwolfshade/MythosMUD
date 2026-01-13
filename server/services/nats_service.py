"""
NATS service for MythosMUD chat system.

This module provides NATS pub/sub functionality for real-time chat messaging,
replacing the previous Redis-based implementation with a more lightweight
and Windows-native solution.
"""

# pylint: disable=too-many-instance-attributes,too-many-lines  # Reason: NATS service requires many state tracking and configuration attributes. NATS service requires extensive NATS integration logic for comprehensive real-time messaging system.

import asyncio
import json
import ssl
from collections import deque
from collections.abc import Callable
from pathlib import Path
from typing import Any

import nats
from anyio import sleep

from ..config.models import NATSConfig
from ..realtime.connection_state_machine import NATSConnectionStateMachine
from ..structured_logging.enhanced_logging_config import get_logger
from .nats_exceptions import (
    NATSPublishError,
    NATSSubscribeError,
)
from .nats_subject_manager import NATSSubjectManager, SubjectValidationError

logger = get_logger("nats")


class NATSMetrics:  # pylint: disable=too-many-instance-attributes  # Reason: Metrics class requires many fields to capture complete NATS metrics
    """NATS-specific metrics collection for monitoring and alerting."""

    def __init__(self) -> None:
        self.publish_count = 0
        self.publish_errors = 0
        self.subscribe_count = 0
        self.subscribe_errors = 0
        # Use deque with maxlen for automatic rotation - more memory efficient than list slicing
        self.message_processing_times: deque[float] = deque(maxlen=1000)
        self.connection_health_score = 100.0
        self.batch_flush_count = 0
        self.batch_flush_errors = 0
        self.pool_utilization = 0.0

    def record_publish(self, success: bool, processing_time: float):
        """Record publish operation metrics."""
        self.publish_count += 1
        if not success:
            self.publish_errors += 1
        # Deque automatically rotates when maxlen is reached - no manual slicing needed
        self.message_processing_times.append(processing_time)

    def record_subscribe(self, success: bool):
        """Record subscribe operation metrics."""
        self.subscribe_count += 1
        if not success:
            self.subscribe_errors += 1

    def record_batch_flush(self, success: bool, _message_count: int):
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
        # Deque supports len() and iteration like a list
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


class NATSService:  # pylint: disable=too-many-instance-attributes  # Reason: NATS service requires many state tracking and configuration attributes
    """
    NATS service for handling pub/sub operations and real-time messaging.

    This service provides a clean interface for publishing chat messages
    and managing real-time communication between players using NATS.

    CONNECTION POOLING:
    The service uses connection pooling by default for high-throughput scenarios.
    - Default pool size: 5 connections (configurable via NATSConfig.connection_pool_size)
    - Connections are managed via asyncio.Queue for thread-safe access
    - Pool is initialized lazily on first use
    - All publish operations automatically use pooled connections

    MESSAGE BATCHING:
    Supports message batching for bulk operations to reduce network overhead.
    - Default batch size: 100 messages (configurable via NATSConfig.batch_size)
    - Default batch timeout: 100ms (configurable via NATSConfig.batch_timeout)
    - Batching improves throughput for high-volume message scenarios

    AI Agent: Connection pooling follows NATS best practices from nats.mdc Section 1.3.
              The nats-py client library also provides built-in connection management
              on top of our application-level pooling for optimal performance.
    """

    def __init__(self, config: NATSConfig | dict[str, Any] | None = None, subject_manager=None):
        """
        Initialize NATS service with state machine and connection pooling.

        Args:
            config: NATS configuration (NATSConfig model, dict, or None for defaults)
            subject_manager: NATSSubjectManager instance (optional, for subject validation)

        AI: State machine tracks connection lifecycle and prevents invalid state transitions.
        AI: Accepts dict and converts to Pydantic model for type safety.
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

        # Primary connection (used for subscriptions and fallback)
        self.nc: nats.NATS | None = None
        self.subscriptions: dict[str, Any] = {}
        self._running = False
        self._connection_retries = 0
        self._max_retries = self.config.max_reconnect_attempts

        # Health monitoring
        self._health_check_task: asyncio.Task | None = None
        self._last_health_check: float = 0.0
        self._consecutive_health_failures = 0
        self._health_check_timeout = 5.0  # seconds

        # Tracked background tasks for proper lifecycle management
        # AnyIO Pattern: Track all background tasks for proper cleanup
        self._background_tasks: set[asyncio.Task] = set()

        # NEW: Connection state machine (CRITICAL-1)
        # AI: FSM provides robust connection management with automatic recovery
        self.state_machine = NATSConnectionStateMachine(
            connection_id="nats-primary", max_reconnect_attempts=self._max_retries
        )

        # NATSSubjectManager for subject validation (optional)
        if subject_manager is None and self.config.enable_subject_validation:
            # Create subject manager with configuration
            subject_manager = NATSSubjectManager(strict_validation=self.config.strict_subject_validation)
        self.subject_manager = subject_manager

    def _check_connection_allowed(self) -> bool:
        """Check if connection attempt is allowed by state machine."""
        if not self.state_machine.can_attempt_connection():
            logger.warning(
                "Connection attempt blocked by state machine",
                current_state=self.state_machine.current_state.id,
                reconnect_attempts=self.state_machine.reconnect_attempts,
            )
            return False

        if self.state_machine.current_state.id == "disconnected":
            self.state_machine.connect()
        elif self.state_machine.current_state.id == "reconnecting":
            pass

        return True

    def _build_connect_options(self) -> dict[str, Any]:
        """Build connection options for NATS."""
        connect_options: dict[str, Any] = {
            "reconnect_time_wait": self.config.reconnect_time_wait,
            "max_reconnect_attempts": self._max_retries,
            "connect_timeout": self.config.connect_timeout,
            "ping_interval": self.config.ping_interval,
            "max_outstanding_pings": self.config.max_outstanding_pings,
        }
        return connect_options

    def _configure_tls(self, connect_options: dict[str, Any]) -> None:
        """Configure TLS settings for NATS connection."""
        if not self.config.tls_enabled:
            return

        ssl_context = ssl.create_default_context()

        if self.config.tls_cert_file and self.config.tls_key_file:
            cert_path = Path(self.config.tls_cert_file)
            key_path = Path(self.config.tls_key_file)
            ssl_context.load_cert_chain(cert_path, key_path)
            logger.debug("Loaded TLS client certificate", cert_file=str(cert_path), key_file=str(key_path))

        if self.config.tls_ca_file:
            ca_path = Path(self.config.tls_ca_file)
            ssl_context.load_verify_locations(ca_path)
            logger.debug("Loaded TLS CA certificate", ca_file=str(ca_path))

        if self.config.tls_verify:
            ssl_context.check_hostname = True
            ssl_context.verify_mode = ssl.CERT_REQUIRED
        else:
            ssl_context.check_hostname = False
            ssl_context.verify_mode = ssl.CERT_NONE
            logger.warning("TLS verification disabled - using unverified certificates")

        connect_options["tls"] = ssl_context
        logger.info("TLS enabled for NATS connection", verify=self.config.tls_verify)

    def _setup_connection_handlers(self) -> None:
        """Set up connection event handlers."""
        if self.nc is None:
            return
        try:
            self.nc.add_error_listener(self._on_error)
            self.nc.add_disconnect_listener(self._on_disconnect)
            self.nc.add_reconnect_listener(self._on_reconnect)
        except AttributeError:
            logger.debug("Event listeners not available in nats-py version")

    async def connect(self) -> bool:
        """
        Connect to NATS server with state machine tracking.

        Returns:
            True if connection successful, False otherwise

        AI: State machine tracks connection lifecycle and enables circuit breaker integration.
        """
        if not self._check_connection_allowed():
            return False

        try:
            nats_url = self.config.url
            connect_options = self._build_connect_options()
            self._configure_tls(connect_options)

            logger.info(
                "Connecting to NATS server",
                url=nats_url,
                tls_enabled=self.config.tls_enabled,
                state=self.state_machine.current_state.id,
            )

            self.nc = await nats.connect(nats_url, **connect_options)
            self._setup_connection_handlers()

            self._running = True
            self._connection_retries = 0
            self.state_machine.connected_successfully()
            await self._initialize_connection_pool()

            # Start health check monitoring task
            await self._start_health_monitoring()

            logger.info(
                "Connected to NATS server successfully",
                url=nats_url,
                state=self.state_machine.current_state.id,
                pool_size=self.pool_size,
            )
            return True

        except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: NATS connection errors unpredictable, must handle all errors
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
        AnyIO Pattern: Cancels all background tasks for proper cleanup.
        """
        try:
            # Cancel all background tasks first (AnyIO Pattern: structured cleanup)
            await self._cancel_background_tasks()

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
                    except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Subscription drain errors unpredictable, must not fail cleanup
                        logger.warning("Error draining subscription", subject=subject, error=str(e))

                # Close all subscriptions
                for subject, subscription in self.subscriptions.items():
                    try:
                        await subscription.unsubscribe()
                        logger.debug("Unsubscribed from NATS subject", subject=subject)
                    except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Unsubscribe errors unpredictable, must not fail cleanup
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

            # Stop health check monitoring
            await self._stop_health_monitoring()

        except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Disconnect errors unpredictable, must handle gracefully
            logger.error("Error disconnecting from NATS server", error=str(e))

    async def _start_health_monitoring(self):
        """Start periodic health check monitoring task."""
        health_check_interval = getattr(self.config, "health_check_interval", 30)
        if health_check_interval <= 0:
            logger.debug("Health monitoring disabled (interval <= 0)")
            return

        # Cancel existing task if any
        if self._health_check_task and not self._health_check_task.done():
            self._health_check_task.cancel()
            try:
                await self._health_check_task
            except asyncio.CancelledError:
                pass

        # Start new health check task with proper tracking
        # AnyIO Pattern: Track long-running background tasks for proper cleanup
        self._health_check_task = self._create_tracked_task(
            self._health_check_loop(), task_name="nats_health_check", task_type="lifecycle"
        )
        logger.info("Health monitoring started", interval_seconds=health_check_interval)

    async def _cancel_background_tasks(self):
        """
        Cancel all tracked background tasks for proper cleanup.

        AnyIO Pattern: Structured cleanup of all background tasks ensures
        no orphaned tasks remain after shutdown.
        """
        if not self._background_tasks:
            return

        logger.debug("Cancelling background tasks", task_count=len(self._background_tasks))

        # Cancel all background tasks
        for task in list(self._background_tasks):
            if not task.done():
                task.cancel()

        # Wait for tasks to complete with timeout
        if self._background_tasks:
            try:
                _done, pending = await asyncio.wait(
                    self._background_tasks, timeout=2.0, return_when=asyncio.ALL_COMPLETED
                )

                # Force cancel any remaining tasks
                if pending:
                    for task in pending:
                        if not task.done():
                            task.cancel()
                    # Give them a brief moment to cancel
                    try:
                        await asyncio.wait_for(asyncio.gather(*pending, return_exceptions=True), timeout=0.5)
                    except (TimeoutError, Exception):  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Task cancellation errors unpredictable, must abandon remaining tasks on any error during shutdown
                        pass  # Abandon remaining tasks

            except (RuntimeError, asyncio.CancelledError) as e:
                logger.debug("Error during background task cancellation", error=str(e))
            finally:
                self._background_tasks.clear()

        logger.debug("Background tasks cancelled")

    async def _stop_health_monitoring(self):
        """Stop health check monitoring task."""
        if self._health_check_task and not self._health_check_task.done():
            self._health_check_task.cancel()
            try:
                await self._health_check_task
            except asyncio.CancelledError:
                pass
            self._health_check_task = None
        logger.debug("Health monitoring stopped")

    async def _health_check_loop(self):
        """Periodic health check loop using ping/pong."""
        health_check_interval = getattr(self.config, "health_check_interval", 30)

        while self._running:
            try:
                await sleep(health_check_interval)

                if not self.nc or not self._running:
                    break

                # Perform health check via ping/pong
                health_ok = await self._perform_health_check()

                if health_ok:
                    self._consecutive_health_failures = 0
                    self._last_health_check = asyncio.get_running_loop().time()
                    # Update health score in metrics
                    self.metrics.update_connection_health(100.0)
                else:
                    self._consecutive_health_failures += 1
                    # Degrade health score based on failures
                    health_score = max(0.0, 100.0 - (self._consecutive_health_failures * 20))
                    self.metrics.update_connection_health(health_score)

                    # Transition to degraded state if too many failures
                    if self._consecutive_health_failures >= 3:
                        if self.state_machine.current_state.id == "connected":
                            self.state_machine.degrade()
                            logger.warning(
                                "NATS connection degraded due to health check failures",
                                failures=self._consecutive_health_failures,
                            )

            except asyncio.CancelledError:
                break
            except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Health check errors unpredictable, must continue loop
                logger.error("Error in health check loop", error=str(e))
                self._consecutive_health_failures += 1
                await sleep(health_check_interval)  # Wait before retrying

    async def _perform_health_check(self) -> bool:
        """
        Perform a single health check via ping/pong.

        Returns:
            True if health check passed, False otherwise
        """
        if not self.nc:
            return False

        try:
            # Use NATS ping/pong mechanism for health check
            # The nats-py client has built-in ping handling
            # We can check if the connection is still alive by attempting a simple operation
            # or checking connection state

            # Try to flush any pending operations (lightweight check)
            await asyncio.wait_for(self.nc.flush(), timeout=self._health_check_timeout)
            return True

        except TimeoutError:
            logger.warning("Health check timeout", timeout=self._health_check_timeout)
            return False
        except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Health check errors unpredictable, must return False
            logger.warning("Health check failed", error=str(e), error_type=type(e).__name__)
            return False

    async def publish(self, subject: str, data: dict[str, Any]) -> None:
        """
        Publish a message to a NATS subject using connection pool.

        Args:
            subject: NATS subject name (e.g., 'chat.say', 'chat.global')
            data: Message data to publish

        Raises:
            NATSPublishError: If publishing fails or connection pool is not available

        AI: Requires connection pool to be initialized. Raises exceptions instead of
            returning False for better error handling.
        """
        # Require connection pool - fail if not available
        if not self._pool_initialized:
            error_msg = "Connection pool not initialized - cannot publish"
            logger.error("Connection pool not initialized", subject=subject)
            raise NATSPublishError(error_msg, subject=subject)

        if self.available_connections.empty():
            error_msg = "No available connections in pool"
            logger.error("No available connections in pool", subject=subject, pool_size=self.pool_size)
            raise NATSPublishError(error_msg, subject=subject)

        # Use connection pool
        await self.publish_with_pool(subject, data)

    async def _decode_message_data(self, msg: Any) -> dict[str, Any]:
        """Decode message data from NATS message."""
        loop = asyncio.get_running_loop()
        return await loop.run_in_executor(None, lambda: json.loads(msg.data.decode("utf-8")))

    async def _call_callback(self, callback: Callable[[dict[str, Any]], None], message_data: dict[str, Any]) -> None:
        """Call the registered callback, handling both async and sync callbacks."""
        if asyncio.iscoroutinefunction(callback):
            await callback(message_data)
        else:
            callback(message_data)

    async def _acknowledge_message(self, msg: Any, subject: str, message_data: dict[str, Any]) -> bool:
        """Acknowledge message if manual ack is enabled. Returns True if acknowledged."""
        if not hasattr(msg, "ack"):
            return False

        try:
            await msg.ack()
            logger.debug(
                "Message acknowledged",
                subject=subject,
                message_id=message_data.get("message_id"),
            )
            return True
        except Exception as ack_error:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Message ack errors unpredictable, must log but continue
            logger.error(
                "Failed to acknowledge message",
                error=str(ack_error),
                subject=subject,
                message_id=message_data.get("message_id"),
            )
            return False

    async def _negatively_acknowledge_message(self, msg: Any, subject: str) -> None:
        """Negatively acknowledge message if manual ack is enabled."""
        if not hasattr(msg, "nak"):
            return

        try:
            await msg.nak()
        except Exception as nak_error:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Message nak errors unpredictable, must log but continue
            logger.error("Failed to negatively acknowledge message", error=str(nak_error), subject=subject)

    async def subscribe(self, subject: str, callback: Callable[[dict[str, Any]], None]) -> None:
        """
        Subscribe to a NATS subject and register a callback for incoming messages.

        Args:
            subject: NATS subject name to subscribe to
            callback: Function to call when messages are received (signature: async def callback(message_data: dict))

        Raises:
            NATSSubscribeError: If subscription fails

        AI: When manual_ack is enabled, messages are acknowledged after successful processing
            and negatively acknowledged on failure. This provides at-least-once delivery semantics.
            Raises exceptions instead of returning False for better error handling.
        """
        try:
            if not self.nc or not self._running:
                error_msg = "NATS client not connected"
                logger.error("NATS client not connected")
                raise NATSSubscribeError(error_msg, subject=subject)

            manual_ack_enabled = getattr(self.config, "manual_ack", False)

            async def message_handler(msg: Any) -> None:
                message_acknowledged = False
                try:
                    message_data = await self._decode_message_data(msg)
                    await self._call_callback(callback, message_data)

                    if manual_ack_enabled:
                        message_acknowledged = await self._acknowledge_message(msg, subject, message_data)

                    logger.debug(
                        "Message received from NATS subject",
                        subject=subject,
                        message_id=message_data.get("message_id"),
                        sender_id=message_data.get("sender_id"),
                        acknowledged=message_acknowledged,
                    )

                except json.JSONDecodeError as e:
                    logger.error("Failed to decode NATS message", error=str(e), subject=subject)
                    if manual_ack_enabled:
                        await self._negatively_acknowledge_message(msg, subject)
                except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Message handling errors unpredictable, must handle gracefully
                    logger.error("Error handling NATS message", error=str(e), subject=subject)
                    if manual_ack_enabled:
                        await self._negatively_acknowledge_message(msg, subject)

            subscription = await self.nc.subscribe(subject, cb=message_handler)
            self.subscriptions[subject] = subscription

            self.metrics.record_subscribe(True)

            logger.info(
                "Subscribed to NATS subject",
                subject=subject,
                manual_ack=manual_ack_enabled,
            )

        except NATSSubscribeError:
            raise
        except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Subscribe errors unpredictable, must record metrics and handle
            # Record metrics
            self.metrics.record_subscribe(False)
            error_msg = f"Failed to subscribe to NATS subject: {str(e)}"
            logger.error("Failed to subscribe to NATS subject", error=str(e), subject=subject)
            raise NATSSubscribeError(error_msg, subject=subject, error=e) from e

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

        except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Unsubscribe errors unpredictable, must return False
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
        except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Request errors unpredictable, must return None
            logger.error("Failed to send request", error=str(e), subject=subject)
            return None

    def is_connected(self) -> bool:
        """
        Check if NATS client is connected and healthy.

        Returns:
            True if connected and healthy, False otherwise

        AI: Verifies both connection state and recent health check success.
            A stale connection (no recent successful health check) is considered disconnected.
        """
        if not self.nc or not self._running:
            return False

        # Check if we have a recent successful health check
        # If health checks are enabled and we haven't had one recently, consider disconnected
        health_check_interval = getattr(self.config, "health_check_interval", 30)
        if health_check_interval > 0:
            try:
                current_time = asyncio.get_running_loop().time()
            except RuntimeError:
                # No event loop running, can't check time - assume connected if nc and _running are True
                return True

            time_since_last_check = current_time - self._last_health_check

            # If it's been more than 2x the interval since last check, consider unhealthy
            if self._last_health_check > 0 and time_since_last_check > (health_check_interval * 2):
                logger.warning(
                    "Connection health check stale",
                    time_since_last_check=time_since_last_check,
                    health_check_interval=health_check_interval,
                )
                return False

            # If we've had too many consecutive failures, consider disconnected
            if self._consecutive_health_failures >= 3:
                logger.warning(
                    "Too many consecutive health check failures",
                    failures=self._consecutive_health_failures,
                )
                return False

        return True

    def get_subscription_count(self) -> int:
        """
        Get the number of active subscriptions.

        Returns:
            Number of active subscriptions
        """
        return len(self.subscriptions)

    def _create_tracked_task(
        self, coro, task_name: str = "nats_background", task_type: str = "background"
    ) -> asyncio.Task:
        """
        Create a tracked background task with proper lifecycle management.

        AnyIO Pattern: Track all background tasks for proper cleanup and monitoring.
        Ensures tasks are properly cancelled during shutdown.

        Args:
            coro: Coroutine to run as background task
            task_name: Human-readable name for the task
            task_type: Type of task (lifecycle, background, etc.)

        Returns:
            Created and tracked asyncio.Task
        """
        try:
            task = asyncio.create_task(coro)
            self._background_tasks.add(task)

            # Remove from tracking when complete
            def remove_task(t: asyncio.Task) -> None:
                self._background_tasks.discard(t)

            task.add_done_callback(remove_task)
            logger.debug("Created tracked background task", task_name=task_name, task_type=task_type)
            return task
        except RuntimeError as e:
            logger.error("Failed to create tracked task - no event loop", task_name=task_name, error=str(e))
            raise

    # Event handlers with state machine integration (fire-and-forget async tasks)
    def _on_error(self, error):
        """
        Handle NATS connection errors with state machine tracking.

        AI: Errors may trigger degradation or reconnection.
        AI: Runs as fire-and-forget async task to prevent blocking NATS client.
        AnyIO Pattern: Fire-and-forget tasks are tracked for proper cleanup.
        """
        # Fire-and-forget async task to prevent blocking, but track it
        try:
            self._create_tracked_task(
                self._handle_error_async(error), task_name="nats_error_handler", task_type="background"
            )
        except RuntimeError:
            # No event loop available - this should not happen in normal operation
            logger.error("NATS connection error handler called without event loop", error=str(error))

    async def _handle_error_async(self, error):
        """Async handler for NATS connection errors."""
        try:
            logger.error("NATS connection error", error=str(error), state=self.state_machine.current_state.id)

            # Degrade connection if currently connected
            if self.state_machine.current_state.id == "connected":
                self.state_machine.degrade()
        except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Error handler errors unpredictable, must log but not fail
            logger.error("Error in async error handler", error=str(e), original_error=str(error))

    def _on_disconnect(self):
        """
        Handle NATS disconnection events with state machine tracking.

        AI: Disconnection triggers reconnection attempt.
        AI: Runs as fire-and-forget async task to prevent blocking NATS client.
        AnyIO Pattern: Fire-and-forget tasks are tracked for proper cleanup.
        """
        # Fire-and-forget async task to prevent blocking, but track it
        try:
            self._create_tracked_task(
                self._handle_disconnect_async(), task_name="nats_disconnect_handler", task_type="background"
            )
        except RuntimeError:
            # No event loop available - this should not happen in normal operation
            logger.error("NATS disconnect handler called without event loop")
            self._running = False

    async def _handle_disconnect_async(self):
        """Async handler for NATS disconnection events."""
        try:
            logger.warning("NATS client disconnected", state=self.state_machine.current_state.id)
            self._running = False

            # Transition to reconnecting if we were connected
            if self.state_machine.current_state.id in ["connected", "degraded"]:
                self.state_machine.disconnect()
                self.state_machine.start_reconnect()
        except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Disconnect handler errors unpredictable, must log but not fail
            logger.error("Error in async disconnect handler", error=str(e))

    def _on_reconnect(self):
        """
        Handle NATS reconnection events with state machine tracking.

        AI: Successful reconnection transitions to connected state.
        AI: Runs as fire-and-forget async task to prevent blocking NATS client.
        AnyIO Pattern: Fire-and-forget tasks are tracked for proper cleanup.
        """
        # Fire-and-forget async task to prevent blocking, but track it
        try:
            self._create_tracked_task(
                self._handle_reconnect_async(), task_name="nats_reconnect_handler", task_type="background"
            )
        except RuntimeError:
            # No event loop available - this should not happen in normal operation
            logger.error("NATS reconnect handler called without event loop")
            self._running = True
            self._connection_retries = 0

    async def _handle_reconnect_async(self):
        """Async handler for NATS reconnection events."""
        try:
            logger.info("NATS client reconnected", state=self.state_machine.current_state.id)
            self._running = True
            self._connection_retries = 0

            # Transition to connected if we were reconnecting
            if self.state_machine.current_state.id == "reconnecting":
                self.state_machine.connected_successfully()
            elif self.state_machine.current_state.id == "degraded":
                self.state_machine.recover()
        except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Reconnect handler errors unpredictable, must log but not fail
            logger.error("Error in async reconnect handler", error=str(e))

    def get_connection_stats(self) -> dict[str, Any]:
        """
        Get connection statistics from state machine.

        Returns:
            Dictionary with connection state and metrics

        AI: For monitoring dashboards and health checks.
        """
        try:
            current_time = asyncio.get_running_loop().time()
            time_since_last_check = current_time - self._last_health_check if self._last_health_check > 0 else None
        except RuntimeError:
            time_since_last_check = None

        return {
            "nats_connected": self._running,
            "pool_initialized": self._pool_initialized,
            "pool_size": self.pool_size,
            "available_connections": self.available_connections.qsize(),
            "health_check_enabled": getattr(self.config, "health_check_interval", 30) > 0,
            "last_health_check": self._last_health_check if self._last_health_check > 0 else None,
            "time_since_last_check": time_since_last_check,
            "consecutive_health_failures": self._consecutive_health_failures,
            **self.state_machine.get_stats(),
            **self.metrics.get_metrics(),
        }

    async def _initialize_connection_pool(self) -> None:
        """Initialize connection pool for high-throughput scenarios."""
        if self._pool_initialized:
            return

        try:
            nats_url = self.config.url
            # Type annotation allows TLS context to be added
            connect_options: dict[str, Any] = {
                "reconnect_time_wait": self.config.reconnect_time_wait,
                "max_reconnect_attempts": self._max_retries,
                "connect_timeout": self.config.connect_timeout,
                "ping_interval": self.config.ping_interval,
                "max_outstanding_pings": self.config.max_outstanding_pings,
            }

            # Configure TLS for pool connections if enabled
            if self.config.tls_enabled:
                ssl_context = ssl.create_default_context()

                if self.config.tls_cert_file and self.config.tls_key_file:
                    cert_path = Path(self.config.tls_cert_file)
                    key_path = Path(self.config.tls_key_file)
                    ssl_context.load_cert_chain(cert_path, key_path)

                if self.config.tls_ca_file:
                    ca_path = Path(self.config.tls_ca_file)
                    ssl_context.load_verify_locations(ca_path)

                if self.config.tls_verify:
                    ssl_context.check_hostname = True
                    ssl_context.verify_mode = ssl.CERT_REQUIRED
                else:
                    ssl_context.check_hostname = False
                    ssl_context.verify_mode = ssl.CERT_NONE

                connect_options["tls"] = ssl_context

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

        except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Pool initialization errors unpredictable, must handle gracefully
            logger.error(
                "Failed to initialize NATS connection pool",
                error=str(e),
                pool_size=self.pool_size,
            )
            # Continue with single connection if pool fails
            self._pool_initialized = False

    async def _get_connection(self) -> nats.NATS:
        """
        Get connection from pool.

        Raises:
            NATSPublishError: If no connection is available
        """
        if not self._pool_initialized:
            raise NATSPublishError("Connection pool not initialized", subject="")
        if self.available_connections.empty():
            raise NATSPublishError("No available connections in pool", subject="")
        return await self.available_connections.get()

    async def _return_connection(self, connection: nats.NATS):
        """Return connection to pool."""
        if self._pool_initialized and connection in self.connection_pool:
            await self.available_connections.put(connection)

    async def publish_with_pool(self, subject: str, data: dict[str, Any]) -> None:
        """
        Publish message using connection pool for high-throughput scenarios.

        Args:
            subject: NATS subject name
            data: Message data to publish

        Raises:
            NATSPublishError: If publishing fails

        AI: Raises exceptions instead of returning False for better error handling.
        """
        # AI Agent: Use asyncio.get_running_loop() instead of deprecated get_event_loop()
        #           Python 3.10+ deprecates get_event_loop() in async contexts
        start_time = asyncio.get_running_loop().time()
        success = False
        connection = None

        try:
            # Validate subject if subject manager is available and validation is enabled
            if self.subject_manager and self.config.enable_subject_validation:
                try:
                    if not self.subject_manager.validate_subject(subject):
                        error_msg = f"Subject validation failed: {subject}"
                        logger.error(
                            "Subject validation failed",
                            subject=subject,
                            message_id=data.get("message_id"),
                            correlation_id=data.get("correlation_id"),
                        )
                        raise NATSPublishError(error_msg, subject=subject)
                except SubjectValidationError as e:
                    error_msg = f"Subject validation error: {str(e)}"
                    logger.error(
                        "Subject validation error",
                        error=str(e),
                        subject=subject,
                        message_id=data.get("message_id"),
                        correlation_id=data.get("correlation_id"),
                    )
                    raise NATSPublishError(error_msg, subject=subject, error=e) from e

            connection = await self._get_connection()

            # Serialize message data using thread pool for CPU-bound operation
            loop = asyncio.get_running_loop()
            message_bytes = await loop.run_in_executor(None, lambda: json.dumps(data).encode("utf-8"))

            # Publish to NATS subject
            await connection.publish(subject, message_bytes)
            success = True

            logger.debug(
                "Message published via connection pool",
                subject=subject,
                message_id=data.get("message_id"),
                sender_id=data.get("sender_id"),
                data_size=len(message_bytes),
            )

        except NATSPublishError:
            # Re-raise NATS publish errors
            raise
        except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Publish errors unpredictable, must handle and log
            error_msg = f"Failed to publish message via connection pool: {str(e)}"
            logger.error(
                "Failed to publish message via connection pool",
                error=str(e),
                subject=subject,
                message_id=data.get("message_id"),
            )
            raise NATSPublishError(error_msg, subject=subject, error=e) from e
        finally:
            if connection:
                await self._return_connection(connection)
            # Record metrics
            processing_time = asyncio.get_running_loop().time() - start_time
            self.metrics.record_publish(success, processing_time)

    async def _cleanup_connection_pool(self):
        """Clean up connection pool during shutdown."""
        try:
            # Close all connections in pool
            for connection in self.connection_pool:
                try:
                    await connection.close()
                except asyncio.CancelledError:
                    logger.warning("NATS connection close cancelled during shutdown", connection=str(connection))
                    continue
                except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Connection close errors unpredictable, must continue cleanup
                    logger.warning("Error closing pool connection", error=str(e))

            # Clear pool
            self.connection_pool.clear()
            self._pool_initialized = False

            logger.info("Connection pool cleaned up", pool_size=len(self.connection_pool))

        except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Pool cleanup errors unpredictable, must handle gracefully
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
            # Validate subject if subject manager is available and validation is enabled
            if self.subject_manager and self.config.enable_subject_validation:
                try:
                    if not self.subject_manager.validate_subject(subject):
                        logger.error(
                            "Subject validation failed",
                            subject=subject,
                            message_id=data.get("message_id"),
                            correlation_id=data.get("correlation_id"),
                        )
                        return False
                except SubjectValidationError as e:
                    logger.error(
                        "Subject validation error",
                        error=str(e),
                        subject=subject,
                        message_id=data.get("message_id"),
                        correlation_id=data.get("correlation_id"),
                    )
                    return False

            # Add message to batch
            self.message_batch.append((subject, data))

            # Flush batch if size threshold reached
            if len(self.message_batch) >= self.batch_size:
                await self._flush_batch()
            elif not self._batch_task:
                # Start timeout task for batch with proper tracking
                # AnyIO Pattern: Track short-lived tasks for proper cancellation
                self._batch_task = self._create_tracked_task(
                    self._batch_timeout(), task_name="nats_batch_timeout", task_type="background"
                )

            logger.debug(
                "Message added to batch",
                subject=subject,
                batch_size=len(self.message_batch),
                message_id=data.get("message_id"),
            )

            return True

        except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Batch add errors unpredictable, must handle gracefully
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
            await sleep(self.batch_timeout)
            await self._flush_batch()
        except asyncio.CancelledError:
            # Task was cancelled, which is expected
            pass
        finally:
            self._batch_task = None

    async def _flush_batch(self) -> None:
        """Flush all batched messages efficiently."""
        if not self.message_batch:
            return

        try:
            # Group messages by subject for efficient publishing
            grouped_messages: dict[str, list[Any]] = {}
            for subject, data in self.message_batch:
                if subject not in grouped_messages:
                    grouped_messages[subject] = []
                grouped_messages[subject].append(data)

            # Publish each group using connection pool
            for subject, messages in grouped_messages.items():
                batch_data = {
                    "messages": messages,
                    "count": len(messages),
                    "batch_timestamp": asyncio.get_running_loop().time(),
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

        except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Batch flush errors unpredictable, must handle gracefully
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
