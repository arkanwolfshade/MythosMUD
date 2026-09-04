# Test Npc Event Handlers

> 31 nodes

## Key Concepts

- **asyncio** (16 connections)
- **test_handle_npc_entered_no_connection_manager()** (4 connections) — `server/tests/unit/realtime/test_npc_event_handlers.py`
- **test_handle_npc_entered_no_persistence()** (4 connections) — `server/tests/unit/realtime/test_npc_event_handlers.py`
- **test_handle_npc_entered_room()** (4 connections) — `server/tests/unit/realtime/test_npc_event_handlers.py`
- **test_handle_npc_entered_room_not_found()** (4 connections) — `server/tests/unit/realtime/test_npc_event_handlers.py`
- **test_handle_npc_entered_room_with_npc_instance()** (4 connections) — `server/tests/unit/realtime/test_npc_event_handlers.py`
- **test_handle_npc_left_no_connection_manager()** (4 connections) — `server/tests/unit/realtime/test_npc_event_handlers.py`
- **test_handle_npc_left_no_persistence()** (4 connections) — `server/tests/unit/realtime/test_npc_event_handlers.py`
- **test_handle_npc_left_room()** (4 connections) — `server/tests/unit/realtime/test_npc_event_handlers.py`
- **test_handle_npc_left_room_not_found()** (4 connections) — `server/tests/unit/realtime/test_npc_event_handlers.py`
- **test_handle_npc_left_room_with_npc_instance()** (4 connections) — `server/tests/unit/realtime/test_npc_event_handlers.py`
- **test_determine_direction_from_rooms_no_match()** (3 connections) — `server/tests/unit/realtime/test_npc_event_handlers.py`
- **test_determine_direction_from_rooms_no_persistence()** (3 connections) — `server/tests/unit/realtime/test_npc_event_handlers.py`
- **test_determine_direction_from_rooms_room_not_found()** (3 connections) — `server/tests/unit/realtime/test_npc_event_handlers.py`
- **test_send_room_message_no_connection_manager()** (3 connections) — `server/tests/unit/realtime/test_npc_event_handlers.py`
- **test_send_room_message_no_room_manager()** (3 connections) — `server/tests/unit/realtime/test_npc_event_handlers.py`
- **Test handle_npc_entered_room() processes event.** (1 connections) — `server/tests/unit/realtime/test_npc_event_handlers.py`
- **Test handle_npc_left_room() processes event.** (1 connections) — `server/tests/unit/realtime/test_npc_event_handlers.py`
- **Test handle_npc_entered_room() with valid NPC instance.** (1 connections) — `server/tests/unit/realtime/test_npc_event_handlers.py`
- **Test handle_npc_left_room() with valid NPC instance.** (1 connections) — `server/tests/unit/realtime/test_npc_event_handlers.py`
- **Test _determine_direction_from_rooms() returns None when persistence not…** (1 connections) — `server/tests/unit/realtime/test_npc_event_handlers.py`
- **Test _determine_direction_from_rooms() returns None when room not found.** (1 connections) — `server/tests/unit/realtime/test_npc_event_handlers.py`
- **Test _determine_direction_from_rooms() returns None when no matching exit.** (1 connections) — `server/tests/unit/realtime/test_npc_event_handlers.py`
- **Test _send_room_message() handles missing connection_manager.** (1 connections) — `server/tests/unit/realtime/test_npc_event_handlers.py`
- **Test _send_room_message() handles missing room_manager.** (1 connections) — `server/tests/unit/realtime/test_npc_event_handlers.py`
- *... and 6 more nodes in this community*

## Relationships

- [Test Npc Event Handlers](Test_Npc_Event_Handlers.md) (15 shared connections)
- [Async Persistence & NPC Events](Async_Persistence_&_NPC_Events.md) (10 shared connections)
- [Npc Event Handlers](Npc_Event_Handlers.md) (1 shared connections)

## Source Files

- `server/tests/unit/realtime/test_npc_event_handlers.py`

## Audit Trail

- EXTRACTED: 46 (82%)
- INFERRED: 10 (18%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*