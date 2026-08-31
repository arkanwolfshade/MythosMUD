# resolve_connection_manager

> 14 nodes

## Key Concepts

- **resolve_connection_manager()** (10 connections) — `server/realtime/connection_manager_utils.py`
- **_require_manager()** (8 connections) — `server/realtime/connection_manager_api.py`
- **connection_manager_utils.py** (8 connections) — `server/realtime/connection_manager_utils.py`
- **send_room_event()** (7 connections) — `server/realtime/connection_manager_api.py`
- **_ensure_async_compat()** (4 connections) — `server/realtime/connection_manager_utils.py`
- **_coerce_connection_manager()** (3 connections) — `server/realtime/connection_manager_utils.py`
- **_make_async_compat_wrapper()** (3 connections) — `server/realtime/connection_manager_utils.py`
- **Resolve manager without importing ConnectionManager (import cycle).** (1 connections) — `server/realtime/connection_manager_api.py`
- **Send a room event to all players in a specific room. Args: room_id: The room's…** (1 connections) — `server/realtime/connection_manager_api.py`
- **Utility functions and module-level code for ConnectionManager. This module…** (1 connections) — `server/realtime/connection_manager_utils.py`
- **Pass-through for container values; typing lives at call sites.** (1 connections) — `server/realtime/connection_manager_utils.py`
- **Wrap a sync or async callable so callers can always await it.** (1 connections) — `server/realtime/connection_manager_utils.py`
- **Ensure connection manager methods are awaitable. Wraps synchronous callables in…** (1 connections) — `server/realtime/connection_manager_utils.py`
- **Resolve a connection manager instance. Prefers explicitly supplied candidate,…** (1 connections) — `server/realtime/connection_manager_utils.py`

## Relationships

- [magic_service.py](magic_service.py.md) (6 shared connections)
- [get_logger](get_logger.md) (4 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (2 shared connections)
- [connection_manager.py](connection_manager.py.md) (2 shared connections)
- [game_tick_processing.py](game_tick_processing.py.md) (1 shared connections)
- [build_event](build_event.md) (1 shared connections)
- [api/monitoring.py](api-monitoring.py.md) (1 shared connections)
- [GameStateProvider](GameStateProvider.md) (1 shared connections)

## Source Files

- `server/realtime/connection_manager_api.py`
- `server/realtime/connection_manager_utils.py`

## Audit Trail

- EXTRACTED: 32 (94%)
- INFERRED: 2 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*