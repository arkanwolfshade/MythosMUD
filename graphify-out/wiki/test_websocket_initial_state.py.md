# test_websocket_initial_state.py

> 152 nodes

## Key Concepts

- **test_websocket_initial_state.py** (47 connections) — `server/tests/unit/realtime/test_websocket_initial_state.py`
- **websocket_initial_state.py** (46 connections) — `server/realtime/websocket_initial_state.py`
- **player_event_handlers_respawn_room.py** (23 connections) — `server/realtime/player_event_handlers_respawn_room.py`
- **asyncio** (21 connections)
- **get_container_async_persistence()** (19 connections) — `server/async_persistence.py`
- **send_initial_room_state()** (19 connections) — `server/realtime/websocket_initial_state.py`
- **send_initial_game_state()** (15 connections) — `server/realtime/websocket_initial_state.py`
- **validate_occupant_name()** (14 connections) — `server/realtime/websocket_helpers.py`
- **check_and_send_death_notification()** (14 connections) — `server/realtime/websocket_initial_state.py`
- **RespawnPlayerEventPayload** (13 connections) — `server/realtime/player_event_handlers_respawn_types.py`
- **prepare_player_data()** (12 connections) — `server/realtime/websocket_helpers.py`
- **convert_uuids_to_strings()** (11 connections) — `server/realtime/websocket_helpers.py`
- **get_occupant_names()** (11 connections) — `server/realtime/websocket_helpers.py`
- **send_game_state_event_safely()** (10 connections) — `server/realtime/websocket_initial_state.py`
- **_RespawnRoomHost** (9 connections) — `server/realtime/player_event_handlers_respawn_room.py`
- **extract_occupant_names()** (9 connections) — `server/realtime/player_event_handlers_respawn_room.py`
- **get_event_handler_for_initial_state()** (9 connections) — `server/realtime/websocket_initial_state.py`
- **prepare_room_data_with_occupants()** (9 connections) — `server/realtime/websocket_initial_state.py`
- **player_event_handlers_respawn_types.py** (9 connections) — `server/realtime/player_event_handlers_respawn_types.py`
- **add_npc_occupants_to_list()** (8 connections) — `server/realtime/websocket_initial_state.py`
- **send_occupants_snapshot_if_needed()** (8 connections) — `server/realtime/websocket_initial_state.py`
- **enrich_room_data_with_occupant_names()** (7 connections) — `server/realtime/player_event_handlers_respawn_room.py`
- **prepare_room_data_for_respawn()** (7 connections) — `server/realtime/player_event_handlers_respawn_room.py`
- **Protocol** (7 connections)
- **room_data_from_persistence_room()** (6 connections) — `server/realtime/player_event_handlers_respawn_room.py`
- *... and 127 more nodes in this community*

## Relationships

- [websocket_handler.py](websocket_handler.py.md) (21 shared connections)
- [websocket_helpers.py](websocket_helpers.py.md) (17 shared connections)
- [PlayerRespawnEventHandler](PlayerRespawnEventHandler.md) (10 shared connections)
- [PlayerEnteredRoom](PlayerEnteredRoom.md) (6 shared connections)
- [Player](Player.md) (6 shared connections)
- [ConnectionManager](ConnectionManager.md) (5 shared connections)
- [build_event](build_event.md) (5 shared connections)
- [get_logger](get_logger.md) (5 shared connections)
- [AsyncPersistenceLayer](AsyncPersistenceLayer.md) (4 shared connections)
- [event_types.py](event_types.py.md) (4 shared connections)
- [Room](Room.md) (4 shared connections)
- [real_time.py](real_time.py.md) (3 shared connections)

## Source Files

- `server/async_persistence.py`
- `server/realtime/player_event_handlers_respawn_room.py`
- `server/realtime/player_event_handlers_respawn_types.py`
- `server/realtime/websocket_helpers.py`
- `server/realtime/websocket_initial_state.py`
- `server/tests/unit/realtime/test_websocket_initial_state.py`

## Audit Trail

- EXTRACTED: 364 (97%)
- INFERRED: 11 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*