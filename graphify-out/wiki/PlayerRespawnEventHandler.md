# PlayerRespawnEventHandler

> 163 nodes

## Key Concepts

- **PlayerRespawnEventHandler** (55 connections) — `server/realtime/player_event_handlers_respawn.py`
- **PlayerEventHandlerUtils** (46 connections) — `server/realtime/player_event_handlers_utils.py`
- **test_player_event_handlers_respawn.py** (38 connections) — `server/tests/unit/realtime/test_player_event_handlers_respawn.py`
- **player_event_handlers_respawn.py** (30 connections) — `server/realtime/player_event_handlers_respawn.py`
- **asyncio** (22 connections)
- **player_event_handlers_utils.py** (16 connections) — `server/realtime/player_event_handlers_utils.py`
- **RespawnPlayerEventPayload** (13 connections) — `server/realtime/player_event_handlers_respawn_types.py`
- **_async_persistence()** (10 connections) — `server/tests/unit/realtime/test_player_event_handlers_respawn.py`
- **.handle_player_respawned()** (9 connections) — `server/realtime/player_event_handlers_respawn.py`
- **test_player_event_handlers_utils_grace_period.py** (9 connections) — `server/tests/unit/realtime/test_player_event_handlers_utils_grace_period.py`
- **._fetch_delirium_respawn_player_snapshot()** (8 connections) — `server/realtime/player_event_handlers_respawn.py`
- **.get_player_data_for_respawn()** (8 connections) — `server/realtime/player_event_handlers_respawn.py`
- **._resolve_player_data_for_respawn_event()** (8 connections) — `server/realtime/player_event_handlers_respawn.py`
- **._build_respawn_player_payload()** (7 connections) — `server/realtime/player_event_handlers_respawn.py`
- **._fetch_fallback_player_data_for_respawn()** (7 connections) — `server/realtime/player_event_handlers_respawn.py`
- **.handle_player_delirium_respawned()** (7 connections) — `server/realtime/player_event_handlers_respawn.py`
- **.send_respawn_event_with_retry()** (7 connections) — `server/realtime/player_event_handlers_respawn.py`
- **_logger_method()** (7 connections) — `server/tests/unit/realtime/test_player_event_handlers_respawn.py`
- **UUID** (7 connections)
- **Any** (7 connections)
- **._build_fallback_respawn_player_payload()** (6 connections) — `server/realtime/player_event_handlers_respawn.py`
- **._build_player_respawned_event()** (6 connections) — `server/realtime/player_event_handlers_respawn.py`
- **._emit_respawn_room_posture()** (6 connections) — `server/realtime/player_event_handlers_respawn.py`
- **._send_room_occupants_after_respawn()** (6 connections) — `server/realtime/player_event_handlers_respawn.py`
- **_send_personal_message()** (6 connections) — `server/tests/unit/realtime/test_player_event_handlers_respawn.py`
- *... and 138 more nodes in this community*

## Relationships

- [event_types.py](event_types.py.md) (14 shared connections)
- [PlayerEventHandler](PlayerEventHandler.md) (12 shared connections)
- [PlayerDPUpdated](PlayerDPUpdated.md) (9 shared connections)
- [coerce_int](coerce_int.md) (6 shared connections)
- [player_event_handlers_respawn_room.py](player_event_handlers_respawn_room.py.md) (4 shared connections)
- [build_event](build_event.md) (4 shared connections)
- [test_player_event_handlers_utils.py](test_player_event_handlers_utils.py.md) (3 shared connections)
- [PlayerNameExtractor](PlayerNameExtractor.md) (3 shared connections)
- [emit_posture_change](emit_posture_change.md) (3 shared connections)
- [Player](Player.md) (3 shared connections)
- [ConnectionManager](ConnectionManager.md) (2 shared connections)
- [get_async_session](get_async_session.md) (2 shared connections)

## Source Files

- `server/realtime/__init__.py`
- `server/realtime/player_event_handlers_respawn.py`
- `server/realtime/player_event_handlers_respawn_types.py`
- `server/realtime/player_event_handlers_utils.py`
- `server/tests/unit/realtime/test_player_event_handlers_respawn.py`
- `server/tests/unit/realtime/test_player_event_handlers_utils_grace_period.py`

## Audit Trail

- EXTRACTED: 332 (89%)
- INFERRED: 42 (11%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*