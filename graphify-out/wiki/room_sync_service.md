# room sync service

> 27 nodes

## Key Concepts

- **AttributeError** (45 connections)
- **test_handle_nats_message_connection_manager_resolution_error()** (3 connections) — `server/tests/unit/realtime/test_nats_message_handler.py`
- **test_handle_nats_message_attribute_error_handled()** (3 connections) — `server/tests/unit/realtime/test_nats_message_handler.py`
- **test_create_player_occupant_info_grace_period_exception()** (3 connections) — `server/tests/unit/realtime/test_player_occupant_processor.py`
- **test_get_room_occupants_get_players_error()** (3 connections) — `server/tests/unit/realtime/test_room_occupant_manager.py`
- **test_persist_player_dp_sync_get_stats_error()** (3 connections) — `server/tests/unit/services/test_combat_persistence_handler_persistence.py`
- **test_persist_player_dp_sync_get_stats_error_new()** (3 connections) — `server/tests/unit/services/test_combat_persistence_handler_persistence.py`
- **test_handle_player_attack_on_npc_grace_period_check_fails()** (3 connections) — `server/tests/unit/services/test_npc_combat_integration_service_player_attacks.py`
- **test_get_npc_instances_get_stats_exception()** (3 connections) — `server/tests/unit/services/test_npc_instance_service.py`
- **test_process_room_update_with_validation_handles_error()** (3 connections) — `server/tests/unit/services/test_room_sync_service.py`
- **test_invalidate_stale_cache_error()** (3 connections) — `server/tests/unit/services/test_room_sync_service.py`
- **test_fetch_fresh_room_data_handles_error()** (3 connections) — `server/tests/unit/services/test_room_sync_service.py`
- **test_process_command_string_attribute_error()** (3 connections) — `server/tests/unit/utils/test_command_processor.py`
- **test_get_command_help_attribute_error()** (3 connections) — `server/tests/unit/utils/test_command_processor.py`
- **Test _handle_nats_message handles connection manager resolution errors.** (1 connections) — `server/tests/unit/realtime/test_nats_message_handler.py`
- **Test _handle_nats_message handles AttributeError and adds to DLQ.** (1 connections) — `server/tests/unit/realtime/test_nats_message_handler.py`
- **Test _create_player_occupant_info handles grace period check exceptions.** (1 connections) — `server/tests/unit/realtime/test_player_occupant_processor.py`
- **Test get_room_occupants handles get_players error.** (1 connections) — `server/tests/unit/realtime/test_room_occupant_manager.py`
- **Test _persist_player_dp_sync handles get_stats error.** (1 connections) — `server/tests/unit/services/test_combat_persistence_handler_persistence.py`
- **Test _persist_player_dp_sync handles get_stats error gracefully.** (1 connections) — `server/tests/unit/services/test_combat_persistence_handler_persistence.py`
- **Test handle_player_attack_on_npc continues when grace period check fails.** (1 connections) — `server/tests/unit/services/test_npc_combat_integration_service_player_attacks.py`
- **Test get_npc_instances() handles exception from get_stats.** (1 connections) — `server/tests/unit/services/test_npc_instance_service.py`
- **Test _process_room_update_with_validation() handles errors gracefully.** (1 connections) — `server/tests/unit/services/test_room_sync_service.py`
- **Test _invalidate_stale_cache() handles errors gracefully.** (1 connections) — `server/tests/unit/services/test_room_sync_service.py`
- **Test _fetch_fresh_room_data() handles errors.** (1 connections) — `server/tests/unit/services/test_room_sync_service.py`
- *... and 2 more nodes in this community*

## Relationships

- [websocket handler realtime](websocket_handler_realtime.md) (3 shared connections)
- [command models moderation](command_models_moderation.md) (3 shared connections)
- [inventory mutation guard](inventory_mutation_guard.md) (3 shared connections)
- [commands status rationale](commands_status_rationale.md) (2 shared connections)
- [message handler factory](message_handler_factory.md) (2 shared connections)
- [realtime connection helpers](realtime_connection_helpers.md) (2 shared connections)
- [nats message handler](nats_message_handler.md) (2 shared connections)
- [message queue realtime](message_queue_realtime.md) (2 shared connections)
- [command processor rationale](command_processor_rationale.md) (2 shared connections)
- [Magic Spell Service](Magic_Spell_Service.md) (1 shared connections)
- [circuit breaker realtime](circuit_breaker_realtime.md) (1 shared connections)
- [lucidity npc combat](lucidity_npc_combat.md) (1 shared connections)

## Source Files

- `server/tests/unit/realtime/test_nats_message_handler.py`
- `server/tests/unit/realtime/test_player_occupant_processor.py`
- `server/tests/unit/realtime/test_room_occupant_manager.py`
- `server/tests/unit/services/test_combat_persistence_handler_persistence.py`
- `server/tests/unit/services/test_npc_combat_integration_service_player_attacks.py`
- `server/tests/unit/services/test_npc_instance_service.py`
- `server/tests/unit/services/test_room_sync_service.py`
- `server/tests/unit/utils/test_command_processor.py`

## Audit Trail

- EXTRACTED: 40 (41%)
- INFERRED: 57 (59%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*