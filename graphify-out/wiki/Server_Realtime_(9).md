# Server Realtime (9)

> 109 nodes

## Key Concepts

- **test_websocket_helpers.py** (34 connections) — `server/tests/unit/realtime/test_websocket_helpers.py`
- **websocket_room_updates.py** (32 connections) — `server/realtime/websocket_room_updates.py`
- **test_websocket_room_updates.py** (32 connections) — `server/tests/unit/realtime/test_websocket_room_updates.py`
- **broadcast_room_update()** (23 connections) — `server/realtime/websocket_room_updates.py`
- **validate_occupant_name()** (14 connections) — `server/realtime/websocket_helpers.py`
- **build_room_update_event()** (13 connections) — `server/realtime/websocket_room_updates.py`
- **get_npc_name_from_instance()** (12 connections) — `server/realtime/websocket_helpers.py`
- **convert_uuids_to_strings()** (11 connections) — `server/realtime/websocket_helpers.py`
- **get_npc_occupants_from_lifecycle_manager()** (11 connections) — `server/realtime/websocket_room_updates.py`
- **get_npc_occupants_fallback()** (9 connections) — `server/realtime/websocket_room_updates.py`
- **load_player_mute_data()** (7 connections) — `server/realtime/websocket_helpers.py`
- **update_player_room_subscription()** (7 connections) — `server/realtime/websocket_room_updates.py`
- **test_websocket_room_updates_build_event.py** (6 connections) — `server/tests/unit/realtime/test_websocket_room_updates_build_event.py`
- **_resolve_room_with_fallback()** (4 connections) — `server/realtime/websocket_room_updates.py`
- **Test validate_occupant_name() returns False for UUID string.** (4 connections) — `server/tests/unit/realtime/test_websocket_helpers.py`
- **test_get_npc_occupants_from_lifecycle_manager_handles_exception()** (4 connections) — `server/tests/unit/realtime/test_websocket_room_updates.py`
- **test_broadcast_room_update_fallback_npc_method()** (4 connections) — `server/tests/unit/realtime/test_websocket_room_updates.py`
- **test_get_npc_name_from_instance_success()** (3 connections) — `server/tests/unit/realtime/test_websocket_helpers.py`
- **test_get_npc_name_from_instance_not_found()** (3 connections) — `server/tests/unit/realtime/test_websocket_helpers.py`
- **test_get_npc_name_from_instance_no_name_attribute()** (3 connections) — `server/tests/unit/realtime/test_websocket_helpers.py`
- **test_get_npc_name_from_instance_import_error()** (3 connections) — `server/tests/unit/realtime/test_websocket_helpers.py`
- **test_get_npc_name_from_instance_runtime_error()** (3 connections) — `server/tests/unit/realtime/test_websocket_helpers.py`
- **test_load_player_mute_data_success()** (3 connections) — `server/tests/unit/realtime/test_websocket_helpers.py`
- **test_load_player_mute_data_import_error()** (3 connections) — `server/tests/unit/realtime/test_websocket_helpers.py`
- **test_validate_occupant_name_valid()** (3 connections) — `server/tests/unit/realtime/test_websocket_helpers.py`
- *... and 84 more nodes in this community*

## Relationships

- [Server Realtime (21)](Server_Realtime_%2821%29.md) (14 shared connections)
- [Server Realtime (6)](Server_Realtime_%286%29.md) (10 shared connections)
- [Server Realtime (8)](Server_Realtime_%288%29.md) (8 shared connections)
- [Server Realtime (2)](Server_Realtime_%282%29.md) (6 shared connections)
- [Server Npc](Server_Npc.md) (5 shared connections)
- [Server Utils (8)](Server_Utils_%288%29.md) (5 shared connections)
- [Server Realtime (13)](Server_Realtime_%2813%29.md) (3 shared connections)
- [Server Services (35)](Server_Services_%2835%29.md) (3 shared connections)
- [Server Realtime (24)](Server_Realtime_%2824%29.md) (2 shared connections)
- [Server Commands](Server_Commands.md) (2 shared connections)
- [Server App](Server_App.md) (2 shared connections)
- [Server Services (4)](Server_Services_%284%29.md) (2 shared connections)

## Source Files

- `server/realtime/websocket_helpers.py`
- `server/realtime/websocket_room_updates.py`
- `server/tests/unit/realtime/test_websocket_helpers.py`
- `server/tests/unit/realtime/test_websocket_room_updates.py`
- `server/tests/unit/realtime/test_websocket_room_updates_build_event.py`

## Audit Trail

- EXTRACTED: 398 (99%)
- INFERRED: 3 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*