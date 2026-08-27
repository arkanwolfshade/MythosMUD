# _parse_env_list

> 15 nodes

## Key Concepts

- **connection_websocket_close.py** (9 connections) — `server/realtime/connection_websocket_close.py`
- **safe_close_websocket_impl()** (8 connections) — `server/realtime/connection_websocket_close.py`
- **_CloseableWebSocketManager** (5 connections) — `server/realtime/connection_websocket_close.py`
- **is_websocket_open_impl()** (5 connections) — `server/realtime/connection_websocket_close.py`
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

- [test_message_handler_factory.py](test_message_handler_factory.py.md) (3 shared connections)
- [roomHandlers.ts](roomHandlers.ts.md) (2 shared connections)
- [generate_invites_db.py](generate_invites_db.py.md) (2 shared connections)
- [test_chat_logger.py](test_chat_logger.py.md) (1 shared connections)
- [NPCDefinition](NPCDefinition.md) (1 shared connections)
- [FeatureFlagService](FeatureFlagService.md) (1 shared connections)

## Source Files

- `server/realtime/connection_websocket_close.py`
- `server/tests/unit/realtime/test_connection_manager_methods.py`

## Audit Trail

- EXTRACTED: 27 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*