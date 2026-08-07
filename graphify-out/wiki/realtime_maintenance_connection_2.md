# realtime maintenance connection

> 144 nodes

## Key Concepts

- **websocket_initial_state.py** (45 connections) — `server/realtime/websocket_initial_state.py`
- **test_websocket_helpers.py** (41 connections) — `server/tests/unit/realtime/test_websocket_helpers.py`
- **websocket_helpers.py** (38 connections) — `server/realtime/websocket_helpers.py`
- **test_websocket_helpers_player.py** (23 connections) — `server/tests/unit/realtime/test_websocket_helpers_player.py`
- **send_initial_game_state()** (15 connections) — `server/realtime/websocket_initial_state.py`
- **validate_occupant_name()** (14 connections) — `server/realtime/websocket_helpers.py`
- **get_player_and_room()** (14 connections) — `server/realtime/websocket_helpers.py`
- **check_shutdown_and_reject()** (12 connections) — `server/realtime/websocket_helpers.py`
- **prepare_player_data()** (12 connections) — `server/realtime/websocket_helpers.py`
- **get_occupant_names()** (11 connections) — `server/realtime/websocket_helpers.py`
- **convert_uuids_to_strings()** (11 connections) — `server/realtime/websocket_helpers.py`
- **is_client_disconnected_exception()** (9 connections) — `server/realtime/websocket_helpers.py`
- **get_player_service_from_connection_manager()** (9 connections) — `server/realtime/websocket_helpers.py`
- **get_player_stats_data()** (9 connections) — `server/realtime/websocket_helpers.py`
- **prepare_room_data_with_occupants()** (9 connections) — `server/realtime/websocket_initial_state.py`
- **get_npc_lifecycle_manager_from_connection_manager()** (8 connections) — `server/realtime/websocket_initial_state.py`
- **load_player_mute_data()** (7 connections) — `server/realtime/websocket_helpers.py`
- **convert_schema_to_dict()** (7 connections) — `server/realtime/websocket_helpers.py`
- **build_basic_player_data()** (7 connections) — `server/realtime/websocket_helpers.py`
- **Protocol** (7 connections)
- **_AppWithState** (7 connections) — `server/realtime/websocket_initial_state.py`
- **UUID** (6 connections)
- **_ensure_player_in_room_occupancy()** (6 connections) — `server/realtime/websocket_helpers.py`
- **_AppStateForEventHandler** (6 connections) — `server/realtime/websocket_initial_state.py`
- **_NpcLifecycleManagerForOccupants** (6 connections) — `server/realtime/websocket_initial_state.py`
- *... and 119 more nodes in this community*

## Relationships

- [realtime websocket initial](realtime_websocket_initial.md) (24 shared connections)
- [occupant formatter realtime](occupant_formatter_realtime.md) (16 shared connections)
- [command models moderation](command_models_moderation.md) (10 shared connections)
- [Room Broadcast](Room_Broadcast.md) (9 shared connections)
- [inventory mutation guard](inventory_mutation_guard.md) (9 shared connections)
- [logging examples fastapi](logging_examples_fastapi.md) (7 shared connections)
- [NATS Messaging](NATS_Messaging.md) (6 shared connections)
- [player room realtime](player_room_realtime.md) (4 shared connections)
- [websocket helpers realtime](websocket_helpers_realtime.md) (3 shared connections)
- [game weapon player](game_weapon_player.md) (3 shared connections)
- [alias storage rationale](alias_storage_rationale.md) (3 shared connections)
- [eventLog projectorRoom roomMergeUtils](eventLog_projectorRoom_roomMergeUtils.md) (2 shared connections)

## Source Files

- `server/models/alias.py`
- `server/realtime/websocket_helpers.py`
- `server/realtime/websocket_initial_state.py`
- `server/tests/unit/realtime/test_websocket_helpers.py`
- `server/tests/unit/realtime/test_websocket_helpers_player.py`

## Audit Trail

- EXTRACTED: 535 (94%)
- INFERRED: 32 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*