# Community 344

> 49 nodes

## Key Concepts

- **RoomEventHandler** (27 connections) — `server/realtime/integration/room_event_handler.py`
- **test_room_event_handler.py** (15 connections) — `server/tests/unit/realtime/integration/test_room_event_handler.py`
- **room_event_handler.py** (11 connections) — `server/realtime/integration/room_event_handler.py`
- **asyncio** (11 connections)
- **._broadcast_room_occupants_update()** (8 connections) — `server/realtime/integration/room_event_handler.py`
- **server/realtime/integration/__init__.py** (5 connections) — `server/realtime/integration/__init__.py`
- **_EventBusPublishPort** (4 connections) — `server/realtime/event_handlers.py`
- **._extract_valid_occupant_names()** (4 connections) — `server/realtime/integration/room_event_handler.py`
- **.handle_player_entered_room()** (4 connections) — `server/realtime/integration/room_event_handler.py`
- **.handle_player_left_room()** (4 connections) — `server/realtime/integration/room_event_handler.py`
- **.__init__()** (4 connections) — `server/realtime/integration/room_event_handler.py`
- **._publish_room_movement_nats_event()** (4 connections) — `server/realtime/integration/room_event_handler.py`
- **test_handle_player_entered_room_occupant_lookup_error_is_caught()** (4 connections) — `server/tests/unit/realtime/integration/test_room_event_handler.py`
- **test_handle_player_left_room_missing_room_id()** (4 connections) — `server/tests/unit/realtime/integration/test_room_event_handler.py`
- **Any** (4 connections)
- **.publish()** (3 connections) — `server/realtime/event_handlers.py`
- **._looks_like_uuid()** (3 connections) — `server/realtime/integration/room_event_handler.py`
- **room_handler()** (3 connections) — `server/tests/unit/realtime/integration/test_room_event_handler.py`
- **test_handle_player_entered_nats_publish_failure()** (3 connections) — `server/tests/unit/realtime/integration/test_room_event_handler.py`
- **test_handle_player_entered_room_broadcasts()** (3 connections) — `server/tests/unit/realtime/integration/test_room_event_handler.py`
- **test_handle_player_entered_room_missing_room_id()** (3 connections) — `server/tests/unit/realtime/integration/test_room_event_handler.py`
- **test_handle_player_entered_skips_uuid_player_names()** (3 connections) — `server/tests/unit/realtime/integration/test_room_event_handler.py`
- **test_handle_player_left_room_broadcasts()** (3 connections) — `server/tests/unit/realtime/integration/test_room_event_handler.py`
- **test_subscribe_handles_exception()** (3 connections) — `server/tests/unit/realtime/integration/test_room_event_handler.py`
- **test_subscribe_to_events()** (3 connections) — `server/tests/unit/realtime/integration/test_room_event_handler.py`
- *... and 24 more nodes in this community*

## Relationships

- [Event Bus & Persistence Core](Event_Bus_&_Persistence_Core.md) (7 shared connections)
- [Community 41](Community_41.md) (3 shared connections)
- [Community 220](Community_220.md) (1 shared connections)
- [Community 155](Community_155.md) (1 shared connections)

## Source Files

- `server/realtime/event_handlers.py`
- `server/realtime/integration/__init__.py`
- `server/realtime/integration/room_event_handler.py`
- `server/tests/unit/realtime/integration/test_room_event_handler.py`

## Audit Trail

- EXTRACTED: 83 (89%)
- INFERRED: 10 (11%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*