# RoomEventHandler

> 28 nodes

## Key Concepts

- **RoomEventHandler** (21 connections) — `server/realtime/integration/room_event_handler.py`
- **test_room_event_handler.py** (13 connections) — `server/tests/unit/realtime/integration/test_room_event_handler.py`
- **asyncio** (9 connections)
- **.handle_player_entered_room()** (4 connections) — `server/realtime/integration/room_event_handler.py`
- **.handle_player_left_room()** (4 connections) — `server/realtime/integration/room_event_handler.py`
- **.__init__()** (4 connections) — `server/realtime/integration/room_event_handler.py`
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
- **Any** (3 connections)
- **.subscribe_to_events()** (2 connections) — `server/realtime/integration/room_event_handler.py`
- **.unsubscribe_from_events()** (2 connections) — `server/realtime/integration/room_event_handler.py`
- **UUID** (2 connections)
- **fixture** (1 connections)
- **Handle PlayerEnteredRoom events by broadcasting updated occupant count.** (1 connections) — `server/realtime/integration/room_event_handler.py`
- **Handle PlayerLeftRoom events by broadcasting updated occupant count.** (1 connections) — `server/realtime/integration/room_event_handler.py`
- **Handles room movement events and broadcasts occupant updates. This class…** (1 connections) — `server/realtime/integration/room_event_handler.py`
- **Initialize the room event handler. Args: room_manager: RoomSubscriptionManager…** (1 connections) — `server/realtime/integration/room_event_handler.py`
- *... and 3 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (5 shared connections)
- [build_event](build_event.md) (2 shared connections)
- [HealthMonitor](HealthMonitor.md) (1 shared connections)

## Source Files

- `server/realtime/integration/room_event_handler.py`
- `server/tests/unit/realtime/integration/test_room_event_handler.py`

## Audit Trail

- EXTRACTED: 45 (82%)
- INFERRED: 10 (18%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*