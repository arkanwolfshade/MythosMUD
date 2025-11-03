"""
Test utilities for coordinating with the async EventBus.

Provides a helper to drain the EventBus queue and let any scheduled
tasks complete before assertions.
"""

import asyncio
from typing import Any


async def drain_event_bus(event_bus: Any, timeout: float = 0.2) -> None:
    """Await briefly to allow EventBus to process queued events.

    This helper is intentionally simple; the EventBus processes events on the
    running loop. A short sleep yields control so the queue can be drained.

    Args:
        event_bus: EventBus instance (unused introspectively, for future use)
        timeout: seconds to await
    """
    try:
        await asyncio.sleep(timeout)
    except Exception:
        # In sync contexts converted with pytest-asyncio, guard against oddities
        pass
