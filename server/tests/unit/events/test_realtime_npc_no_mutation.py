"""
Ensure RealTimeEventHandler does not mutate Room state on NPCEnteredRoom/NPCLeftRoom.

Room state must be mutated by Room API callers (e.g., lifecycle/spawning), and
the handler should only broadcast updates. This guards against duplicate
"NPC already in room" warnings and double-publish loops reminiscent of certain
Arkham case studies.
"""

from unittest.mock import MagicMock

from server.events.event_bus import EventBus
from server.events.event_types import NPCEnteredRoom, NPCLeftRoom
from server.realtime.event_handler import RealTimeEventHandler


class _FakeRoom:
    def __init__(self) -> None:
        self.npc_entered_called = False
        self.npc_left_called = False

    # Room API (should NOT be invoked by the handler)
    def npc_entered(self, npc_id: str) -> None:  # pragma: no cover - if called, test fails below
        self.npc_entered_called = True

    def npc_left(self, npc_id: str) -> None:  # pragma: no cover - if called, test fails below
        self.npc_left_called = True

    # Minimal surface used by handler for occupants snapshot
    def get_players(self) -> list[str]:  # pragma: no cover
        return []

    def get_npcs(self) -> list[str]:  # pragma: no cover
        return []


class _FakePersistence:
    def __init__(self, room: _FakeRoom | None) -> None:
        self._room = room

    def get_room(self, room_id: str):  # pragma: no cover
        return self._room


async def test_event_handler_does_not_mutate_room_on_npc_events() -> None:
    event_bus = EventBus()
    connection_manager = MagicMock()
    handler = RealTimeEventHandler(event_bus=event_bus, connection_manager=connection_manager)

    fake_room = _FakeRoom()
    handler.connection_manager.persistence = _FakePersistence(fake_room)

    # NPC enters
    await handler._handle_npc_entered(NPCEnteredRoom(npc_id="npc_001", room_id="room_001"))
    assert fake_room.npc_entered_called is False

    # NPC leaves
    await handler._handle_npc_left(NPCLeftRoom(npc_id="npc_001", room_id="room_001"))
    assert fake_room.npc_left_called is False
