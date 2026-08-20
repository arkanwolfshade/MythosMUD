# RoomEventHandler

> 32 nodes

## Key Concepts

- **RoomEventHandler** (21 connections) — `server/realtime/integration/room_event_handler.py`
- **test_room_event_handler.py** (14 connections) — `server/tests/unit/realtime/integration/test_room_event_handler.py`
- **room_event_handler.py** (13 connections) — `server/realtime/integration/room_event_handler.py`
- **asyncio** (9 connections)
- **server/realtime/integration/__init__.py** (5 connections) — `server/realtime/integration/__init__.py`
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
- **Integration components for connection management. This package provides…** (1 connections) — `server/realtime/integration/__init__.py`
- **Room event handling for connection management. This module provides integration…** (1 connections) — `server/realtime/integration/room_event_handler.py`
- *... and 7 more nodes in this community*

## Relationships

- [connection_manager.py](connection_manager.py.md) (3 shared connections)
- [build_event](build_event.md) (3 shared connections)
- [test_game_state_provider.py](test_game_state_provider.py.md) (2 shared connections)
- [get_logger](get_logger.md) (2 shared connections)
- [RoomSubscriptionManager](RoomSubscriptionManager.md) (2 shared connections)
- [PlayerEnteredRoom](PlayerEnteredRoom.md) (2 shared connections)
- [pytest.md](pytest.md.md) (1 shared connections)

## Source Files

- `server/realtime/integration/__init__.py`
- `server/realtime/integration/room_event_handler.py`
- `server/tests/unit/realtime/integration/test_room_event_handler.py`

## Audit Trail

- EXTRACTED: 62 (90%)
- INFERRED: 7 (10%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*