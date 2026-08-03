"""Unit tests for DistributedEventBus."""

import asyncio
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from server.events.distributed_event_bus import DistributedEventBus
from server.events.event_types import BaseEvent


class SampleEvent(BaseEvent):
    """Minimal event for distributed bus tests."""


@pytest.fixture
def distributed_bus() -> DistributedEventBus:
    """Create a DistributedEventBus without NATS."""
    return DistributedEventBus()


def test_distributed_event_bus_init_without_nats(distributed_bus: DistributedEventBus) -> None:
    """Single-instance mode has no bridge until NATS is set."""
    assert distributed_bus._nats_service is None  # pylint: disable=protected-access
    assert distributed_bus._nats_bridge is None  # pylint: disable=protected-access
    assert distributed_bus._instance_id  # pylint: disable=protected-access


def test_set_nats_service_same_reference_noop(distributed_bus: DistributedEventBus) -> None:
    """Setting the same NATS service twice does not recreate the bridge."""
    nats = MagicMock()
    distributed_bus.set_nats_service(nats)
    bridge_first = distributed_bus._nats_bridge  # pylint: disable=protected-access
    distributed_bus.set_nats_service(nats)
    assert distributed_bus._nats_bridge is bridge_first  # pylint: disable=protected-access


@pytest.mark.asyncio
async def test_publish_without_nats_delegates_to_parent(distributed_bus: DistributedEventBus) -> None:
    """Publish without NATS behaves like plain EventBus."""
    handler = AsyncMock()
    distributed_bus.subscribe(SampleEvent, handler)
    event = SampleEvent()
    distributed_bus.publish(event)
    await asyncio.sleep(0.1)
    handler.assert_awaited()


@pytest.mark.asyncio
async def test_publish_with_nats_bridge_publishes_to_nats() -> None:
    """When bridge is active, publish also sends to NATS."""
    nats = MagicMock()
    bus = DistributedEventBus()
    mock_bridge = MagicMock()
    mock_bridge.publish = AsyncMock()
    bus._nats_bridge = mock_bridge  # pylint: disable=protected-access
    bus._nats_service = nats  # pylint: disable=protected-access

    event = SampleEvent()
    bus.publish(event)
    await asyncio.sleep(0.05)
    mock_bridge.publish.assert_awaited_once_with(event)


@pytest.mark.asyncio
async def test_shutdown_stops_bridge(distributed_bus: DistributedEventBus) -> None:
    """Shutdown awaits bridge stop before parent shutdown."""
    mock_bridge = MagicMock()
    mock_bridge.stop = AsyncMock()
    distributed_bus._nats_bridge = mock_bridge  # pylint: disable=protected-access

    await distributed_bus.shutdown()
    mock_bridge.stop.assert_awaited_once()


@pytest.mark.asyncio
async def test_shutdown_bridge_stop_error_is_swallowed(distributed_bus: DistributedEventBus) -> None:
    """Bridge stop errors do not prevent shutdown."""
    mock_bridge = MagicMock()
    mock_bridge.stop = AsyncMock(side_effect=RuntimeError("nats gone"))
    distributed_bus._nats_bridge = mock_bridge  # pylint: disable=protected-access

    await distributed_bus.shutdown()
    mock_bridge.stop.assert_awaited_once()


@pytest.mark.asyncio
async def test_set_nats_service_starts_bridge_when_loop_running() -> None:
    """set_nats_service creates bridge and schedules start when loop is running."""
    nats = MagicMock()
    bus = DistributedEventBus()

    with patch("server.events.distributed_event_bus.NATSEventBusBridge") as mock_bridge_cls:
        mock_bridge = MagicMock()
        mock_bridge.start = AsyncMock()
        mock_bridge_cls.return_value = mock_bridge

        bus.set_nats_service(nats)
        await asyncio.sleep(0.05)
        mock_bridge_cls.assert_called_once()
        mock_bridge.start.assert_awaited()
