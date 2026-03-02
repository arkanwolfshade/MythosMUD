"""Tests for NATS EventBus bridge - skip self-echo to prevent duplicate event processing."""

import pytest

from server.events.event_types import NPCEnteredRoom
from server.events.nats_event_bridge import NATSEventBusBridge


@pytest.mark.asyncio
async def test_handle_nats_message_skips_own_origin():
    """NATS bridge must not inject events that originated from this instance (prevents duplicate)."""
    inject_called = []

    def capture_inject(event):
        inject_called.append(event)

    mock_bus = type("MockBus", (), {})()
    mock_bus.inject = capture_inject
    mock_nats = type("MockNats", (), {})()
    instance_id = "test-instance-123"
    bridge = NATSEventBusBridge(event_bus=mock_bus, nats_service=mock_nats, instance_id=instance_id)

    message_data = {
        "_event_type": "NPCEnteredRoom",
        "_origin_instance_id": instance_id,
        "npc_id": "npc_001",
        "room_id": "room_001",
        "from_room_id": None,
    }
    await bridge.handle_nats_message(message_data)

    assert len(inject_called) == 0, "Should skip inject when origin matches instance"


@pytest.mark.asyncio
async def test_handle_nats_message_injects_remote_origin():
    """NATS bridge must inject events from other instances."""
    inject_called = []

    def capture_inject(event):
        inject_called.append(event)

    mock_bus = type("MockBus", (), {})()
    mock_bus.inject = capture_inject
    mock_nats = type("MockNats", (), {})()
    bridge = NATSEventBusBridge(event_bus=mock_bus, nats_service=mock_nats, instance_id="local-instance")

    message_data = {
        "_event_type": "NPCEnteredRoom",
        "_origin_instance_id": "remote-instance-456",
        "npc_id": "npc_001",
        "room_id": "room_001",
        "from_room_id": None,
    }
    await bridge.handle_nats_message(message_data)

    assert len(inject_called) == 1
    assert isinstance(inject_called[0], NPCEnteredRoom)
    assert inject_called[0].npc_id == "npc_001"
