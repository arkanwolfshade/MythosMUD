"""NATS connection pool and batch publishing (extracted from nats_service)."""

# pylint: disable=too-many-lines,missing-class-docstring,missing-function-docstring,too-few-public-methods  # Reason: Pool mixin stays one module; Protocol/TypedDict stubs (PEP 544)

from __future__ import annotations

import asyncio
import json
import ssl
import time
from collections.abc import Coroutine, Mapping
from pathlib import Path
from typing import NotRequired, Protocol, TypedDict, cast

import nats
from anyio import sleep
from nats.aio.client import Client

from ..config.models import NATSConfig
from ..structured_logging.enhanced_logging_config import get_logger
from .nats_exceptions import NATSPublishError
from .nats_metrics import NATSMetrics
from .nats_subject_manager import NATSSubjectManager, SubjectValidationError

logger = get_logger("nats")


class NatsConnectOptions(TypedDict):
    reconnect_time_wait: int
    max_reconnect_attempts: int
    connect_timeout: int
    ping_interval: int
    max_outstanding_pings: int
    token: NotRequired[str]
    user: NotRequired[str]
    password: NotRequired[str]
    tls: NotRequired[ssl.SSLContext]


class _NatsConnectFn(Protocol):
    async def __call__(
        self,
        servers: str,
        *,
        reconnect_time_wait: int = 2,
        max_reconnect_attempts: int = 60,
        connect_timeout: int = 2,
        ping_interval: int = 120,
        max_outstanding_pings: int = 2,
        token: str | None = None,
        user: str | None = None,
        password: str | None = None,
        tls: ssl.SSLContext | None = None,
    ) -> Client:
        _ = (servers, tls)
        raise NotImplementedError


async def nats_connect(url: str, options: NatsConnectOptions) -> Client:
    connect = cast(_NatsConnectFn, nats.connect)
    if "tls" in options:
        return await connect(
            url,
            reconnect_time_wait=options["reconnect_time_wait"],
            max_reconnect_attempts=options["max_reconnect_attempts"],
            connect_timeout=options["connect_timeout"],
            ping_interval=options["ping_interval"],
            max_outstanding_pings=options["max_outstanding_pings"],
            token=options.get("token"),
            user=options.get("user"),
            password=options.get("password"),
            tls=options["tls"],
        )
    return await connect(
        url,
        reconnect_time_wait=options["reconnect_time_wait"],
        max_reconnect_attempts=options["max_reconnect_attempts"],
        connect_timeout=options["connect_timeout"],
        ping_interval=options["ping_interval"],
        max_outstanding_pings=options["max_outstanding_pings"],
        token=options.get("token"),
        user=options.get("user"),
        password=options.get("password"),
    )


class NATSServicePoolMixin:
    """Pool/batch helpers mixed into NATSService. Attributes set in NATSService.__init__."""

    config: NATSConfig  # pyright: ignore[reportUninitializedInstanceVariable]
    connection_pool: list[Client]  # pyright: ignore[reportUninitializedInstanceVariable]
    pool_size: int  # pyright: ignore[reportUninitializedInstanceVariable]
    available_connections: asyncio.Queue[Client]  # pyright: ignore[reportUninitializedInstanceVariable]
    _pool_initialized: bool  # pyright: ignore[reportUninitializedInstanceVariable]
    _max_retries: int  # pyright: ignore[reportUninitializedInstanceVariable]
    subject_manager: NATSSubjectManager | None  # pyright: ignore[reportUninitializedInstanceVariable]
    metrics: NATSMetrics  # pyright: ignore[reportUninitializedInstanceVariable]
    message_batch: list[tuple[str, dict[str, object]]]  # pyright: ignore[reportUninitializedInstanceVariable]
    batch_size: int  # pyright: ignore[reportUninitializedInstanceVariable]
    batch_timeout: float  # pyright: ignore[reportUninitializedInstanceVariable]
    _batch_task: asyncio.Task[None] | None  # pyright: ignore[reportUninitializedInstanceVariable]
    _failed_batch_queue: list[tuple[str, dict[str, object]]]  # pyright: ignore[reportUninitializedInstanceVariable]
    _max_batch_retries: int  # pyright: ignore[reportUninitializedInstanceVariable]

    def _create_tracked_task(
        self,
        coro: Coroutine[None, None, None],
        task_name: str = "nats_background",
        task_type: str = "background",
    ) -> asyncio.Task[None]:
        """Implemented on NATSService."""
        raise NotImplementedError(task_name, task_type, coro)

    def _build_connect_options(self) -> NatsConnectOptions:
        """Build connection options for NATS (primary client and pool)."""
        connect_options: NatsConnectOptions = {
            "reconnect_time_wait": self.config.reconnect_time_wait,
            "max_reconnect_attempts": self._max_retries,
            "connect_timeout": self.config.connect_timeout,
            "ping_interval": self.config.ping_interval,
            "max_outstanding_pings": self.config.max_outstanding_pings,
        }
        if self.config.token:
            connect_options["token"] = self.config.token
        elif self.config.user and self.config.password:
            connect_options["user"] = self.config.user
            connect_options["password"] = self.config.password
        return connect_options

    def _configure_tls(self, connect_options: NatsConnectOptions) -> None:
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

    async def _initialize_connection_pool(self) -> None:
        """
        Initialize connection pool for high-throughput scenarios.

        AI: Tracks successful vs failed connections and reports partial failures.
            Continues with partial pool if some connections succeed.
        """
        if self._pool_initialized:
            return

        try:
            nats_url = self.config.url
            connect_options = self._build_connect_options()
            self._configure_tls(connect_options)

            # Create pool connections with error tracking
            successful_connections = 0
            failed_connections = 0
            connection_errors: list[str] = []

            for i in range(self.pool_size):
                try:
                    connection = await nats_connect(nats_url, connect_options)
                    self.connection_pool.append(connection)
                    await self.available_connections.put(connection)
                    successful_connections += 1
                    logger.debug("Connection pool connection created", connection_index=i + 1, pool_size=self.pool_size)
                except Exception as conn_error:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Individual connection failures must not stop pool initialization
                    failed_connections += 1
                    error_msg = f"Connection {i + 1}: {str(conn_error)}"
                    connection_errors.append(error_msg)
                    logger.warning(
                        "Failed to create connection pool connection",
                        connection_index=i + 1,
                        pool_size=self.pool_size,
                        error=str(conn_error),
                    )

            # Determine pool initialization status
            if not successful_connections:
                # No connections succeeded, disable pool
                self._pool_initialized = False
                logger.error(
                    "Failed to initialize NATS connection pool - no connections succeeded",
                    pool_size=self.pool_size,
                    failed_connections=failed_connections,
                    errors=connection_errors,
                )
            elif successful_connections < self.pool_size:
                # Partial success - pool initialized but smaller than configured
                self._pool_initialized = True
                logger.warning(
                    "NATS connection pool initialized with partial success",
                    pool_size=self.pool_size,
                    successful_connections=successful_connections,
                    failed_connections=failed_connections,
                    actual_pool_size=len(self.connection_pool),
                    errors=connection_errors,
                )
            else:
                # Full success
                self._pool_initialized = True
                logger.info(
                    "NATS connection pool initialized successfully",
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

    async def _get_connection(self) -> Client:
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

    async def _return_connection(self, connection: Client) -> None:
        """Return connection to pool."""
        if self._pool_initialized and connection in self.connection_pool:
            await self.available_connections.put(connection)

    async def publish_with_pool(self, subject: str, data: Mapping[str, object]) -> None:
        """
        Publish message using connection pool for high-throughput scenarios.

        Args:
            subject: NATS subject name
            data: Message data to publish

        Raises:
            NATSPublishError: If publishing fails

        AI: Raises exceptions instead of returning False for better error handling.
        """
        start_time = time.monotonic()
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
            processing_time = time.monotonic() - start_time
            self.metrics.record_publish(success, processing_time)

    async def _cleanup_connection_pool(self) -> None:
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

    async def publish_batch(self, subject: str, data: Mapping[str, object]) -> bool:
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
            self.message_batch.append((subject, dict(data)))

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

    async def _batch_timeout(self) -> None:
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
        """
        Flush all batched messages efficiently with retry and partial flush support.

        AI: Implements partial flush - successful groups are published, failed groups are retried.
            After max retries, failed messages are added to failed batch queue for manual recovery.
        """
        if not self.message_batch:
            return

        # Group messages by subject for efficient publishing
        grouped_messages: dict[str, list[Mapping[str, object]]] = {}
        for subject, data in self.message_batch:
            if subject not in grouped_messages:
                grouped_messages[subject] = []
            grouped_messages[subject].append(data)

        # Track successful and failed groups for partial flush
        successful_groups: list[str] = []
        failed_groups: dict[str, list[Mapping[str, object]]] = {}

        # Try to publish each group
        for subject, messages in grouped_messages.items():
            batch_data: dict[str, object] = {
                "messages": messages,
                "count": len(messages),
                "batch_timestamp": time.monotonic(),
            }

            try:
                # Use connection pool for batch publishing
                await self.publish_with_pool(subject, batch_data)
                successful_groups.append(subject)
                logger.debug("Batch group published successfully", subject=subject, message_count=len(messages))
            except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Individual group failures must not stop other groups
                failed_groups[subject] = messages
                logger.warning(
                    "Failed to publish batch group",
                    subject=subject,
                    message_count=len(messages),
                    error=str(e),
                )

        # Retry failed groups
        if failed_groups:
            await self._retry_failed_batch_groups(failed_groups)

        # Record batch flush metrics
        total_messages = len(self.message_batch)
        successful_messages = sum(len(grouped_messages[subject]) for subject in successful_groups)
        failed_messages = total_messages - successful_messages

        if not failed_messages:
            self.metrics.record_batch_flush(True, total_messages)
            logger.info(
                "Message batch flushed successfully",
                total_messages=total_messages,
                unique_subjects=len(grouped_messages),
            )
        else:
            # Partial success
            self.metrics.record_batch_flush(False, total_messages)
            logger.warning(
                "Message batch flushed with partial success",
                total_messages=total_messages,
                successful_messages=successful_messages,
                failed_messages=failed_messages,
                unique_subjects=len(grouped_messages),
            )

        # Clear batch and cancel timeout task
        self.message_batch.clear()
        if self._batch_task and not self._batch_task.done():
            _ = self._batch_task.cancel()
            self._batch_task = None

    async def _retry_failed_batch_groups(
        self, failed_groups: dict[str, list[Mapping[str, object]]], retry_count: int = 0
    ) -> None:
        """
        Retry failed batch groups with exponential backoff.

        Args:
            failed_groups: Dictionary of subject -> messages that failed to publish
            retry_count: Current retry attempt number

        AI: Retries failed groups up to max_batch_retries times with exponential backoff.
            After max retries, messages are added to failed batch queue.
        """
        if not failed_groups or retry_count >= self._max_batch_retries:
            # Max retries reached, add to failed batch queue
            for subject, messages in failed_groups.items():
                for message in messages:
                    self._failed_batch_queue.append((subject, dict(message)))
            logger.error(
                "Batch groups failed after max retries, added to failed queue",
                failed_groups=len(failed_groups),
                total_failed_messages=sum(len(msgs) for msgs in failed_groups.values()),
                retry_count=retry_count,
            )
            return

        # Exponential backoff: 100ms, 200ms, 400ms
        backoff_delay = 0.1 * float(1 << retry_count)
        await sleep(backoff_delay)

        # Retry failed groups
        still_failed: dict[str, list[Mapping[str, object]]] = {}
        for subject, messages in failed_groups.items():
            batch_data: dict[str, object] = {
                "messages": messages,
                "count": len(messages),
                "batch_timestamp": time.monotonic(),
            }

            try:
                await self.publish_with_pool(subject, batch_data)
                logger.info(
                    "Batch group published successfully on retry",
                    subject=subject,
                    message_count=len(messages),
                    retry_count=retry_count + 1,
                )
            except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Retry failures must be tracked
                still_failed[subject] = messages
                logger.warning(
                    "Batch group failed on retry",
                    subject=subject,
                    message_count=len(messages),
                    retry_count=retry_count + 1,
                    error=str(e),
                )

        # Recursively retry still-failed groups
        if still_failed:
            await self._retry_failed_batch_groups(still_failed, retry_count + 1)

    async def recover_failed_batches(self) -> int:
        """
        Attempt to recover messages from the failed batch queue.

        Returns:
            Number of messages successfully recovered

        AI: Provides manual recovery mechanism for messages that failed after max retries.
        """
        if not self._failed_batch_queue:
            return 0

        # Move failed messages back to batch for retry
        recovered_count = 0
        failed_messages = self._failed_batch_queue.copy()
        self._failed_batch_queue.clear()

        for subject, data in failed_messages:
            try:
                # Try to publish individually (not batched)
                await self.publish_with_pool(subject, data)
                recovered_count += 1
                logger.debug("Recovered failed batch message", subject=subject, message_id=data.get("message_id"))
            except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Recovery failures must be logged but not fail
                # Add back to failed queue if recovery fails
                self._failed_batch_queue.append((subject, data))
                logger.warning(
                    "Failed to recover batch message",
                    subject=subject,
                    message_id=data.get("message_id"),
                    error=str(e),
                )

        if recovered_count > 0:
            logger.info(
                "Recovered failed batch messages", recovered_count=recovered_count, total_attempted=len(failed_messages)
            )

        return recovered_count
