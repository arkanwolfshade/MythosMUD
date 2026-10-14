# PlayerRespawnEventHandler

> 134 nodes

## Key Concepts

- **PlayerRespawnEventHandler** (57 connections) — `server/realtime/player_event_handlers_respawn.py`
- **test_player_event_handlers_respawn.py** (39 connections) — `server/tests/unit/realtime/test_player_event_handlers_respawn.py`
- **player_event_handlers_respawn.py** (34 connections) — `server/realtime/player_event_handlers_respawn.py`
- **PlayerRespawnedEvent** (25 connections) — `server/events/event_types.py`
- **asyncio** (23 connections)
- **test_player_event_handler_base.py** (15 connections) — `server/tests/unit/realtime/test_player_event_handler_base.py`
- **PlayerEventHandlerBase** (13 connections) — `server/realtime/player_event_handler_base.py`
- **RespawnPlayerEventPayload** (13 connections) — `server/realtime/player_event_handlers_respawn_types.py`
- **_async_persistence()** (11 connections) — `server/tests/unit/realtime/test_player_event_handlers_respawn.py`
- **._fetch_delirium_respawn_player_snapshot()** (9 connections) — `server/realtime/player_event_handlers_respawn.py`
- **.handle_player_respawned()** (9 connections) — `server/realtime/player_event_handlers_respawn.py`
- **_collaborators()** (9 connections) — `server/tests/unit/realtime/test_player_event_handler_base.py`
- **player_event_handler_base.py** (9 connections) — `server/realtime/player_event_handler_base.py`
- **.get_player_data_for_respawn()** (8 connections) — `server/realtime/player_event_handlers_respawn.py`
- **.handle_player_delirium_respawned()** (8 connections) — `server/realtime/player_event_handlers_respawn.py`
- **._resolve_player_data_for_respawn_event()** (8 connections) — `server/realtime/player_event_handlers_respawn.py`
- **._build_player_respawned_event()** (7 connections) — `server/realtime/player_event_handlers_respawn.py`
- **._build_respawn_player_payload()** (7 connections) — `server/realtime/player_event_handlers_respawn.py`
- **._fetch_fallback_player_data_for_respawn()** (7 connections) — `server/realtime/player_event_handlers_respawn.py`
- **.send_respawn_event_with_retry()** (7 connections) — `server/realtime/player_event_handlers_respawn.py`
- **_logger_method()** (7 connections) — `server/tests/unit/realtime/test_player_event_handlers_respawn.py`
- **_send_personal_message()** (7 connections) — `server/tests/unit/realtime/test_player_event_handlers_respawn.py`
- **test_get_player_data_for_delirium_respawn_error_handling()** (7 connections) — `server/tests/unit/realtime/test_player_event_handlers_respawn.py`
- **UUID** (7 connections)
- **._build_fallback_respawn_player_payload()** (6 connections) — `server/realtime/player_event_handlers_respawn.py`
- *... and 109 more nodes in this community*

## Relationships

- [PlayerEventHandlerUtils](PlayerEventHandlerUtils.md) (10 shared connections)
- [test_message_category_invariants.py](test_message_category_invariants.py.md) (9 shared connections)
- [get_logger](get_logger.md) (9 shared connections)
- [build_event](build_event.md) (7 shared connections)
- [player_event_handlers.py](player_event_handlers.py.md) (6 shared connections)
- [coerce_int](coerce_int.md) (6 shared connections)
- [PlayerDPUpdated](PlayerDPUpdated.md) (5 shared connections)
- [NpcDisposition](NpcDisposition.md) (5 shared connections)
- [test_player_respawn_service.py](test_player_respawn_service.py.md) (4 shared connections)
- [ConnectionManager](ConnectionManager.md) (4 shared connections)
- [player_event_handlers_respawn_room.py](player_event_handlers_respawn_room.py.md) (4 shared connections)
- [event_handler.py](event_handler.py.md) (2 shared connections)

## Source Files

- `server/events/event_types.py`
- `server/realtime/__init__.py`
- `server/realtime/player_event_handler_base.py`
- `server/realtime/player_event_handlers_respawn.py`
- `server/realtime/player_event_handlers_respawn_types.py`
- `server/tests/unit/realtime/test_player_event_handler_base.py`
- `server/tests/unit/realtime/test_player_event_handlers_respawn.py`

## Audit Trail

- EXTRACTED: 308 (88%)
- INFERRED: 44 (12%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*