"""NATS connection pool and batch publishing (extracted from nats_service)."""

# pylint: disable=too-many-lines,missing-class-docstring,missing-function-docstring  # Reason: Pool mixin stays one module

from __future__ import annotations

import asyncio
import json
import time
from collections.abc import Coroutine, Mapping

from anyio import sleep
from nats.aio.client import Client

from ..config.models import NATSConfig
from ..structured_logging.enhanced_logging_config import get_logger
from .nats_exceptions import NATSPublishError
from .nats_metrics import NATSMetrics
from .nats_service_connect import NatsConnectOptions, configure_nats_tls, nats_connect
from .nats_subject_manager import NATSSubjectManager, SubjectValidationError

logger = get_logger("nats")

__all__ = ["NATSServicePoolMixin", "NatsConnectOptions", "nats_connect"]


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
        configure_nats_tls(self.config, connect_options)

    async def _create_pool_connections(
        self, nats_url: str, connect_options: NatsConnectOptions
    ) -> tuple[int, int, list[str]]:
        """Create pool connections; return success/fail counts and error messages."""
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
                connection_errors.append(f"Connection {i + 1}: {str(conn_error)}")
                logger.warning(
                    "Failed to create connection pool connection",
                    connection_index=i + 1,
                    pool_size=self.pool_size,
                    error=str(conn_error),
                )

        return successful_connections, failed_connections, connection_errors

    def _finalize_pool_init_status(
        self,
        nats_url: str,
        successful_connections: int,
        failed_connections: int,
        connection_errors: list[str],
    ) -> None:
        """Set pool initialized flag and log full/partial/none success."""
        if not successful_connections:
            self._pool_initialized = False
            logger.error(
                "Failed to initialize NATS connection pool - no connections succeeded",
                pool_size=self.pool_size,
                failed_connections=failed_connections,
                errors=connection_errors,
            )
            return

        self._pool_initialized = True
        if successful_connections < self.pool_size:
            logger.warning(
                "NATS connection pool initialized with partial success",
                pool_size=self.pool_size,
                successful_connections=successful_connections,
                failed_connections=failed_connections,
                actual_pool_size=len(self.connection_pool),
                errors=connection_errors,
            )
            return

        logger.info(
            "NATS connection pool initialized successfully",
            pool_size=self.pool_size,
            url=nats_url,
        )

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
            successful, failed, errors = await self._create_pool_connections(nats_url, connect_options)
            self._finalize_pool_init_status(nats_url, successful, failed, errors)
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

    def _validate_pool_publish_subject(self, subject: str, data: Mapping[str, object]) -> None:
        """Validate subject when subject manager and validation are enabled."""
        if not (self.subject_manager and self.config.enable_subject_validation):
            return
        try:
            if not self.subject_manager.validate_subject(subject):
                logger.error(
                    "Subject validation failed",
                    subject=subject,
                    message_id=data.get("message_id"),
                    correlation_id=data.get("correlation_id"),
                )
                raise NATSPublishError(f"Subject validation failed: {subject}", subject=subject)
        except SubjectValidationError as e:
            logger.error(
                "Subject validation error",
                error=str(e),
                subject=subject,
                message_id=data.get("message_id"),
                correlation_id=data.get("correlation_id"),
            )
            raise NATSPublishError(f"Subject validation error: {str(e)}", subject=subject, error=e) from e

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
            self._validate_pool_publish_subject(subject, data)
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
            try:
                self._validate_pool_publish_subject(subject, data)
            except NATSPublishError:
                return False

            self.message_batch.append((subject, dict(data)))
            if len(self.message_batch) >= self.batch_size:
                await self._flush_batch()
            elif not self._batch_task:
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

    @staticmethod
    def _group_batch_messages(
        message_batch: list[tuple[str, dict[str, object]]],
    ) -> dict[str, list[Mapping[str, object]]]:
        """Group batched (subject, data) pairs by subject."""
        grouped_messages: dict[str, list[Mapping[str, object]]] = {}
        for subject, data in message_batch:
            if subject not in grouped_messages:
                grouped_messages[subject] = []
            grouped_messages[subject].append(data)
        return grouped_messages

    async def _publish_batch_groups(
        self, grouped_messages: dict[str, list[Mapping[str, object]]]
    ) -> tuple[list[str], dict[str, list[Mapping[str, object]]]]:
        """Publish each subject group; return successful subjects and failed groups."""
        successful_groups: list[str] = []
        failed_groups: dict[str, list[Mapping[str, object]]] = {}

        for subject, messages in grouped_messages.items():
            batch_data: dict[str, object] = {
                "messages": messages,
                "count": len(messages),
                "batch_timestamp": time.monotonic(),
            }
            try:
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

        return successful_groups, failed_groups

    def _record_batch_flush_metrics(
        self,
        grouped_messages: dict[str, list[Mapping[str, object]]],
        successful_groups: list[str],
    ) -> None:
        """Record batch flush metrics and log full or partial success."""
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
            return

        self.metrics.record_batch_flush(False, total_messages)
        logger.warning(
            "Message batch flushed with partial success",
            total_messages=total_messages,
            successful_messages=successful_messages,
            failed_messages=failed_messages,
            unique_subjects=len(grouped_messages),
        )

    async def _flush_batch(self) -> None:
        """
        Flush all batched messages efficiently with retry and partial flush support.

        AI: Implements partial flush - successful groups are published, failed groups are retried.
            After max retries, failed messages are added to failed batch queue for manual recovery.
        """
        if not self.message_batch:
            return

        grouped_messages = self._group_batch_messages(self.message_batch)
        successful_groups, failed_groups = await self._publish_batch_groups(grouped_messages)

        if failed_groups:
            await self._retry_failed_batch_groups(failed_groups)

        self._record_batch_flush_metrics(grouped_messages, successful_groups)

        self.message_batch.clear()
        if self._batch_task and not self._batch_task.done():
            _ = self._batch_task.cancel()
            self._batch_task = None

    def _enqueue_exhausted_batch_groups(
        self, failed_groups: dict[str, list[Mapping[str, object]]], retry_count: int
    ) -> None:
        """Move exhausted batch groups into the failed queue after max retries."""
        for subject, messages in failed_groups.items():
            for message in messages:
                self._failed_batch_queue.append((subject, dict(message)))
        logger.error(
            "Batch groups failed after max retries, added to failed queue",
            failed_groups=len(failed_groups),
            total_failed_messages=sum(len(msgs) for msgs in failed_groups.values()),
            retry_count=retry_count,
        )

    async def _attempt_retry_batch_groups(
        self, failed_groups: dict[str, list[Mapping[str, object]]], retry_count: int
    ) -> dict[str, list[Mapping[str, object]]]:
        """Retry each failed group once; return groups that still fail."""
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
        return still_failed

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
            self._enqueue_exhausted_batch_groups(failed_groups, retry_count)
            return

        # Exponential backoff: 100ms, 200ms, 400ms
        await sleep(0.1 * float(1 << retry_count))
        still_failed = await self._attempt_retry_batch_groups(failed_groups, retry_count)
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
