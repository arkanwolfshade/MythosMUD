# test_connection_manager_api.py

> 41 nodes

## Key Concepts

- **test_connection_manager_api.py** (11 connections) — `server/tests/unit/realtime/test_connection_manager_api.py`
- **resolve_connection_manager()** (10 connections) — `server/realtime/connection_manager_utils.py`
- **__getattr__()** (9 connections) — `server/realtime/connection_manager.py`
- **_require_manager()** (8 connections) — `server/realtime/connection_manager_api.py`
- **connection_manager_utils.py** (8 connections) — `server/realtime/connection_manager_utils.py`
- **_ConnectionManagerAPI** (7 connections) — `server/realtime/connection_manager_api.py`
- **send_player_status_update()** (7 connections) — `server/realtime/connection_manager_api.py`
- **send_room_description()** (7 connections) — `server/realtime/connection_manager_api.py`
- **send_room_event()** (7 connections) — `server/realtime/connection_manager_api.py`
- **send_system_notification()** (7 connections) — `server/realtime/connection_manager_api.py`
- **asyncio** (7 connections)
- **UUID** (6 connections)
- **_ensure_async_compat()** (4 connections) — `server/realtime/connection_manager_utils.py`
- **_coerce_connection_manager()** (3 connections) — `server/realtime/connection_manager_utils.py`
- **_make_async_compat_wrapper()** (3 connections) — `server/realtime/connection_manager_utils.py`
- **test_broadcast_game_event()** (3 connections) — `server/tests/unit/realtime/test_connection_manager_api.py`
- **test_require_manager_raises_when_missing()** (3 connections) — `server/tests/unit/realtime/test_connection_manager_api.py`
- **test_send_game_event_with_uuid()** (3 connections) — `server/tests/unit/realtime/test_connection_manager_api.py`
- **test_send_player_status_update()** (3 connections) — `server/tests/unit/realtime/test_connection_manager_api.py`
- **test_send_room_description()** (3 connections) — `server/tests/unit/realtime/test_connection_manager_api.py`
- **test_send_room_event()** (3 connections) — `server/tests/unit/realtime/test_connection_manager_api.py`
- **test_send_system_notification()** (3 connections) — `server/tests/unit/realtime/test_connection_manager_api.py`
- **.send_personal_message()** (2 connections) — `server/realtime/connection_manager_api.py`
- **mock_manager()** (2 connections) — `server/tests/unit/realtime/test_connection_manager_api.py`
- **.broadcast_global()** (1 connections) — `server/realtime/connection_manager_api.py`
- *... and 16 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (10 shared connections)
- [PlayerService](PlayerService.md) (7 shared connections)
- [connection_manager.py](connection_manager.py.md) (7 shared connections)
- [game_tick_processing.py](game_tick_processing.py.md) (3 shared connections)
- [build_event](build_event.md) (1 shared connections)
- [AttributeError](AttributeError.md) (1 shared connections)
- [api/monitoring.py](api-monitoring.py.md) (1 shared connections)
- [.get_instance](get_instance.md) (1 shared connections)
- [GameStateProvider](GameStateProvider.md) (1 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (1 shared connections)
- [pytest.md](pytest.md.md) (1 shared connections)

## Source Files

- `server/realtime/connection_manager.py`
- `server/realtime/connection_manager_api.py`
- `server/realtime/connection_manager_utils.py`
- `server/tests/unit/realtime/test_connection_manager_api.py`

## Audit Trail

- EXTRACTED: 82 (91%)
- INFERRED: 8 (9%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*