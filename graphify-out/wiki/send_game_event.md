# send_game_event

> 45 nodes

## Key Concepts

- **send_game_event()** (29 connections) — `server/realtime/connection_manager_api.py`
- **broadcast_game_event()** (11 connections) — `server/realtime/connection_manager_api.py`
- **resolve_connection_manager()** (10 connections) — `server/realtime/connection_manager_utils.py`
- **test_connection_manager_api.py** (10 connections) — `server/tests/unit/realtime/test_connection_manager_api.py`
- **__getattr__()** (9 connections) — `server/realtime/connection_manager.py`
- **connection_manager_utils.py** (9 connections) — `server/realtime/connection_manager_utils.py`
- **_require_manager()** (8 connections) — `server/realtime/connection_manager_api.py`
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
- *... and 20 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (15 shared connections)
- [DatabaseError](DatabaseError.md) (12 shared connections)
- [magic_service.py](magic_service.py.md) (4 shared connections)
- [build_event](build_event.md) (3 shared connections)
- [FollowService](FollowService.md) (3 shared connections)
- [MPRegenerationService](MPRegenerationService.md) (2 shared connections)
- [test_lucidity_event_dispatcher.py](test_lucidity_event_dispatcher.py.md) (2 shared connections)
- [asyncio](asyncio.md) (1 shared connections)
- [MythosTimeEventConsumer](MythosTimeEventConsumer.md) (1 shared connections)
- [test_magic_healing_events.py](test_magic_healing_events.py.md) (1 shared connections)
- [_MagicServiceCore](_MagicServiceCore.md) (1 shared connections)
- [PartyService](PartyService.md) (1 shared connections)

## Source Files

- `server/realtime/connection_manager.py`
- `server/realtime/connection_manager_api.py`
- `server/realtime/connection_manager_utils.py`
- `server/tests/unit/realtime/test_connection_manager_api.py`

## Audit Trail

- EXTRACTED: 112 (93%)
- INFERRED: 8 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*