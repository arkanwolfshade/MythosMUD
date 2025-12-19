"""
Debug test to identify infinite loop in async fixtures.
"""

import asyncio

import pytest

from server.events.event_bus import EventBus


@pytest.mark.asyncio
async def test_event_bus_creation_and_shutdown():
    """Test basic EventBus creation and shutdown to identify infinite loop."""
    print("Creating EventBus...")
    event_bus = EventBus()

    print("Setting main loop...")
    try:
        loop = asyncio.get_running_loop()
        event_bus.set_main_loop(loop)
        print("Main loop set successfully")
    except RuntimeError:
        print("No running loop available")

    print("Publishing test event...")
    from uuid import uuid4

    from server.events import PlayerLeftRoom

    event = PlayerLeftRoom(player_id=str(uuid4()), room_id=str(uuid4()))
    # Fix assignment to datetime field
    from typing import Any, cast

    cast(Any, event).timestamp = None
    event_bus.publish(event)

    print("Waiting for processing...")
    await asyncio.sleep(0.1)

    print("Shutting down EventBus...")
    await event_bus.shutdown()
    print("EventBus shutdown complete")


@pytest.mark.asyncio
async def test_async_fixture_directly(_async_event_bus):
    """Test the async_event_bus fixture directly."""
    print("Getting async_event_bus fixture...")
    print("Got EventBus from fixture")
    print("Test complete")
    # The async_event_bus fixture is an async generator, not an EventBus instance
    # We don't need to call shutdown() on it
