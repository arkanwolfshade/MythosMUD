"""
Integration test to ensure spawning an NPC results in a single NPCEnteredRoom
event and no duplicate room mutations.
"""

import asyncio
from types import SimpleNamespace
from typing import cast

import pytest

from server.events.event_bus import EventBus
from server.events.event_types import NPCEnteredRoom
from server.models.npc import NPCDefinition
from server.models.room import Room
from server.npc.lifecycle_manager import NPCLifecycleManager
from server.npc.spawning_service import NPCSpawningService


class _FakePersistence:
    def __init__(self, room: Room):
        self._room = room

    def get_room(self, room_id: str):  # pragma: no cover
        return self._room if self._room.id == room_id else None


@pytest.mark.asyncio
async def test_spawn_npc_emits_single_enter_event(monkeypatch) -> None:
    event_bus = EventBus()

    # Wire a real Room with the same event bus so it publishes via the bus
    room = Room({"id": "room_001", "name": "Test Room", "exits": {}}, event_bus=event_bus)
    fake_persistence = _FakePersistence(room)

    # Patch get_persistence used inside lifecycle_manager.spawn_npc
    import server.npc.lifecycle_manager as lm

    monkeypatch.setattr(lm, "get_persistence", lambda: fake_persistence)

    # Capture NPCEnteredRoom events
    events: list[NPCEnteredRoom] = []
    event_bus.subscribe(NPCEnteredRoom, lambda e: events.append(e))

    # Minimal NPC definition compatible with spawning service (cast for mypy)
    def_ns = SimpleNamespace(
        id=1,
        name="Test NPC",
        npc_type="passive_mob",
        room_id=None,
        base_stats="{}",
        behavior_config="{}",
        ai_integration_stub="{}",
        sub_zone_id="arkhamcity",  # unused in this path
        is_required=lambda: False,
        can_spawn=lambda current: True,
        spawn_probability=1.0,
    )
    definition: NPCDefinition = cast(NPCDefinition, def_ns)

    spawning_service = NPCSpawningService(event_bus, population_controller=None)
    lifecycle_manager = NPCLifecycleManager(
        event_bus, population_controller=None, spawning_service=spawning_service, persistence=None
    )

    npc_id = lifecycle_manager.spawn_npc(definition, "room_001")

    # Allow async EventBus to process the event
    await asyncio.sleep(0.05)

    # Exactly one event emitted
    assert len(events) == 1
    assert events[0].npc_id == npc_id
    assert events[0].room_id == "room_001"

    # Room should contain the spawned NPC
    assert npc_id in room.get_npcs()
