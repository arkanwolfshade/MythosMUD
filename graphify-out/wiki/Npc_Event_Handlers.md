# Npc Event Handlers

> 22 nodes

## Key Concepts

- **NPCEventHandler** (23 connections) — `server/realtime/npc_event_handlers.py`
- **.handle_npc_entered()** (8 connections) — `server/realtime/npc_event_handlers.py`
- **._send_npc_left_message()** (8 connections) — `server/realtime/npc_event_handlers.py`
- **.handle_npc_left()** (6 connections) — `server/realtime/npc_event_handlers.py`
- **._send_room_message()** (6 connections) — `server/realtime/npc_event_handlers.py`
- **._get_npc_name()** (5 connections) — `server/realtime/npc_event_handlers.py`
- **._schedule_room_occupants_update()** (5 connections) — `server/realtime/npc_event_handlers.py`
- **._determine_direction_from_rooms()** (4 connections) — `server/realtime/npc_event_handlers.py`
- **._get_npc_departure_message()** (4 connections) — `server/realtime/npc_event_handlers.py`
- **._validate_npc_left_room()** (4 connections) — `server/realtime/npc_event_handlers.py`
- **test_schedule_room_occupants_update_does_not_leak_coro_when_register_fails()** (4 connections) — `server/tests/unit/realtime/test_npc_event_handlers.py`
- **Get the name of an NPC by ID. Args: npc_id: The NPC ID Returns: NPC name or…** (1 connections) — `server/realtime/npc_event_handlers.py`
- **Determine the direction from one room to another by checking room exits. Args:…** (1 connections) — `server/realtime/npc_event_handlers.py`
- **Handles all NPC-related real-time events.** (1 connections) — `server/realtime/npc_event_handlers.py`
- **Get the departure message for an NPC from its behavior_config. If no custom…** (1 connections) — `server/realtime/npc_event_handlers.py`
- **Send a message to all players in a room. Args: room_id: The room ID message:…** (1 connections) — `server/realtime/npc_event_handlers.py`
- **Handle NPC entering a room. This method broadcasts NPC appearance and triggers…** (1 connections) — `server/realtime/npc_event_handlers.py`
- **Handle NPC leaving a room. This method broadcasts NPC departure and triggers…** (1 connections) — `server/realtime/npc_event_handlers.py`
- **Validate room and persistence for NPC left event.** (1 connections) — `server/realtime/npc_event_handlers.py`
- **Send movement or departure message for NPC left event.** (1 connections) — `server/realtime/npc_event_handlers.py`
- **Schedule room occupants update broadcast.** (1 connections) — `server/realtime/npc_event_handlers.py`
- **register_task RuntimeError must close the occupants coroutine (startup…** (1 connections) — `server/tests/unit/realtime/test_npc_event_handlers.py`

## Relationships

- [Npc Event Handlers](Npc_Event_Handlers.md) (7 shared connections)
- [Test Npc Event Handlers](Test_Npc_Event_Handlers.md) (4 shared connections)
- [Async Persistence & NPC Events](Async_Persistence_&_NPC_Events.md) (4 shared connections)
- [Memory Monitor & Health Alerts](Memory_Monitor_&_Health_Alerts.md) (3 shared connections)
- [Test Npc Event Handlers Helpers](Test_Npc_Event_Handlers_Helpers.md) (2 shared connections)
- [Test Npc Admin Commands](Test_Npc_Admin_Commands.md) (2 shared connections)
- [Message Builders](Message_Builders.md) (1 shared connections)
- [Test Envelope](Test_Envelope.md) (1 shared connections)

## Source Files

- `server/realtime/npc_event_handlers.py`
- `server/tests/unit/realtime/test_npc_event_handlers.py`

## Audit Trail

- EXTRACTED: 52 (93%)
- INFERRED: 4 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*