# websocket helpers realtime

> 31 nodes

## Key Concepts

- **AttributeError** (45 connections)
- **test_decode_access_token_attribute_error()** (5 connections) — `server/tests/unit/auth/test_auth_utils.py`
- **test_extract_parsed_fields_handles_missing_attributes()** (3 connections) — `server/tests/unit/commands/test_command_service.py`
- **test_apply_combat_effects_attribute_error_raises()** (3 connections) — `server/tests/unit/npc/test_combat_integration_base.py`
- **test_handle_nats_message_connection_manager_resolution_error()** (3 connections) — `server/tests/unit/realtime/test_nats_message_handler.py`
- **test_handle_nats_message_attribute_error_handled()** (3 connections) — `server/tests/unit/realtime/test_nats_message_handler.py`
- **test_create_player_occupant_info_grace_period_exception()** (3 connections) — `server/tests/unit/realtime/test_player_occupant_processor.py`
- **test_persist_player_dp_sync_get_stats_error()** (3 connections) — `server/tests/unit/services/test_combat_persistence_handler_persistence.py`
- **test_persist_player_dp_sync_get_stats_error_new()** (3 connections) — `server/tests/unit/services/test_combat_persistence_handler_persistence.py`
- **test_handle_player_attack_on_npc_grace_period_check_fails()** (3 connections) — `server/tests/unit/services/test_npc_combat_integration_service_player_attacks.py`
- **test_get_npc_instances_get_stats_exception()** (3 connections) — `server/tests/unit/services/test_npc_instance_service.py`
- **test_process_room_update_with_validation_handles_error()** (3 connections) — `server/tests/unit/services/test_room_sync_service.py`
- **test_invalidate_stale_cache_error()** (3 connections) — `server/tests/unit/services/test_room_sync_service.py`
- **test_fetch_fresh_room_data_handles_error()** (3 connections) — `server/tests/unit/services/test_room_sync_service.py`
- **test_process_command_string_attribute_error()** (3 connections) — `server/tests/unit/utils/test_command_processor.py`
- **test_get_command_help_attribute_error()** (3 connections) — `server/tests/unit/utils/test_command_processor.py`
- **.is_admin()** (2 connections) — `server/tests/unit/commands/test_admin_permission_utils.py`
- **Test decode_access_token handles AttributeError and returns None.** (1 connections) — `server/tests/unit/auth/test_auth_utils.py`
- **Test _extract_parsed_fields handles missing attributes gracefully.** (1 connections) — `server/tests/unit/commands/test_command_service.py`
- **Test _handle_nats_message handles connection manager resolution errors.** (1 connections) — `server/tests/unit/realtime/test_nats_message_handler.py`
- **Test _handle_nats_message handles AttributeError and adds to DLQ.** (1 connections) — `server/tests/unit/realtime/test_nats_message_handler.py`
- **Test _create_player_occupant_info handles grace period check exceptions.** (1 connections) — `server/tests/unit/realtime/test_player_occupant_processor.py`
- **Test _persist_player_dp_sync handles get_stats error.** (1 connections) — `server/tests/unit/services/test_combat_persistence_handler_persistence.py`
- **Test _persist_player_dp_sync handles get_stats error gracefully.** (1 connections) — `server/tests/unit/services/test_combat_persistence_handler_persistence.py`
- **Test handle_player_attack_on_npc continues when grace period check fails.** (1 connections) — `server/tests/unit/services/test_npc_combat_integration_service_player_attacks.py`
- *... and 6 more nodes in this community*

## Relationships

- [npc lifecycle combat](npc_lifecycle_combat.md) (5 shared connections)
- [command models moderation](command_models_moderation.md) (3 shared connections)
- [room service sync](room_service_sync.md) (3 shared connections)
- [commands status rationale](commands_status_rationale.md) (2 shared connections)
- [realtime message filtering](realtime_message_filtering.md) (2 shared connections)
- [realtime connection helpers](realtime_connection_helpers.md) (2 shared connections)
- [services nats service](services_nats_service.md) (2 shared connections)
- [nats message handler](nats_message_handler.md) (2 shared connections)
- [persistence combat services](persistence_combat_services.md) (2 shared connections)
- [command processor rationale](command_processor_rationale.md) (2 shared connections)
- [room cache services](room_cache_services.md) (1 shared connections)
- [npc combat base](npc_combat_base.md) (1 shared connections)

## Source Files

- `server/tests/unit/auth/test_auth_utils.py`
- `server/tests/unit/commands/test_admin_permission_utils.py`
- `server/tests/unit/commands/test_command_service.py`
- `server/tests/unit/npc/test_combat_integration_base.py`
- `server/tests/unit/realtime/test_nats_message_handler.py`
- `server/tests/unit/realtime/test_player_occupant_processor.py`
- `server/tests/unit/services/test_combat_persistence_handler_persistence.py`
- `server/tests/unit/services/test_npc_combat_integration_service_player_attacks.py`
- `server/tests/unit/services/test_npc_instance_service.py`
- `server/tests/unit/services/test_room_sync_service.py`
- `server/tests/unit/utils/test_command_processor.py`

## Audit Trail

- EXTRACTED: 48 (44%)
- INFERRED: 60 (56%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*