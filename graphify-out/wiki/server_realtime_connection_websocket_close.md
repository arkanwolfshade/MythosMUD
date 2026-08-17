# server realtime connection websocket close

> 15 nodes

## Key Concepts

- **safe_close_websocket_impl()** (13 connections) — `server/realtime/connection_websocket_close.py`
- **connection_websocket_close.py** (9 connections) — `server/realtime/connection_websocket_close.py`
- **is_websocket_open_impl()** (7 connections) — `server/realtime/connection_websocket_close.py`
- **_CloseableWebSocketManager** (5 connections) — `server/realtime/connection_websocket_close.py`
- **test_safe_close_websocket_impl()** (3 connections) — `server/tests/unit/realtime/test_connection_manager_methods.py`
- **.is_websocket_closed()** (2 connections) — `server/realtime/connection_websocket_close.py`
- **.mark_websocket_closed()** (2 connections) — `server/realtime/connection_websocket_close.py`
- **test_is_websocket_open_impl()** (2 connections) — `server/tests/unit/realtime/test_connection_manager_methods.py`
- **WebSocket** (2 connections)
- **Protocol** (1 connections)
- **Safe WebSocket close helpers for connection management. Leaf module: no imports…** (1 connections) — `server/realtime/connection_websocket_close.py`
- **Return True if this WebSocket id was already marked closed.** (1 connections) — `server/realtime/connection_websocket_close.py`
- **Record that this WebSocket id has been closed.** (1 connections) — `server/realtime/connection_websocket_close.py`
- **Check if a WebSocket is open.** (1 connections) — `server/realtime/connection_websocket_close.py`
- **Safely close a WebSocket connection.** (1 connections) — `server/realtime/connection_websocket_close.py`

## Relationships

- [claude rules asyncio](claude_rules_asyncio.md) (4 shared connections)
- [server realtime connection disconnection](server_realtime_connection_disconnection.md) (4 shared connections)
- [server realtime connection manager methods](server_realtime_connection_manager_methods.md) (4 shared connections)
- [server realtime connection manager connectionmanager](server_realtime_connection_manager_connectionmanager.md) (2 shared connections)
- [server realtime connection disconnection cleanup](server_realtime_connection_disconnection_cleanup.md) (2 shared connections)
- [claude rules fastapi](claude_rules_fastapi.md) (1 shared connections)

## Source Files

- `server/realtime/connection_websocket_close.py`
- `server/tests/unit/realtime/test_connection_manager_methods.py`

## Audit Trail

- EXTRACTED: 34 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*