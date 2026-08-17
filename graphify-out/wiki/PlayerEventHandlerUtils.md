# PlayerEventHandlerUtils

> 343 nodes

## Key Concepts

- **PlayerEventHandlerUtils** (41 connections) — `server/realtime/player_event_handlers_utils.py`
- **PlayerDPUpdated** (38 connections) — `server/events/event_types.py`
- **test_player_event_handlers_respawn.py** (36 connections) — `server/tests/unit/realtime/test_player_event_handlers_respawn.py`
- **test_player_event_handlers.py** (34 connections) — `server/tests/unit/realtime/test_player_event_handlers.py`
- **test_player_event_handlers_state.py** (34 connections) — `server/tests/unit/realtime/test_player_event_handlers_state.py`
- **PlayerRespawnEventHandler** (33 connections) — `server/realtime/player_event_handlers_respawn.py`
- **player_event_handlers_respawn.py** (33 connections) — `server/realtime/player_event_handlers_respawn.py`
- **PlayerEventHandler** (32 connections) — `server/realtime/player_event_handlers.py`
- **PlayerXPAwardEvent** (30 connections) — `server/services/player_combat_service.py`
- **player_event_handlers_state.py** (23 connections) — `server/realtime/player_event_handlers_state.py`
- **asyncio** (22 connections)
- **asyncio** (19 connections)
- **player_event_handlers_utils.py** (16 connections) — `server/realtime/player_event_handlers_utils.py`
- **asyncio** (15 connections)
- **PlayerStateEventHandler** (14 connections) — `server/realtime/player_event_handlers_state.py`
- **RespawnPlayerEventPayload** (11 connections) — `server/realtime/player_event_handlers_respawn.py`
- **.__init__()** (10 connections) — `server/realtime/player_event_handlers.py`
- **_dispatch_player_dp_updated_payload()** (10 connections) — `server/realtime/player_event_handlers_state.py`
- **test_player_event_handlers_utils_grace_period.py** (10 connections) — `server/tests/unit/realtime/test_player_event_handlers_utils_grace_period.py`
- **._extract_occupant_names()** (9 connections) — `server/realtime/player_event_handlers_respawn.py`
- **._initialize_handlers()** (8 connections) — `server/realtime/player_event_handlers.py`
- **._fetch_delirium_respawn_player_snapshot()** (8 connections) — `server/realtime/player_event_handlers_respawn.py`
- **.get_player_data_for_respawn()** (8 connections) — `server/realtime/player_event_handlers_respawn.py`
- **.handle_player_respawned()** (8 connections) — `server/realtime/player_event_handlers_respawn.py`
- **._resolve_player_data_for_respawn_event()** (8 connections) — `server/realtime/player_event_handlers_respawn.py`
- *... and 318 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (64 shared connections)
- [pytest.md](pytest.md.md) (14 shared connections)
- [PlayerRoomEventHandler](PlayerRoomEventHandler.md) (11 shared connections)
- [ConnectionManager](ConnectionManager.md) (10 shared connections)
- [build_event](build_event.md) (10 shared connections)
- [RealTimeEventHandler](RealTimeEventHandler.md) (6 shared connections)
- [realtime/conftest.py](realtime-conftest.py.md) (6 shared connections)
- [coerce_int](coerce_int.md) (6 shared connections)
- [test_websocket_initial_state.py](test_websocket_initial_state.py.md) (6 shared connections)
- [PlayerNameExtractor](PlayerNameExtractor.md) (5 shared connections)
- [CombatPersistenceHandler](CombatPersistenceHandler.md) (4 shared connections)
- [CombatDPSync](CombatDPSync.md) (4 shared connections)

## Source Files

- `server/events/event_types.py`
- `server/realtime/player_event_handlers.py`
- `server/realtime/player_event_handlers_respawn.py`
- `server/realtime/player_event_handlers_state.py`
- `server/realtime/player_event_handlers_utils.py`
- `server/services/combat_hp_sync.py`
- `server/services/player_combat_service.py`
- `server/tests/unit/realtime/test_player_event_handlers.py`
- `server/tests/unit/realtime/test_player_event_handlers_respawn.py`
- `server/tests/unit/realtime/test_player_event_handlers_state.py`
- `server/tests/unit/realtime/test_player_event_handlers_utils_grace_period.py`

## Audit Trail

- EXTRACTED: 640 (91%)
- INFERRED: 64 (9%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*