# passive_lucidity_flux/service.py

> 66 nodes · cohesion 0.04

## Key Concepts

- **resolve_lazy_attr()** (14 connections) — `server/realtime/connection_manager_lazy.py`
- **test_connection_manager_api.py** (14 connections) — `server/tests/unit/realtime/test_connection_manager_api.py`
- **broadcast_game_event()** (11 connections) — `server/realtime/connection_manager_api.py`
- **resolve_connection_manager()** (11 connections) — `server/realtime/connection_manager_utils.py`
- **remove_online_player()** (9 connections) — `server/realtime/connection_manager_api.py`
- **_require_manager()** (9 connections) — `server/realtime/connection_manager_api.py`
- **send_system_notification()** (9 connections) — `server/realtime/connection_manager_api.py`
- **connection_manager_lazy.py** (9 connections) — `server/realtime/connection_manager_lazy.py`
- **connection_manager_utils.py** (8 connections) — `server/realtime/connection_manager_utils.py`
- **asyncio** (8 connections)
- **_ConnectionManagerAPI** (7 connections) — `server/realtime/connection_manager_api.py`
- **UUID** (7 connections)
- **send_player_status_update()** (7 connections) — `server/realtime/connection_manager_api.py`
- **send_room_description()** (7 connections) — `server/realtime/connection_manager_api.py`
- **send_room_event()** (7 connections) — `server/realtime/connection_manager_api.py`
- **test_connection_manager_lazy.py** (6 connections) — `server/tests/unit/realtime/test_connection_manager_lazy.py`
- **test_missing_manager_is_logged_not_raised()** (5 connections) — `server/tests/unit/realtime/test_connection_manager_api.py`
- **ConnectionManagerUnavailable** (4 connections) — `server/realtime/connection_manager_api.py`
- **_ensure_async_compat()** (4 connections) — `server/realtime/connection_manager_utils.py`
- **test_resolve_lazy_attr_returns_api_function()** (4 connections) — `server/tests/unit/realtime/test_connection_manager_lazy.py`
- **_coerce_connection_manager()** (3 connections) — `server/realtime/connection_manager_utils.py`
- **_make_async_compat_wrapper()** (3 connections) — `server/realtime/connection_manager_utils.py`
- **test_broadcast_game_event()** (3 connections) — `server/tests/unit/realtime/test_connection_manager_api.py`
- **test_remove_online_player_is_a_noop_without_a_manager()** (3 connections) — `server/tests/unit/realtime/test_connection_manager_api.py`
- **test_remove_online_player_pops_the_roster_entry()** (3 connections) — `server/tests/unit/realtime/test_connection_manager_api.py`
- *... and 41 more nodes in this community*

## Relationships

- [LoggingPatternLinter](LoggingPatternLinter.md) (14 shared connections)
- [test_database_extended.py](test_database_extended.py.md) (8 shared connections)
- [connection_initialization.py](connection_initialization.py.md) (4 shared connections)
- [CombatService](CombatService.md) (2 shared connections)
- [.publish_with_pool](publish_with_pool.md) (2 shared connections)
- [Communities (11 total, 0 thin omitted)](Communities_11_total,_0_thin_omitted.md) (2 shared connections)
- [game_tick_processing.py](game_tick_processing.py.md) (1 shared connections)
- [container_endpoints_basic.py](container_endpoints_basic.py.md) (1 shared connections)
- [_find_item_in_equipped](_find_item_in_equipped.md) (1 shared connections)
- [test_container_persistence_extended_row_helpers.py](test_container_persistence_extended_row_helpers.py.md) (1 shared connections)
- [security.ts](security.ts.md) (1 shared connections)
- [test_message_handlers.py](test_message_handlers.py.md) (1 shared connections)

## Source Files

- `server/realtime/connection_manager.py`
- `server/realtime/connection_manager_api.py`
- `server/realtime/connection_manager_lazy.py`
- `server/realtime/connection_manager_utils.py`
- `server/tests/unit/realtime/test_connection_manager_api.py`
- `server/tests/unit/realtime/test_connection_manager_lazy.py`

## Audit Trail

- EXTRACTED: 129 (93%)
- INFERRED: 9 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*