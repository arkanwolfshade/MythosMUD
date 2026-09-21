# player_event_handlers_respawn_room.py

> 53 nodes

## Key Concepts

- **player_event_handlers_respawn_room.py** (24 connections) — `server/realtime/player_event_handlers_respawn_room.py`
- **get_container_async_persistence()** (18 connections) — `server/container/async_persistence_access.py`
- **test_player_event_handlers_respawn_room.py** (13 connections) — `server/tests/unit/realtime/test_player_event_handlers_respawn_room.py`
- **prepare_room_data_for_respawn()** (11 connections) — `server/realtime/player_event_handlers_respawn_room.py`
- **extract_occupant_names()** (10 connections) — `server/realtime/player_event_handlers_respawn_room.py`
- **_RespawnRoomHost** (9 connections) — `server/realtime/player_event_handlers_respawn_room.py`
- **_host()** (9 connections) — `server/tests/unit/realtime/test_player_event_handlers_respawn_room.py`
- **player_event_handlers_respawn_types.py** (9 connections) — `server/realtime/player_event_handlers_respawn_types.py`
- **enrich_room_data_with_occupant_names()** (8 connections) — `server/realtime/player_event_handlers_respawn_room.py`
- **get_npc_name_from_lifecycle_manager()** (7 connections) — `server/realtime/player_event_handlers_respawn_room.py`
- **room_data_from_persistence_room()** (7 connections) — `server/realtime/player_event_handlers_respawn_room.py`
- **convert_npc_ids_to_names()** (6 connections) — `server/realtime/player_event_handlers_respawn_room.py`
- **get_npc_lifecycle_manager_from_connection_manager()** (6 connections) — `server/realtime/websocket_initial_state.py`
- **asyncio** (5 connections)
- **merge_player_lists()** (4 connections) — `server/realtime/player_event_handlers_respawn_room.py`
- **append_unique_valid_occupant()** (4 connections) — `server/realtime/player_event_handlers_respawn_types.py`
- **ensure_respawned_player_in_lists()** (4 connections) — `server/realtime/player_event_handlers_respawn_types.py`
- **is_npc_occupant_row()** (4 connections) — `server/realtime/player_event_handlers_respawn_types.py`
- **occupant_str_field()** (4 connections) — `server/realtime/player_event_handlers_respawn_types.py`
- **test_convert_npc_ids_to_names_resolves_lifecycle_and_short_ids()** (4 connections) — `server/tests/unit/realtime/test_player_event_handlers_respawn_room.py`
- **test_enrich_room_data_with_occupant_names()** (4 connections) — `server/tests/unit/realtime/test_player_event_handlers_respawn_room.py`
- **test_prepare_room_data_for_respawn_logs_on_error()** (4 connections) — `server/tests/unit/realtime/test_player_event_handlers_respawn_room.py`
- **test_prepare_room_data_for_respawn_no_connection_manager()** (4 connections) — `server/tests/unit/realtime/test_player_event_handlers_respawn_room.py`
- **test_prepare_room_data_for_respawn_with_connection_manager()** (4 connections) — `server/tests/unit/realtime/test_player_event_handlers_respawn_room.py`
- **test_get_container_async_persistence_raises_when_not_initialized()** (3 connections) — `server/tests/unit/infrastructure/test_async_persistence_delegates.py`
- *... and 28 more nodes in this community*

## Relationships

- [test_websocket_initial_state.py](test_websocket_initial_state.py.md) (7 shared connections)
- [Player](Player.md) (6 shared connections)
- [real_time.py](real_time.py.md) (3 shared connections)
- [ConnectionManager](ConnectionManager.md) (2 shared connections)
- [websocket_helpers.py](websocket_helpers.py.md) (2 shared connections)
- [test_websocket_helpers.py](test_websocket_helpers.py.md) (2 shared connections)
- [PlayerRespawnEventHandler](PlayerRespawnEventHandler.md) (2 shared connections)
- [CombatAttackHandler](CombatAttackHandler.md) (1 shared connections)
- [get_config](get_config.md) (1 shared connections)
- [async_persistence.py](async_persistence.py.md) (1 shared connections)
- [Protocol](Protocol.md) (1 shared connections)
- [Room](Room.md) (1 shared connections)

## Source Files

- `server/container/async_persistence_access.py`
- `server/realtime/player_event_handlers_respawn_room.py`
- `server/realtime/player_event_handlers_respawn_types.py`
- `server/realtime/websocket_initial_state.py`
- `server/tests/unit/infrastructure/test_async_persistence_delegates.py`
- `server/tests/unit/realtime/test_player_event_handlers_respawn_room.py`

## Audit Trail

- EXTRACTED: 124 (98%)
- INFERRED: 3 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*