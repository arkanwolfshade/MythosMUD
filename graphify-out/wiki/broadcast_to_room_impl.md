# broadcast_to_room_impl

> 6 nodes

## Key Concepts

- **broadcast_to_room_impl()** (7 connections) — `server/realtime/connection_manager_methods.py`
- **broadcast_room_event_impl()** (6 connections) — `server/realtime/connection_manager_methods.py`
- **test_broadcast_room_event_impl()** (3 connections) — `server/tests/unit/realtime/test_connection_manager_methods.py`
- **test_broadcast_to_room_impl()** (3 connections) — `server/tests/unit/realtime/test_connection_manager_methods.py`
- **Broadcast a message to all players in a room.** (1 connections) — `server/realtime/connection_manager_methods.py`
- **Broadcast a room-specific event to all players in the room.** (1 connections) — `server/realtime/connection_manager_methods.py`

## Relationships

- [ConnectionManager](ConnectionManager.md) (3 shared connections)
- [connection_manager.py](connection_manager.py.md) (3 shared connections)
- [asyncio](asyncio.md) (2 shared connections)
- [test_connection_manager_methods.py](test_connection_manager_methods.py.md) (2 shared connections)
- [build_event](build_event.md) (1 shared connections)

## Source Files

- `server/realtime/connection_manager_methods.py`
- `server/tests/unit/realtime/test_connection_manager_methods.py`

## Audit Trail

- EXTRACTED: 16 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*