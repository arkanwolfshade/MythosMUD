# PlayerRespawnEventHandler

> 119 nodes

## Key Concepts

- **PlayerRespawnEventHandler** (55 connections) — `server/realtime/player_event_handlers_respawn.py`
- **test_player_event_handlers_respawn.py** (38 connections) — `server/tests/unit/realtime/test_player_event_handlers_respawn.py`
- **asyncio** (22 connections)
- **PlayerRespawnedEvent** (21 connections) — `server/events/event_types.py`
- **RespawnPlayerEventPayload** (13 connections) — `server/realtime/player_event_handlers_respawn_types.py`
- **_async_persistence()** (10 connections) — `server/tests/unit/realtime/test_player_event_handlers_respawn.py`
- **.handle_player_respawned()** (9 connections) — `server/realtime/player_event_handlers_respawn.py`
- **._fetch_delirium_respawn_player_snapshot()** (8 connections) — `server/realtime/player_event_handlers_respawn.py`
- **.get_player_data_for_respawn()** (8 connections) — `server/realtime/player_event_handlers_respawn.py`
- **._resolve_player_data_for_respawn_event()** (8 connections) — `server/realtime/player_event_handlers_respawn.py`
- **._build_respawn_player_payload()** (7 connections) — `server/realtime/player_event_handlers_respawn.py`
- **._fetch_fallback_player_data_for_respawn()** (7 connections) — `server/realtime/player_event_handlers_respawn.py`
- **.handle_player_delirium_respawned()** (7 connections) — `server/realtime/player_event_handlers_respawn.py`
- **.send_respawn_event_with_retry()** (7 connections) — `server/realtime/player_event_handlers_respawn.py`
- **_logger_method()** (7 connections) — `server/tests/unit/realtime/test_player_event_handlers_respawn.py`
- **UUID** (7 connections)
- **._build_fallback_respawn_player_payload()** (6 connections) — `server/realtime/player_event_handlers_respawn.py`
- **._build_player_respawned_event()** (6 connections) — `server/realtime/player_event_handlers_respawn.py`
- **._emit_respawn_room_posture()** (6 connections) — `server/realtime/player_event_handlers_respawn.py`
- **._send_room_occupants_after_respawn()** (6 connections) — `server/realtime/player_event_handlers_respawn.py`
- **_send_personal_message()** (6 connections) — `server/tests/unit/realtime/test_player_event_handlers_respawn.py`
- **test_get_player_data_for_delirium_respawn_error_handling()** (6 connections) — `server/tests/unit/realtime/test_player_event_handlers_respawn.py`
- **test_get_player_data_for_respawn_error_handling()** (6 connections) — `server/tests/unit/realtime/test_player_event_handlers_respawn.py`
- **test_get_player_data_for_respawn_no_get_stats()** (6 connections) — `server/tests/unit/realtime/test_player_event_handlers_respawn.py`
- **test_handle_player_delirium_respawned_success()** (6 connections) — `server/tests/unit/realtime/test_player_event_handlers_respawn.py`
- *... and 94 more nodes in this community*

## Relationships

- [PlayerEventHandlerUtils](PlayerEventHandlerUtils.md) (15 shared connections)
- [event_types.py](event_types.py.md) (7 shared connections)
- [models/player.py](models-player.py.md) (4 shared connections)
- [Player](Player.md) (4 shared connections)
- [test_event_handler.py](test_event_handler.py.md) (3 shared connections)
- [build_event](build_event.md) (3 shared connections)
- [player_event_handlers_respawn_room.py](player_event_handlers_respawn_room.py.md) (2 shared connections)
- [PlayerRespawnService](PlayerRespawnService.md) (1 shared connections)
- [EventBus](EventBus.md) (1 shared connections)
- [._bind_event_type](_bind_event_type.md) (1 shared connections)
- [ConnectionManager](ConnectionManager.md) (1 shared connections)
- [emit_posture_change](emit_posture_change.md) (1 shared connections)

## Source Files

- `server/events/event_types.py`
- `server/realtime/player_event_handlers.py`
- `server/realtime/player_event_handlers_respawn.py`
- `server/realtime/player_event_handlers_respawn_types.py`
- `server/tests/unit/realtime/test_player_event_handlers_respawn.py`

## Audit Trail

- EXTRACTED: 236 (87%)
- INFERRED: 35 (13%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*