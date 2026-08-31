# resolve_lazy_attr

> 43 nodes

## Key Concepts

- **resolve_lazy_attr()** (14 connections) — `server/realtime/connection_manager_lazy.py`
- **broadcast_game_event()** (11 connections) — `server/realtime/connection_manager_api.py`
- **test_connection_manager_api.py** (11 connections) — `server/tests/unit/realtime/test_connection_manager_api.py`
- **connection_manager_lazy.py** (9 connections) — `server/realtime/connection_manager_lazy.py`
- **_require_manager()** (8 connections) — `server/realtime/connection_manager_api.py`
- **_ConnectionManagerAPI** (7 connections) — `server/realtime/connection_manager_api.py`
- **send_player_status_update()** (7 connections) — `server/realtime/connection_manager_api.py`
- **send_room_description()** (7 connections) — `server/realtime/connection_manager_api.py`
- **send_room_event()** (7 connections) — `server/realtime/connection_manager_api.py`
- **send_system_notification()** (7 connections) — `server/realtime/connection_manager_api.py`
- **asyncio** (7 connections)
- **test_connection_manager_lazy.py** (7 connections) — `server/tests/unit/realtime/test_connection_manager_lazy.py`
- **UUID** (6 connections)
- **test_resolve_lazy_attr_returns_api_function()** (4 connections) — `server/tests/unit/realtime/test_connection_manager_lazy.py`
- **test_broadcast_game_event()** (3 connections) — `server/tests/unit/realtime/test_connection_manager_api.py`
- **test_require_manager_raises_when_missing()** (3 connections) — `server/tests/unit/realtime/test_connection_manager_api.py`
- **test_send_game_event_with_uuid()** (3 connections) — `server/tests/unit/realtime/test_connection_manager_api.py`
- **test_send_player_status_update()** (3 connections) — `server/tests/unit/realtime/test_connection_manager_api.py`
- **test_send_room_description()** (3 connections) — `server/tests/unit/realtime/test_connection_manager_api.py`
- **test_send_room_event()** (3 connections) — `server/tests/unit/realtime/test_connection_manager_api.py`
- **test_send_system_notification()** (3 connections) — `server/tests/unit/realtime/test_connection_manager_api.py`
- **test_resolve_lazy_attr_unknown_name_raises_attribute_error()** (3 connections) — `server/tests/unit/realtime/test_connection_manager_lazy.py`
- **.send_personal_message()** (2 connections) — `server/realtime/connection_manager_api.py`
- **__getattr__()** (2 connections) — `server/realtime/connection_manager.py`
- **mock_manager()** (2 connections) — `server/tests/unit/realtime/test_connection_manager_api.py`
- *... and 18 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (22 shared connections)
- [build_event](build_event.md) (2 shared connections)
- [pytest.md](pytest.md.md) (2 shared connections)
- [test_game_tick_death.py](test_game_tick_death.py.md) (1 shared connections)
- [MythosTimeEventConsumer](MythosTimeEventConsumer.md) (1 shared connections)
- [game_tick_processing.py](game_tick_processing.py.md) (1 shared connections)
- [AttributeError](AttributeError.md) (1 shared connections)

## Source Files

- `server/realtime/connection_manager.py`
- `server/realtime/connection_manager_api.py`
- `server/realtime/connection_manager_lazy.py`
- `server/tests/unit/realtime/test_connection_manager_api.py`
- `server/tests/unit/realtime/test_connection_manager_lazy.py`

## Audit Trail

- EXTRACTED: 88 (93%)
- INFERRED: 7 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*