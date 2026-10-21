# NATSError

> 42 nodes · cohesion 0.08

## Key Concepts

- **RoomEventHandler** (27 connections) — `server/realtime/integration/room_event_handler.py`
- **test_room_event_handler.py** (15 connections) — `server/tests/unit/realtime/integration/test_room_event_handler.py`
- **room_event_handler.py** (13 connections) — `server/realtime/integration/room_event_handler.py`
- **asyncio** (11 connections)
- **._broadcast_room_occupants_update()** (8 connections) — `server/realtime/integration/room_event_handler.py`
- **Any** (4 connections)
- **._extract_valid_occupant_names()** (4 connections) — `server/realtime/integration/room_event_handler.py`
- **.handle_player_entered_room()** (4 connections) — `server/realtime/integration/room_event_handler.py`
- **.handle_player_left_room()** (4 connections) — `server/realtime/integration/room_event_handler.py`
- **.__init__()** (4 connections) — `server/realtime/integration/room_event_handler.py`
- **test_handle_player_entered_room_occupant_lookup_error_is_caught()** (4 connections) — `server/tests/unit/realtime/integration/test_room_event_handler.py`
- **test_handle_player_left_room_missing_room_id()** (4 connections) — `server/tests/unit/realtime/integration/test_room_event_handler.py`
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
- **UUID** (2 connections)
- *... and 17 more nodes in this community*

## Relationships

- [test_container_persistence_async_helpers.py](test_container_persistence_async_helpers.py.md) (4 shared connections)
- [test_container_helpers_inventory_find.py](test_container_helpers_inventory_find.py.md) (2 shared connections)
- [.publish_with_pool](publish_with_pool.md) (2 shared connections)
- [Room](Room.md) (2 shared connections)
- [BaseEvent](BaseEvent.md) (2 shared connections)
- [_find_item_in_inventory](_find_item_in_inventory.md) (1 shared connections)

## Source Files

- `server/realtime/integration/room_event_handler.py`
- `server/tests/unit/realtime/integration/test_room_event_handler.py`

## Audit Trail

- EXTRACTED: 77 (90%)
- INFERRED: 9 (10%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*