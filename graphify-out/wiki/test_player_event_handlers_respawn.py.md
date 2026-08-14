# test_player_event_handlers_respawn.py

> 125 nodes

## Key Concepts

- **test_player_event_handlers_respawn.py** (35 connections) — `server/tests/unit/realtime/test_player_event_handlers_respawn.py`
- **PlayerRespawnEventHandler** (33 connections) — `server/realtime/player_event_handlers_respawn.py`
- **asyncio** (22 connections)
- **RespawnPlayerEventPayload** (13 connections) — `server/realtime/player_event_handlers_respawn.py`
- **._extract_occupant_names()** (9 connections) — `server/realtime/player_event_handlers_respawn.py`
- **._fetch_delirium_respawn_player_snapshot()** (8 connections) — `server/realtime/player_event_handlers_respawn.py`
- **.get_player_data_for_respawn()** (8 connections) — `server/realtime/player_event_handlers_respawn.py`
- **.handle_player_respawned()** (8 connections) — `server/realtime/player_event_handlers_respawn.py`
- **._resolve_player_data_for_respawn_event()** (8 connections) — `server/realtime/player_event_handlers_respawn.py`
- **._build_respawn_player_payload()** (7 connections) — `server/realtime/player_event_handlers_respawn.py`
- **._fetch_fallback_player_data_for_respawn()** (7 connections) — `server/realtime/player_event_handlers_respawn.py`
- **.send_respawn_event_with_retry()** (7 connections) — `server/realtime/player_event_handlers_respawn.py`
- **._build_fallback_respawn_player_payload()** (6 connections) — `server/realtime/player_event_handlers_respawn.py`
- **._build_player_respawned_event()** (6 connections) — `server/realtime/player_event_handlers_respawn.py`
- **._enrich_room_data_with_occupant_names()** (6 connections) — `server/realtime/player_event_handlers_respawn.py`
- **.handle_player_delirium_respawned()** (6 connections) — `server/realtime/player_event_handlers_respawn.py`
- **._send_room_occupants_after_respawn()** (6 connections) — `server/realtime/player_event_handlers_respawn.py`
- **UUID** (6 connections)
- **RespawnPlayerStatsPayload** (5 connections) — `server/realtime/player_event_handlers_respawn.py`
- **.get_current_lucidity()** (5 connections) — `server/realtime/player_event_handlers_respawn.py`
- **.get_player_data_for_delirium_respawn()** (5 connections) — `server/realtime/player_event_handlers_respawn.py`
- **.__init__()** (5 connections) — `server/realtime/player_event_handlers_respawn.py`
- **._room_data_from_persistence_room()** (5 connections) — `server/realtime/player_event_handlers_respawn.py`
- **._convert_npc_ids_to_names()** (4 connections) — `server/realtime/player_event_handlers_respawn.py`
- **._get_npc_name_from_lifecycle_manager()** (4 connections) — `server/realtime/player_event_handlers_respawn.py`
- *... and 100 more nodes in this community*

## Relationships

- [event_types.py](event_types.py.md) (18 shared connections)
- [PlayerEventHandlerUtils](PlayerEventHandlerUtils.md) (7 shared connections)
- [websocket_initial_state.py](websocket_initial_state.py.md) (6 shared connections)
- [ConnectionManager](ConnectionManager.md) (4 shared connections)
- [coerce_int](coerce_int.md) (4 shared connections)
- [build_event](build_event.md) (3 shared connections)
- [get_logger](get_logger.md) (1 shared connections)

## Source Files

- `server/realtime/player_event_handlers_respawn.py`
- `server/tests/unit/realtime/test_player_event_handlers_respawn.py`

## Audit Trail

- EXTRACTED: 219 (96%)
- INFERRED: 8 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*