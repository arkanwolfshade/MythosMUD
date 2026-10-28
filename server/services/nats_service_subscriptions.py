"""NATS subscription lifecycle and message-ack helpers (extracted from nats_service)."""

# pylint: disable=too-many-lines,missing-class-docstring,missing-function-docstring,too-few-public-methods  # Reason: Subscription mixin stays one module; Protocol stubs (PEP 544)

from __future__ import annotations

import asyncio
import inspect
import json
import time
from collections.abc import Awaitable, Callable
from typing import Protocol, cast

from nats.aio.client import Client
from nats.aio.msg import Msg
from nats.aio.subscription import Subscription

from ..config.models import NATSConfig
from ..structured_logging.enhanced_logging_config import get_logger
from .nats_exceptions import NATSSubscribeError, NATSUnsubscribeError
from .nats_metrics import NATSMetrics

logger = get_logger("nats")

JsonMap = dict[str, object]

__all__ = [
    "JsonMap",
    "NATSServiceSubscriptionMixin",
    "NatsMessageCallback",
    "NatsSubscription",
    "as_json_map",
]


class _NatsSubscribeFn(Protocol):
    async def __call__(self, subject: str, *, cb: Callable[[Msg], Awaitable[None]] | None = None) -> Subscription:
        _ = cb
        raise NotImplementedError


class NatsMessageCallback(Protocol):
    def __call__(self, message_data: JsonMap) -> None | Awaitable[None]: ...


class NatsSubscription(Protocol):
    async def drain(self) -> None: ...

    async def unsubscribe(self) -> None: ...


def as_json_map(value: object) -> JsonMap:
    if not isinstance(value, dict):
        raise TypeError("NATS payload must be a JSON object")
    typed = cast(dict[object, object], value)
    return {str(k): v for k, v in typed.items()}


class NATSServiceSubscriptionMixin:
    """Subscription/ack helpers mixed into NATSService. Attributes set in NATSService.__init__."""

    config: NATSConfig  # pyright: ignore[reportUninitializedInstanceVariable]
    metrics: NATSMetrics  # pyright: ignore[reportUninitializedInstanceVariable]
    nc: Client | None  # pyright: ignore[reportUninitializedInstanceVariable]
    subscriptions: dict[str, NatsSubscription]  # pyright: ignore[reportUninitializedInstanceVariable]
    _running: bool  # pyright: ignore[reportUninitializedInstanceVariable]
    _subscription_timestamps: list[tuple[str, float]]  # pyright: ignore[reportUninitializedInstanceVariable]
    _unsubscription_timestamps: list[tuple[str, float]]  # pyright: ignore[reportUninitializedInstanceVariable]
    _subscription_count: int  # pyright: ignore[reportUninitializedInstanceVariable]
    _unsubscription_count: int  # pyright: ignore[reportUninitializedInstanceVariable]
    _last_cleanup_time: float | None  # pyright: ignore[reportUninitializedInstanceVariable]
    _max_timestamp_history: int  # pyright: ignore[reportUninitializedInstanceVariable]

    async def _drain_subscriptions(self) -> None:
        """Drain in-flight messages from all subscriptions."""
        for subject, subscription in self.subscriptions.items():
            try:
                await subscription.drain()
                logger.debug("Subscription drained", subject=subject)
            except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Subscription drain errors unpredictable, must not fail cleanup
                logger.warning("Error draining subscription", subject=subject, error=str(e))

    async def _close_all_subscriptions(self) -> None:
        """Close and unsubscribe from all subscriptions."""

        for subject, subscription in self.subscriptions.items():
            try:
                await subscription.unsubscribe()
                # Track unsubscription for metrics
                self._unsubscription_count += 1  # pylint: disable=no-member  # Reason: astroid does not infer an augmented-assignment read against a bare class-level annotation on a mixin with no __init__; declared and set on NATSService.__init__
                self._unsubscription_timestamps.append((subject, time.time()))
                # Keep only last N timestamps to prevent unbounded growth
                if len(self._unsubscription_timestamps) > self._max_timestamp_history:
                    self._unsubscription_timestamps = self._unsubscription_timestamps[-self._max_timestamp_history :]
                logger.debug("Unsubscribed from NATS subject", subject=subject)
            except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Unsubscribe errors unpredictable, must not fail cleanup
                logger.warning("Error unsubscribing from subject", subject=subject, error=str(e))

    def _verify_subscription_cleanup(self, subscriptions_before_cleanup: list[str]) -> None:
        """Verify all subscriptions were cleaned up and log warnings if any remain."""

        self._last_cleanup_time = time.time()
        remaining_subscriptions = list(self.subscriptions.keys())
        if remaining_subscriptions:
            logger.warning(
                "Subscriptions remain after cleanup",
                remaining_subscriptions=remaining_subscriptions,
                total_before=len(subscriptions_before_cleanup),
            )
        else:
            logger.info(
                "All NATS subscriptions cleaned up successfully",
                total_cleaned=len(subscriptions_before_cleanup),
            )

    async def _decode_message_data(self, msg: Msg) -> JsonMap:
        """Decode message data from NATS message."""
        loop = asyncio.get_running_loop()
        payload = msg.data

        def _loads() -> JsonMap:
            return as_json_map(cast(object, json.loads(payload.decode("utf-8"))))

        return await loop.run_in_executor(None, _loads)

    async def _call_callback(self, callback: NatsMessageCallback, message_data: JsonMap) -> None:
        """Call the registered callback, handling both async and sync callbacks.
        Sync callbacks must not perform blocking I/O (see subscribe() docstring).
        """
        maybe = callback(message_data)
        if inspect.iscoroutine(maybe):
            await maybe

    async def _acknowledge_message(self, msg: Msg, subject: str, message_data: JsonMap) -> bool:
        """
        Acknowledge message if manual ack is enabled. Returns True if acknowledged.

        AI: Records metrics for acknowledgment success/failure for monitoring.
        """
        if not hasattr(msg, "ack"):
            return False

        try:
            await msg.ack()
            self.metrics.record_ack_success()
            logger.debug(
                "Message acknowledged",
                subject=subject,
                message_id=message_data.get("message_id"),
            )
            return True
        except Exception as ack_error:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Message ack errors unpredictable, must log but continue
            self.metrics.record_ack_failure()
            logger.error(
                "Failed to acknowledge message",
                error=str(ack_error),
                subject=subject,
                message_id=message_data.get("message_id"),
            )
            return False

    async def _negatively_acknowledge_message(self, msg: Msg, subject: str) -> None:
        """
        Negatively acknowledge message if manual ack is enabled.

        AI: Records metrics for negative acknowledgments (requeue requests).
        """
        if not hasattr(msg, "nak"):
            return

        try:
            await msg.nak()
            self.metrics.record_nak()
            logger.debug("Message negatively acknowledged (requeued)", subject=subject)
        except Exception as nak_error:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Message nak errors unpredictable, must log but continue
            logger.error("Failed to negatively acknowledge message", error=str(nak_error), subject=subject)

    async def subscribe(self, subject: str, callback: NatsMessageCallback) -> None:
        """
        Subscribe to a NATS subject and register a callback for incoming messages.

        Args:
            subject: NATS subject name to subscribe to
            callback: Sync or async function when messages are received (message_data: dict).
                Prefer async callbacks; they must not perform blocking I/O. Sync callbacks are
                supported for backward compatibility but must complete quickly (no I/O) to avoid
                blocking the event loop.

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

            manual_ack_enabled = self.config.manual_ack

            async def message_handler(msg: Msg) -> None:
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

            subscribe = cast(_NatsSubscribeFn, self.nc.subscribe)
            subscription = await subscribe(subject, cb=message_handler)
            # Track subscription for metrics

            self._subscription_count += 1  # pylint: disable=no-member  # Reason: astroid does not infer an augmented-assignment read against a bare class-level annotation on a mixin with no __init__; declared and set on NATSService.__init__
            self._subscription_timestamps.append((subject, time.time()))
            # Keep only last N timestamps to prevent unbounded growth
            if len(self._subscription_timestamps) > self._max_timestamp_history:
                self._subscription_timestamps = self._subscription_timestamps[-self._max_timestamp_history :]
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

    def get_active_subscriptions(self) -> list[str]:
        """
        Get list of all active NATS subscription subjects.

        Returns:
            List of subject names that are currently subscribed

        This method is used for monitoring and verification during shutdown
        to ensure all subscriptions are properly cleaned up.
        """
        return list(self.subscriptions.keys())

    async def unsubscribe(self, subject: str) -> None:
        """
        Unsubscribe from a NATS subject.

        Args:
            subject: NATS subject name to unsubscribe from

        Raises:
            NATSUnsubscribeError: If unsubscribe fails or subject is not subscribed

        AI: Raises exceptions instead of returning False for better error handling.
        """
        try:
            if subject not in self.subscriptions:
                error_msg = f"Not subscribed to NATS subject: {subject}"
                logger.warning("Not subscribed to NATS subject", subject=subject)
                raise NATSUnsubscribeError(error_msg, subject=subject)

            subscription = self.subscriptions[subject]
            await subscription.unsubscribe()
            del self.subscriptions[subject]

            logger.info("Unsubscribed from NATS subject", subject=subject)

        except NATSUnsubscribeError:
            raise
        except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Unsubscribe errors unpredictable, must handle and raise
            error_msg = f"Failed to unsubscribe from NATS subject: {str(e)}"
            logger.error("Failed to unsubscribe from NATS subject", error=str(e), subject=subject)
            raise NATSUnsubscribeError(error_msg, subject=subject, error=e) from e

    def verify_subscription_cleanup(self) -> JsonMap:
        """
        Verify that all subscriptions are properly cleaned up.

        Returns:
            Dictionary with cleanup verification status
        """
        active_subscriptions = self.get_active_subscriptions()
        cleanup_verified = not active_subscriptions  # pylint: disable=use-implicit-booleaness-not-comparison-to-zero  # Reason: Empty list is falsy, explicit comparison unnecessary

        return {
            "cleanup_verified": cleanup_verified,
            "active_subscriptions_count": len(active_subscriptions),
            "active_subscriptions": active_subscriptions,
            "last_cleanup_time": self._last_cleanup_time,
            "subscription_count_total": self._subscription_count,  # pylint: disable=no-member  # Reason: astroid does not infer this bare class-level annotation on a mixin with no __init__; declared and set on NATSService.__init__
            "unsubscription_count_total": self._unsubscription_count,  # pylint: disable=no-member  # Reason: astroid does not infer this bare class-level annotation on a mixin with no __init__; declared and set on NATSService.__init__
        }

    def get_subscription_count(self) -> int:
        """
        Get the number of active subscriptions.

        Returns:
            Number of active subscriptions
        """
        return len(self.subscriptions)
