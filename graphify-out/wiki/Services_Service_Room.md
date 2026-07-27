# Services Service Room

> 16 nodes · cohesion 0.12

## Key Concepts

- **AttributeError** (39 connections) — `server/npc/combat_integration_base.py`
- **test_handle_status_command_error_handling()** (4 connections) — `server/tests/unit/commands/test_status_commands.py`
- **test_create_player_occupant_info_grace_period_exception()** (3 connections) — `server/tests/unit/realtime/test_player_occupant_processor.py`
- **test_persist_player_dp_sync_get_stats_error()** (3 connections) — `server/tests/unit/services/test_combat_persistence_handler_persistence.py`
- **test_get_npc_instances_get_stats_exception()** (3 connections) — `server/tests/unit/services/test_npc_instance_service.py`
- **.test_apply_room_data_fixes_exception_handling()** (3 connections) — `server/tests/unit/services/test_room_data_fixer.py`
- **test_fetch_fresh_room_data_handles_error()** (3 connections) — `server/tests/unit/services/test_room_sync_service.py`
- **test_invalidate_stale_cache_error()** (3 connections) — `server/tests/unit/services/test_room_sync_service.py`
- **test_process_room_update_with_validation_handles_error()** (3 connections) — `server/tests/unit/services/test_room_sync_service.py`
- **Test _create_player_occupant_info handles grace period check exceptions.** (1 connections) — `server/tests/unit/realtime/test_player_occupant_processor.py`
- **Test _persist_player_dp_sync handles get_stats error.** (1 connections) — `server/tests/unit/services/test_combat_persistence_handler_persistence.py`
- **Test get_npc_instances() handles exception from get_stats.** (1 connections) — `server/tests/unit/services/test_npc_instance_service.py`
- **Test apply_room_data_fixes handles exceptions.** (1 connections) — `server/tests/unit/services/test_room_data_fixer.py`
- **Test _process_room_update_with_validation() handles errors gracefully.** (1 connections) — `server/tests/unit/services/test_room_sync_service.py`
- **Test _invalidate_stale_cache() handles errors gracefully.** (1 connections) — `server/tests/unit/services/test_room_sync_service.py`
- **Test _fetch_fresh_room_data() handles errors.** (1 connections) — `server/tests/unit/services/test_room_sync_service.py`

## Relationships

- [[Auth Token Utilities]] (3 shared connections)
- [[Status Command Handlers]] (3 shared connections)
- [[Look Command Helpers]] (3 shared connections)
- [[Room Sync Service]] (3 shared connections)
- [[Game Mechanics Service]] (2 shared connections)
- [[Room Occupant Events]] (2 shared connections)
- [[Realtime Connection Event]] (2 shared connections)
- [[Realtime Connection Impl]] (2 shared connections)
- [[NATS Message Handler Tests]] (2 shared connections)
- [[Combat DP Persistence Tests]] (2 shared connections)
- [[Command Processor Tests]] (2 shared connections)
- [[Memory Leak Metrics]] (1 shared connections)

## Source Files

- `server/npc/combat_integration_base.py`
- `server/tests/unit/commands/test_status_commands.py`
- `server/tests/unit/realtime/test_player_occupant_processor.py`
- `server/tests/unit/services/test_combat_persistence_handler_persistence.py`
- `server/tests/unit/services/test_npc_instance_service.py`
- `server/tests/unit/services/test_room_data_fixer.py`
- `server/tests/unit/services/test_room_sync_service.py`

## Audit Trail

- EXTRACTED: 25 (35%)
- INFERRED: 46 (65%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
