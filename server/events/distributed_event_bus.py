"""
Distributed EventBus that uses NATS for cross-instance event distribution.

Wraps the local EventBus and publishes domain events to NATS when configured,
enabling horizontal scaling across multiple server instances.
"""

from __future__ import annotations

import asyncio
from typing import Any, TypeVar

from ..structured_logging.enhanced_logging_config import get_logger
from .event_bus import EventBus
from .event_types import BaseEvent
from .nats_event_bridge import NATSEventBusBridge

T = TypeVar("T", bound=BaseEvent)

logger = get_logger(__name__)


class DistributedEventBus(EventBus):
    """
    EventBus that distributes domain events via NATS for horizontal scaling.

    When nats_service is set, events published locally are also published to
    NATS. Events received from NATS (from other instances) are injected into
    the local queue for dispatch. When nats_service is None, behaves exactly
    like a plain EventBus (single-instance mode).
    """

    def __init__(self, nats_service: Any = None) -> None:
        """
        Initialize distributed EventBus.

        Args:
            nats_service: NATS service for distribution (None = single-instance mode)
        """
        super().__init__()
        self._nats_service = nats_service
        self._nats_bridge: NATSEventBusBridge | None = None

    def set_nats_service(self, nats_service: Any) -> None:
        """Set NATS service and start the bridge (call after NATS connects)."""
        if self._nats_service is nats_service:
            return
        self._nats_service = nats_service
        if nats_service:
            self._nats_bridge = NATSEventBusBridge(event_bus=self, nats_service=nats_service)
            # Start bridge - fire and forget; it subscribes to NATS
            try:
                loop = asyncio.get_running_loop()
                loop.create_task(self._nats_bridge.start())
            except RuntimeError:
                logger.debug("No event loop - NATS bridge will start when loop available")

    def publish(self, event: BaseEvent) -> None:
        """Publish event locally and to NATS when bridge is active."""
        super().publish(event)
        if self._nats_bridge and self._nats_service:
            try:
                loop = asyncio.get_running_loop()
                loop.create_task(self._nats_bridge.publish(event))
            except RuntimeError:
                pass

    async def shutdown(self) -> None:
        """Shutdown EventBus and stop NATS bridge."""
        if self._nats_bridge:
            try:
                await self._nats_bridge.stop()
            except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904
                logger.debug("Error stopping NATS bridge", error=str(e))
        await super().shutdown()
