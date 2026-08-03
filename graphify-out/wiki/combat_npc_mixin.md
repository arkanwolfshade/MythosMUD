# combat npc mixin

> 16 nodes

## Key Concepts

- **cleanup_dead_websocket_impl()** (14 connections) — `server/realtime/connection_delegates.py`
- **_WebsocketCleanupManager** (7 connections) — `server/realtime/connection_delegates.py`
- **_remove_connection_from_player_list()** (5 connections) — `server/realtime/connection_delegates.py`
- **test_cleanup_dead_websocket_impl_success()** (3 connections) — `server/tests/unit/realtime/test_connection_delegates.py`
- **test_cleanup_dead_websocket_impl_none_websocket()** (3 connections) — `server/tests/unit/realtime/test_connection_delegates.py`
- **test_cleanup_dead_websocket_impl_not_in_active()** (3 connections) — `server/tests/unit/realtime/test_connection_delegates.py`
- **test_cleanup_dead_websocket_impl_close_timeout()** (3 connections) — `server/tests/unit/realtime/test_connection_delegates.py`
- **test_cleanup_dead_websocket_impl_error()** (3 connections) — `server/tests/unit/realtime/test_connection_delegates.py`
- **ConnectionManager surface used by cleanup_dead_websocket_impl.** (1 connections) — `server/realtime/connection_delegates.py`
- **Drop connection_id from player_websockets; delete empty player entries.** (1 connections) — `server/realtime/connection_delegates.py`
- **Clean up a dead WebSocket connection.      Args:         player_id: The player's** (1 connections) — `server/realtime/connection_delegates.py`
- **Test cleanup_dead_websocket_impl() successfully cleans up websocket.** (1 connections) — `server/tests/unit/realtime/test_connection_delegates.py`
- **Test cleanup_dead_websocket_impl() handles None websocket.** (1 connections) — `server/tests/unit/realtime/test_connection_delegates.py`
- **Test cleanup_dead_websocket_impl() handles websocket not in active_websockets.** (1 connections) — `server/tests/unit/realtime/test_connection_delegates.py`
- **Test cleanup_dead_websocket_impl() handles close timeout.** (1 connections) — `server/tests/unit/realtime/test_connection_delegates.py`
- **Test cleanup_dead_websocket_impl() handles errors.** (1 connections) — `server/tests/unit/realtime/test_connection_delegates.py`

## Relationships

- [connection realtime delegates](connection_realtime_delegates.md) (12 shared connections)
- [Room Broadcast](Room_Broadcast.md) (4 shared connections)
- [persistence container rationale](persistence_container_rationale.md) (1 shared connections)

## Source Files

- `server/realtime/connection_delegates.py`
- `server/tests/unit/realtime/test_connection_delegates.py`

## Audit Trail

- EXTRACTED: 47 (96%)
- INFERRED: 2 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*