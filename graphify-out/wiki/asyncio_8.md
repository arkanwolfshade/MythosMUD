# asyncio

> 17 nodes

## Key Concepts

- **asyncio** (12 connections)
- **_send_to_websockets()** (11 connections) — `server/realtime/connection_helpers.py`
- **test_send_to_websockets_websocket_error()** (5 connections) — `server/tests/unit/realtime/test_connection_helpers_impl.py`
- **test_broadcast_global_event_impl()** (4 connections) — `server/tests/unit/realtime/test_connection_helpers_impl.py`
- **test_send_to_websockets()** (4 connections) — `server/tests/unit/realtime/test_connection_helpers_impl.py`
- **test_send_to_websockets_inactive_connection()** (4 connections) — `server/tests/unit/realtime/test_connection_helpers_impl.py`
- **test_send_to_websockets_no_connections()** (4 connections) — `server/tests/unit/realtime/test_connection_helpers_impl.py`
- **test_send_to_websockets_none_websocket()** (4 connections) — `server/tests/unit/realtime/test_connection_helpers_impl.py`
- **test_send_to_websockets_skips_disconnected_client_state()** (4 connections) — `server/tests/unit/realtime/test_connection_helpers_impl.py`
- **Send event to all active websockets for a player. Args: player_id: The player's…** (1 connections) — `server/realtime/connection_helpers.py`
- **Test broadcast_global_event_impl() broadcasts global event.** (1 connections) — `server/tests/unit/realtime/test_connection_helpers_impl.py`
- **Test _send_to_websockets() handles websocket errors.** (1 connections) — `server/tests/unit/realtime/test_connection_helpers_impl.py`
- **Test _send_to_websockets() handles None websocket.** (1 connections) — `server/tests/unit/realtime/test_connection_helpers_impl.py`
- **Test _send_to_websockets() skips inactive connections.** (1 connections) — `server/tests/unit/realtime/test_connection_helpers_impl.py`
- **Do not send on sockets whose client_state is not CONNECTED.** (1 connections) — `server/tests/unit/realtime/test_connection_helpers_impl.py`
- **Test _send_to_websockets() sends to websockets.** (1 connections) — `server/tests/unit/realtime/test_connection_helpers_impl.py`
- **Test _send_to_websockets() returns False when no connections.** (1 connections) — `server/tests/unit/realtime/test_connection_helpers_impl.py`

## Relationships

- [test_connection_helpers_impl.py](test_connection_helpers_impl.py.md) (14 shared connections)
- [handle_new_login_impl](handle_new_login_impl.md) (2 shared connections)
- [get_logger](get_logger.md) (1 shared connections)
- [AttributeError](AttributeError.md) (1 shared connections)

## Source Files

- `server/realtime/connection_helpers.py`
- `server/tests/unit/realtime/test_connection_helpers_impl.py`

## Audit Trail

- EXTRACTED: 38 (97%)
- INFERRED: 1 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*