# test_connection_helpers_impl.py

> 30 nodes

## Key Concepts

- **test_connection_helpers_impl.py** (38 connections) — `server/tests/unit/realtime/test_connection_helpers_impl.py`
- **asyncio** (12 connections)
- **_send_to_websockets()** (11 connections) — `server/realtime/connection_helpers.py`
- **broadcast_room_event_impl()** (6 connections) — `server/realtime/connection_helpers.py`
- **test_send_to_websockets_websocket_error()** (5 connections) — `server/tests/unit/realtime/test_connection_helpers_impl.py`
- **test_broadcast_room_event_impl()** (4 connections) — `server/tests/unit/realtime/test_connection_helpers_impl.py`
- **test_handle_new_login_impl()** (4 connections) — `server/tests/unit/realtime/test_connection_helpers_impl.py`
- **test_handle_new_login_impl_cancels_orphan_rest_countdown()** (4 connections) — `server/tests/unit/realtime/test_connection_helpers_impl.py`
- **test_send_to_websockets()** (4 connections) — `server/tests/unit/realtime/test_connection_helpers_impl.py`
- **test_send_to_websockets_inactive_connection()** (4 connections) — `server/tests/unit/realtime/test_connection_helpers_impl.py`
- **test_send_to_websockets_no_connections()** (4 connections) — `server/tests/unit/realtime/test_connection_helpers_impl.py`
- **test_send_to_websockets_none_websocket()** (4 connections) — `server/tests/unit/realtime/test_connection_helpers_impl.py`
- **test_send_to_websockets_skips_disconnected_client_state()** (4 connections) — `server/tests/unit/realtime/test_connection_helpers_impl.py`
- **mock_manager()** (3 connections) — `server/tests/unit/realtime/test_connection_helpers_impl.py`
- **test_mark_player_seen_impl()** (3 connections) — `server/tests/unit/realtime/test_connection_helpers_impl.py`
- **fixture** (1 connections)
- **Broadcast a room-specific event to all players in the room.** (1 connections) — `server/realtime/connection_helpers.py`
- **Send event to all active websockets for a player. Args: player_id: The player's…** (1 connections) — `server/realtime/connection_helpers.py`
- **Unit tests for connection helpers implementation functions. Tests the…** (1 connections) — `server/tests/unit/realtime/test_connection_helpers_impl.py`
- **Test handle_new_login_impl() handles new login.** (1 connections) — `server/tests/unit/realtime/test_connection_helpers_impl.py`
- **New login must cancel /rest countdown so it cannot kill the new session.** (1 connections) — `server/tests/unit/realtime/test_connection_helpers_impl.py`
- **Test broadcast_room_event_impl() broadcasts room event.** (1 connections) — `server/tests/unit/realtime/test_connection_helpers_impl.py`
- **Test mark_player_seen_impl() marks player as seen.** (1 connections) — `server/tests/unit/realtime/test_connection_helpers_impl.py`
- **Test _send_to_websockets() handles websocket errors.** (1 connections) — `server/tests/unit/realtime/test_connection_helpers_impl.py`
- **Test _send_to_websockets() handles None websocket.** (1 connections) — `server/tests/unit/realtime/test_connection_helpers_impl.py`
- *... and 5 more nodes in this community*

## Relationships

- [send_personal_message_old_impl](send_personal_message_old_impl.md) (13 shared connections)
- [get_logger](get_logger.md) (8 shared connections)
- [convert_uuids_to_strings](convert_uuids_to_strings.md) (5 shared connections)
- [_optimize_payload](_optimize_payload.md) (4 shared connections)
- [_update_delivery_status](_update_delivery_status.md) (4 shared connections)
- [build_event](build_event.md) (1 shared connections)
- [AttributeError](AttributeError.md) (1 shared connections)
- [pytest.md](pytest.md.md) (1 shared connections)

## Source Files

- `server/realtime/connection_helpers.py`
- `server/tests/unit/realtime/test_connection_helpers_impl.py`

## Audit Trail

- EXTRACTED: 80 (99%)
- INFERRED: 1 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*