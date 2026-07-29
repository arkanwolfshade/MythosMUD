# connection manager api

> 23 nodes

## Key Concepts

- **connection_manager_api.py** (15 connections) — `server/realtime/connection_manager_api.py`
- **broadcast_game_event()** (11 connections) — `server/realtime/connection_manager_api.py`
- **resolve_connection_manager()** (8 connections) — `server/realtime/connection_manager_utils.py`
- **_ConnectionManagerAPI** (7 connections) — `server/realtime/connection_manager_api.py`
- **_require_manager()** (7 connections) — `server/realtime/connection_manager_api.py`
- **send_room_event()** (7 connections) — `server/realtime/connection_manager_api.py`
- **connection_manager_utils.py** (7 connections) — `server/realtime/connection_manager_utils.py`
- **_ensure_async_compat()** (4 connections) — `server/realtime/connection_manager_utils.py`
- **_coerce_connection_manager()** (3 connections) — `server/realtime/connection_manager_utils.py`
- **_make_async_compat_wrapper()** (3 connections) — `server/realtime/connection_manager_utils.py`
- **.broadcast_global()** (2 connections) — `server/realtime/connection_manager_api.py`
- **.broadcast_to_room()** (2 connections) — `server/realtime/connection_manager_api.py`
- **Protocol** (1 connections)
- **Public API utility functions for connection manager.  This module provides conve** (1 connections) — `server/realtime/connection_manager_api.py`
- **Structural type for API helpers; avoids importing ConnectionManager.** (1 connections) — `server/realtime/connection_manager_api.py`
- **Resolve manager without importing ConnectionManager (import cycle).** (1 connections) — `server/realtime/connection_manager_api.py`
- **Broadcast a game event to all connected players.      Args:         event_type:** (1 connections) — `server/realtime/connection_manager_api.py`
- **Send a room event to all players in a specific room.      Args:         room_id:** (1 connections) — `server/realtime/connection_manager_api.py`
- **Utility functions and module-level code for ConnectionManager.  This module cont** (1 connections) — `server/realtime/connection_manager_utils.py`
- **Pass-through for container values; typing lives at call sites.** (1 connections) — `server/realtime/connection_manager_utils.py`
- **Wrap a sync or async callable so callers can always await it.** (1 connections) — `server/realtime/connection_manager_utils.py`
- **Ensure connection manager methods are awaitable.      Wraps synchronous callable** (1 connections) — `server/realtime/connection_manager_utils.py`
- **Resolve a connection manager instance.      Prefers explicitly supplied candidat** (1 connections) — `server/realtime/connection_manager_utils.py`

## Relationships

- [UUID](UUID.md) (12 shared connections)
- [Any](Any.md) (4 shared connections)
- [game tick processing](game_tick_processing.md) (3 shared connections)
- [main()](main%28%29.md) (2 shared connections)
- [. post init ()](_post_init_%28%29.md) (1 shared connections)
- [memory leak metrics](memory_leak_metrics.md) (1 shared connections)

## Source Files

- `server/realtime/connection_manager_api.py`
- `server/realtime/connection_manager_utils.py`

## Audit Trail

- EXTRACTED: 85 (98%)
- INFERRED: 2 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*