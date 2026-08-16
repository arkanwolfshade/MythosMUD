# test_connection_helpers_impl.py

> 26 nodes

## Key Concepts

- **test_connection_helpers_impl.py** (38 connections) — `server/tests/unit/realtime/test_connection_helpers_impl.py`
- **asyncio** (12 connections)
- **_send_to_websockets()** (11 connections) — `server/realtime/connection_helpers.py`
- **test_send_to_websockets_websocket_error()** (5 connections) — `server/tests/unit/realtime/test_connection_helpers_impl.py`
- **test_broadcast_global_event_impl()** (4 connections) — `server/tests/unit/realtime/test_connection_helpers_impl.py`
- **test_broadcast_room_event_impl()** (4 connections) — `server/tests/unit/realtime/test_connection_helpers_impl.py`
- **test_send_personal_message_old_impl_no_connections()** (4 connections) — `server/tests/unit/realtime/test_connection_helpers_impl.py`
- **test_send_to_websockets()** (4 connections) — `server/tests/unit/realtime/test_connection_helpers_impl.py`
- **test_send_to_websockets_inactive_connection()** (4 connections) — `server/tests/unit/realtime/test_connection_helpers_impl.py`
- **test_send_to_websockets_no_connections()** (4 connections) — `server/tests/unit/realtime/test_connection_helpers_impl.py`
- **test_send_to_websockets_none_websocket()** (4 connections) — `server/tests/unit/realtime/test_connection_helpers_impl.py`
- **test_send_to_websockets_skips_disconnected_client_state()** (4 connections) — `server/tests/unit/realtime/test_connection_helpers_impl.py`
- **mock_manager()** (3 connections) — `server/tests/unit/realtime/test_connection_helpers_impl.py`
- **fixture** (1 connections)
- **Send event to all active websockets for a player. Args: player_id: The player's…** (1 connections) — `server/realtime/connection_helpers.py`
- **Unit tests for connection helpers implementation functions. Tests the…** (1 connections) — `server/tests/unit/realtime/test_connection_helpers_impl.py`
- **Test broadcast_room_event_impl() broadcasts room event.** (1 connections) — `server/tests/unit/realtime/test_connection_helpers_impl.py`
- **Test broadcast_global_event_impl() broadcasts global event.** (1 connections) — `server/tests/unit/realtime/test_connection_helpers_impl.py`
- **Test _send_to_websockets() handles websocket errors.** (1 connections) — `server/tests/unit/realtime/test_connection_helpers_impl.py`
- **Test _send_to_websockets() handles None websocket.** (1 connections) — `server/tests/unit/realtime/test_connection_helpers_impl.py`
- **Test _send_to_websockets() skips inactive connections.** (1 connections) — `server/tests/unit/realtime/test_connection_helpers_impl.py`
- **Do not send on sockets whose client_state is not CONNECTED.** (1 connections) — `server/tests/unit/realtime/test_connection_helpers_impl.py`
- **Create a mock connection manager.** (1 connections) — `server/tests/unit/realtime/test_connection_helpers_impl.py`
- **Test send_personal_message_old_impl() when no connections.** (1 connections) — `server/tests/unit/realtime/test_connection_helpers_impl.py`
- **Test _send_to_websockets() sends to websockets.** (1 connections) — `server/tests/unit/realtime/test_connection_helpers_impl.py`
- *... and 1 more nodes in this community*

## Relationships

- [connection_helpers.py](connection_helpers.py.md) (16 shared connections)
- [handle_new_login_impl](handle_new_login_impl.md) (5 shared connections)
- [convert_uuids_to_strings](convert_uuids_to_strings.md) (5 shared connections)
- [_optimize_payload](_optimize_payload.md) (4 shared connections)
- [_update_delivery_status](_update_delivery_status.md) (4 shared connections)
- [build_event](build_event.md) (1 shared connections)
- [pytest.md](pytest.md.md) (1 shared connections)

## Source Files

- `server/realtime/connection_helpers.py`
- `server/tests/unit/realtime/test_connection_helpers_impl.py`

## Audit Trail

- EXTRACTED: 74 (99%)
- INFERRED: 1 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*