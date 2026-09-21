# Any

> 7 nodes

## Key Concepts

- **Any** (10 connections)
- **broadcast_global_event_impl()** (6 connections) — `server/realtime/connection_helpers.py`
- **broadcast_room_event_impl()** (6 connections) — `server/realtime/connection_helpers.py`
- **test_broadcast_global_event_impl()** (4 connections) — `server/tests/unit/realtime/test_connection_helpers_impl.py`
- **Broadcast a room-specific event to all players in the room.** (1 connections) — `server/realtime/connection_helpers.py`
- **Broadcast a global event to all connected players.** (1 connections) — `server/realtime/connection_helpers.py`
- **Test broadcast_global_event_impl() broadcasts global event.** (1 connections) — `server/tests/unit/realtime/test_connection_helpers_impl.py`

## Relationships

- [test_connection_helpers_impl.py](test_connection_helpers_impl.py.md) (4 shared connections)
- [asyncio](asyncio.md) (3 shared connections)
- [build_event](build_event.md) (2 shared connections)
- [get_logger](get_logger.md) (2 shared connections)
- [send_personal_message_old_impl](send_personal_message_old_impl.md) (2 shared connections)
- [_optimize_payload](_optimize_payload.md) (1 shared connections)
- [handle_new_login_impl](handle_new_login_impl.md) (1 shared connections)
- [mark_player_seen_impl](mark_player_seen_impl.md) (1 shared connections)
- [convert_uuids_to_strings](convert_uuids_to_strings.md) (1 shared connections)

## Source Files

- `server/realtime/connection_helpers.py`
- `server/tests/unit/realtime/test_connection_helpers_impl.py`

## Audit Trail

- EXTRACTED: 23 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*