# test_room_system_message_categories.py

> 52 nodes · cohesion 0.08

## Key Concepts

- **player_event_handlers_respawn_room.py** (28 connections) — `server/realtime/player_event_handlers_respawn_room.py`
- **player_event_handlers_respawn_types.py** (15 connections) — `server/realtime/player_event_handlers_respawn_types.py`
- **test_player_event_handlers_respawn_room.py** (15 connections) — `server/tests/unit/realtime/test_player_event_handlers_respawn_room.py`
- **extract_occupant_names()** (13 connections) — `server/realtime/player_event_handlers_respawn_room.py`
- **prepare_room_data_for_respawn()** (12 connections) — `server/realtime/player_event_handlers_respawn_room.py`
- **convert_npc_ids_to_names()** (10 connections) — `server/realtime/player_event_handlers_respawn_room.py`
- **enrich_room_data_with_occupant_names()** (9 connections) — `server/realtime/player_event_handlers_respawn_room.py`
- **_RespawnRoomHost** (9 connections) — `server/realtime/player_event_handlers_respawn_room.py`
- **append_unique_npc_occupant()** (9 connections) — `server/realtime/player_event_handlers_respawn_types.py`
- **_host()** (9 connections) — `server/tests/unit/realtime/test_player_event_handlers_respawn_room.py`
- **room_data_from_persistence_room()** (8 connections) — `server/realtime/player_event_handlers_respawn_room.py`
- **get_npc_name_from_lifecycle_manager()** (7 connections) — `server/realtime/player_event_handlers_respawn_room.py`
- **get_npc_lifecycle_manager_from_connection_manager()** (6 connections) — `server/realtime/websocket_initial_state.py`
- **NpcOccupant** (5 connections)
- **asyncio** (5 connections)
- **test_convert_npc_ids_to_names_resolves_lifecycle_and_short_ids()** (5 connections) — `server/tests/unit/realtime/test_player_event_handlers_respawn_room.py`
- **test_enrich_room_data_with_occupant_names()** (5 connections) — `server/tests/unit/realtime/test_player_event_handlers_respawn_room.py`
- **merge_player_lists()** (4 connections) — `server/realtime/player_event_handlers_respawn_room.py`
- **append_unique_valid_occupant()** (4 connections) — `server/realtime/player_event_handlers_respawn_types.py`
- **ensure_respawned_player_in_lists()** (4 connections) — `server/realtime/player_event_handlers_respawn_types.py`
- **is_npc_occupant_row()** (4 connections) — `server/realtime/player_event_handlers_respawn_types.py`
- **occupant_str_field()** (4 connections) — `server/realtime/player_event_handlers_respawn_types.py`
- **test_prepare_room_data_for_respawn_logs_on_error()** (4 connections) — `server/tests/unit/realtime/test_player_event_handlers_respawn_room.py`
- **test_prepare_room_data_for_respawn_no_connection_manager()** (4 connections) — `server/tests/unit/realtime/test_player_event_handlers_respawn_room.py`
- **test_prepare_room_data_for_respawn_with_connection_manager()** (4 connections) — `server/tests/unit/realtime/test_player_event_handlers_respawn_room.py`
- *... and 27 more nodes in this community*

## Relationships

- [look_container.py](look_container.py.md) (10 shared connections)
- [is_player_in_login_grace_period](is_player_in_login_grace_period.md) (7 shared connections)
- [alias_storage.py](alias_storage.py.md) (6 shared connections)
- [test_game.py](test_game.py.md) (4 shared connections)
- [ChatService](ChatService.md) (2 shared connections)
- [session](session.md) (2 shared connections)
- [asyncio](asyncio.md) (2 shared connections)
- [test_combat_monitoring_service.py](test_combat_monitoring_service.py.md) (1 shared connections)
- [BaseEvent](BaseEvent.md) (1 shared connections)
- [connection_initialization.py](connection_initialization.py.md) (1 shared connections)

## Source Files

- `server/realtime/player_event_handlers_respawn_room.py`
- `server/realtime/player_event_handlers_respawn_types.py`
- `server/realtime/websocket_initial_state.py`
- `server/tests/unit/realtime/test_player_event_handlers_respawn_room.py`

## Audit Trail

- EXTRACTED: 128 (93%)
- INFERRED: 9 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*