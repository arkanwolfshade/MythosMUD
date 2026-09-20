"""
NATS service for MythosMUD chat system.

This module provides NATS pub/sub functionality for real-time chat messaging,
replacing the previous Redis-based implementation with a more lightweight
and Windows-native solution.
"""

# pylint: disable=too-many-instance-attributes,too-many-lines,missing-class-docstring,missing-function-docstring,too-few-public-methods  # Reason: NATS service is large; Protocol stubs (PEP 544)

import asyncio
import json
import time
from collections.abc import Coroutine, Mapping
from typing import Protocol, cast, override

from anyio import sleep
from nats.aio.client import Client

from ..config.models import NATSConfig
from ..realtime.connection_state_machine import NATSConnectionStateMachine
from ..structured_logging.enhanced_logging_config import get_logger
from .nats_exceptions import NATSPublishError, NATSRequestError
from .nats_metrics import NATSMetrics
from .nats_service_pool import NATSServicePoolMixin, nats_connect
from .nats_service_subscriptions import JsonMap, NATSServiceSubscriptionMixin, NatsSubscription, as_json_map
from .nats_subject_manager import NATSSubjectManager

logger = get_logger("nats")


class _NatsListenerClient(Protocol):
    def add_error_listener(self, cb: object) -> object:
        return cb

    def add_disconnect_listener(self, cb: object) -> object:
        return cb

    def add_reconnect_listener(self, cb: object) -> object:
        return cb


class NATSService(NATSServicePoolMixin, NATSServiceSubscriptionMixin):  # pylint: disable=too-many-instance-attributes  # Reason: NATS service requires many state tracking and configuration attributes
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

    config: NATSConfig
    connection_pool: list[Client]
    pool_size: int
    available_connections: asyncio.Queue[Client]
    _pool_initialized: bool
    message_batch: list[tuple[str, JsonMap]]
    batch_size: int
    batch_timeout: float
    _batch_task: asyncio.Task[None] | None
    _failed_batch_queue: list[tuple[str, JsonMap]]
    _max_batch_retries: int
    metrics: NATSMetrics
    nc: Client | None
    subscriptions: dict[str, NatsSubscription]
    _running: bool
    _connection_retries: int
    _max_retries: int
    _health_check_task: asyncio.Task[None] | None
    _last_health_check: float
    _consecutive_health_failures: int
    _health_check_timeout: float
    _background_tasks: set[asyncio.Task[None]]
    state_machine: NATSConnectionStateMachine
    subject_manager: NATSSubjectManager | None
    _subscription_timestamps: list[tuple[str, float]]
    _unsubscription_timestamps: list[tuple[str, float]]
    _subscription_count: int
    _unsubscription_count: int
    _last_cleanup_time: float | None
    _max_timestamp_history: int

    def __init__(
        self,
        config: NATSConfig | Mapping[str, object] | None = None,
        subject_manager: NATSSubjectManager | None = None,
    ) -> None:
        """
        Initialize NATS service with state machine and connection pooling.

        Args:
            config: NATS configuration (NATSConfig model, dict, or None for defaults)
            subject_manager: NATSSubjectManager instance (optional, for subject validation)

        AI: State machine tracks connection lifecycle and prevents invalid state transitions.
        AI: Accepts dict and converts to Pydantic model for type safety.
        """
        if config is None:
            self.config = NATSConfig()
        elif isinstance(config, NATSConfig):
            self.config = config
        else:
            self.config = NATSConfig.model_validate(config)

        self.connection_pool = []
        self.pool_size = self.config.connection_pool_size
        self.available_connections = asyncio.Queue()
        self._pool_initialized = False

        self.message_batch = []
        self.batch_size = self.config.batch_size
        self.batch_timeout = self.config.batch_timeout
        self._batch_task = None
        self._failed_batch_queue = []
        self._max_batch_retries = self.config.max_batch_retries

        self.metrics = NATSMetrics()

        self.nc = None
        self.subscriptions = {}
        self._running = False
        self._connection_retries = 0
        self._max_retries = self.config.max_reconnect_attempts

        self._health_check_task = None
        self._last_health_check = 0.0
        self._consecutive_health_failures = 0
        self._health_check_timeout = 5.0

        self._background_tasks = set()

        self.state_machine = NATSConnectionStateMachine(
            connection_id="nats-primary", max_reconnect_attempts=self._max_retries
        )

        if subject_manager is None and self.config.enable_subject_validation:
            subject_manager = NATSSubjectManager(strict_validation=self.config.strict_subject_validation)
        self.subject_manager = subject_manager

        self._subscription_timestamps = []
        self._unsubscription_timestamps = []
        self._subscription_count = 0
        self._unsubscription_count = 0
        self._last_cleanup_time = None
        self._max_timestamp_history = 1000

    def _check_connection_allowed(self) -> bool:
        """Check if connection attempt is allowed by state machine."""
        if not self.state_machine.can_attempt_connection():
            logger.warning(
                "Connection attempt blocked by state machine",
                current_state=self.state_machine.state.id,
                reconnect_attempts=self.state_machine.reconnect_attempts,
            )
            return False

        if self.state_machine.state.id == "disconnected":
            self.state_machine.connect()
        elif self.state_machine.state.id == "reconnecting":
            pass

        return True

    def _setup_connection_handlers(self) -> None:
        """Set up connection event handlers."""
        if self.nc is None:
            return
        listeners = cast(_NatsListenerClient, cast(object, self.nc))
        try:
            _ = listeners.add_error_listener(self._on_error)
            _ = listeners.add_disconnect_listener(self._on_disconnect)
            _ = listeners.add_reconnect_listener(self._on_reconnect)
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
                state=self.state_machine.state.id,
            )

            self.nc = await nats_connect(nats_url, connect_options)
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
                state=self.state_machine.state.id,
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
                state=self.state_machine.state.id,
            )

            # Check if circuit breaker should be triggered
            if self.state_machine.should_open_circuit():
                if self.state_machine.state.id == "disconnected":
                    # Need to be in reconnecting to open circuit
                    self.state_machine.start_reconnect()
                self.state_machine.open_circuit()
                logger.critical(
                    "NATS connection circuit breaker opened",
                    state=self.state_machine.state.id,
                )

            return False

    async def _close_nats_connection(self) -> None:
        """Close NATS connection and transition to disconnected state."""
        if self.nc is None:
            return

        await self.nc.close()
        self.nc = None
        self.subscriptions.clear()
        self._running = False

        # Transition to disconnected state
        if self.state_machine.state.id in ["connected", "degraded"]:
            self.state_machine.disconnect()

        logger.info("Disconnected from NATS server", state=self.state_machine.state.id)

    async def disconnect(self) -> None:
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
                # Track subscriptions before cleanup for verification (Task 4: NATS Subscription Cleanup)
                subscriptions_before_cleanup = list(self.subscriptions.keys())
                logger.info(
                    "Starting NATS subscription cleanup",
                    active_subscriptions=len(subscriptions_before_cleanup),
                    subscription_subjects=subscriptions_before_cleanup,
                )

                # Drain in-flight messages before closing subscriptions
                await self._drain_subscriptions()

                # Close all subscriptions
                await self._close_all_subscriptions()

                # Verify all subscriptions were cleaned up
                self._verify_subscription_cleanup(subscriptions_before_cleanup)

                # Close NATS connection
                await self._close_nats_connection()

            # Clean up connection pool
            if self._pool_initialized:
                await self._cleanup_connection_pool()

            # Stop health check monitoring
            await self._stop_health_monitoring()

        except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Disconnect errors unpredictable, must handle gracefully
            logger.error("Error disconnecting from NATS server", error=str(e))

    async def _start_health_monitoring(self) -> None:
        """Start periodic health check monitoring task."""
        health_check_interval = self.config.health_check_interval
        if health_check_interval <= 0:
            logger.debug("Health monitoring disabled (interval <= 0)")
            return

        # Cancel existing task if any
        if self._health_check_task and not self._health_check_task.done():
            _ = self._health_check_task.cancel()
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

    async def _force_cancel_pending_tasks(self, pending: set[asyncio.Task[None]]) -> None:
        """Force-cancel stragglers left after the initial cancellation wait, best-effort."""
        for task in pending:
            if not task.done():
                _ = task.cancel()
        # Give them a brief moment to cancel
        try:
            _ = await asyncio.wait_for(asyncio.gather(*pending, return_exceptions=True), timeout=0.5)
        except (TimeoutError, Exception):  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Task cancellation errors unpredictable, must abandon remaining tasks on any error during shutdown
            pass  # Abandon remaining tasks

    async def _cancel_background_tasks(self) -> None:
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
                _ = task.cancel()

        # Wait for tasks to complete with timeout
        if self._background_tasks:
            try:
                _done, pending = await asyncio.wait(
                    self._background_tasks, timeout=2.0, return_when=asyncio.ALL_COMPLETED
                )
                if pending:
                    await self._force_cancel_pending_tasks(pending)

            except (RuntimeError, asyncio.CancelledError) as e:
                logger.debug("Error during background task cancellation", error=str(e))
            finally:
                self._background_tasks.clear()

        logger.debug("Background tasks cancelled")

    async def _stop_health_monitoring(self) -> None:
        """Stop health check monitoring task."""
        if self._health_check_task and not self._health_check_task.done():
            _ = self._health_check_task.cancel()
            try:
                await self._health_check_task
            except asyncio.CancelledError:
                pass
            self._health_check_task = None
        logger.debug("Health monitoring stopped")

    async def _health_check_loop(self) -> None:
        """Periodic health check loop using ping/pong."""
        health_check_interval = self.config.health_check_interval

        while self._running:
            try:
                await sleep(health_check_interval)

                if not self.nc or not self._running:
                    break

                # Perform health check via ping/pong
                health_ok = await self._perform_health_check()

                if health_ok:
                    self._consecutive_health_failures = 0
                    self._last_health_check = time.monotonic()
                    # Update health score in metrics
                    self.metrics.update_connection_health(100.0)
                else:
                    self._consecutive_health_failures += 1
                    # Degrade health score based on failures
                    health_score = max(0.0, 100.0 - (self._consecutive_health_failures * 20))
                    self.metrics.update_connection_health(health_score)

                    # Transition to degraded state if too many failures
                    if self._consecutive_health_failures >= 3:
                        if self.state_machine.state.id == "connected":
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

    async def publish(self, subject: str, data: JsonMap) -> None:
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

        # When pool is exhausted, wait for a connection to become available instead of failing immediately
        pool_wait_timeout = self.config.pool_wait_timeout
        if self.available_connections.empty():
            try:
                conn = await asyncio.wait_for(self.available_connections.get(), timeout=pool_wait_timeout)
                await self.available_connections.put(conn)
            except TimeoutError as err:
                error_msg = "No available connections in pool"
                logger.error("No available connections in pool", subject=subject, pool_size=self.pool_size)
                raise NATSPublishError(error_msg, subject=subject) from err

        # Use connection pool
        await self.publish_with_pool(subject, data)

    async def request(self, subject: str, data: JsonMap, timeout: float = 5.0) -> JsonMap:
        """
        Send a request to a NATS subject and wait for a response.

        Args:
            subject: NATS subject name to send request to
            data: Request data to send
            timeout: Timeout in seconds for the response

        Returns:
            Response data if successful

        Raises:
            NATSRequestError: If request fails, times out, or client is not connected

        AI: Raises exceptions instead of returning None for better error handling.
        """
        try:
            if not self.nc or not self._running:
                error_msg = "NATS client not connected"
                logger.error("NATS client not connected")
                raise NATSRequestError(error_msg, subject=subject)

            loop = asyncio.get_running_loop()
            payload = data
            response_bytes_holder: list[bytes] = []

            def _encode() -> bytes:
                return json.dumps(payload).encode("utf-8")

            request_bytes = await loop.run_in_executor(None, _encode)
            response = await self.nc.request(subject, request_bytes, timeout=timeout)
            response_bytes_holder.append(response.data)

            def _decode() -> JsonMap:
                return as_json_map(cast(object, json.loads(response_bytes_holder[0].decode("utf-8"))))

            result = await loop.run_in_executor(None, _decode)
            logger.debug(
                "Request/response completed",
                subject=subject,
                request_id=data.get("request_id"),
                response_size=len(response.data),
            )
            return result

        except TimeoutError as e:
            error_msg = f"Request timeout after {timeout}s"
            logger.warning("Request timeout", subject=subject, timeout=timeout)
            raise NATSRequestError(error_msg, subject=subject, timeout=timeout, error=e) from e
        except NATSRequestError:
            raise
        except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Request errors unpredictable, must handle and raise
            error_msg = f"Failed to send request: {str(e)}"
            logger.error("Failed to send request", error=str(e), subject=subject)
            raise NATSRequestError(error_msg, subject=subject, timeout=timeout, error=e) from e

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
        health_check_interval = self.config.health_check_interval
        if health_check_interval > 0:
            current_time = time.monotonic()
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

    @override
    def _create_tracked_task(
        self,
        coro: Coroutine[None, None, None],
        task_name: str = "nats_background",
        task_type: str = "background",
    ) -> asyncio.Task[None]:
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
            def remove_task(t: asyncio.Task[None]) -> None:
                self._background_tasks.discard(t)

            task.add_done_callback(remove_task)
            logger.debug("Created tracked background task", task_name=task_name, task_type=task_type)
            return task
        except RuntimeError as e:
            # Close unscheduled coro so GC does not warn "coroutine was never awaited"
            # (common when NATS callbacks fire during test teardown with no running loop).
            coro.close()
            logger.error("Failed to create tracked task - no event loop", task_name=task_name, error=str(e))
            raise

    # Event handlers with state machine integration (fire-and-forget async tasks)
    def _on_error(self, error: BaseException) -> None:
        """
        Handle NATS connection errors with state machine tracking.

        AI: Errors may trigger degradation or reconnection.
        AI: Runs as fire-and-forget async task to prevent blocking NATS client.
        AnyIO Pattern: Fire-and-forget tasks are tracked for proper cleanup.
        """
        # Fire-and-forget async task to prevent blocking, but track it
        coro = self._handle_error_async(error)
        try:
            _ = self._create_tracked_task(coro, task_name="nats_error_handler", task_type="background")
        except RuntimeError:
            coro.close()
            # No event loop available - this should not happen in normal operation
            logger.error("NATS connection error handler called without event loop", error=str(error))

    async def _handle_error_async(self, error: BaseException) -> None:
        """Async handler for NATS connection errors."""
        try:
            logger.error("NATS connection error", error=str(error), state=self.state_machine.state.id)

            # Degrade connection if currently connected
            if self.state_machine.state.id == "connected":
                self.state_machine.degrade()
        except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Error handler errors unpredictable, must log but not fail
            logger.error("Error in async error handler", error=str(e), original_error=str(error))

    def _on_disconnect(self) -> None:
        """
        Handle NATS disconnection events with state machine tracking.

        AI: Disconnection triggers reconnection attempt.
        AI: Runs as fire-and-forget async task to prevent blocking NATS client.
        AnyIO Pattern: Fire-and-forget tasks are tracked for proper cleanup.
        """
        # Fire-and-forget async task to prevent blocking, but track it
        coro = self._handle_disconnect_async()
        try:
            _ = self._create_tracked_task(coro, task_name="nats_disconnect_handler", task_type="background")
        except RuntimeError:
            coro.close()
            # No event loop available - this should not happen in normal operation
            logger.error("NATS disconnect handler called without event loop")
            self._running = False

    async def _handle_disconnect_async(self) -> None:
        """Async handler for NATS disconnection events."""
        try:
            logger.warning("NATS client disconnected", state=self.state_machine.state.id)
            self._running = False

            # Transition to reconnecting if we were connected
            if self.state_machine.state.id in ["connected", "degraded"]:
                self.state_machine.disconnect()
                self.state_machine.start_reconnect()
        except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Disconnect handler errors unpredictable, must log but not fail
            logger.error("Error in async disconnect handler", error=str(e))

    def _on_reconnect(self) -> None:
        """
        Handle NATS reconnection events with state machine tracking.

        AI: Successful reconnection transitions to connected state.
        AI: Runs as fire-and-forget async task to prevent blocking NATS client.
        AnyIO Pattern: Fire-and-forget tasks are tracked for proper cleanup.
        """
        # Fire-and-forget async task to prevent blocking, but track it
        coro = self._handle_reconnect_async()
        try:
            _ = self._create_tracked_task(coro, task_name="nats_reconnect_handler", task_type="background")
        except RuntimeError:
            coro.close()
            # No event loop available - this should not happen in normal operation
            logger.error("NATS reconnect handler called without event loop")
            self._running = True
            self._connection_retries = 0

    async def _handle_reconnect_async(self) -> None:
        """Async handler for NATS reconnection events."""
        try:
            logger.info("NATS client reconnected", state=self.state_machine.state.id)
            self._running = True
            self._connection_retries = 0

            # Transition to connected if we were reconnecting
            if self.state_machine.state.id == "reconnecting":
                self.state_machine.connected_successfully()
            elif self.state_machine.state.id == "degraded":
                self.state_machine.recover()
        except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Reconnect handler errors unpredictable, must log but not fail
            logger.error("Error in async reconnect handler", error=str(e))

    def get_connection_stats(self) -> JsonMap:
        """
        Get connection statistics from state machine.

        Returns:
            Dictionary with connection state and metrics

        AI: For monitoring dashboards and health checks.
        """
        current_time = time.monotonic()
        time_since_last_check = current_time - self._last_health_check if self._last_health_check > 0 else None

        stats: JsonMap = {
            "nats_connected": self._running,
            "pool_initialized": self._pool_initialized,
            "pool_size": self.pool_size,
            "available_connections": self.available_connections.qsize(),
            "health_check_enabled": self.config.health_check_interval > 0,
            "last_health_check": self._last_health_check if self._last_health_check > 0 else None,
            "time_since_last_check": time_since_last_check,
            "consecutive_health_failures": self._consecutive_health_failures,
            "failed_batch_queue_size": len(self._failed_batch_queue),
            "current_batch_size": len(self.message_batch),
        }
        stats.update(as_json_map(cast(object, self.state_machine.get_stats())))
        stats.update(as_json_map(cast(object, self.metrics.get_metrics())))
        return stats


# Global NATS service instance
nats_service = NATSService()
