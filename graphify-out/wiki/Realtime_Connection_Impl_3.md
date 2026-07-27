# Realtime Connection Impl

> 11 nodes · cohesion 0.20

## Key Concepts

- **_send_to_websockets()** (10 connections) — `server/realtime/connection_helpers.py`
- **test_send_to_websockets_websocket_error()** (4 connections) — `server/tests/unit/realtime/test_connection_helpers_impl.py`
- **test_send_to_websockets()** (3 connections) — `server/tests/unit/realtime/test_connection_helpers_impl.py`
- **test_send_to_websockets_inactive_connection()** (3 connections) — `server/tests/unit/realtime/test_connection_helpers_impl.py`
- **test_send_to_websockets_no_connections()** (3 connections) — `server/tests/unit/realtime/test_connection_helpers_impl.py`
- **test_send_to_websockets_none_websocket()** (3 connections) — `server/tests/unit/realtime/test_connection_helpers_impl.py`
- **Test _send_to_websockets() handles websocket errors.** (2 connections) — `server/tests/unit/realtime/test_connection_helpers_impl.py`
- **Send event to all active websockets for a player.      Args:         player_id:** (1 connections) — `server/realtime/connection_helpers.py`
- **Test _send_to_websockets() skips inactive connections.** (1 connections) — `server/tests/unit/realtime/test_connection_helpers_impl.py`
- **Test _send_to_websockets() sends to websockets.** (1 connections) — `server/tests/unit/realtime/test_connection_helpers_impl.py`
- **Test _send_to_websockets() returns False when no connections.** (1 connections) — `server/tests/unit/realtime/test_connection_helpers_impl.py`

## Relationships

- [[Realtime Connection Impl]] (9 shared connections)
- [[Services Service Room]] (1 shared connections)

## Source Files

- `server/realtime/connection_helpers.py`
- `server/tests/unit/realtime/test_connection_helpers_impl.py`

## Audit Trail

- EXTRACTED: 31 (97%)
- INFERRED: 1 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
