# server realtime connection helpers rationale

> 21 nodes

## Key Concepts

- **asyncio** (12 connections)
- **_send_to_websockets()** (11 connections) — `server/realtime/connection_helpers.py`
- **test_send_to_websockets_websocket_error()** (5 connections) — `server/tests/unit/realtime/test_connection_helpers_impl.py`
- **test_broadcast_room_event_impl()** (4 connections) — `server/tests/unit/realtime/test_connection_helpers_impl.py`
- **test_send_personal_message_old_impl()** (4 connections) — `server/tests/unit/realtime/test_connection_helpers_impl.py`
- **test_send_personal_message_old_impl_no_connections()** (4 connections) — `server/tests/unit/realtime/test_connection_helpers_impl.py`
- **test_send_to_websockets()** (4 connections) — `server/tests/unit/realtime/test_connection_helpers_impl.py`
- **test_send_to_websockets_inactive_connection()** (4 connections) — `server/tests/unit/realtime/test_connection_helpers_impl.py`
- **test_send_to_websockets_no_connections()** (4 connections) — `server/tests/unit/realtime/test_connection_helpers_impl.py`
- **test_send_to_websockets_none_websocket()** (4 connections) — `server/tests/unit/realtime/test_connection_helpers_impl.py`
- **test_send_to_websockets_skips_disconnected_client_state()** (4 connections) — `server/tests/unit/realtime/test_connection_helpers_impl.py`
- **Send event to all active websockets for a player. Args: player_id: The player's…** (1 connections) — `server/realtime/connection_helpers.py`
- **Test send_personal_message_old_impl() sends message.** (1 connections) — `server/tests/unit/realtime/test_connection_helpers_impl.py`
- **Test broadcast_room_event_impl() broadcasts room event.** (1 connections) — `server/tests/unit/realtime/test_connection_helpers_impl.py`
- **Test _send_to_websockets() handles websocket errors.** (1 connections) — `server/tests/unit/realtime/test_connection_helpers_impl.py`
- **Test _send_to_websockets() handles None websocket.** (1 connections) — `server/tests/unit/realtime/test_connection_helpers_impl.py`
- **Test _send_to_websockets() skips inactive connections.** (1 connections) — `server/tests/unit/realtime/test_connection_helpers_impl.py`
- **Do not send on sockets whose client_state is not CONNECTED.** (1 connections) — `server/tests/unit/realtime/test_connection_helpers_impl.py`
- **Test send_personal_message_old_impl() when no connections.** (1 connections) — `server/tests/unit/realtime/test_connection_helpers_impl.py`
- **Test _send_to_websockets() sends to websockets.** (1 connections) — `server/tests/unit/realtime/test_connection_helpers_impl.py`
- **Test _send_to_websockets() returns False when no connections.** (1 connections) — `server/tests/unit/realtime/test_connection_helpers_impl.py`

## Relationships

- [server realtime connection helpers convert](server_realtime_connection_helpers_convert.md) (10 shared connections)
- [server realtime connection helpers](server_realtime_connection_helpers.md) (7 shared connections)
- [server realtime connection helpers handle](server_realtime_connection_helpers_handle.md) (2 shared connections)
- [attributeerror](attributeerror.md) (1 shared connections)

## Source Files

- `server/realtime/connection_helpers.py`
- `server/tests/unit/realtime/test_connection_helpers_impl.py`

## Audit Trail

- EXTRACTED: 44 (98%)
- INFERRED: 1 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*