# ConnectionManager

> 212 nodes

## Key Concepts

- **ConnectionManager** (162 connections) — `server/realtime/connection_manager.py`
- **PlayerEventHandlerUtils** (42 connections) — `server/realtime/player_event_handlers_utils.py`
- **PlayerRespawnEventHandler** (33 connections) — `server/realtime/player_event_handlers_respawn.py`
- **player_event_handlers_respawn.py** (33 connections) — `server/realtime/player_event_handlers_respawn.py`
- **test_player_event_handlers_state.py** (33 connections) — `server/tests/unit/realtime/test_player_event_handlers_state.py`
- **PlayerXPAwardEvent** (32 connections) — `server/services/player_combat_service.py`
- **player_event_handlers_state.py** (23 connections) — `server/realtime/player_event_handlers_state.py`
- **get_async_persistence()** (19 connections) — `server/async_persistence.py`
- **asyncio** (19 connections)
- **PlayerRespawnedEvent** (16 connections) — `server/events/event_types.py`
- **PlayerStateEventHandler** (14 connections) — `server/realtime/player_event_handlers_state.py`
- **RespawnPlayerEventPayload** (13 connections) — `server/realtime/player_event_handlers_respawn.py`
- **_dispatch_player_dp_updated_payload()** (10 connections) — `server/realtime/player_event_handlers_state.py`
- **._extract_occupant_names()** (9 connections) — `server/realtime/player_event_handlers_respawn.py`
- **test_player_event_handlers_utils_grace_period.py** (9 connections) — `server/tests/unit/realtime/test_player_event_handlers_utils_grace_period.py`
- **._fetch_delirium_respawn_player_snapshot()** (8 connections) — `server/realtime/player_event_handlers_respawn.py`
- **.get_player_data_for_respawn()** (8 connections) — `server/realtime/player_event_handlers_respawn.py`
- **.handle_player_respawned()** (8 connections) — `server/realtime/player_event_handlers_respawn.py`
- **._resolve_player_data_for_respawn_event()** (8 connections) — `server/realtime/player_event_handlers_respawn.py`
- **._initialize_handlers()** (7 connections) — `server/realtime/player_event_handlers.py`
- **._build_respawn_player_payload()** (7 connections) — `server/realtime/player_event_handlers_respawn.py`
- **._fetch_fallback_player_data_for_respawn()** (7 connections) — `server/realtime/player_event_handlers_respawn.py`
- **._prepare_room_data_for_respawn()** (7 connections) — `server/realtime/player_event_handlers_respawn.py`
- **.send_respawn_event_with_retry()** (7 connections) — `server/realtime/player_event_handlers_respawn.py`
- **_send_player_death_notification()** (7 connections) — `server/realtime/player_event_handlers_state.py`
- *... and 187 more nodes in this community*

## Relationships

- [UUID](UUID.md) (54 shared connections)
- [get_npc_instance_service](get_npc_instance_service.md) (38 shared connections)
- [get_logger](get_logger.md) (20 shared connections)
- [Player](Player.md) (11 shared connections)
- [websocket_initial_state.py](websocket_initial_state.py.md) (10 shared connections)
- [BaseEvent](BaseEvent.md) (8 shared connections)
- [PlayerCombatService](PlayerCombatService.md) (8 shared connections)
- [connection_manager.py](connection_manager.py.md) (8 shared connections)
- [connection_manager_health_cleanup.py](connection_manager_health_cleanup.py.md) (8 shared connections)
- [PlayerNameExtractor](PlayerNameExtractor.md) (8 shared connections)
- [Protocol](Protocol.md) (6 shared connections)
- [server/exceptions.py](server-exceptions.py.md) (6 shared connections)

## Source Files

- `server/async_persistence.py`
- `server/events/event_types.py`
- `server/realtime/connection_manager.py`
- `server/realtime/player_event_handlers.py`
- `server/realtime/player_event_handlers_respawn.py`
- `server/realtime/player_event_handlers_state.py`
- `server/realtime/player_event_handlers_utils.py`
- `server/services/player_combat_service.py`
- `server/tests/unit/realtime/test_player_event_handlers_state.py`
- `server/tests/unit/realtime/test_player_event_handlers_utils_grace_period.py`

## Audit Trail

- EXTRACTED: 908 (95%)
- INFERRED: 48 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*