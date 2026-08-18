# resolve_lazy_attr

> 32 nodes

## Key Concepts

- **resolve_lazy_attr()** (11 connections) — `server/realtime/connection_manager_lazy.py`
- **resolve_connection_manager()** (10 connections) — `server/realtime/connection_manager_utils.py`
- **_require_manager()** (8 connections) — `server/realtime/connection_manager_api.py`
- **connection_manager_lazy.py** (8 connections) — `server/realtime/connection_manager_lazy.py`
- **connection_manager_utils.py** (8 connections) — `server/realtime/connection_manager_utils.py`
- **_ConnectionManagerAPI** (7 connections) — `server/realtime/connection_manager_api.py`
- **send_player_status_update()** (7 connections) — `server/realtime/connection_manager_api.py`
- **send_room_description()** (7 connections) — `server/realtime/connection_manager_api.py`
- **send_room_event()** (7 connections) — `server/realtime/connection_manager_api.py`
- **send_system_notification()** (7 connections) — `server/realtime/connection_manager_api.py`
- **UUID** (6 connections)
- **_ensure_async_compat()** (4 connections) — `server/realtime/connection_manager_utils.py`
- **_coerce_connection_manager()** (3 connections) — `server/realtime/connection_manager_utils.py`
- **_make_async_compat_wrapper()** (3 connections) — `server/realtime/connection_manager_utils.py`
- **.send_personal_message()** (2 connections) — `server/realtime/connection_manager_api.py`
- **__getattr__()** (2 connections) — `server/realtime/connection_manager.py`
- **.broadcast_global()** (1 connections) — `server/realtime/connection_manager_api.py`
- **.broadcast_to_room()** (1 connections) — `server/realtime/connection_manager_api.py`
- **Protocol** (1 connections)
- **Send a system notification to a player. Args: player_id: The player's ID…** (1 connections) — `server/realtime/connection_manager_api.py`
- **Send a player status update to a player. Args: player_id: The player's ID…** (1 connections) — `server/realtime/connection_manager_api.py`
- **Send room description to a player. Args: player_id: The player's ID room_data:…** (1 connections) — `server/realtime/connection_manager_api.py`
- **Structural type for API helpers; avoids importing ConnectionManager.** (1 connections) — `server/realtime/connection_manager_api.py`
- **Resolve manager without importing ConnectionManager (import cycle).** (1 connections) — `server/realtime/connection_manager_api.py`
- **Send a room event to all players in a specific room. Args: room_id: The room's…** (1 connections) — `server/realtime/connection_manager_api.py`
- *... and 7 more nodes in this community*

## Relationships

- [DatabaseError](DatabaseError.md) (9 shared connections)
- [test_lucidity_event_dispatcher.py](test_lucidity_event_dispatcher.py.md) (7 shared connections)
- [test_connection_manager_api.py](test_connection_manager_api.py.md) (5 shared connections)
- [get_logger](get_logger.md) (5 shared connections)
- [test_game_tick_death.py](test_game_tick_death.py.md) (3 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (2 shared connections)
- [build_event](build_event.md) (1 shared connections)
- [AttributeError](AttributeError.md) (1 shared connections)
- [.state](state.md) (1 shared connections)

## Source Files

- `server/realtime/connection_manager.py`
- `server/realtime/connection_manager_api.py`
- `server/realtime/connection_manager_lazy.py`
- `server/realtime/connection_manager_utils.py`

## Audit Trail

- EXTRACTED: 67 (89%)
- INFERRED: 8 (11%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*