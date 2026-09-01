# test_connection_helpers_impl.py

> 30 nodes

## Key Concepts

- **test_connection_helpers_impl.py** (38 connections) — `server/tests/unit/realtime/test_connection_helpers_impl.py`
- **send_personal_message_old_impl()** (12 connections) — `server/realtime/connection_helpers.py`
- **Any** (10 connections)
- **_update_delivery_status()** (8 connections) — `server/realtime/connection_helpers.py`
- **broadcast_global_event_impl()** (6 connections) — `server/realtime/connection_helpers.py`
- **broadcast_room_event_impl()** (6 connections) — `server/realtime/connection_helpers.py`
- **_queue_message_if_needed()** (6 connections) — `server/realtime/connection_helpers.py`
- **test_broadcast_room_event_impl()** (4 connections) — `server/tests/unit/realtime/test_connection_helpers_impl.py`
- **test_send_personal_message_old_impl()** (4 connections) — `server/tests/unit/realtime/test_connection_helpers_impl.py`
- **test_send_personal_message_old_impl_no_connections()** (4 connections) — `server/tests/unit/realtime/test_connection_helpers_impl.py`
- **mock_manager()** (3 connections) — `server/tests/unit/realtime/test_connection_helpers_impl.py`
- **test_queue_message_if_needed()** (3 connections) — `server/tests/unit/realtime/test_connection_helpers_impl.py`
- **test_update_delivery_status_failed()** (3 connections) — `server/tests/unit/realtime/test_connection_helpers_impl.py`
- **test_update_delivery_status_no_attempts()** (3 connections) — `server/tests/unit/realtime/test_connection_helpers_impl.py`
- **test_update_delivery_status_success()** (3 connections) — `server/tests/unit/realtime/test_connection_helpers_impl.py`
- **fixture** (1 connections)
- **Queue message for later delivery if no active connections. Args: player_id: The…** (1 connections) — `server/realtime/connection_helpers.py`
- **Update final delivery status based on connection results. Args:…** (1 connections) — `server/realtime/connection_helpers.py`
- **Send a personal message to a player via WebSocket (deprecated implementation).…** (1 connections) — `server/realtime/connection_helpers.py`
- **Broadcast a room-specific event to all players in the room.** (1 connections) — `server/realtime/connection_helpers.py`
- **Broadcast a global event to all connected players.** (1 connections) — `server/realtime/connection_helpers.py`
- **Unit tests for connection helpers implementation functions. Tests the…** (1 connections) — `server/tests/unit/realtime/test_connection_helpers_impl.py`
- **Test send_personal_message_old_impl() sends message.** (1 connections) — `server/tests/unit/realtime/test_connection_helpers_impl.py`
- **Test broadcast_room_event_impl() broadcasts room event.** (1 connections) — `server/tests/unit/realtime/test_connection_helpers_impl.py`
- **Test _update_delivery_status() when no connection attempts.** (1 connections) — `server/tests/unit/realtime/test_connection_helpers_impl.py`
- *... and 5 more nodes in this community*

## Relationships

- [asyncio](asyncio.md) (14 shared connections)
- [get_logger](get_logger.md) (6 shared connections)
- [_optimize_payload](_optimize_payload.md) (6 shared connections)
- [convert_uuids_to_strings](convert_uuids_to_strings.md) (6 shared connections)
- [handle_new_login_impl](handle_new_login_impl.md) (4 shared connections)
- [mark_player_seen_impl](mark_player_seen_impl.md) (3 shared connections)
- [build_event](build_event.md) (2 shared connections)
- [ConnectionManager](ConnectionManager.md) (1 shared connections)
- [connection_manager.py](connection_manager.py.md) (1 shared connections)
- [pytest.md](pytest.md.md) (1 shared connections)

## Source Files

- `server/realtime/connection_helpers.py`
- `server/tests/unit/realtime/test_connection_helpers_impl.py`

## Audit Trail

- EXTRACTED: 86 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*