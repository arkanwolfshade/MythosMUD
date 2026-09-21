# RoomEventHandler

> 40 nodes

## Key Concepts

- **RoomEventHandler** (27 connections) — `server/realtime/integration/room_event_handler.py`
- **test_room_event_handler.py** (15 connections) — `server/tests/unit/realtime/integration/test_room_event_handler.py`
- **asyncio** (11 connections)
- **._broadcast_room_occupants_update()** (8 connections) — `server/realtime/integration/room_event_handler.py`
- **._extract_valid_occupant_names()** (4 connections) — `server/realtime/integration/room_event_handler.py`
- **.handle_player_entered_room()** (4 connections) — `server/realtime/integration/room_event_handler.py`
- **.handle_player_left_room()** (4 connections) — `server/realtime/integration/room_event_handler.py`
- **.__init__()** (4 connections) — `server/realtime/integration/room_event_handler.py`
- **test_handle_player_entered_room_occupant_lookup_error_is_caught()** (4 connections) — `server/tests/unit/realtime/integration/test_room_event_handler.py`
- **test_handle_player_left_room_missing_room_id()** (4 connections) — `server/tests/unit/realtime/integration/test_room_event_handler.py`
- **Any** (4 connections)
- **._looks_like_uuid()** (3 connections) — `server/realtime/integration/room_event_handler.py`
- **._publish_room_movement_nats_event()** (3 connections) — `server/realtime/integration/room_event_handler.py`
- **room_handler()** (3 connections) — `server/tests/unit/realtime/integration/test_room_event_handler.py`
- **test_handle_player_entered_nats_publish_failure()** (3 connections) — `server/tests/unit/realtime/integration/test_room_event_handler.py`
- **test_handle_player_entered_room_broadcasts()** (3 connections) — `server/tests/unit/realtime/integration/test_room_event_handler.py`
- **test_handle_player_entered_room_missing_room_id()** (3 connections) — `server/tests/unit/realtime/integration/test_room_event_handler.py`
- **test_handle_player_entered_skips_uuid_player_names()** (3 connections) — `server/tests/unit/realtime/integration/test_room_event_handler.py`
- **test_handle_player_left_room_broadcasts()** (3 connections) — `server/tests/unit/realtime/integration/test_room_event_handler.py`
- **test_subscribe_handles_exception()** (3 connections) — `server/tests/unit/realtime/integration/test_room_event_handler.py`
- **test_subscribe_to_events()** (3 connections) — `server/tests/unit/realtime/integration/test_room_event_handler.py`
- **test_subscribe_to_events_no_bus()** (3 connections) — `server/tests/unit/realtime/integration/test_room_event_handler.py`
- **test_unsubscribe_from_events()** (3 connections) — `server/tests/unit/realtime/integration/test_room_event_handler.py`
- **.subscribe_to_events()** (2 connections) — `server/realtime/integration/room_event_handler.py`
- **.unsubscribe_from_events()** (2 connections) — `server/realtime/integration/room_event_handler.py`
- *... and 15 more nodes in this community*

## Relationships

- [connection_manager.py](connection_manager.py.md) (5 shared connections)
- [GameStateProvider](GameStateProvider.md) (1 shared connections)
- [build_event](build_event.md) (1 shared connections)

## Source Files

- `server/realtime/integration/room_event_handler.py`
- `server/tests/unit/realtime/integration/test_room_event_handler.py`

## Audit Trail

- EXTRACTED: 67 (88%)
- INFERRED: 9 (12%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*