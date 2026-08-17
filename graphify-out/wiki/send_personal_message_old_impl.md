# send_personal_message_old_impl

> 17 nodes

## Key Concepts

- **send_personal_message_old_impl()** (12 connections) — `server/realtime/connection_helpers.py`
- **Any** (10 connections)
- **broadcast_global_event_impl()** (6 connections) — `server/realtime/connection_helpers.py`
- **_queue_message_if_needed()** (6 connections) — `server/realtime/connection_helpers.py`
- **.send_personal_message_old()** (4 connections) — `server/realtime/connection_manager.py`
- **test_broadcast_global_event_impl()** (4 connections) — `server/tests/unit/realtime/test_connection_helpers_impl.py`
- **test_send_personal_message_old_impl()** (4 connections) — `server/tests/unit/realtime/test_connection_helpers_impl.py`
- **test_send_personal_message_old_impl_no_connections()** (4 connections) — `server/tests/unit/realtime/test_connection_helpers_impl.py`
- **test_queue_message_if_needed()** (3 connections) — `server/tests/unit/realtime/test_connection_helpers_impl.py`
- **Queue message for later delivery if no active connections. Args: player_id: The…** (1 connections) — `server/realtime/connection_helpers.py`
- **Send a personal message to a player via WebSocket (deprecated implementation).…** (1 connections) — `server/realtime/connection_helpers.py`
- **Broadcast a global event to all connected players.** (1 connections) — `server/realtime/connection_helpers.py`
- **Send a personal message to a player via WebSocket (deprecated).** (1 connections) — `server/realtime/connection_manager.py`
- **Test send_personal_message_old_impl() sends message.** (1 connections) — `server/tests/unit/realtime/test_connection_helpers_impl.py`
- **Test broadcast_global_event_impl() broadcasts global event.** (1 connections) — `server/tests/unit/realtime/test_connection_helpers_impl.py`
- **Test send_personal_message_old_impl() when no connections.** (1 connections) — `server/tests/unit/realtime/test_connection_helpers_impl.py`
- **Test _queue_message_if_needed() queues message.** (1 connections) — `server/tests/unit/realtime/test_connection_helpers_impl.py`

## Relationships

- [test_connection_helpers_impl.py](test_connection_helpers_impl.py.md) (13 shared connections)
- [get_logger](get_logger.md) (6 shared connections)
- [_optimize_payload](_optimize_payload.md) (2 shared connections)
- [_update_delivery_status](_update_delivery_status.md) (2 shared connections)
- [ConnectionManager](ConnectionManager.md) (2 shared connections)
- [build_event](build_event.md) (1 shared connections)
- [convert_uuids_to_strings](convert_uuids_to_strings.md) (1 shared connections)

## Source Files

- `server/realtime/connection_helpers.py`
- `server/realtime/connection_manager.py`
- `server/tests/unit/realtime/test_connection_helpers_impl.py`

## Audit Trail

- EXTRACTED: 44 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*