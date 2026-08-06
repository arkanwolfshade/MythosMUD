# command models moderation

> 80 nodes

## Key Concepts

- **websocket_room_updates.py** (36 connections) — `server/realtime/websocket_room_updates.py`
- **test_websocket_room_updates.py** (32 connections) — `server/tests/unit/realtime/test_websocket_room_updates.py`
- **broadcast_room_update()** (26 connections) — `server/realtime/websocket_room_updates.py`
- **build_room_update_event()** (13 connections) — `server/realtime/websocket_room_updates.py`
- **get_npc_name_from_instance()** (12 connections) — `server/realtime/websocket_helpers.py`
- **get_player_occupants()** (11 connections) — `server/realtime/websocket_room_updates.py`
- **get_npc_occupants_from_lifecycle_manager()** (11 connections) — `server/realtime/websocket_room_updates.py`
- **get_npc_occupants_fallback()** (9 connections) — `server/realtime/websocket_room_updates.py`
- **update_player_room_subscription()** (8 connections) — `server/realtime/websocket_room_updates.py`
- **UUID** (6 connections)
- **_decorate_occupant_name()** (6 connections) — `server/realtime/websocket_room_updates.py`
- **test_websocket_room_updates_build_event.py** (6 connections) — `server/tests/unit/realtime/test_websocket_room_updates_build_event.py`
- **_resolve_room_with_fallback()** (5 connections) — `server/realtime/websocket_room_updates.py`
- **_parse_occupant_player_id()** (4 connections) — `server/realtime/websocket_room_updates.py`
- **test_get_player_occupants_handles_exception()** (4 connections) — `server/tests/unit/realtime/test_websocket_room_updates.py`
- **test_get_npc_occupants_from_lifecycle_manager_handles_exception()** (4 connections) — `server/tests/unit/realtime/test_websocket_room_updates.py`
- **test_broadcast_room_update_fallback_npc_method()** (4 connections) — `server/tests/unit/realtime/test_websocket_room_updates.py`
- **test_get_player_occupants_success()** (3 connections) — `server/tests/unit/realtime/test_websocket_room_updates.py`
- **test_get_player_occupants_empty()** (3 connections) — `server/tests/unit/realtime/test_websocket_room_updates.py`
- **test_get_npc_occupants_from_lifecycle_manager_success()** (3 connections) — `server/tests/unit/realtime/test_websocket_room_updates.py`
- **test_get_npc_occupants_from_lifecycle_manager_filters_dead()** (3 connections) — `server/tests/unit/realtime/test_websocket_room_updates.py`
- **test_get_npc_occupants_from_lifecycle_manager_wrong_room()** (3 connections) — `server/tests/unit/realtime/test_websocket_room_updates.py`
- **test_get_npc_occupants_from_lifecycle_manager_no_service()** (3 connections) — `server/tests/unit/realtime/test_websocket_room_updates.py`
- **test_get_npc_occupants_fallback_success()** (3 connections) — `server/tests/unit/realtime/test_websocket_room_updates.py`
- **test_get_npc_occupants_fallback_filters_dead()** (3 connections) — `server/tests/unit/realtime/test_websocket_room_updates.py`
- *... and 55 more nodes in this community*

## Relationships

- [room websocket updates](room_websocket_updates.md) (8 shared connections)
- [command utility models](command_utility_models.md) (6 shared connections)
- [player service game](player_service_game.md) (5 shared connections)
- [commands npc admin](commands_npc_admin.md) (4 shared connections)
- [Error Conversion](Error_Conversion.md) (4 shared connections)
- [combat services messaging](combat_services_messaging.md) (4 shared connections)
- [npc combat base](npc_combat_base.md) (3 shared connections)
- [room sync service](room_sync_service.md) (3 shared connections)
- [realtime maintenance connection](realtime_maintenance_connection.md) (2 shared connections)
- [command commands aliases](command_commands_aliases.md) (2 shared connections)
- [player room event](player_room_event.md) (2 shared connections)
- [follow game service](follow_game_service.md) (2 shared connections)

## Source Files

- `server/realtime/websocket_helpers.py`
- `server/realtime/websocket_room_updates.py`
- `server/tests/unit/realtime/test_websocket_room_updates.py`
- `server/tests/unit/realtime/test_websocket_room_updates_build_event.py`

## Audit Trail

- EXTRACTED: 299 (99%)
- INFERRED: 4 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*