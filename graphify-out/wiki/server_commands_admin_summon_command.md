# server commands admin summon command

> 53 nodes

## Key Concepts

- **admin_summon_command.py** (35 connections) — `server/commands/admin_summon_command.py`
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
- *... and 28 more nodes in this community*

## Relationships

- [iteminstance](iteminstance.md) (6 shared connections)
- [claude rules sqlalchemy](claude_rules_sqlalchemy.md) (5 shared connections)
- [server commands inventory command helpers](server_commands_inventory_command_helpers.md) (4 shared connections)
- [server container main get container](server_container_main_get_container.md) (3 shared connections)
- [dropresolved](dropresolved.md) (3 shared connections)
- [server commands admin permission utils](server_commands_admin_permission_utils.md) (3 shared connections)
- [server structured logging admin actions](server_structured_logging_admin_actions.md) (3 shared connections)
- [server monitoring exception tracker](server_monitoring_exception_tracker.md) (3 shared connections)
- [server commands alias commands](server_commands_alias_commands.md) (2 shared connections)
- [server alias storage aliasstorage](server_alias_storage_aliasstorage.md) (2 shared connections)
- [server commands admin commands](server_commands_admin_commands.md) (2 shared connections)
- [claude rules asyncio](claude_rules_asyncio.md) (2 shared connections)

## Source Files

- `server/commands/admin_summon_command.py`
- `server/tests/unit/commands/test_admin_summon_command.py`

## Audit Trail

- EXTRACTED: 147 (97%)
- INFERRED: 5 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*