# npc behavior engine

> 27 nodes

## Key Concepts

- **test_admin_summon_command.py** (33 connections) — `server/tests/unit/commands/test_admin_summon_command.py`
- **test_persist_summoned_item_swallows_db_error()** (2 connections) — `server/tests/unit/commands/test_admin_summon_command.py`
- **test_validate_summon_prerequisites_missing_item_services()** (1 connections) — `server/tests/unit/commands/test_admin_summon_command.py`
- **test_validate_summon_prerequisites_missing_room_manager()** (1 connections) — `server/tests/unit/commands/test_admin_summon_command.py`
- **test_validate_summon_prerequisites_ok()** (1 connections) — `server/tests/unit/commands/test_admin_summon_command.py`
- **test_summon_npc_stub_response()** (1 connections) — `server/tests/unit/commands/test_admin_summon_command.py`
- **test_summon_npc_stub_response_item_type()** (1 connections) — `server/tests/unit/commands/test_admin_summon_command.py`
- **test_create_summon_item_instance_success()** (1 connections) — `server/tests/unit/commands/test_admin_summon_command.py`
- **test_parse_summon_command_data_missing_prototype()** (1 connections) — `server/tests/unit/commands/test_admin_summon_command.py`
- **test_parse_summon_command_data_npc_stub()** (1 connections) — `server/tests/unit/commands/test_admin_summon_command.py`
- **test_parse_summon_command_data_item_ok()** (1 connections) — `server/tests/unit/commands/test_admin_summon_command.py`
- **test_persist_summoned_item_success()** (1 connections) — `server/tests/unit/commands/test_admin_summon_command.py`
- **test_parse_summon_command_data_quantity_spike()** (1 connections) — `server/tests/unit/commands/test_admin_summon_command.py`
- **test_parse_summon_command_data_room_manager_missing_at_execution()** (1 connections) — `server/tests/unit/commands/test_admin_summon_command.py`
- **test_complete_summon_success()** (1 connections) — `server/tests/unit/commands/test_admin_summon_command.py`
- **test_complete_summon_no_instance_without_error()** (1 connections) — `server/tests/unit/commands/test_admin_summon_command.py`
- **test_broadcast_and_log_summon_success()** (1 connections) — `server/tests/unit/commands/test_admin_summon_command.py`
- **test_handle_summon_command_success()** (1 connections) — `server/tests/unit/commands/test_admin_summon_command.py`
- **test_handle_summon_command_context_error()** (1 connections) — `server/tests/unit/commands/test_admin_summon_command.py`
- **test_handle_summon_command_parse_error()** (1 connections) — `server/tests/unit/commands/test_admin_summon_command.py`
- **test_resolve_summon_context_permission_denied()** (1 connections) — `server/tests/unit/commands/test_admin_summon_command.py`
- **test_validate_summon_prerequisites_room_manager_no_add_drop()** (1 connections) — `server/tests/unit/commands/test_admin_summon_command.py`
- **test_log_summon_success()** (1 connections) — `server/tests/unit/commands/test_admin_summon_command.py`
- **test_resolve_summon_context_success()** (1 connections) — `server/tests/unit/commands/test_admin_summon_command.py`
- **test_resolve_summon_context_player_error()** (1 connections) — `server/tests/unit/commands/test_admin_summon_command.py`
- *... and 2 more nodes in this community*

## Relationships

- [schedule service services](schedule_service_services.md) (4 shared connections)
- [endpoints auth rationale](endpoints_auth_rationale.md) (2 shared connections)
- [shutdown command commands](shutdown_command_commands.md) (1 shared connections)
- [Error Handling Core](Error_Handling_Core.md) (1 shared connections)

## Source Files

- `server/tests/unit/commands/test_admin_summon_command.py`

## Audit Trail

- EXTRACTED: 60 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*