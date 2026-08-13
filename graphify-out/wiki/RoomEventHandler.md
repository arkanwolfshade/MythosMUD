# RoomEventHandler

> 9 nodes

## Key Concepts

- **RoomEventHandler** (10 connections) — `server/realtime/integration/room_event_handler.py`
- **.__init__()** (4 connections) — `server/realtime/integration/room_event_handler.py`
- **.subscribe_to_events()** (2 connections) — `server/realtime/integration/room_event_handler.py`
- **.unsubscribe_from_events()** (2 connections) — `server/realtime/integration/room_event_handler.py`
- **UUID** (2 connections)
- **Handles room movement events and broadcasts occupant updates. This class…** (1 connections) — `server/realtime/integration/room_event_handler.py`
- **Initialize the room event handler. Args: room_manager: RoomSubscriptionManager…** (1 connections) — `server/realtime/integration/room_event_handler.py`
- **Subscribe to room movement events for occupant broadcasting.** (1 connections) — `server/realtime/integration/room_event_handler.py`
- **Unsubscribe from room movement events.** (1 connections) — `server/realtime/integration/room_event_handler.py`

## Relationships

- [get_logger](get_logger.md) (3 shared connections)
- [build_event](build_event.md) (3 shared connections)
- [test_connection_initialization.py](test_connection_initialization.py.md) (1 shared connections)
- [is_player_in_login_grace_period](is_player_in_login_grace_period.md) (1 shared connections)

## Source Files

- `server/realtime/integration/room_event_handler.py`

## Audit Trail

- EXTRACTED: 16 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*