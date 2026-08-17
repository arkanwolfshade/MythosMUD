# server commands admin summon command

> 51 nodes

## Key Concepts

- **test_admin_summon_command.py** (34 connections) — `server/tests/unit/commands/test_admin_summon_command.py`
- **_resolve_summon_context()** (15 connections) — `server/commands/admin_summon_command.py`
- **handle_summon_command()** (13 connections) — `server/commands/admin_summon_command.py`
- **asyncio** (13 connections)
- **_complete_summon()** (10 connections) — `server/commands/admin_summon_command.py`
- **_parse_summon_command_data()** (10 connections) — `server/commands/admin_summon_command.py`
- **Any** (10 connections)
- **_broadcast_and_log_summon_success()** (8 connections) — `server/commands/admin_summon_command.py`
- **_validate_summon_prerequisites()** (8 connections) — `server/commands/admin_summon_command.py`
- **_create_summon_item_instance()** (6 connections) — `server/commands/admin_summon_command.py`
- **_persist_summoned_item()** (6 connections) — `server/commands/admin_summon_command.py`
- **_summon_npc_stub_response()** (6 connections) — `server/commands/admin_summon_command.py`
- **_log_summon_success()** (5 connections) — `server/commands/admin_summon_command.py`
- **test_complete_summon_factory_error()** (4 connections) — `server/tests/unit/commands/test_admin_summon_command.py`
- **test_persist_summoned_item_swallows_db_error()** (4 connections) — `server/tests/unit/commands/test_admin_summon_command.py`
- **test_broadcast_and_log_summon_success()** (3 connections) — `server/tests/unit/commands/test_admin_summon_command.py`
- **test_complete_summon_no_instance_without_error()** (3 connections) — `server/tests/unit/commands/test_admin_summon_command.py`
- **test_complete_summon_success()** (3 connections) — `server/tests/unit/commands/test_admin_summon_command.py`
- **test_create_summon_item_instance_factory_error()** (3 connections) — `server/tests/unit/commands/test_admin_summon_command.py`
- **test_handle_summon_command_context_error()** (3 connections) — `server/tests/unit/commands/test_admin_summon_command.py`
- **test_handle_summon_command_context_none()** (3 connections) — `server/tests/unit/commands/test_admin_summon_command.py`
- **test_handle_summon_command_parse_error()** (3 connections) — `server/tests/unit/commands/test_admin_summon_command.py`
- **test_handle_summon_command_success()** (3 connections) — `server/tests/unit/commands/test_admin_summon_command.py`
- **test_persist_summoned_item_success()** (3 connections) — `server/tests/unit/commands/test_admin_summon_command.py`
- **test_resolve_summon_context_permission_denied()** (3 connections) — `server/tests/unit/commands/test_admin_summon_command.py`
- *... and 26 more nodes in this community*

## Relationships

- [claude rules asyncio](claude_rules_asyncio.md) (12 shared connections)
- [iteminstance](iteminstance.md) (4 shared connections)
- [aliasrecord](aliasrecord.md) (3 shared connections)
- [server commands container helpers inventory](server_commands_container_helpers_inventory.md) (2 shared connections)
- [scripts populate test npc databases](scripts_populate_test_npc_databases.md) (2 shared connections)
- [server realtime envelope build event](server_realtime_envelope_build_event.md) (1 shared connections)
- [server commands alias commands](server_commands_alias_commands.md) (1 shared connections)
- [server alias storage aliasstorage](server_alias_storage_aliasstorage.md) (1 shared connections)
- [server commands admin commands](server_commands_admin_commands.md) (1 shared connections)
- [server commands admin permission utils](server_commands_admin_permission_utils.md) (1 shared connections)
- [server structured logging admin actions](server_structured_logging_admin_actions.md) (1 shared connections)
- [server api monitoring models](server_api_monitoring_models.md) (1 shared connections)

## Source Files

- `server/commands/admin_summon_command.py`
- `server/tests/unit/commands/test_admin_summon_command.py`

## Audit Trail

- EXTRACTED: 122 (95%)
- INFERRED: 6 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*