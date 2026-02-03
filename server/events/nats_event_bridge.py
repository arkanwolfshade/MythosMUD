"""
NATS EventBus bridge for distributed event distribution.

Publishes domain events to NATS and subscribes to receive events from other
instances, enabling horizontal scaling of the EventBus across multiple servers.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from ..structured_logging.enhanced_logging_config import get_logger
from .event_serialization import deserialize_event, serialize_event
from .event_types import BaseEvent

if TYPE_CHECKING:
    from ..services.nats_service import NATSService

DOMAIN_EVENTS_SUBJECT_PREFIX = "events.domain"
DOMAIN_EVENTS_SUBJECT_PATTERN = "events.domain.>"

logger = get_logger(__name__)


class NATSEventBusBridge:
    """
    Bridges domain events between local EventBus and NATS for distribution.

    When events are published locally, they are also published to NATS.
    When events are received from NATS (from other instances), they are
    injected into the local EventBus for dispatch to subscribers.
    """

    def __init__(self, event_bus: Any, nats_service: NATSService) -> None:
        """
        Initialize the NATS EventBus bridge.

        Args:
            event_bus: Local EventBus instance (must have inject method)
            nats_service: NATS service for publish/subscribe
        """
        self._event_bus = event_bus
        self._nats_service = nats_service
        self._subscription: Any = None
        self._running = False

    def _subject_for_event(self, event: BaseEvent) -> str:
        """Build NATS subject for an event."""
        event_type = getattr(event, "event_type", type(event).__name__)
        return f"{DOMAIN_EVENTS_SUBJECT_PREFIX}.{event_type}"

    async def publish(self, event: BaseEvent) -> None:
        """
        Publish event to NATS for distribution to other instances.

        Args:
            event: Domain event to publish
        """
        try:
            data = serialize_event(event)
            subject = self._subject_for_event(event)
            await self._nats_service.publish(subject, data)
            logger.debug(
                "Published domain event to NATS",
                subject=subject,
                event_type=type(event).__name__,
            )
        except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904
            logger.warning(
                "Failed to publish domain event to NATS",
                event_type=type(event).__name__,
                error=str(e),
                exc_info=True,
            )

    async def _handle_nats_message(self, message_data: dict[str, Any]) -> None:
        """Handle message received from NATS - deserialize and inject into local EventBus."""
        try:
            event = deserialize_event(message_data)
            self._event_bus.inject(event)
            logger.debug(
                "Injected domain event from NATS",
                event_type=type(event).__name__,
            )
        except ValueError as e:
            logger.warning(
                "Failed to deserialize domain event from NATS",
                error=str(e),
                message_keys=list(message_data.keys())[:5],
            )
        except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904
            logger.error(
                "Error handling domain event from NATS",
                error=str(e),
                exc_info=True,
            )

    async def start(self) -> None:
        """Subscribe to NATS domain events and start receiving."""
        if self._running:
            return
        try:
            await self._nats_service.subscribe(
                DOMAIN_EVENTS_SUBJECT_PATTERN,
                self._handle_nats_message,
            )
            self._running = True
            logger.info(
                "NATS EventBus bridge started",
                subject_pattern=DOMAIN_EVENTS_SUBJECT_PATTERN,
            )
        except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904
            logger.error(
                "Failed to start NATS EventBus bridge",
                error=str(e),
                exc_info=True,
            )

    async def stop(self) -> None:
        """Stop the bridge and unsubscribe from NATS."""
        self._running = False
        logger.debug("NATS EventBus bridge stopped")
