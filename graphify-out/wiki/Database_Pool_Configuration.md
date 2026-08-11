# Database Pool Configuration

> 8 nodes

## Key Concepts

- **test_combat_messaging_integration.py** (32 connections) — `server/tests/unit/services/test_combat_messaging_integration.py`
- **test_messaging_integration_init_no_connection_manager()** (3 connections) — `server/tests/unit/services/test_combat_messaging_integration.py`
- **test_resolve_connection_manager_from_container_error()** (2 connections) — `server/tests/unit/services/test_combat_messaging_integration.py`
- **test_broadcast_player_mortally_wounded()** (2 connections) — `server/tests/unit/services/test_combat_messaging_integration.py`
- **Unit tests for combat messaging integration.  Tests the CombatMessagingIntegrati** (1 connections) — `server/tests/unit/services/test_combat_messaging_integration.py`
- **Test CombatMessagingIntegration initialization without connection manager.** (1 connections) — `server/tests/unit/services/test_combat_messaging_integration.py`
- **Test _resolve_connection_manager_from_container handles errors.** (1 connections) — `server/tests/unit/services/test_combat_messaging_integration.py`
- **Test broadcast_player_mortally_wounded broadcasts message.** (1 connections) — `server/tests/unit/services/test_combat_messaging_integration.py`

## Relationships

- [Archive Room Hierarchy](Archive_Room_Hierarchy.md) (1 shared connections)
- [test_movement_monitor_init](test_movement_monitor_init.md) (1 shared connections)
- [test_load_room_cache_async_rooms_none](test_load_room_cache_async_rooms_none.md) (1 shared connections)
- [test_build_room_objects_success](test_build_room_objects_success.md) (1 shared connections)
- [Testing Error Handling](Testing_Error_Handling.md) (1 shared connections)
- [test_process_exit_rows_debug_logging](test_process_exit_rows_debug_logging.md) (1 shared connections)
- [test_validate_room_integrity_calculates_occupancy](test_validate_room_integrity_calculates_occupancy.md) (1 shared connections)
- [Value Distribution](Value_Distribution.md) (1 shared connections)
- [test_record_movement_attempt_success](test_record_movement_attempt_success.md) (1 shared connections)
- [test_record_movement_attempt_multiple_players](test_record_movement_attempt_multiple_players.md) (1 shared connections)
- [test_process_exit_rows_with_full_room_ids](test_process_exit_rows_with_full_room_ids.md) (1 shared connections)
- [test_parse_exits_json_list](test_parse_exits_json_list.md) (1 shared connections)

## Source Files

- `server/tests/unit/services/test_combat_messaging_integration.py`

## Audit Trail

- EXTRACTED: 42 (98%)
- INFERRED: 1 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*