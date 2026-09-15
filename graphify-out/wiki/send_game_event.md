# send_game_event

> 64 nodes

## Key Concepts

- **send_game_event()** (31 connections) — `server/realtime/connection_manager_api.py`
- **connection_manager_api.py** (23 connections) — `server/realtime/connection_manager_api.py`
- **resolve_lazy_attr()** (14 connections) — `server/realtime/connection_manager_lazy.py`
- **test_connection_manager_api.py** (13 connections) — `server/tests/unit/realtime/test_connection_manager_api.py`
- **broadcast_game_event()** (11 connections) — `server/realtime/connection_manager_api.py`
- **resolve_connection_manager()** (11 connections) — `server/realtime/connection_manager_utils.py`
- **remove_online_player()** (9 connections) — `server/realtime/connection_manager_api.py`
- **connection_manager_lazy.py** (9 connections) — `server/realtime/connection_manager_lazy.py`
- **_require_manager()** (8 connections) — `server/realtime/connection_manager_api.py`
- **connection_manager_utils.py** (8 connections) — `server/realtime/connection_manager_utils.py`
- **_ConnectionManagerAPI** (7 connections) — `server/realtime/connection_manager_api.py`
- **send_player_status_update()** (7 connections) — `server/realtime/connection_manager_api.py`
- **send_room_description()** (7 connections) — `server/realtime/connection_manager_api.py`
- **send_room_event()** (7 connections) — `server/realtime/connection_manager_api.py`
- **send_system_notification()** (7 connections) — `server/realtime/connection_manager_api.py`
- **UUID** (7 connections)
- **asyncio** (7 connections)
- **test_connection_manager_lazy.py** (6 connections) — `server/tests/unit/realtime/test_connection_manager_lazy.py`
- **_ensure_async_compat()** (4 connections) — `server/realtime/connection_manager_utils.py`
- **test_resolve_lazy_attr_returns_api_function()** (4 connections) — `server/tests/unit/realtime/test_connection_manager_lazy.py`
- **_coerce_connection_manager()** (3 connections) — `server/realtime/connection_manager_utils.py`
- **_make_async_compat_wrapper()** (3 connections) — `server/realtime/connection_manager_utils.py`
- **test_broadcast_game_event()** (3 connections) — `server/tests/unit/realtime/test_connection_manager_api.py`
- **test_remove_online_player_is_a_noop_without_a_manager()** (3 connections) — `server/tests/unit/realtime/test_connection_manager_api.py`
- **test_remove_online_player_pops_the_roster_entry()** (3 connections) — `server/tests/unit/realtime/test_connection_manager_api.py`
- *... and 39 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (6 shared connections)
- [build_event](build_event.md) (4 shared connections)
- [PlayerService](PlayerService.md) (4 shared connections)
- [FollowService](FollowService.md) (4 shared connections)
- [connection_manager.py](connection_manager.py.md) (4 shared connections)
- [game_tick_processing.py](game_tick_processing.py.md) (3 shared connections)
- [HolidayService](HolidayService.md) (3 shared connections)
- [SecureBaseModel](SecureBaseModel.md) (3 shared connections)
- [magic_healing_events.py](magic_healing_events.py.md) (2 shared connections)
- [MPRegenerationService](MPRegenerationService.md) (2 shared connections)
- [test_lucidity_event_dispatcher.py](test_lucidity_event_dispatcher.py.md) (2 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (2 shared connections)

## Source Files

- `server/realtime/connection_manager.py`
- `server/realtime/connection_manager_api.py`
- `server/realtime/connection_manager_lazy.py`
- `server/realtime/connection_manager_utils.py`
- `server/tests/unit/realtime/test_connection_manager_api.py`
- `server/tests/unit/realtime/test_connection_manager_lazy.py`

## Audit Trail

- EXTRACTED: 151 (95%)
- INFERRED: 8 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*