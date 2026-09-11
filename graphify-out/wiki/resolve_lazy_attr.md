# resolve_lazy_attr

> 48 nodes

## Key Concepts

- **resolve_lazy_attr()** (14 connections) — `server/realtime/connection_manager_lazy.py`
- **test_connection_manager_api.py** (13 connections) — `server/tests/unit/realtime/test_connection_manager_api.py`
- **remove_online_player()** (9 connections) — `server/realtime/connection_manager_api.py`
- **connection_manager_lazy.py** (9 connections) — `server/realtime/connection_manager_lazy.py`
- **_require_manager()** (8 connections) — `server/realtime/connection_manager_api.py`
- **_ConnectionManagerAPI** (7 connections) — `server/realtime/connection_manager_api.py`
- **send_player_status_update()** (7 connections) — `server/realtime/connection_manager_api.py`
- **send_room_description()** (7 connections) — `server/realtime/connection_manager_api.py`
- **send_room_event()** (7 connections) — `server/realtime/connection_manager_api.py`
- **send_system_notification()** (7 connections) — `server/realtime/connection_manager_api.py`
- **UUID** (7 connections)
- **asyncio** (7 connections)
- **test_connection_manager_lazy.py** (6 connections) — `server/tests/unit/realtime/test_connection_manager_lazy.py`
- **test_resolve_lazy_attr_returns_api_function()** (4 connections) — `server/tests/unit/realtime/test_connection_manager_lazy.py`
- **test_broadcast_game_event()** (3 connections) — `server/tests/unit/realtime/test_connection_manager_api.py`
- **test_remove_online_player_is_a_noop_without_a_manager()** (3 connections) — `server/tests/unit/realtime/test_connection_manager_api.py`
- **test_remove_online_player_pops_the_roster_entry()** (3 connections) — `server/tests/unit/realtime/test_connection_manager_api.py`
- **test_require_manager_raises_when_missing()** (3 connections) — `server/tests/unit/realtime/test_connection_manager_api.py`
- **test_send_game_event_with_uuid()** (3 connections) — `server/tests/unit/realtime/test_connection_manager_api.py`
- **test_send_player_status_update()** (3 connections) — `server/tests/unit/realtime/test_connection_manager_api.py`
- **test_send_room_description()** (3 connections) — `server/tests/unit/realtime/test_connection_manager_api.py`
- **test_send_room_event()** (3 connections) — `server/tests/unit/realtime/test_connection_manager_api.py`
- **test_send_system_notification()** (3 connections) — `server/tests/unit/realtime/test_connection_manager_api.py`
- **test_resolve_lazy_attr_unknown_name_raises_attribute_error()** (3 connections) — `server/tests/unit/realtime/test_connection_manager_lazy.py`
- **.send_personal_message()** (2 connections) — `server/realtime/connection_manager_api.py`
- *... and 23 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (10 shared connections)
- [Player](Player.md) (8 shared connections)
- [game_tick_processing.py](game_tick_processing.py.md) (4 shared connections)
- [PlayerService](PlayerService.md) (2 shared connections)
- [resolve_connection_manager](resolve_connection_manager.md) (2 shared connections)
- [connection_manager.py](connection_manager.py.md) (2 shared connections)
- [build_event](build_event.md) (1 shared connections)
- [websocket_handler.py](websocket_handler.py.md) (1 shared connections)

## Source Files

- `server/realtime/connection_manager.py`
- `server/realtime/connection_manager_api.py`
- `server/realtime/connection_manager_lazy.py`
- `server/tests/unit/realtime/test_connection_manager_api.py`
- `server/tests/unit/realtime/test_connection_manager_lazy.py`

## Audit Trail

- EXTRACTED: 93 (93%)
- INFERRED: 7 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*