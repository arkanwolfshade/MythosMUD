"""Attribute stubs for EventBus mixins (mypy attr-defined).

Mirrors server/realtime/nats_message_handler_base.py.
"""

# Stub-only attrs are provided by EventBus at runtime.
# pyright: reportUninitializedInstanceVariable=false

from __future__ import annotations

import asyncio
from collections.abc import Callable

from anyio import Event
from structlog.stdlib import BoundLogger

from .event_types import BaseEvent


class EventBusMixinBase:  # pylint: disable=too-few-public-methods  # Reason: Mixin; methods are _-prefixed by design
    """Attrs/methods provided by EventBus when mixed in."""

    _subscribers: dict[type[BaseEvent], list[Callable[[BaseEvent], object]]]
    _event_queue: asyncio.Queue[BaseEvent | None]
    _running: bool
    _logger: BoundLogger
    _active_tasks: set[asyncio.Task[object]]
    _shutdown_event: Event
    _processing_task: asyncio.Task[object] | None
    _subscriber_tracking: dict[str, list[tuple[type[BaseEvent], Callable[[BaseEvent], object]]]]

    def _ensure_async_processing(self) -> None:
        """Start the async consumer. Real impl is EventBusLifecycleMixin."""
        return None

    async def _process_events_async(self) -> None:
        """Drain the event queue. Real impl is EventBusProcessingMixin."""
        return None

    def unsubscribe_all_for_service(self, service_id: str) -> int:
        """Drop tracked service handlers. Real impl is EventBus."""
        del service_id
        return 0
