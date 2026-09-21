# send_game_event

> 60 nodes

## Key Concepts

- **send_game_event()** (31 connections) — `server/realtime/connection_manager_api.py`
- **connection_manager_api.py** (24 connections) — `server/realtime/connection_manager_api.py`
- **resolve_lazy_attr()** (14 connections) — `server/realtime/connection_manager_lazy.py`
- **test_connection_manager_api.py** (14 connections) — `server/tests/unit/realtime/test_connection_manager_api.py`
- **broadcast_game_event()** (11 connections) — `server/realtime/connection_manager_api.py`
- **remove_online_player()** (9 connections) — `server/realtime/connection_manager_api.py`
- **_require_manager()** (9 connections) — `server/realtime/connection_manager_api.py`
- **connection_manager_lazy.py** (9 connections) — `server/realtime/connection_manager_lazy.py`
- **asyncio** (8 connections)
- **_ConnectionManagerAPI** (7 connections) — `server/realtime/connection_manager_api.py`
- **send_player_status_update()** (7 connections) — `server/realtime/connection_manager_api.py`
- **send_room_description()** (7 connections) — `server/realtime/connection_manager_api.py`
- **send_room_event()** (7 connections) — `server/realtime/connection_manager_api.py`
- **send_system_notification()** (7 connections) — `server/realtime/connection_manager_api.py`
- **UUID** (7 connections)
- **test_connection_manager_lazy.py** (6 connections) — `server/tests/unit/realtime/test_connection_manager_lazy.py`
- **test_missing_manager_is_logged_not_raised()** (5 connections) — `server/tests/unit/realtime/test_connection_manager_api.py`
- **ConnectionManagerUnavailable** (4 connections) — `server/realtime/connection_manager_api.py`
- **test_resolve_lazy_attr_returns_api_function()** (4 connections) — `server/tests/unit/realtime/test_connection_manager_lazy.py`
- **test_broadcast_game_event()** (3 connections) — `server/tests/unit/realtime/test_connection_manager_api.py`
- **test_remove_online_player_is_a_noop_without_a_manager()** (3 connections) — `server/tests/unit/realtime/test_connection_manager_api.py`
- **test_remove_online_player_pops_the_roster_entry()** (3 connections) — `server/tests/unit/realtime/test_connection_manager_api.py`
- **test_require_manager_raises_when_missing()** (3 connections) — `server/tests/unit/realtime/test_connection_manager_api.py`
- **test_send_game_event_with_uuid()** (3 connections) — `server/tests/unit/realtime/test_connection_manager_api.py`
- **test_send_player_status_update()** (3 connections) — `server/tests/unit/realtime/test_connection_manager_api.py`
- *... and 35 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (6 shared connections)
- [build_event](build_event.md) (4 shared connections)
- [GameStateProvider](GameStateProvider.md) (4 shared connections)
- [follow_service.py](follow_service.py.md) (4 shared connections)
- [test_websocket_handler_core.py](test_websocket_handler_core.py.md) (3 shared connections)
- [game_tick_processing.py](game_tick_processing.py.md) (2 shared connections)
- [MPRegenerationService](MPRegenerationService.md) (2 shared connections)
- [SpellCostsService](SpellCostsService.md) (2 shared connections)
- [PartyService](PartyService.md) (2 shared connections)
- [CorruptionTier](CorruptionTier.md) (2 shared connections)
- [LucidityService](LucidityService.md) (2 shared connections)
- [connection_manager.py](connection_manager.py.md) (2 shared connections)

## Source Files

- `server/realtime/connection_manager.py`
- `server/realtime/connection_manager_api.py`
- `server/realtime/connection_manager_lazy.py`
- `server/tests/unit/realtime/test_connection_manager_api.py`
- `server/tests/unit/realtime/test_connection_manager_lazy.py`

## Audit Trail

- EXTRACTED: 142 (95%)
- INFERRED: 8 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*