# room websocket updates

> 117 nodes

## Key Concepts

- **AttributeError** (37 connections)
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
- **test_warded_indicator_in_websocket_room_updates()** (4 connections) — `server/tests/unit/realtime/test_login_grace_period_visual_indicator.py`
- **test_get_player_occupants_handles_exception()** (4 connections) — `server/tests/unit/realtime/test_websocket_room_updates.py`
- **test_get_npc_occupants_from_lifecycle_manager_handles_exception()** (4 connections) — `server/tests/unit/realtime/test_websocket_room_updates.py`
- **test_broadcast_room_update_fallback_npc_method()** (4 connections) — `server/tests/unit/realtime/test_websocket_room_updates.py`
- **test_extract_parsed_fields_handles_missing_attributes()** (3 connections) — `server/tests/unit/commands/test_command_service.py`
- **test_handle_nats_message_connection_manager_resolution_error()** (3 connections) — `server/tests/unit/realtime/test_nats_message_handler.py`
- **test_handle_nats_message_attribute_error_handled()** (3 connections) — `server/tests/unit/realtime/test_nats_message_handler.py`
- **test_create_player_occupant_info_grace_period_exception()** (3 connections) — `server/tests/unit/realtime/test_player_occupant_processor.py`
- **test_get_room_occupants_get_players_error()** (3 connections) — `server/tests/unit/realtime/test_room_occupant_manager.py`
- **test_get_npc_name_from_instance_success()** (3 connections) — `server/tests/unit/realtime/test_websocket_helpers.py`
- *... and 92 more nodes in this community*

## Relationships

- [realtime websocket initial](realtime_websocket_initial.md) (8 shared connections)
- [Room Broadcast](Room_Broadcast.md) (6 shared connections)
- [room renderer functions](room_renderer_functions.md) (5 shared connections)
- [player occupant processor](player_occupant_processor.md) (5 shared connections)
- [commands npc admin](commands_npc_admin.md) (4 shared connections)
- [combat services messaging](combat_services_messaging.md) (4 shared connections)
- [command utility models](command_utility_models.md) (4 shared connections)
- [command inventory factories](command_inventory_factories.md) (3 shared connections)
- [auth rationale access](auth_rationale_access.md) (3 shared connections)
- [grace period disconnect](grace_period_disconnect.md) (3 shared connections)
- [room service sync](room_service_sync.md) (3 shared connections)
- [commands status rationale](commands_status_rationale.md) (2 shared connections)

## Source Files

- `server/realtime/websocket_helpers.py`
- `server/realtime/websocket_room_updates.py`
- `server/tests/unit/commands/test_command_service.py`
- `server/tests/unit/realtime/test_login_grace_period_visual_indicator.py`
- `server/tests/unit/realtime/test_nats_message_handler.py`
- `server/tests/unit/realtime/test_player_occupant_processor.py`
- `server/tests/unit/realtime/test_room_occupant_manager.py`
- `server/tests/unit/realtime/test_websocket_helpers.py`
- `server/tests/unit/realtime/test_websocket_room_updates.py`
- `server/tests/unit/realtime/test_websocket_room_updates_build_event.py`
- `server/tests/unit/services/test_npc_combat_integration_service_player_attacks.py`
- `server/tests/unit/services/test_npc_instance_service.py`
- `server/tests/unit/services/test_room_sync_service.py`
- `server/tests/unit/utils/test_command_processor.py`

## Audit Trail

- EXTRACTED: 361 (87%)
- INFERRED: 52 (13%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*