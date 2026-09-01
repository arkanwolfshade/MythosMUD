# PlayerRespawnEventHandler

> 281 nodes

## Key Concepts

- **PlayerRespawnEventHandler** (55 connections) — `server/realtime/player_event_handlers_respawn.py`
- **PlayerEventHandlerUtils** (46 connections) — `server/realtime/player_event_handlers_utils.py`
- **test_player_event_handlers_respawn.py** (39 connections) — `server/tests/unit/realtime/test_player_event_handlers_respawn.py`
- **PlayerStateEventHandler** (36 connections) — `server/realtime/player_event_handlers_state.py`
- **test_player_event_handlers_state.py** (35 connections) — `server/tests/unit/realtime/test_player_event_handlers_state.py`
- **PlayerEventHandler** (32 connections) — `server/realtime/player_event_handlers.py`
- **player_event_handlers_respawn.py** (30 connections) — `server/realtime/player_event_handlers_respawn.py`
- **realtime/conftest.py** (24 connections) — `server/tests/unit/realtime/conftest.py`
- **asyncio** (22 connections)
- **PlayerRespawnedEvent** (21 connections) — `server/events/event_types.py`
- **asyncio** (21 connections)
- **player_event_handlers_utils.py** (16 connections) — `server/realtime/player_event_handlers_utils.py`
- **fixture** (15 connections)
- **RespawnPlayerEventPayload** (13 connections) — `server/realtime/player_event_handlers_respawn_types.py`
- **PlayerRoomEventHandlerDeps** (12 connections) — `server/realtime/player_event_handlers_room.py`
- **.__init__()** (10 connections) — `server/realtime/player_event_handlers.py`
- **_async_persistence()** (10 connections) — `server/tests/unit/realtime/test_player_event_handlers_respawn.py`
- **test_player_event_handlers_utils_grace_period.py** (10 connections) — `server/tests/unit/realtime/test_player_event_handlers_utils_grace_period.py`
- **.handle_player_respawned()** (9 connections) — `server/realtime/player_event_handlers_respawn.py`
- **._initialize_handlers()** (8 connections) — `server/realtime/player_event_handlers.py`
- **._fetch_delirium_respawn_player_snapshot()** (8 connections) — `server/realtime/player_event_handlers_respawn.py`
- **.get_player_data_for_respawn()** (8 connections) — `server/realtime/player_event_handlers_respawn.py`
- **._resolve_player_data_for_respawn_event()** (8 connections) — `server/realtime/player_event_handlers_respawn.py`
- **._build_respawn_player_payload()** (7 connections) — `server/realtime/player_event_handlers_respawn.py`
- **._fetch_fallback_player_data_for_respawn()** (7 connections) — `server/realtime/player_event_handlers_respawn.py`
- *... and 256 more nodes in this community*

## Relationships

- [event_types.py](event_types.py.md) (41 shared connections)
- [build_event](build_event.md) (16 shared connections)
- [PlayerRoomEventHandler](PlayerRoomEventHandler.md) (11 shared connections)
- [PlayerXPAwardEvent](PlayerXPAwardEvent.md) (7 shared connections)
- [RealTimeEventHandler](RealTimeEventHandler.md) (6 shared connections)
- [PlayerNameExtractor](PlayerNameExtractor.md) (6 shared connections)
- [coerce_int](coerce_int.md) (6 shared connections)
- [test_player_respawn_service.py](test_player_respawn_service.py.md) (5 shared connections)
- [ConnectionManager](ConnectionManager.md) (4 shared connections)
- [player_event_handlers_respawn_room.py](player_event_handlers_respawn_room.py.md) (4 shared connections)
- [pytest.md](pytest.md.md) (4 shared connections)
- [get_logger](get_logger.md) (3 shared connections)

## Source Files

- `server/events/event_types.py`
- `server/realtime/player_event_handlers.py`
- `server/realtime/player_event_handlers_respawn.py`
- `server/realtime/player_event_handlers_respawn_types.py`
- `server/realtime/player_event_handlers_room.py`
- `server/realtime/player_event_handlers_state.py`
- `server/realtime/player_event_handlers_utils.py`
- `server/tests/unit/realtime/conftest.py`
- `server/tests/unit/realtime/test_player_event_handlers_respawn.py`
- `server/tests/unit/realtime/test_player_event_handlers_state.py`
- `server/tests/unit/realtime/test_player_event_handlers_utils_grace_period.py`

## Audit Trail

- EXTRACTED: 544 (85%)
- INFERRED: 93 (15%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*